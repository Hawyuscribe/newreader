#!/usr/bin/env python3
"""Check for duplicate MCQs and verify proper categorization by year and exam type."""
import os
import sys
import django
from collections import Counter
import json

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from mcq.models import MCQ

def check_duplicates_and_categorization():
    print("MCQ Database Analysis: Duplicates and Categorization")
    print("=" * 50)
    
    # Get all MCQs
    all_mcqs = MCQ.objects.all()
    total_count = all_mcqs.count()
    print(f"\nTotal MCQs in database: {total_count}")
    
    # 1. Check categorization by exam type and year
    print("\n1. CATEGORIZATION BY EXAM TYPE AND YEAR:")
    print("-" * 40)
    
    # Group by exam type and year
    exam_type_year_combos = all_mcqs.values('exam_type', 'exam_year').distinct()
    
    categorization_summary = {}
    for combo in exam_type_year_combos:
        exam_type = combo['exam_type'] or 'Unknown'
        exam_year = combo['exam_year'] or 'Unknown'
        count = all_mcqs.filter(exam_type=combo['exam_type'], exam_year=combo['exam_year']).count()
        
        key = f"{exam_type} - {exam_year}"
        categorization_summary[key] = count
    
    # Display sorted by exam type and year
    for key in sorted(categorization_summary.keys()):
        print(f"  {key}: {categorization_summary[key]} MCQs")
    
    # 2. Check for duplicate MCQs
    print("\n2. DUPLICATE CHECK:")
    print("-" * 40)
    
    # Find potential duplicates based on question text and options
    duplicate_groups = {}
    processed_ids = set()
    
    for mcq in all_mcqs:
        if mcq.id in processed_ids:
            continue
            
        # Create a unique key from question text and options
        options_str = json.dumps(mcq.get_options_dict(), sort_keys=True) if mcq.options else ""
        key = f"{mcq.question_text.strip().lower()}||{options_str}"
        
        if key not in duplicate_groups:
            duplicate_groups[key] = []
        duplicate_groups[key].append(mcq)
        processed_ids.add(mcq.id)
    
    # Find groups with duplicates
    actual_duplicates = {k: v for k, v in duplicate_groups.items() if len(v) > 1}
    
    if actual_duplicates:
        print(f"Found {len(actual_duplicates)} groups of duplicate MCQs:")
        
        for i, (key, duplicates) in enumerate(list(actual_duplicates.items())[:5], 1):
            print(f"\n  Duplicate Group {i}:")
            print(f"  Question: {duplicates[0].question_text[:100]}...")
            print(f"  MCQs in this group:")
            for mcq in duplicates:
                print(f"    - ID: {mcq.id}, Q#{mcq.question_number}, {mcq.exam_type} {mcq.exam_year}, {mcq.subspecialty}")
        
        if len(actual_duplicates) > 5:
            print(f"\n  ... and {len(actual_duplicates) - 5} more duplicate groups")
            
        # Count total duplicates
        total_duplicate_mcqs = sum(len(group) - 1 for group in actual_duplicates.values())
        print(f"\nTotal duplicate MCQs that could be removed: {total_duplicate_mcqs}")
    else:
        print("No exact duplicates found!")
    
    # 3. Check Part II 2022 MCQs specifically
    print("\n3. PART II 2022 MCQs ANALYSIS:")
    print("-" * 40)
    
    part_ii_2022 = all_mcqs.filter(exam_type='Part II', exam_year=2022)
    part_ii_2022_count = part_ii_2022.count()
    
    print(f"Total Part II 2022 MCQs: {part_ii_2022_count}")
    
    # Check for duplicates within Part II 2022
    part_ii_duplicates = {}
    for mcq in part_ii_2022:
        options_str = json.dumps(mcq.get_options_dict(), sort_keys=True) if mcq.options else ""
        key = f"{mcq.question_text.strip().lower()}||{options_str}"
        
        if key not in part_ii_duplicates:
            part_ii_duplicates[key] = []
        part_ii_duplicates[key].append(mcq)
    
    part_ii_actual_duplicates = {k: v for k, v in part_ii_duplicates.items() if len(v) > 1}
    
    if part_ii_actual_duplicates:
        print(f"\nDuplicates within Part II 2022: {len(part_ii_actual_duplicates)} groups")
        for i, (key, duplicates) in enumerate(list(part_ii_actual_duplicates.items())[:3], 1):
            print(f"\n  Group {i}:")
            print(f"  Question: {duplicates[0].question_text[:80]}...")
            for mcq in duplicates:
                print(f"    - Q#{mcq.question_number}, {mcq.subspecialty}")
    else:
        print("No duplicates within Part II 2022 MCQs")
    
    # Subspecialty distribution for Part II 2022
    print("\nPart II 2022 Subspecialty Distribution:")
    subspecialty_counts = Counter(part_ii_2022.values_list('subspecialty', flat=True))
    for subspecialty, count in subspecialty_counts.most_common():
        print(f"  {subspecialty}: {count}")
    
    # 4. Check for MCQs with missing exam type or year
    print("\n4. MCQs WITH MISSING CATEGORIZATION:")
    print("-" * 40)
    
    missing_exam_type = all_mcqs.filter(exam_type__isnull=True).count()
    missing_exam_year = all_mcqs.filter(exam_year__isnull=True).count()
    
    print(f"MCQs with missing exam type: {missing_exam_type}")
    print(f"MCQs with missing exam year: {missing_exam_year}")
    
    if missing_exam_type > 0:
        samples = all_mcqs.filter(exam_type__isnull=True)[:3]
        print("\nSample MCQs with missing exam type:")
        for mcq in samples:
            print(f"  ID: {mcq.id}, Q#{mcq.question_number}: {mcq.question_text[:50]}...")
    
    if missing_exam_year > 0:
        samples = all_mcqs.filter(exam_year__isnull=True)[:3]
        print("\nSample MCQs with missing exam year:")
        for mcq in samples:
            print(f"  ID: {mcq.id}, Q#{mcq.question_number}: {mcq.question_text[:50]}...")

if __name__ == "__main__":
    check_duplicates_and_categorization()