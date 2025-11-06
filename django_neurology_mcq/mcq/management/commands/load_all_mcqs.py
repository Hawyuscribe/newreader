from django.core.management.base import BaseCommand
from django.core.management import call_command
from pathlib import Path
import json
from mcq.models import MCQ, Flashcard, IncorrectAnswer, Bookmark
from django.db import transaction
import os

class Command(BaseCommand):
    help = 'Load all MCQs from available fixture files'

    def handle(self, *args, **options):
        self.stdout.write("Starting MCQ loading process...")
        
        # Clear existing data
        with transaction.atomic():
            self.stdout.write("Clearing existing data...")
            Flashcard.objects.all().delete()
            IncorrectAnswer.objects.all().delete()
            Bookmark.objects.all().delete()
            deleted_count = MCQ.objects.all().delete()[0]
            self.stdout.write(f"Deleted {deleted_count} existing MCQs")
        
        # Try to find fixture files
        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        
        # List of possible fixture locations
        fixture_paths = [
            base_dir / 'rere_fixtures.json',
            base_dir / 'final_rere_fixtures.json',
            base_dir / 'complete_mcq_fixtures.json',
            base_dir / 'mcq_fixtures_final.json',
            base_dir / 'mcq_fixtures.json'
        ]
        
        # Try each fixture file
        loaded = False
        for fixture_path in fixture_paths:
            if fixture_path.exists():
                self.stdout.write(f"Found {fixture_path.name}")
                try:
                    # Check if it's a valid fixture
                    with open(fixture_path, 'r') as f:
                        data = json.load(f)
                        if isinstance(data, list) and len(data) > 0:
                            mcq_count = sum(1 for item in data if item.get('model') == 'mcq.mcq')
                            if mcq_count > 0:
                                self.stdout.write(f"  Contains {mcq_count} MCQs")
                                call_command('loaddata', str(fixture_path))
                                loaded = True
                                break
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Error with {fixture_path.name}: {e}"))
        
        if not loaded:
            # Check for heroku_sync chunks
            sync_dir = base_dir / 'heroku_sync'
            if sync_dir.exists():
                chunk_files = sorted(sync_dir.glob('heroku_sync_chunk_*.json'))
                if chunk_files:
                    self.stdout.write(f"Found {len(chunk_files)} sync chunks")
                    for chunk_file in chunk_files:
                        try:
                            call_command('loaddata', str(chunk_file))
                            self.stdout.write(f"Loaded {chunk_file.name}")
                            loaded = True
                        except Exception as e:
                            self.stdout.write(self.style.ERROR(f"Error loading {chunk_file.name}: {e}"))
        
        if loaded:
            count = MCQ.objects.count()
            self.stdout.write(self.style.SUCCESS(f"\n✅ Successfully loaded {count} MCQs"))
            
            # Show subspecialty breakdown
            from django.db.models import Count
            subspecialties = MCQ.objects.values('subspecialty').annotate(count=Count('id')).order_by('-count')[:10]
            self.stdout.write("\nTop subspecialties:")
            for spec in subspecialties:
                self.stdout.write(f"  {spec['subspecialty']}: {spec['count']}")
        else:
            self.stdout.write(self.style.WARNING("No fixture files found or loaded."))