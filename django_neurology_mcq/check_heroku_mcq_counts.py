#!/usr/bin/env python
"""
Check actual MCQ counts on Heroku database
"""
import os
import sys
import django
from collections import defaultdict

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mcq.settings')
django.setup()

from mcq.models import MCQ, Subspecialty

def check_mcq_counts():
    """Check and display MCQ counts by subspecialty"""
    print("=" * 80)
    print("HEROKU MCQ COUNT CHECK")
    print("=" * 80)
    
    # Total MCQ count
    total_mcqs = MCQ.objects.count()
    print(f"\nTotal MCQs in database: {total_mcqs}")
    
    # Count by subspecialty
    print("\nMCQs by Subspecialty:")
    print("-" * 60)
    
    subspecialty_counts = defaultdict(int)
    
    for mcq in MCQ.objects.all():
        if mcq.subspecialty:
            subspecialty_counts[mcq.subspecialty.name] += 1
        else:
            subspecialty_counts["No Subspecialty"] += 1
    
    # Sort by count (descending)
    sorted_counts = sorted(subspecialty_counts.items(), key=lambda x: x[1], reverse=True)
    
    for subspecialty_name, count in sorted_counts:
        print(f"{subspecialty_name:<40} {count:>10}")
    
    print("-" * 60)
    
    # Check for specific subspecialties mentioned in the problem
    print("\nSpecific Subspecialty Checks:")
    print("-" * 60)
    
    problem_subspecialties = {
        "Movement Disorders": 269,
        "Vascular Neurology/Stroke": 439,
        "Neuromuscular": 483
    }
    
    for sub_name, expected_count in problem_subspecialties.items():
        actual_count = subspecialty_counts.get(sub_name, 0)
        status = "✓" if actual_count == expected_count else "✗"
        diff = actual_count - expected_count
        diff_str = f"+{diff}" if diff > 0 else str(diff)
        print(f"{sub_name:<30} Expected: {expected_count:<6} Actual: {actual_count:<6} {status} ({diff_str})")
    
    # Check for duplicate questions
    print("\nDuplicate Check:")
    print("-" * 60)
    
    question_texts = {}
    duplicates = []
    
    for mcq in MCQ.objects.all():
        if mcq.question in question_texts:
            duplicates.append((mcq.id, question_texts[mcq.question], mcq.question[:100]))
        else:
            question_texts[mcq.question] = mcq.id
    
    if duplicates:
        print(f"Found {len(duplicates)} duplicate questions!")
        for dup_id, orig_id, question_preview in duplicates[:5]:  # Show first 5
            print(f"  - MCQ {dup_id} duplicates MCQ {orig_id}: {question_preview}...")
    else:
        print("No duplicate questions found.")
    
    # Check exam types
    print("\nMCQs by Exam Type:")
    print("-" * 60)
    
    exam_counts = defaultdict(int)
    for mcq in MCQ.objects.all():
        exam_counts[mcq.exam_type] += 1
    
    for exam_type, count in sorted(exam_counts.items()):
        print(f"{exam_type:<30} {count:>10}")
    
    # Check for MCQs with missing data
    print("\nData Quality Check:")
    print("-" * 60)
    
    missing_subspecialty = MCQ.objects.filter(subspecialty__isnull=True).count()
    missing_exam_type = MCQ.objects.filter(exam_type='').count()
    missing_year = MCQ.objects.filter(year__isnull=True).count()
    
    print(f"MCQs without subspecialty: {missing_subspecialty}")
    print(f"MCQs without exam type: {missing_exam_type}")
    print(f"MCQs without year: {missing_year}")
    
    print("\n" + "=" * 80)

if __name__ == "__main__":
    check_mcq_counts()