#!/usr/bin/env python3
"""
Test MCQ-to-Case conversion accuracy with specific trusted MCQs from local database
"""

import os
import sys
import django

# Setup Django
sys.path.append('/Users/tariqalmatrudi/NEWreader/django_neurology_mcq')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
django.setup()

from mcq.models import MCQ
from mcq.mcq_case_converter import convert_mcq_to_case

def test_specific_mcq(mcq_id, expected_keywords):
    """Test a specific MCQ and validate key terms are preserved"""
    try:
        mcq = MCQ.objects.get(id=mcq_id)
    except MCQ.DoesNotExist:
        print(f"❌ MCQ {mcq_id} not found in database")
        return "not_found"
    
    print(f"\n{'='*100}")
    print(f"🔬 Testing MCQ {mcq.id}")
    print(f"Question: {mcq.question_text}")
    print(f"Correct Answer: {mcq.correct_answer}")
    print(f"Expected Keywords: {', '.join(expected_keywords)}")
    print(f"{'='*100}")
    
    try:
        # Convert MCQ to case
        case_data = convert_mcq_to_case(mcq)
        
        # Get clinical presentation
        clinical_presentation = case_data.get('clinical_presentation', '').lower()
        
        print(f"\n📋 Generated Case:")
        print(f"Clinical Presentation: {case_data.get('clinical_presentation', 'None')}")
        print(f"Patient Demographics: {case_data.get('patient_demographics', 'None')}")
        print(f"Question Type: {case_data.get('question_type', 'None')}")
        
        if case_data.get('fallback_used'):
            print(f"⚠️ FALLBACK USED - AI generation failed, using simple fallback")
        
        print(f"\n🔍 KEYWORD VALIDATION:")
        
        # Check preservation of expected keywords
        preserved_keywords = []
        missing_keywords = []
        
        for keyword in expected_keywords:
            keyword_lower = keyword.lower()
            if keyword_lower in clinical_presentation:
                preserved_keywords.append(keyword)
            else:
                missing_keywords.append(keyword)
        
        if preserved_keywords:
            print(f"  ✅ Preserved: {', '.join(preserved_keywords)}")
        if missing_keywords:
            print(f"  ❌ Missing: {', '.join(missing_keywords)}")
        
        # Calculate score
        if len(expected_keywords) == 0:
            score = "N/A"
            result = "unclear"
        else:
            preservation_rate = len(preserved_keywords) / len(expected_keywords)
            score = f"{preservation_rate*100:.0f}%"
            
            if preservation_rate >= 0.8:
                result = "excellent"
                print(f"  🎉 EXCELLENT: {score} of keywords preserved!")
            elif preservation_rate >= 0.6:
                result = "good"
                print(f"  ✅ GOOD: {score} of keywords preserved")
            elif preservation_rate >= 0.4:
                result = "partial"
                print(f"  ⚠️ PARTIAL: {score} of keywords preserved")
            else:
                result = "poor"
                print(f"  ❌ POOR: Only {score} of keywords preserved")
        
        return result
            
    except Exception as e:
        print(f"  ❌ ERROR during conversion: {e}")
        import traceback
        traceback.print_exc()
        return "error"

def find_trusted_mcqs():
    """Find specific MCQs with clear medical content for testing"""
    
    print("🔍 Searching for trusted MCQs in your database...")
    
    # Look for MCQs with specific medical terms
    test_cases = []
    
    # Test case 1: Huntington's disease / Caudate atrophy
    huntington_mcqs = MCQ.objects.filter(
        question_text__icontains='caudate'
    ).filter(
        question_text__icontains='atrophy'
    )[:1]
    
    if huntington_mcqs:
        test_cases.append({
            'mcq_id': huntington_mcqs[0].id,
            'keywords': ['caudate', 'atrophy', 'bilateral'],
            'description': 'Huntington disease / Caudate atrophy'
        })
    
    # Test case 2: Parkinson's disease
    parkinson_mcqs = MCQ.objects.filter(
        question_text__icontains='parkinson'
    )[:1]
    
    if parkinson_mcqs:
        test_cases.append({
            'mcq_id': parkinson_mcqs[0].id,
            'keywords': ['parkinson', 'tremor', 'rigidity'],
            'description': 'Parkinson disease'
        })
    
    # Test case 3: Stroke
    stroke_mcqs = MCQ.objects.filter(
        question_text__icontains='stroke'
    ).filter(
        question_text__icontains='ischemic'
    )[:1]
    
    if stroke_mcqs:
        test_cases.append({
            'mcq_id': stroke_mcqs[0].id,
            'keywords': ['stroke', 'ischemic'],
            'description': 'Ischemic stroke'
        })
    
    # Test case 4: Epilepsy/Seizure
    epilepsy_mcqs = MCQ.objects.filter(
        question_text__icontains='seizure'
    )[:1]
    
    if epilepsy_mcqs:
        test_cases.append({
            'mcq_id': epilepsy_mcqs[0].id,
            'keywords': ['seizure', 'epilepsy'],
            'description': 'Seizure/Epilepsy'
        })
    
    # Test case 5: Multiple Sclerosis
    ms_mcqs = MCQ.objects.filter(
        question_text__icontains='multiple sclerosis'
    )[:1]
    
    if ms_mcqs:
        test_cases.append({
            'mcq_id': ms_mcqs[0].id,
            'keywords': ['multiple sclerosis', 'demyelinating'],
            'description': 'Multiple Sclerosis'
        })
    
    # If we don't have enough specific ones, add some general neurological MCQs
    if len(test_cases) < 4:
        # Look for MCQs with clear neurological terms
        neuro_terms = ['weakness', 'neuropathy', 'headache', 'migraine', 'tremor']
        for term in neuro_terms:
            if len(test_cases) >= 4:
                break
            mcqs = MCQ.objects.filter(question_text__icontains=term)[:1]
            if mcqs and mcqs[0].id not in [tc['mcq_id'] for tc in test_cases]:
                test_cases.append({
                    'mcq_id': mcqs[0].id,
                    'keywords': [term],
                    'description': f'{term.title()} related'
                })
    
    return test_cases

