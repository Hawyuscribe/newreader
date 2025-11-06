#!/usr/bin/env python
"""
Remove old MCQs and keep only the new ones imported from output_by_specialty
"""

import os
import sys
import django
from datetime import datetime

# Setup Django environment
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
django.setup()

from mcq.models import MCQ
from django.db import transaction
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def remove_old_keep_new():
    """Remove old MCQs and keep only new ones"""
    
    # Get current total
    total_before = MCQ.objects.count()
    logger.info(f"Total MCQs before cleanup: {total_before}")
    
    # The new MCQs are those that have explanation_sections
    # Old MCQs only have explanation field
    
    # First, let's analyze what we have
    logger.info("\nAnalyzing MCQs...")
    
    # Count MCQs with explanation_sections (these are the new ones)
    mcqs_with_sections = MCQ.objects.exclude(explanation_sections__isnull=True).exclude(explanation_sections={})
    new_count = mcqs_with_sections.count()
    logger.info(f"MCQs with explanation_sections (new format): {new_count}")
    
    # Get IDs of new MCQs to keep
    new_mcq_ids = set(mcqs_with_sections.values_list('id', flat=True))
    
    # Delete old MCQs (those not in the new set)
    old_mcqs = MCQ.objects.exclude(id__in=new_mcq_ids)
    old_count = old_mcqs.count()
    
    logger.info(f"MCQs to delete (old format): {old_count}")
    
    # Show sample of MCQs to be deleted
    logger.info("\nSample of MCQs to be deleted:")
    for mcq in old_mcqs[:10]:
        logger.info(f"  - ID: {mcq.id}, Question: {mcq.question_text[:50]}...")
        logger.info(f"    Source: {mcq.source_file}, Exam: {mcq.exam_type} {mcq.exam_year}")
    
    # Perform deletion
    if old_count > 0:
        logger.info(f"\n🗑️  Deleting {old_count} old MCQs...")
        
        with transaction.atomic():
            # First delete related records to avoid foreign key issues
            from mcq.models import Flashcard, IncorrectAnswer, Bookmark
            
            # Delete related flashcards
            flashcard_count = Flashcard.objects.filter(mcq__in=old_mcqs).delete()[0]
            logger.info(f"  Deleted {flashcard_count} related flashcards")
            
            # Delete related incorrect answers
            incorrect_count = IncorrectAnswer.objects.filter(mcq__in=old_mcqs).delete()[0]
            logger.info(f"  Deleted {incorrect_count} related incorrect answers")
            
            # Delete related bookmarks
            bookmark_count = Bookmark.objects.filter(mcq__in=old_mcqs).delete()[0]
            logger.info(f"  Deleted {bookmark_count} related bookmarks")
            
            # Now delete the MCQs
            deleted_count = old_mcqs.delete()[0]
            logger.info(f"✅ Deleted {deleted_count} old MCQs")
            
            # Verify final count
            final_count = MCQ.objects.count()
            logger.info(f"\nFinal MCQ count: {final_count}")
            
            # Verify all remaining have explanation_sections
            remaining_without_sections = MCQ.objects.filter(
                explanation_sections__isnull=True
            ).count() + MCQ.objects.filter(explanation_sections={}).count()
            
            logger.info(f"MCQs without explanation_sections: {remaining_without_sections}")
            
            # Show distribution
            from django.db.models import Count
            subspecialty_counts = MCQ.objects.values('subspecialty').annotate(
                count=Count('id')
            ).order_by('-count')[:10]
            
            logger.info("\nTop subspecialties after cleanup:")
            for item in subspecialty_counts:
                logger.info(f"  {item['subspecialty']}: {item['count']}")
    else:
        logger.info("✅ No old MCQs to delete - all MCQs are in the new format!")

def main():
    """Main function"""
    logger.info("MCQ Cleanup Script - Remove Old, Keep New")
    logger.info("=" * 50)
    
    remove_old_keep_new()
    
    logger.info("\n✅ Cleanup complete!")

if __name__ == "__main__":
    main()