#!/usr/bin/env python3
"""
Import new MCQs from output_by_specialty directory to Heroku
Handles both unified and subsection explanation formats
"""

import os
import sys
import json
import glob
from datetime import datetime

# Add Django settings
sys.path.append('/app/django_neurology_mcq')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')

import django
django.setup()

from mcq.models import MCQ


def process_explanation(mcq_data):
    """
    Process explanation data from either unified or subsection format
    Returns structured explanation_sections dictionary
    """
    explanation_sections = {}
    
    # Check if we have a unified explanation
    if 'unified_explanation' in mcq_data and mcq_data['unified_explanation']:
        # This is a unified explanation format
        unified_text = mcq_data['unified_explanation']
        
        # Store the unified explanation in the main explanation field
        explanation = unified_text
        
        # Try to extract any subsection data if available
        if 'explanation' in mcq_data and isinstance(mcq_data['explanation'], dict):
            exp_dict = mcq_data['explanation']
            
            # Map the sections
            section_mapping = {
                'option_analysis': 'option_analysis',
                'conceptual_foundation': 'conceptual_foundation',
                'pathophysiology': 'pathophysiology',
                'clinical_manifestation': 'clinical_manifestation',
                'diagnostic_approach': 'diagnostic_approach',
                'management_principles': 'management_principles',
                'follow_up_guidelines': 'follow_up_guidelines',
                'clinical_pearls': 'clinical_pearls',
                'references': 'references'
            }
            
            for old_key, new_key in section_mapping.items():
                if old_key in exp_dict and exp_dict[old_key] and \
                   not exp_dict[old_key].startswith("This section information is included"):
                    explanation_sections[new_key] = exp_dict[old_key]
        
    elif 'explanation' in mcq_data and isinstance(mcq_data['explanation'], dict):
        # This is a subsection format
        exp_dict = mcq_data['explanation']
        
        # Build a complete explanation from subsections
        explanation_parts = []
        
        if exp_dict.get('option_analysis'):
            explanation_parts.append(f"**Option Analysis:**\n{exp_dict['option_analysis']}")
        
        if exp_dict.get('conceptual_foundation'):
            explanation_parts.append(f"**Conceptual Foundation:**\n{exp_dict['conceptual_foundation']}")
            
        if exp_dict.get('pathophysiology'):
            explanation_parts.append(f"**Pathophysiology:**\n{exp_dict['pathophysiology']}")
            
        if exp_dict.get('clinical_manifestation'):
            explanation_parts.append(f"**Clinical Manifestation:**\n{exp_dict['clinical_manifestation']}")
            
        if exp_dict.get('diagnostic_approach'):
            explanation_parts.append(f"**Diagnostic Approach:**\n{exp_dict['diagnostic_approach']}")
            
        if exp_dict.get('management_principles'):
            explanation_parts.append(f"**Management Principles:**\n{exp_dict['management_principles']}")
            
        if exp_dict.get('follow_up_guidelines'):
            explanation_parts.append(f"**Follow-up Guidelines:**\n{exp_dict['follow_up_guidelines']}")
            
        if exp_dict.get('clinical_pearls'):
            if isinstance(exp_dict['clinical_pearls'], list):
                pearls_text = '\n'.join(f"• {pearl}" for pearl in exp_dict['clinical_pearls'])
            else:
                pearls_text = exp_dict['clinical_pearls']
            explanation_parts.append(f"**Clinical Pearls:**\n{pearls_text}")
            
        if exp_dict.get('references'):
            explanation_parts.append(f"**References:**\n{exp_dict['references']}")
        
        explanation = '\n\n'.join(explanation_parts) if explanation_parts else ""
        
        # Also store structured sections
        explanation_sections = {
            'option_analysis': exp_dict.get('option_analysis', ''),
            'conceptual_foundation': exp_dict.get('conceptual_foundation', ''),
            'pathophysiology': exp_dict.get('pathophysiology', ''),
            'clinical_manifestation': exp_dict.get('clinical_manifestation', ''),
            'diagnostic_approach': exp_dict.get('diagnostic_approach', ''),
            'management_principles': exp_dict.get('management_principles', ''),
            'follow_up_guidelines': exp_dict.get('follow_up_guidelines', ''),
            'clinical_pearls': exp_dict.get('clinical_pearls', []),
            'references': exp_dict.get('references', '')
        }
    else:
        # No structured explanation
        explanation = mcq_data.get('explanation', '') or ''
        
    return explanation, explanation_sections


