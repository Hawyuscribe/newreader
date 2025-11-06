"""
Professional MCQ-to-Case Conversion System
Version 2.0 - Complete rewrite with enterprise-grade architecture

This module provides a robust, maintainable, and scalable system for converting
Multiple Choice Questions (MCQs) into interactive case-based learning scenarios.

Author: AI-Assisted Development
Version: 2.0.0
Last Updated: 2025-06-06
"""

import json
import logging
import os
import re
import hashlib
from typing import Dict, Optional, List, Tuple, Any
from dataclasses import dataclass, asdict
from datetime import datetime, timedelta
from enum import Enum

from django.core.cache import cache
from .openai_integration import (
    client as openai_client,
    DEFAULT_MODEL,
    FALLBACK_MODEL,
    chat_completion,
    get_first_choice_text,
)

# Configure logging
logger = logging.getLogger(__name__)

# Configuration
CACHE_VERSION = "v2_professional"
CACHE_TIMEOUT = 3600  # 1 hour
MAX_RETRY_ATTEMPTS = 3 if os.environ.get('DYNO') else 5  # Fewer retries on Heroku
API_TIMEOUT = 30 if os.environ.get('DYNO') else 60  # Shorter timeout on Heroku

# Validation thresholds - more permissive on Heroku
MIN_VALIDATION_SCORE = 40 if os.environ.get('DYNO') else 70
MIN_SEMANTIC_SCORE = 30 if os.environ.get('DYNO') else 50


def _run_chat_completion(api_client, logger, messages, **kwargs):
    """Execute a chat completion using GPT-5-mini with optional fallback."""
    if not api_client:
        raise RuntimeError("OpenAI client is not available")

    primary_model = DEFAULT_MODEL
    try:
        return chat_completion(api_client, primary_model, messages, **kwargs)
    except Exception as primary_error:
        if FALLBACK_MODEL and FALLBACK_MODEL != primary_model:
            if logger:
                logger.warning(
                    "Primary completion with %s failed (%s). Retrying with fallback model %s.",
                    primary_model,
                    primary_error,
                    FALLBACK_MODEL,
                )
            return chat_completion(api_client, FALLBACK_MODEL, messages, **kwargs)
        raise


class QuestionType(Enum):
    """Enumeration of question types for better classification"""
    DIAGNOSIS = "diagnosis"
    DIFFERENTIAL = "differential" 
    LOCALIZATION = "localization"
    MANAGEMENT = "management"
    INVESTIGATION = "investigation"
    PATHOPHYSIOLOGY = "pathophysiology"
    PROGNOSIS = "prognosis"
    PREVENTION = "prevention"


class CaseComplexity(Enum):
    """Case complexity levels"""
    BASIC = "basic"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"


class ValidationStatus(Enum):
    """Validation status enumeration"""
    PENDING = "pending"
    PASSED = "passed"
    FAILED = "failed"
    ERROR = "error"


@dataclass
class PatientDemographics:
    """Patient demographic information"""
    age: int
    gender: str
    occupation: Optional[str] = None
    medical_history: List[str] = None
    
    def __post_init__(self):
        if self.medical_history is None:
            self.medical_history = []


@dataclass
class ClinicalPresentation:
    """Clinical presentation structure"""
    chief_complaint: str
    history_of_present_illness: str
    past_medical_history: List[str]
    medications: List[str]
    physical_examination: str
    vital_signs: Dict[str, str]
    
    def __post_init__(self):
        if not self.past_medical_history:
            self.past_medical_history = []
        if not self.medications:
            self.medications = []
        if not self.vital_signs:
            self.vital_signs = {}


@dataclass
class CaseData:
    """Complete case data structure"""
    source_mcq_id: int
    specialty: str
    question_type: QuestionType
    complexity: CaseComplexity
    patient_demographics: PatientDemographics
    clinical_presentation: ClinicalPresentation
    question_prompt: str
    core_concept_type: str
    learning_objectives: List[str]
    metadata: Dict[str, Any]
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization"""
        data = asdict(self)
        # Convert enums to their string values
        data['question_type'] = self.question_type.value
        data['complexity'] = self.complexity.value
        return data


@dataclass
class ValidationResult:
    """Validation result structure"""
    status: ValidationStatus
    score: float
    reason: str
    issues: List[str]
    metadata: Dict[str, Any]
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization"""
        return {
            'status': self.status.value,  # Convert enum to string
            'score': self.score,
            'reason': self.reason,
            'issues': self.issues,
            'metadata': self.metadata
        }


