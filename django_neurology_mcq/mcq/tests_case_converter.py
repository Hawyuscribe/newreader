"""
Test suite for the Professional MCQ Case Converter
Comprehensive testing for all components of the conversion system
"""

import unittest
from unittest.mock import Mock, patch, MagicMock
import json
from datetime import datetime
from django.test import TestCase
from django.core.cache import cache

from .mcq_case_converter_professional import (
    MCQCaseConverter, MCQAnalyzer, CaseGenerator, CaseValidator,
    CacheManager, QuestionType, CaseComplexity, ValidationStatus,
    PatientDemographics, ClinicalPresentation, CaseData, ValidationResult
)
from .models import MCQ


class MockMCQ:
    """Mock MCQ object for testing"""
    def __init__(self, id=1, question_text="Test question", subspecialty="Neurology", correct_answer="A"):
        self.id = id
        self.question_text = question_text
        self.subspecialty = subspecialty
        self.correct_answer = correct_answer


class TestMCQAnalyzer(TestCase):
    """Test cases for MCQ analysis functionality"""
    
    def setUp(self):
        self.analyzer = MCQAnalyzer()
        self.mock_mcq = MockMCQ(
            id=1,
            question_text="A 65-year-old male presents with tremor and bradykinesia. What is the most likely diagnosis?",
            subspecialty="Movement Disorders",
            correct_answer="A"
        )
    
    def test_question_type_detection_diagnosis(self):
        """Test diagnosis question type detection"""
        question_type = self.analyzer._detect_question_type("What is the most likely diagnosis?")
        self.assertEqual(question_type, QuestionType.DIAGNOSIS)
    
    def test_question_type_detection_management(self):
        """Test management question type detection"""
        question_type = self.analyzer._detect_question_type("What is the next step in management?")
        self.assertEqual(question_type, QuestionType.MANAGEMENT)
    
    def test_question_type_detection_investigation(self):
        """Test investigation question type detection"""
        question_type = self.analyzer._detect_question_type("What is the best test to perform?")
        self.assertEqual(question_type, QuestionType.INVESTIGATION)
    
    def test_complexity_assessment_basic(self):
        """Test basic complexity assessment"""
        simple_mcq = MockMCQ(question_text="Simple question")
        complexity = self.analyzer._assess_complexity(simple_mcq)
        self.assertEqual(complexity, CaseComplexity.BASIC)
    
    def test_complexity_assessment_advanced(self):
        """Test advanced complexity assessment"""
        complex_mcq = MockMCQ(
            question_text="This is a very complex refractory case with multiple complications that is resistant to standard therapy and requires differential diagnosis considerations with extensive workup"
        )
        complexity = self.analyzer._assess_complexity(complex_mcq)
        self.assertEqual(complexity, CaseComplexity.ADVANCED)
    
    def test_patient_info_extraction_age(self):
        """Test patient age extraction"""
        patient_info = self.analyzer._extract_patient_info("A 65-year-old male presents with symptoms")
        self.assertEqual(patient_info.age, 65)
        self.assertEqual(patient_info.gender, "male")
    
    def test_patient_info_extraction_female(self):
        """Test female gender detection"""
        patient_info = self.analyzer._extract_patient_info("A 45-year-old woman presents with headache")
        self.assertEqual(patient_info.age, 45)
        self.assertEqual(patient_info.gender, "female")
    
    def test_analyze_mcq_complete(self):
        """Test complete MCQ analysis"""
        analysis = self.analyzer.analyze_mcq(self.mock_mcq)
        
        self.assertIn('question_type', analysis)
        self.assertIn('complexity', analysis)
        self.assertIn('patient_info', analysis)
        self.assertIn('clinical_context', analysis)
        self.assertIn('key_concepts', analysis)
        self.assertIn('specialty_confidence', analysis)
        
        self.assertEqual(analysis['question_type'], QuestionType.DIAGNOSIS)
        self.assertIsInstance(analysis['patient_info'], PatientDemographics)


