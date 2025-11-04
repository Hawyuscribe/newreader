import json
import os
from django.core.management.base import BaseCommand
from mcq.models import MCQ
from django.db import transaction

class Command(BaseCommand):
    help = 'Import consolidated MCQs from local JSON files'
    
    def add_arguments(self, parser):
        parser.add_argument('--clear-existing', action='store_true', help='Clear existing MCQs before import')
        parser.add_argument('--batch-size', type=int, default=50, help='Batch size for import')
        parser.add_argument('--dry-run', action='store_true', help='Count MCQs without importing')
    
    def handle(self, *args, **options):
        clear_existing = options['clear_existing']
        batch_size = options['batch_size']
        dry_run = options['dry_run']
        
        # List of MCQ files to import (relative to the project root)
        mcq_files = [
            'consolidated_mcqs/Part II_2018.json',
            'consolidated_mcqs/Part II_2019.json', 
            'consolidated_mcqs/Part II_2020.json',
            'consolidated_mcqs/Part II_2021.json',
            'consolidated_mcqs/Part II_2022.json',
            'consolidated_mcqs/Part II_2023.json',
            'consolidated_mcqs/Part II_2024.json',
            'consolidated_mcqs/Part I_2018.json',
            'consolidated_mcqs/Part I_2019.json',
            'consolidated_mcqs/Part I_2022.json',
            'consolidated_mcqs/Part I_2023.json',
            'consolidated_mcqs/Part I_2024.json',
            'consolidated_mcqs/Promotion_2018.json',
            'consolidated_mcqs/Promotion_2019.json',
            'consolidated_mcqs/Promotion_2021.json',
            'consolidated_mcqs/Promotion_2022.json',
            'consolidated_mcqs/Promotion_2023.json',
            'consolidated_mcqs/Unknown_2020.json',
            'consolidated_mcqs/Unknown_2021.json'
        ]
        
        if clear_existing and not dry_run:
            existing_count = MCQ.objects.count()
            self.stdout.write(f"Clearing {existing_count} existing MCQs...")
            MCQ.objects.all().delete()
            self.stdout.write("Existing MCQs cleared")
        
        all_mcqs = []
        total_count = 0
        
        # Load all MCQ files
        self.stdout.write("Loading MCQ files...")
        for mcq_file in mcq_files:
            try:
                # Try to read from the app root directory
                if os.path.exists(mcq_file):
                    file_path = mcq_file
                else:
                    # Fallback: construct absolute path (for local development)
                    file_path = f"/Users/tariqalmatrudi/NEWreader/{mcq_file}"
                
                if not os.path.exists(file_path):
                    self.stdout.write(f"Warning: File not found: {mcq_file}")
                    continue
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    
                    # Handle both direct list format and object with "mcqs" key
                    mcqs_data = []
                    if isinstance(data, list):
                        mcqs_data = data
                    elif isinstance(data, dict) and 'mcqs' in data:
                        mcqs_data = data['mcqs']
                    else:
                        self.stdout.write(f"Warning: {mcq_file} has unexpected format")
                        continue
                    
                    all_mcqs.extend(mcqs_data)
                    total_count += len(mcqs_data)
                    self.stdout.write(f"Loaded {len(mcqs_data)} MCQs from {mcq_file}")
                    
            except Exception as e:
                self.stdout.write(f"Error loading {mcq_file}: {e}")
        
        self.stdout.write(f"Total MCQs loaded: {total_count}")
        
        if dry_run:
            self.stdout.write(f"DRY RUN: Would import {total_count} MCQs")
            return
        
        if not all_mcqs:
            self.stdout.write("No MCQs found to import!")
            return
        
        # Import MCQs in batches
        success_count = 0
        error_count = 0
        total_batches = (len(all_mcqs) + batch_size - 1) // batch_size
        
        self.stdout.write(f"Starting import in {total_batches} batches of {batch_size}...")
        
        for batch_num in range(total_batches):
            start_idx = batch_num * batch_size
            end_idx = min(start_idx + batch_size, len(all_mcqs))
            batch = all_mcqs[start_idx:end_idx]
            
            self.stdout.write(f"Processing batch {batch_num + 1}/{total_batches} (MCQs {start_idx + 1}-{end_idx})")
            
            try:
                with transaction.atomic():
                    for i, mcq_data in enumerate(batch):
                        try:
                            self.import_single_mcq(mcq_data, start_idx + i + 1)
                            success_count += 1
                        except Exception as e:
                            error_count += 1
                            self.stdout.write(f"Error importing MCQ {start_idx + i + 1}: {e}")
                
                self.stdout.write(f"Batch {batch_num + 1} completed successfully")
                
            except Exception as e:
                self.stdout.write(f"Batch {batch_num + 1} failed: {e}")
                error_count += len(batch)
        
        final_count = MCQ.objects.count()
        self.stdout.write(f"\n=== Import Complete ===")
        self.stdout.write(f"Successfully imported: {success_count} MCQs")
        self.stdout.write(f"Errors: {error_count} MCQs")
        self.stdout.write(f"Total in database: {final_count} MCQs")
        
        if error_count == 0:
            self.stdout.write("✅ All MCQs imported successfully!")
        else:
            self.stdout.write(f"⚠️  {error_count} MCQs failed to import")
    
    def import_single_mcq(self, mcq_data, mcq_number):
        """Import a single MCQ with proper data validation"""
        
        # Handle correct_answer field - ensure it's a string and within limits
        correct_answer = mcq_data.get('correct_answer', '')
        if isinstance(correct_answer, (list, tuple)) and len(correct_answer) > 0:
            correct_answer = str(correct_answer[0])
        else:
            correct_answer = str(correct_answer)
        
        # Ensure correct_answer is within field limits (max 10 chars)
        correct_answer = correct_answer[:10] if correct_answer else ''
        
        # Get question text from various possible fields
        question_text = (
            mcq_data.get('question_text') or 
            mcq_data.get('question') or 
            ''
        )
        
        # Handle explanation_sections with option_analysis
        explanation_sections = mcq_data.get('explanation_sections', {})
        if 'option_analysis' in mcq_data and mcq_data['option_analysis']:
            explanation_sections['option_analysis'] = mcq_data['option_analysis']
        
        # Create MCQ instance with correct field names
        mcq = MCQ(
            question_number=str(mcq_data.get('question_number', mcq_number))[:20],
            question_text=question_text,
            options=mcq_data.get('options', []),
            correct_answer=correct_answer,
            correct_answer_text=mcq_data.get('correct_answer_text', ''),
            subspecialty=mcq_data.get('subspecialty', 'General Neurology'),
            exam_year=str(mcq_data.get('exam_year', ''))[:10],
            exam_type=str(mcq_data.get('exam_type', ''))[:50],
            explanation=mcq_data.get('explanation', ''),
            explanation_sections=explanation_sections,
            primary_category=mcq_data.get('primary_category', ''),
            secondary_category=mcq_data.get('secondary_category', ''),
            difficulty_level=mcq_data.get('difficulty_level', ''),
            key_concept=mcq_data.get('key_concept', ''),
            verification_confidence=mcq_data.get('verification_confidence', ''),
            ai_generated=mcq_data.get('ai_generated', False)
        )
        
        mcq.save()