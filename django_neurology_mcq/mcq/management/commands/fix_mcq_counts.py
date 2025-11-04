"""
Django management command to fix MCQ counts by clearing and reimporting
"""
from django.core.management.base import BaseCommand
from django.db import transaction
from django.core.management import call_command
from mcq.models import MCQ, Subspecialty
import json
import os
from collections import defaultdict

class Command(BaseCommand):
    help = 'Fix MCQ counts by clearing and reimporting from fixtures'
    
    def add_arguments(self, parser):
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Run in dry-run mode (no changes)',
        )
        parser.add_argument(
            '--fixture-path',
            type=str,
            help='Path to fixture file',
            default='rere_fixtures.json'
        )
    
    def handle(self, *args, **options):
        dry_run = options['dry_run']
        fixture_path = options['fixture_path']
        
        self.stdout.write(self.style.WARNING('=' * 80))
        self.stdout.write(self.style.WARNING('MCQ COUNT FIX TOOL'))
        self.stdout.write(self.style.WARNING('=' * 80))
        
        # Expected counts
        expected_counts = {
            "Movement Disorders": 269,
            "Vascular Neurology/Stroke": 439,
            "Neuromuscular": 483,
            "Total": 2853
        }
        
        # Show current state
        self.stdout.write('\nCurrent MCQ counts:')
        current_total = MCQ.objects.count()
        self.stdout.write(f'Total: {current_total}')
        
        subspecialty_counts = defaultdict(int)
        for mcq in MCQ.objects.all():
            if mcq.subspecialty:
                subspecialty_counts[mcq.subspecialty.name] += 1
        
        for sub_name, count in sorted(subspecialty_counts.items()):
            expected = expected_counts.get(sub_name, 'N/A')
            status = self.style.SUCCESS('✓') if count == expected else self.style.ERROR('✗')
            self.stdout.write(f'  {sub_name}: {count} (expected: {expected}) {status}')
        
        if dry_run:
            self.stdout.write(self.style.WARNING('\nDRY RUN MODE - No changes will be made'))
            return
        
        # Ask for confirmation
        self.stdout.write(self.style.WARNING('\nThis will DELETE ALL MCQs and reimport them!'))
        confirm = input('Type "yes" to continue: ')
        if confirm.lower() != 'yes':
            self.stdout.write(self.style.ERROR('Aborted'))
            return
        
        try:
            with transaction.atomic():
                # Clear all MCQs
                self.stdout.write('\nClearing all MCQs...')
                deleted_count = MCQ.objects.all().delete()[0]
                self.stdout.write(f'Deleted {deleted_count} MCQs')
                
                # Check if fixture file exists
                if not os.path.exists(fixture_path):
                    # Try alternative paths
                    alt_paths = [
                        'rere_fixtures.json',
                        'rere_final_fixtures.json',
                        'rere_complete_fixtures.json',
                        'final_rere_fixtures.json'
                    ]
                    
                    for alt_path in alt_paths:
                        if os.path.exists(alt_path):
                            fixture_path = alt_path
                            self.stdout.write(f'Using fixture file: {fixture_path}')
                            break
                    else:
                        raise FileNotFoundError(f'No fixture file found. Tried: {", ".join(alt_paths)}')
                
                # Load fixture
                self.stdout.write(f'\nLoading fixtures from {fixture_path}...')
                call_command('loaddata', fixture_path)
                
                # Verify import
                new_total = MCQ.objects.count()
                self.stdout.write(f'\nImported {new_total} MCQs')
                
                # Check new counts
                new_subspecialty_counts = defaultdict(int)
                for mcq in MCQ.objects.all():
                    if mcq.subspecialty:
                        new_subspecialty_counts[mcq.subspecialty.name] += 1
                
                self.stdout.write('\nNew subspecialty counts:')
                all_correct = True
                for sub_name, expected in expected_counts.items():
                    if sub_name == 'Total':
                        actual = new_total
                    else:
                        actual = new_subspecialty_counts.get(sub_name, 0)
                    
                    if actual == expected:
                        self.stdout.write(self.style.SUCCESS(f'  ✓ {sub_name}: {actual}'))
                    else:
                        self.stdout.write(self.style.ERROR(f'  ✗ {sub_name}: {actual} (expected {expected})'))
                        all_correct = False
                
                if all_correct:
                    self.stdout.write(self.style.SUCCESS('\n✓ All counts are correct!'))
                else:
                    self.stdout.write(self.style.ERROR('\n✗ Some counts are still incorrect'))
                    
                    # Show which MCQs might be duplicated
                    self.stdout.write('\nChecking for duplicates...')
                    questions = {}
                    duplicates = []
                    
                    for mcq in MCQ.objects.all():
                        if mcq.question in questions:
                            duplicates.append((mcq.id, questions[mcq.question], mcq.subspecialty.name if mcq.subspecialty else 'None'))
                        else:
                            questions[mcq.question] = mcq.id
                    
                    if duplicates:
                        self.stdout.write(f'Found {len(duplicates)} duplicate questions!')
                        for dup_id, orig_id, subspecialty in duplicates[:10]:
                            self.stdout.write(f'  MCQ {dup_id} duplicates {orig_id} (subspecialty: {subspecialty})')
                
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'\nError: {str(e)}'))
            raise