#!/usr/bin/env python3
"""Import MCQs from RERE files with correct answer extraction and subspecialty mapping."""
import os
import sys
import json
import re
import glob
from datetime import datetime

# Django setup
sys.path.append('/app/django_neurology_mcq')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
import django
django.setup()

from mcq.models import MCQ
from django.db import transaction

# Subspecialty mapping to match Heroku database
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
    'vascular_neurology': 'Vascular Neurology/Stroke'
}

class REREImporter:
    def __init__(self, source_dir):
        self.source_dir = source_dir
        self.stats = {
            'total_files': 0,
            'total_mcqs': 0,
            'imported': 0,
            'errors': 0,
            'correct_found': 0,
            'correct_not_found': 0,
            'by_specialty': {}
        }
        self.error_log = []
    
    def extract_correct_answer(self, option_analysis_text):
        """Extract the correct answer letter from option_analysis section."""
        if not option_analysis_text:
            return None
            
        # Handle different data types
        if isinstance(option_analysis_text, dict):
            return None
            
        lines = option_analysis_text.split('\n') if '\n' in option_analysis_text else [option_analysis_text]
        
        for line in lines:
            # Multiple patterns to match correct answers
            patterns = [
                r'Option\s+([A-Z]):\s*.*?[–—-]\s*(?:Correct|CORRECT)[\.\s]',
                r'Option\s+([A-Z])\s*.*?\((?:Correct|CORRECT)\)',
                r'Option\s+([A-Z]):\s*(?:Correct|CORRECT)[\.\s]',
                r'Option\s+([A-Z])\s*[–—-]\s*(?:Correct|CORRECT)',
                r'Option\s+([A-Z]):.*?[-–—]\s*(?:Correct|CORRECT)',
                r'Option\s+([A-Z]).*?(?:is|appears)\s+(?:correct|best)',
            ]
            
            for pattern in patterns:
                match = re.search(pattern, line, re.IGNORECASE)
                if match:
                    return match.group(1).upper()
        
        return None
    
    def map_subspecialty(self, specialty, primary_category):
        """Map specialty to proper subspecialty name for Heroku."""
        # First try primary_category
        if primary_category:
            # Direct mapping for known categories
            if primary_category in SUBSPECIALTY_MAPPING.values():
                return primary_category
            # Try to map from file-based naming
            key = primary_category.lower().replace(' ', '_').replace('/', '_')
            if key in SUBSPECIALTY_MAPPING:
                return SUBSPECIALTY_MAPPING[key]
        
        # Fallback to specialty
        specialty_key = specialty.lower().replace(' ', '_').replace('/', '_')
        return SUBSPECIALTY_MAPPING.get(specialty_key, 'Other/Unclassified')
    
    def import_all_files(self):
        """Import all JSON files from RERE directory."""
        json_files = glob.glob(os.path.join(self.source_dir, '*.json'))
        self.stats['total_files'] = len(json_files)
        
        print(f"Starting import at {datetime.now()}")
        print(f"Found {len(json_files)} specialty files to import")
        
        for file_path in sorted(json_files):
            self.import_file(file_path)
        
        self.print_summary()
    
    def import_file(self, file_path):
        """Import a single specialty file."""
        filename = os.path.basename(file_path)
        print(f"\n{'='*50}")
        print(f"Importing {filename}")
        
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
            
            specialty = data.get('specialty', 'unknown')
            mcqs = data.get('mcqs', [])
            
            self.stats['by_specialty'][specialty] = {
                'total': len(mcqs),
                'imported': 0,
                'errors': 0
            }
            
            print(f"Specialty: {specialty}")
            print(f"MCQs to process: {len(mcqs)}")
            
            # Process MCQs in batches
            batch_size = 25
            for i in range(0, len(mcqs), batch_size):
                batch = mcqs[i:i+batch_size]
                print(f"  Processing batch {i//batch_size + 1} ({i+1}-{min(i+batch_size, len(mcqs))} of {len(mcqs)})")
                self.import_batch(batch, specialty, filename)
            
            specialty_stats = self.stats['by_specialty'][specialty]
            print(f"✓ Completed {filename}: {specialty_stats['imported']}/{specialty_stats['total']} imported")
            
        except Exception as e:
            error_msg = f"ERROR in {filename}: {str(e)}"
            print(error_msg)
            self.error_log.append(error_msg)
            self.stats['errors'] += 1
    
    def import_batch(self, batch, specialty, source_file):
        """Import a batch of MCQs."""
        with transaction.atomic():
            for mcq_data in batch:
                question_num = mcq_data.get('question_number', 'Unknown')
                try:
                    # Extract correct answer from option_analysis
                    exp_sections = mcq_data.get('explanation_sections', {})
                    option_analysis = exp_sections.get('option_analysis', '')
                    
                    correct_answer = self.extract_correct_answer(option_analysis)
                    
                    if correct_answer:
                        self.stats['correct_found'] += 1
                    else:
                        self.stats['correct_not_found'] += 1
                        # Fallback to verified_answer if no correct answer found
                        correct_answer = mcq_data.get('verified_answer') or mcq_data.get('correct_answer')
                    
                    # Map subspecialty
                    primary_category = mcq_data.get('primary_category')
                    subspecialty = self.map_subspecialty(specialty, primary_category)
                    
                    mcq = self.create_mcq_object(mcq_data, subspecialty, source_file, correct_answer)
                    mcq.save()
                    
                    self.stats['imported'] += 1
                    self.stats['by_specialty'][specialty]['imported'] += 1
                    
                except Exception as e:
                    error_msg = f"    Error in Q{question_num}: {str(e)}"
                    print(error_msg)
                    self.error_log.append(error_msg)
                    self.stats['errors'] += 1
                    self.stats['by_specialty'][specialty]['errors'] += 1
    
    def create_mcq_object(self, data, subspecialty, source_file, correct_answer):
        """Create MCQ object from RERE data."""
        # Convert options format
        options_dict = {}
        for option in data.get('options', []):
            letter = option.get('letter', '')
            text = option.get('text', '')
            if letter and text:
                options_dict[letter] = text
        
        # Create MCQ object with all fields
        mcq = MCQ(
            question_number=data.get('question_number'),
            question_text=data.get('question_text'),
            options=options_dict,
            correct_answer=correct_answer,
            
            # Use mapped subspecialty
            subspecialty=subspecialty,
            source_file=source_file,
            exam_type=data.get('exam_type', 'Other'),
            exam_year=data.get('exam_year'),
            
            # Explanation - traditional field
            explanation=self.format_traditional_explanation(data),
            
            # Structured explanations - PRESERVE ALL SUBSECTIONS
            explanation_sections=data.get('explanation_sections'),
            
            # Verification fields
            verification_confidence=data.get('verification_confidence'),
            
            # Categories
            primary_category=data.get('primary_category'),
            secondary_category=data.get('secondary_category'),
            key_concept=data.get('key_concept'),
            difficulty_level=data.get('difficulty_level'),
            
            # Image
            image_url=data.get('source_image') if data.get('has_image') else None
        )
        
        return mcq
    
    def format_traditional_explanation(self, data):
        """Format a traditional explanation from various fields."""
        parts = []
        
        # Add key concept
        if data.get('key_concept'):
            parts.append(f"**Key Concept:** {data['key_concept']}")
            parts.append("")
        
        # Add clinical scenario
        if data.get('clinical_scenario'):
            parts.append("**Clinical Scenario:**")
            parts.append(data['clinical_scenario'])
            parts.append("")
        
        # Add keywords
        if data.get('keywords'):
            parts.append(f"**Keywords:** {', '.join(data['keywords'])}")
        
        return '\n'.join(parts) if parts else None
    
    def print_summary(self):
        """Print import summary."""
        print("\n" + "="*60)
        print("IMPORT SUMMARY")
        print("="*60)
        print(f"Completed at: {datetime.now()}")
        print(f"Total files processed: {self.stats['total_files']}")
        print(f"Total MCQs imported: {self.stats['imported']}")
        print(f"Total errors: {self.stats['errors']}")
        print(f"Correct answers extracted: {self.stats['correct_found']}")
        print(f"Fallback to verified_answer: {self.stats['correct_not_found']}")
        
        print("\nBreakdown by Specialty:")
        print(f"{'Specialty':<25} {'Total':<8} {'Imported':<10} {'Errors':<8}")
        print("-" * 55)
        
        for specialty in sorted(self.stats['by_specialty'].keys()):
            spec_stats = self.stats['by_specialty'][specialty]
            print(f"{specialty:<25} {spec_stats['total']:<8} {spec_stats['imported']:<10} {spec_stats['errors']:<8}")
        
        if self.error_log:
            print("\nError Summary (first 10):")
            for error in self.error_log[:10]:
                print(error)

# Usage
if __name__ == "__main__":
    # Path for Heroku or local testing
    if len(sys.argv) > 1:
        source_dir = sys.argv[1]
    else:
        source_dir = "/app/rere_mcqs"
    
    importer = REREImporter(source_dir)
    importer.import_all_files()