class TestCaseGenerator(TestCase):
    """Test cases for case generation functionality"""
    
    def setUp(self):
        self.mock_client = Mock()
        self.generator = CaseGenerator(self.mock_client)
        self.mock_mcq = MockMCQ()
        self.sample_analysis = {
            'question_type': QuestionType.DIAGNOSIS,
            'complexity': CaseComplexity.INTERMEDIATE,
            'patient_info': PatientDemographics(age=65, gender="male"),
            'clinical_context': {'symptoms': ['tremor'], 'medications': [], 'procedures': [], 'findings': []},
            'key_concepts': ['movement disorders'],
            'specialty_confidence': 0.9
        }
    
    def test_create_generation_prompt(self):
        """Test prompt creation for case generation"""
        prompt = self.generator._create_generation_prompt(self.mock_mcq, self.sample_analysis)
        
        self.assertIn("MCQ (ID: 1)", prompt)
        self.assertIn("Question Type: diagnosis", prompt)
        self.assertIn("65-year-old male", prompt)
        self.assertIn("JSON", prompt)
    
    @patch('openai.OpenAI')
    def test_call_openai_api_success(self, mock_openai):
        """Test successful OpenAI API call"""
        mock_response = Mock()
        mock_response.choices[0].message.content = '{"test": "response"}'
        self.mock_client.chat.completions.create.return_value = mock_response
        
        result = self.generator._call_openai_api("test prompt")
        self.assertEqual(result, '{"test": "response"}')
    
    def test_parse_api_response_valid_json(self):
        """Test parsing valid API response"""
        sample_response = '''
        {
            "clinical_presentation": {
                "chief_complaint": "Tremor and stiffness",
                "history_present_illness": "65-year-old male with progressive tremor",
                "past_medical_history": ["Hypertension"],
                "medications": ["Lisinopril"],
                "physical_examination": "Resting tremor, bradykinesia",
                "vital_signs": {"bp": "140/90", "hr": "72"}
            },
            "question_prompt": "What is the most likely diagnosis?",
            "core_concept_type": "Movement disorders",
            "learning_objectives": ["Recognize Parkinson's disease", "Understand motor symptoms"]
        }
        '''
        
        case_data = self.generator._parse_api_response(self.mock_mcq, sample_response, self.sample_analysis)
        
        self.assertIsInstance(case_data, CaseData)
        self.assertEqual(case_data.source_mcq_id, 1)
        self.assertEqual(case_data.clinical_presentation.chief_complaint, "Tremor and stiffness")
        self.assertEqual(case_data.question_prompt, "What is the most likely diagnosis?")


