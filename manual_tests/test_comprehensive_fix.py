#!/usr/bin/env python3
"""
Test Comprehensive Professional Fix for MCQ-to-Case Conversion
Tests the 4 critical issues identified in the 7-year-old epilepsy case:
1. Age inconsistency (7-year-old → 8-year-old)
2. Missing critical diagnostic information (EEG findings)
3. Inappropriate clinical inference (post-ictal confusion for visual auras)
4. Missing examination component
"""

import os
import sys
import django
import json
from datetime import datetime

# Setup Django environment
sys.path.append('/Users/tariqalmatrudi/NEWreader/django_neurology_mcq')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_neurology_mcq.settings')
django.setup()

from mcq.models import MCQ
from mcq.mcq_case_converter import MCQCaseConverter


def test_comprehensive_fix():
    """Test the comprehensive fix with the 7-year-old epilepsy case"""
    
    print("="*80)
    print("COMPREHENSIVE PROFESSIONAL FIX TEST")
    print("="*80)
    print(f"Test started at: {datetime.now().isoformat()}")
    print()
    
    # Create a test MCQ that mimics the 7-year-old epilepsy case
    test_mcq_data = {
        'question_text': 'A 7-year-old boy presents with visual hallucinations described as colorful, circular objects moving in his visual field. An electroencephalogram (EEG) shows occipital lobe spikes. What is the most appropriate management?',
        'subspecialty': 'Epilepsy',
        'correct_answer': 'A',
        'option_a': 'Carbamazepine',
        'option_b': 'Valproate', 
        'option_c': 'Levetiracetam',
        'option_d': 'Observation only',
        'explanation': 'This case represents benign childhood epilepsy with occipital paroxysms. These are typically brief visual auras without loss of consciousness.',
        'id': 999999  # Test ID
    }
    
    # Create a mock MCQ object
    class MockMCQ:
        def __init__(self, data):
            for key, value in data.items():
                setattr(self, key, value)
                
        @property
        def correct_answer_text(self):
            return getattr(self, f'option_{self.correct_answer.lower()}', '')
    
    test_mcq = MockMCQ(test_mcq_data)
    
    print("TEST MCQ:")
    print(f"Question: {test_mcq.question_text}")
    print(f"Subspecialty: {test_mcq.subspecialty}")
    print(f"Correct Answer: {test_mcq.correct_answer} - {test_mcq.correct_answer_text}")
    print()
    
    # Initialize converter
    print("Initializing MCQ Case Converter...")
    converter = MCQCaseConverter()
    
    if not converter.openai_client:
        print("ERROR: OpenAI client not available - cannot test conversion")
        return
    
    print("Converter initialized successfully")
    print()
    
    # Test the conversion
    print("TESTING MCQ-TO-CASE CONVERSION...")
    print("-"*50)
    
    try:
        # Convert with debug information
        result = converter.convert_mcq_to_case(test_mcq, include_debug=True)
        
        print("✅ CONVERSION SUCCESSFUL!")
        print()
        
        # Analyze results for the 4 critical issues
        print("CRITICAL ISSUES ANALYSIS:")
        print("="*40)
        
        # Issue 1: Age consistency check
        print("1. AGE CONSISTENCY CHECK:")
        patient_demographics = result.get('patient_demographics', '')
        clinical_presentation = result.get('clinical_presentation', '')
        
        age_preserved = '7-year-old' in patient_demographics or '7-year-old' in clinical_presentation
        if age_preserved:
            print("   ✅ PASS: Age correctly preserved as 7-year-old")
        else:
            print(f"   ❌ FAIL: Age not preserved correctly")
            print(f"      Demographics: {patient_demographics}")
        print()
        
        # Issue 2: Investigation preservation check
        print("2. INVESTIGATION PRESERVATION CHECK:")
        eeg_preserved = ('EEG' in clinical_presentation or 
                        'electroencephalogram' in clinical_presentation or
                        'occipital lobe spikes' in clinical_presentation)
        
        if eeg_preserved:
            print("   ✅ PASS: EEG findings preserved in case")
        else:
            print("   ❌ FAIL: EEG findings missing from case")
        print()
        
        # Issue 3: Inappropriate clinical inference check
        print("3. INAPPROPRIATE CLINICAL INFERENCE CHECK:")
        has_post_ictal_confusion = 'post-ictal confusion' in clinical_presentation.lower()
        
        if not has_post_ictal_confusion:
            print("   ✅ PASS: No inappropriate post-ictal confusion added")
        else:
            print("   ❌ FAIL: Inappropriate post-ictal confusion detected")
            print("      (This should not occur for visual auras in children)")
        print()
        
        # Issue 4: Examination component check
        print("4. EXAMINATION COMPONENT CHECK:")
        has_examination = ('examination' in clinical_presentation.lower() or 
                          'exam' in clinical_presentation.lower() or
                          'neurological' in clinical_presentation.lower())
        
        if has_examination:
            print("   ✅ PASS: Examination component included")
        else:
            print("   ❌ FAIL: Missing examination component")
        print()
        
        # Validation results
        print("VALIDATION RESULTS:")
        print("="*40)
        validation = result.get('professional_validation', {})
        
        print(f"Validation Status: {'✅ PASSED' if validation.get('passed') else '❌ FAILED'}")
        print(f"Validation Score: {validation.get('score', 'N/A')}/100")
        print(f"Validation Method: {validation.get('method', 'unknown')}")
        
        if validation.get('issues'):
            print("Issues detected:")
            for i, issue in enumerate(validation['issues'], 1):
                print(f"  {i}. {issue}")
        else:
            print("No validation issues detected")
        print()
        
        # Show generated case
        print("GENERATED CASE:")
        print("="*40)
        print("Patient Demographics:", patient_demographics)
        print()
        print("Clinical Presentation:")
        print(clinical_presentation)
        print()
        print("Question Prompt:", result.get('question_prompt', ''))
        print()
        print("Core Concept:", result.get('core_concept_type', ''))
        print()
        
        # Debug information if available
        if '_debug_log' in result:
            print("DEBUG LOG:")
            print("="*40)
            for entry in result['_debug_log'][-5:]:  # Show last 5 entries
                print(f"[{entry['timestamp']}] {entry['step']}: {str(entry['data'])[:100]}...")
            print()
        
        # Overall assessment
        print("OVERALL ASSESSMENT:")
        print("="*40)
        
        critical_issues_fixed = (age_preserved and 
                               eeg_preserved and 
                               not has_post_ictal_confusion and 
                               has_examination)
        
        if critical_issues_fixed:
            print("🎉 SUCCESS: All 4 critical issues have been addressed!")
            print("   - Age consistency: Maintained")
            print("   - Investigation preservation: Working")
            print("   - Clinical inference appropriateness: Enhanced")
            print("   - Examination component: Included")
        else:
            print("⚠️  PARTIAL SUCCESS: Some issues remain")
            failed_checks = []
            if not age_preserved:
                failed_checks.append("Age consistency")
            if not eeg_preserved:
                failed_checks.append("Investigation preservation")
            if has_post_ictal_confusion:
                failed_checks.append("Inappropriate clinical inference")
            if not has_examination:
                failed_checks.append("Missing examination")
            
            print(f"   Issues to address: {', '.join(failed_checks)}")
        
    except Exception as e:
        print(f"❌ CONVERSION FAILED: {str(e)}")
        print()
        
        # Try to get more details
        import traceback
        print("ERROR DETAILS:")
        print(traceback.format_exc())
    
    print("="*80)
    print(f"Test completed at: {datetime.now().isoformat()}")
    print("="*80)


if __name__ == "__main__":
    test_comprehensive_fix()