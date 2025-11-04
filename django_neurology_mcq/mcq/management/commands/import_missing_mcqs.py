import json
from django.core.management.base import BaseCommand
from django.db import transaction
from mcq.models import MCQ


class Command(BaseCommand):
    help = 'Import only missing MCQs from consolidated file'

    def handle(self, *args, **options):
        self.stdout.write('Loading consolidated MCQs file...')
        
        try:
            # Try different locations for the consolidated file
            import os
            possible_paths = [
                'consolidated_all_mcqs.json',
                '../consolidated_all_mcqs.json',
                '../../consolidated_all_mcqs.json',
                '../../../consolidated_all_mcqs.json',
                os.path.join(os.path.dirname(__file__), '../../../../consolidated_all_mcqs.json')
            ]
            
            json_file_path = None
            for path in possible_paths:
                if os.path.exists(path):
                    json_file_path = path
                    break
            
            if not json_file_path:
                self.stdout.write(self.style.ERROR('Could not find consolidated_all_mcqs.json in any expected location'))
                return
            
            self.stdout.write(f'Found consolidated file at: {json_file_path}')
            with open(json_file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Handle different JSON structures
            if isinstance(data, dict) and 'mcqs' in data:
                all_mcqs = data['mcqs']
            elif isinstance(data, list):
                all_mcqs = data
            else:
                self.stdout.write(self.style.ERROR('Unexpected JSON structure'))
                return
            
            self.stdout.write(f'Loaded {len(all_mcqs)} MCQs from file')
            
            # Get existing question numbers
            existing_question_numbers = set(MCQ.objects.values_list('question_number', flat=True))
            self.stdout.write(f'Found {len(existing_question_numbers)} existing MCQs in database')
            
            # Filter to only missing MCQs
            missing_mcqs = []
            for mcq_data in all_mcqs:
                question_number = mcq_data.get('question_number', '')
                if question_number and question_number not in existing_question_numbers:
                    missing_mcqs.append(mcq_data)
            
            self.stdout.write(f'Found {len(missing_mcqs)} missing MCQs to import')
            
            if not missing_mcqs:
                self.stdout.write(self.style.SUCCESS('No missing MCQs to import!'))
                return
            
            # Import missing MCQs
            created_count = 0
            with transaction.atomic():
                for mcq_data in missing_mcqs:
                    try:
                        # Process explanation sections
                        explanation_sections = {}
                        if 'explanation' in mcq_data and isinstance(mcq_data['explanation'], dict):
                            explanation_sections = mcq_data['explanation']
                        
                        # Create MCQ with correct field mapping
                        mcq = MCQ(
                            question_number=mcq_data.get('question_number', ''),
                            question_text=mcq_data.get('question', ''),  # question -> question_text
                            options=mcq_data.get('options', []),  # Already in array format
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
                        mcq.save()
                        created_count += 1
                        
                        if created_count % 50 == 0:
                            self.stdout.write(f'Imported {created_count}/{len(missing_mcqs)} missing MCQs...')
                    
                    except Exception as e:
                        self.stdout.write(
                            self.style.WARNING(
                                f'Error importing MCQ {mcq_data.get("question_number", "Unknown")}: {str(e)}'
                            )
                        )
            
            # Final summary
            total_mcqs = MCQ.objects.count()
            self.stdout.write(
                self.style.SUCCESS(
                    f'\nSuccessfully imported {created_count} missing MCQs!\n'
                    f'Total MCQs in database: {total_mcqs}'
                )
            )
            
            # Show subspecialty breakdown
            from django.db.models import Count
            self.stdout.write('\nSubspecialty breakdown:')
            subspecialty_counts = MCQ.objects.values('subspecialty').annotate(count=Count('id')).order_by('-count')
            for item in subspecialty_counts:
                self.stdout.write(f'  {item["subspecialty"]}: {item["count"]}')
        
        except FileNotFoundError:
            self.stdout.write(
                self.style.ERROR(
                    'consolidated_all_mcqs.json file not found. '
                    'Please ensure the file exists in the project root.'
                )
            )
        except json.JSONDecodeError as e:
            self.stdout.write(self.style.ERROR(f'Error parsing JSON file: {str(e)}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Unexpected error: {str(e)}'))