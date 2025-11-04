from django.core.management.base import BaseCommand
from mcq.models import MCQ
import json


class Command(BaseCommand):
    help = 'Check for MCQs without answer options in the database'

    def handle(self, *args, **options):
        all_mcqs = MCQ.objects.all()
        total_count = all_mcqs.count()
        
        missing_options_mcqs = []
        empty_options_mcqs = []
        invalid_json_mcqs = []
        
        for mcq in all_mcqs:
            # Check if options field exists
            if not hasattr(mcq, 'options') or mcq.options is None:
                missing_options_mcqs.append(mcq)
                continue
                
            # Check if options is an empty string
            if isinstance(mcq.options, str) and mcq.options.strip() == '':
                empty_options_mcqs.append(mcq)
                continue
                
            # Try to parse JSON if it's a string
            if isinstance(mcq.options, str):
                try:
                    options_dict = json.loads(mcq.options)
                    # Check if the parsed JSON is empty
                    if not options_dict:
                        empty_options_mcqs.append(mcq)
                except json.JSONDecodeError:
                    invalid_json_mcqs.append(mcq)
                    continue
            elif isinstance(mcq.options, dict):
                # Check if the dict is empty
                if not mcq.options:
                    empty_options_mcqs.append(mcq)
        
        # Summary report
        self.stdout.write(self.style.NOTICE('=== MCQ Options Analysis ==='))
        self.stdout.write(f'Total MCQs: {total_count}')
        self.stdout.write(f'MCQs with no options field: {len(missing_options_mcqs)}')
        self.stdout.write(f'MCQs with empty options: {len(empty_options_mcqs)}')
        self.stdout.write(f'MCQs with invalid JSON in options: {len(invalid_json_mcqs)}')
        
        total_problematic = len(missing_options_mcqs) + len(empty_options_mcqs) + len(invalid_json_mcqs)
        self.stdout.write(self.style.ERROR(f'Total MCQs without valid options: {total_problematic}'))
        self.stdout.write(f'Percentage with problems: {(total_problematic/total_count*100):.2f}%')
        
        # Show sample problematic MCQs
        if missing_options_mcqs:
            self.stdout.write(self.style.WARNING('\nSample MCQs with no options field:'))
            for mcq in missing_options_mcqs[:3]:
                self.stdout.write(f'ID: {mcq.id}, Question: {mcq.question_text[:100]}...')
                
        if empty_options_mcqs:
            self.stdout.write(self.style.WARNING('\nSample MCQs with empty options:'))
            for mcq in empty_options_mcqs[:3]:
                self.stdout.write(f'ID: {mcq.id}, Question: {mcq.question_text[:100]}...')
                
        if invalid_json_mcqs:
            self.stdout.write(self.style.WARNING('\nSample MCQs with invalid JSON:'))
            for mcq in invalid_json_mcqs[:3]:
                self.stdout.write(f'ID: {mcq.id}, Options content: {mcq.options[:50]}...')
                self.stdout.write(f'Question: {mcq.question_text[:100]}...')
        
        # Check a properly formatted MCQ for comparison
        valid_mcqs = MCQ.objects.exclude(
            id__in=[m.id for m in missing_options_mcqs + empty_options_mcqs + invalid_json_mcqs]
        )
        
        if valid_mcqs.exists():
            sample_valid = valid_mcqs.first()
            self.stdout.write(self.style.SUCCESS('\nSample valid MCQ options format:'))
            self.stdout.write(f'ID: {sample_valid.id}')
            self.stdout.write(f'Options type: {type(sample_valid.options)}')
            if isinstance(sample_valid.options, str):
                try:
                    parsed = json.loads(sample_valid.options)
                    self.stdout.write(f'Parsed options: {json.dumps(parsed, indent=2)}')
                except:
                    self.stdout.write(f'Raw options: {sample_valid.options[:200]}...')
            else:
                self.stdout.write(f'Options: {sample_valid.options}')