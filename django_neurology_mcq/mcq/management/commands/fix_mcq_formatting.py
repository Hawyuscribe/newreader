import json
from django.core.management.base import BaseCommand
from mcq.models import MCQ
from django.db import transaction

class Command(BaseCommand):
    help = 'Fix MCQ formatting issues: explanation sections and options'
    
    def add_arguments(self, parser):
        parser.add_argument('--batch-size', type=int, default=50, help='Batch size for processing')
        parser.add_argument('--dry-run', action='store_true', help='Show what would be changed without saving')
    
    def handle(self, *args, **options):
        batch_size = options['batch_size']
        dry_run = options['dry_run']
        
        # Define the correct explanation section headings
        correct_headings = [
            'option_analysis',
            'conceptual_foundation',
            'pathophysiology',
            'clinical_manifestation',
            'diagnostic_approach',
            'management_principles',
            'follow_up_guidelines',
            'clinical_pearls',
            'references'
        ]
        
        # Old headings that need to be mapped
        heading_mappings = {
            # Common variations
            'option_analysis': ['option_analysis', 'options_analysis', 'answer_analysis'],
            'conceptual_foundation': ['conceptual_foundation', 'conceptual_basis', 'foundation', 'basic_concepts'],
            'pathophysiology': ['pathophysiology', 'pathophysiological_mechanisms', 'mechanisms'],
            'clinical_manifestation': ['clinical_manifestation', 'clinical_manifestations', 'clinical_correlation', 'clinical_features'],
            'diagnostic_approach': ['diagnostic_approach', 'diagnosis', 'diagnostic_criteria', 'evaluation'],
            'management_principles': ['management_principles', 'management', 'treatment', 'treatment_principles'],
            'follow_up_guidelines': ['follow_up_guidelines', 'follow_up', 'monitoring', 'prognosis'],
            'clinical_pearls': ['clinical_pearls', 'pearls', 'key_points', 'important_points'],
            'references': ['references', 'bibliography', 'current_evidence', 'evidence']
        }
        
        total_mcqs = MCQ.objects.count()
        self.stdout.write(f"Processing {total_mcqs} MCQs...")
        
        fixed_explanations = 0
        fixed_options = 0
        errors = 0
        
        # Process MCQs in batches
        for start_idx in range(0, total_mcqs, batch_size):
            mcqs = MCQ.objects.all()[start_idx:start_idx + batch_size]
            
            with transaction.atomic():
                for mcq in mcqs:
                    try:
                        changed = False
                        
                        # Fix explanation sections
                        if mcq.explanation_sections:
                            new_sections = {}
                            explanation_fixed = False
                            
                            # Check if it's already using correct headings
                            current_keys = list(mcq.explanation_sections.keys())
                            
                            for section_key, section_content in mcq.explanation_sections.items():
                                # Find the correct heading
                                correct_heading = None
                                for correct, variations in heading_mappings.items():
                                    if section_key.lower() in [v.lower() for v in variations]:
                                        correct_heading = correct
                                        break
                                
                                if correct_heading:
                                    new_sections[correct_heading] = section_content
                                    if correct_heading != section_key:
                                        explanation_fixed = True
                                else:
                                    # Keep unknown sections as-is but log them
                                    new_sections[section_key] = section_content
                                    self.stdout.write(f"Unknown section '{section_key}' in MCQ {mcq.id}")
                            
                            if explanation_fixed:
                                mcq.explanation_sections = new_sections
                                fixed_explanations += 1
                                changed = True
                                
                                if dry_run:
                                    self.stdout.write(f"Would fix explanation sections for MCQ {mcq.id}")
                        
                        # Fix options formatting
                        if mcq.options and isinstance(mcq.options, list):
                            options_fixed = False
                            
                            # Check if options need fixing
                            for i, option in enumerate(mcq.options):
                                if isinstance(option, dict) and 'text' in option and 'letter' in option:
                                    # This is the problematic format
                                    options_fixed = True
                                    break
                            
                            if options_fixed:
                                # Convert to the correct format
                                new_options = []
                                for option in mcq.options:
                                    if isinstance(option, dict) and 'text' in option and 'letter' in option:
                                        # Convert letter to uppercase and create proper format
                                        letter = option['letter'].upper()
                                        text = option['text']
                                        new_options.append({
                                            'letter': letter,
                                            'text': text
                                        })
                                    else:
                                        # Keep as-is if it's already in correct format
                                        new_options.append(option)
                                
                                mcq.options = new_options
                                fixed_options += 1
                                changed = True
                                
                                if dry_run:
                                    self.stdout.write(f"Would fix options for MCQ {mcq.id}: {mcq.question_text[:50]}...")
                        
                        # Save changes if not dry run
                        if changed and not dry_run:
                            mcq.save()
                            
                    except Exception as e:
                        errors += 1
                        self.stdout.write(f"Error processing MCQ {mcq.id}: {str(e)}")
            
            # Progress update
            processed = min(start_idx + batch_size, total_mcqs)
            self.stdout.write(f"Processed {processed}/{total_mcqs} MCQs...")
        
        # Final report
        self.stdout.write("\n=== Formatting Fix Complete ===")
        if dry_run:
            self.stdout.write("DRY RUN - No changes were saved")
        self.stdout.write(f"Fixed explanation sections: {fixed_explanations} MCQs")
        self.stdout.write(f"Fixed options formatting: {fixed_options} MCQs")
        self.stdout.write(f"Errors: {errors}")
        
        # Show sample of fixed explanation sections
        if fixed_explanations > 0 and not dry_run:
            self.stdout.write("\nSample fixed MCQ:")
            sample_mcq = MCQ.objects.exclude(explanation_sections={}).first()
            if sample_mcq and sample_mcq.explanation_sections:
                self.stdout.write(f"MCQ {sample_mcq.id} explanation sections:")
                for heading in correct_headings:
                    if heading in sample_mcq.explanation_sections:
                        content = sample_mcq.explanation_sections[heading]
                        if len(content) > 100:
                            content = content[:100] + "..."
                        self.stdout.write(f"  {heading}: {content}")