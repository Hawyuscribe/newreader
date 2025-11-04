#!/usr/bin/env python3
"""
Import MCQs from JSON chunk
Usage: python import_mcq_chunk.py <chunk_file>
"""
import os
import sys
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
sys.path.insert(0, '/app/django_neurology_mcq')

import django
django.setup()

from mcq.models import MCQ

def import_chunk(chunk_file):
    with open(chunk_file, 'r') as f:
        mcqs = json.load(f)
    
    imported = 0
    errors = []
    
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
                    
                    if exp_dict.get('option_analysis'):
                        parts.append(f"**Option Analysis:**\n{exp_dict['option_analysis']}")
                    if exp_dict.get('conceptual_foundation'):
                        parts.append(f"**Conceptual Foundation:**\n{exp_dict['conceptual_foundation']}")
                    if exp_dict.get('pathophysiology'):
                        parts.append(f"**Pathophysiology:**\n{exp_dict['pathophysiology']}")
                    if exp_dict.get('clinical_manifestation'):
                        parts.append(f"**Clinical Manifestation:**\n{exp_dict['clinical_manifestation']}")
                    if exp_dict.get('diagnostic_approach'):
                        parts.append(f"**Diagnostic Approach:**\n{exp_dict['diagnostic_approach']}")
                    if exp_dict.get('management_principles'):
                        parts.append(f"**Management Principles:**\n{exp_dict['management_principles']}")
                    if exp_dict.get('follow_up_guidelines'):
                        parts.append(f"**Follow-up Guidelines:**\n{exp_dict['follow_up_guidelines']}")
                    
                    if exp_dict.get('clinical_pearls'):
                        if isinstance(exp_dict['clinical_pearls'], list):
                            pearls_text = '\n'.join(f"• {pearl}" for pearl in exp_dict['clinical_pearls'])
                        else:
                            pearls_text = exp_dict['clinical_pearls']
                        parts.append(f"**Clinical Pearls:**\n{pearls_text}")
                    
                    if exp_dict.get('references'):
                        parts.append(f"**References:**\n{exp_dict['references']}")
                    
                    explanation = '\n\n'.join(parts)
                    
                    # Also save structured sections
                    for key in ['option_analysis', 'conceptual_foundation', 'pathophysiology', 
                               'clinical_manifestation', 'diagnostic_approach', 'management_principles',
                               'follow_up_guidelines', 'clinical_pearls', 'references']:
                        if key in exp_dict and exp_dict[key]:
                            if not (isinstance(exp_dict[key], str) and exp_dict[key].startswith("This section information")):
                                explanation_sections[key] = exp_dict[key]
                else:
                    explanation = mcq_data.get('explanation', '')
            
            mcq_obj = MCQ(
                question_number=mcq_data.get('question_number', ''),
                question_text=mcq_data.get('question', ''),
                options=mcq_data.get('options', {}),
                correct_answer=mcq_data.get('correct_answer', ''),
                subspecialty=mcq_data.get('subspecialty', mcq_data.get('import_specialty', '')),
                source_file=mcq_data.get('source_file', mcq_data.get('import_source', '')),
                exam_type=mcq_data.get('exam_type', ''),
                exam_year=mcq_data.get('exam_year'),
                explanation=explanation,
                explanation_sections=explanation_sections if explanation_sections else None,
                image_url=mcq_data.get('image_url', '')
            )
            
            mcq_obj.save()
            imported += 1
            
        except Exception as e:
            errors.append(str(e))
    
    print(f"Imported {imported} MCQs from {os.path.basename(chunk_file)}")
    if errors:
        print(f"Errors: {len(errors)}")
        for e in errors[:5]:
            print(f"  - {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python import_mcq_chunk.py <chunk_file>")
        sys.exit(1)
    
    import_chunk(sys.argv[1])
