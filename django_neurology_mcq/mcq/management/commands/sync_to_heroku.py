from django.core.management.base import BaseCommand
from django.db import transaction
from mcq.models import MCQ
import json
import gzip
import os
import math

class Command(BaseCommand):
    help = 'Export missing MCQs in chunks for Heroku import'

    def handle(self, *args, **options):
        self.stdout.write("Creating MCQ export for Heroku sync...")
        
        # Get all MCQs from local database
        local_mcqs = MCQ.objects.all().order_by('id')
        total_count = local_mcqs.count()
        
        self.stdout.write(f"Total MCQs in local database: {total_count}")
        
        # Create fixture data
        fixture_data = []
        
        for mcq in local_mcqs:
            mcq_data = {
                'model': 'mcq.mcq',
                'pk': None,  # Let Heroku assign new IDs
                'fields': {
                    'question_text': mcq.question_text,
                    'options': mcq.options,
                    'correct_answer': mcq.correct_answer,
                    'explanation': mcq.explanation,
                    'explanation_sections': mcq.explanation_sections,
                    'subspecialty': mcq.subspecialty,
                    'exam_type': mcq.exam_type,
                    'exam_year': mcq.exam_year,
                    'question_number': mcq.question_number,
                    'source_file': mcq.source_file,
                    'image_url': mcq.image_url,
                    'correct_answer_text': mcq.correct_answer_text,
                    'ai_generated': mcq.ai_generated,
                    'verification_confidence': mcq.verification_confidence,
                    'primary_category': mcq.primary_category,
                    'secondary_category': mcq.secondary_category,
                    'key_concept': mcq.key_concept,
                    'difficulty_level': mcq.difficulty_level
                }
            }
            fixture_data.append(mcq_data)
        
        # Split into chunks to avoid memory issues
        chunk_size = 100  # Smaller chunks for Heroku
        total_chunks = math.ceil(len(fixture_data) / chunk_size)
        
        self.stdout.write(f"Creating {total_chunks} chunks of {chunk_size} MCQs each...")
        
        for i in range(0, len(fixture_data), chunk_size):
            chunk_num = (i // chunk_size) + 1
            chunk_data = fixture_data[i:i + chunk_size]
            
            # Create filename
            filename = f'heroku_sync_chunk_{chunk_num:03d}_of_{total_chunks:03d}.json'
            
            # Write chunk to file
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(chunk_data, f, ensure_ascii=False, indent=2)
            
            # Also create compressed version
            with gzip.open(f'{filename}.gz', 'wt', encoding='utf-8') as f:
                json.dump(chunk_data, f, ensure_ascii=False)
            
            self.stdout.write(f"Created {filename} with {len(chunk_data)} MCQs")
        
        # Create a script to load all chunks on Heroku
        script_content = f'''#!/bin/bash
# Heroku MCQ sync script
echo "Starting MCQ sync to Heroku..."

# Clear existing MCQs first
echo "Clearing existing MCQs..."
heroku run "cd django_neurology_mcq && python manage.py shell -c 'from mcq.models import MCQ; MCQ.objects.all().delete(); print(f\\"Cleared {{MCQ.objects.count()}} MCQs\\")'" --app radiant-gorge-35079

# Load each chunk
'''
        
        for chunk_num in range(1, total_chunks + 1):
            filename = f'heroku_sync_chunk_{chunk_num:03d}_of_{total_chunks:03d}.json'
            script_content += f'''
echo "Loading chunk {chunk_num}/{total_chunks}..."
heroku run "cd django_neurology_mcq && python manage.py loaddata {filename}" --app radiant-gorge-35079
'''
        
        script_content += '''
echo "Verifying final count..."
heroku run "cd django_neurology_mcq && python manage.py shell -c 'from mcq.models import MCQ; print(f\\"Final count: {{MCQ.objects.count()}} MCQs\\")'" --app radiant-gorge-35079

echo "MCQ sync complete!"
'''
        
        with open('sync_to_heroku.sh', 'w') as f:
            f.write(script_content)
        
        os.chmod('sync_to_heroku.sh', 0o755)
        
        self.stdout.write(self.style.SUCCESS(f"Export complete!"))
        self.stdout.write(f"Created {total_chunks} chunk files")
        self.stdout.write(f"Created sync_to_heroku.sh script")
        self.stdout.write("\nTo sync to Heroku:")
        self.stdout.write("1. Upload chunk files to Heroku")
        self.stdout.write("2. Run: ./sync_to_heroku.sh")
        
        # Create a simple upload command
        upload_cmd = 'heroku run "cd django_neurology_mcq && python manage.py import_all_remaining_mcqs" --app radiant-gorge-35079'
        self.stdout.write(f"\nOr try running the existing import command:")
        self.stdout.write(upload_cmd)