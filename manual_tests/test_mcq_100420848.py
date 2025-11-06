#!/usr/bin/env python3
"""
Test specific MCQ 100420848 that was showing wrong case
"""
import os
import sys
import django

# Setup Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_neurology_mcq.mcq.settings')
django.setup()

from django_neurology_mcq.mcq.models import MCQ
from django_neurology_mcq.mcq.mcq_case_converter import convert_mcq_to_case, clear_mcq_cache
import json

def test_specific_mcq():
    """Test MCQ 100420848 that was showing peripheral neuropathy instead of Parkinson's"""
    mcq_id = 100420848
    print(f"Testing MCQ {mcq_id} - Previously showed wrong case (peripheral neuropathy instead of Parkinson's)")
    print("=" * 80)
    
    try:
        # Get the MCQ
        mcq = MCQ.objects.get(id=mcq_id)
        print(f"\nMCQ Found!")
        print(f"Question: {mcq.question_text[:200]}...")
        print(f"Subspecialty: {mcq.subspecialty}")
        
        # Clear cache to force regeneration
        clear_mcq_cache(mcq_id)
        print("\nCache cleared - forcing new conversion...")
        
        # Convert to case
        case_data = convert_mcq_to_case(mcq)
        
        # Check if it's about Parkinson's
        case_text = json.dumps(case_data).lower()
        has_parkinsons = 'parkinson' in case_text
        has_peripheral_neuropathy = 'peripheral neuropathy' in case_text
        
        print(f"\n✓ Conversion successful!")
        print(f"\nCase Analysis:")
        print(f"- Contains 'Parkinson': {has_parkinsons}")
        print(f"- Contains 'Peripheral Neuropathy': {has_peripheral_neuropathy}")
        print(f"\nCase Summary:")
        print(f"- Patient: {case_data.get('patient_demographics', 'N/A')}")
        print(f"- Core Concept: {case_data.get('core_concept_type', 'N/A')}")
        print(f"- Clinical Presentation: {case_data.get('clinical_presentation', 'N/A')[:200]}...")
        
        # Validation info
        if '_extended_data' in case_data and 'validation_metadata' in case_data['_extended_data']:
            validation = case_data['_extended_data']['validation_metadata']
            print(f"\nValidation:")
            print(f"- Status: {validation.get('status', 'N/A')}")
            print(f"- Score: {validation.get('score', 'N/A')}")
            
        if has_parkinsons and not has_peripheral_neuropathy:
            print("\n✅ SUCCESS: Case is correctly about Parkinson's disease!")
        else:
            print("\n❌ WARNING: Case may not be correctly aligned with the MCQ!")
            
    except MCQ.DoesNotExist:
        print(f"\nMCQ {mcq_id} not found in database")
    except Exception as e:
        print(f"\nError: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_specific_mcq()