from django.core.management.base import BaseCommand
from mcq.models import MCQ
import json
import os

class Command(BaseCommand):
    help = 'Export all MCQs for Heroku import'

    def handle(self, *args, **options):
        self.stdout.write("Exporting all MCQs for Heroku...")
        
        # Get all MCQs
        mcqs = MCQ.objects.all().order_by('id')
        total = mcqs.count()
        
        self.stdout.write(f"Total MCQs to export: {total}")
        
        # Create export data
        export_data = []
        
        for mcq in mcqs:
            mcq_data = {
                'model': 'mcq.mcq',
                'pk': mcq.id,
                'fields': {
                    'question_text': mcq.question_text,
                    'options': mcq.options,
                    'correct_answer': mcq.correct_answer,
                    'explanation': mcq.explanation,
                    'explanation_sections': mcq.explanation_sections,
                    'subspecialty': mcq.subspecialty,
                    'exam_type': mcq.exam_type,
                    'exam_year': mcq.exam_year,
                    'question_number': mcq.question_number,
                    'source_file': mcq.source_file,
                    'image_url': mcq.image_url,
                    'correct_answer_text': mcq.correct_answer_text,
                    'ai_generated': mcq.ai_generated,
                    'verification_confidence': mcq.verification_confidence,
                    'primary_category': mcq.primary_category,
                    'secondary_category': mcq.secondary_category,
                    'key_concept': mcq.key_concept,
                    'difficulty_level': mcq.difficulty_level
                }
            }
            export_data.append(mcq_data)
        
        # Save to file
        output_file = 'heroku_mcqs_export.json'
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(export_data, f, indent=2, ensure_ascii=False)
        
        self.stdout.write(self.style.SUCCESS(f"Successfully exported {total} MCQs to {output_file}"))
        
        # Check file size
        file_size = os.path.getsize(output_file)
        size_mb = file_size / (1024 * 1024)
        self.stdout.write(f"File size: {size_mb:.2f} MB")
        
        if size_mb > 50:
            self.stdout.write(self.style.WARNING("File is large. Consider splitting for upload."))