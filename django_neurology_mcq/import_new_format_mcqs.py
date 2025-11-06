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

# Mapping for section names from new format to existing format
SECTION_MAPPING = {
    'conceptual_foundation': 'conceptual_foundation',
    'pathophysiology': 'pathophysiological_mechanisms',
    'clinical_manifestation': 'clinical_correlation',
    'diagnostic_approach': 'diagnostic_approach',
    'management_principles': 'management_principles',
    'option_analysis': 'option_analysis',
    'clinical_pearls': 'clinical_pearls',
    'references': 'current_evidence',
    'follow_up_guidelines': None,  # This section doesn't exist in current format
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
            
            # Special handling for references (merge with follow_up_guidelines if exists)
            if new_key == 'references' and 'follow_up_guidelines' in explanation_obj:
                follow_up = explanation_obj.get('follow_up_guidelines', '')
                if follow_up:
                    value = f"{value}\n\n**Follow-up Guidelines:**\n{follow_up}"
            
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

def import_mcqs_from_file(file_path):
    """Import MCQs from a single JSON file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Handle both formats: direct list or object with mcqs array
        if isinstance(data, dict) and 'mcqs' in data:
            mcqs_data = data['mcqs']
            specialty = data.get('specialty', 'Unknown')
            logger.info(f"Processing {specialty} specialty with {len(mcqs_data)} MCQs")
        elif isinstance(data, list):
            mcqs_data = data
        else:
            logger.error(f"Invalid file format in {file_path}: expected list or dict with 'mcqs', got {type(data)}")
            return 0, 0
        
        imported = 0
        skipped = 0
        
        for mcq_data in mcqs_data:
            try:
                # Check if MCQ already exists (by question text and exam year)
                existing = MCQ.objects.filter(
                    question_text=mcq_data.get('question', ''),
                    exam_year=mcq_data.get('exam_year', '')
                ).first()
                
                if existing:
                    logger.info(f"Skipping duplicate MCQ: {mcq_data.get('question_number', 'Unknown')}")
                    skipped += 1
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
                    subspecialty=mcq_data.get('subspecialty', 'Other/Unclassified'),
                    exam_type=mcq_data.get('exam_type', ''),
                    exam_year=mcq_data.get('exam_year', ''),
                    source_file=mcq_data.get('source_file', file_path.name),
                    ai_generated=mcq_data.get('ai_generated', False),
                    explanation_sections=explanation_sections,
                    # Set explanation to None since we're using explanation_sections
                    explanation=None,
                )
                
                mcq.save()
                imported += 1
                logger.info(f"Imported MCQ {mcq.question_number} from {file_path.name}")
                
            except Exception as e:
                logger.error(f"Error importing MCQ from {file_path}: {str(e)}")
                continue
        
        return imported, skipped
        
    except Exception as e:
        logger.error(f"Error reading file {file_path}: {str(e)}")
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
    total_skipped = 0
    
    # Process each file
    with transaction.atomic():
        for json_file in json_files:
            logger.info(f"\nProcessing {json_file.name}...")
            imported, skipped = import_mcqs_from_file(json_file)
            total_imported += imported
            total_skipped += skipped
            logger.info(f"Completed {json_file.name}: {imported} imported, {skipped} skipped")
    
    # Final summary
    logger.info("\n" + "="*50)
    logger.info(f"IMPORT COMPLETE")
    logger.info(f"Total files processed: {len(json_files)}")
    logger.info(f"Total MCQs imported: {total_imported}")
    logger.info(f"Total MCQs skipped (duplicates): {total_skipped}")
    logger.info(f"Total MCQs in database: {MCQ.objects.count()}")
    logger.info("="*50)

if __name__ == "__main__":
    main()