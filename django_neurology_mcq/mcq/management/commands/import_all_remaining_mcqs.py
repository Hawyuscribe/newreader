from django.core.management.base import BaseCommand
from django.db import transaction
from mcq.models import MCQ
import json
import os
from collections import defaultdict

class Command(BaseCommand):
    help = 'Import all remaining MCQs from consolidated_mcqs directory'

    def handle(self, *args, **options):
        self.stdout.write("Importing all remaining MCQs...")
        
        # Get existing MCQ question texts to avoid duplicates
        existing_questions = set(MCQ.objects.values_list('question_text', flat=True))
        self.stdout.write(f"Found {len(existing_questions)} existing MCQs in database")
        
        # Load all MCQs from consolidated directory
        consolidated_dir = '/Users/tariqalmatrudi/NEWreader/consolidated_mcqs'
        
        all_mcqs = []
        stats = defaultdict(int)
        
        for filename in sorted(os.listdir(consolidated_dir)):
            if filename.endswith('.json') and not filename.startswith('.'):
                filepath = os.path.join(consolidated_dir, filename)
                with open(filepath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    mcqs = data.get('mcqs', [])
                    self.stdout.write(f"Loading {len(mcqs)} MCQs from {filename}")
                    all_mcqs.extend(mcqs)
                    stats['total_loaded'] += len(mcqs)
        
        self.stdout.write(f"\nTotal MCQs loaded from files: {stats['total_loaded']}")
        
        # Process MCQs
        created_count = 0
        skipped_count = 0
        error_count = 0
        
        with transaction.atomic():
            for idx, mcq_data in enumerate(all_mcqs):
                # Skip if already exists
                if mcq_data.get('question_text') in existing_questions:
                    skipped_count += 1
                    continue
                
                try:
                    # Clean correct_answer field
                    correct_answer = str(mcq_data.get('correct_answer', '')).strip()
                    if correct_answer.lower().startswith('option '):
                        correct_answer = correct_answer.replace('Option ', '').replace('option ', '').strip()
                    correct_answer = correct_answer[:5]  # Ensure max 5 chars
                    
                    # Handle options
                    options = mcq_data.get('options', {})
                    if isinstance(options, list):
                        # Convert list to dict
                        options_dict = {}
                        for opt in options:
                            if isinstance(opt, dict) and 'letter' in opt and 'text' in opt:
                                options_dict[opt['letter'].upper()] = opt['text']
                        options = options_dict
                    
                    # Handle explanation sections
                    explanation_sections = mcq_data.get('explanation_sections', {})
                    
                    # Map common variations to standard keys
                    if 'option_analysis' in mcq_data and mcq_data['option_analysis']:
                        explanation_sections['option_analysis'] = mcq_data['option_analysis']
                    
                    # Standardize section keys
                    standardized_sections = {}
                    key_mappings = {
                        'conceptual_foundation': ['conceptual foundation', 'Conceptual Foundation'],
                        'pathophysiological_mechanisms': ['pathophysiology', 'Pathophysiology', 'pathophysiological mechanisms'],
                        'clinical_correlation': ['clinical correlation', 'Clinical Correlation', 'clinical context'],
                        'classification_and_nosology': ['classification and neurology', 'classification and nosology'],
                        'diagnostic_approach': ['diagnostic approach', 'Diagnostic Approach'],
                        'management_principles': ['management principles', 'Management Principles'],
                        'option_analysis': ['option analysis', 'Option Analysis', 'options analysis'],
                        'clinical_pearls': ['clinical pearls', 'Clinical Pearls', 'key insight'],
                        'current_evidence': ['current evidence', 'Current Evidence', 'quick reference']
                    }
                    
                    for standard_key, variations in key_mappings.items():
                        # Check if standard key exists
                        if standard_key in explanation_sections:
                            standardized_sections[standard_key] = explanation_sections[standard_key]
                        else:
                            # Check variations
                            for var in variations:
                                if var in explanation_sections:
                                    standardized_sections[standard_key] = explanation_sections[var]
                                    break
                    
                    # Copy any other keys
                    for key, value in explanation_sections.items():
                        if key not in standardized_sections and value:
                            standardized_sections[key] = value
                    
                    # Create MCQ
                    mcq = MCQ(
                        question_text=mcq_data['question_text'],
                        options=options,
                        correct_answer=correct_answer,
                        explanation=mcq_data.get('explanation', ''),
                        explanation_sections=standardized_sections,
                        subspecialty=mcq_data.get('subspecialty', 'Other/Unclassified'),
                        exam_type=mcq_data.get('exam_type', ''),
                        exam_year=mcq_data.get('exam_year', ''),
                        question_number=mcq_data.get('question_number', ''),
                        source_file=mcq_data.get('source_file', ''),
                        image_url=mcq_data.get('image_url', ''),
                        correct_answer_text=mcq_data.get('correct_answer_text', '')
                    )
                    mcq.save()
                    created_count += 1
                    
                    if created_count % 100 == 0:
                        self.stdout.write(f"Progress: {created_count} MCQs imported...")
                        
                except Exception as e:
                    error_count += 1
                    self.stdout.write(
                        self.style.ERROR(
                            f"Error importing MCQ {idx + 1}: {str(e)}\n"
                            f"Question: {mcq_data.get('question_text', '')[:100]}..."
                        )
                    )
        
        # Final stats
        self.stdout.write(self.style.SUCCESS(f"\nImport completed!"))
        self.stdout.write(f"Total MCQs in files: {stats['total_loaded']}")
        self.stdout.write(f"Already in database: {skipped_count}")
        self.stdout.write(f"Successfully imported: {created_count}")
        self.stdout.write(f"Errors: {error_count}")
        self.stdout.write(f"Total MCQs now in database: {MCQ.objects.count()}")