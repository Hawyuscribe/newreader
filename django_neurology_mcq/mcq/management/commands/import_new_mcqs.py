"""
Django management command to import new MCQs
"""
from django.core.management.base import BaseCommand
from django.db import transaction
from mcq.models import MCQ
import json
import os
from datetime import datetime


class Command(BaseCommand):
    help = 'Import new MCQs from JSON data'

    def add_arguments(self, parser):
        parser.add_argument(
            '--data-file',
            type=str,
            help='Path to JSON file containing MCQ data'
        )
        parser.add_argument(
            '--clear-existing',
            action='store_true',
            help='Clear existing MCQs before import'
        )

    def process_explanation(self, mcq_data):
        """Process explanation data from either unified or subsection format"""
        explanation_sections = {}
        
        if 'unified_explanation' in mcq_data and mcq_data['unified_explanation']:
            unified_text = mcq_data['unified_explanation']
            explanation = unified_text
            
            if 'explanation' in mcq_data and isinstance(mcq_data['explanation'], dict):
                exp_dict = mcq_data['explanation']
                section_mapping = {
                    'option_analysis': 'option_analysis',
                    'conceptual_foundation': 'conceptual_foundation',
                    'pathophysiology': 'pathophysiology',
                    'clinical_manifestation': 'clinical_manifestation',
                    'diagnostic_approach': 'diagnostic_approach',
                    'management_principles': 'management_principles',
                    'follow_up_guidelines': 'follow_up_guidelines',
                    'clinical_pearls': 'clinical_pearls',
                    'references': 'references'
                }
                
                for old_key, new_key in section_mapping.items():
                    if old_key in exp_dict and exp_dict[old_key] and \
                       not exp_dict[old_key].startswith("This section information is included"):
                        explanation_sections[new_key] = exp_dict[old_key]
            
        elif 'explanation' in mcq_data and isinstance(mcq_data['explanation'], dict):
            exp_dict = mcq_data['explanation']
            explanation_parts = []
            
            if exp_dict.get('option_analysis'):
                explanation_parts.append(f"**Option Analysis:**\n{exp_dict['option_analysis']}")
            if exp_dict.get('conceptual_foundation'):
                explanation_parts.append(f"**Conceptual Foundation:**\n{exp_dict['conceptual_foundation']}")
            if exp_dict.get('pathophysiology'):
                explanation_parts.append(f"**Pathophysiology:**\n{exp_dict['pathophysiology']}")
            if exp_dict.get('clinical_manifestation'):
                explanation_parts.append(f"**Clinical Manifestation:**\n{exp_dict['clinical_manifestation']}")
            if exp_dict.get('diagnostic_approach'):
                explanation_parts.append(f"**Diagnostic Approach:**\n{exp_dict['diagnostic_approach']}")
            if exp_dict.get('management_principles'):
                explanation_parts.append(f"**Management Principles:**\n{exp_dict['management_principles']}")
            if exp_dict.get('follow_up_guidelines'):
                explanation_parts.append(f"**Follow-up Guidelines:**\n{exp_dict['follow_up_guidelines']}")
            
            if exp_dict.get('clinical_pearls'):
                if isinstance(exp_dict['clinical_pearls'], list):
                    pearls_text = '\n'.join(f"• {pearl}" for pearl in exp_dict['clinical_pearls'])
                else:
                    pearls_text = exp_dict['clinical_pearls']
                explanation_parts.append(f"**Clinical Pearls:**\n{pearls_text}")
                
            if exp_dict.get('references'):
                explanation_parts.append(f"**References:**\n{exp_dict['references']}")
            
            explanation = '\n\n'.join(explanation_parts) if explanation_parts else ""
            
            explanation_sections = {
                'option_analysis': exp_dict.get('option_analysis', ''),
                'conceptual_foundation': exp_dict.get('conceptual_foundation', ''),
                'pathophysiology': exp_dict.get('pathophysiology', ''),
                'clinical_manifestation': exp_dict.get('clinical_manifestation', ''),
                'diagnostic_approach': exp_dict.get('diagnostic_approach', ''),
                'management_principles': exp_dict.get('management_principles', ''),
                'follow_up_guidelines': exp_dict.get('follow_up_guidelines', ''),
                'clinical_pearls': exp_dict.get('clinical_pearls', []),
                'references': exp_dict.get('references', '')
            }
        else:
            explanation = mcq_data.get('explanation', '') or ''
            
        return explanation, explanation_sections

    def handle(self, *args, **options):
        data_file = options.get('data_file')
        clear_existing = options.get('clear_existing', False)
        
        if not data_file:
            self.stdout.write(self.style.ERROR('Please provide a data file path'))
            return
        
        # Load data
        try:
            with open(data_file, 'r') as f:
                data = json.load(f)
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error loading data file: {e}'))
            return
        
        # Clear existing if requested
        if clear_existing:
            count = MCQ.objects.count()
            MCQ.objects.all().delete()
            self.stdout.write(self.style.SUCCESS(f'Deleted {count} existing MCQs'))
        
        # Import MCQs
        total_imported = 0
        errors = []
        
        with transaction.atomic():
            specialty = data.get('specialty', 'Unknown')
            mcqs = data.get('mcqs', [])
            
            self.stdout.write(f'Importing {len(mcqs)} MCQs for {specialty}...')
            
            for idx, mcq_data in enumerate(mcqs):
                try:
                    explanation, explanation_sections = self.process_explanation(mcq_data)
                    
                    mcq_obj = MCQ(
                        question_number=mcq_data.get('question_number', ''),
                        question_text=mcq_data.get('question', ''),
                        options=mcq_data.get('options', {}),
                        correct_answer=mcq_data.get('correct_answer', ''),
                        subspecialty=mcq_data.get('subspecialty', specialty),
                        source_file=mcq_data.get('source_file', ''),
                        exam_type=mcq_data.get('exam_type', ''),
                        exam_year=mcq_data.get('exam_year'),
                        explanation=explanation,
                        explanation_sections=explanation_sections if explanation_sections else None,
                        image_url=mcq_data.get('image_url', '')
                    )
                    
                    mcq_obj.save()
                    total_imported += 1
                    
                    if (idx + 1) % 50 == 0:
                        self.stdout.write(f'  Imported {idx + 1}/{len(mcqs)}...')
                        
                except Exception as e:
                    errors.append(f'Error in MCQ {idx}: {str(e)}')
        
        # Summary
        self.stdout.write(self.style.SUCCESS(f'\nImport complete: {total_imported} MCQs imported'))
        
        if errors:
            self.stdout.write(self.style.ERROR(f'{len(errors)} errors occurred:'))
            for error in errors[:10]:
                self.stdout.write(f'  - {error}')