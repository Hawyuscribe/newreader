#!/usr/bin/env python3
"""
Direct test of MCQ conversion on Heroku
Run this with: heroku run python test_mcq_on_heroku_direct.py --app radiant-gorge-35079
"""

import os
import sys
import django
import json
import random

# Setup Django
sys.path.append('/app')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_neurology_mcq.mcq.settings')
django.setup()

from django_neurology_mcq.mcq.models import MCQ
from django_neurology_mcq.mcq.mcq_case_converter import convert_mcq_to_case, clear_mcq_cache

def test_random_mcq_conversion():
    print("=" * 80)
    print("Testing Random MCQ Conversion on Heroku Production")
    print("=" * 80)
    
    # Get a random MCQ (excluding the problematic one we already fixed)
    mcqs = MCQ.objects.exclude(id=100420848).order_by('?')[:5]
    
    if not mcqs:
        print("No MCQs found!")
        return
    
    # Pick a random one
    mcq = mcqs[0]
    
    print(f"\nSelected MCQ:")
    print(f"- ID: {mcq.id}")
    print(f"- Subspecialty: {mcq.subspecialty}")
    print(f"- Exam Type: {mcq.exam_type}")
    print(f"- Question: {mcq.question_text[:150]}...")
    
    # Clear cache to force fresh conversion
    print("\nClearing cache...")
    clear_mcq_cache(mcq.id)
    
    # Test conversion
    print("\nStarting conversion...")
    try:
        case_data = convert_mcq_to_case(mcq)
        
        print("\n✅ CONVERSION SUCCESSFUL!")
        
        # Display case summary
        print("\nCase Summary:")
        print(f"- Patient: {case_data.get('patient_demographics', 'N/A')}")
        print(f"- Specialty: {case_data.get('specialty', 'N/A')}")
        print(f"- Question Type: {case_data.get('question_type', 'N/A')}")
        print(f"- Core Concept: {case_data.get('core_concept_type', 'N/A')}")
        print(f"- Clinical Presentation: {case_data.get('clinical_presentation', 'N/A')[:200]}...")
        
        # Check validation
        if 'professional_validation' in case_data:
            val = case_data['professional_validation']
            print(f"\nValidation:")
            print(f"- Passed: {val.get('passed', 'N/A')}")
            print(f"- Score: {val.get('score', 'N/A')}")
            print(f"- Method: {val.get('method', 'N/A')}")
        
        # Verify JSON serialization works
        print("\nTesting JSON serialization...")
        json_str = json.dumps(case_data)
        print(f"✅ JSON serialization successful ({len(json_str)} characters)")
        
        # Check if content matches MCQ topic
        case_text = json.dumps(case_data).lower()
        mcq_text = mcq.question_text.lower()
        
        # Find common medical terms
        medical_terms = ['parkinson', 'alzheimer', 'seizure', 'stroke', 'migraine', 
                        'neuropathy', 'dementia', 'epilepsy', 'tremor', 'weakness']
        
        mcq_terms = [term for term in medical_terms if term in mcq_text]
        case_terms = [term for term in medical_terms if term in case_text]
        
        print(f"\nContent Alignment Check:")
        print(f"- MCQ contains: {mcq_terms if mcq_terms else 'No specific terms found'}")
        print(f"- Case contains: {case_terms if case_terms else 'No specific terms found'}")
        
        if mcq_terms and any(term in case_terms for term in mcq_terms):
            print("✅ Case content aligns with MCQ topic!")
        else:
            print("⚠️  Case may not perfectly align with MCQ topic")
        
    except Exception as e:
        print(f"\n❌ CONVERSION FAILED!")
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
    
    print("\n" + "=" * 80)
    print("Test Complete")

if __name__ == "__main__":
    test_random_mcq_conversion()