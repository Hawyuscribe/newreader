"""
Django management command to reset database to only new MCQs
"""

from django.core.management.base import BaseCommand
from django.db import transaction
from django.db.models import Count
from mcq.models import MCQ, Flashcard, IncorrectAnswer, Bookmark


class Command(BaseCommand):
    help = 'Reset database to only contain the new MCQs from output_by_specialty'

    def handle(self, *args, **options):
        self.stdout.write("Reset Database to New MCQs Only")
        self.stdout.write("=" * 50)
        
        # First, clear everything
        self.stdout.write("\nClearing all existing data...")
        
        with transaction.atomic():
            # Delete all related records
            flashcard_count = Flashcard.objects.all().delete()[0]
            self.stdout.write(f"  Deleted {flashcard_count} flashcards")
            
            incorrect_count = IncorrectAnswer.objects.all().delete()[0]
            self.stdout.write(f"  Deleted {incorrect_count} incorrect answers")
            
            bookmark_count = Bookmark.objects.all().delete()[0]
            self.stdout.write(f"  Deleted {bookmark_count} bookmarks")
            
            # Delete all MCQs
            mcq_count = MCQ.objects.all().delete()[0]
            self.stdout.write(f"  Deleted {mcq_count} MCQs")
        
        self.stdout.write(self.style.SUCCESS("\n✅ Database cleared. Ready for new MCQ import."))