def run_trusted_mcq_tests():
    """Run tests on trusted MCQs from local database"""
    
    print("🧪 Testing MCQ-to-Case Conversion with Trusted Questions")
    print("=" * 100)
    
    # Find trusted MCQs
    test_cases = find_trusted_mcqs()
    
    if not test_cases:
        print("❌ No suitable MCQs found for testing")
        return
    
    print(f"Found {len(test_cases)} trusted MCQs for testing:")
    for i, case in enumerate(test_cases, 1):
        print(f"  {i}. {case['description']} (MCQ {case['mcq_id']})")
    
    results = []
    
    # Test each MCQ
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n🔬 TEST {i}/{len(test_cases)}: {test_case['description']}")
        result = test_specific_mcq(test_case['mcq_id'], test_case['keywords'])
        results.append({
            'description': test_case['description'],
            'result': result,
            'mcq_id': test_case['mcq_id']
        })
    
    # Summary
    print(f"\n{'='*100}")
    print(f"📊 FINAL RESULTS SUMMARY")
    print(f"{'='*100}")
    
    excellent_count = len([r for r in results if r['result'] == 'excellent'])
    good_count = len([r for r in results if r['result'] == 'good'])
    partial_count = len([r for r in results if r['result'] == 'partial'])
    poor_count = len([r for r in results if r['result'] == 'poor'])
    error_count = len([r for r in results if r['result'] == 'error'])
    not_found_count = len([r for r in results if r['result'] == 'not_found'])
    
    total_tests = len(results)
    
    print(f"🎉 Excellent (≥80% keywords): {excellent_count}/{total_tests}")
    print(f"✅ Good (≥60% keywords): {good_count}/{total_tests}")
    print(f"⚠️ Partial (≥40% keywords): {partial_count}/{total_tests}")
    print(f"❌ Poor (<40% keywords): {poor_count}/{total_tests}")
    print(f"🚫 Errors: {error_count}/{total_tests}")
    print(f"❓ Not Found: {not_found_count}/{total_tests}")
    
    acceptable_count = excellent_count + good_count
    success_rate = acceptable_count / total_tests * 100 if total_tests > 0 else 0
    
    print(f"\n🎯 Overall Success Rate: {acceptable_count}/{total_tests} ({success_rate:.0f}%)")
    
    # Detailed results
    print(f"\n📋 Detailed Results:")
    for result in results:
        status_emoji = {
            'excellent': '🎉',
            'good': '✅', 
            'partial': '⚠️',
            'poor': '❌',
            'error': '🚫',
            'not_found': '❓'
        }.get(result['result'], '❓')
        
        print(f"  {status_emoji} {result['description']} (MCQ {result['mcq_id']}): {result['result']}")
    
    # Final assessment
    if success_rate >= 75:
        print(f"\n🎉 EXCELLENT: MCQ conversion is working very well!")
        print("The fixes have significantly improved content preservation.")
    elif success_rate >= 50:
        print(f"\n✅ GOOD: MCQ conversion is working well!")
        print("Most cases preserve the original MCQ content properly.")
    elif success_rate >= 25:
        print(f"\n⚠️ NEEDS IMPROVEMENT: Some cases still lose content")
        print("Further refinement of validation logic may be needed.")
    else:
        print(f"\n❌ POOR: Major issues with content preservation")
        print("The conversion system needs significant fixes.")

if __name__ == "__main__":
    run_trusted_mcq_tests()