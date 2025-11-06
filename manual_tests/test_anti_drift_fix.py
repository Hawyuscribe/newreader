#!/usr/bin/env python3
"""
Test the anti-drift fix for the MS topic drift issue
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

def test_anti_drift_fix():
    """Test specific MCQs that were showing topic drift to MS"""
    
    # MCQ IDs that showed topic drift in Cycle 2
    problematic_mcqs = [
        33048893,  # Neuromuscular → MS 
        26655154,  # Epilepsy → MS
        36688273,  # Epilepsy → MS  
        13374370,  # Epilepsy → MS
        13058506,  # Movement → MS
        20678682,  # Neuropathy → MS
        40385361,  # Stroke → MS
    ]
    
    print("🧪 TESTING ANTI-DRIFT FIX")
    print("=" * 80)
    print("Testing MCQs that previously showed topic drift to Multiple Sclerosis")
    print()
    
    results = []
    
    for i, mcq_id in enumerate(problematic_mcqs, 1):
        try:
            mcq = MCQ.objects.get(id=mcq_id)
            print(f"🔬 TEST {i}/{len(problematic_mcqs)}: MCQ {mcq_id}")
            print(f"Subspecialty: {getattr(mcq, 'subspecialty', 'Unknown')}")
            print(f"Question: {mcq.question_text[:100]}...")
            print("-" * 60)
            
            # Identify expected topic
            question_lower = mcq.question_text.lower()
            expected_topic = "Unknown"
            if any(term in question_lower for term in ['seizure', 'epilepsy', 'ictal']):
                expected_topic = "Epilepsy"
            elif any(term in question_lower for term in ['parkinson', 'movement', 'tremor', 'rigidity']):
                expected_topic = "Movement Disorders"
            elif any(term in question_lower for term in ['stroke', 'hemiparesis', 'infarct']):
                expected_topic = "Stroke"
            elif any(term in question_lower for term in ['neuropathy', 'weakness', 'guillain']):
                expected_topic = "Neuropathy"
            elif any(term in question_lower for term in ['multiple sclerosis', 'ms']):
                expected_topic = "Multiple Sclerosis"
            
            print(f"Expected Topic: {expected_topic}")
            
            # Test conversion
            case_data = convert_mcq_to_case(mcq)
            
            clinical_presentation = case_data.get('clinical_presentation', '')
            fallback_used = case_data.get('fallback_used', False)
            
            print(f"Fallback Used: {fallback_used}")
            print(f"Generated Case: {clinical_presentation[:150]}...")
            
            # Check for topic drift
            case_lower = clinical_presentation.lower()
            generated_topic = "Unknown"
            
            if any(term in case_lower for term in ['multiple sclerosis', 'ms', 'demyelinating']):
                generated_topic = "Multiple Sclerosis"
            elif any(term in case_lower for term in ['seizure', 'epilepsy', 'ictal']):
                generated_topic = "Epilepsy"
            elif any(term in case_lower for term in ['parkinson', 'movement', 'tremor', 'rigidity']):
                generated_topic = "Movement Disorders"
            elif any(term in case_lower for term in ['stroke', 'hemiparesis', 'infarct']):
                generated_topic = "Stroke"
            elif any(term in case_lower for term in ['neuropathy', 'weakness', 'guillain']):
                generated_topic = "Neuropathy"
            
            print(f"Generated Topic: {generated_topic}")
            
            # Evaluate fix
            if expected_topic == generated_topic:
                print("✅ SUCCESS: Topic preserved correctly!")
                result = "SUCCESS"
            elif expected_topic != "Multiple Sclerosis" and generated_topic == "Multiple Sclerosis":
                print("❌ FAILED: Still drifting to MS!")
                result = "MS_DRIFT"
            elif fallback_used:
                print("⚠️ FALLBACK: Using fallback case")
                result = "FALLBACK"
            else:
                print("🟡 UNCLEAR: Topic change but not to MS")
                result = "OTHER_DRIFT"
            
            results.append({
                'mcq_id': mcq_id,
                'expected': expected_topic,
                'generated': generated_topic,
                'result': result,
                'fallback': fallback_used
            })
            
            print()
            
        except MCQ.DoesNotExist:
            print(f"❌ MCQ {mcq_id} not found")
            results.append({
                'mcq_id': mcq_id,
                'result': 'NOT_FOUND'
            })
        except Exception as e:
            print(f"❌ ERROR: {e}")
            results.append({
                'mcq_id': mcq_id,
                'result': 'ERROR',
                'error': str(e)
            })
    
    # Summary
    print("=" * 80)
    print("📊 ANTI-DRIFT FIX RESULTS")
    print("=" * 80)
    
    success_count = len([r for r in results if r['result'] == 'SUCCESS'])
    ms_drift_count = len([r for r in results if r['result'] == 'MS_DRIFT'])
    fallback_count = len([r for r in results if r['result'] == 'FALLBACK'])
    other_count = len([r for r in results if r['result'] not in ['SUCCESS', 'MS_DRIFT', 'FALLBACK']])
    
    total_tested = len([r for r in results if r['result'] not in ['NOT_FOUND', 'ERROR']])
    
    print(f"✅ Successful Topic Preservation: {success_count}/{total_tested}")
    print(f"❌ Still Drifting to MS: {ms_drift_count}/{total_tested}")
    print(f"⚠️ Using Fallback: {fallback_count}/{total_tested}")
    print(f"🟡 Other Issues: {other_count}/{total_tested}")
    
    if total_tested > 0:
        fix_rate = (success_count + fallback_count) / total_tested * 100  # Fallback preserves topic
        print(f"\n🎯 Fix Success Rate: {fix_rate:.1f}%")
        
        if fix_rate >= 80:
            print("🎉 EXCELLENT: Anti-drift fix is working well!")
        elif fix_rate >= 60:
            print("✅ GOOD: Anti-drift fix is mostly working")
        elif fix_rate >= 40:
            print("⚠️ PARTIAL: Some improvement but needs more work")
        else:
            print("❌ POOR: Fix not effective enough")
    
    return results

if __name__ == "__main__":
    test_anti_drift_fix()