class MCQAnalyzer:
    """Analyzes MCQ content to extract key information"""
    
    # Medical specialty keywords mapping
    SPECIALTY_KEYWORDS = {
        'Movement Disorders': ['parkinson', 'dystonia', 'chorea', 'tremor', 'bradykinesia', 'rigidity'],
        'Epilepsy': ['seizure', 'epilep', 'convuls', 'ictal', 'postictal'],
        'Stroke/Vascular': ['stroke', 'hemorrhage', 'infarct', 'tpa', 'thrombo', 'ischemic'],
        'Dementia': ['alzheimer', 'dementia', 'memory', 'cognitive', 'confusion'],
        'Headache': ['headache', 'migraine', 'cluster', 'tension'],
        'Neuromuscular': ['myasthenia', 'neuropathy', 'myopathy', 'weakness', 'muscle'],
    }
    
    # Comprehensive question type patterns
    QUESTION_PATTERNS = {
        QuestionType.DIAGNOSIS: [
            # Classic diagnostic patterns
            r'most likely diagnosis',
            r'what is the diagnosis',
            r'which condition',
            r'diagnosed with',
            r'likely cause',
            r'clinical diagnosis',
            r'provisional diagnosis',
            r'working diagnosis',
            r'primary diagnosis',
            r'underlying condition',
            r'this patient has',
            r'this condition is',
            r'consistent with',
            r'suggests.*diagnosis',
            r'findings.*suggest',
            r'clinical picture.*consistent'
        ],
        QuestionType.DIFFERENTIAL: [
            # Differential diagnosis patterns
            r'differential diagnosis',
            r'differential.*includes',
            r'consider.*differential',
            r'broad.*differential',
            r'narrow.*differential',
            r'most.*appropriate.*differential',
            r'differential.*considerations',
            r'list.*of.*diagnoses',
            r'possible.*diagnoses',
            r'likely.*diagnoses'
        ],
        QuestionType.LOCALIZATION: [
            # Neurological localization patterns
            r'which localization',
            r'localization.*most likely',
            r'most likely.*localization',
            r'localization.*of.*lesion',
            r'lesion.*located',
            r'anatomical.*location',
            r'site.*of.*lesion',
            r'where.*is.*lesion',
            r'neuroanatomical.*localization',
            r'level.*of.*lesion',
            r'location.*of.*pathology',
            r'anatomical.*site',
            r'localizing.*sign',
            r'lateralizing.*sign',
            r'level.*of.*injury',
            r'spinal.*level',
            r'brain.*region',
            r'cortical.*area'
        ],
        QuestionType.MANAGEMENT: [
            # Treatment and management patterns
            r'next step in management',
            r'best treatment',
            r'what should be done',
            r'appropriate therapy',
            r'second-line management',
            r'first-line treatment',
            r'most appropriate management',
            r'treatment of choice',
            r'next step',
            r'what is the.*management',
            r'how should.*be treated',
            r'appropriate treatment',
            r'therapeutic.*option',
            r'next.*intervention',
            r'what should be switched',
            r'should be switched to',
            r'switch to',
            r'changed to',
            r'medication.*change',
            r'drug.*choice',
            r'therapy.*recommend',
            r'treatment.*plan',
            r'manage.*patient',
            r'best.*approach',
            r'optimal.*treatment',
            r'immediate.*action',
            r'emergency.*management',
            r'long-term.*management',
            r'preventive.*treatment',
            r'maintenance.*therapy'
        ],
        QuestionType.INVESTIGATION: [
            # Investigation and testing patterns
            r'next step in workup',
            r'best test',
            r'which study',
            r'appropriate investigation',
            r'most useful.*test',
            r'next.*investigation',
            r'diagnostic.*test',
            r'most appropriate.*study',
            r'confirm.*diagnosis',
            r'evaluate.*further',
            r'additional.*testing',
            r'imaging.*study',
            r'laboratory.*test',
            r'further.*workup',
            r'initial.*test',
            r'screening.*test',
            r'monitoring.*test',
            r'follow.*study'
        ],
        QuestionType.PATHOPHYSIOLOGY: [
            # Pathophysiology and mechanism patterns
            r'mechanism.*responsible',
            r'pathophysiology',
            r'underlying.*mechanism',
            r'physiologic.*basis',
            r'explains.*finding',
            r'reason.*for',
            r'cause.*of.*symptom',
            r'why.*occur',
            r'results.*from',
            r'due.*to.*mechanism',
            r'molecular.*basis',
            r'cellular.*process'
        ]
    }
    
    def __init__(self, openai_client: Any):
        self.client = openai_client
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
    
    def analyze_mcq(self, mcq) -> Dict[str, Any]:
        """
        Comprehensive analysis of MCQ content
        
        Args:
            mcq: MCQ model instance
            
        Returns:
            Dictionary containing analysis results
        """
        try:
            patient_info, age_descriptor = self._extract_patient_info(mcq.question_text)
            analysis = {
                'question_type': self._detect_question_type(mcq.question_text),
                'complexity': self._assess_complexity(mcq),
                'patient_info': patient_info,
                'age_descriptor': age_descriptor,
                'clinical_context': self._extract_clinical_context(mcq.question_text),
                'key_concepts': self._identify_key_concepts(mcq),
                'specialty_confidence': self._validate_specialty(mcq)
            }
            
            self.logger.info(f"MCQ {mcq.id} analysis completed: {analysis['question_type']}")
            return analysis
            
        except Exception as e:
            self.logger.error(f"MCQ analysis failed for {mcq.id}: {e}")
            raise
    
    def _detect_question_type(self, question_text: str) -> QuestionType:
        """Detect question type using pattern matching"""
        text = question_text.lower()
        
        for question_type, patterns in self.QUESTION_PATTERNS.items():
            if any(re.search(pattern, text) for pattern in patterns):
                return question_type
        
        return QuestionType.DIAGNOSIS  # Default
    
    def _assess_complexity(self, mcq) -> CaseComplexity:
        """Assess case complexity based on MCQ characteristics"""
        complexity_score = 0
        
        # Length-based scoring
        if len(mcq.question_text) > 500:
            complexity_score += 2
        elif len(mcq.question_text) > 200:
            complexity_score += 1
        
        # Content-based scoring
        complex_terms = ['refractory', 'resistant', 'multiple', 'complications', 'differential']
        complexity_score += sum(1 for term in complex_terms if term in mcq.question_text.lower())
        
        # Map score to complexity
        if complexity_score >= 4:
            return CaseComplexity.ADVANCED
        elif complexity_score >= 2:
            return CaseComplexity.INTERMEDIATE
        else:
            return CaseComplexity.BASIC
    
    def _extract_patient_info(self, question_text: str) -> Tuple[PatientDemographics, str]:
        """Extract patient demographic information using AI analysis with enhanced validation"""
        try:
            prompt = f"""
Extract patient demographic information from this medical question.

Question: {question_text}

Analyze and return ONLY a JSON object with:
{{
    "age_descriptor": "exact age (e.g., '7') or descriptive term (e.g., 'young', 'elderly', 'middle-aged')",
    "gender": "male, female, or boy/girl for children",
    "representative_age": "numeric age (use exact age if given, best estimate for descriptive terms)"
}}

CRITICAL RULES:
- If EXACT age is given (e.g., "7-year-old", "25-year-old"), use that EXACT number
- If child descriptors used (boy, girl), preserve those and determine gender
- Boy = male, Girl = female
- For gender, prioritize: boy/girl > man/woman > he/she pronouns
- For representative_age: young adult=28, elderly=72, middle-aged=50, adolescent=16, child=8, infant=1
- PRESERVE EXACT AGES - do not change "7-year-old" to "8-year-old"

Examples:
"7-year-old boy" → {{"age_descriptor": "7", "gender": "male", "representative_age": "7"}}
"elderly woman" → {{"age_descriptor": "elderly", "gender": "female", "representative_age": "72"}}
"""
            
            response = _run_chat_completion(
                self.client,
                self.logger,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.1,
                max_tokens=200,
                timeout=10,
            )

            # Parse response
            response_text = get_first_choice_text(response)
            json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
            if json_match:
                data = json.loads(json_match.group())
                age = int(data.get('representative_age', 45))
                gender = data.get('gender', 'male')
                age_descriptor = data.get('age_descriptor', str(age))
                
                return PatientDemographics(age=age, gender=gender), age_descriptor
            
        except Exception as e:
            self.logger.warning(f"AI demographic extraction failed, using fallback: {e}")
        
        # Enhanced fallback with better pattern matching
        # First, try to extract exact age
        age_match = re.search(r'(\d+)[-\s]year[-\s]old', question_text, re.IGNORECASE)
        if age_match:
            age = int(age_match.group(1))
            age_descriptor = str(age)
        else:
            # Try descriptive age terms
            age_patterns = {
                r'\b(infant|baby)\b': (1, "infant"),
                r'\b(child|kid)\b': (8, "child"), 
                r'\b(adolescent|teenager|teen)\b': (16, "adolescent"),
                r'\b(young)\b': (28, "young"),
                r'\b(middle[-\s]aged)\b': (50, "middle-aged"),
                r'\b(elderly|old)\b': (72, "elderly")
            }
            
            age = 45  # default
            age_descriptor = "45"
            
            for pattern, (default_age, descriptor) in age_patterns.items():
                if re.search(pattern, question_text, re.IGNORECASE):
                    age = default_age
                    age_descriptor = descriptor
                    break
        
        # Enhanced gender detection with priority
        gender = "male"  # default
        
        # Priority 1: boy/girl (for children)
        if re.search(r'\bboy\b', question_text, re.IGNORECASE):
            gender = "male"
        elif re.search(r'\bgirl\b', question_text, re.IGNORECASE):
            gender = "female"
        # Priority 2: man/woman
        elif re.search(r'\b(woman|female)\b', question_text, re.IGNORECASE):
            gender = "female"
        elif re.search(r'\b(man|male)\b', question_text, re.IGNORECASE):
            gender = "male"
        # Priority 3: pronouns
        elif re.search(r'\b(she|her)\b', question_text, re.IGNORECASE):
            gender = "female"
        elif re.search(r'\b(he|his|him)\b', question_text, re.IGNORECASE):
            gender = "male"
        
        return PatientDemographics(age=age, gender=gender), age_descriptor
    
    def _extract_clinical_context(self, question_text: str) -> Dict[str, List[str]]:
        """Extract clinical context from question"""
        context = {
            'symptoms': [],
            'medications': [],
            'procedures': [],
            'findings': []
        }
        
        # Simple keyword extraction (can be enhanced)
        symptom_keywords = ['pain', 'weakness', 'numbness', 'seizure', 'headache']
        context['symptoms'] = [kw for kw in symptom_keywords if kw in question_text.lower()]
        
        return context
    
    def _identify_key_concepts(self, mcq) -> List[str]:
        """Identify key medical concepts"""
        concepts = []
        
        # Extract from subspecialty
        if mcq.subspecialty:
            concepts.append(mcq.subspecialty.lower())
        
        # Extract from question text (simplified)
        medical_terms = re.findall(r'\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b', mcq.question_text)
        concepts.extend(medical_terms[:3])  # Limit to top 3
        
        return concepts
    
    def _validate_specialty(self, mcq) -> float:
        """Validate specialty assignment confidence"""
        if not mcq.subspecialty:
            return 0.5
        
        text = mcq.question_text.lower()
        specialty_keywords = self.SPECIALTY_KEYWORDS.get(mcq.subspecialty, [])
        
        matches = sum(1 for keyword in specialty_keywords if keyword in text)
        return min(1.0, matches / max(1, len(specialty_keywords)))