class TestCaseValidator(TestCase):
    """Test cases for case validation functionality"""
    
    def setUp(self):
        self.mock_client = Mock()
        self.validator = CaseValidator(self.mock_client)
        self.mock_mcq = MockMCQ()
        
        self.sample_case_data = CaseData(
            source_mcq_id=1,
            specialty="Movement Disorders",
            question_type=QuestionType.DIAGNOSIS,
            complexity=CaseComplexity.INTERMEDIATE,
            patient_demographics=PatientDemographics(age=65, gender="male"),
            clinical_presentation=ClinicalPresentation(
                chief_complaint="Tremor and stiffness",
                history_of_present_illness="Patient presents with progressive tremor over 2 years",
                past_medical_history=["Hypertension"],
                medications=["Lisinopril"],
                physical_examination="Resting tremor, bradykinesia, cogwheel rigidity",
                vital_signs={"bp": "140/90", "hr": "72"}
            ),
            question_prompt="What is the most likely diagnosis?",
            core_concept_type="Movement disorders",
            learning_objectives=["Recognize Parkinson's disease"],
            metadata={"generated_at": datetime.now().isoformat()}
        )
    
    def test_validate_structure_valid_case(self):
        """Test structural validation with valid case"""
        issues = self.validator._validate_structure(self.sample_case_data)
        self.assertEqual(len(issues), 0)
    
    def test_validate_structure_missing_fields(self):
        """Test structural validation with missing fields"""
        invalid_case = CaseData(
            source_mcq_id=1,
            specialty="Neurology",
            question_type=QuestionType.DIAGNOSIS,
            complexity=CaseComplexity.BASIC,
            patient_demographics=PatientDemographics(age=45, gender="male"),
            clinical_presentation=ClinicalPresentation(
                chief_complaint="",  # Missing
                history_of_present_illness="",  # Missing
                past_medical_history=[],
                medications=[],
                physical_examination="Normal",
                vital_signs={}
            ),
            question_prompt="",  # Missing
            core_concept_type="",  # Missing
            learning_objectives=[],
            metadata={}
        )
        
        issues = self.validator._validate_structure(invalid_case)
        self.assertGreater(len(issues), 0)
        self.assertIn("Missing chief complaint", issues)
        self.assertIn("Missing history of present illness", issues)
    
    def test_validate_content_mcq_id_mismatch(self):
        """Test content validation with MCQ ID mismatch"""
        self.sample_case_data.source_mcq_id = 999  # Wrong ID
        issues = self.validator._validate_content(self.mock_mcq, self.sample_case_data)
        
        self.assertGreater(len(issues), 0)
        self.assertTrue(any("MCQ ID mismatch" in issue for issue in issues))
    
    def test_validate_content_specialty_mismatch(self):
        """Test content validation with specialty mismatch"""
        self.mock_mcq.subspecialty = "Epilepsy"
        self.sample_case_data.specialty = "Movement Disorders"
        
        issues = self.validator._validate_content(self.mock_mcq, self.sample_case_data)
        self.assertTrue(any("Specialty mismatch" in issue for issue in issues))
    
    def test_validation_score_calculation(self):
        """Test validation score calculation"""
        structural_issues = ["issue1"]
        content_issues = ["issue2", "issue3"]
        semantic_validation = {"score": 80, "issues": []}
        
        score = self.validator._calculate_validation_score(
            structural_issues, content_issues, semantic_validation
        )
        
        self.assertIsInstance(score, float)
        self.assertGreaterEqual(score, 0)
        self.assertLessEqual(score, 100)
    
    def test_validate_case_complete_success(self):
        """Test complete case validation with successful result"""
        with patch.object(self.validator, '_validate_semantics') as mock_semantic:
            mock_semantic.return_value = {"score": 85, "issues": [], "method": "ai"}
            
            result = self.validator.validate_case(self.mock_mcq, self.sample_case_data)
            
            self.assertIsInstance(result, ValidationResult)
            self.assertEqual(result.status, ValidationStatus.PASSED)
            self.assertGreater(result.score, 70)


class TestCacheManager(TestCase):
    """Test cases for cache management functionality"""
    
    def setUp(self):
        cache.clear()  # Clear cache before each test
    
    def tearDown(self):
        cache.clear()  # Clear cache after each test
    
    def test_cache_key_generation(self):
        """Test cache key generation"""
        key = CacheManager.get_cache_key(123)
        self.assertIn("mcq_case_conversion_123", key)
        self.assertIn("v2_professional", key)
    
    def test_cache_and_retrieve_conversion(self):
        """Test caching and retrieving conversion data"""
        test_data = {"test": "data", "mcq_id": 123}
        
        # Cache the data
        CacheManager.cache_conversion(123, test_data)
        
        # Retrieve the data
        cached_data = CacheManager.get_cached_conversion(123)
        
        self.assertIsNotNone(cached_data)
        self.assertEqual(cached_data['case_data'], test_data)
        self.assertIn('cached_at', cached_data)
    
    def test_clear_cache(self):
        """Test cache clearing"""
        test_data = {"test": "data"}
        
        # Cache the data
        CacheManager.cache_conversion(123, test_data)
        
        # Verify it's cached
        self.assertIsNotNone(CacheManager.get_cached_conversion(123))
        
        # Clear the cache
        CacheManager.clear_cache(123)
        
        # Verify it's cleared
        self.assertIsNone(CacheManager.get_cached_conversion(123))


