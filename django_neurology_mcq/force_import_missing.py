#!/usr/bin/env python
"""Force import missing MCQs with detailed error reporting"""
import os
import sys
import django
import json
from django.db import transaction, connection

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
django.setup()

from mcq.models import MCQ

# First check the field length
with connection.cursor() as cursor:
    cursor.execute("""
        SELECT character_maximum_length 
        FROM information_schema.columns 
        WHERE table_name = 'mcq_mcq' 
        AND column_name = 'correct_answer'
    """)
    result = cursor.fetchone()
    if result:
        print(f"Current correct_answer field length: {result[0]}")
    else:
        print("Could not determine field length")

# Load consolidated file
print("\nLoading MCQs...")
with open('consolidated_all_mcqs.json', 'r') as f:
    data = json.load(f)

all_mcqs = data['mcqs']
print(f"Total MCQs in file: {len(all_mcqs)}")

# Get current counts
current_count = MCQ.objects.count()
print(f"Current MCQs in database: {current_count}")

# Filter for Dementia and Epilepsy only
target_mcqs = [m for m in all_mcqs if m['subspecialty'] in ['Dementia', 'Epilepsy']]
print(f"\nTarget MCQs (Dementia + Epilepsy): {len(target_mcqs)}")

# Try to import with detailed error tracking
errors = []
success = 0

for i, mcq_data in enumerate(target_mcqs):
    try:
        # Check if this specific MCQ exists
        exists = MCQ.objects.filter(
            question_text=mcq_data.get('question', ''),
            subspecialty=mcq_data.get('subspecialty', '')
        ).exists()
        
        if not exists:
            explanation_sections = {}
            if 'explanation' in mcq_data and isinstance(mcq_data['explanation'], dict):
                explanation_sections = mcq_data['explanation']
            
            mcq = MCQ(
                question_number=mcq_data.get('question_number', ''),
                question_text=mcq_data.get('question', ''),
                options=mcq_data.get('options', []),
                correct_answer=mcq_data.get('correct_answer', ''),
                correct_answer_text=mcq_data.get('correct_answer_text', ''),
                subspecialty=mcq_data.get('subspecialty', 'General Neurology'),
                explanation_sections=explanation_sections,
                source_file=mcq_data.get('source_file', ''),
                exam_type=mcq_data.get('exam_type', ''),
                exam_year=mcq_data.get('exam_year', ''),
                ai_generated=mcq_data.get('ai_generated', False),
                unified_explanation=mcq_data.get('unified_explanation', ''),
                image_url=mcq_data.get('image_url', '')
            )
            mcq.save()
            success += 1
            if success % 10 == 0:
                print(f"  Imported {success} MCQs...")
    
    except Exception as e:
        error_msg = f"{mcq_data['subspecialty']} Q{mcq_data.get('question_number', '?')}: {str(e)}"
        if 'correct_answer' in str(e):
            error_msg += f" (answer: '{mcq_data.get('correct_answer', '')}', length: {len(mcq_data.get('correct_answer', ''))})"
        errors.append(error_msg)

final_count = MCQ.objects.count()
print(f"\nImport complete!")
print(f"Successfully imported: {success}")
print(f"Initial count: {current_count}")
print(f"Final count: {final_count}")
print(f"Net change: +{final_count - current_count}")

if errors:
    print(f"\nErrors ({len(errors)}):")
    for error in errors[:10]:  # Show first 10 errors
        print(f"  - {error}")