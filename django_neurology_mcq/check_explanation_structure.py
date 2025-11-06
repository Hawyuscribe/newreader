#!/usr/bin/env python
import os
import sys

# Add project path
sys.path.insert(0, '/Users/tariqalmatrudi/NEWreader/django_neurology_mcq')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')

import django
django.setup()

from mcq.models import MCQ
import json

# Check a few MCQs to see their explanation structure
mcqs_with_explanations = MCQ.objects.exclude(explanation_sections__isnull=True).exclude(explanation_sections={})[:5]

print(f"Found {mcqs_with_explanations.count()} MCQs with explanation_sections")

for i, mcq in enumerate(mcqs_with_explanations):
    print(f"\n--- MCQ {i+1} (ID: {mcq.id}, Q#: {mcq.question_number}) ---")
    print(f"Question: {mcq.question_text[:100]}...")
    
    if mcq.explanation_sections:
        print("\nExplanation sections found:")
        sections = mcq.explanation_sections
        for key, value in sections.items():
            print(f"  - {key}: {len(value)} chars" if value else f"  - {key}: empty")
        
        # Show first section that has content
        for key, value in sections.items():
            if value:
                print(f"\nSample from '{key}':")
                print(value[:200] + "..." if len(value) > 200 else value)
                break
    else:
        print("No explanation_sections")

# Also check if any MCQs have explanation field but no explanation_sections
mcqs_with_old_format = MCQ.objects.filter(
    explanation_sections__isnull=True
).exclude(explanation="").exclude(explanation__isnull=True)[:3]

print(f"\n\nFound {mcqs_with_old_format.count()} MCQs with old format explanations")

for mcq in mcqs_with_old_format:
    print(f"\nMCQ ID {mcq.id} has explanation field:")
    print(mcq.explanation[:200] + "..." if len(mcq.explanation) > 200 else mcq.explanation)