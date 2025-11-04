from django.core.management.base import BaseCommand
from django.db import transaction
from mcq.models import MCQ
import json
import os


class Command(BaseCommand):
    help = 'Import missing MCQs from consolidated file - quick execution version'

    def handle(self, *args, **options):
        self.stdout.write('Starting MCQ import...')
        
        try:
            # Find consolidated file
            paths = [
                'consolidated_all_mcqs.json',
                '/app/consolidated_all_mcqs.json',
                '/app/django_neurology_mcq/consolidated_all_mcqs.json',
                os.path.join(os.path.dirname(__file__), '../../../../consolidated_all_mcqs.json')
            ]
            
            json_file = None
            for path in paths:
                if os.path.exists(path):
                    json_file = path
                    break
            
            if not json_file:
                self.stdout.write(self.style.ERROR('Cannot find consolidated_all_mcqs.json'))
                return
            
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            all_mcqs = data.get('mcqs', [])
            self.stdout.write(f'Loaded {len(all_mcqs)} MCQs')
            
            # Get existing
            existing = set(MCQ.objects.values_list('question_number', flat=True))
            self.stdout.write(f'Found {len(existing)} existing MCQs')
            
            # Find missing
            missing = []
            for mcq in all_mcqs:
                if mcq.get('question_number') and mcq['question_number'] not in existing:
                    missing.append(mcq)
            
            self.stdout.write(f'Found {len(missing)} missing MCQs')
            
            if not missing:
                self.stdout.write(self.style.SUCCESS('No missing MCQs!'))
                return
            
            # Import all at once
            created = 0
            with transaction.atomic():
                for mcq_data in missing:
                    try:
                        explanation_sections = {}
                        if 'explanation' in mcq_data and isinstance(mcq_data['explanation'], dict):
                            explanation_sections = mcq_data['explanation']
                        
                        MCQ.objects.create(
                            question_number=mcq_data.get('question_number', ''),
                            question_text=mcq_data.get('question', ''),
                            options=mcq_data.get('options', []),
                            correct_answer=mcq_data.get('correct_answer', ''),
                            correct_answer_text=mcq_data.get('correct_answer_text', ''),
                            subspecialty=mcq_data.get('subspecialty', 'General Neurology'),
                            explanation_sections=explanation_sections,
                            source_file=mcq_data.get('source_file', ''),
                            exam_type=mcq_data.get('exam_type', ''),
                            exam_year=mcq_data.get('exam_year', ''),
                            ai_generated=mcq_data.get('ai_generated', False),
                            unified_explanation=mcq_data.get('unified_explanation', ''),
                            image_url=mcq_data.get('image_url', '')
                        )
                        created += 1
                        if created % 50 == 0:
                            self.stdout.write(f'Imported {created} MCQs...')
                    except Exception as e:
                        self.stdout.write(self.style.WARNING(f'Error: {mcq_data.get("question_number")}: {str(e)}'))
            
            total = MCQ.objects.count()
            self.stdout.write(self.style.SUCCESS(f'\nSuccess! Imported {created} MCQs'))
            self.stdout.write(self.style.SUCCESS(f'Total MCQs: {total}'))
            
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {str(e)}'))
            import traceback
            traceback.print_exc()