#!/usr/bin/env python
"""
Import MCQs from output_by_specialty folder with proper format conversion.
This script converts the new MCQ format to match the existing database structure.
"""

import os
import sys
import json
import django
from pathlib import Path

# Setup Django environment
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
django.setup()

from mcq.models import MCQ
from django.db import transaction
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Path to the output_by_specialty folder
SOURCE_FOLDER = "/Users/tariqalmatrudi/Documents/FFF/output_by_specialty"

# Updated mapping - now includes follow_up_guidelines
SECTION_MAPPING = {
    'option_analysis': 'option_analysis',
    'conceptual_foundation': 'conceptual_foundation',
    'pathophysiology': 'pathophysiological_mechanisms',
    'clinical_manifestation': 'clinical_correlation',
    'diagnostic_approach': 'diagnostic_approach',
    'management_principles': 'management_principles',
    'follow_up_guidelines': 'follow_up_guidelines',  # Now properly mapped
    'clinical_pearls': 'clinical_pearls',
    'references': 'current_evidence',
    'classification_and_nosology': 'classification_and_nosology'
}

def convert_explanation_format(explanation_obj):
    """Convert new explanation format to existing database format."""
    if not explanation_obj:
        return None
    
    converted_sections = {}
    
    for new_key, old_key in SECTION_MAPPING.items():
        if new_key in explanation_obj and old_key is not None:
            value = explanation_obj[new_key]
            
            # Special handling for clinical_pearls (array to text)
            if new_key == 'clinical_pearls' and isinstance(value, list):
                value = '\n'.join([f"• {pearl}" for pearl in value])
            
            # Store the value directly without merging
            converted_sections[old_key] = value
    
    return converted_sections

def convert_options_format(options_array):
    """Convert options from array format to dictionary format."""
    if not options_array:
        return {}
    
    options_dict = {}
    for i, option in enumerate(options_array):
        letter = chr(65 + i)  # A, B, C, D...
        options_dict[letter] = option
    
    return options_dict

def import_mcqs_from_file(filepath):
    """Import MCQs from a single JSON file."""
    logger.info(f"Processing file: {filepath}")
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Handle both formats: direct list or object with mcqs array
        if isinstance(data, dict) and 'mcqs' in data:
            mcqs_data = data['mcqs']
            specialty = data.get('specialty', 'Unknown')
            logger.info(f"Processing {specialty} specialty with {len(mcqs_data)} MCQs")
        elif isinstance(data, list):
            mcqs_data = data
            # Get the subspecialty from filename if not in data
            filename = os.path.basename(filepath)
            specialty = filename.replace('_mcqs.json', '').replace('_', ' ').title()
        else:
            logger.error(f"Unexpected data format in {filepath}")
            return 0, 0
        
        # Get the subspecialty from filename or data
        filename = os.path.basename(filepath)
        subspecialty = filename.replace('_mcqs.json', '').replace('_', ' ').title()
        
        imported_count = 0
        error_count = 0
        
        for mcq_data in mcqs_data:
            try:
                # Check if MCQ already exists (by question text and exam year)
                existing = MCQ.objects.filter(
                    question_text=mcq_data.get('question', ''),
                    exam_year=mcq_data.get('exam_year', '')
                ).first()
                
                if existing:
                    logger.info(f"Skipping duplicate MCQ: {mcq_data.get('question_number', 'Unknown')}")
                    continue
                
                # Convert explanation format
                explanation_sections = None
                if 'explanation' in mcq_data and isinstance(mcq_data['explanation'], dict):
                    explanation_sections = convert_explanation_format(mcq_data['explanation'])
                
                # Convert options format
                options = convert_options_format(mcq_data.get('options', []))
                
                # Create MCQ object
                mcq = MCQ(
                    question_number=mcq_data.get('question_number', ''),
                    question_text=mcq_data.get('question', ''),
                    options=options,
                    correct_answer=mcq_data.get('correct_answer', ''),
                    correct_answer_text=mcq_data.get('correct_answer_text', ''),
                    subspecialty=mcq_data.get('subspecialty', subspecialty),
                    exam_type=mcq_data.get('exam_type', ''),
                    exam_year=mcq_data.get('exam_year', ''),
                    source_file=filename,
                    ai_generated=mcq_data.get('ai_generated', False),
                    explanation_sections=explanation_sections,
                    # Set explanation to None since we're using explanation_sections
                    explanation=None,
                )
                
                mcq.save()
                imported_count += 1
                logger.info(f"Imported MCQ {mcq.question_number} from {filename}")
                
            except Exception as e:
                logger.error(f"Error importing MCQ: {str(e)}")
                error_count += 1
                continue
        
        logger.info(f"Completed {filename}: {imported_count} imported, {error_count} errors")
        return imported_count, error_count
        
    except Exception as e:
        logger.error(f"Error reading file {filepath}: {str(e)}")
        return 0, 0

def main():
    """Main import function."""
    source_path = Path(SOURCE_FOLDER)
    
    if not source_path.exists():
        logger.error(f"Source folder not found: {SOURCE_FOLDER}")
        return
    
    # Get all JSON files in the folder
    json_files = list(source_path.glob("*.json"))
    
    if not json_files:
        logger.error(f"No JSON files found in {SOURCE_FOLDER}")
        return
    
    logger.info(f"Found {len(json_files)} JSON files to process")
    
    total_imported = 0
    total_errors = 0
    
    # Process each file
    with transaction.atomic():
        for json_file in json_files:
            logger.info(f"\nProcessing {json_file.name}...")
            imported, errors = import_mcqs_from_file(json_file)
            total_imported += imported
            total_errors += errors
    
    # Final summary
    logger.info("\n" + "="*50)
    logger.info(f"IMPORT COMPLETE")
    logger.info(f"Total files processed: {len(json_files)}")
    logger.info(f"Total MCQs imported: {total_imported}")
    logger.info(f"Total errors: {total_errors}")
    logger.info(f"Total MCQs in database: {MCQ.objects.count()}")
    logger.info("="*50)

if __name__ == "__main__":
    main()