def import_mcqs_from_directory(directory_path):
    """
    Import all MCQs from the output_by_specialty directory
    """
    print(f"Starting MCQ import from {directory_path}")
    
    # Get all JSON files
    json_files = glob.glob(os.path.join(directory_path, '*.json'))
    print(f"Found {len(json_files)} JSON files to process")
    
    total_imported = 0
    errors = []
    
    for json_file in json_files:
        filename = os.path.basename(json_file)
        
        # Skip non-MCQ files
        if filename in ['reorganization_summary.txt']:
            continue
            
        print(f"\nProcessing {filename}...")
        
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            specialty = data.get('specialty', 'Unknown')
            mcqs = data.get('mcqs', [])
            
            print(f"  Specialty: {specialty}")
            print(f"  MCQs to import: {len(mcqs)}")
            
            # Import each MCQ
            for idx, mcq_data in enumerate(mcqs):
                try:
                    # Process explanation
                    explanation, explanation_sections = process_explanation(mcq_data)
                    
                    # Prepare MCQ data
                    mcq_obj = MCQ(
                        question_number=mcq_data.get('question_number', ''),
                        question_text=mcq_data.get('question', ''),
                        options=mcq_data.get('options', {}),
                        correct_answer=mcq_data.get('correct_answer', ''),
                        subspecialty=mcq_data.get('subspecialty', specialty),
                        source_file=mcq_data.get('source_file', filename),
                        exam_type=mcq_data.get('exam_type', ''),
                        exam_year=mcq_data.get('exam_year'),
                        explanation=explanation,
                        explanation_sections=explanation_sections if explanation_sections else None,
                        image_url=mcq_data.get('image_url', '')
                    )
                    
                    # Save the MCQ
                    mcq_obj.save()
                    total_imported += 1
                    
                    if (idx + 1) % 50 == 0:
                        print(f"    Imported {idx + 1}/{len(mcqs)} MCQs...")
                        
                except Exception as e:
                    error_msg = f"Error importing MCQ {idx} from {filename}: {str(e)}"
                    print(f"    ERROR: {error_msg}")
                    errors.append(error_msg)
            
            print(f"  Successfully imported {len(mcqs)} MCQs from {filename}")
            
        except Exception as e:
            error_msg = f"Error processing file {filename}: {str(e)}"
            print(f"  ERROR: {error_msg}")
            errors.append(error_msg)
    
    # Summary
    print(f"\n{'='*60}")
    print(f"Import Summary:")
    print(f"  Total MCQs imported: {total_imported}")
    print(f"  Total errors: {len(errors)}")
    
    if errors:
        print(f"\nErrors encountered:")
        for error in errors[:10]:  # Show first 10 errors
            print(f"  - {error}")
        if len(errors) > 10:
            print(f"  ... and {len(errors) - 10} more errors")
    
    return total_imported, errors


def main():
    """
    Main function to orchestrate the import process
    """
    # First, delete all existing MCQs
    print("Deleting existing MCQs...")
    existing_count = MCQ.objects.count()
    MCQ.objects.all().delete()
    print(f"Deleted {existing_count} existing MCQs")
    
    # Import new MCQs
    directory_path = '/Users/tariqalmatrudi/Documents/FFF/output_by_specialty'
    total_imported, errors = import_mcqs_from_directory(directory_path)
    
    # Verify import
    final_count = MCQ.objects.count()
    print(f"\nFinal verification:")
    print(f"  MCQs in database: {final_count}")
    
    # Get subspecialty distribution
    subspecialties = MCQ.objects.values_list('subspecialty', flat=True).distinct()
    print(f"  Subspecialties: {len(subspecialties)}")
    for subspecialty in sorted(subspecialties):
        count = MCQ.objects.filter(subspecialty=subspecialty).count()
        print(f"    - {subspecialty}: {count} MCQs")


if __name__ == "__main__":
    main()