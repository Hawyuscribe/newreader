#!/usr/bin/env python3
"""
Export MCQs from Heroku database
"""

import os
os.chdir('django_neurology_mcq')
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
django.setup()

from mcq.models import MCQ
import json
from datetime import datetime

# Get all MCQs
mcqs = MCQ.objects.all().values(
    'id', 
    'question_number', 
    'question_text', 
    'options', 
    'correct_answer', 
    'subspecialty',
    'source_file',
    'exam_type',
    'exam_year',
    'explanation',
    'explanation_sections',
    'verification_confidence',
    'primary_category',
    'secondary_category',
    'key_concept',
    'difficulty_level',
    'image_url'
)

# Convert to list
mcq_list = list(mcqs)
print(f"Total MCQs to backup: {len(mcq_list)}")

# Save to JSON
backup_data = {
    'backup_date': datetime.now().isoformat(),
    'total_mcqs': len(mcq_list),
    'mcqs': mcq_list
}

# Save to file
backup_filename = f'heroku_mcqs_backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'
with open(backup_filename, 'w') as f:
    json.dump(backup_data, f, indent=2, default=str)

print(f"Backup saved to: {backup_filename}")