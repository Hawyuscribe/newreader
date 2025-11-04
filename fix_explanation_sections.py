#!/usr/bin/env python
import os
import sys
import re
import json
from datetime import datetime

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_neurology_mcq.settings')

import django
django.setup()

from mcq.models import MCQ


def extract_section_content(full_text, section_pattern, next_section_pattern=None):
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


def fix_explanation_sections(mcq):
    """Fix explanation sections that contain duplicated content."""
    if not mcq.explanation_sections:
        return False
    
    # Check if this MCQ needs fixing
    needs_fixing = False
    for key, value in mcq.explanation_sections.items():
        if value and '##' in value and any(pattern in value.lower() for pattern in ['## 3.', '## 4.', '## 5.', '## 6.', '## 7.', '## 8.', '## 9.']):
            needs_fixing = True
            break
    
    if not needs_fixing:
        return False
    
    # Get the full explanation text (usually from option_analysis which often contains everything)
    full_text = ""
    for section in ['option_analysis', 'conceptual_foundation', 'pathophysiology', 'clinical_manifestation']:
        if mcq.explanation_sections.get(section) and '##' in mcq.explanation_sections.get(section, ''):
            full_text = mcq.explanation_sections[section]
            break
    
    if not full_text:
        return False
    
    # Define section patterns
    section_patterns = [
        ('option_analysis', r'(?:## 1\.|###?\s*Option Analysis|###?\s*A\)|Option A)', r'## 2\.'),
        ('conceptual_foundation', r'## 2\.', r'## 3\.'),
        ('pathophysiology', r'## 3\.', r'## 4\.'),
        ('clinical_manifestation', r'## 4\.', r'## 5\.'),
        ('diagnostic_approach', r'## 5\.', r'## 6\.'),
        ('management_principles', r'## 6\.', r'## 7\.'),
        ('follow_up_guidelines', r'## 7\.', r'## 8\.'),
        ('clinical_pearls', r'## 8\.', r'## 9\.'),
        ('references', r'## 9\.', None)
    ]
    
    # Also map to the database field names
    field_mapping = {
        'pathophysiology': 'pathophysiological_mechanisms',
        'clinical_manifestation': 'clinical_correlation',
        'references': 'current_evidence'
    }
    
    # Extract each section
    new_sections = {}
    for i, (section_name, pattern, next_pattern) in enumerate(section_patterns):
        content = extract_section_content(full_text, pattern, next_pattern)
        
        # Map to the correct database field name
        db_field = field_mapping.get(section_name, section_name)
        
        if content and content != "This section information is included within the unified explanation.":
            new_sections[db_field] = content
    
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


def main():
    print("Fixing explanation sections with duplicated content...")
    
    # Get MCQs that need fixing
    mcqs_to_fix = []
    for mcq in MCQ.objects.all():
        if mcq.explanation_sections:
            for key, value in mcq.explanation_sections.items():
                if value and 'unified explanation' in value.lower():
                    mcqs_to_fix.append(mcq)
                    break
    
    print(f"Found {len(mcqs_to_fix)} MCQs with placeholder text")
    
    # Also check for MCQs with duplicated content
    for mcq in MCQ.objects.all():
        if mcq.explanation_sections and mcq not in mcqs_to_fix:
            # Check if sections contain numbered sections like ## 3., ## 4., etc.
            for key, value in mcq.explanation_sections.items():
                if value and '##' in value and any(pattern in value for pattern in ['## 3.', '## 4.', '## 5.']):
                    mcqs_to_fix.append(mcq)
                    break
    
    print(f"Total MCQs to fix: {len(mcqs_to_fix)}")
    
    fixed_count = 0
    for i, mcq in enumerate(mcqs_to_fix):
        if i % 100 == 0:
            print(f"Processing MCQ {i+1}/{len(mcqs_to_fix)}...")
        
        if fix_explanation_sections(mcq):
            fixed_count += 1
    
    print(f"\nFixed {fixed_count} MCQs")
    
    # Verify the fixes
    print("\nVerifying fixes...")
    still_has_placeholders = 0
    for mcq in MCQ.objects.all():
        if mcq.explanation_sections:
            for key, value in mcq.explanation_sections.items():
                if value and 'unified explanation' in value.lower():
                    still_has_placeholders += 1
                    break
    
    print(f"MCQs still with placeholder text: {still_has_placeholders}")


if __name__ == "__main__":
    main()