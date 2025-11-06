#!/usr/bin/env python
"""
Cleanup script to remove old MCQs from Heroku and keep only new ones
"""

from mcq.models import MCQ, Flashcard, IncorrectAnswer, Bookmark
from django.db import transaction
from django.db.models import Count

print("MCQ Cleanup on Heroku - Remove Old, Keep New")
print("=" * 50)

# Get current total
total_before = MCQ.objects.count()
print(f"Total MCQs before cleanup: {total_before}")

# Count MCQs with explanation_sections (these are the new ones)
mcqs_with_sections = MCQ.objects.exclude(explanation_sections__isnull=True).exclude(explanation_sections={})
new_count = mcqs_with_sections.count()
print(f"MCQs with explanation_sections (new format): {new_count}")

# Get IDs of new MCQs to keep
new_mcq_ids = set(mcqs_with_sections.values_list('id', flat=True))

# Delete old MCQs (those not in the new set)
old_mcqs = MCQ.objects.exclude(id__in=new_mcq_ids)
old_count = old_mcqs.count()

print(f"MCQs to delete (old format): {old_count}")

if old_count > 0:
    print(f"\nDeleting {old_count} old MCQs...")
    
    with transaction.atomic():
        # Delete related records
        flashcard_count = Flashcard.objects.filter(mcq__in=old_mcqs).delete()[0]
        print(f"  Deleted {flashcard_count} related flashcards")
        
        incorrect_count = IncorrectAnswer.objects.filter(mcq__in=old_mcqs).delete()[0]
        print(f"  Deleted {incorrect_count} related incorrect answers")
        
        bookmark_count = Bookmark.objects.filter(mcq__in=old_mcqs).delete()[0]
        print(f"  Deleted {bookmark_count} related bookmarks")
        
        # Delete the MCQs
        deleted_count = old_mcqs.delete()[0]
        print(f"Deleted {deleted_count} old MCQs")

# Verify final count
final_count = MCQ.objects.count()
print(f"\nFinal MCQ count: {final_count}")

# Show distribution
subspecialty_counts = MCQ.objects.values('subspecialty').annotate(
    count=Count('id')
).order_by('-count')[:10]

print("\nTop subspecialties after cleanup:")
for item in subspecialty_counts:
    print(f"  {item['subspecialty']}: {item['count']}")

print("\nCleanup complete!")