class TestMCQCaseConverter(TestCase):
    """Test cases for the main converter class"""
    
    @patch('os.environ.get')
    @patch('openai.OpenAI')
    def setUp(self, mock_openai, mock_env):
        mock_env.return_value = 'test_api_key'
        self.mock_client = Mock()
        mock_openai.return_value = self.mock_client
        
        self.converter = MCQCaseConverter()
        self.mock_mcq = MockMCQ()
    
    def test_initialization_with_api_key(self):
        """Test converter initialization with API key"""
        self.assertIsNotNone(self.converter.openai_client)
        self.assertIsNotNone(self.converter.analyzer)
        self.assertIsNotNone(self.converter.generator)
        self.assertIsNotNone(self.converter.validator)
    
    @patch('os.environ.get')
    def test_initialization_without_api_key(self, mock_env):
        """Test converter initialization without API key"""
        mock_env.return_value = None
        
        converter = MCQCaseConverter()
        self.assertIsNone(converter.openai_client)
        self.assertIsNone(converter.generator)
    
    def test_convert_to_legacy_format(self):
        """Test conversion to legacy format"""
        sample_case_data = CaseData(
            source_mcq_id=1,
            specialty="Movement Disorders",
            question_type=QuestionType.DIAGNOSIS,
            complexity=CaseComplexity.INTERMEDIATE,
            patient_demographics=PatientDemographics(age=65, gender="male"),
            clinical_presentation=ClinicalPresentation(
                chief_complaint="Tremor",
                history_of_present_illness="Progressive tremor",
                past_medical_history=[],
                medications=[],
                physical_examination="Tremor present",
                vital_signs={}
            ),
            question_prompt="What is the diagnosis?",
            core_concept_type="Movement disorders",
            learning_objectives=[],
            metadata={"generated_at": datetime.now().isoformat()}
        )
        
        validation_result = ValidationResult(
            status=ValidationStatus.PASSED,
            score=85.0,
            reason="Good quality case",
            issues=[],
            metadata={}
        )
        
        legacy_format = self.converter._convert_to_legacy_format(sample_case_data, validation_result)
        
        # Check required legacy fields
        self.assertIn('source_mcq_id', legacy_format)
        self.assertIn('clinical_presentation', legacy_format)
        self.assertIn('patient_demographics', legacy_format)
        self.assertIn('question_prompt', legacy_format)
        self.assertIn('core_concept_type', legacy_format)
        self.assertIn('professional_validation', legacy_format)
        
        # Check validation metadata
        self.assertTrue(legacy_format['professional_validation']['passed'])
        self.assertEqual(legacy_format['professional_validation']['score'], 85.0)
    
    def test_get_conversion_stats(self):
        """Test conversion statistics retrieval"""
        stats = self.converter.get_conversion_stats()
        
        self.assertIn('cache_version', stats)
        self.assertIn('max_retry_attempts', stats)
        self.assertIn('openai_available', stats)
        self.assertIn('components_initialized', stats)
        
        self.assertTrue(stats['components_initialized']['analyzer'])
        self.assertTrue(stats['components_initialized']['validator'])
    
    @patch.object(CacheManager, 'get_cached_conversion')
    def test_convert_mcq_to_case_cached_result(self, mock_cache):
        """Test conversion with cached result"""
        cached_data = {'case_data': {'test': 'cached_case'}}
        mock_cache.return_value = cached_data
        
        result = self.converter.convert_mcq_to_case(self.mock_mcq)
        
        self.assertEqual(result, cached_data['case_data'])
        mock_cache.assert_called_once_with(self.mock_mcq.id)


