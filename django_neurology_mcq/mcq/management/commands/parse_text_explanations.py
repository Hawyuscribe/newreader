"""
Management command to parse text explanations into structured sections
"""
import re
import json
from django.core.management.base import BaseCommand
from mcq.models import MCQ


class Command(BaseCommand):
    help = 'Parse text explanations into structured sections'

    def parse_explanation_text(self, text):
        """Parse a large explanation text into sections"""
        sections = {}
        
        # First check if it's plain text with section headers
        if not text.strip().startswith('{'):
            # Define section patterns
            section_patterns = {
                'conceptual_foundation': [
                    r'(?:^|\n)(Conceptual Foundation)\s*\n+(.*?)(?=\n\n[A-Z][^a-z]*:|$)',
                ],
                'pathophysiology': [
                    r'(?:^|\n)(Pathophysiology)\s*\n+(.*?)(?=\n\n[A-Z][^a-z]*:|$)',
                ],
                'clinical_correlation': [
                    r'(?:^|\n)(Clinical Correlation)\s*\n+(.*?)(?=\n\n[A-Z][^a-z]*:|$)',
                ],
                'diagnostic_approach': [
                    r'(?:^|\n)(Diagnostic Approach)\s*\n+(.*?)(?=\n\n[A-Z][^a-z]*:|$)',
                ],
                'classification_nosology': [
                    r'(?:^|\n)(Classification & Nosology)\s*\n+(.*?)(?=\n\n[A-Z][^a-z]*:|$)',
                ],
                'management_principles': [
                    r'(?:^|\n)(Management Principles)\s*\n+(.*?)(?=\n\n[A-Z][^a-z]*:|$)',
                ],
                'option_analysis': [
                    r'(?:^|\n)(Option Analysis)\s*\n+(.*?)(?=\n\n[A-Z][^a-z]*:|$)',
                ],
                'clinical_pearls': [
                    r'(?:^|\n)(Clinical Pearls)\s*\n+(.*?)(?=\n\n[A-Z][^a-z]*:|$)',
                ],
                'memory_aid': [
                    r'(?:^|\n)(Memory aid:)\s*(.*?)(?=\n\n[A-Z][^a-z]*:|$)',
                ],
                'current_evidence': [
                    r'(?:^|\n)(Current Evidence)\s*\n+(.*?)(?=\n\n[A-Z][^a-z]*:|$)',
                ],
            }
            
            # Extract sections
            for key, patterns in section_patterns.items():
                for pattern in patterns:
                    match = re.search(pattern, text, re.DOTALL | re.MULTILINE)
                    if match:
                        content = match.group(2).strip()
                        if content:
                            sections[key] = content
                            break
        
        # If still no sections, try to parse as JSON
        if not sections:
            try:
                data = json.loads(text)
                if isinstance(data, dict):
                    sections = data
            except:
                pass
        
        return sections

    def handle(self, *args, **options):
        # Find MCQs with text explanations
        mcqs = MCQ.objects.all()
        updated_count = 0
        
        for mcq in mcqs:
            if mcq.explanation and len(mcq.explanation) > 500:
                # Try to parse it
                sections = self.parse_explanation_text(mcq.explanation)
                
                if sections and len(sections) > 2:  # Only update if we found multiple sections
                    if not mcq.explanation_sections or len(mcq.explanation_sections) < len(sections):
                        mcq.explanation_sections = sections
                        mcq.save()
                        updated_count += 1
                        self.stdout.write(f"Updated MCQ #{mcq.question_number}")
        
        self.stdout.write(self.style.SUCCESS(f'Successfully updated {updated_count} MCQs'))