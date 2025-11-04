#!/usr/bin/env python3
"""Script to analyze the final remaining unclassified MCQs."""
import os
import sys
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from mcq.models import MCQ

def analyze_final_unclassified():
    print("Analysis of Final Remaining Unclassified MCQs")
    print("=" * 40)
    
    # Get remaining unclassified MCQs
    unclassified_mcqs = MCQ.objects.filter(
        exam_type='Part II', 
        exam_year=2022,
        subspecialty='Other/Unclassified'
    )
    
    total_count = unclassified_mcqs.count()
    print(f"\nRemaining unclassified MCQs: {total_count}")
    
    # Detailed analysis of each remaining MCQ
    print("\nDetailed Analysis of Each MCQ:")
    
    for i, mcq in enumerate(unclassified_mcqs, 1):
        print(f"\n{i}. Question {mcq.question_number or 'Unknown'}")
        print(f"   Primary Category: {mcq.primary_category}")
        print(f"   Secondary Category: {mcq.secondary_category}")
        print(f"   Question Text: {mcq.question_text}")
        print(f"   Key Concept: {mcq.key_concept}")
        
        # Look for classification hints in explanation
        if mcq.explanation_sections:
            if 'classification_and_nosology' in mcq.explanation_sections:
                print(f"   Classification Info: {mcq.explanation_sections['classification_and_nosology'][:200]}...")
        
        print("-" * 40)

if __name__ == "__main__":
    analyze_final_unclassified()