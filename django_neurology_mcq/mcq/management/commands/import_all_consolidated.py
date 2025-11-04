import json
import sys
from django.core.management.base import BaseCommand
from mcq.models import MCQ
from django.db import transaction
import logging

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Import all consolidated MCQs to database'
    
    def add_arguments(self, parser):
        parser.add_argument('--chunk-size', type=int, default=50, help='Number of MCQs to process per chunk')
        parser.add_argument('--start-chunk', type=int, default=0, help='Starting chunk number (for resuming)')
        
    def handle(self, *args, **options):
        chunk_size = options['chunk_size']
        start_chunk = options['start_chunk']
        
        # Total MCQ count: 3046
        total_mcqs = 3046
        total_chunks = (total_mcqs + chunk_size - 1) // chunk_size
        
        self.stdout.write(f"Starting import of {total_mcqs} MCQs in {total_chunks} chunks")
        self.stdout.write(f"Chunk size: {chunk_size}, Starting from chunk: {start_chunk}")
        
        # Process in chunks to avoid memory issues
        success_count = 0
        error_count = 0
        
        for chunk_num in range(start_chunk, total_chunks):
            start_idx = chunk_num * chunk_size
            end_idx = min(start_idx + chunk_size, total_mcqs)
            
            self.stdout.write(f"\nProcessing chunk {chunk_num + 1}/{total_chunks} (MCQs {start_idx + 1}-{end_idx})")
            
            # Get chunk data
            chunk_mcqs = self.get_mcq_chunk(start_idx, end_idx)
            
            try:
                with transaction.atomic():
                    for i, mcq_data in enumerate(chunk_mcqs):
                        try:
                            self.import_single_mcq(mcq_data, start_idx + i + 1)
                            success_count += 1
                        except Exception as e:
                            error_count += 1
                            self.stdout.write(f"Error importing MCQ {start_idx + i + 1}: {e}")
                            
                self.stdout.write(f"Chunk {chunk_num + 1} completed successfully")
                
            except Exception as e:
                self.stdout.write(f"Chunk {chunk_num + 1} failed: {e}")
                error_count += len(chunk_mcqs)
        
        self.stdout.write(f"\nImport completed!")
        self.stdout.write(f"Successfully imported: {success_count} MCQs")
        self.stdout.write(f"Errors: {error_count} MCQs")
        self.stdout.write(f"Total in database: {MCQ.objects.count()} MCQs")
    
    def get_mcq_chunk(self, start_idx, end_idx):
        """Get a chunk of MCQ data"""
        # This would normally load from file, but for size limits we'll embed small chunks
        # For now, return empty to create the structure
        return []
    
    def import_single_mcq(self, mcq_data, mcq_number):
        """Import a single MCQ with proper data validation"""
        
        # Handle correct_answer field
        correct_answer = mcq_data.get('correct_answer', '')
        if isinstance(correct_answer, (list, tuple)) and len(correct_answer) > 0:
            correct_answer = str(correct_answer[0])
        else:
            correct_answer = str(correct_answer)
        
        # Ensure correct_answer is within field limits (max 10 chars)
        correct_answer = correct_answer[:10] if correct_answer else ''
        
        # Create MCQ instance
        mcq = MCQ(
            question_number=str(mcq_data.get('question_number', mcq_number))[:20],
            question_text=mcq_data.get('question', mcq_data.get('question_text', '')),
            options=mcq_data.get('options', []),
            correct_answer=correct_answer,
            correct_answer_text=mcq_data.get('correct_answer_text', ''),
            subspecialty=mcq_data.get('subspecialty', 'General Neurology'),
            exam_year=mcq_data.get('exam_year', ''),
            exam_type=mcq_data.get('exam_type', ''),
            explanation=mcq_data.get('explanation', ''),
            option_analysis=mcq_data.get('option_analysis', {})
        )
        
        mcq.save()
