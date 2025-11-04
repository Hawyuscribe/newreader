"""
Django management command to load RERE fixture chunks.
"""
import json
from pathlib import Path
from django.core.management.base import BaseCommand
from django.db import transaction
from mcq.models import MCQ


class Command(BaseCommand):
    help = 'Load RERE MCQ fixtures from chunks'
    
    def add_arguments(self, parser):
        parser.add_argument('--clear', action='store_true', help='Clear all existing MCQs')
        parser.add_argument('--chunk-dir', default='rere_chunks', help='Directory containing chunks')
    
    def handle(self, *args, **options):
        if options['clear']:
            self.stdout.write('Clearing all existing MCQs...')
            MCQ.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('All MCQs cleared'))
        
        chunk_dir = Path(options['chunk_dir'])
        
        # Read manifest
        manifest_file = chunk_dir / 'manifest.json'
        if manifest_file.exists():
            with open(manifest_file, 'r') as f:
                manifest = json.load(f)
            
            self.stdout.write(f"Loading {manifest['total_chunks']} chunks...")
        else:
            # Find all chunk files
            chunk_files = sorted(chunk_dir.glob('rere_chunk_*.json'))
            self.stdout.write(f"Found {len(chunk_files)} chunk files")
        
        total_imported = 0
        errors = 0
        
        # Process each chunk
        chunk_files = sorted(chunk_dir.glob('rere_chunk_*.json'))
        for chunk_file in chunk_files:
            self.stdout.write(f'\nProcessing {chunk_file.name}...')
            
            try:
                with open(chunk_file, 'r') as f:
                    fixtures = json.load(f)
                
                chunk_imported = 0
                with transaction.atomic():
                    for fixture in fixtures:
                        try:
                            fields = fixture['fields']
                            MCQ.objects.create(**fields)
                            chunk_imported += 1
                        except Exception as e:
                            errors += 1
                            self.stdout.write(self.style.ERROR(f"Error: {str(e)[:100]}"))
                
                total_imported += chunk_imported
                self.stdout.write(f"Imported {chunk_imported} MCQs from {chunk_file.name}")
            
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Failed to process {chunk_file.name}: {str(e)}"))
        
        # Final report
        self.stdout.write(self.style.SUCCESS(
            f'\nImport complete: {total_imported} MCQs imported, {errors} errors'
        ))
        
        # Verification
        total_in_db = MCQ.objects.count()
        self.stdout.write(f"Total MCQs in database: {total_in_db}")
        
        # Check subspecialties
        from django.db.models import Count
        subspecialty_counts = MCQ.objects.values('subspecialty').annotate(count=Count('id')).order_by('subspecialty')
        self.stdout.write("\nMCQs by subspecialty:")
        for sub in subspecialty_counts:
            self.stdout.write(f"  {sub['subspecialty']}: {sub['count']}")
        
        # Check explanations
        mcqs_with_explanations = MCQ.objects.exclude(explanation_sections=None).exclude(explanation_sections={}).count()
        self.stdout.write(f"\nMCQs with explanation sections: {mcqs_with_explanations}")