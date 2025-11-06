#!/usr/bin/env python
"""
Remove duplicate MCQs based on question_text
"""

import os
import sys
import django

# Setup Django environment
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
django.setup()

from mcq.models import MCQ
from django.db import transaction
from django.db.models import Count
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def remove_duplicates():
    """Remove duplicate MCQs keeping only one of each"""
    
    # Get current total
    total_before = MCQ.objects.count()
    logger.info(f"Total MCQs before removing duplicates: {total_before}")
    
    # Find duplicates by question_text
    duplicates = MCQ.objects.values('question_text').annotate(
        count=Count('id')
    ).filter(count__gt=1)
    
    duplicate_count = len(duplicates)
    logger.info(f"Found {duplicate_count} questions with duplicates")
    
    if duplicate_count > 0:
        total_deleted = 0
        
        with transaction.atomic():
            for dup in duplicates:
                # Get all MCQs with this question text
                dup_mcqs = MCQ.objects.filter(question_text=dup['question_text']).order_by('id')
                
                # Keep the first, delete the rest
                to_delete = dup_mcqs[1:]
                deleted_count = len(to_delete)
                
                if deleted_count > 0:
                    logger.info(f"Question has {dup_mcqs.count()} copies, deleting {deleted_count}: {dup['question_text'][:60]}...")
                    for mcq in to_delete:
                        mcq.delete()
                    total_deleted += deleted_count
        
        logger.info(f"\n✅ Deleted {total_deleted} duplicate MCQs")
    else:
        logger.info("✅ No duplicates found!")
    
    # Final count
    final_count = MCQ.objects.count()
    logger.info(f"\nFinal MCQ count: {final_count}")
    
    # Show distribution
    subspecialty_counts = MCQ.objects.values('subspecialty').annotate(
        count=Count('id')
    ).order_by('-count')[:15]
    
    logger.info("\nTop 15 subspecialties:")
    for item in subspecialty_counts:
        logger.info(f"  {item['subspecialty']}: {item['count']}")

def main():
    """Main function"""
    logger.info("Remove Duplicate MCQs")
    logger.info("=" * 50)
    
    remove_duplicates()
    
    logger.info("\n✅ Duplicate removal complete!")

if __name__ == "__main__":
    main()