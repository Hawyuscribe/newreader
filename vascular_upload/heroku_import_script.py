
import json
import os
from django.db import transaction
from mcq.models import MCQ

# Load MCQ data from temp file
with open('/tmp/vascular_chunk.json', 'r') as f:
    mcqs_data = json.load(f)

print(f"Importing {len(mcqs_data)} vascular MCQs")

# Import MCQs
with transaction.atomic():
    for mcq_data in mcqs_data:
        # Ensure required fields
        if 'question_text' not in mcq_data:
            print(f"Missing question_text, skipping")
            continue
            
        # Create or update MCQ
        defaults = {
            'subspecialty': mcq_data.get('subspecialty', 'vascular_neurology'),
            'question_text': mcq_data.get('question_text', ''),
            'options': mcq_data.get('options', {}),
            'correct_answer': mcq_data.get('correct_answer', ''),
            'explanation': mcq_data.get('explanation', ''),
            'exam_year': mcq_data.get('exam_year', ''),
            'exam_type': mcq_data.get('exam_type', ''),
        }
        
        # Add image URL if present
        if 'image_url' in mcq_data:
            defaults['image_url'] = mcq_data['image_url']
        
        # Use question_text as unique identifier
        mcq, created = MCQ.objects.update_or_create(
            question_text=mcq_data.get('question_text'),
            defaults=defaults
        )
        
print("Import completed successfully")
