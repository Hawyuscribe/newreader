#\!/usr/bin/env python3
"""
Direct MCQ import from URL for Heroku
This script downloads MCQ data from a URL and imports it directly
"""
import os
import sys
import django
import json
import requests
from django.db import transaction

# Django setup
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
django.setup()

from mcq.models import MCQ

def import_mcqs_from_url(url):
    """Download and import MCQs from a URL"""
    print(f"Downloading MCQs from: {url}")
    
    try:
        response = requests.get(url, timeout=300)
        response.raise_for_status()
        mcqs_data = response.json()
        
        if isinstance(mcqs_data, dict) and 'mcqs' in mcqs_data:
            mcqs = mcqs_data['mcqs']
        else:
            mcqs = mcqs_data
            
        print(f"Downloaded {len(mcqs)} MCQs")
        
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
                                    parts.append(f"**{title}:**\n{content}")
                                    explanation_sections[key] = content
                        
                        explanation = '\n\n'.join(parts)
                    
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
                        question_text=mcq_data.get('question', mcq_data.get('question_text', '')),
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
                    imported += 1
                    
                    if imported % 100 == 0:
                        print(f"Progress: {imported} MCQs imported...")
                        
                except Exception as e:
                    error_msg = f"MCQ {mcq_data.get('question_number', 'unknown')}: {str(e)}"
                    errors.append(error_msg)
                    if len(errors) <= 5:
                        print(f"Error: {error_msg}")
        
        return imported, errors
        
    except Exception as e:
        print(f"Error downloading/importing: {e}")
        return 0, [str(e)]

def main():
    """Main import function"""
    print("=== Direct MCQ Import from URL ===")
    
    # Check current MCQ count
    current_count = MCQ.objects.count()
    print(f"Current MCQ count: {current_count}")
    
    if current_count > 0:
        print(f"Clearing {current_count} existing MCQs...")
        MCQ.objects.all().delete()
        print("✓ Cleared")
    
    # URLs to import from
    # These would be URLs where the MCQ JSON files are hosted
    urls = [
        # Add URLs here
    ]
    
    # Also check environment variable
    import_url = os.environ.get('MCQ_IMPORT_URL')
    if import_url:
        urls = [import_url]
    
    if not urls:
        print("No URLs provided. Set MCQ_IMPORT_URL environment variable.")
        return
    
    total_imported = 0
    total_errors = []
    
    for url in urls:
        print(f"\nImporting from: {url}")
        imported, errors = import_mcqs_from_url(url)
        total_imported += imported
        total_errors.extend(errors)
    
    print(f"\n=== Import Summary ===")
    print(f"Total MCQs imported: {total_imported}")
    print(f"Total errors: {len(total_errors)}")
    print(f"Final MCQ count: {MCQ.objects.count()}")
    
    if total_errors:
        print(f"\nShowing first 10 errors:")
        for error in total_errors[:10]:
            print(f"- {error}")

if __name__ == "__main__":
    main()
