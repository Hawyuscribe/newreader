#!/usr/bin/env python
"""Find all types of duplicate MCQs"""

import os
import sys
import django
import json
from collections import defaultdict

# Setup Django
sys.path.insert(0, '/Users/tariqalmatrudi/NEWreader/django_neurology_mcq')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
django.setup()

from mcq.models import MCQ
from django.db.models import Count

print("Analyzing MCQs for duplicates...")

# 1. Check for exact duplicates (question text + options)
print("\n1. Checking for exact duplicates (question + options)...")
exact_duplicates = defaultdict(list)
for mcq in MCQ.objects.all():
    options_str = json.dumps(mcq.get_options_dict(), sort_keys=True) if mcq.options else ""
    key = f"{mcq.question_text.strip().lower()}||{options_str}"
    exact_duplicates[key].append(mcq)

exact_dup_count = sum(1 for group in exact_duplicates.values() if len(group) > 1)
print(f"Found {exact_dup_count} groups of exact duplicates")

# 2. Check for question text duplicates (ignoring options)
print("\n2. Checking for question text duplicates (ignoring options)...")
text_duplicates = defaultdict(list)
for mcq in MCQ.objects.all():
    key = mcq.question_text.strip().lower()
    text_duplicates[key].append(mcq)

text_dup_count = sum(1 for group in text_duplicates.values() if len(group) > 1)
print(f"Found {text_dup_count} groups of text duplicates")

# 3. Check for question number duplicates
print("\n3. Checking for question number duplicates...")
number_duplicates = defaultdict(list)
for mcq in MCQ.objects.exclude(question_number__isnull=True).exclude(question_number=''):
    key = mcq.question_number
    number_duplicates[key].append(mcq)

number_dup_count = sum(1 for group in number_duplicates.values() if len(group) > 1)
print(f"Found {number_dup_count} question numbers with duplicates")

# 4. Check for source file + question number duplicates
print("\n4. Checking for source file + question number duplicates...")
source_duplicates = defaultdict(list)
for mcq in MCQ.objects.exclude(question_number__isnull=True).exclude(question_number=''):
    if mcq.source_file:
        key = f"{mcq.source_file}||{mcq.question_number}"
        source_duplicates[key].append(mcq)

source_dup_count = sum(1 for group in source_duplicates.values() if len(group) > 1)
print(f"Found {source_dup_count} source file + question number duplicates")

# Show detailed examples
if text_dup_count > 0:
    print("\n--- Examples of Text Duplicates ---")
    count = 0
    for question_text, mcqs in text_duplicates.items():
        if len(mcqs) > 1 and count < 5:
            print(f"\nQuestion: {question_text[:100]}...")
            print(f"Found {len(mcqs)} copies:")
            for mcq in mcqs[:5]:
                print(f"  - ID: {mcq.id}, Q#: {mcq.question_number}, Source: {mcq.source_file}, Year: {mcq.exam_year}")
            count += 1

if number_dup_count > 0:
    print("\n--- Examples of Question Number Duplicates ---")
    count = 0
    for q_num, mcqs in number_duplicates.items():
        if len(mcqs) > 1 and count < 5:
            print(f"\nQuestion Number: {q_num}")
            print(f"Found {len(mcqs)} MCQs:")
            for mcq in mcqs[:5]:
                print(f"  - ID: {mcq.id}, Text: {mcq.question_text[:50]}..., Source: {mcq.source_file}")
            count += 1

# Summary
print("\n=== SUMMARY ===")
print(f"Total MCQs: {MCQ.objects.count()}")
print(f"Exact duplicates (text + options): {exact_dup_count} groups")
print(f"Text duplicates (ignoring options): {text_dup_count} groups")
print(f"Question number duplicates: {number_dup_count} groups")
print(f"Source + number duplicates: {source_dup_count} groups")

# Calculate total duplicates to remove
total_to_remove = 0
for group in text_duplicates.values():
    if len(group) > 1:
        total_to_remove += len(group) - 1

print(f"\nIf we remove all text duplicates, we would delete: {total_to_remove} MCQs")