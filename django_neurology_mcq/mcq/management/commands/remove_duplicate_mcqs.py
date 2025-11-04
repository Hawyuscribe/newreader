"""
Management command to identify and remove duplicate MCQs
"""
from django.core.management.base import BaseCommand
from django.db.models import Count, Min
from mcq.models import MCQ
import json


class Command(BaseCommand):
    help = 'Identify and remove duplicate MCQs, keeping only one copy'

    def add_arguments(self, parser):
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Show what would be deleted without actually deleting',
        )
        parser.add_argument(
            '--verbose',
            action='store_true',
            help='Show detailed information about duplicates',
        )

    def handle(self, *args, **options):
        dry_run = options['dry_run']
        verbose = options['verbose']
        
        self.stdout.write("Finding duplicate MCQs...")
        
        # Find duplicates based on question_text and options
        duplicates = []
        total_duplicates = 0
        total_to_delete = 0
        
        # Get all MCQs
        all_mcqs = MCQ.objects.all()
        
        # Dictionary to track seen questions
        seen_questions = {}
        
        for mcq in all_mcqs:
            # Create a unique key based on question text and options
            options_str = json.dumps(mcq.get_options_dict(), sort_keys=True) if mcq.options else ""
            key = f"{mcq.question_text.strip().lower()}||{options_str}"
            
            if key in seen_questions:
                # This is a duplicate
                duplicates.append({
                    'original_id': seen_questions[key],
                    'duplicate_id': mcq.id,
                    'question_number': mcq.question_number,
                    'question_text': mcq.question_text[:100] + "..." if len(mcq.question_text) > 100 else mcq.question_text
                })
                total_duplicates += 1
            else:
                # First time seeing this question
                seen_questions[key] = mcq.id
        
        if not duplicates:
            self.stdout.write(self.style.SUCCESS("No duplicate MCQs found!"))
            return
        
        # Group duplicates
        duplicate_groups = {}
        for dup in duplicates:
            orig_id = dup['original_id']
            if orig_id not in duplicate_groups:
                duplicate_groups[orig_id] = []
            duplicate_groups[orig_id].append(dup['duplicate_id'])
        
        # Display results
        self.stdout.write(f"\nFound {total_duplicates} duplicate MCQs in {len(duplicate_groups)} groups")
        
        if verbose:
            self.stdout.write("\nDuplicate groups:")
            for orig_id, dup_ids in duplicate_groups.items():
                orig_mcq = MCQ.objects.get(id=orig_id)
                self.stdout.write(f"\n--- Group ---")
                self.stdout.write(f"Original: ID={orig_id}, Question #{orig_mcq.question_number}")
                self.stdout.write(f"Question: {orig_mcq.question_text[:100]}...")
                self.stdout.write(f"Duplicates: {len(dup_ids)} copies")
                for dup_id in dup_ids[:5]:  # Show first 5 duplicates
                    dup_mcq = MCQ.objects.get(id=dup_id)
                    self.stdout.write(f"  - ID={dup_id}, Question #{dup_mcq.question_number}")
                if len(dup_ids) > 5:
                    self.stdout.write(f"  ... and {len(dup_ids) - 5} more")
        
        # Delete duplicates
        if dry_run:
            self.stdout.write(self.style.WARNING(f"\nDRY RUN: Would delete {total_duplicates} duplicate MCQs"))
        else:
            # Get all duplicate IDs
            all_duplicate_ids = []
            for dup_list in duplicate_groups.values():
                all_duplicate_ids.extend(dup_list)
            
            # Delete in batches
            batch_size = 100
            for i in range(0, len(all_duplicate_ids), batch_size):
                batch_ids = all_duplicate_ids[i:i + batch_size]
                deleted_count = MCQ.objects.filter(id__in=batch_ids).delete()[0]
                total_to_delete += deleted_count
                self.stdout.write(f"Deleted batch: {deleted_count} MCQs")
            
            self.stdout.write(self.style.SUCCESS(f"\nSuccessfully deleted {total_to_delete} duplicate MCQs"))
            self.stdout.write(f"Kept {len(duplicate_groups)} original MCQs")