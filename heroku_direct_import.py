#!/usr/bin/env python3
import os
import sys
import django
import json
import base64
from pathlib import Path

# Django setup
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
django.setup()

from mcq.models import MCQ
from django.db import transaction

def import_mcqs_from_data(encoded_data):
    """Import MCQs from base64 encoded data"""
    try:
        # Decode the data
        json_data = base64.b64decode(encoded_data).decode('utf-8')
        mcqs = json.loads(json_data)
        
        imported = 0
        errors = []
        
        with transaction.atomic():
            for mcq_data in mcqs:
                try:
                    # Process explanation
                    explanation = ""
                    explanation_sections = {}
                    
                    if 'unified_explanation' in mcq_data and mcq_data['unified_explanation']:
                        explanation = mcq_data['unified_explanation']
                    elif 'explanation' in mcq_data:
                        if isinstance(mcq_data['explanation'], dict):
                            exp_dict = mcq_data['explanation']
                            parts = []
                            
                            # Build explanation from sections
                            section_mapping = {
                                'option_analysis': 'Option Analysis',
                                'conceptual_foundation': 'Conceptual Foundation',
                                'pathophysiology': 'Pathophysiology',
                                'clinical_manifestation': 'Clinical Manifestation',
                                'diagnostic_approach': 'Diagnostic Approach',
                                'management_principles': 'Management Principles',
                                'follow_up_guidelines': 'Follow-up Guidelines',
                                'clinical_pearls': 'Clinical Pearls',
                                'references': 'References'
                            }
                            
                            for section_key, section_title in section_mapping.items():
                                if section_key in exp_dict and exp_dict[section_key]:
                                    content = exp_dict[section_key]
                                    if not (isinstance(content, str) and content.startswith("This section information")):
                                        parts.append(f"**{section_title}:**\n{content}")
                                        explanation_sections[section_key] = content
                            
                            explanation = '\n\n'.join(parts)
                        else:
                            explanation = str(mcq_data.get('explanation', ''))
                    
                    # Get correct answer
                    correct_answer = mcq_data.get('correct_answer', '')
                    if not correct_answer and 'correct_answer_text' in mcq_data:
                        # Try to match correct_answer_text to options
                        correct_text = mcq_data['correct_answer_text']
                        options = mcq_data.get('options', [])
                        if isinstance(options, list):
                            for i, option in enumerate(options):
                                if option.strip() == correct_text.strip():
                                    correct_answer = chr(65 + i)  # A, B, C, etc.
                                    break
                    
                    # Ensure correct_answer fits in the field (max 10 chars)
                    correct_answer = str(correct_answer)[:10]
                    
                    # Create MCQ object
                    mcq_obj = MCQ(
                        question_number=str(mcq_data.get('question_number', ''))[:20],
                        question_text=mcq_data.get('question', ''),
                        options=mcq_data.get('options', {}),
                        correct_answer=correct_answer,
                        correct_answer_text=mcq_data.get('correct_answer_text', ''),
                        subspecialty=mcq_data.get('subspecialty', mcq_data.get('import_specialty', '')),
                        source_file=mcq_data.get('source_file', mcq_data.get('import_source', ''))[:200],
                        exam_type=mcq_data.get('exam_type', ''),
                        exam_year=mcq_data.get('exam_year'),
                        explanation=explanation,
                        explanation_sections=explanation_sections if explanation_sections else None,
                        image_url=mcq_data.get('image_url', ''),
                        ai_generated=mcq_data.get('ai_generated', False)
                    )
                    
                    mcq_obj.save()
                    imported += 1
                    
                    if imported % 50 == 0:
                        print(f"  Imported {imported} MCQs...")
                    
                except Exception as e:
                    error_msg = f"Error importing MCQ {mcq_data.get('question_number', 'unknown')}: {str(e)}"
                    errors.append(error_msg)
                    print(f"  ✗ {error_msg}")
        
        return imported, errors
        
    except Exception as e:
        print(f"✗ Error processing data: {e}")
        return 0, [str(e)]

def main():
    """Main import function"""
    print("=== MCQ Import to Heroku ===")
    print("Target: https://radiant-gorge-35079-2b52ba172c1e.herokuapp.com/")
    
    # Check current MCQ count
    current_count = MCQ.objects.count()
    print(f"Current MCQ count: {current_count}")
    
    if current_count > 0:
        response = input(f"There are {current_count} existing MCQs. Delete them? (yes/no): ")
        if response.lower() == 'yes':
            MCQ.objects.all().delete()
            print("✓ Deleted existing MCQs")
    
    total_imported = 0
    total_errors = []
    
    # Import from environment variable data
    chunk_num = 0
    while True:
        env_var = f"MCQ_CHUNK_{chunk_num}"
        encoded_data = os.environ.get(env_var)
        
        if not encoded_data:
            break
            
        print(f"\nProcessing chunk {chunk_num}...")
        imported, errors = import_mcqs_from_data(encoded_data)
        total_imported += imported
        total_errors.extend(errors)
        chunk_num += 1
    
    print(f"\n=== Import Summary ===")
    print(f"Total MCQs imported: {total_imported}")
    print(f"Total errors: {len(total_errors)}")
    print(f"Final MCQ count: {MCQ.objects.count()}")
    
    if total_errors:
        print("\nFirst 10 errors:")
        for error in total_errors[:10]:
            print(f"- {error}")

if __name__ == "__main__":
    main()
