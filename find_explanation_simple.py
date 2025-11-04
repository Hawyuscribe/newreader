#!/usr/bin/env python
"""Find the specific explanation text - simplified"""

import os
import sys
import django
import json

# Setup Django
sys.path.insert(0, '/Users/tariqalmatrudi/NEWreader/django_neurology_mcq')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
django.setup()

from mcq.models import MCQ

# Search for the specific text pattern
search_patterns = [
    "Acute ischemic stroke occurs",
    "cerebral artery is occluded",
    "Conceptual Foundation",
]

print("Searching for explanations with specific patterns...")

found_count = 0
for mcq in MCQ.objects.all():
    if mcq.explanation_sections:
        full_text = json.dumps(mcq.explanation_sections)
        for pattern in search_patterns:
            if pattern in full_text:
                found_count += 1
                print(f"\nMCQ #{mcq.question_number}")
                print(f"  Found pattern: {pattern}")
                
                # Show the fields
                for key, value in mcq.explanation_sections.items():
                    if pattern in str(value):
                        print(f"  Field: {key}")
                        print(f"  Content preview: {str(value)[:200]}...")
                        
                # Create the form to see what gets populated
                from mcq.admin import MCQAdminForm
                form = MCQAdminForm(instance=mcq)
                
                print("  Form fields:")
                for field_name in ['conceptual_foundation', 'option_analysis', 'clinical_context']:
                    initial = form.fields[field_name].initial
                    if initial:
                        print(f"    {field_name}: {initial[:50]}...")
                    else:
                        print(f"    {field_name}: (empty)")
                
                if found_count >= 3:
                    break
        if found_count >= 3:
            break

print(f"\nFound {found_count} MCQs with the patterns")