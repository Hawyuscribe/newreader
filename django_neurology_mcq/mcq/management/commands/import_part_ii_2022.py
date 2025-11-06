"""
Django management command to import MCQs from Part II 2022 JSON files.
This command extracts correct answers from option_analysis and handles existing MCQ model fields.
"""
import json
import re
from pathlib import Path
from django.core.management.base import BaseCommand
from django.db import transaction
from mcq.models import MCQ


class Command(BaseCommand):
    help = 'Import MCQs from Part II 2022 JSON files with proper subspecialty mapping'
    
    # Fixed subspecialty mapping
    SUBSPECIALTY_MAPPING = {
        'anatomy': 'Neuroanatomy',
        'critical_care_neurology': 'Critical Care Neurology',
        'critical care neurology': 'Critical Care Neurology',
        'dementia': 'Dementia',
        'epilepsy': 'Epilepsy',
        'headache': 'Headache',
        'movement_disorders': 'Movement Disorders',
        'movement disorders': 'Movement Disorders',
        'neuro-otology': 'Neuro-otology',
        'neuro otology': 'Neuro-otology',
        'neurogenetics': 'Neurogenetics',
        'neuroimmunology': 'Neuroimmunology',
        'neuroinfectious': 'Neuro-infectious',
        'neuroinfectious diseases': 'Neuro-infectious',
        'neuromuscular': 'Neuromuscular',
        'neurooncology': 'Neuro-oncology',
        'neuro-oncology': 'Neuro-oncology',
        'neuroophthalmology': 'Neuroophthalmology',
        'neuropsychiatry': 'Neuropsychiatry',
        'neurotoxicology': 'Neurotoxicology',
        'other': 'Other/Unclassified',
        'pediatric_neurology': 'Pediatric Neurology',
        'pediatric neurology': 'Pediatric Neurology',
        'sleep_neurology': 'Sleep Neurology',
        'sleep neurology': 'Sleep Neurology',
        'vascular_neurology': 'Vascular Neurology/Stroke',
        'vascular neurology': 'Vascular Neurology/Stroke',
        'vascular neurology/stroke': 'Vascular Neurology/Stroke',
        'cerebrovascular/stroke': 'Vascular Neurology/Stroke',
        'stroke': 'Vascular Neurology/Stroke',
        'vascular neurology / stroke': 'Vascular Neurology/Stroke',
        'neuroimmunology/autoimmune neurology': 'Neuroimmunology',
        'demyelinating/multiple sclerosis': 'Neuroimmunology',
        'demyelinating diseases': 'Neuroimmunology',
    }
    
    def add_arguments(self, parser):
        parser.add_argument('file', help='File path to JSON data')
        parser.add_argument('--batch-size', type=int, default=25, help='Batch size for import')
        parser.add_argument('--clear', action='store_true', help='Clear all existing MCQs before importing')
    
    def handle(self, *args, **options):
        batch_size = options['batch_size']
        
        if options['clear']:
            self.stdout.write('Clearing all existing MCQs...')
            MCQ.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('All MCQs cleared'))
        
        self.import_from_file(options['file'], batch_size)
        
        # Final verification
        total_count = MCQ.objects.count()
        self.stdout.write(self.style.SUCCESS(f'\nTotal MCQs in database: {total_count}'))
    
    def import_from_file(self, filepath, batch_size):
        self.stdout.write(f'Loading data from file: {filepath}')
        with open(filepath, 'r') as f:
            data = json.load(f)
        self.import_data(data, batch_size)
    
    def import_data(self, data, batch_size):
        # Extract specialty from data or use Part II 2022 default
        specialty = data.get('specialty', 'Part II 2022')
        mcqs = data.get('mcqs', [])
        
        self.stdout.write(f'Specialty: {specialty}')
        self.stdout.write(f'MCQs to import: {len(mcqs)}')
        
        # Import statistics
        imported = 0
        errors = 0
        correct_found = 0
        error_details = []
        
        # Process in batches
        for i in range(0, len(mcqs), batch_size):
            batch = mcqs[i:i+batch_size]
            batch_end = min(i + batch_size, len(mcqs))
            self.stdout.write(f'Processing batch {i+1}-{batch_end}...')
            
            with transaction.atomic():
                for mcq_data in batch:
                    question_num = mcq_data.get('question_number', 'Unknown')
                    try:
                        # Extract correct answer from option_analysis
                        exp_sections = mcq_data.get('explanation_sections', {})
                        option_analysis = exp_sections.get('option_analysis', '')
                        
                        # Handle dict type option_analysis
                        if isinstance(option_analysis, dict):
                            option_analysis = ' '.join(str(v) for v in option_analysis.values() if v)
                        
                        correct_answer = self.extract_correct_answer(option_analysis)
                        
                        if correct_answer:
                            correct_found += 1
                        else:
                            # Fallback to verified_answer or correct_answer
                            correct_answer = mcq_data.get('verified_answer', mcq_data.get('correct_answer', 'B'))
                        
                        # Handle long answers - truncate if necessary
                        if len(correct_answer) > 5:
                            correct_answer = correct_answer[:5]
                        
                        # Map subspecialty
                        subspecialty = self.map_subspecialty(specialty, mcq_data.get('primary_category'))
                        
                        # Convert options format
                        options_dict = self.convert_options(mcq_data.get('options', []))
                        
                        # Prepare MCQ fields - only include fields that exist in the model
                        mcq_fields = {
                            'question_number': question_num,
                            'question_text': mcq_data.get('question_text', ''),
                            'options': options_dict,
                            'correct_answer': correct_answer,
                            'subspecialty': subspecialty,
                            'source_file': f"Part II 2022_mcqs_20250514_203145.json",
                            'exam_type': 'Part II',
                            'exam_year': 2022,
                            'explanation': mcq_data.get('explanation', mcq_data.get('answer_explanation', '')),
                            'explanation_sections': exp_sections,
                            'verification_confidence': mcq_data.get('verification_confidence'),
                            'primary_category': mcq_data.get('primary_category'),
                            'secondary_category': mcq_data.get('secondary_category'),
                            'key_concept': mcq_data.get('key_concept'),
                            'difficulty_level': mcq_data.get('difficulty_level'),
                            'image_url': mcq_data.get('source_image') if mcq_data.get('has_image') else None
                        }
                        
                        # Create MCQ
                        MCQ.objects.create(**mcq_fields)
                        imported += 1
                        
                    except Exception as e:
                        errors += 1
                        error_details.append(f"Q{question_num}: {str(e)[:100]}")
                        self.stdout.write(self.style.ERROR(f"Error on Q{question_num}: {str(e)[:100]}"))
        
        # Print summary
        self.stdout.write(self.style.SUCCESS(
            f'\nImport completed: {imported} imported, {errors} errors'
        ))
        if imported > 0:
            self.stdout.write(f'Correct answers found: {correct_found}/{imported} ({correct_found/imported*100:.1f}%)')
        
        if error_details:
            self.stdout.write(self.style.ERROR('\nError details:'))
            for error in error_details[:5]:
                self.stdout.write(self.style.ERROR(f'  {error}'))
            if len(error_details) > 5:
                self.stdout.write(f'  ... and {len(error_details) - 5} more errors')
    
    def extract_correct_answer(self, option_analysis):
        """Extract correct answer from option_analysis text."""
        if not option_analysis:
            return None
        
        patterns = [
            r'Option\s+([A-Z]):\s*.*?[–—-]\s*(?:Correct|CORRECT)',
            r'Option\s+([A-Z])\s*.*?\((?:Correct|CORRECT)\)',
            r'Option\s+([A-Z]):\s*(?:Correct|CORRECT)',
            r'Option\s+([A-Z]).*?(?:is|appears)\s+(?:correct|best)',
            r'Option\s+([A-Z])[:\s]+[^.]*?(?:—|–)\s*(?:Correct|CORRECT)',
            r'([A-Z])\.\s*.*?[–—-]\s*(?:Correct|CORRECT)',
            r'([A-Z])\)\s*.*?[–—-]\s*(?:Correct|CORRECT)',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, option_analysis, re.IGNORECASE | re.MULTILINE | re.DOTALL)
            if match:
                return match.group(1).upper()
        
        return None
    
    def map_subspecialty(self, specialty, primary_category):
        """Map specialty to proper subspecialty name."""
        # Clean the input
        if primary_category:
            # Try primary_category first
            category_clean = primary_category.lower().replace('_', ' ').strip()
            
            # Remove trailing /something
            if '/' in category_clean:
                variants = [
                    category_clean,  # full name
                    category_clean.split('/')[0].strip(),  # first part
                    category_clean.replace('/', ' ').strip()  # spaces instead of slashes
                ]
                
                for variant in variants:
                    if variant in self.SUBSPECIALTY_MAPPING:
                        return self.SUBSPECIALTY_MAPPING[variant]
                    # Try with underscores
                    variant_underscore = variant.replace(' ', '_')
                    if variant_underscore in self.SUBSPECIALTY_MAPPING:
                        return self.SUBSPECIALTY_MAPPING[variant_underscore]
            else:
                # Direct mapping
                if category_clean in self.SUBSPECIALTY_MAPPING:
                    return self.SUBSPECIALTY_MAPPING[category_clean]
                # Try with underscores
                category_underscore = category_clean.replace(' ', '_')
                if category_underscore in self.SUBSPECIALTY_MAPPING:
                    return self.SUBSPECIALTY_MAPPING[category_underscore]
        
        # Default to Other/Unclassified
        return 'Other/Unclassified'
    
    def convert_options(self, options):
        """Convert options to dictionary format."""
        if isinstance(options, dict):
            return options
        
        options_dict = {}
        for i, option in enumerate(options):
            if isinstance(option, dict):
                letter = option.get('letter', chr(65 + i))
                text = option.get('text', '')
                options_dict[letter] = text
            elif isinstance(option, str):
                letter = chr(65 + i)
                options_dict[letter] = option
        
        return options_dict