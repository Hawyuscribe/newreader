#!/usr/bin/env python3
"""
Test MCQ-to-Case conversion accuracy
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

def test_mcq_conversion():
    """Test MCQ conversion accuracy"""
    
    print("🔍 Testing MCQ-to-Case conversion accuracy...")
    print("=" * 60)
    
    # Find MCQ about caudate atrophy
    mcqs = MCQ.objects.filter(question_text__icontains='caudate atrophy')[:1]
    if mcqs:
        mcq = mcqs[0]
        print(f"Testing MCQ {mcq.id}:")
        print(f"Question: {mcq.question_text}")
        print(f"Correct Answer: {mcq.correct_answer}")
        print("\n" + "="*60 + "\n")
        
        try:
            case_data = convert_mcq_to_case(mcq)
            clinical_presentation = case_data.get('clinical_presentation', '').lower()
            question_lower = mcq.question_text.lower()
            
            print("Generated Case Data:")
            for key, value in case_data.items():
                if isinstance(value, str) and len(value) > 100:
                    print(f"{key}: {value[:100]}...")
                else:
                    print(f"{key}: {value}")
            
            print("\n" + "="*60)
            print("VALIDATION CHECK:")
            
            # Check for key terms
            key_terms = ['caudate', 'huntington', 'atrophy', 'chorea']
            preserved_terms = []
            missing_terms = []
            
            for term in key_terms:
                if term in question_lower:
                    if term in clinical_presentation:
                        preserved_terms.append(term)
                    else:
                        missing_terms.append(term)
            
            if preserved_terms:
                print(f"✅ Preserved terms: {', '.join(preserved_terms)}")
            if missing_terms:
                print(f"❌ Missing terms: {', '.join(missing_terms)}")
            
            if missing_terms:
                print("\n⚠️ ISSUE: The generated case is not preserving key MCQ content!")
                print("The AI is generating generic cases instead of MCQ-specific ones.")
            else:
                print("\n✅ SUCCESS: The case properly preserves MCQ content!")
                
        except Exception as e:
            print(f"ERROR during conversion: {e}")
            import traceback
            traceback.print_exc()
    else:
        print("No MCQ found about caudate atrophy")
        
        # Look for any movement disorder MCQs
        print("\nLooking for movement disorder MCQs...")
        movement_mcqs = MCQ.objects.filter(question_text__icontains='huntington')[:3]
        
        for mcq in movement_mcqs:
            print(f"\nMCQ {mcq.id}: {mcq.question_text[:100]}...")
            print(f"Correct Answer: {mcq.correct_answer}")

if __name__ == "__main__":
    test_mcq_conversion()