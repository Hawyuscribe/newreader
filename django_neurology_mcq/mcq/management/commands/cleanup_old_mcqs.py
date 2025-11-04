"""
Django management command to remove old MCQs and keep only new ones
"""

from django.core.management.base import BaseCommand
from django.db import transaction
from django.db.models import Count
from mcq.models import MCQ, Flashcard, IncorrectAnswer, Bookmark


class Command(BaseCommand):
    help = 'Remove old MCQs and keep only new ones with explanation_sections'

    def handle(self, *args, **options):
        self.stdout.write("MCQ Cleanup - Remove Old, Keep New")
        self.stdout.write("=" * 50)
        
        # Get current total
        total_before = MCQ.objects.count()
        self.stdout.write(f"Total MCQs before cleanup: {total_before}")
        
        # Count MCQs with explanation_sections (these are the new ones)
        mcqs_with_sections = MCQ.objects.exclude(
            explanation_sections__isnull=True
        ).exclude(explanation_sections={})
        new_count = mcqs_with_sections.count()
        self.stdout.write(f"MCQs with explanation_sections (new format): {new_count}")
        
        # Get IDs of new MCQs to keep
        new_mcq_ids = set(mcqs_with_sections.values_list('id', flat=True))
        
        # Find old MCQs (those not in the new set)
        old_mcqs = MCQ.objects.exclude(id__in=new_mcq_ids)
        old_count = old_mcqs.count()
        
        self.stdout.write(f"MCQs to delete (old format): {old_count}")
        
        if old_count > 0:
            self.stdout.write(f"\nDeleting {old_count} old MCQs...")
            
            with transaction.atomic():
                # Delete related records
                flashcard_count = Flashcard.objects.filter(mcq__in=old_mcqs).delete()[0]
                self.stdout.write(f"  Deleted {flashcard_count} related flashcards")
                
                incorrect_count = IncorrectAnswer.objects.filter(mcq__in=old_mcqs).delete()[0]
                self.stdout.write(f"  Deleted {incorrect_count} related incorrect answers")
                
                bookmark_count = Bookmark.objects.filter(mcq__in=old_mcqs).delete()[0]
                self.stdout.write(f"  Deleted {bookmark_count} related bookmarks")
                
                # Delete the MCQs
                deleted_count = old_mcqs.delete()[0]
                self.stdout.write(self.style.SUCCESS(f"✅ Deleted {deleted_count} old MCQs"))
        
        # Verify final count
        final_count = MCQ.objects.count()
        self.stdout.write(f"\nFinal MCQ count: {final_count}")
        
        # Verify all remaining have explanation_sections
        remaining_without_sections = MCQ.objects.filter(
            explanation_sections__isnull=True
        ).count() + MCQ.objects.filter(explanation_sections={}).count()
        
        self.stdout.write(f"MCQs without explanation_sections: {remaining_without_sections}")
        
        # Show distribution
        subspecialty_counts = MCQ.objects.values('subspecialty').annotate(
            count=Count('id')
        ).order_by('-count')[:10]
        
        self.stdout.write("\nTop subspecialties after cleanup:")
        for item in subspecialty_counts:
            self.stdout.write(f"  {item['subspecialty']}: {item['count']}")
        
        self.stdout.write(self.style.SUCCESS("\n✅ Cleanup complete!"))