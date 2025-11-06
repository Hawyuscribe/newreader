import json
from django.core.management.base import BaseCommand
from django.db import transaction
from mcq.models import MCQ


class Command(BaseCommand):
    help = 'Sync all MCQs from exported JSON file'

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear all existing MCQs before importing',
        )

    def handle(self, *args, **options):
        if options['clear']:
            self.stdout.write('Clearing all existing MCQs...')
            MCQ.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Cleared all MCQs'))

        # Read the exported MCQs
        try:
            with open('local_mcqs_export.json', 'r', encoding='utf-8') as f:
                mcqs_data = json.load(f)
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR('local_mcqs_export.json not found!'))
            return

        self.stdout.write(f'Loading {len(mcqs_data)} MCQs...')
        
        created = 0
        updated = 0
        errors = 0
        
        with transaction.atomic():
            for mcq_data in mcqs_data:
                try:
                    # Check if MCQ already exists by question_number and question_text
                    existing_mcq = MCQ.objects.filter(
                        question_number=mcq_data['question_number'],
                        question_text=mcq_data['question_text']
                    ).first()
                    
                    if existing_mcq:
                        # Update existing MCQ
                        for field, value in mcq_data.items():
                            if value is not None:
                                setattr(existing_mcq, field, value)
                        existing_mcq.save()
                        updated += 1
                    else:
                        # Create new MCQ
                        MCQ.objects.create(**mcq_data)
                        created += 1
                        
                except Exception as e:
                    errors += 1
                    self.stdout.write(
                        self.style.WARNING(
                            f'Error with MCQ {mcq_data.get("question_number", "Unknown")}: {str(e)}'
                        )
                    )
        
        self.stdout.write(
            self.style.SUCCESS(
                f'\nImport complete!\n'
                f'Created: {created}\n'
                f'Updated: {updated}\n'
                f'Errors: {errors}\n'
                f'Total MCQs in database: {MCQ.objects.count()}'
            )
        )