import os
import csv
import json
import logging
import pandas as pd
from datetime import datetime
from pathlib import Path
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone

from mcq.models import MCQ
from mcq.utils import is_nan_like, clean_option_text, normalize_option_letter

class Command(BaseCommand):
    help = 'Import corrected MCQs from CSV files and replace existing MCQs for each subspecialty'

    def add_arguments(self, parser):
        parser.add_argument('--csv-dir', default="/Users/tariqalmatrudi/Documents/MCQs for the board/test",
                          help='Directory containing CSV files')
        parser.add_argument('--subspecialty', help='Import only specific subspecialty')
        parser.add_argument('--dry-run', action='store_true', help='Run without modifying the database')

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
        "vascular": "Vascular Neurology/Stroke",
    }

    def normalize_subspecialty_name(self, filename):
        """Extract subspecialty name from CSV filename and normalize it."""
        for key in self.SUBSPECIALTY_MAPPING.keys():
            if key in filename.lower():
                return self.SUBSPECIALTY_MAPPING[key]
        
        # If no match found, try to extract from filename
        base_name = os.path.basename(filename).lower()
        parts = base_name.split('_')
        if parts:
            subspecialty = parts[0]
            if subspecialty in self.SUBSPECIALTY_MAPPING:
                return self.SUBSPECIALTY_MAPPING[subspecialty]
        
        self.stdout.write(self.style.WARNING(f"Could not determine subspecialty for {filename}"))
        return None

    def backup_existing_mcqs(self, subspecialty):
        """Create a backup of existing MCQs for a specific subspecialty."""
        mcqs = MCQ.objects.filter(subspecialty=subspecialty)
        
        if not mcqs.exists():
            self.stdout.write(self.style.SUCCESS(f"No existing MCQs found for {subspecialty} to backup"))
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
        
        self.stdout.write(self.style.SUCCESS(f"Created backup of {len(backup_data)} MCQs for {subspecialty} at {backup_file}"))
        return backup_file

    def extract_explanation_sections(self, row):
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

    def extract_options(self, row):
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

    def import_mcqs_from_csv(self, csv_file, dry_run=False):
        """Import MCQs from a CSV file."""
        subspecialty = self.normalize_subspecialty_name(csv_file)
        if not subspecialty:
            self.stdout.write(self.style.ERROR(f"Could not determine subspecialty for {csv_file}"))
            return 0, 0
        
        self.stdout.write(self.style.SUCCESS(f"Importing MCQs for subspecialty: {subspecialty} from {csv_file}"))
        
        # Backup existing MCQs if not dry run
        if not dry_run:
            backup_file = self.backup_existing_mcqs(subspecialty)
        
        # Read CSV file with pandas to handle large files and proper encoding
        try:
            # Read CSV and replace NaN values with None for proper JSON handling
            df = pd.read_csv(csv_file, encoding='utf-8')
            
            # Fill NaN values with None for proper JSON serialization
            df = df.where(pd.notna(df), None)
            
            self.stdout.write(self.style.SUCCESS(f"Read {len(df)} rows from {csv_file}"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error reading CSV file {csv_file}: {e}"))
            return 0, 0
        
        # Convert to dict for processing
        rows = df.to_dict('records')
        
        success_count = 0
        error_count = 0
        
        # Start a transaction to safely update the database
        if not dry_run:
            with transaction.atomic():
                # Delete all existing MCQs for this subspecialty
                deleted_count = MCQ.objects.filter(subspecialty=subspecialty).delete()[0]
                self.stdout.write(self.style.SUCCESS(f"Deleted {deleted_count} existing MCQs for {subspecialty}"))
                
                # Import new MCQs - using individual create for better error handling
                for i, row in enumerate(rows):
                    try:
                        # Skip rows without critical fields
                        if not row.get('Question Text'):
                            self.stdout.write(self.style.WARNING(f"Skipping row with missing question text: {row.get('ID')}"))
                            error_count += 1
                            continue
                        
                        # Check if correct answer is NaN-like
                        correct_answer = row.get('Correct Answer')
                        if is_nan_like(correct_answer):
                            self.stdout.write(self.style.WARNING(f"Skipping row with missing or invalid correct answer: {row.get('ID')}"))
                            error_count += 1
                            continue
                        
                        # Normalize correct answer (make sure it's a single uppercase letter)
                        correct_answer = normalize_option_letter(correct_answer)
                        if not correct_answer:
                            self.stdout.write(self.style.WARNING(f"Skipping row with invalid correct answer format: {row.get('ID')}"))
                            error_count += 1
                            continue
                        
                        # Extract options and explanation sections
                        options = self.extract_options(row)
                        explanation_sections = self.extract_explanation_sections(row)
                        
                        # Verify that the correct answer matches one of the options
                        if options and correct_answer not in options:
                            self.stdout.write(self.style.WARNING(f"Correct answer '{correct_answer}' not found in options for MCQ {row.get('ID')}. Options: {options}"))
                        
                        # Parse exam year
                        exam_year = None
                        if 'Exam Year' in row and row['Exam Year']:
                            try:
                                if not is_nan_like(row['Exam Year']):
                                    exam_year = int(row['Exam Year'])
                            except (ValueError, TypeError):
                                self.stdout.write(self.style.WARNING(f"Invalid exam year: {row['Exam Year']} for MCQ {row.get('ID')}"))
                        
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
                        
                        # Debug options
                        if i == 0 or i == 1:
                            self.stdout.write(f"Options for row {i}: {options}")
                        
                        # Create new MCQ object - use create() instead of bulk_create
                        mcq_id = row.get('ID')
                        if mcq_id:
                            MCQ.objects.create(
                                id=mcq_id,
                                question_number=row.get('Question Number'),
                                question_text=row.get('Question Text'),
                                options={} if not options else options,
                                correct_answer=correct_answer,
                                subspecialty=subspecialty,
                                exam_type=exam_type,
                                exam_year=exam_year,
                                explanation_sections=explanation_sections,
                                source_file=row.get('Source File'),
                                image_url=image_url
                            )
                        else:
                            MCQ.objects.create(
                                question_number=row.get('Question Number'),
                                question_text=row.get('Question Text'),
                                options={} if not options else options,
                                correct_answer=correct_answer,
                                subspecialty=subspecialty,
                                exam_type=exam_type,
                                exam_year=exam_year,
                                explanation_sections=explanation_sections,
                                source_file=row.get('Source File'),
                                image_url=image_url
                            )
                            
                        success_count += 1
                        
                        # Log progress
                        if success_count % 50 == 0:
                            self.stdout.write(self.style.SUCCESS(f"Processed {success_count} MCQs..."))
                    
                    except Exception as e:
                        self.stdout.write(self.style.ERROR(f"Error processing row {i}: {e}"))
                        self.stdout.write(self.style.ERROR(f"Problematic row ID: {row.get('ID')}"))
                        if 'options' in locals():
                            self.stdout.write(self.style.ERROR(f"Options: {options}"))
                        error_count += 1
        else:
            # Dry run - just count the MCQs
            for row in rows:
                if row.get('Question Text') and row.get('Correct Answer'):
                    success_count += 1
                else:
                    error_count += 1
            self.stdout.write(self.style.SUCCESS(f"DRY RUN: Would import {success_count} MCQs for {subspecialty}"))
        
        return success_count, error_count

    def handle(self, *args, **options):
        csv_dir = options['csv_dir']
        target_subspecialty = options.get('subspecialty')
        dry_run = options.get('dry_run', False)
        
        if dry_run:
            self.stdout.write(self.style.WARNING("DRY RUN MODE - No changes will be made to the database"))
        
        csv_files = [f for f in os.listdir(csv_dir) if f.endswith('.csv')]
        if not csv_files:
            self.stdout.write(self.style.ERROR(f"No CSV files found in {csv_dir}"))
            return
        
        self.stdout.write(self.style.SUCCESS(f"Found {len(csv_files)} CSV files for import"))
        
        total_success = 0
        total_errors = 0
        
        if target_subspecialty:
            # Import specific subspecialty
            matching_files = [f for f in csv_files if target_subspecialty.lower() in f.lower()]
            if not matching_files:
                self.stdout.write(self.style.ERROR(f"No CSV file found for subspecialty {target_subspecialty}"))
                return
            
            file_path = os.path.join(csv_dir, matching_files[0])
            success, errors = self.import_mcqs_from_csv(file_path, dry_run)
            
            total_success += success
            total_errors += errors
        else:
            # Import all subspecialties
            for csv_file in csv_files:
                file_path = os.path.join(csv_dir, csv_file)
                success, errors = self.import_mcqs_from_csv(file_path, dry_run)
                
                total_success += success
                total_errors += errors
        
        self.stdout.write(self.style.SUCCESS(f"=== Import Summary ==="))
        if dry_run:
            self.stdout.write(self.style.SUCCESS(f"DRY RUN: Would import {total_success} MCQs"))
            self.stdout.write(self.style.SUCCESS(f"DRY RUN: Would encounter {total_errors} errors"))
        else:
            self.stdout.write(self.style.SUCCESS(f"Successfully imported {total_success} MCQs"))
            self.stdout.write(self.style.SUCCESS(f"Encountered {total_errors} errors during import"))
        
        self.stdout.write(self.style.SUCCESS(f"Total processed: {total_success + total_errors}"))