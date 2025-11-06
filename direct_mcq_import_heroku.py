#!/usr/bin/env python3
import os
import sys
import django
import json
from pathlib import Path

# Add the project root to the Python path
project_root = Path(__file__).parent.resolve()
sys.path.insert(0, str(project_root))

# Django setup
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_neurology_mcq.settings')
django.setup()

from django_neurology_mcq.mcq.models import MCQ

def import_mcqs_from_directory(directory_path):
    """Import all MCQs from the specified directory"""
    imported_count = 0
    errors = []
    
    # Get all JSON files in the directory
    json_files = sorted(Path(directory_path).glob('*.json'))
    
    print(f"Found {len(json_files)} JSON files to process")
    
    for json_file in json_files:
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            mcqs = data.get('mcqs', [])
            subspecialty = data.get('subspecialty', 'Unknown')
            
            print(f"\nProcessing {json_file.name}: {subspecialty} with {len(mcqs)} MCQs")
            
            for mcq_data in mcqs:
                try:
                    # Process explanation
                    explanation = ""
                    explanation_sections = None
                    
                    if 'unified_explanation' in mcq_data and mcq_data['unified_explanation']:
                        explanation = mcq_data['unified_explanation']
                    elif 'explanation' in mcq_data and isinstance(mcq_data['explanation'], dict):
                        explanation_sections = {}
                        explanation_parts = []
                        
                        for section, content in mcq_data['explanation'].items():
                            if content and not content.startswith("This section information is included"):
                                explanation_sections[section] = content
                                explanation_parts.append(f"**{section.replace('_', ' ').title()}**\n{content}")
                        
                        explanation = "\n\n".join(explanation_parts)
                    
                    # Create MCQ
                    mcq = MCQ(
                        question_number=mcq_data.get('question_number', ''),
                        question_text=mcq_data.get('question_text', ''),
                        options=mcq_data.get('options', {}),
                        correct_answer=mcq_data.get('correct_answer', ''),
                        subspecialty=subspecialty,
                        topic=mcq_data.get('topic', ''),
                        exam_type=mcq_data.get('exam_type', ''),
                        year=mcq_data.get('year'),
                        explanation=explanation,
                        explanation_sections=explanation_sections,
                        difficulty=mcq_data.get('difficulty'),
                        cognitive_level=mcq_data.get('cognitive_level'),
                        key_concepts=mcq_data.get('key_concepts', []),
                        clinical_context=mcq_data.get('clinical_context'),
                        image_url=mcq_data.get('image_url'),
                        lab_data=mcq_data.get('lab_data'),
                        feedback=mcq_data.get('feedback', {})
                    )
                    mcq.save()
                    imported_count += 1
                    
                    if imported_count % 100 == 0:
                        print(f"  Imported {imported_count} MCQs so far...")
                    
                except Exception as e:
                    error_msg = f"Error importing MCQ: {str(e)}"
                    errors.append(error_msg)
                    print(f"  ERROR: {error_msg}")
                    
        except Exception as e:
            error_msg = f"Error processing file {json_file.name}: {str(e)}"
            errors.append(error_msg)
            print(f"ERROR: {error_msg}")
    
    return imported_count, errors

if __name__ == "__main__":
    print("Starting MCQ import process...")
    
    # Directory containing the new MCQs
    # Check if running on Heroku or locally
    if os.environ.get('DYNO'):
        # Running on Heroku
        mcq_directory = "/app/mcq_data_to_import"
    else:
        # Running locally
        mcq_directory = "/Users/tariqalmatrudi/Documents/FFF/output_by_specialty"
    
    # Check current MCQ count
    current_count = MCQ.objects.count()
    print(f"Current MCQ count in database: {current_count}")
    
    if current_count > 0:
        print("WARNING: There are existing MCQs in the database!")
        print("Please delete them first if you want to replace all MCQs.")
        sys.exit(1)
    
    # Import MCQs
    imported, errors = import_mcqs_from_directory(mcq_directory)
    
    # Print summary
    print("\n" + "="*50)
    print(f"Import complete!")
    print(f"Total MCQs imported: {imported}")
    print(f"Total errors: {len(errors)}")
    
    if errors:
        print("\nErrors encountered:")
        for error in errors[:10]:  # Show first 10 errors
            print(f"- {error}")
        if len(errors) > 10:
            print(f"... and {len(errors) - 10} more errors")
    
    # Final count
    final_count = MCQ.objects.count()
    print(f"\nFinal MCQ count in database: {final_count}")