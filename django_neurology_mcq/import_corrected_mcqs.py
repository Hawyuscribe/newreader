#!/usr/bin/env python3
"""
Import corrected MCQs from CSV files and replace existing MCQs for each subspecialty.
"""

import os
import sys
import csv
import json
import logging
import pandas as pd
from datetime import datetime
from pathlib import Path
from django.core.management.base import BaseCommand
from django.conf import settings
from django.db import transaction
from django.utils import timezone

# Set up Django environment
import django
import os

# Setup Django - fix path to point to current directory
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

# Now import models and utils
from mcq.models import MCQ
from mcq.utils import is_nan_like, clean_option_text, normalize_option_letter

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(f"import_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Directory containing CSV files
CSV_DIR = "/Users/tariqalmatrudi/Documents/MCQs for the board/test"

# Map CSV filenames to subspecialty names in the database
SUBSPECIALTY_MAPPING = {
    "critical_care_neurology": "Critical Care Neurology",
    "dementia": "Dementia",
    "epilepsy": "Epilepsy",
    "headache": "Headache",
    "movement_disorders": "Movement Disorders",
    "neuro_infectious": "Neuro-infectious",
    "neuro-infectious": "Neuro-infectious",
    "neuro-oncology": "Neuro-oncology",
    "neuro-otology": "Neuro-otology",
    "neuroanatomy": "Neuroanatomy",
    "neurogenetics": "Neurogenetics",
    "neuroimmunology": "Neuroimmunology",
    "neuromuscular": "Neuromuscular",
    "neuroophthalmology": "Neuroophthalmology",
    "neuropsychiatry": "Neuropsychiatry",
    "other_unclassified": "Other/Unclassified",
    "pediatric_neurology": "Pediatric Neurology",
    "sleep_neurology": "Sleep Neurology",
    "vascular": "Vascular Neurology/Stroke"
}

def normalize_subspecialty_name(filename):
    """Extract subspecialty name from CSV filename and normalize it."""
    for key in SUBSPECIALTY_MAPPING.keys():
        if key in filename.lower():
            return SUBSPECIALTY_MAPPING[key]
    
    # If no match found, try to extract from filename
    base_name = os.path.basename(filename).lower()
    parts = base_name.split('_')
    if parts:
        subspecialty = parts[0]
        if subspecialty in SUBSPECIALTY_MAPPING:
            return SUBSPECIALTY_MAPPING[subspecialty]
    
    logger.warning(f"Could not determine subspecialty for {filename}")
    return None

def backup_existing_mcqs(subspecialty):
    """Create a backup of existing MCQs for a specific subspecialty."""
    mcqs = MCQ.objects.filter(subspecialty=subspecialty)
    
    if not mcqs.exists():
        logger.info(f"No existing MCQs found for {subspecialty} to backup")
        return
    
    # Create backups directory if it doesn't exist
    backup_dir = Path("mcq_backups")
    backup_dir.mkdir(exist_ok=True)
    
    # Create backup file
    backup_file = backup_dir / f"{subspecialty.replace('/', '_').replace(' ', '_')}_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    
    # Prepare data for serialization
    backup_data = []
    for mcq in mcqs:
        mcq_data = {
            'id': mcq.id,
            'question_number': mcq.question_number,
            'question_text': mcq.question_text,
            'options': mcq.options,
            'correct_answer': mcq.correct_answer,
            'subspecialty': mcq.subspecialty,
            'exam_type': mcq.exam_type,
            'exam_year': mcq.exam_year,
            'explanation': mcq.explanation,
            'explanation_sections': mcq.explanation_sections,
            'source_file': mcq.source_file,
            'image_url': mcq.image_url if hasattr(mcq, 'image_url') else None
        }
        backup_data.append(mcq_data)
    
    # Write to file
    with open(backup_file, 'w', encoding='utf-8') as f:
        json.dump(backup_data, f, indent=2, ensure_ascii=False)
    
    logger.info(f"Created backup of {len(backup_data)} MCQs for {subspecialty} at {backup_file}")
    return backup_file

def extract_explanation_sections(row):
    """Extract explanation sections from a CSV row."""
    explanation_sections = {}
    
    # Map CSV columns to explanation section keys
    section_mappings = {
        'Conceptual Foundation': 'conceptual_foundation',
        'Pathophysiology': 'pathophysiology',
        'Clinical Correlation': 'clinical_correlation',
        'Diagnostic Approach': 'diagnostic_approach',
        'Classification and Neurology': 'classification_and_neurology',
        'Management Principles': 'management_principles',
        'Option Analysis': 'option_analysis',
        'Clinical Pearls': 'clinical_pearls',
        'Current Evidence': 'current_evidence'
    }
    
    for csv_key, section_key in section_mappings.items():
        if csv_key in row and row[csv_key]:
            # Skip NaN-like values
            if not is_nan_like(row[csv_key]):
                explanation_sections[section_key] = row[csv_key]
    
    return explanation_sections

def extract_options(row):
    """Extract options from CSV row and handle missing options."""
    options = {}
    
    # First try to get from option columns
    for option_letter in ['A', 'B', 'C', 'D', 'E', 'F']:
        option_key = f'Option {option_letter}'
        if option_key in row and row[option_key]:
            # Skip if the value is NaN-like
            if not is_nan_like(row[option_key]):
                # Clean the option text
                clean_text = clean_option_text(row[option_key])
                if clean_text:
                    options[option_letter] = clean_text
    
    # If no options found and option analysis exists, try to extract from there
    if not options and 'Option Analysis' in row and row['Option Analysis']:
        option_analysis = row['Option Analysis']
        # Skip if the option analysis is NaN-like
        if is_nan_like(option_analysis):
            return options
        
        # Look for patterns like "Option A: text" or "Option A (text): description"
        import re
        option_patterns = [
            r'Option\s+([A-F])\s*(?:\([^)]*\))?\s*:\s*([^.]+)',  # Option A: text
            r'Option\s+([A-F])\s*\(([^)]+)\)',                  # Option A (text)
            r'Option\s+([A-F])\s*–\s*([^.]+)',                  # Option A – text
            r'([A-F])\s*:\s*([^.]+)'                            # A: text
        ]
        
        for pattern in option_patterns:
            matches = re.findall(pattern, option_analysis)
            for match in matches:
                if len(match) >= 2:
                    letter = normalize_option_letter(match[0])
                    text = clean_option_text(match[1])
                    if letter and text:
                        options[letter] = text
    
    return options

def import_mcqs_from_csv(csv_file):
    """Import MCQs from a CSV file."""
    subspecialty = normalize_subspecialty_name(csv_file)
    if not subspecialty:
        logger.error(f"Could not determine subspecialty for {csv_file}")
        return 0, 0
    
    logger.info(f"Importing MCQs for subspecialty: {subspecialty} from {csv_file}")
    
    # Backup existing MCQs
    backup_file = backup_existing_mcqs(subspecialty)
    
    # Read CSV file with pandas to handle large files and proper encoding
    try:
        df = pd.read_csv(csv_file, encoding='utf-8')
        logger.info(f"Read {len(df)} rows from {csv_file}")
    except Exception as e:
        logger.error(f"Error reading CSV file {csv_file}: {e}")
        return 0, 0
    
    # Convert to dict for processing
    rows = df.to_dict('records')
    
    # Start a transaction to safely update the database
    success_count = 0
    error_count = 0
    
    with transaction.atomic():
        # Delete all existing MCQs for this subspecialty
        deleted_count = MCQ.objects.filter(subspecialty=subspecialty).delete()[0]
        logger.info(f"Deleted {deleted_count} existing MCQs for {subspecialty}")
        
        # Import new MCQs
        new_mcqs = []
        
        for row in rows:
            try:
                # Skip rows without critical fields
                if not row.get('Question Text'):
                    logger.warning(f"Skipping row with missing question text: {row.get('ID')}")
                    error_count += 1
                    continue
                
                # Check if correct answer is NaN-like
                correct_answer = row.get('Correct Answer')
                if is_nan_like(correct_answer):
                    logger.warning(f"Skipping row with missing or invalid correct answer: {row.get('ID')}")
                    error_count += 1
                    continue
                
                # Normalize correct answer (make sure it's a single uppercase letter)
                correct_answer = normalize_option_letter(correct_answer)
                if not correct_answer:
                    logger.warning(f"Skipping row with invalid correct answer format: {row.get('ID')}")
                    error_count += 1
                    continue
                
                # Extract options and explanation sections
                options = extract_options(row)
                explanation_sections = extract_explanation_sections(row)
                
                # Verify that the correct answer matches one of the options
                if options and correct_answer not in options:
                    logger.warning(f"Correct answer '{correct_answer}' not found in options for MCQ {row.get('ID')}. Options: {options}")
                
                # Parse exam year
                exam_year = None
                if 'Exam Year' in row and row['Exam Year']:
                    try:
                        if not is_nan_like(row['Exam Year']):
                            exam_year = int(row['Exam Year'])
                    except (ValueError, TypeError):
                        logger.warning(f"Invalid exam year: {row['Exam Year']} for MCQ {row.get('ID')}")
                
                # Determine exam type
                exam_type = row.get('Exam Type')
                if is_nan_like(exam_type):
                    exam_type = MCQ.OTHER
                elif exam_type and exam_type not in [MCQ.PART_I, MCQ.PART_II, MCQ.PROMOTION, MCQ.OTHER]:
                    # Try to normalize exam type
                    if exam_type.lower() == 'part i' or exam_type.lower() == 'part 1':
                        exam_type = MCQ.PART_I
                    elif exam_type.lower() == 'part ii' or exam_type.lower() == 'part 2':
                        exam_type = MCQ.PART_II
                    elif 'promotion' in exam_type.lower():
                        exam_type = MCQ.PROMOTION
                    else:
                        exam_type = MCQ.OTHER
                
                # Prepare image URL
                image_url = row.get('Image URL') if 'Image URL' in row and not is_nan_like(row.get('Image URL')) else None
                
                # Create new MCQ object
                new_mcq = MCQ(
                    id=row.get('ID'),  # Use original ID if available
                    question_number=row.get('Question Number'),
                    question_text=row.get('Question Text'),
                    options=options,
                    correct_answer=correct_answer,
                    subspecialty=subspecialty,
                    exam_type=exam_type,
                    exam_year=exam_year,
                    explanation_sections=explanation_sections,
                    source_file=row.get('Source File'),
                    image_url=image_url
                )
                
                new_mcqs.append(new_mcq)
                success_count += 1
            
            except Exception as e:
                logger.error(f"Error processing row: {e}")
                logger.error(f"Problematic row: {row.get('ID')}")
                error_count += 1
        
        # Bulk create new MCQs
        MCQ.objects.bulk_create(new_mcqs, batch_size=100)
        logger.info(f"Successfully created {success_count} new MCQs for {subspecialty}")
    
    return success_count, error_count

def import_all_csv_files():
    """Import MCQs from all CSV files in the directory."""
    csv_files = [f for f in os.listdir(CSV_DIR) if f.endswith('.csv')]
    if not csv_files:
        logger.error(f"No CSV files found in {CSV_DIR}")
        return
    
    logger.info(f"Found {len(csv_files)} CSV files for import")
    
    total_success = 0
    total_errors = 0
    
    for csv_file in csv_files:
        file_path = os.path.join(CSV_DIR, csv_file)
        success, errors = import_mcqs_from_csv(file_path)
        
        total_success += success
        total_errors += errors
    
    logger.info(f"=== Import Summary ===")
    logger.info(f"Successfully imported {total_success} MCQs")
    logger.info(f"Encountered {total_errors} errors during import")
    logger.info(f"Total processed: {total_success + total_errors}")

def import_single_subspecialty(subspecialty_name):
    """Import MCQs for a specific subspecialty."""
    csv_files = [f for f in os.listdir(CSV_DIR) if f.endswith('.csv')]
    
    for csv_file in csv_files:
        if subspecialty_name.lower() in csv_file.lower():
            file_path = os.path.join(CSV_DIR, csv_file)
            success, errors = import_mcqs_from_csv(file_path)
            
            logger.info(f"=== Import Summary for {subspecialty_name} ===")
            logger.info(f"Successfully imported {success} MCQs")
            logger.info(f"Encountered {errors} errors during import")
            logger.info(f"Total processed: {success + errors}")
            return success, errors
    
    logger.error(f"No CSV file found for subspecialty {subspecialty_name}")
    return 0, 0

if __name__ == "__main__":
    # Check if a specific subspecialty name was provided
    if len(sys.argv) > 1:
        subspecialty_name = sys.argv[1]
        logger.info(f"Importing MCQs for subspecialty: {subspecialty_name}")
        import_single_subspecialty(subspecialty_name)
    else:
        logger.info("Importing MCQs from all CSV files")
        import_all_csv_files()