"""
Export vascular neurology MCQs to CSV format for analysis.
"""
import csv
import json
from django.core.management.base import BaseCommand
from mcq.models import MCQ
from datetime import datetime


class Command(BaseCommand):
    help = 'Export vascular neurology/stroke MCQs to CSV format'

    def add_arguments(self, parser):
        parser.add_argument(
            '--filename',
            type=str,
            default=f'vascular_mcqs_export_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv',
            help='Output filename for the CSV export'
        )

    def handle(self, *args, **options):
        filename = options['filename']
        
        # Query for vascular neurology MCQs
        vascular_mcqs = MCQ.objects.filter(
            subspecialty__in=['Vascular Neurology/Stroke', 'Vascular Neurology', 'Stroke']
        ).order_by('exam_type', 'exam_year', 'question_number')
        
        self.stdout.write(f"Found {vascular_mcqs.count()} vascular neurology MCQs")
        
        # Define CSV headers
        headers = [
            'ID',
            'Question Number',
            'Exam Type',
            'Exam Year',
            'Question Text',
            'Option A',
            'Option B',
            'Option C',
            'Option D',
            'Option E',
            'Option F',
            'Correct Answer',
            'Subspecialty',
            'Conceptual Foundation',
            'Pathophysiology',
            'Clinical Correlation',
            'Diagnostic Approach',
            'Classification and Neurology',
            'Management Principles',
            'Option Analysis',
            'Clinical Pearls',
            'Current Evidence',
            'Has Image',
            'Image URL',
            'Source File'
        ]
        
        # Write to CSV
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headers)
            
            for mcq in vascular_mcqs:
                # Get options
                options = mcq.get_options_dict()
                
                # Extract explanation sections
                explanation_sections = mcq.explanation_sections or {}
                
                # Helper function to get section content
                def get_section(keys):
                    """Get section content checking multiple possible keys"""
                    for key in keys:
                        if key in explanation_sections and explanation_sections[key]:
                            return explanation_sections[key].replace('\n', ' ').strip()
                    return ''
                
                # Create row data
                row = [
                    mcq.id,
                    mcq.question_number or '',
                    mcq.exam_type or '',
                    mcq.exam_year or '',
                    mcq.question_text,
                    options.get('A', ''),
                    options.get('B', ''),
                    options.get('C', ''),
                    options.get('D', ''),
                    options.get('E', ''),
                    options.get('F', ''),
                    mcq.correct_answer,
                    mcq.subspecialty,
                    get_section(['conceptual foundation', 'conceptual_foundation']),
                    get_section(['pathophysiology', 'pathophysiological_mechanisms']),
                    get_section(['clinical correlation', 'clinical_correlation', 'clinical context', 'clinical_context']),
                    get_section(['diagnostic approach', 'diagnostic_approach']),
                    get_section(['classification and neurology', 'classification_neurology', 'classification_and_nosology']),
                    get_section(['management principles', 'management_principles']),
                    get_section(['option analysis', 'option_analysis']),
                    get_section(['clinical pearls', 'clinical_pearls', 'key insight', 'key_insight']),
                    get_section(['current evidence', 'current_evidence', 'quick reference', 'quick_reference']),
                    'Yes' if mcq.image_url else 'No',
                    mcq.image_url or '',
                    mcq.source_file or ''
                ]
                
                writer.writerow(row)
        
        self.stdout.write(self.style.SUCCESS(f"Successfully exported {vascular_mcqs.count()} MCQs to {filename}"))
        
        # Also create a more detailed JSON export for complete data
        json_filename = filename.replace('.csv', '.json')
        
        mcq_data = []
        for mcq in vascular_mcqs:
            mcq_dict = {
                'id': mcq.id,
                'question_number': mcq.question_number,
                'exam_type': mcq.exam_type,
                'exam_year': mcq.exam_year,
                'question_text': mcq.question_text,
                'options': mcq.get_options_dict(),
                'correct_answer': mcq.correct_answer,
                'subspecialty': mcq.subspecialty,
                'explanation_sections': mcq.explanation_sections,
                'has_image': bool(mcq.image_url),
                'image_url': mcq.image_url,
                'source_file': mcq.source_file
            }
            mcq_data.append(mcq_dict)
        
        with open(json_filename, 'w', encoding='utf-8') as jsonfile:
            json.dump(mcq_data, jsonfile, indent=2, ensure_ascii=False)
        
        self.stdout.write(self.style.SUCCESS(f"Also exported JSON format to {json_filename}"))
        
        # Print summary statistics
        self.stdout.write("\n=== Export Summary ===")
        self.stdout.write(f"Total MCQs: {vascular_mcqs.count()}")
        
        # Count by exam type and year
        exam_counts = {}
        for mcq in vascular_mcqs:
            key = f"{mcq.exam_type or 'Unknown'} - {mcq.exam_year or 'Unknown'}"
            exam_counts[key] = exam_counts.get(key, 0) + 1
        
        self.stdout.write("\nBreakdown by Exam Type and Year:")
        for exam_key, count in sorted(exam_counts.items()):
            self.stdout.write(f"  {exam_key}: {count} MCQs")
        
        # Count MCQs with explanations
        with_explanations = sum(1 for mcq in vascular_mcqs if mcq.explanation_sections)
        self.stdout.write(f"\nMCQs with explanation sections: {with_explanations}/{vascular_mcqs.count()}")
        
        # Count MCQs with images
        with_images = sum(1 for mcq in vascular_mcqs if mcq.image_url)
        self.stdout.write(f"MCQs with images: {with_images}/{vascular_mcqs.count()}")