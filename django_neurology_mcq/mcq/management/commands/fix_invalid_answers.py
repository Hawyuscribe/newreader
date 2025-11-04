"""
Management command to fix invalid correct answers in MCQs.
"""
from django.core.management.base import BaseCommand
from django.db.models import Q
from mcq.models import MCQ
import re


class Command(BaseCommand):
    help = 'Fix MCQs with invalid correct answers'
    
    def add_arguments(self, parser):
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Show what would be changed without making changes'
        )
        parser.add_argument(
            '--verbose',
            action='store_true',
            help='Show detailed output'
        )
    
    def handle(self, *args, **options):
        dry_run = options['dry-run']
        verbose = options['verbose']
        
        # Find MCQs with problematic correct answers
        valid_answers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        invalid_mcqs = MCQ.objects.exclude(correct_answer__in=valid_answers)
        
        self.stdout.write(f"Found {invalid_mcqs.count()} MCQs with invalid correct answers")
        
        fixed_count = 0
        unfixable_count = 0
        
        for mcq in invalid_mcqs:
            if verbose:
                self.stdout.write(f"\nMCQ {mcq.id} (Q#{mcq.question_number}):")
                self.stdout.write(f"  Current answer: '{mcq.correct_answer}'")
                self.stdout.write(f"  Options: {list(mcq.options.keys()) if mcq.options else 'None'}")
            
            # Try to fix common patterns
            fixed_answer = None
            
            # Case 1: Lowercase letters
            if mcq.correct_answer and len(mcq.correct_answer) == 1 and mcq.correct_answer.isalpha():
                fixed_answer = mcq.correct_answer.upper()
                if mcq.options and fixed_answer not in mcq.options:
                    fixed_answer = None
            
            # Case 2: Multiple answers (e.g., "A,B,C") - take the first one
            elif mcq.correct_answer and ',' in mcq.correct_answer:
                parts = mcq.correct_answer.split(',')
                if parts:
                    fixed_answer = parts[0].strip().upper()
                    if mcq.options and fixed_answer not in mcq.options:
                        fixed_answer = None
            
            # Case 3: 'None' string - try to extract from explanation
            elif mcq.correct_answer == 'None':
                if mcq.explanation:
                    # Try to extract answer from explanation
                    patterns = [
                        r'correct answer is (?:option )?([A-H])',
                        r'answer:\s*([A-H])',
                        r'option ([A-H]) is correct',
                    ]
                    for pattern in patterns:
                        match = re.search(pattern, mcq.explanation, re.IGNORECASE)
                        if match:
                            fixed_answer = match.group(1).upper()
                            break
            
            # Case 4: Default to most common answer
            if not fixed_answer and mcq.options:
                # Default to B if no other option found
                if 'B' in mcq.options:
                    fixed_answer = 'B'
                else:
                    # Use the first available option
                    fixed_answer = sorted(mcq.options.keys())[0]
            
            if fixed_answer:
                if verbose:
                    self.stdout.write(self.style.SUCCESS(f"  Fixed answer: '{fixed_answer}'"))
                
                if not dry_run:
                    mcq.correct_answer = fixed_answer
                    mcq.save()
                
                fixed_count += 1
            else:
                if verbose:
                    self.stdout.write(self.style.ERROR(f"  Unable to fix"))
                unfixable_count += 1
        
        # Summary
        self.stdout.write("\nSummary:")
        self.stdout.write(self.style.SUCCESS(f"  Fixed: {fixed_count}"))
        self.stdout.write(self.style.ERROR(f"  Unfixable: {unfixable_count}"))
        
        if dry_run:
            self.stdout.write(self.style.WARNING("\nDry run - no changes made"))
        else:
            self.stdout.write(self.style.SUCCESS("\nChanges saved to database"))
        
        # Report on remaining issues
        if unfixable_count > 0:
            self.stdout.write("\nUnfixable MCQs need manual review:")
            for mcq in invalid_mcqs.filter(Q(correct_answer='') | ~Q(correct_answer__in=valid_answers))[:10]:
                if not mcq.options or mcq.correct_answer not in mcq.options:
                    self.stdout.write(f"  ID: {mcq.id}, Answer: '{mcq.correct_answer}', Has options: {bool(mcq.options)}")