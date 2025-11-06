#!/usr/bin/env python3
"""Script to verify the imported MCQs from Part II 2022."""
import os
import sys
import django
from collections import Counter

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from mcq.models import MCQ

def verify_import():
    print("Verification of Part II 2022 MCQ Import")
    print("=" * 40)
    
    # Get Part II 2022 MCQs
    part_ii_2022_mcqs = MCQ.objects.filter(exam_type='Part II', exam_year=2022)
    total_count = part_ii_2022_mcqs.count()
    
    print(f"\nTotal Part II 2022 MCQs: {total_count}")
    
    # Count by subspecialty
    subspecialty_counts = Counter(part_ii_2022_mcqs.values_list('subspecialty', flat=True))
    print("\nMCQs by Subspecialty:")
    for subspecialty, count in subspecialty_counts.most_common():
        print(f"  {subspecialty}: {count}")
    
    # Check correct answer extraction
    correct_answer_counts = Counter(part_ii_2022_mcqs.values_list('correct_answer', flat=True))
    print("\nCorrect Answer Distribution:")
    for answer, count in sorted(correct_answer_counts.items()):
        print(f"  {answer}: {count}")
    
    # Sample 5 MCQs to verify option_analysis extraction
    print("\nSample MCQs with Option Analysis:")
    sample_mcqs = part_ii_2022_mcqs.filter(explanation_sections__isnull=False)[:5]
    
    for i, mcq in enumerate(sample_mcqs, 1):
        print(f"\n{i}. Question #{mcq.question_number}: {mcq.question_text[:100]}...")
        print(f"   Subspecialty: {mcq.subspecialty}")
        print(f"   Correct Answer: {mcq.correct_answer}")
        
        if mcq.explanation_sections and 'option_analysis' in mcq.explanation_sections:
            option_analysis = mcq.explanation_sections['option_analysis']
            if isinstance(option_analysis, str):
                # Find the correct answer mention in option analysis
                if f"Option {mcq.correct_answer}" in option_analysis and "Correct" in option_analysis:
                    print(f"   ✓ Correct answer {mcq.correct_answer} found in option_analysis")
                else:
                    print(f"   ⚠ Correct answer {mcq.correct_answer} not clearly marked in option_analysis")
    
    # Check for MCQs with missing correct answers from option_analysis
    mcqs_with_sections = part_ii_2022_mcqs.filter(explanation_sections__isnull=False)
    mcqs_with_option_analysis = 0
    mcqs_with_correct_extracted = 0
    
    for mcq in mcqs_with_sections:
        if mcq.explanation_sections and 'option_analysis' in mcq.explanation_sections:
            mcqs_with_option_analysis += 1
            option_analysis = mcq.explanation_sections['option_analysis']
            if isinstance(option_analysis, str) and f"Option {mcq.correct_answer}" in option_analysis:
                mcqs_with_correct_extracted += 1
    
    print(f"\nOption Analysis Stats:")
    print(f"  MCQs with explanation sections: {mcqs_with_sections.count()}")
    print(f"  MCQs with option_analysis: {mcqs_with_option_analysis}")
    print(f"  MCQs with correct answer extracted: {mcqs_with_correct_extracted}")
    
    # Check for unclassified MCQs
    unclassified_count = part_ii_2022_mcqs.filter(subspecialty='Other/Unclassified').count()
    if unclassified_count > 0:
        print(f"\nUnclassified MCQs: {unclassified_count}")
        unclassified_samples = part_ii_2022_mcqs.filter(subspecialty='Other/Unclassified')[:3]
        for mcq in unclassified_samples:
            print(f"  Q{mcq.question_number}: {mcq.primary_category}")

if __name__ == "__main__":
    verify_import()