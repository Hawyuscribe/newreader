from django.core.management.base import BaseCommand
from django.core.management import call_command
from mcq.models import MCQ, Flashcard, IncorrectAnswer, Bookmark
import os


class Command(BaseCommand):
    help = 'Load all heroku_sync_chunk files'

    def handle(self, *args, **options):
        self.stdout.write("Starting MCQ sync process...")
        
        # Clear existing data
        self.stdout.write("Clearing existing data...")
        Flashcard.objects.all().delete()
        IncorrectAnswer.objects.all().delete()
        Bookmark.objects.all().delete()
        deleted_count = MCQ.objects.all().delete()[0]
        self.stdout.write(f"Deleted {deleted_count} existing MCQs")
        
        # Load chunks
        chunk_files = []
        for i in range(1, 30):  # We have 29 chunks
            filename = f'heroku_sync_chunk_{i:03d}_of_029.json'
            if os.path.exists(filename):
                chunk_files.append(filename)
        
        self.stdout.write(f"Found {len(chunk_files)} chunk files to load")
        
        loaded_count = 0
        for i, filename in enumerate(chunk_files, 1):
            self.stdout.write(f"Loading chunk {i}/{len(chunk_files)}: {filename}")
            try:
                call_command('loaddata', filename)
                # Count MCQs after each load to track progress
                current_count = MCQ.objects.count()
                self.stdout.write(f"  Total MCQs so far: {current_count}")
                loaded_count = current_count
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"  Error loading {filename}: {e}"))
        
        # Final count
        final_count = MCQ.objects.count()
        self.stdout.write(self.style.SUCCESS(f"\nSync complete! Total MCQs: {final_count}"))