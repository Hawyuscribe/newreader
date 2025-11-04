from django.core.management.base import BaseCommand
from django.db import transaction
from mcq.models import MCQ, Flashcard, IncorrectAnswer, Bookmark
from django.core.management import call_command
import os


class Command(BaseCommand):
    help = 'Reset database and load correct MCQs'

    def handle(self, *args, **options):
        self.stdout.write("=== MCQ Database Reset and Load ===")
        
        # Step 1: Clear everything
        self.stdout.write("\nStep 1: Clearing all existing data...")
        with transaction.atomic():
            # Clear related models first
            flashcard_count = Flashcard.objects.all().delete()[0]
            self.stdout.write(f"  Deleted {flashcard_count} flashcards")
            
            incorrect_count = IncorrectAnswer.objects.all().delete()[0]
            self.stdout.write(f"  Deleted {incorrect_count} incorrect answers")
            
            bookmark_count = Bookmark.objects.all().delete()[0]
            self.stdout.write(f"  Deleted {bookmark_count} bookmarks")
            
            # Now clear MCQs
            mcq_count = MCQ.objects.all().delete()[0]
            self.stdout.write(f"  Deleted {mcq_count} MCQs")
        
        self.stdout.write(self.style.SUCCESS("✅ Database cleared"))
        
        # Step 2: Check if sync chunks exist
        self.stdout.write("\nStep 2: Looking for sync chunks...")
        chunk_files = []
        for i in range(1, 30):  # We have 29 chunks
            filename = f'heroku_sync_chunk_{i:03d}_of_029.json'
            if os.path.exists(filename):
                chunk_files.append(filename)
        
        if chunk_files:
            self.stdout.write(f"Found {len(chunk_files)} chunk files")
            
            # Load each chunk
            for i, filename in enumerate(chunk_files, 1):
                self.stdout.write(f"\nLoading chunk {i}/{len(chunk_files)}: {filename}")
                try:
                    call_command('loaddata', filename)
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Error loading {filename}: {e}"))
        else:
            self.stdout.write(self.style.WARNING("No sync chunks found. Please generate them first."))
            self.stdout.write("Run: python manage.py sync_to_heroku")
        
        # Step 3: Report final counts
        self.stdout.write("\nStep 3: Final MCQ counts:")
        total = MCQ.objects.count()
        self.stdout.write(f"\nTotal MCQs: {total}")
        
        # Count by subspecialty
        from django.db.models import Count
        subspecialty_counts = MCQ.objects.values('subspecialty').annotate(
            count=Count('id')
        ).order_by('-count')
        
        self.stdout.write("\nTop subspecialties:")
        for item in subspecialty_counts[:10]:
            self.stdout.write(f"  {item['subspecialty']}: {item['count']}")
        
        # Expected vs actual
        expected = {
            'Neuromuscular': 483,
            'Vascular Neurology/Stroke': 439,
            'Neuroimmunology': 299,
            'Epilepsy': 284,
            'Movement Disorders': 269
        }
        
        self.stdout.write("\nExpected vs Actual (top 5):")
        for subspecialty, expected_count in expected.items():
            actual = MCQ.objects.filter(subspecialty=subspecialty).count()
            status = "✅" if actual == expected_count else "❌"
            self.stdout.write(f"  {subspecialty}: {actual} (expected {expected_count}) {status}")
        
        if total == 2853:
            self.stdout.write(self.style.SUCCESS("\n✅ Success! MCQ count matches expected total."))
        else:
            self.stdout.write(self.style.ERROR(f"\n❌ MCQ count mismatch. Expected 2853, got {total}"))