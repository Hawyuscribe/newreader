#!/usr/bin/env python
import os
import sys
import django
import json

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
django.setup()

from mcq.models import MCQ
from collections import Counter

# Load consolidated file
with open('consolidated_all_mcqs.json', 'r') as f:
    data = json.load(f)

all_mcqs = data['mcqs']
print(f"Total MCQs in file: {len(all_mcqs)}")

# Get current database state
db_mcqs = MCQ.objects.all()
print(f"Total MCQs in database: {db_mcqs.count()}")

# Count by subspecialty in database
db_subspecialties = Counter(db_mcqs.values_list('subspecialty', flat=True))
file_subspecialties = Counter(mcq['subspecialty'] for mcq in all_mcqs)

print("\nSubspecialty comparison (File vs Database):")
all_subspecialties = sorted(set(list(file_subspecialties.keys()) + list(db_subspecialties.keys())))

for subspecialty in all_subspecialties:
    file_count = file_subspecialties.get(subspecialty, 0)
    db_count = db_subspecialties.get(subspecialty, 0)
    diff = file_count - db_count
    if diff != 0:
        print(f"  {subspecialty}: {file_count} in file, {db_count} in DB (missing: {diff})")

# Check specific missing MCQs
print("\nChecking missing Dementia and Epilepsy MCQs...")

# Create a unique identifier for each MCQ
def get_mcq_identifier(mcq):
    # Use combination of fields to identify unique MCQs
    return (
        mcq.get('question_number', ''),
        mcq.get('question', '')[:100],  # First 100 chars of question
        mcq.get('exam_type', ''),
        mcq.get('exam_year', '')
    )

# Get identifiers from database
db_identifiers = set()
for mcq in db_mcqs:
    db_identifiers.add((
        mcq.question_number or '',
        mcq.question_text[:100] if mcq.question_text else '',
        mcq.exam_type or '',
        mcq.exam_year or ''
    ))

# Find missing MCQs
missing_by_subspecialty = {}
for mcq in all_mcqs:
    identifier = get_mcq_identifier(mcq)
    if identifier not in db_identifiers:
        subspecialty = mcq['subspecialty']
        if subspecialty not in missing_by_subspecialty:
            missing_by_subspecialty[subspecialty] = []
        missing_by_subspecialty[subspecialty].append(mcq)

# Show sample missing MCQs
for subspecialty in ['Dementia', 'Epilepsy']:
    if subspecialty in missing_by_subspecialty:
        missing = missing_by_subspecialty[subspecialty]
        print(f"\n{subspecialty} - {len(missing)} missing MCQs")
        print("Sample missing MCQs:")
        for mcq in missing[:3]:  # Show first 3
            print(f"  Q{mcq['question_number']}: {mcq['question'][:60]}...")
            print(f"    Answer: '{mcq['correct_answer']}' (length: {len(mcq['correct_answer'])})")
            print(f"    Exam: {mcq.get('exam_type', 'N/A')} {mcq.get('exam_year', 'N/A')}")