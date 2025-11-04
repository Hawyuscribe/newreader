#!/usr/bin/env python3
"""
Test specific fixes for identified issues
"""

import os
import sys
import django

# Setup Django
sys.path.append('/Users/tariqalmatrudi/NEWreader/django_neurology_mcq')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
django.setup()

from mcq.models import MCQ
from mcq.mcq_case_converter import convert_mcq_to_case, detect_question_type

def test_specific_mcq_fix(mcq_id, expected_issue_type):
    """Test a specific MCQ to verify fix"""
    try:
        mcq = MCQ.objects.get(id=mcq_id)
        print(f"\n{'='*80}")
        print(f"🔬 TESTING FIX FOR MCQ {mcq_id}")
        print(f"Issue Type: {expected_issue_type}")
        print(f"Subspecialty: {getattr(mcq, 'subspecialty', 'Unknown')}")
        print(f"Question: {mcq.question_text}")
        print(f"Correct Answer: {mcq.correct_answer}")
        print(f"{'='*80}")
        
        # Test question type detection
        detected_type = detect_question_type(mcq)
        print(f"🎯 Detected Question Type: {detected_type}")
        
        # Test case conversion
        case_data = convert_mcq_to_case(mcq)
        
        clinical_presentation = case_data.get('clinical_presentation', '')
        question_type = case_data.get('question_type', '')
        fallback_used = case_data.get('fallback_used', False)
        
        print(f"\n📋 Generated Case:")
        print(f"  Question Type: {question_type}")
        print(f"  Fallback Used: {fallback_used}")
        print(f"  Clinical Presentation: {clinical_presentation}")
        
        # Analyze for specific issues
        original_lower = mcq.question_text.lower()
        case_lower = clinical_presentation.lower()
        
        # Check for missing critical terms
        critical_terms = ['ms', 'multiple sclerosis', 'parkinson', 'huntington', 'horner', 'stroke', 'seizure', 'epilepsy']
        missing_terms = []
        for term in critical_terms:
            if term in original_lower and term not in case_lower:
                missing_terms.append(term)
        
        # Check for topic drift
        topic_categories = {
            'movement': ['parkinson', 'huntington', 'chorea', 'tremor', 'rigidity'],
            'ms': ['multiple sclerosis', 'ms', 'demyelinating'],
            'dementia': ['alzheimer', 'dementia', 'cognitive'],
            'stroke': ['stroke', 'infarct', 'hemorrhage'],
            'seizure': ['seizure', 'epilepsy', 'ictal']
        }
        
        original_topics = set()
        case_topics = set()
        
        for topic, keywords in topic_categories.items():
            if any(kw in original_lower for kw in keywords):
                original_topics.add(topic)
            if any(kw in case_lower for kw in keywords):
                case_topics.add(topic)
        
        # Results analysis
        print(f"\n🔍 ANALYSIS:")
        
        if missing_terms:
            print(f"  ❌ Missing Critical Terms: {', '.join(missing_terms)}")
        else:
            print(f"  ✅ All Critical Terms Preserved")
        
        if original_topics and case_topics:
            if original_topics.intersection(case_topics):
                print(f"  ✅ Topic Consistency: {original_topics} → {case_topics}")
            else:
                print(f"  ❌ Topic Drift: {original_topics} → {case_topics}")
        elif original_topics:
            print(f"  ⚠️ Original topics not found in case: {original_topics}")
        
        # Purpose alignment
        purpose_check = {
            'diagnosis': ['diagnosis'],
            'management': ['management'],
            'investigation': ['investigation'],
            'advanced_management': ['advanced_management']
        }
        
        if detected_type == question_type:
            print(f"  ✅ Purpose Alignment: {detected_type}")
        else:
            print(f"  ❌ Purpose Mismatch: detected {detected_type} → generated {question_type}")
        
        # Overall assessment
        issues = 0
        if missing_terms:
            issues += 1
        if original_topics and case_topics and not original_topics.intersection(case_topics):
            issues += 1
        if detected_type != question_type:
            issues += 1
        if fallback_used:
            issues += 1
        
        if issues == 0:
            print(f"\n🎉 SUCCESS: All issues resolved!")
            return True
        else:
            print(f"\n⚠️ REMAINING ISSUES: {issues} problems detected")
            return False
            
    except MCQ.DoesNotExist:
        print(f"❌ MCQ {mcq_id} not found")
        return False
    except Exception as e:
        print(f"❌ Error testing MCQ {mcq_id}: {e}")
        return False

def test_targeted_fixes():
    """Test fixes for specific identified issues"""
    print("🔧 TESTING TARGETED FIXES")
    print("=" * 80)
    
    # Test cases based on the comprehensive analysis findings
    test_cases = [
        # MS-related MCQs (missing MS terms)
        {'mcq_id': 67993499, 'issue': 'MISSING_CONDITION: ms'},
        {'mcq_id': 99986656, 'issue': 'MISSING_CONDITION: ms'},
        {'mcq_id': 89723153, 'issue': 'MISSING_CONDITION: ms'},
        
        # Topic drift cases
        {'mcq_id': 33989838, 'issue': 'TOPIC_DRIFT: movement → dementia'},
        {'mcq_id': 62940617, 'issue': 'TOPIC_DRIFT: movement → dementia'},
        
        # Purpose mismatch cases (random examples from analysis)
        {'mcq_id': 98264238, 'issue': 'PURPOSE_MISMATCH: diagnosis → investigation'},
        {'mcq_id': 69236274, 'issue': 'PURPOSE_MISMATCH: diagnosis → management'},
        {'mcq_id': 95155123, 'issue': 'PURPOSE_MISMATCH with NON_CLINICAL_LANGUAGE'},
    ]
    
    results = []
    successful_fixes = 0
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n🧪 TEST {i}/{len(test_cases)}")
        success = test_specific_mcq_fix(test_case['mcq_id'], test_case['issue'])
        results.append(success)
        if success:
            successful_fixes += 1
    
    # Summary
    print(f"\n{'='*80}")
    print(f"📊 FIX VERIFICATION RESULTS")
    print(f"{'='*80}")
    print(f"🎯 Successful Fixes: {successful_fixes}/{len(test_cases)} ({successful_fixes/len(test_cases)*100:.1f}%)")
    
    if successful_fixes == len(test_cases):
        print(f"🎉 ALL FIXES SUCCESSFUL! The targeted improvements are working.")
    elif successful_fixes >= len(test_cases) * 0.8:
        print(f"✅ GOOD IMPROVEMENT! Most fixes are working, some refinement needed.")
    elif successful_fixes >= len(test_cases) * 0.5:
        print(f"⚠️ PARTIAL IMPROVEMENT! Some fixes working, more work needed.")
    else:
        print(f"❌ FIXES NOT EFFECTIVE! Need to revisit the implementation.")
    
    return results

if __name__ == "__main__":
    test_targeted_fixes()