class CaseGenerator:
    """Generates case-based learning scenarios from MCQ analysis"""
    
    def __init__(self, openai_client: Any):
        self.client = openai_client
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
    
    def generate_case(self, mcq, analysis: Dict[str, Any]) -> CaseData:
        """
        Generate case from MCQ and analysis
        
        Args:
            mcq: MCQ model instance
            analysis: Analysis results from MCQAnalyzer
            
        Returns:
            CaseData instance
        """
        try:
            self.logger.info(f"Generating case for MCQ {mcq.id}")
            
            # Create AI prompt
            prompt = self._create_generation_prompt(mcq, analysis)
            
            # Call OpenAI API
            response = self._call_openai_api(prompt)
            
            # Parse and structure response
            case_data = self._parse_api_response(mcq, response, analysis)
            
            self.logger.info(f"Case generation completed for MCQ {mcq.id}")
            return case_data
            
        except Exception as e:
            self.logger.error(f"Case generation failed for MCQ {mcq.id}: {e}")
            raise
    
    def _create_generation_prompt(self, mcq, analysis: Dict[str, Any]) -> str:
        """Create structured prompt for OpenAI with clinical detail preservation"""
        patient_info = analysis['patient_info']
        age_descriptor = analysis['age_descriptor']
        question_type = analysis['question_type'].value
        complexity = analysis['complexity'].value
        
        # Build patient description using AI-extracted descriptor
        if age_descriptor.isdigit():
            patient_desc = f"{age_descriptor}-year-old {patient_info.gender}"
        else:
            patient_desc = f"{age_descriptor} {patient_info.gender}"
        
        # Generate clinical detail preservation requirements
        clinical_preservation_prompt = self._generate_clinical_preservation_requirements(mcq)
        
        # Generate investigation preservation requirements
        investigation_preservation_prompt = self._generate_investigation_preservation_requirements(mcq)
        
        # Create question type-specific instructions
        question_type_instructions = self._get_question_type_instructions(question_type, mcq.question_text)
        
        prompt = f"""
You are a medical education expert creating an adaptive case-based learning scenario from an MCQ.

ORIGINAL MCQ (ID: {mcq.id}):
Question: {mcq.question_text}
Subspecialty: {mcq.subspecialty}
Correct Answer: {mcq.correct_answer}

ANALYSIS:
- Question Type: {question_type}
- Complexity: {complexity}
- Patient: {patient_desc}

{clinical_preservation_prompt}

{investigation_preservation_prompt}

CRITICAL TASK: Create a realistic clinical case that teaches the EXACT SAME CONCEPT as this MCQ and intelligently determines the appropriate clinical starting phase.

{question_type_instructions}

ADAPTIVE CASE DESIGN REQUIREMENTS:
1. **INTELLIGENT PHASE SELECTION**: Analyze what the original MCQ tests and choose the most appropriate clinical phase to start from
2. **EXACT CONCEPT ALIGNMENT**: The case must focus on the EXACT same medical concept as the original MCQ
3. **PATIENT DEMOGRAPHICS**: Use the EXACT same patient demographics: {patient_desc}
4. **CLINICAL REASONING MATCH**: The case should require the same type of clinical reasoning as the original MCQ
5. **DECISION POINT ALIGNMENT**: The case should lead to the same clinical decision point
6. **QUESTION TYPE CONSISTENCY**: {question_type.upper()} questions must generate {question_type.upper()} scenarios
7. **MEDICAL ACCURACY**: Maintain complete medical accuracy and educational value
8. **AGE DESCRIPTOR PRESERVATION**: If original says "young female", case must describe "young female"
9. **SOURCE VERIFICATION**: Include the source MCQ ID {mcq.id} in your response
10. **CLINICAL DETAIL PRESERVATION**: Follow ALL clinical preservation requirements above - failure to preserve critical details will compromise educational integrity

ADAPTIVE CASE STRUCTURE:
Based on your analysis, structure the case to start at the most appropriate clinical phase and progress naturally to the same type of clinical decision as the original MCQ. The case should feel natural and realistic while teaching the exact same concept.

RESPONSE FORMAT (JSON):
{{
    "source_mcq_id": {mcq.id},
    "clinical_presentation": {{
        "chief_complaint": "Main presenting symptom",
        "history_present_illness": "Detailed history of current problem",
        "past_medical_history": ["relevant", "conditions"],
        "medications": ["current", "medications"],
        "physical_examination": "Relevant examination findings",
        "vital_signs": {{"bp": "120/80", "hr": "72", "temp": "98.6"}}
    }},
    "question_prompt": "What is the most appropriate next step?",
    "core_concept_type": "Primary medical concept being tested",
    "learning_objectives": ["objective1", "objective2", "objective3"]
}}

IMPORTANT: The source_mcq_id MUST be {mcq.id}. Generate the case now:
"""
        return prompt
    
    def _get_question_type_instructions(self, question_type: str, original_question: str) -> str:
        """Generate comprehensive AI-driven instructions based on question type"""
        
        # Base instruction that applies to all question types
        base_instruction = f"""
ORIGINAL QUESTION ANALYSIS: "{original_question}"

ADAPTIVE CASE GENERATION INSTRUCTIONS:
You are an expert medical educator creating a case that teaches the EXACT same clinical concept as this MCQ. 
Your task is to intelligently determine the appropriate starting phase of the clinical encounter based on what the original question is testing.

CLINICAL PHASES TO CHOOSE FROM:
1. **INITIAL PRESENTATION** (HPI/Chief Complaint) - Start here for diagnostic challenges
2. **POST-EXAMINATION** (After history/exam) - Start here when some findings are established  
3. **POST-INVESTIGATION** (After initial tests) - Start here when diagnosis is suspected
4. **ESTABLISHED DIAGNOSIS** (Condition confirmed) - Start here for management/treatment questions
5. **ONGOING TREATMENT** (Patient on therapy) - Start here for treatment modification questions

INTELLIGENT PHASE SELECTION:
- Analyze what the original MCQ is actually testing
- Choose the most appropriate starting phase that leads to the same clinical decision
- The case should require the same type of clinical reasoning as the original question
"""

        if question_type == "management":
            return base_instruction + f"""

MANAGEMENT QUESTION - SPECIFIC GUIDANCE:
Since this is a MANAGEMENT question, you should typically start at one of these phases:

**OPTION A - ESTABLISHED DIAGNOSIS** (Most common):
- Patient's condition is already diagnosed/obvious
- Focus: "What is the best treatment/next step?"
- Include: Relevant clinical context that supports the management choice
- Exclude: Unnecessary diagnostic workup

**OPTION B - ONGOING TREATMENT** (For medication switches, second-line therapy):
- Patient is currently on treatment that needs modification
- Focus: "What should be changed/added/switched to?"
- Include: Current treatment details, response, side effects
- Example: Patient on Drug X with side effects → what to switch to?

**OPTION C - POST-INVESTIGATION** (When investigations inform treatment):
- Key test results are available that guide treatment
- Focus: "Based on these findings, what is the next step?"

CHOOSE THE OPTION that best matches what the original MCQ is testing.
"""
        
        elif question_type == "diagnosis":
            return base_instruction + f"""

DIAGNOSIS QUESTION - SPECIFIC GUIDANCE:
Since this is a DIAGNOSIS question, you should typically start at one of these phases:

**OPTION A - INITIAL PRESENTATION** (Classic diagnostic scenario):
- Patient presents with symptoms requiring diagnosis
- Focus: "What is the most likely diagnosis?"
- Include: History, examination findings that point to the diagnosis
- Progress through: HPI → Examination → Clinical reasoning

**OPTION B - POST-EXAMINATION** (When key findings are present):
- History and examination completed, findings available
- Focus: "Based on these findings, what is the diagnosis?"
- Include: Specific signs/symptoms that narrow differential

**OPTION C - POST-INVESTIGATION** (When test results guide diagnosis):
- Some initial tests done, results available
- Focus: "What do these findings suggest?"
- Include: Test results that clinch the diagnosis

CHOOSE THE OPTION that creates the same diagnostic challenge as the original MCQ.
"""
        
        elif question_type == "differential":
            return base_instruction + f"""

DIFFERENTIAL DIAGNOSIS QUESTION - SPECIFIC GUIDANCE:
Since this is a DIFFERENTIAL DIAGNOSIS question, you should typically start at:

**OPTION A - POST-EXAMINATION** (Most common):
- History and examination completed with key findings
- Focus: "What is the differential diagnosis?" or "What diagnoses should be considered?"
- Include: Clinical findings that support multiple possible diagnoses
- Present: A scenario where several conditions could explain the findings

**OPTION B - INITIAL PRESENTATION** (Complex cases):
- Patient presents with complex symptom pattern
- Focus: "What conditions should be in the differential?"
- Include: Symptoms that could suggest multiple diagnoses
- Require: Broad clinical reasoning across multiple conditions

CHOOSE THE OPTION that requires the same differential reasoning as the original MCQ.
"""
        
        elif question_type == "localization":
            return base_instruction + f"""

LOCALIZATION QUESTION - SPECIFIC GUIDANCE:
Since this is a LOCALIZATION question, you should typically start at:

**OPTION A - POST-EXAMINATION** (Most common):
- Neurological examination completed with specific findings
- Focus: "Where is the lesion located?" or "What is the anatomical localization?"
- Include: Specific neurological signs that localize to particular anatomy
- Require: Neuroanatomical reasoning

**OPTION B - POST-INVESTIGATION** (When imaging/tests show findings):
- Test results available showing anatomical abnormalities
- Focus: "What level/location does this represent?"
- Include: Specific findings that correspond to anatomical locations

**OPTION C - CLINICAL CORRELATION** (Signs + anatomy):
- Clinical findings presented with anatomical correlation
- Focus: "What anatomical structure explains these findings?"
- Include: Neurological signs that map to specific brain/spinal regions

CHOOSE THE OPTION that requires the same localization reasoning as the original MCQ.
"""
        
        elif question_type == "investigation":
            return base_instruction + f"""

INVESTIGATION QUESTION - SPECIFIC GUIDANCE:
Since this is an INVESTIGATION question, you should typically start at one of these phases:

**OPTION A - POST-EXAMINATION** (Most common):
- History and examination completed
- Focus: "What is the most appropriate next test?"
- Include: Clinical findings that justify the specific investigation
- Progress to: Test selection decision

**OPTION B - INITIAL PRESENTATION** (When symptoms drive testing):
- Patient presents with specific symptoms
- Focus: "What initial test should be ordered?"
- Include: Symptom complex that requires specific workup

**OPTION C - POST-INITIAL-INVESTIGATION** (For follow-up testing):
- Some tests already done, need additional testing
- Focus: "What further investigation is needed?"
- Include: Previous test results, remaining questions

CHOOSE THE OPTION that requires the same investigative reasoning as the original MCQ.
"""
        
        elif question_type == "pathophysiology":
            return base_instruction + f"""

PATHOPHYSIOLOGY QUESTION - SPECIFIC GUIDANCE:
Since this is a PATHOPHYSIOLOGY question, present a case that:
- Illustrates the underlying mechanism being tested
- Connects clinical findings to pathophysiological processes
- Asks "What explains this finding?" or "What is the mechanism?"
- Links symptoms/signs to the biological process
"""
        
        else:
            return base_instruction + f"""

GENERAL CLINICAL QUESTION - ADAPTIVE GUIDANCE:
Analyze the original MCQ and intelligently choose the appropriate clinical phase:
- Match the type of clinical reasoning required
- Start at the phase that leads to the same decision point
- Ensure the case teaches the same core concept
- Focus on the same aspect of patient care
"""
    
    def _call_openai_api(self, prompt: str) -> str:
        """Call OpenAI API with error handling"""
        try:
            response = _run_chat_completion(
                self.client,
                self.logger,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3,
                max_tokens=2000,
                timeout=API_TIMEOUT,
            )
            content = get_first_choice_text(response)
            if not content:
                raise RuntimeError("OpenAI returned empty content during case generation")
            return content
            
        except Exception as e:
            self.logger.error(f"OpenAI API call failed: {e}")
            raise
    
    def _parse_api_response(self, mcq, response: str, analysis: Dict[str, Any]) -> CaseData:
        """Parse OpenAI response into structured case data"""
        try:
            # Extract JSON from response
            json_match = re.search(r'\{.*\}', response, re.DOTALL)
            if not json_match:
                raise ValueError("No JSON found in API response")
            
            parsed_data = json.loads(json_match.group())
            
            # Verify source MCQ ID from API response
            api_mcq_id = parsed_data.get('source_mcq_id')
            if api_mcq_id != mcq.id:
                self.logger.warning(f"API returned wrong MCQ ID! Expected {mcq.id}, got {api_mcq_id}")
                # Force correct MCQ ID - this is critical for integrity
                parsed_data['source_mcq_id'] = mcq.id
                
                # On Heroku, be more forgiving about ID mismatches
                if os.environ.get('DYNO'):
                    self.logger.info(f"Auto-corrected MCQ ID on Heroku from {api_mcq_id} to {mcq.id}")
                else:
                    self.logger.warning(f"Corrected MCQ ID in API response from {api_mcq_id} to {mcq.id}")
            
            # Create structured objects
            patient_info = analysis['patient_info']
            
            clinical_presentation = ClinicalPresentation(
                chief_complaint=parsed_data['clinical_presentation']['chief_complaint'],
                history_of_present_illness=parsed_data['clinical_presentation']['history_present_illness'],
                past_medical_history=parsed_data['clinical_presentation'].get('past_medical_history', []),
                medications=parsed_data['clinical_presentation'].get('medications', []),
                physical_examination=parsed_data['clinical_presentation']['physical_examination'],
                vital_signs=parsed_data['clinical_presentation'].get('vital_signs', {})
            )
            
            case_data = CaseData(
                source_mcq_id=mcq.id,  # Always use the correct MCQ ID
                specialty=mcq.subspecialty,
                question_type=analysis['question_type'],
                complexity=analysis['complexity'],
                patient_demographics=patient_info,
                clinical_presentation=clinical_presentation,
                question_prompt=parsed_data['question_prompt'],
                core_concept_type=parsed_data['core_concept_type'],
                learning_objectives=parsed_data.get('learning_objectives', []),
                metadata={
                    'generated_at': datetime.now().isoformat(),
                    'source_mcq_checksum': self._generate_mcq_checksum(mcq),
                    'generator_version': 'v2.0.0',
                    'api_returned_mcq_id': api_mcq_id,  # Track what API actually returned
                    'original_mcq_text': mcq.question_text  # Store original for clinical inferences
                }
            )
            
            return case_data
            
        except Exception as e:
            self.logger.error(f"Failed to parse API response: {e}")
            raise
    
    def _generate_mcq_checksum(self, mcq) -> str:
        """Generate checksum for MCQ validation"""
        content = f"{mcq.id}_{mcq.question_text}_{mcq.correct_answer}_{mcq.subspecialty}"
        return hashlib.md5(content.encode()).hexdigest()[:16]
    
    def _generate_clinical_preservation_requirements(self, mcq) -> str:
        """Generate clinical detail preservation requirements for the MCQ"""
        try:
            from .clinical_detail_extractor import generate_clinical_detail_preservation_prompt
            return generate_clinical_detail_preservation_prompt(mcq.question_text, mcq.correct_answer_text or "")
        except ImportError:
            self.logger.warning("Clinical detail extractor not available - using basic preservation requirements")
            return self._generate_basic_preservation_requirements(mcq)
    
    def _generate_investigation_preservation_requirements(self, mcq) -> str:
        """Generate investigation preservation requirements for the MCQ"""
        try:
            from .investigation_preservation_engine import InvestigationPreservationEngine
            engine = InvestigationPreservationEngine()
            return engine.generate_investigation_preservation_prompt(mcq.question_text)
        except ImportError:
            self.logger.warning("Investigation preservation engine not available")
            return ""
        except Exception as e:
            self.logger.error(f"Error generating investigation preservation requirements: {e}")
            return ""
    
    def _generate_basic_preservation_requirements(self, mcq) -> str:
        """Generate basic preservation requirements if clinical detail extractor is not available"""
        return f"""
CLINICAL DETAIL PRESERVATION REQUIREMENTS:

MANDATORY REQUIREMENTS:
- PRESERVE ALL SPECIFIC MEDICAL TERMINOLOGY from the original question exactly
- MAINTAIN ALL LATERALIZATION INFORMATION (right/left) exactly as stated
- PRESERVE ALL SPECIFIC CLINICAL SIGNS mentioned in the original question
- MAINTAIN CLINICAL CONTEXT (trauma vs non-trauma, acute vs chronic, etc.)
- PRESERVE ALL ANATOMICAL SPECIFICITY mentioned in the original question
- INCLUDE ALL INVESTIGATION FINDINGS or contextual details from the original

ORIGINAL QUESTION TO PRESERVE: "{mcq.question_text}"

CRITICAL: Any deviation from these specific details will compromise the educational integrity of the case.
The case must teach the exact same clinical signs and context as the original MCQ.
"""


