#!/usr/bin/env python3
"""
Test MCQ-to-Case conversion accuracy with multiple random MCQs
"""

import os
import sys
import django
import random

# Setup Django
sys.path.append('/Users/tariqalmatrudi/NEWreader/django_neurology_mcq')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
django.setup()

from mcq.models import MCQ
from mcq.mcq_case_converter import convert_mcq_to_case

def extract_key_terms_from_question(question_text):
    """Extract important medical terms from question"""
    text = question_text.lower()
    key_terms = []
    
    # Medical conditions
    conditions = [
        'parkinson', 'huntington', 'alzheimer', 'epilepsy', 'seizure', 'stroke', 
        'migraine', 'headache', 'multiple sclerosis', 'ms', 'dementia',
        'caudate', 'atrophy', 'chorea', 'tremor', 'rigidity', 'bradykinesia',
        'weakness', 'paralysis', 'aphasia', 'dysarthria', 'dysphagia',
        'neuropathy', 'myopathy', 'guillain', 'gbs'
    ]
    
    # Anatomical locations
    locations = [
        'bilateral', 'left', 'right', 'frontal', 'temporal', 'parietal', 'occipital',
        'brainstem', 'cerebellum', 'spinal cord', 'caudate', 'putamen', 'thalamus'
    ]
    
    # Investigation findings
    investigations = [
        'ct', 'mri', 'eeg', 'emg', 'lumbar puncture', 'csf', 'oligoclonal'
    ]
    
    all_terms = conditions + locations + investigations
    
    for term in all_terms:
        if term in text:
            key_terms.append(term)
    
    return key_terms

def test_mcq_conversion(mcq):
    """Test single MCQ conversion"""
    print(f"\n{'='*80}")
    print(f"Testing MCQ {mcq.id}")
    print(f"Question: {mcq.question_text}")
    print(f"Correct Answer: {mcq.correct_answer}")
    print(f"{'='*80}")
    
    # Extract key terms from original question
    original_key_terms = extract_key_terms_from_question(mcq.question_text)
    print(f"🔍 Key terms to preserve: {', '.join(original_key_terms)}")
    
    try:
        # Convert MCQ to case
        case_data = convert_mcq_to_case(mcq)
        
        # Get clinical presentation
        clinical_presentation = case_data.get('clinical_presentation', '').lower()
        question_lower = mcq.question_text.lower()
        
        print(f"\n📋 Generated Case Data:")
        for key, value in case_data.items():
            if key == 'clinical_presentation':
                print(f"  {key}: {value}")
            elif isinstance(value, str) and len(value) > 80:
                print(f"  {key}: {value[:80]}...")
            else:
                print(f"  {key}: {value}")
        
        print(f"\n🔍 VALIDATION RESULTS:")
        
        # Check preservation of key terms
        preserved_terms = []
        missing_terms = []
        
        for term in original_key_terms:
            if term in clinical_presentation:
                preserved_terms.append(term)
            else:
                missing_terms.append(term)
        
        if preserved_terms:
            print(f"  ✅ Preserved terms: {', '.join(preserved_terms)}")
        if missing_terms:
            print(f"  ❌ Missing terms: {', '.join(missing_terms)}")
        
        # Overall assessment
        if len(original_key_terms) == 0:
            print(f"  ⚠️ No specific key terms found in original question")
            return "unclear"
        elif len(missing_terms) == 0:
            print(f"  ✅ SUCCESS: All key terms preserved!")
            return "success"
        elif len(preserved_terms) > len(missing_terms):
            print(f"  ⚠️ PARTIAL: Most terms preserved but some missing")
            return "partial"
        else:
            print(f"  ❌ FAILURE: Many key terms missing")
            return "failure"
            
    except Exception as e:
        print(f"  ❌ ERROR during conversion: {e}")
        import traceback
        traceback.print_exc()
        return "error"

def test_multiple_mcqs():
    """Test MCQ conversion with 4 different random MCQs"""
    
    print("🧪 Testing MCQ-to-Case Conversion Accuracy")
    print("Testing with 4 random MCQs to verify fixes are working...")
    
    # Get 4 random MCQs from different subspecialties
    all_mcqs = list(MCQ.objects.all())
    
    if len(all_mcqs) < 4:
        print("❌ Not enough MCQs in database for testing")
        return
    
    # Try to get diverse MCQs
    random.seed(42)  # For reproducible results
    test_mcqs = random.sample(all_mcqs, min(20, len(all_mcqs)))  # Sample 20 and pick 4 diverse ones
    
    # Filter for diverse content
    selected_mcqs = []
    keywords_used = set()
    
    for mcq in test_mcqs:
        question_lower = mcq.question_text.lower()
        # Check if this MCQ has different content from already selected ones
        current_keywords = set(extract_key_terms_from_question(mcq.question_text))
        
        if len(selected_mcqs) < 4 and (not keywords_used or not current_keywords.intersection(keywords_used)):
            selected_mcqs.append(mcq)
            keywords_used.update(current_keywords)
    
    # If we don't have 4 diverse ones, just take the first 4
    if len(selected_mcqs) < 4:
        selected_mcqs = test_mcqs[:4]
    
    results = []
    
    # Test each MCQ
    for i, mcq in enumerate(selected_mcqs, 1):
        print(f"\n🔬 TEST {i}/4")
        result = test_mcq_conversion(mcq)
        results.append(result)
    
    # Summary
    print(f"\n{'='*80}")
    print(f"📊 SUMMARY OF RESULTS")
    print(f"{'='*80}")
    
    success_count = results.count("success")
    partial_count = results.count("partial") 
    failure_count = results.count("failure")
    error_count = results.count("error")
    unclear_count = results.count("unclear")
    
    print(f"✅ Success: {success_count}/4 ({success_count/4*100:.0f}%)")
    print(f"⚠️ Partial: {partial_count}/4 ({partial_count/4*100:.0f}%)")
    print(f"❌ Failure: {failure_count}/4 ({failure_count/4*100:.0f}%)")
    print(f"🚫 Errors: {error_count}/4 ({error_count/4*100:.0f}%)")
    print(f"❓ Unclear: {unclear_count}/4 ({unclear_count/4*100:.0f}%)")
    
    total_acceptable = success_count + partial_count
    print(f"\n🎯 Overall Performance: {total_acceptable}/4 ({total_acceptable/4*100:.0f}%) acceptable")
    
    if total_acceptable >= 3:
        print("🎉 GOOD: MCQ conversion is working well!")
    elif total_acceptable >= 2:
        print("⚠️ OKAY: MCQ conversion needs some improvement")
    else:
        print("❌ POOR: MCQ conversion needs significant fixes")

if __name__ == "__main__":
    test_multiple_mcqs()