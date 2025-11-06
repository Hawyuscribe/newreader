#\!/usr/bin/env python3
"""
Import MCQs from Heroku config vars
This script runs on Heroku to import MCQs stored in config variables
"""
import os
import sys
import django
import json
import base64
from django.db import transaction

# Django setup
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
django.setup()

from mcq.models import MCQ

def import_from_config_vars():
    """Import MCQs from config variables"""
    print("=== MCQ Import from Config Vars ===")
    print(f"Target: https://radiant-gorge-35079-2b52ba172c1e.herokuapp.com/")
    
    # Check current MCQ count
    current_count = MCQ.objects.count()
    print(f"Current MCQ count: {current_count}")
    
    if current_count > 0:
        print(f"Clearing {current_count} existing MCQs...")
        MCQ.objects.all().delete()
        print("✓ Cleared")
    
    total_imported = 0
    total_errors = []
    chunk_num = 0
    
    print("\nImporting MCQs from config vars...")
    
    while True:
        var_name = f"MCQ_CHUNK_{chunk_num:03d}"
        encoded_data = os.environ.get(var_name)
        
        if not encoded_data:
            break
        
        try:
            # Decode the chunk
            chunk_data = base64.b64decode(encoded_data).decode('utf-8')
            mcqs = json.loads(chunk_data)
            
            chunk_imported = 0
            
            with transaction.atomic():
                for mcq_data in mcqs:
                    try:
                        # Process explanation
                        explanation = ""
                        explanation_sections = {}
                        
                        if 'unified_explanation' in mcq_data and mcq_data['unified_explanation']:
                            explanation = mcq_data['unified_explanation']
                        elif 'explanation' in mcq_data and isinstance(mcq_data['explanation'], dict):
                            exp_dict = mcq_data['explanation']
                            parts = []
                            
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
                            
                            for key, title in section_mapping.items():
                                if key in exp_dict and exp_dict[key]:
                                    content = exp_dict[key]
                                    if not (isinstance(content, str) and content.startswith("This section information")):
                                        parts.append(f"**{title}:**\\n{content}")
                                        explanation_sections[key] = content
                            
                            explanation = '\\n\\n'.join(parts)
                        
                        # Get correct answer
                        correct_answer = mcq_data.get('correct_answer', '')
                        if not correct_answer and 'correct_answer_text' in mcq_data:
                            correct_text = mcq_data['correct_answer_text']
                            options = mcq_data.get('options', [])
                            if isinstance(options, list):
                                for j, option in enumerate(options):
                                    if option.strip() == correct_text.strip():
                                        correct_answer = chr(65 + j)
                                        break
                        
                        # Create MCQ
                        mcq = MCQ(
                            question_number=str(mcq_data.get('question_number', ''))[:20],
                            question_text=mcq_data.get('question', ''),
                            options=mcq_data.get('options', {}),
                            correct_answer=str(correct_answer)[:10],
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
                        mcq.save()
                        chunk_imported += 1
                        
                    except Exception as e:
                        error_msg = f"MCQ {mcq_data.get('question_number', 'unknown')}: {str(e)}"
                        total_errors.append(error_msg)
            
            total_imported += chunk_imported
            
            if chunk_num % 10 == 0:
                print(f"Progress: Processed {chunk_num + 1} chunks, imported {total_imported} MCQs...")
                
        except Exception as e:
            error_msg = f"Chunk {chunk_num}: {str(e)}"
            total_errors.append(error_msg)
            print(f"Error processing {var_name}: {str(e)}")
        
        chunk_num += 1
    
    print(f"\n=== Import Summary ===")
    print(f"Total chunks processed: {chunk_num}")
    print(f"Total MCQs imported: {total_imported}")
    print(f"Total errors: {len(total_errors)}")
    print(f"Final MCQ count: {MCQ.objects.count()}")
    
    if total_errors:
        print("\nFirst 10 errors:")
        for error in total_errors[:10]:
            print(f"- {error}")
    
    # Clear config vars after import to free up space
    if total_imported > 0:
        print("\nCleaning up config vars...")
        # This would need to be done via Heroku CLI or API
        print("Note: Config vars should be cleared manually to free up space")
    
    print("\n✅ Import complete\!")
    return total_imported > 0

if __name__ == "__main__":
    success = import_from_config_vars()
    sys.exit(0 if success else 1)
