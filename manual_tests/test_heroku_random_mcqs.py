#!/usr/bin/env python3
"""
Test MCQ-to-Case conversion with 5 random MCQs from Heroku database
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

def extract_medical_terms(question_text):
    """Extract important medical terms from question for validation"""
    text = question_text.lower()
    
    # Medical conditions and symptoms
    medical_terms = [
        'stroke', 'seizure', 'epilepsy', 'parkinson', 'huntington', 'alzheimer',
        'multiple sclerosis', 'ms', 'migraine', 'headache', 'neuropathy', 'myopathy',
        'weakness', 'paralysis', 'tremor', 'rigidity', 'chorea', 'dystonia',
        'ataxia', 'aphasia', 'dysarthria', 'dysphagia', 'diplopia',
        'dementia', 'cognitive', 'memory', 'confusion',
        'bilateral', 'left', 'right', 'frontal', 'temporal', 'parietal',
        'brainstem', 'cerebellum', 'spinal', 'caudate', 'putamen',
        'ct', 'mri', 'eeg', 'emg', 'csf', 'lumbar puncture',
        'surgery', 'surgical', 'cabg', 'bypass', 'cardiac',
        'hypertension', 'diabetes', 'atrial fibrillation'
    ]
    
    found_terms = []
    for term in medical_terms:
        if term in text:
            found_terms.append(term)
    
    return found_terms

def test_random_heroku_mcq(mcq):
    """Test a single random MCQ from Heroku database"""
    print(f"\n{'='*100}")
    print(f"🔬 Testing MCQ {mcq.id} from Heroku Database")
    print(f"Question: {mcq.question_text}")
    print(f"Correct Answer: {mcq.correct_answer}")
    print(f"Subspecialty: {getattr(mcq, 'subspecialty', 'Unknown')}")
    print(f"{'='*100}")
    
    # Extract expected medical terms
    expected_terms = extract_medical_terms(mcq.question_text)
    print(f"🔍 Key medical terms to preserve: {', '.join(expected_terms) if expected_terms else 'None specific'}")
    
    try:
        # Convert MCQ to case
        case_data = convert_mcq_to_case(mcq)
        
        # Extract case details
        clinical_presentation = case_data.get('clinical_presentation', '')
        patient_demographics = case_data.get('patient_demographics', '')
        question_type = case_data.get('question_type', '')
        fallback_used = case_data.get('fallback_used', False)
        
        print(f"\n📋 Generated Case:")
        print(f"  Question Type: {question_type}")
        print(f"  Patient Demographics: {patient_demographics}")
        print(f"  Clinical Presentation: {clinical_presentation}")
        
        if fallback_used:
            print(f"  ⚠️ FALLBACK USED - AI generation failed, using simple fallback")
        else:
            print(f"  ✅ AI GENERATION SUCCESS")
        
        # Validate term preservation
        if expected_terms:
            presentation_lower = clinical_presentation.lower()
            preserved_terms = [term for term in expected_terms if term in presentation_lower]
            missing_terms = [term for term in expected_terms if term not in presentation_lower]
            
            print(f"\n🔍 KEYWORD VALIDATION:")
            if preserved_terms:
                print(f"  ✅ Preserved: {', '.join(preserved_terms)}")
            if missing_terms:
                print(f"  ❌ Missing: {', '.join(missing_terms)}")
            
            # Calculate score
            if len(expected_terms) > 0:
                preservation_rate = len(preserved_terms) / len(expected_terms)
                score_pct = preservation_rate * 100
                
                print(f"  📊 Preservation Score: {score_pct:.0f}% ({len(preserved_terms)}/{len(expected_terms)})")
                
                if preservation_rate >= 0.8:
                    result = "excellent"
                    print(f"  🎉 EXCELLENT: High term preservation!")
                elif preservation_rate >= 0.6:
                    result = "good"
                    print(f"  ✅ GOOD: Most terms preserved")
                elif preservation_rate >= 0.4:
                    result = "partial"
                    print(f"  ⚠️ PARTIAL: Some terms preserved")
                else:
                    result = "poor"
                    print(f"  ❌ POOR: Few terms preserved")
            else:
                result = "no_terms"
                print(f"  ℹ️ No specific medical terms identified for validation")
        else:
            result = "no_terms"
            print(f"\n🔍 No specific medical terms found for validation")
        
        # Check for quality indicators
        quality_indicators = []
        if len(clinical_presentation) > 50:
            quality_indicators.append("Good length")
        if any(word in clinical_presentation.lower() for word in ['presents', 'history', 'examination', 'symptoms']):
            quality_indicators.append("Clinical language")
        if any(char.isdigit() for char in clinical_presentation):
            quality_indicators.append("Specific details")
        
        if quality_indicators:
            print(f"  💡 Quality indicators: {', '.join(quality_indicators)}")
        
        return {
            'mcq_id': mcq.id,
            'result': result,
            'preservation_rate': preservation_rate if expected_terms else 1.0,
            'fallback_used': fallback_used,
            'has_content': len(clinical_presentation.strip()) > 10
        }
        
    except Exception as e:
        print(f"  ❌ ERROR during conversion: {e}")
        import traceback
        traceback.print_exc()
        return {
            'mcq_id': mcq.id,
            'result': 'error',
            'preservation_rate': 0.0,
            'fallback_used': False,
            'has_content': False
        }

def test_heroku_random_mcqs():
    """Test 5 random MCQs from Heroku database"""
    
    print("🧪 Testing MCQ-to-Case Conversion with 5 Random Heroku MCQs")
    print("=" * 100)
    
    # Get all MCQ IDs and sample 5 random ones
    all_mcq_ids = list(MCQ.objects.values_list('id', flat=True))
    
    if len(all_mcq_ids) < 5:
        print(f"❌ Only {len(all_mcq_ids)} MCQs found in database, need at least 5")
        return
    
    # Sample 5 random MCQs
    random.seed(42)  # For reproducible results
    selected_ids = random.sample(all_mcq_ids, 5)
    
    print(f"📊 Database contains {len(all_mcq_ids)} MCQs total")
    print(f"🎲 Testing 5 randomly selected MCQs: {', '.join(map(str, selected_ids))}")
    
    results = []
    
    # Test each selected MCQ
    for i, mcq_id in enumerate(selected_ids, 1):
        try:
            mcq = MCQ.objects.get(id=mcq_id)
            print(f"\n🔬 TEST {i}/5")
            result = test_random_heroku_mcq(mcq)
            results.append(result)
        except MCQ.DoesNotExist:
            print(f"\n🔬 TEST {i}/5")
            print(f"❌ MCQ {mcq_id} not found in database")
            results.append({
                'mcq_id': mcq_id,
                'result': 'not_found',
                'preservation_rate': 0.0,
                'fallback_used': False,
                'has_content': False
            })
    
    # Summary
    print(f"\n{'='*100}")
    print(f"📊 FINAL RESULTS SUMMARY - 5 Random Heroku MCQs")
    print(f"{'='*100}")
    
    # Count results
    excellent_count = len([r for r in results if r['result'] == 'excellent'])
    good_count = len([r for r in results if r['result'] == 'good'])
    partial_count = len([r for r in results if r['result'] == 'partial'])
    poor_count = len([r for r in results if r['result'] == 'poor'])
    no_terms_count = len([r for r in results if r['result'] == 'no_terms'])
    error_count = len([r for r in results if r['result'] == 'error'])
    not_found_count = len([r for r in results if r['result'] == 'not_found'])
    
    # Performance metrics
    successful_conversions = len([r for r in results if r['has_content']])
    fallback_count = len([r for r in results if r['fallback_used']])
    ai_success_count = successful_conversions - fallback_count
    
    print(f"🎯 Conversion Success Rate: {successful_conversions}/5 ({successful_conversions/5*100:.0f}%)")
    print(f"🤖 AI Generation Success: {ai_success_count}/5 ({ai_success_count/5*100:.0f}%)")
    print(f"🔄 Fallback Usage: {fallback_count}/5 ({fallback_count/5*100:.0f}%)")
    
    print(f"\n📈 Content Preservation Quality:")
    print(f"🎉 Excellent (≥80% terms): {excellent_count}/5")
    print(f"✅ Good (≥60% terms): {good_count}/5")
    print(f"⚠️ Partial (≥40% terms): {partial_count}/5")
    print(f"❌ Poor (<40% terms): {poor_count}/5")
    print(f"ℹ️ No specific terms: {no_terms_count}/5")
    print(f"🚫 Errors: {error_count}/5")
    print(f"❓ Not found: {not_found_count}/5")
    
    # Average preservation rate
    valid_results = [r for r in results if r['result'] not in ['error', 'not_found']]
    if valid_results:
        avg_preservation = sum(r['preservation_rate'] for r in valid_results) / len(valid_results)
        print(f"\n📊 Average Term Preservation: {avg_preservation*100:.1f}%")
    
    # Overall assessment
    acceptable_count = excellent_count + good_count + no_terms_count  # no_terms is acceptable if no specific terms
    success_rate = acceptable_count / 5 * 100
    
    print(f"\n🎯 Overall Assessment:")
    if success_rate >= 80:
        print(f"🎉 EXCELLENT ({success_rate:.0f}%): MCQ conversion is working very well!")
        print("The system successfully preserves medical content and generates quality cases.")
    elif success_rate >= 60:
        print(f"✅ GOOD ({success_rate:.0f}%): MCQ conversion is working well!")
        print("Most cases preserve important medical content properly.")
    elif success_rate >= 40:
        print(f"⚠️ ACCEPTABLE ({success_rate:.0f}%): MCQ conversion is working reasonably well")
        print("Some improvement in content preservation could be beneficial.")
    else:
        print(f"❌ NEEDS IMPROVEMENT ({success_rate:.0f}%): Content preservation needs work")
    
    print(f"\n📋 Detailed Results:")
    for i, result in enumerate(results, 1):
        status_emoji = {
            'excellent': '🎉',
            'good': '✅',
            'partial': '⚠️',
            'poor': '❌',
            'no_terms': 'ℹ️',
            'error': '🚫',
            'not_found': '❓'
        }.get(result['result'], '❓')
        
        fallback_indicator = " (Fallback)" if result['fallback_used'] else " (AI Generated)"
        content_indicator = fallback_indicator if result['has_content'] else " (No Content)"
        
        print(f"  {status_emoji} Test {i} (MCQ {result['mcq_id']}): {result['result']}{content_indicator}")

if __name__ == "__main__":
    test_heroku_random_mcqs()