"""
Django management command to deploy all RERE MCQs from fixture chunks.
"""
import json
from pathlib import Path
from django.core.management.base import BaseCommand
from django.db import transaction
from mcq.models import MCQ
from django.db.models import Count


class Command(BaseCommand):
    help = 'Deploy all RERE MCQs from fixture chunks'
    
    def add_arguments(self, parser):
        parser.add_argument('--clear', action='store_true', help='Clear all existing MCQs first')
        parser.add_argument('--chunk-dir', default='rere_chunks', help='Directory containing fixture chunks')
        parser.add_argument('--batch-size', type=int, default=50, help='Number of MCQs per batch')
    
    def handle(self, *args, **options):
        if options['clear']:
            self.stdout.write('Clearing all existing MCQs...')
            count = MCQ.objects.count()
            MCQ.objects.all().delete()
            self.stdout.write(self.style.SUCCESS(f'Cleared {count} MCQs'))
        
        chunk_dir = Path(options['chunk_dir'])
        batch_size = options['batch_size']
        total_imported = 0
        total_errors = 0
        
        # Find all chunk files
        chunk_files = sorted(chunk_dir.glob('rere_chunk_*.json'))
        self.stdout.write(f'Found {len(chunk_files)} chunk files')
        
        # Process each chunk
        for chunk_file in chunk_files:
            self.stdout.write(f'\nProcessing {chunk_file.name}...')
            
            try:
                with open(chunk_file, 'r') as f:
                    fixtures = json.load(f)
                
                chunk_imported = 0
                chunk_errors = 0
                
                # Process fixtures in batches
                for i in range(0, len(fixtures), batch_size):
                    batch = fixtures[i:i+batch_size]
                    
                    with transaction.atomic():
                        for fixture in batch:
                            try:
                                fields = fixture['fields']
                                
                                # Filter out fields that don't exist in the model
                                model_field_names = [f.name for f in MCQ._meta.get_fields()]
                                filtered_fields = {k: v for k, v in fields.items() if k in model_field_names}
                                
                                # Ensure correct_answer is not None
                                if not filtered_fields.get('correct_answer'):
                                    filtered_fields['correct_answer'] = 'B'  # Default fallback
                                
                                MCQ.objects.create(**filtered_fields)
                                chunk_imported += 1
                            except Exception as e:
                                chunk_errors += 1
                                self.stdout.write(self.style.ERROR(f"Error: {str(e)[:100]}"))
                
                total_imported += chunk_imported
                total_errors += chunk_errors
                self.stdout.write(f"Imported {chunk_imported} MCQs from {chunk_file.name} ({chunk_errors} errors)")
            
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Failed to process {chunk_file.name}: {str(e)}"))
        
        # Final report
        self.stdout.write(self.style.SUCCESS(
            f'\n\nDeployment complete: {total_imported} MCQs imported, {total_errors} errors'
        ))
        
        # Verification
        self.verify_deployment()
    
    def verify_deployment(self):
        """Verify the deployment results."""
        self.stdout.write('\n=== Deployment Verification ===')
        
        # Total count
        total = MCQ.objects.count()
        self.stdout.write(f'Total MCQs in database: {total}')
        
        # By subspecialty
        subspecialty_counts = MCQ.objects.values('subspecialty').annotate(count=Count('id')).order_by('subspecialty')
        self.stdout.write('\nMCQs by subspecialty:')
        for sub in subspecialty_counts:
            self.stdout.write(f"  {sub['subspecialty']}: {sub['count']}")
        
        # Check explanations
        mcqs_with_explanations = MCQ.objects.exclude(explanation_sections=None).exclude(explanation_sections={}).count()
        self.stdout.write(f'\nMCQs with explanation sections: {mcqs_with_explanations}')
        
        # Check Vascular Neurology/Stroke specifically
        vascular_count = MCQ.objects.filter(subspecialty='Vascular Neurology/Stroke').count()
        self.stdout.write(f'\nVascular Neurology/Stroke count: {vascular_count}')
        
        # Sample MCQ
        sample = MCQ.objects.filter(subspecialty='Vascular Neurology/Stroke').first()
        if sample:
            self.stdout.write(f'\nSample Vascular MCQ:')
            self.stdout.write(f'  ID: {sample.id}')
            self.stdout.write(f'  Question: {sample.question_text[:100]}...')
            self.stdout.write(f'  Correct Answer: {sample.correct_answer}')
            exp_sections = sample.explanation_sections
            if exp_sections:
                self.stdout.write(f'  Has explanation sections: Yes')
                if 'option_analysis' in exp_sections:
                    option_analysis = exp_sections['option_analysis']
                    if isinstance(option_analysis, str):
                        self.stdout.write(f'  Option analysis preview: {option_analysis[:100]}...')
                    else:
                        self.stdout.write(f'  Option analysis type: {type(option_analysis)}')
            else:
                self.stdout.write(f'  Has explanation sections: No')