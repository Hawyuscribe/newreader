#!/usr/bin/env python
"""
Simple script to import missing MCQs from consolidated file
Can be run directly with: python import_missing_mcqs_simple.py
"""
import os
import sys
import django
import json

# Add the Django project to the Python path
sys.path.append('/app')  # For Heroku
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_neurology_mcq.settings')

# Initialize Django
django.setup()

from django.db import transaction
from mcq.models import MCQ

def main():
    print('Loading consolidated MCQs file...')
    
    try:
        # Try different locations for the consolidated file
        possible_paths = [
            'consolidated_all_mcqs.json',
            '../consolidated_all_mcqs.json',
            '/app/consolidated_all_mcqs.json',
            '/app/django_neurology_mcq/consolidated_all_mcqs.json'
        ]
        
        json_file_path = None
        for path in possible_paths:
            if os.path.exists(path):
                json_file_path = path
                break
        
        if not json_file_path:
            print('ERROR: Could not find consolidated_all_mcqs.json in any expected location')
            return
        
        print(f'Found consolidated file at: {json_file_path}')
        with open(json_file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Handle different JSON structures
        if isinstance(data, dict) and 'mcqs' in data:
            all_mcqs = data['mcqs']
        elif isinstance(data, list):
            all_mcqs = data
        else:
            print('ERROR: Unexpected JSON structure')
            return
        
        print(f'Loaded {len(all_mcqs)} MCQs from file')
        
        # Get existing question numbers
        existing_question_numbers = set(MCQ.objects.values_list('question_number', flat=True))
        print(f'Found {len(existing_question_numbers)} existing MCQs in database')
        
        # Filter to only missing MCQs
        missing_mcqs = []
        for mcq_data in all_mcqs:
            question_number = mcq_data.get('question_number', '')
            if question_number and question_number not in existing_question_numbers:
                missing_mcqs.append(mcq_data)
        
        print(f'Found {len(missing_mcqs)} missing MCQs to import')
        
        if not missing_mcqs:
            print('SUCCESS: No missing MCQs to import!')
            return
        
        # Import missing MCQs in batches
        created_count = 0
        batch_size = 10
        
        for i in range(0, len(missing_mcqs), batch_size):
            batch = missing_mcqs[i:i + batch_size]
            
            with transaction.atomic():
                for mcq_data in batch:
                    try:
                        # Process explanation sections
                        explanation_sections = {}
                        if 'explanation' in mcq_data and isinstance(mcq_data['explanation'], dict):
                            explanation_sections = mcq_data['explanation']
                        
                        # Create MCQ with correct field mapping
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
                        created_count += 1
                    
                    except Exception as e:
                        print(f'ERROR importing MCQ {mcq_data.get("question_number", "Unknown")}: {str(e)}')
            
            print(f'Imported batch {i//batch_size + 1}: {created_count}/{len(missing_mcqs)} total MCQs imported...')
        
        # Final summary
        total_mcqs = MCQ.objects.count()
        print(f'\nSUCCESS: Imported {created_count} missing MCQs!')
        print(f'Total MCQs in database: {total_mcqs}')
        
        # Show subspecialty breakdown of missing MCQs
        from collections import Counter
        subspecialty_counts = Counter(mcq['subspecialty'] for mcq in missing_mcqs[:created_count])
        print('\nImported MCQs by subspecialty:')
        for subspecialty, count in subspecialty_counts.most_common():
            print(f'  {subspecialty}: {count}')
    
    except FileNotFoundError:
        print('ERROR: consolidated_all_mcqs.json file not found.')
    except json.JSONDecodeError as e:
        print(f'ERROR: Error parsing JSON file: {str(e)}')
    except Exception as e:
        print(f'ERROR: Unexpected error: {str(e)}')
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()