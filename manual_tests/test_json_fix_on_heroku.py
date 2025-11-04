#!/usr/bin/env python3
"""
Test MCQ conversion after JSON serialization fix
"""
import os
import sys
import django

# Setup Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mcq.settings')
django.setup()

from mcq.models import MCQ, MCQCaseConversionSession
from mcq.mcq_case_converter import convert_mcq_to_case
from django.contrib.auth.models import User
import random
import json

def test_mcq_conversion():
    """Test a random MCQ conversion"""
    print("Testing MCQ conversion after JSON serialization fix...")
    print("=" * 80)
    
    # Get a random MCQ
    mcqs = MCQ.objects.filter(subspecialty='Movement Disorders')[:10]
    if not mcqs:
        mcqs = MCQ.objects.all()[:10]
    
    if not mcqs:
        print("No MCQs found in database!")
        return
    
    # Pick a random MCQ
    mcq = random.choice(mcqs)
    print(f"\nSelected MCQ ID: {mcq.id}")
    print(f"Subspecialty: {mcq.subspecialty}")
    print(f"Question preview: {mcq.question_text[:100]}...")
    
    # Clear any cache for this MCQ
    from mcq.mcq_case_converter import clear_mcq_cache
    clear_mcq_cache(mcq.id)
    print("\nCleared cache for this MCQ")
    
    # Test conversion
    print("\nAttempting conversion...")
    try:
        case_data = convert_mcq_to_case(mcq)
        print("\n✓ Conversion successful!")
        
        # Check for validation metadata
        if '_extended_data' in case_data and 'validation_metadata' in case_data['_extended_data']:
            validation = case_data['_extended_data']['validation_metadata']
            print(f"\nValidation Details:")
            print(f"- Status: {validation.get('status', 'N/A')}")
            print(f"- Score: {validation.get('score', 'N/A')}")
            print(f"- Reason: {validation.get('reason', 'N/A')}")
        
        # Test JSON serialization
        print("\nTesting JSON serialization...")
        json_str = json.dumps(case_data, indent=2)
        print("✓ JSON serialization successful!")
        
        # Show case summary
        print(f"\nCase Summary:")
        print(f"- Patient: {case_data.get('patient_demographics', 'N/A')}")
        print(f"- Specialty: {case_data.get('specialty', 'N/A')}")
        print(f"- Question Type: {case_data.get('question_type', 'N/A')}")
        print(f"- Core Concept: {case_data.get('core_concept_type', 'N/A')}")
        
    except Exception as e:
        print(f"\n✗ Conversion failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_mcq_conversion()