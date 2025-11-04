#!/usr/bin/env python
"""
Script to validate MCQ imports, checking data integrity across various fields.
"""

import os
import sys
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
django.setup()

from mcq.models import MCQ
from collections import Counter, defaultdict

def validate_imports():
    """Validate the imported MCQs, checking key fields for data integrity."""
    total_mcqs = MCQ.objects.count()
    print(f"Total MCQs: {total_mcqs}")
    
    # Check for missing data
    mcqs_missing_answer = MCQ.objects.filter(correct_answer='').count()
    mcqs_missing_subspecialty = MCQ.objects.filter(subspecialty='').count()
    mcqs_missing_explanation_sections = MCQ.objects.filter(explanation_sections__isnull=True).count()
    mcqs_missing_verification = MCQ.objects.filter(verification_confidence='').count()
    mcqs_missing_primary_category = MCQ.objects.filter(primary_category='').count()
    mcqs_missing_difficulty = MCQ.objects.filter(difficulty_level='').count()
    
    print("\n--- Data Completeness ---")
    print(f"MCQs missing correct answers: {mcqs_missing_answer}")
    print(f"MCQs missing subspecialty: {mcqs_missing_subspecialty}")
    print(f"MCQs missing explanation sections: {mcqs_missing_explanation_sections}")
    print(f"MCQs missing verification confidence: {mcqs_missing_verification}")
    print(f"MCQs missing primary category: {mcqs_missing_primary_category}")
    print(f"MCQs missing difficulty level: {mcqs_missing_difficulty}")
    
    # Check options format
    problem_options = 0
    for mcq in MCQ.objects.all():
        if not isinstance(mcq.options, dict) or not mcq.options:
            problem_options += 1
            print(f"  - MCQ #{mcq.id} has problematic options format: {type(mcq.options)}")
    
    print(f"\nMCQs with problematic option formats: {problem_options}")
    
    # Check classification
    subspecialty_counts = dict(Counter(MCQ.objects.values_list('subspecialty', flat=True)))
    exam_type_counts = dict(Counter(MCQ.objects.values_list('exam_type', flat=True)))
    exam_year_counts = dict(Counter(MCQ.objects.values_list('exam_year', flat=True)))
    verification_counts = dict(Counter(MCQ.objects.values_list('verification_confidence', flat=True)))
    difficulty_counts = dict(Counter(MCQ.objects.values_list('difficulty_level', flat=True)))
    
    print("\n--- Classification Summary ---")
    print("Subspecialties:")
    for subspecialty, count in sorted(subspecialty_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"  - {subspecialty}: {count}")
    
    print("\nExam Types:")
    for exam_type, count in sorted(exam_type_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"  - {exam_type}: {count}")
    
    print("\nExam Years:")
    for year, count in sorted(exam_year_counts.items(), key=lambda x: (x[0] is None, x[0]), reverse=False):
        print(f"  - {year}: {count}")
    
    print("\nVerification Confidence Levels:")
    for level, count in sorted(verification_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"  - {level}: {count}")
    
    print("\nDifficulty Levels:")
    for level, count in sorted(difficulty_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"  - {level}: {count}")
    
    # Check explanation sections
    print("\n--- Explanation Sections ---")
    section_presence = defaultdict(int)
    for mcq in MCQ.objects.all():
        if mcq.explanation_sections:
            for section_name in mcq.explanation_sections.keys():
                section_presence[section_name] += 1
    
    total_with_sections = MCQ.objects.exclude(explanation_sections__isnull=True).count()
    for section_name, count in sorted(section_presence.items(), key=lambda x: x[1], reverse=True):
        percentage = (count / total_with_sections) * 100 if total_with_sections > 0 else 0
        print(f"  - {section_name}: {count} ({percentage:.1f}%)")
    
    # Overall assessment
    print("\n--- Overall Assessment ---")
    if (mcqs_missing_answer + mcqs_missing_subspecialty + mcqs_missing_explanation_sections + 
            mcqs_missing_verification + problem_options) == 0:
        print("✅ All MCQs have complete data with no obvious issues.")
    else:
        print("⚠️ Some issues were detected. Please review the summary above.")
        
    return {
        'total_mcqs': total_mcqs,
        'missing_answers': mcqs_missing_answer,
        'missing_subspecialty': mcqs_missing_subspecialty,
        'missing_explanation_sections': mcqs_missing_explanation_sections,
        'problem_options': problem_options
    }

if __name__ == "__main__":
    validate_imports()