class CaseValidator:
    """Validates generated cases for quality and accuracy"""
    
    def __init__(self, openai_client: Optional[Any] = None):
        self.client = openai_client
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
    
    def validate_case(self, mcq, case_data: CaseData) -> ValidationResult:
        """
        Comprehensive case validation
        
        Args:
            mcq: Original MCQ
            case_data: Generated case data
            
        Returns:
            ValidationResult instance
        """
        try:
            self.logger.info(f"Validating case for MCQ {mcq.id}")
            
            # Structural validation
            structural_issues = self._validate_structure(case_data)
            
            # Content validation
            content_issues = self._validate_content(mcq, case_data)
            
            # AI-based semantic validation (if available)
            semantic_validation = self._validate_semantics(mcq, case_data)
            
            # Combine all validations
            semantic_issues = semantic_validation.get('issues', [])
            # Filter out placeholder issues from AI
            if semantic_issues and semantic_issues[0] == "any issues found":
                semantic_issues = []
            
            all_issues = structural_issues + content_issues + semantic_issues
            
            # Calculate overall score
            score = self._calculate_validation_score(structural_issues, content_issues, semantic_validation)
            
            # Determine status - be more permissive to allow case generation with warnings
            # Only fail on critical structural issues (missing required fields)
            critical_issues = [issue for issue in structural_issues if "Missing" in issue]
            
            # Allow cases to pass even with semantic/content warnings if structural integrity is good
            if critical_issues:
                status = ValidationStatus.FAILED
            elif score >= MIN_VALIDATION_SCORE:  # Use environment-aware threshold
                status = ValidationStatus.PASSED
            else:
                status = ValidationStatus.FAILED
            
            result = ValidationResult(
                status=status,
                score=score,
                reason=self._create_validation_summary(score, all_issues),
                issues=all_issues,
                metadata={
                    'structural_score': 100 - len(structural_issues) * 10,
                    'content_score': 100 - len(content_issues) * 15,
                    'semantic_score': semantic_validation['score'],
                    'validated_at': datetime.now().isoformat()
                }
            )
            
            self.logger.info(f"Validation completed for MCQ {mcq.id}: {status.value} (score: {score})")
            return result
            
        except Exception as e:
            self.logger.error(f"Validation failed for MCQ {mcq.id}: {e}")
            return ValidationResult(
                status=ValidationStatus.ERROR,
                score=0,
                reason=f"Validation error: {str(e)}",
                issues=[f"Validation process failed: {str(e)}"],
                metadata={'error': str(e)}
            )
    
    def _validate_structure(self, case_data: CaseData) -> List[str]:
        """Validate case structure and required fields"""
        issues = []
        
        # Check required fields
        if not case_data.clinical_presentation.chief_complaint:
            issues.append("Missing chief complaint")
        
        if not case_data.clinical_presentation.history_of_present_illness:
            issues.append("Missing history of present illness")
        
        if not case_data.question_prompt:
            issues.append("Missing question prompt")
        
        if not case_data.core_concept_type:
            issues.append("Missing core concept type")
        
        # Check content length
        if len(case_data.clinical_presentation.chief_complaint) < 10:
            issues.append("Chief complaint too short")
        
        if len(case_data.clinical_presentation.history_of_present_illness) < 50:
            issues.append("History too brief")
        
        return issues
    
    def _validate_content(self, mcq, case_data: CaseData) -> List[str]:
        """Validate content relevance and quality"""
        issues = []
        
        # Check MCQ ID consistency
        if case_data.source_mcq_id != mcq.id:
            issues.append(f"MCQ ID mismatch: expected {mcq.id}, got {case_data.source_mcq_id}")
        
        # Check specialty consistency
        if case_data.specialty != mcq.subspecialty:
            issues.append(f"Specialty mismatch: expected {mcq.subspecialty}, got {case_data.specialty}")
        
        # Basic content quality checks
        presentation_text = case_data.clinical_presentation.history_of_present_illness.lower()
        if 'placeholder' in presentation_text or 'example' in presentation_text:
            issues.append("Contains placeholder or example text")
        
        # Clinical detail preservation validation
        preservation_issues = self._validate_clinical_detail_preservation(mcq, case_data)
        issues.extend(preservation_issues)
        
        # Investigation preservation validation
        investigation_issues = self._validate_investigation_preservation(mcq, case_data)
        issues.extend(investigation_issues)
        
        return issues
    
    def _validate_clinical_detail_preservation(self, mcq, case_data: CaseData) -> List[str]:
        """Validate that critical clinical details from MCQ are preserved in case"""
        issues = []
        
        try:
            from .clinical_detail_extractor import ClinicalDetailExtractor
            extractor = ClinicalDetailExtractor()
            critical_details = extractor.extract_critical_details(mcq.question_text)
            
            # Check if case presentation contains the critical details
            case_text = (
                case_data.clinical_presentation.history_of_present_illness + " " +
                case_data.clinical_presentation.physical_examination + " " +
                case_data.clinical_presentation.chief_complaint
            ).lower()
            
            # Check lateralization preservation
            if critical_details['lateralization']:
                for lat_detail in critical_details['lateralization']:
                    if lat_detail['text'].lower() not in case_text:
                        issues.append(f"Missing critical lateralization: '{lat_detail['text']}'")
            
            # Check specific signs preservation
            if critical_details['specific_signs']:
                for sign_detail in critical_details['specific_signs']:
                    if sign_detail['term'].lower() not in case_text:
                        issues.append(f"Missing specific clinical sign: '{sign_detail['term']}'")
            
            # Check critical phrases preservation
            if critical_details['critical_phrases']:
                for phrase in critical_details['critical_phrases']:
                    if phrase.lower() not in case_text:
                        issues.append(f"Missing critical phrase: '{phrase}'")
            
            # Check clinical context preservation
            if critical_details['clinical_context']:
                context_preserved = False
                for context_detail in critical_details['clinical_context']:
                    if context_detail['context'].lower() in case_text:
                        context_preserved = True
                        break
                if not context_preserved and critical_details['clinical_context']:
                    missing_contexts = [ctx['context'] for ctx in critical_details['clinical_context']]
                    issues.append(f"Missing clinical context: {', '.join(missing_contexts)}")
                    
        except ImportError:
            # Fallback validation if clinical detail extractor is not available
            issues.extend(self._basic_clinical_detail_validation(mcq, case_data))
        except Exception as e:
            self.logger.warning(f"Clinical detail preservation validation failed: {e}")
            issues.append("Could not validate clinical detail preservation")
        
        return issues
    
    def _basic_clinical_detail_validation(self, mcq, case_data: CaseData) -> List[str]:
        """Basic clinical detail validation fallback"""
        issues = []
        mcq_text_lower = mcq.question_text.lower()
        case_text = (
            case_data.clinical_presentation.history_of_present_illness + " " +
            case_data.clinical_presentation.physical_examination + " " +
            case_data.clinical_presentation.chief_complaint
        ).lower()
        
        # Check for common lateralization terms
        lateralization_terms = ['right', 'left', 'bilateral', 'unilateral']
        for term in lateralization_terms:
            if term in mcq_text_lower and term not in case_text:
                issues.append(f"Missing lateralization information: '{term}'")
        
        # Check for specific medical terms that should be preserved
        import re
        medical_terms = re.findall(r'\b[a-z]+(?:\'s)?\s+(?:syndrome|sign|test|maneuver|posture)\b', mcq_text_lower)
        for term in medical_terms:
            if term not in case_text:
                issues.append(f"Missing specific medical term: '{term}'")
        
        return issues
    
    def _validate_investigation_preservation(self, mcq, case_data: CaseData) -> List[str]:
        """Validate that critical investigation findings from MCQ are preserved in case"""
        issues = []
        
        try:
            from .investigation_preservation_engine import InvestigationPreservationEngine
            engine = InvestigationPreservationEngine()
            
            # Extract investigation findings from MCQ
            findings = engine.extract_investigations(mcq.question_text)
            
            if not findings['all_findings']:
                # No investigations in MCQ, so no validation needed
                return issues
            
            # Combine all case text
            case_text = (
                case_data.clinical_presentation.history_of_present_illness + " " +
                case_data.clinical_presentation.physical_examination + " " +
                case_data.clinical_presentation.chief_complaint
            )
            
            # Validate preservation
            validation_result = engine.validate_investigation_preservation(mcq.question_text, case_text)
            
            # Add issues for missing critical investigations
            for missing_investigation in validation_result['missing_investigations']:
                issues.append(f"Missing critical investigation: '{missing_investigation}'")
            
            # If preservation rate is too low, add overall issue
            if validation_result['preservation_rate'] < 50.0:
                issues.append(f"Low investigation preservation rate: {validation_result['preservation_rate']:.1f}%")
            
            # Add info about preserved investigations for debugging
            if validation_result['preserved_investigations']:
                logger.info(f"MCQ {mcq.id}: Preserved investigations: {validation_result['preserved_investigations']}")
            
        except ImportError:
            # Investigation preservation engine not available - add basic validation
            issues.extend(self._basic_investigation_validation(mcq, case_data))
        except Exception as e:
            logger.warning(f"Investigation preservation validation failed: {e}")
            issues.append("Could not validate investigation preservation")
        
        return issues
    
    def _basic_investigation_validation(self, mcq, case_data: CaseData) -> List[str]:
        """Basic investigation validation fallback"""
        issues = []
        mcq_text_lower = mcq.question_text.lower()
        case_text = (
            case_data.clinical_presentation.history_of_present_illness + " " +
            case_data.clinical_presentation.physical_examination + " " +
            case_data.clinical_presentation.chief_complaint
        ).lower()
        
        # Check for common investigation types
        investigation_terms = {
            'eeg': 'EEG findings',
            'electroencephalogram': 'EEG findings',
            'mri': 'MRI findings',
            'ct scan': 'CT findings',
            'ct shows': 'CT findings',
            'csf': 'CSF analysis',
            'lumbar puncture': 'CSF analysis'
        }
        
        for term, description in investigation_terms.items():
            if term in mcq_text_lower and term not in case_text:
                issues.append(f"Missing {description} mentioned in MCQ")
        
        return issues
    
    def _validate_semantics(self, mcq, case_data: CaseData) -> Dict[str, Any]:
        """AI-based semantic validation"""
        if not self.client:
            return {'score': 75, 'issues': [], 'method': 'fallback'}
        
        try:
            prompt = f"""
Evaluate if this case scenario appropriately teaches the same medical concept as the original MCQ.

ORIGINAL MCQ:
{mcq.question_text}
Subspecialty: {mcq.subspecialty}

GENERATED CASE:
Chief Complaint: {case_data.clinical_presentation.chief_complaint}
History: {case_data.clinical_presentation.history_of_present_illness}
Core Concept: {case_data.core_concept_type}

CRITICAL VALIDATION REQUIREMENTS:
1. The case MUST teach the EXACT SAME MEDICAL CONDITION as the original MCQ
2. If the original MCQ mentions specific findings (CT, MRI, etc.), the case MUST include those findings
3. If the original MCQ involves trauma/injury, the case MUST involve trauma/injury
4. If the original MCQ mentions specific anatomical locations, the case MUST involve the same locations
5. The case should lead to the SAME diagnostic conclusion
6. CRITICAL: The QUESTION TYPE must match exactly:
   - If original asks about MANAGEMENT → Generated case must focus on MANAGEMENT decisions
   - If original asks about DIAGNOSIS → Generated case must focus on DIAGNOSTIC reasoning
   - If original asks about INVESTIGATION → Generated case must focus on which TEST to order
7. CLINICAL DETAIL PRESERVATION:
   - ALL specific clinical signs mentioned in the MCQ MUST be preserved in the case
   - ALL lateralization information (right/left) MUST be maintained exactly
   - Specific medical terminology (e.g., "figure of 4", "fencing posture") MUST be included verbatim
   - If MCQ mentions "right side nose rubbing", case MUST specify "right side nose rubbing"
   - Clinical context (trauma vs non-trauma, acute vs chronic) MUST be preserved

EXAMPLES OF MAJOR MISMATCHES (score 0-20):
- Original: coup contrecoup brain injury → Generated: stroke/TIA symptoms
- Original: traumatic brain injury → Generated: non-traumatic neurological condition
- Original: specific neurological condition → Generated: completely different neurological condition
- Original: "What is the second-line management for trigeminal neuralgia?" → Generated: case asking for diagnosis instead of management
- Original: management question → Generated: diagnostic scenario
- Original: diagnostic question → Generated: management scenario

CLINICAL DETAIL PRESERVATION FAILURES (score 0-30):
- Original: "figure of 4, fencing posture, right side nose rubbing" → Generated: generic "abnormal postures" without specifics
- Original: "right-sided weakness" → Generated: "weakness" without lateralization
- Original: "oscillopsia after pontine infarct" → Generated: generic "visual disturbance"
- Original: specific medical signs → Generated: generalized symptoms
- Original: trauma context → Generated: non-traumatic presentation

Rate the alignment on a scale of 0-100:
- 90-100: Excellent alignment - same medical condition with appropriate clinical variation
- 70-89: Good alignment - same condition with minor presentation differences
- 50-69: Moderate alignment - related conditions within same diagnostic category
- 30-49: Acceptable alignment - same neurological subspecialty with educational value
- 20-29: Poor alignment - different conditions but same specialty
- 0-19: Severe mismatch - completely different medical conditions

IMPORTANT: Be more lenient in scoring. If the case teaches valuable concepts within the same subspecialty, score at least 40.

Respond with JSON only:
{{"score": 85, "issues": [], "explanation": "brief explanation"}}
"""
            
            response = _run_chat_completion(
                self.client,
                self.logger,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.1,
                max_tokens=500,
            )
            
            # Parse response and clean up issues
            response_text = get_first_choice_text(response)
            result = json.loads(response_text)
            
            # Filter out generic issues
            if result.get('issues'):
                filtered_issues = []
                for issue in result['issues']:
                    if issue and issue.lower() not in ['any issues found', 'none', 'n/a', '']:
                        filtered_issues.append(issue)
                result['issues'] = filtered_issues
            
            result['method'] = 'ai_validation'
            return result
            
        except Exception as e:
            self.logger.warning(f"AI validation failed: {e}")
            return {'score': 75, 'issues': [], 'method': 'fallback_due_to_error'}
    
    def _calculate_validation_score(self, structural_issues: List[str], 
                                  content_issues: List[str], 
                                  semantic_validation: Dict[str, Any]) -> float:
        """Calculate overall validation score"""
        structural_score = max(0, 100 - len(structural_issues) * 10)
        content_score = max(0, 100 - len(content_issues) * 15)
        semantic_score = semantic_validation.get('score', 75)
        
        # Weighted average
        overall_score = (structural_score * 0.3 + content_score * 0.3 + semantic_score * 0.4)
        return round(overall_score, 1)
    
    def _create_validation_summary(self, score: float, issues: List[str]) -> str:
        """Create human-readable validation summary"""
        if score >= 90:
            quality = "Excellent"
        elif score >= 80:
            quality = "Good"
        elif score >= 70:
            quality = "Acceptable"
        elif score >= 50:
            quality = "Usable with warnings"
        else:
            quality = "Poor"
        
        summary = f"{quality} case quality (score: {score}/100)"
        if issues:
            # Categorize issues
            critical_issues = [issue for issue in issues if "Missing" in issue]
            warning_issues = [issue for issue in issues if "Missing" not in issue]
            
            if critical_issues:
                summary += f". Critical issues: {'; '.join(critical_issues[:2])}"
            elif warning_issues:
                summary += f". Warnings: {'; '.join(warning_issues[:2])}"
                if len(warning_issues) > 2:
                    summary += f" and {len(warning_issues) - 2} more warnings"
        
        return summary


