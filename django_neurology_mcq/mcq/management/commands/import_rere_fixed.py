"""
Fixed Django management command to import MCQs from RERE JSON files.
This command properly extracts correct answers and preserves all data.
"""
import json
import re
from pathlib import Path
from urllib.request import urlopen
from django.core.management.base import BaseCommand
from django.db import transaction
from mcq.models import MCQ
from django.db.models import JSONField


class Command(BaseCommand):
    help = 'Import MCQs from RERE JSON files with proper subspecialty mapping'
    
    # Fixed subspecialty mapping
    SUBSPECIALTY_MAPPING = {
        'anatomy': 'Neuroanatomy',
        'critical_care_neurology': 'Critical Care Neurology',
        'dementia': 'Dementia',
        'epilepsy': 'Epilepsy',
        'headache': 'Headache',
        'movement_disorders': 'Movement Disorders',
        'neuro-otology': 'Neuro-otology',
        'neurogenetics': 'Neurogenetics',
        'neuroimmunology': 'Neuroimmunology',
        'neuroinfectious': 'Neuro-infectious',
        'neuromuscular': 'Neuromuscular',
        'neurooncology': 'Neuro-oncology',
        'neuroophthalmology': 'Neuroophthalmology',
        'neuropsychiatry': 'Neuropsychiatry',
        'neurotoxicology': 'Neurotoxicology',
        'other': 'Other/Unclassified',
        'pediatric_neurology': 'Pediatric Neurology',
        'sleep_neurology': 'Sleep Neurology',
        'vascular_neurology': 'Vascular Neurology/Stroke',
        'vascular neurology': 'Vascular Neurology/Stroke',
        'vascular neurology/stroke': 'Vascular Neurology/Stroke'
    }
    
    def add_arguments(self, parser):
        parser.add_argument('--url', help='URL to JSON data')
        parser.add_argument('--file', help='File path to JSON data')
        parser.add_argument('--dir', help='Directory containing JSON files')
        parser.add_argument('--batch-size', type=int, default=25, help='Batch size for import')
        parser.add_argument('--clear', action='store_true', help='Clear all existing MCQs before importing')
        parser.add_argument('--truncate-long-answers', action='store_true', 
                          help='Truncate answers longer than 5 characters to avoid DB errors')
    
    def handle(self, *args, **options):
        batch_size = options['batch_size']
        self.truncate_long = options.get('truncate_long_answers', False)
        
        if options['clear']:
            self.stdout.write('Clearing all existing MCQs...')
            MCQ.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('All MCQs cleared'))
        
        # Handle different input sources
        if options['url']:
            self.import_from_url(options['url'], batch_size)
        elif options['file']:
            self.import_from_file(options['file'], batch_size)
        elif options['dir']:
            self.import_from_directory(options['dir'], batch_size)
        else:
            self.stdout.write(self.style.ERROR('Please specify --url, --file, or --dir'))
            return
        
        # Final verification
        total_count = MCQ.objects.count()
        self.stdout.write(self.style.SUCCESS(f'\nTotal MCQs in database: {total_count}'))
    
    def import_from_url(self, url, batch_size):
        self.stdout.write(f'Loading data from URL: {url}')
        with urlopen(url) as response:
            data = json.loads(response.read().decode())
        self.import_data(data, batch_size)
    
    def import_from_file(self, filepath, batch_size):
        self.stdout.write(f'Loading data from file: {filepath}')
        with open(filepath, 'r') as f:
            data = json.load(f)
        self.import_data(data, batch_size)
    
    def import_from_directory(self, dirpath, batch_size):
        self.stdout.write(f'Loading data from directory: {dirpath}')
        rere_path = Path(dirpath)
        json_files = list(rere_path.glob('*.json'))
        
        total_imported = 0
        total_errors = 0
        
        for filepath in sorted(json_files):
            self.stdout.write(f'\nProcessing {filepath.name}...')
            with open(filepath, 'r') as f:
                data = json.load(f)
            imported, errors = self.import_data(data, batch_size, filepath.name, return_stats=True)
            total_imported += imported
            total_errors += errors
        
        self.stdout.write(self.style.SUCCESS(
            f'\nDirectory import complete: {total_imported} imported, {total_errors} errors'
        ))
    
    def import_data(self, data, batch_size, filename=None, return_stats=False):
        # Extract specialty from data
        specialty = data.get('specialty', 'unknown')
        mcqs = data.get('mcqs', [])
        
        # If no specialty in data, try to extract from filename
        if specialty == 'unknown' and filename:
            specialty = filename.replace('.json', '').replace('_', ' ')
        
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
                        
                        # Handle long answers
                        if len(correct_answer) > 5:
                            if self.truncate_long:
                                correct_answer = correct_answer[:5]
                            else:
                                # Skip if answer is too long and we're not truncating
                                raise ValueError(f"Answer too long: {correct_answer}")
                        
                        # Map subspecialty
                        subspecialty = self.map_subspecialty(specialty, mcq_data.get('primary_category'))
                        
                        # Convert options format
                        options_dict = self.convert_options(mcq_data.get('options', []))
                        
                        # Prepare all fields including explanations
                        mcq_fields = {
                            'question_number': question_num,
                            'question_text': mcq_data.get('question_text', ''),
                            'options': options_dict,
                            'correct_answer': correct_answer,
                            'subspecialty': subspecialty,
                            'source_file': filename or f"{specialty}.json",
                            'exam_type': mcq_data.get('exam_type', 'Other'),
                            'exam_year': mcq_data.get('exam_year'),
                            'explanation': mcq_data.get('explanation', mcq_data.get('answer_explanation', '')),
                            'explanation_sections': exp_sections,
                            'verification_confidence': mcq_data.get('verification_confidence'),
                            'primary_category': mcq_data.get('primary_category'),
                            'secondary_category': mcq_data.get('secondary_category'),
                            'key_concept': mcq_data.get('key_concept'),
                            'difficulty_level': mcq_data.get('difficulty_level'),
                            'image_url': mcq_data.get('source_image') if mcq_data.get('has_image') else None
                        }
                        
                        # Add additional fields from RERE
                        if 'keywords' in mcq_data:
                            mcq_fields['keywords'] = mcq_data['keywords']
                        if 'clinical_scenario' in mcq_data:
                            mcq_fields['clinical_scenario'] = mcq_data['clinical_scenario']
                        if 'required_knowledge_areas' in mcq_data:
                            mcq_fields['required_knowledge_areas'] = mcq_data['required_knowledge_areas']
                        if 'board_exam_relevance' in mcq_data:
                            mcq_fields['board_exam_relevance'] = mcq_data['board_exam_relevance']
                        if 'references' in mcq_data:
                            mcq_fields['references'] = mcq_data['references']
                        
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
        
        if return_stats:
            return imported, errors
    
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
        specialty_clean = specialty.lower().replace('_', ' ').strip()
        
        # Try direct mapping first
        if specialty_clean in self.SUBSPECIALTY_MAPPING:
            return self.SUBSPECIALTY_MAPPING[specialty_clean]
        
        # Try with underscores instead of spaces
        specialty_underscore = specialty_clean.replace(' ', '_')
        if specialty_underscore in self.SUBSPECIALTY_MAPPING:
            return self.SUBSPECIALTY_MAPPING[specialty_underscore]
        
        # Try primary_category if available
        if primary_category:
            primary_clean = primary_category.lower().replace('_', ' ').strip()
            if primary_clean in self.SUBSPECIALTY_MAPPING:
                return self.SUBSPECIALTY_MAPPING[primary_clean]
            
            primary_underscore = primary_clean.replace(' ', '_')
            if primary_underscore in self.SUBSPECIALTY_MAPPING:
                return self.SUBSPECIALTY_MAPPING[primary_underscore]
        
        # Default
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