"""
Management command to update exam type names in the database.
Changes:
- Promotion -> Basic level
- Part I -> Advanced
- Part II -> Board-level
"""

from django.core.management.base import BaseCommand
from mcq.models import MCQ
from django.db import transaction


class Command(BaseCommand):
    help = 'Update exam type names: Promotion->Basic level, Part I->Advanced, Part II->Board-level'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting exam type name updates...'))
        
        # Define the mapping
        exam_type_mapping = {
            'Promotion': 'Basic level',
            'Part I': 'Advanced',
            'Part II': 'Board-level',
            # Also handle variations
            'Part 1': 'Advanced',
            'Part 2': 'Board-level',
            'PartI': 'Advanced',
            'PartII': 'Board-level',
            'Part One': 'Advanced',
            'Part Two': 'Board-level',
            'part one': 'Advanced',
            'part two': 'Board-level',
        }
        
        with transaction.atomic():
            total_updated = 0
            
            for old_name, new_name in exam_type_mapping.items():
                # Update MCQs with exact match
                updated = MCQ.objects.filter(exam_type=old_name).update(exam_type=new_name)
                if updated > 0:
                    self.stdout.write(
                        self.style.SUCCESS(
                            f'Updated {updated} MCQs from "{old_name}" to "{new_name}"'
                        )
                    )
                    total_updated += updated
            
            # Also check for case variations
            # Update any remaining "part i" variations to "Advanced"
            part_i_variations = MCQ.objects.filter(exam_type__iregex=r'^part\s*i$|^part\s*1$')
            if part_i_variations.exists():
                count = part_i_variations.update(exam_type='Advanced')
                self.stdout.write(
                    self.style.SUCCESS(
                        f'Updated {count} MCQs with Part I variations to "Advanced"'
                    )
                )
                total_updated += count
            
            # Update any remaining "part ii" variations to "Board-level"
            part_ii_variations = MCQ.objects.filter(exam_type__iregex=r'^part\s*ii$|^part\s*2$')
            if part_ii_variations.exists():
                count = part_ii_variations.update(exam_type='Board-level')
                self.stdout.write(
                    self.style.SUCCESS(
                        f'Updated {count} MCQs with Part II variations to "Board-level"'
                    )
                )
                total_updated += count
            
            # Update any remaining "promotion" variations to "Basic level"
            promotion_variations = MCQ.objects.filter(exam_type__iexact='promotion')
            if promotion_variations.exists():
                count = promotion_variations.update(exam_type='Basic level')
                self.stdout.write(
                    self.style.SUCCESS(
                        f'Updated {count} MCQs with Promotion variations to "Basic level"'
                    )
                )
                total_updated += count
        
        self.stdout.write(
            self.style.SUCCESS(
                f'\nTotal MCQs updated: {total_updated}'
            )
        )
        
        # Show current exam type distribution
        self.stdout.write(self.style.SUCCESS('\nCurrent exam type distribution:'))
        exam_types = MCQ.objects.values('exam_type').distinct().order_by('exam_type')
        for exam_type in exam_types:
            if exam_type['exam_type']:
                count = MCQ.objects.filter(exam_type=exam_type['exam_type']).count()
                self.stdout.write(f"  {exam_type['exam_type']}: {count} MCQs")