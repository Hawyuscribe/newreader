from django.core.management.base import BaseCommand
from mcq.models import MCQ
import json


class Command(BaseCommand):
    help = 'Check for explanation sections in MCQs'

    def handle(self, *args, **options):
        all_mcqs = MCQ.objects.all()
        total_count = all_mcqs.count()
        
        # Track different explanation scenarios
        no_explanation_field = []
        none_explanations = []
        empty_explanations = []
        string_explanations = []
        dict_explanations = []
        complete_sections = []
        partial_sections = []
        invalid_json = []
        
        # Expected sections
        expected_sections = [
            'concept_explanation',
            'question_breakdown', 
            'option_analysis',
            'key_points',
            'additional_context'
        ]
        
        for mcq in all_mcqs:
            # Check if explanation_sections field exists
            if not hasattr(mcq, 'explanation_sections'):
                no_explanation_field.append(mcq)
                continue
                
            # Check if it's None
            if mcq.explanation_sections is None:
                none_explanations.append(mcq)
                continue
                
            # Check if it's empty
            if isinstance(mcq.explanation_sections, (str, dict)) and not mcq.explanation_sections:
                empty_explanations.append(mcq)
                continue
                
            # Handle string type (might be JSON)
            if isinstance(mcq.explanation_sections, str):
                string_explanations.append(mcq)
                try:
                    # Try to parse as JSON
                    sections = json.loads(mcq.explanation_sections)
                    if isinstance(sections, dict):
                        # Check which sections exist
                        existing_sections = [s for s in expected_sections if s in sections]
                        if len(existing_sections) == len(expected_sections):
                            complete_sections.append(mcq)
                        else:
                            partial_sections.append(mcq)
                except json.JSONDecodeError:
                    invalid_json.append(mcq)
                    
            # Handle dict type
            elif isinstance(mcq.explanation_sections, dict):
                dict_explanations.append(mcq)
                sections = mcq.explanation_sections
                existing_sections = [s for s in expected_sections if s in sections]
                if len(existing_sections) == len(expected_sections):
                    complete_sections.append(mcq)
                else:
                    partial_sections.append(mcq)
        
        # Summary report
        self.stdout.write(self.style.NOTICE('=== MCQ Explanation Sections Analysis ==='))
        self.stdout.write(f'Total MCQs: {total_count}')
        self.stdout.write('')
        
        self.stdout.write(self.style.WARNING('Field Status:'))
        self.stdout.write(f'No explanation_sections field: {len(no_explanation_field)}')
        self.stdout.write(f'explanation_sections is None: {len(none_explanations)}')
        self.stdout.write(f'Empty explanation_sections: {len(empty_explanations)}')
        self.stdout.write('')
        
        self.stdout.write(self.style.WARNING('Data Types:'))
        self.stdout.write(f'String type: {len(string_explanations)}')
        self.stdout.write(f'Dict type: {len(dict_explanations)}')
        self.stdout.write(f'Invalid JSON: {len(invalid_json)}')
        self.stdout.write('')
        
        self.stdout.write(self.style.SUCCESS('Section Completeness:'))
        self.stdout.write(f'Complete sections (all 5): {len(complete_sections)}')
        self.stdout.write(f'Partial sections: {len(partial_sections)}')
        
        total_with_explanations = len(complete_sections) + len(partial_sections)
        percentage_with_explanations = (total_with_explanations / total_count * 100) if total_count > 0 else 0
        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS(f'Total MCQs with explanation sections: {total_with_explanations} ({percentage_with_explanations:.1f}%)'))
        
        # Sample analysis
        if partial_sections:
            self.stdout.write('')
            self.stdout.write(self.style.WARNING('Sample partial sections analysis:'))
            for i, mcq in enumerate(partial_sections[:3]):
                self.stdout.write(f'\nMCQ ID: {mcq.id}')
                self.stdout.write(f'Question: {mcq.question_text[:100]}...')
                if isinstance(mcq.explanation_sections, str):
                    try:
                        sections = json.loads(mcq.explanation_sections)
                    except:
                        continue
                else:
                    sections = mcq.explanation_sections
                    
                if isinstance(sections, dict):
                    present = [s for s in expected_sections if s in sections]
                    missing = [s for s in expected_sections if s not in sections]
                    self.stdout.write(f'Present sections: {", ".join(present)}')
                    self.stdout.write(f'Missing sections: {", ".join(missing)}')
                    
        # Sample complete section
        if complete_sections:
            self.stdout.write('')
            self.stdout.write(self.style.SUCCESS('Sample complete explanation sections:'))
            sample = complete_sections[0]
            self.stdout.write(f'\nMCQ ID: {sample.id}')
            self.stdout.write(f'Question: {sample.question_text[:100]}...')
            
            if isinstance(sample.explanation_sections, str):
                try:
                    sections = json.loads(sample.explanation_sections)
                except:
                    sections = {}
            else:
                sections = sample.explanation_sections
                
            if isinstance(sections, dict):
                for section, content in sections.items():
                    if section in expected_sections:
                        self.stdout.write(f'\n{section}: {str(content)[:200]}...')
                        
        # Sample MCQs without any explanations
        no_explanations = no_explanation_field + none_explanations + empty_explanations
        if no_explanations:
            self.stdout.write('')
            self.stdout.write(self.style.ERROR('Sample MCQs without explanations:'))
            for mcq in no_explanations[:5]:
                self.stdout.write(f'ID: {mcq.id}, Question: {mcq.question_text[:100]}...')
                
        # Check for specific section content
        if partial_sections or complete_sections:
            self.stdout.write('')
            self.stdout.write(self.style.NOTICE('=== Section Content Analysis ==='))
            section_counts = {section: 0 for section in expected_sections}
            
            for mcq in partial_sections + complete_sections:
                if isinstance(mcq.explanation_sections, str):
                    try:
                        sections = json.loads(mcq.explanation_sections)
                    except:
                        continue
                else:
                    sections = mcq.explanation_sections
                    
                if isinstance(sections, dict):
                    for section in expected_sections:
                        if section in sections:
                            section_counts[section] += 1
                            
            for section, count in section_counts.items():
                percentage = (count / total_count * 100) if total_count > 0 else 0
                self.stdout.write(f'{section}: {count} MCQs ({percentage:.1f}%)')