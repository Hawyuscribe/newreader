import re
from django.core.management.base import BaseCommand
from django.db import transaction
from mcq.models import MCQ


class Command(BaseCommand):
    help = 'Fix explanation sections that contain duplicated content'

    def extract_section_content(self, full_text, section_pattern, next_section_pattern=None):
        """Extract content for a specific section."""
        if not full_text:
            return ""
        
        # Find the start of this section
        match = re.search(section_pattern, full_text, re.IGNORECASE | re.MULTILINE)
        if not match:
            return ""
        
        start_pos = match.end()
        
        # Find the start of the next section (if provided)
        if next_section_pattern:
            next_match = re.search(next_section_pattern, full_text[start_pos:], re.IGNORECASE | re.MULTILINE)
            if next_match:
                end_pos = start_pos + next_match.start()
                content = full_text[start_pos:end_pos].strip()
            else:
                content = full_text[start_pos:].strip()
        else:
            content = full_text[start_pos:].strip()
        
        return content

    def fix_explanation_sections(self, mcq):
        """Fix explanation sections that contain duplicated content."""
        if not mcq.explanation_sections:
            return False
        
        # Check if this MCQ needs fixing
        needs_fixing = False
        for key, value in mcq.explanation_sections.items():
            if value and isinstance(value, str) and '##' in value and any(pattern in value.lower() for pattern in ['## 3.', '## 4.', '## 5.', '## 6.', '## 7.', '## 8.', '## 9.']):
                needs_fixing = True
                break
        
        if not needs_fixing:
            return False
        
        # Get the full explanation text (usually from option_analysis which often contains everything)
        full_text = ""
        for section in ['option_analysis', 'conceptual_foundation', 'pathophysiology', 'pathophysiological_mechanisms', 'clinical_manifestation', 'clinical_correlation']:
            if mcq.explanation_sections.get(section) and '##' in mcq.explanation_sections.get(section, ''):
                full_text = mcq.explanation_sections[section]
                break
        
        if not full_text:
            return False
        
        # Define section patterns
        section_patterns = [
            ('option_analysis', r'(?:## 1\.|###?\s*Option Analysis|###?\s*A\)|Option A)', r'## 2\.'),
            ('conceptual_foundation', r'## 2\.', r'## 3\.'),
            ('pathophysiological_mechanisms', r'## 3\.', r'## 4\.'),
            ('clinical_correlation', r'## 4\.', r'## 5\.'),
            ('diagnostic_approach', r'## 5\.', r'## 6\.'),
            ('management_principles', r'## 6\.', r'## 7\.'),
            ('follow_up_guidelines', r'## 7\.', r'## 8\.'),
            ('clinical_pearls', r'## 8\.', r'## 9\.'),
            ('current_evidence', r'## 9\.', None)
        ]
        
        # Extract each section
        new_sections = {}
        for i, (section_name, pattern, next_pattern) in enumerate(section_patterns):
            content = self.extract_section_content(full_text, pattern, next_pattern)
            
            if content and content != "This section information is included within the unified explanation.":
                new_sections[section_name] = content
        
        # Special handling for option_analysis - if it contains option breakdowns
        if 'option_analysis' in new_sections:
            # Check if it starts with option breakdown
            option_content = new_sections['option_analysis']
            if re.match(r'###?\s*[A-E]\)', option_content) or 'Option A' in option_content:
                # Extract only the option analysis part (before ## 2.)
                section_2_match = re.search(r'## 2\.', option_content)
                if section_2_match:
                    new_sections['option_analysis'] = option_content[:section_2_match.start()].strip()
        
        # Update the MCQ if we extracted meaningful sections
        if len(new_sections) >= 5:  # Require at least 5 sections with content
            mcq.explanation_sections = new_sections
            mcq.save()
            return True
        
        return False

    def handle(self, *args, **options):
        self.stdout.write("Fixing explanation sections with duplicated content...")
        
        # Get MCQs that need fixing
        mcqs_to_fix = []
        
        # First, find MCQs with placeholder text
        for mcq in MCQ.objects.all():
            if mcq.explanation_sections:
                for key, value in mcq.explanation_sections.items():
                    if value and isinstance(value, str) and 'unified explanation' in value.lower():
                        mcqs_to_fix.append(mcq)
                        break
        
        self.stdout.write(f"Found {len(mcqs_to_fix)} MCQs with placeholder text")
        
        # Also check for MCQs with duplicated content
        checked_ids = {mcq.id for mcq in mcqs_to_fix}
        for mcq in MCQ.objects.all():
            if mcq.id not in checked_ids and mcq.explanation_sections:
                # Check if sections contain numbered sections like ## 3., ## 4., etc.
                for key, value in mcq.explanation_sections.items():
                    if value and isinstance(value, str) and '##' in value and any(pattern in value for pattern in ['## 3.', '## 4.', '## 5.']):
                        mcqs_to_fix.append(mcq)
                        break
        
        self.stdout.write(f"Total MCQs to fix: {len(mcqs_to_fix)}")
        
        fixed_count = 0
        with transaction.atomic():
            for i, mcq in enumerate(mcqs_to_fix):
                if i % 100 == 0:
                    self.stdout.write(f"Processing MCQ {i+1}/{len(mcqs_to_fix)}...")
                
                if self.fix_explanation_sections(mcq):
                    fixed_count += 1
        
        self.stdout.write(self.style.SUCCESS(f"\nFixed {fixed_count} MCQs"))
        
        # Verify the fixes
        self.stdout.write("\nVerifying fixes...")
        still_has_placeholders = 0
        for mcq in MCQ.objects.all():
            if mcq.explanation_sections:
                for key, value in mcq.explanation_sections.items():
                    if value and isinstance(value, str) and 'unified explanation' in value.lower():
                        still_has_placeholders += 1
                        break
        
        self.stdout.write(f"MCQs still with placeholder text: {still_has_placeholders}")