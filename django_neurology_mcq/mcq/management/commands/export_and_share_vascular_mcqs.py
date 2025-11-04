"""
Export vascular neurology MCQs and provide a shareable link
"""
import csv
import json
import io
import base64
from django.core.management.base import BaseCommand
from mcq.models import MCQ
from datetime import datetime
import requests


class Command(BaseCommand):
    help = 'Export vascular neurology MCQs and provide shareable links'

    def handle(self, *args, **options):
        # Query for vascular neurology MCQs
        vascular_mcqs = MCQ.objects.filter(
            subspecialty__in=['Vascular Neurology/Stroke', 'Vascular Neurology', 'Stroke']
        ).order_by('exam_type', 'exam_year', 'question_number')
        
        self.stdout.write(f"Found {vascular_mcqs.count()} vascular neurology MCQs")
        
        # Create CSV in memory
        csv_output = io.StringIO()
        headers = [
            'ID', 'Question Number', 'Exam Type', 'Exam Year', 'Question Text',
            'Option A', 'Option B', 'Option C', 'Option D', 'Option E', 'Option F',
            'Correct Answer', 'Subspecialty', 'Conceptual Foundation',
            'Pathophysiology', 'Clinical Correlation', 'Diagnostic Approach',
            'Classification and Neurology', 'Management Principles',
            'Option Analysis', 'Clinical Pearls', 'Current Evidence',
            'Has Image', 'Image URL', 'Source File'
        ]
        
        writer = csv.writer(csv_output)
        writer.writerow(headers)
        
        for mcq in vascular_mcqs:
            options = mcq.get_options_dict()
            explanation_sections = mcq.explanation_sections or {}
            
            def get_section(keys):
                for key in keys:
                    if key in explanation_sections and explanation_sections[key]:
                        return explanation_sections[key].replace('\n', ' ').strip()
                return ''
            
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
                get_section(['clinical correlation', 'clinical_correlation', 'clinical context']),
                get_section(['diagnostic approach', 'diagnostic_approach']),
                get_section(['classification and neurology', 'classification_neurology', 'classification_and_nosology']),
                get_section(['management principles', 'management_principles']),
                get_section(['option analysis', 'option_analysis']),
                get_section(['clinical pearls', 'clinical_pearls', 'key insight']),
                get_section(['current evidence', 'current_evidence', 'quick reference']),
                'Yes' if mcq.image_url else 'No',
                mcq.image_url or '',
                mcq.source_file or ''
            ]
            writer.writerow(row)
        
        # Get the CSV content
        csv_content = csv_output.getvalue()
        csv_output.close()
        
        # Upload to transfer.sh (simple file sharing that works with curl)
        try:
            response = requests.put(
                f'https://transfer.sh/vascular_mcqs_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv',
                data=csv_content.encode('utf-8'),
                headers={'Max-Days': '1', 'Max-Downloads': '50'}
            )
            
            if response.status_code == 200:
                download_url = response.text.strip()
                self.stdout.write(self.style.SUCCESS(f"CSV file uploaded successfully!"))
                self.stdout.write(f"Download URL: {download_url}")
                self.stdout.write("This link will expire in 1 day or after 50 downloads")
                
                # Also create a smaller summary file for preview
                summary_data = {
                    'total_mcqs': vascular_mcqs.count(),
                    'breakdown': {},
                    'with_explanations': sum(1 for mcq in vascular_mcqs if mcq.explanation_sections),
                    'with_images': sum(1 for mcq in vascular_mcqs if mcq.image_url)
                }
                
                for mcq in vascular_mcqs:
                    key = f"{mcq.exam_type or 'Unknown'} - {mcq.exam_year or 'Unknown'}"
                    summary_data['breakdown'][key] = summary_data['breakdown'].get(key, 0) + 1
                
                summary_json = json.dumps(summary_data, indent=2)
                
                # Upload summary
                summary_response = requests.put(
                    f'https://transfer.sh/vascular_mcqs_summary_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json',
                    data=summary_json.encode('utf-8'),
                    headers={'Max-Days': '1', 'Max-Downloads': '50'}
                )
                
                if summary_response.status_code == 200:
                    summary_url = summary_response.text.strip()
                    self.stdout.write(f"\nSummary JSON URL: {summary_url}")
                
                self.stdout.write(f"\nTo download the CSV file, use:")
                self.stdout.write(f"curl {download_url} -o vascular_mcqs.csv")
                
            else:
                self.stdout.write(self.style.ERROR(f"Upload failed with status {response.status_code}"))
                
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error uploading file: {str(e)}"))