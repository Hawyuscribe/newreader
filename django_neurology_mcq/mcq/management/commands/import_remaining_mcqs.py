import json
import os
from django.core.management.base import BaseCommand
from mcq.models import MCQ
from django.db import transaction

class Command(BaseCommand):
    help = 'Import remaining MCQs with enhanced error handling for correct_answer field'
    
    def add_arguments(self, parser):
        parser.add_argument('--batch-size', type=int, default=25, help='Batch size for import')
        parser.add_argument('--skip-existing', action='store_true', help='Skip MCQs that already exist')
    
    def handle(self, *args, **options):
        batch_size = options['batch_size']
        skip_existing = options['skip_existing']
        
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
        
        # Get existing MCQ question numbers if skip_existing is True
        existing_questions = set()
        if skip_existing:
            existing_questions = set(MCQ.objects.values_list('question_number', flat=True))
            self.stdout.write(f"Found {len(existing_questions)} existing MCQs to skip")
        
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
                    # Fallback: construct absolute path
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
                    
                    # Filter out existing MCQs if needed
                    if skip_existing:
                        new_mcqs = [mcq for mcq in mcqs_data 
                                   if str(mcq.get('question_number', '')) not in existing_questions]
                        self.stdout.write(f"Loaded {len(new_mcqs)} new MCQs from {mcq_file} (skipped {len(mcqs_data) - len(new_mcqs)} existing)")
                        all_mcqs.extend(new_mcqs)
                        total_count += len(new_mcqs)
                    else:
                        all_mcqs.extend(mcqs_data)
                        total_count += len(mcqs_data)
                        self.stdout.write(f"Loaded {len(mcqs_data)} MCQs from {mcq_file}")
                    
            except Exception as e:
                self.stdout.write(f"Error loading {mcq_file}: {e}")
        
        self.stdout.write(f"Total MCQs to import: {total_count}")
        
        if not all_mcqs:
            self.stdout.write("No new MCQs found to import!")
            return
        
        # Import MCQs in batches with enhanced error handling
        success_count = 0
        error_count = 0
        correct_answer_errors = 0
        total_batches = (len(all_mcqs) + batch_size - 1) // batch_size
        
        self.stdout.write(f"Starting import in {total_batches} batches of {batch_size}...")
        
        for batch_num in range(total_batches):
            start_idx = batch_num * batch_size
            end_idx = min(start_idx + batch_size, len(all_mcqs))
            batch = all_mcqs[start_idx:end_idx]
            
            self.stdout.write(f"\nProcessing batch {batch_num + 1}/{total_batches} (MCQs {start_idx + 1}-{end_idx})")
            
            # Process each MCQ individually to handle errors better
            for i, mcq_data in enumerate(batch):
                try:
                    result = self.import_single_mcq(mcq_data, start_idx + i + 1)
                    if result:
                        success_count += 1
                    else:
                        error_count += 1
                except Exception as e:
                    error_count += 1
                    if 'correct_answer' in str(e) or 'character varying(5)' in str(e):
                        correct_answer_errors += 1
                    self.stdout.write(f"Error importing MCQ {start_idx + i + 1}: {e}")
            
            self.stdout.write(f"Batch {batch_num + 1} completed: {success_count} successful so far")
        
        final_count = MCQ.objects.count()
        self.stdout.write(f"\n=== Import Complete ===")
        self.stdout.write(f"Successfully imported: {success_count} MCQs")
        self.stdout.write(f"Errors: {error_count} MCQs")
        self.stdout.write(f"  - Correct answer field errors: {correct_answer_errors}")
        self.stdout.write(f"Total in database: {final_count} MCQs")
        
        if error_count == 0:
            self.stdout.write("✅ All MCQs imported successfully!")
        else:
            self.stdout.write(f"⚠️  {error_count} MCQs failed to import")
    
    def clean_correct_answer(self, answer):
        """Clean and validate correct_answer field to fit within 5 characters"""
        if not answer:
            return ''
        
        # Convert to string
        answer = str(answer)
        
        # Handle common patterns
        if answer.startswith('Option '):
            # Extract just the letter (e.g., "Option A" -> "A")
            answer = answer.replace('Option ', '').strip()
        
        # Handle list/array format
        if answer.startswith('[') and answer.endswith(']'):
            # Extract first element from list representation
            try:
                import ast
                parsed = ast.literal_eval(answer)
                if isinstance(parsed, list) and len(parsed) > 0:
                    answer = str(parsed[0])
            except:
                # If parsing fails, try to extract manually
                answer = answer.strip('[]').split(',')[0].strip().strip("'\"")
        
        # Remove quotes if present
        answer = answer.strip("'\"")
        
        # Ensure it's within 5 characters
        answer = answer[:5]
        
        return answer
    
    def import_single_mcq(self, mcq_data, mcq_number):
        """Import a single MCQ with enhanced data validation"""
        
        try:
            # Handle correct_answer field with enhanced cleaning
            correct_answer = mcq_data.get('correct_answer', '')
            if isinstance(correct_answer, (list, tuple)) and len(correct_answer) > 0:
                correct_answer = str(correct_answer[0])
            else:
                correct_answer = str(correct_answer)
            
            # Clean the correct_answer to fit within field limits
            correct_answer = self.clean_correct_answer(correct_answer)
            
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
            return True
            
        except Exception as e:
            # Log detailed error information
            self.stdout.write(f"Failed to import MCQ {mcq_number}:")
            self.stdout.write(f"  Question: {question_text[:50]}...")
            self.stdout.write(f"  Original correct_answer: {mcq_data.get('correct_answer', '')}")
            self.stdout.write(f"  Cleaned correct_answer: {correct_answer}")
            self.stdout.write(f"  Error: {str(e)}")
            return False