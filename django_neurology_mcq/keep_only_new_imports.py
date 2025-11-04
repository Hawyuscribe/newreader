#!/usr/bin/env python
"""
Keep ONLY the MCQs imported from /Users/tariqalmatrudi/Documents/FFF/output_by_specialty
Delete all others and remove duplicates
"""

import os
import sys
import django
from pathlib import Path

# Setup Django environment
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
django.setup()

from mcq.models import MCQ, Flashcard, IncorrectAnswer, Bookmark
from django.db import transaction
from django.db.models import Count
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# List of source files from output_by_specialty
NEW_SOURCE_FILES = [
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

def keep_only_new_imports():
    """Keep only MCQs from output_by_specialty and remove duplicates"""
    
    # Get current total
    total_before = MCQ.objects.count()
    logger.info(f"Total MCQs before cleanup: {total_before}")
    
    # Find MCQs from the new import
    # They should have explanation_sections AND be from the new source files
    new_mcqs = MCQ.objects.exclude(
        explanation_sections__isnull=True
    ).exclude(
        explanation_sections={}
    ).filter(
        source_file__in=NEW_SOURCE_FILES
    )
    
    new_count = new_mcqs.count()
    logger.info(f"MCQs from output_by_specialty: {new_count}")
    
    # Get IDs to keep
    ids_to_keep = set(new_mcqs.values_list('id', flat=True))
    
    # Find all MCQs to delete (those not from the new import)
    mcqs_to_delete = MCQ.objects.exclude(id__in=ids_to_keep)
    delete_count = mcqs_to_delete.count()
    
    logger.info(f"MCQs to delete: {delete_count}")
    
    # Show some examples of what will be deleted
    logger.info("\nSample MCQs to be deleted:")
    for mcq in mcqs_to_delete[:5]:
        logger.info(f"  - ID: {mcq.id}, Source: {mcq.source_file}")
        logger.info(f"    Question: {mcq.question_text[:60]}...")
    
    # Delete old MCQs
    if delete_count > 0:
        logger.info(f"\n🗑️  Deleting {delete_count} MCQs not from output_by_specialty...")
        
        with transaction.atomic():
            # Delete related records first
            flashcard_count = Flashcard.objects.filter(mcq__in=mcqs_to_delete).delete()[0]
            logger.info(f"  Deleted {flashcard_count} related flashcards")
            
            incorrect_count = IncorrectAnswer.objects.filter(mcq__in=mcqs_to_delete).delete()[0]
            logger.info(f"  Deleted {incorrect_count} related incorrect answers")
            
            bookmark_count = Bookmark.objects.filter(mcq__in=mcqs_to_delete).delete()[0]
            logger.info(f"  Deleted {bookmark_count} related bookmarks")
            
            # Delete the MCQs
            deleted_count = mcqs_to_delete.delete()[0]
            logger.info(f"✅ Deleted {deleted_count} MCQs")
    
    # Now check for duplicates within the remaining MCQs
    logger.info("\n🔍 Checking for duplicates...")
    
    # Find duplicates by question_text
    duplicates = MCQ.objects.values('question_text').annotate(
        count=Count('id')
    ).filter(count__gt=1)
    
    duplicate_count = len(duplicates)
    logger.info(f"Found {duplicate_count} duplicate questions")
    
    if duplicate_count > 0:
        logger.info("Removing duplicates (keeping the first occurrence)...")
        
        with transaction.atomic():
            for dup in duplicates:
                # Get all MCQs with this question text
                dup_mcqs = MCQ.objects.filter(question_text=dup['question_text']).order_by('id')
                
                # Keep the first, delete the rest
                to_delete = dup_mcqs[1:]
                for mcq in to_delete:
                    mcq.delete()
                    logger.info(f"  Deleted duplicate: {mcq.id}")
    
    # Final count
    final_count = MCQ.objects.count()
    logger.info(f"\n✅ Final MCQ count: {final_count}")
    
    # Verify all are from new import
    verified_count = MCQ.objects.filter(source_file__in=NEW_SOURCE_FILES).count()
    logger.info(f"Verified MCQs from output_by_specialty: {verified_count}")
    
    # Show distribution
    from django.db.models import Count
    subspecialty_counts = MCQ.objects.values('subspecialty').annotate(
        count=Count('id')
    ).order_by('-count')[:10]
    
    logger.info("\nTop subspecialties:")
    for item in subspecialty_counts:
        logger.info(f"  {item['subspecialty']}: {item['count']}")

def main():
    """Main function"""
    logger.info("Keep Only New Imports - Remove All Others")
    logger.info("=" * 50)
    
    keep_only_new_imports()
    
    logger.info("\n✅ Cleanup complete!")

if __name__ == "__main__":
    main()