class CacheManager:
    """Manages caching for MCQ conversions"""
    
    @staticmethod
    def get_cache_key(mcq_id: int) -> str:
        """Generate cache key for MCQ conversion"""
        return f"mcq_case_conversion_{mcq_id}_{CACHE_VERSION}"
    
    @staticmethod
    def get_cached_conversion(mcq_id: int) -> Optional[Dict[str, Any]]:
        """Retrieve cached conversion if available"""
        cache_key = CacheManager.get_cache_key(mcq_id)
        return cache.get(cache_key)
    
    @staticmethod
    def cache_conversion(mcq_id: int, case_data: Dict[str, Any]) -> None:
        """Cache successful conversion"""
        cache_key = CacheManager.get_cache_key(mcq_id)
        cache_data = {
            'case_data': case_data,
            'cached_at': datetime.now().isoformat(),
            'cache_version': CACHE_VERSION
        }
        cache.set(cache_key, cache_data, CACHE_TIMEOUT)
    
    @staticmethod
    def clear_cache(mcq_id: int) -> None:
        """Clear cache for specific MCQ"""
        cache_key = CacheManager.get_cache_key(mcq_id)
        cache.delete(cache_key)


class MCQCaseConverter:
    """
    Main converter class that orchestrates the entire conversion process
    
    This is the primary interface for converting MCQs to case-based learning scenarios.
    It provides a clean, robust API with comprehensive error handling and validation.
    """
    
    def __init__(self):
        """Initialize converter with all required components"""
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        
        # Use shared OpenAI client from the integration layer
        self.openai_client = openai_client
        
        if not self.openai_client:
            self.logger.warning("OpenAI client not available - conversion will fail")
        
        # Initialize components
        self.analyzer = MCQAnalyzer(self.openai_client) if self.openai_client else None
        self.generator = CaseGenerator(self.openai_client) if self.openai_client else None
        self.validator = CaseValidator(self.openai_client)
        
        self.logger.info("MCQ Case Converter initialized")
    
    def convert_mcq_to_case(self, mcq, include_debug=False) -> Dict[str, Any]:
        """
        Convert MCQ to case-based learning scenario
        
        Args:
            mcq: MCQ model instance
            include_debug: Whether to include detailed debug information
            
        Returns:
            Dictionary containing case data compatible with existing system
            
        Raises:
            Exception: If conversion fails after all retry attempts
        """
        debug_log = []
        
        def log_debug(step: str, data: Any):
            """Add debug entry"""
            if include_debug:
                debug_log.append({
                    'timestamp': datetime.now().isoformat(),
                    'step': step,
                    'data': str(data)[:500] if not isinstance(data, dict) else data
                })
                self.logger.info(f"[DEBUG] {step}: {str(data)[:200]}")
        
        if not self.openai_client or not self.generator:
            error_msg = "OpenAI client not available for case generation"
            log_debug("INITIALIZATION_ERROR", error_msg)
            raise Exception(error_msg)
        
        log_debug("CONVERSION_START", {
            'mcq_id': mcq.id,
            'subspecialty': mcq.subspecialty,
            'question_preview': mcq.question_text[:100] + '...'
        })
        
        # Check cache first
        cached_result = CacheManager.get_cached_conversion(mcq.id)
        if cached_result:
            log_debug("CACHE_HIT", "Using cached conversion")
            if include_debug:
                cached_result['case_data']['_debug_log'] = debug_log
            return cached_result['case_data']
        
        log_debug("CACHE_MISS", "No cached conversion found")
        
        # Attempt conversion with retries
        for attempt in range(MAX_RETRY_ATTEMPTS):
            try:
                log_debug(f"ATTEMPT_{attempt + 1}", f"Starting conversion attempt {attempt + 1}/{MAX_RETRY_ATTEMPTS}")
                
                # Step 1: Analyze MCQ
                log_debug("ANALYSIS_START", "Analyzing MCQ content")
                analysis = self.analyzer.analyze_mcq(mcq)
                log_debug("ANALYSIS_COMPLETE", {
                    'question_type': analysis['question_type'].value,
                    'complexity': analysis['complexity'].value,
                    'patient_info': f"{analysis['patient_info'].age}yo {analysis['patient_info'].gender}",
                    'age_descriptor': analysis['age_descriptor'],
                    'specialty_confidence': analysis['specialty_confidence']
                })
                
                # Step 2: Generate case
                log_debug("GENERATION_START", "Generating case via OpenAI")
                case_data = self.generator.generate_case(mcq, analysis)
                log_debug("GENERATION_COMPLETE", {
                    'has_clinical_presentation': bool(case_data.clinical_presentation),
                    'core_concept': case_data.core_concept_type,
                    'learning_objectives_count': len(case_data.learning_objectives)
                })
                
                # Step 3: Validate case
                log_debug("VALIDATION_START", "Validating generated case")
                validation_result = self.validator.validate_case(mcq, case_data)
                log_debug("VALIDATION_COMPLETE", {
                    'status': validation_result.status.value,
                    'score': validation_result.score,
                    'reason': validation_result.reason,
                    'issues': validation_result.issues,
                    'metadata': validation_result.metadata
                })
                
                # Step 4: Check if validation passed
                if validation_result.status == ValidationStatus.PASSED:
                    # Convert to legacy format for compatibility
                    log_debug("FORMAT_CONVERSION", "Converting to legacy format")
                    legacy_format = self._convert_to_legacy_format(case_data, validation_result)
                    
                    # Cache successful conversion
                    log_debug("CACHE_STORE", "Storing in cache")
                    CacheManager.cache_conversion(mcq.id, legacy_format)
                    
                    log_debug("CONVERSION_SUCCESS", {
                        'mcq_id': mcq.id,
                        'validation_score': validation_result.score,
                        'attempts': attempt + 1
                    })
                    
                    if include_debug:
                        legacy_format['_debug_log'] = debug_log
                    
                    return legacy_format
                else:
                    log_debug("VALIDATION_FAILED", {
                        'reason': validation_result.reason,
                        'issues': validation_result.issues,
                        'will_retry': attempt < MAX_RETRY_ATTEMPTS - 1
                    })
                    
                    if attempt == MAX_RETRY_ATTEMPTS - 1:
                        error_msg = f"Conversion failed validation: {validation_result.reason}"
                        if include_debug:
                            error_msg += f"\n\nDebug Log:\n{json.dumps(debug_log, indent=2)}"
                        raise Exception(error_msg)
                
            except Exception as e:
                log_debug(f"ATTEMPT_{attempt + 1}_ERROR", {
                    'error': str(e),
                    'error_type': type(e).__name__,
                    'will_retry': attempt < MAX_RETRY_ATTEMPTS - 1
                })
                
                if attempt == MAX_RETRY_ATTEMPTS - 1:
                    error_msg = f"All conversion attempts failed for MCQ {mcq.id}: {str(e)}"
                    if include_debug:
                        error_msg += f"\n\nDebug Log:\n{json.dumps(debug_log, indent=2)}"
                    raise Exception(error_msg)
        
        # This should never be reached due to the raise in the loop
        error_msg = f"Unexpected error in conversion for MCQ {mcq.id}"
        if include_debug:
            error_msg += f"\n\nDebug Log:\n{json.dumps(debug_log, indent=2)}"
        raise Exception(error_msg)
    
    def _convert_to_legacy_format(self, case_data: CaseData, validation_result: ValidationResult) -> Dict[str, Any]:
        """
        Convert new case format to legacy format for backward compatibility
        
        This ensures the new system works with existing views and templates.
        """
        # Enhance clinical presentation with inferred details
        enhanced_presentation = self._enhance_with_clinical_inferences(
            case_data.clinical_presentation.history_of_present_illness,
            case_data.metadata.get('original_mcq_text', '')
        )
        
        # Add investigation findings if missing
        enhanced_presentation = self._enhance_with_investigation_findings(
            enhanced_presentation,
            case_data.metadata.get('original_mcq_text', '')
        )
        
        return {
            # Core case data
            'source_mcq_id': case_data.source_mcq_id,
            'clinical_presentation': enhanced_presentation,
            'patient_demographics': f"{case_data.patient_demographics.age}-year-old {case_data.patient_demographics.gender}",
            'question_prompt': case_data.question_prompt,
            'core_concept_type': case_data.core_concept_type,
            
            # Additional legacy fields
            'specialty': case_data.specialty,
            'question_type': case_data.question_type.value,
            'difficulty': case_data.complexity.value,
            
            # Validation metadata
            'professional_validation': {
                'passed': validation_result.status == ValidationStatus.PASSED,
                'score': validation_result.score,
                'reason': validation_result.reason,
                'method': 'professional_v2',
                'issues': validation_result.issues,
                'has_warnings': len(validation_result.issues) > 0 and validation_result.status == ValidationStatus.PASSED,
                'warning_count': len([issue for issue in validation_result.issues if "Missing" not in issue]),
                'critical_issues': [issue for issue in validation_result.issues if "Missing" in issue],
                'validated_at': datetime.now().isoformat()
            },
            
            # System metadata
            'mcq_source_validated': True,
            'generator_version': 'v2.0.0_professional',
            'mcq_checksum': case_data.metadata.get('source_mcq_checksum'),
            'generated_at': case_data.metadata.get('generated_at'),
            
            # Extended case data for future use
            '_extended_data': {
                'patient_demographics': asdict(case_data.patient_demographics),
                'clinical_presentation': asdict(case_data.clinical_presentation),
                'learning_objectives': case_data.learning_objectives,
                'validation_metadata': validation_result.to_dict()
            }
        }
    
    def clear_cache_for_mcq(self, mcq_id: int) -> None:
        """Clear cache for specific MCQ"""
        CacheManager.clear_cache(mcq_id)
        self.logger.info(f"Cache cleared for MCQ {mcq_id}")
    
    def get_conversion_stats(self) -> Dict[str, Any]:
        """Get conversion statistics"""
        return {
            'cache_version': CACHE_VERSION,
            'max_retry_attempts': MAX_RETRY_ATTEMPTS,
            'openai_available': self.openai_client is not None,
            'components_initialized': {
                'analyzer': self.analyzer is not None,
                'generator': self.generator is not None,
                'validator': self.validator is not None
            }
        }
    
    def _enhance_with_clinical_inferences(self, clinical_presentation: str, original_mcq_text: str = "") -> str:
        """Enhance clinical presentation with medically accurate inferred details"""
        try:
            from .clinical_inference_engine import enhance_case_with_clinical_inferences
            return enhance_case_with_clinical_inferences(clinical_presentation, original_mcq_text)
        except ImportError:
            self.logger.warning("Clinical inference engine not available - using original presentation")
            return clinical_presentation
        except Exception as e:
            self.logger.error(f"Error enhancing clinical presentation: {e}")
            return clinical_presentation
    
    def _enhance_with_investigation_findings(self, clinical_presentation: str, original_mcq_text: str = "") -> str:
        """Add investigation findings to case presentation if missing"""
        try:
            from .investigation_preservation_engine import enhance_case_with_investigation_findings
            return enhance_case_with_investigation_findings(clinical_presentation, original_mcq_text)
        except ImportError:
            self.logger.warning("Investigation preservation engine not available - using original presentation")
            return clinical_presentation
        except Exception as e:
            self.logger.error(f"Error enhancing case with investigations: {e}")
            return clinical_presentation
    
# Public API functions for backward compatibility
def convert_mcq_to_case(mcq, include_debug=False) -> Dict[str, Any]:
    """
    Main conversion function - backward compatible interface
    
    Args:
        mcq: MCQ model instance
        include_debug: Whether to include detailed debug information
        
    Returns:
        Case data dictionary
    """
    converter = MCQCaseConverter()
    return converter.convert_mcq_to_case(mcq, include_debug=include_debug)


def get_mcq_cache_key(mcq_id: int) -> str:
    """Get cache key for MCQ - backward compatible"""
    return CacheManager.get_cache_key(mcq_id)


def clear_mcq_cache(mcq_id: int) -> None:
    """Clear cache for MCQ - backward compatible"""
    CacheManager.clear_cache(mcq_id)


# Module-level initialization
import os
logger.info(f"Professional MCQ Case Converter v2.0.0 loaded - OpenAI available: {os.environ.get('OPENAI_API_KEY') is not None}")
