#!/usr/bin/env python
"""
Quick script to test if missing MCQs can be imported via Django shell
"""
import os
import sys
import django

# Setup Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
django.setup()

from mcq.models import MCQ
import json

def import_missing_mcqs():
    print("Starting import process...")
    
    # Load consolidated file
    try:
        with open('consolidated_all_mcqs.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        all_mcqs = data.get('mcqs', [])
        print(f"Loaded {len(all_mcqs)} MCQs from consolidated file")
        
        # Get existing question numbers
        existing_question_numbers = set(MCQ.objects.values_list('question_number', flat=True))
        print(f"Found {len(existing_question_numbers)} existing MCQs in database")
        
        # Find missing MCQs
        missing_mcqs = []
        for mcq_data in all_mcqs:
            question_number = mcq_data.get('question_number', '')
            if question_number and question_number not in existing_question_numbers:
                missing_mcqs.append(mcq_data)
        
        print(f"Found {len(missing_mcqs)} missing MCQs to import")
        
        if not missing_mcqs:
            print("No missing MCQs found!")
            return
        
        # Import in small batches
        created_count = 0
        batch_size = 5  # Very small batches
        
        for i in range(0, min(50, len(missing_mcqs)), batch_size):  # Limit to first 50 for testing
            batch = missing_mcqs[i:i + batch_size]
            
            for mcq_data in batch:
                try:
                    # Process explanation sections
                    explanation_sections = {}
                    if 'explanation' in mcq_data and isinstance(mcq_data['explanation'], dict):
                        explanation_sections = mcq_data['explanation']
                    
                    # Create MCQ
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
                    print(f"Imported MCQ {mcq_data.get('question_number', 'Unknown')}")
                
                except Exception as e:
                    print(f"Error importing MCQ {mcq_data.get('question_number', 'Unknown')}: {str(e)}")
            
            print(f"Batch {i//batch_size + 1} completed: {created_count} total imported")
        
        final_count = MCQ.objects.count()
        print(f"\nImport completed!")
        print(f"Created: {created_count} MCQs")
        print(f"Total MCQs in database: {final_count}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    import_missing_mcqs()