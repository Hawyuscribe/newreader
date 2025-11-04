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
    
    # The new MCQs have these characteristics:
    # 1. They have explanation_sections (not just explanation)
    # 2. Their source_file contains one of the output_by_specialty filenames
    
    # List of source files from output_by_specialty
    new_source_files = [
        'neuroanatomy_mcqs.json',
        'other_unclassified_mcqs.json',
        'multiple_sclerosis_mcqs.json',
        'critical_care_neurology_mcqs.json',
        'vascular_neurology_stroke_mcqs.json',
        'neuromuscular_mcqs.json',
        'movement_disorders_mcqs.json',
        'epilepsy_mcqs.json',
        'neuro_infectious_mcqs.json',
        'pediatric_neurology_mcqs.json',
        'headache_medicine_mcqs.json',
        'neuroimmunology_mcqs.json',
        'cognitive_behavioral_neurology_mcqs.json',
        'neuroophthalmology_mcqs.json',
        'neuro_oncology_mcqs.json',
        'behavioral_neurology_neuropsychiatry_mcqs.json',
        'neuroendocrinology_mcqs.json',
        'neurogenetics_mcqs.json',
        'sleep_medicine_mcqs.json'
    ]
    
    # First, let's analyze what we have
    logger.info("\nAnalyzing MCQs...")
    
    # Count MCQs with explanation_sections
    mcqs_with_sections = MCQ.objects.exclude(explanation_sections__isnull=True).exclude(explanation_sections={})
    logger.info(f"MCQs with explanation_sections: {mcqs_with_sections.count()}")
    
    # Count MCQs from new source files
    new_mcqs = MCQ.objects.filter(source_file__in=new_source_files)
    logger.info(f"MCQs from output_by_specialty files: {new_mcqs.count()}")
    
    # Count MCQs that have both characteristics
    confirmed_new = mcqs_with_sections.filter(source_file__in=new_source_files)
    logger.info(f"Confirmed new MCQs (have sections AND from new files): {confirmed_new.count()}")
    
    # Get IDs of new MCQs to keep
    new_mcq_ids = set(confirmed_new.values_list('id', flat=True))
    
    # Also include MCQs that have explanation_sections even if source_file is different
    # (in case some were imported with modified source_file names)
    all_new_ids = set(mcqs_with_sections.values_list('id', flat=True))
    
    logger.info(f"\nTotal MCQs to keep: {len(all_new_ids)}")
    
    # Delete old MCQs (those not in the new set)
    old_mcqs = MCQ.objects.exclude(id__in=all_new_ids)
    old_count = old_mcqs.count()
    
    logger.info(f"MCQs to delete: {old_count}")
    
    # Show sample of MCQs to be deleted
    logger.info("\nSample of MCQs to be deleted:")
    for mcq in old_mcqs[:5]:
        logger.info(f"  - ID: {mcq.id}, Question: {mcq.question_text[:50]}...")
        logger.info(f"    Source: {mcq.source_file}, Has sections: {bool(mcq.explanation_sections)}")
    
    # Confirm deletion
    if old_count > 0:
        logger.info(f"\n⚠️  About to delete {old_count} old MCQs and keep {len(all_new_ids)} new ones.")
        response = input("Do you want to proceed? (yes/no): ")
        
        if response.lower() == 'yes':
            with transaction.atomic():
                deleted_count = old_mcqs.delete()[0]
                logger.info(f"✅ Deleted {deleted_count} old MCQs")
                
                # Verify final count
                final_count = MCQ.objects.count()
                logger.info(f"\nFinal MCQ count: {final_count}")
                
                # Show distribution
                from django.db.models import Count
                subspecialty_counts = MCQ.objects.values('subspecialty').annotate(
                    count=Count('id')
                ).order_by('-count')[:10]
                
                logger.info("\nTop subspecialties after cleanup:")
                for item in subspecialty_counts:
                    logger.info(f"  {item['subspecialty']}: {item['count']}")
        else:
            logger.info("❌ Deletion cancelled")
    else:
        logger.info("✅ No old MCQs to delete - all MCQs are new!")

def main():
    """Main function"""
    logger.info("MCQ Cleanup Script - Remove Old, Keep New")
    logger.info("=" * 50)
    
    remove_old_keep_new()

if __name__ == "__main__":
    main()