class TestIntegrationMCQCaseConverter(TestCase):
    """Integration tests for the complete conversion pipeline"""
    
    def setUp(self):
        cache.clear()
    
    def tearDown(self):
        cache.clear()
    
    @patch('os.environ.get')
    @patch('openai.OpenAI')
    def test_end_to_end_conversion_success(self, mock_openai_class, mock_env):
        """Test complete end-to-end conversion process"""
        # Setup mocks
        mock_env.return_value = 'test_api_key'
        mock_client = Mock()
        mock_openai_class.return_value = mock_client
        
        # Mock OpenAI responses
        generation_response = Mock()
        generation_response.choices[0].message.content = '''
        {
            "clinical_presentation": {
                "chief_complaint": "Progressive tremor and stiffness",
                "history_present_illness": "65-year-old male presents with 2-year history of progressive tremor",
                "past_medical_history": ["Hypertension"],
                "medications": ["Lisinopril"],
                "physical_examination": "Resting tremor, bradykinesia, cogwheel rigidity",
                "vital_signs": {"bp": "140/90", "hr": "72"}
            },
            "question_prompt": "What is the most likely diagnosis?",
            "core_concept_type": "Movement disorders - Parkinson's disease",
            "learning_objectives": ["Recognize Parkinson's disease symptoms", "Understand motor features"]
        }
        '''
        
        validation_response = Mock()
        validation_response.choices[0].message.content = '{"score": 90, "issues": [], "explanation": "Excellent alignment"}'
        
        mock_client.chat.completions.create.side_effect = [generation_response, validation_response]
        
        # Create test MCQ
        test_mcq = MockMCQ(
            id=1,
            question_text="A 65-year-old male presents with resting tremor and bradykinesia. What is the most likely diagnosis?",
            subspecialty="Movement Disorders",
            correct_answer="A"
        )
        
        # Perform conversion
        converter = MCQCaseConverter()
        result = converter.convert_mcq_to_case(test_mcq)
        
        # Verify result structure
        self.assertIsInstance(result, dict)
        self.assertIn('source_mcq_id', result)
        self.assertIn('clinical_presentation', result)
        self.assertIn('professional_validation', result)
        
        # Verify validation passed
        self.assertTrue(result['professional_validation']['passed'])
        self.assertGreaterEqual(result['professional_validation']['score'], 70)
        
        # Verify MCQ consistency
        self.assertEqual(result['source_mcq_id'], test_mcq.id)
    
    def test_conversion_without_openai_client(self):
        """Test conversion failure without OpenAI client"""
        converter = MCQCaseConverter()
        converter.openai_client = None
        converter.generator = None
        
        test_mcq = MockMCQ()
        
        with self.assertRaises(Exception) as context:
            converter.convert_mcq_to_case(test_mcq)
        
        self.assertIn("OpenAI client not available", str(context.exception))


class TestBackwardCompatibility(TestCase):
    """Test backward compatibility with existing system"""
    
    @patch('mcq.mcq_case_converter_professional.MCQCaseConverter')
    def test_convert_mcq_to_case_function(self, mock_converter_class):
        """Test the backward compatible function interface"""
        from .mcq_case_converter_professional import convert_mcq_to_case
        
        mock_converter = Mock()
        mock_converter.convert_mcq_to_case.return_value = {"test": "result"}
        mock_converter_class.return_value = mock_converter
        
        test_mcq = MockMCQ()
        result = convert_mcq_to_case(test_mcq)
        
        self.assertEqual(result, {"test": "result"})
        mock_converter.convert_mcq_to_case.assert_called_once_with(test_mcq)
    
    def test_cache_functions_compatibility(self):
        """Test backward compatible cache functions"""
        from .mcq_case_converter_professional import get_mcq_cache_key, clear_mcq_cache
        
        # Test cache key function
        key = get_mcq_cache_key(123)
        self.assertIsInstance(key, str)
        self.assertIn("123", key)
        
        # Test clear cache function (should not raise exception)
        clear_mcq_cache(123)


if __name__ == '__main__':
    unittest.main()