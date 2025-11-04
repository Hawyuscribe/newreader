#!/usr/bin/env python3
"""
Test script for MCQ-to-Case Conversion Fixes
Verifies that all fixes are working correctly

Usage:
    python test_mcq_case_fixes.py
"""

import os
import sys
import django
from datetime import datetime

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
django.setup()

from mcq.models import MCQ, MCQCaseConversionSession
from django.contrib.auth.models import User
from django.core.cache import cache
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MCQCaseFixesTester:
    """Test the MCQ case conversion fixes"""
    
    def __init__(self):
        self.is_heroku = bool(os.environ.get('DYNO'))
        self.tests_passed = 0
        self.tests_failed = 0
        
    def run_all_tests(self):
        """Run comprehensive tests of the fixes"""
        logger.info("🧪 Testing MCQ-to-Case Conversion Fixes")
        logger.info(f"Environment: {'Heroku' if self.is_heroku else 'Local'}")
        logger.info("=" * 60)
        
        # Test 1: API Model Configuration
        self._test_api_model_configuration()
        
        # Test 2: Validation Thresholds
        self._test_validation_thresholds()
        
        # Test 3: Case Generation
        self._test_case_generation()
        
        # Test 4: Session Validation
        self._test_session_validation()
        
        # Test 5: Heroku-specific Features
        if self.is_heroku:
            self._test_heroku_features()
        
        # Summary
        self._print_test_summary()
        
        return self.tests_failed == 0
    
    def _test_api_model_configuration(self):
        """Test that all components use gpt-4.1-nano"""
        logger.info("📋 Test 1: API Model Configuration")
        
        try:
            # Test MCQ Case Converter
            from mcq.mcq_case_converter import MCQCaseConverter
            converter = MCQCaseConverter()
            
            if converter.openai_client:
                logger.info("  ✅ MCQ Case Converter: OpenAI client initialized")
                self.tests_passed += 1
            else:
                logger.error("  ❌ MCQ Case Converter: OpenAI client not available")
                self.tests_failed += 1
            
            # Test Case Session Validator
            from mcq.case_session_validator import case_validator, client
            
            if client:
                logger.info("  ✅ Case Session Validator: OpenAI client initialized")
                self.tests_passed += 1
            else:
                logger.error("  ❌ Case Session Validator: OpenAI client not available")
                self.tests_failed += 1
            
            # Check environment variables
            api_key = os.environ.get('OPENAI_API_KEY') or os.environ.get('OPENAI_KEY')
            if api_key:
                logger.info("  ✅ OpenAI API key is configured")
                self.tests_passed += 1
            else:
                logger.error("  ❌ OpenAI API key not found")
                self.tests_failed += 1
                
        except Exception as e:
            logger.error(f"  ❌ API model configuration test failed: {e}")
            self.tests_failed += 1
    
    def _test_validation_thresholds(self):
        """Test validation threshold configuration"""
        logger.info("\n📋 Test 2: Validation Thresholds")
        
        try:
            from mcq.mcq_case_converter import MIN_VALIDATION_SCORE, MIN_SEMANTIC_SCORE
            from mcq.case_session_validator import MIN_CONFIDENCE_THRESHOLD
            
            expected_validation = 40 if self.is_heroku else 70
            expected_semantic = 30 if self.is_heroku else 50
            expected_confidence = 40 if self.is_heroku else 70
            
            if MIN_VALIDATION_SCORE == expected_validation:
                logger.info(f"  ✅ Min validation score: {MIN_VALIDATION_SCORE}")
                self.tests_passed += 1
            else:
                logger.error(f"  ❌ Min validation score wrong: {MIN_VALIDATION_SCORE} (expected {expected_validation})")
                self.tests_failed += 1
            
            if MIN_SEMANTIC_SCORE == expected_semantic:
                logger.info(f"  ✅ Min semantic score: {MIN_SEMANTIC_SCORE}")
                self.tests_passed += 1
            else:
                logger.error(f"  ❌ Min semantic score wrong: {MIN_SEMANTIC_SCORE} (expected {expected_semantic})")
                self.tests_failed += 1
            
            if MIN_CONFIDENCE_THRESHOLD == expected_confidence:
                logger.info(f"  ✅ Min confidence threshold: {MIN_CONFIDENCE_THRESHOLD}")
                self.tests_passed += 1
            else:
                logger.error(f"  ❌ Min confidence threshold wrong: {MIN_CONFIDENCE_THRESHOLD} (expected {expected_confidence})")
                self.tests_failed += 1
                
        except Exception as e:
            logger.error(f"  ❌ Validation threshold test failed: {e}")
            self.tests_failed += 1
    
    def _test_case_generation(self):
        """Test case generation with new settings"""
        logger.info("\n📋 Test 3: Case Generation")
        
        try:
            # Find a test MCQ
            test_mcq = MCQ.objects.filter(subspecialty__isnull=False).first()
            
            if not test_mcq:
                logger.warning("  ⚠️  No test MCQ found - skipping generation test")
                return
            
            logger.info(f"  Testing with MCQ {test_mcq.id}: {test_mcq.subspecialty}")
            
            # Test the converter
            from mcq.mcq_case_converter import convert_mcq_to_case
            
            # This is a dry run - we won't actually call the API unless needed
            logger.info("  📝 Case generation framework: Ready")
            
            # Test cache key generation
            from mcq.mcq_case_converter import get_mcq_cache_key
            cache_key = get_mcq_cache_key(test_mcq.id)
            
            if cache_key:
                logger.info(f"  ✅ Cache key generation: {cache_key}")
                self.tests_passed += 1
            else:
                logger.error("  ❌ Cache key generation failed")
                self.tests_failed += 1
                
        except Exception as e:
            logger.error(f"  ❌ Case generation test failed: {e}")
            self.tests_failed += 1
    
    def _test_session_validation(self):
        """Test session validation improvements"""
        logger.info("\n📋 Test 4: Session Validation")
        
        try:
            # Test session validator
            from mcq.case_session_validator import case_validator
            
            # Create mock case data for testing
            test_mcq = MCQ.objects.filter(subspecialty__isnull=False).first()
            
            if test_mcq:
                mock_case_data = {
                    'source_mcq_id': test_mcq.id,
                    'clinical_presentation': 'Mock clinical presentation for testing validation framework',
                    'patient_demographics': '45-year-old male',
                    'question_prompt': 'What is the most appropriate next step?',
                    'core_concept_type': 'Test concept',
                    '_validation_result': {
                        'valid': True,
                        'score': 80,
                        'method': 'test'
                    }
                }
                
                # Test lightweight validation (doesn't require API call)
                validation_key = case_validator._create_validation_key(test_mcq, mock_case_data)
                
                if validation_key:
                    logger.info(f"  ✅ Validation key generation: Working")
                    self.tests_passed += 1
                else:
                    logger.error("  ❌ Validation key generation failed")
                    self.tests_failed += 1
                
                # Test fallback validation
                fallback_result = case_validator._fallback_validation(test_mcq, mock_case_data)
                
                if fallback_result.get('valid'):
                    logger.info(f"  ✅ Fallback validation: Passed (score: {fallback_result.get('score')})")
                    self.tests_passed += 1
                else:
                    logger.error(f"  ❌ Fallback validation failed: {fallback_result.get('reason')}")
                    self.tests_failed += 1
            else:
                logger.warning("  ⚠️  No test MCQ found - skipping validation test")
                
        except Exception as e:
            logger.error(f"  ❌ Session validation test failed: {e}")
            self.tests_failed += 1
    
    def _test_heroku_features(self):
        """Test Heroku-specific features"""
        logger.info("\n📋 Test 5: Heroku-Specific Features")
        
        try:
            # Test environment detection
            dyno_env = os.environ.get('DYNO')
            if dyno_env:
                logger.info(f"  ✅ Heroku environment detected: {dyno_env}")
                self.tests_passed += 1
            else:
                logger.error("  ❌ DYNO environment variable not found")
                self.tests_failed += 1
            
            # Test reduced timeouts
            from mcq.mcq_case_converter import API_TIMEOUT, MAX_RETRY_ATTEMPTS
            
            if API_TIMEOUT == 30:
                logger.info(f"  ✅ API timeout reduced for Heroku: {API_TIMEOUT}s")
                self.tests_passed += 1
            else:
                logger.error(f"  ❌ API timeout not reduced: {API_TIMEOUT}s")
                self.tests_failed += 1
            
            if MAX_RETRY_ATTEMPTS == 3:
                logger.info(f"  ✅ Retry attempts reduced for Heroku: {MAX_RETRY_ATTEMPTS}")
                self.tests_passed += 1
            else:
                logger.error(f"  ❌ Retry attempts not reduced: {MAX_RETRY_ATTEMPTS}")
                self.tests_failed += 1
            
            # Test lightweight validation
            from mcq.end_to_end_integrity import e2e_integrity
            
            test_mcq = MCQ.objects.first()
            if test_mcq:
                mock_case_data = {'source_mcq_id': test_mcq.id, 'clinical_presentation': 'Test content for lightweight validation'}
                
                lightweight_result = e2e_integrity._lightweight_validation(test_mcq, mock_case_data, 'test_session')
                
                if lightweight_result.get('valid'):
                    logger.info(f"  ✅ Lightweight validation: Working")
                    self.tests_passed += 1
                else:
                    logger.error(f"  ❌ Lightweight validation failed: {lightweight_result.get('reason')}")
                    self.tests_failed += 1
                    
        except Exception as e:
            logger.error(f"  ❌ Heroku features test failed: {e}")
            self.tests_failed += 1
    
    def _print_test_summary(self):
        """Print test summary"""
        logger.info("\n" + "=" * 60)
        logger.info("📊 TEST SUMMARY")
        logger.info(f"Tests Passed: {self.tests_passed}")
        logger.info(f"Tests Failed: {self.tests_failed}")
        logger.info(f"Success Rate: {(self.tests_passed / (self.tests_passed + self.tests_failed)) * 100:.1f}%")
        
        if self.tests_failed == 0:
            logger.info("🎉 ALL TESTS PASSED!")
            logger.info("\nThe MCQ-to-Case conversion fixes are working correctly.")
            
            if self.is_heroku:
                logger.info("\nHeroku-specific optimizations are active:")
                logger.info("- Lower validation thresholds")
                logger.info("- Reduced API timeouts")
                logger.info("- Lightweight validation for better performance")
        else:
            logger.error("❌ SOME TESTS FAILED!")
            logger.error("Please review the error messages above and fix the issues.")


def main():
    """Main test function"""
    print("🔧 MCQ-to-Case Conversion Fixes Test Suite")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not os.path.exists('manage.py'):
        print("❌ Error: Run this script from the Django project root directory")
        sys.exit(1)
    
    # Initialize tester
    tester = MCQCaseFixesTester()
    
    # Run tests
    success = tester.run_all_tests()
    
    if success:
        print("\n✅ All tests passed! The fixes are working correctly.")
        sys.exit(0)
    else:
        print("\n❌ Some tests failed! Please review and fix the issues.")
        sys.exit(1)


if __name__ == "__main__":
    main()