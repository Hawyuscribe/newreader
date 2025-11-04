#!/usr/bin/env python
"""Test explanation editing functionality"""

import os
import sys
import django
import json

# Setup Django
sys.path.insert(0, '/Users/tariqalmatrudi/NEWreader/django_neurology_mcq')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
django.setup()

from mcq.models import MCQ
from mcq.admin import MCQAdminForm
from django.contrib.auth.models import User

# Find an MCQ with explanations
mcq = MCQ.objects.filter(explanation_sections__isnull=False).first()

if mcq:
    print(f"Testing with MCQ #{mcq.question_number}")
    print(f"Original explanation_sections keys: {list(mcq.explanation_sections.keys())}")
    
    # Create form data simulating admin edit
    form_data = {
        'question_text': mcq.question_text,
        'options_text': 'A. Option A\nB. Option B\nC. Option C\nD. Option D',
        'correct_answer': mcq.correct_answer,
        'subspecialty': mcq.subspecialty,
        'exam_type': mcq.exam_type or 'Other',
        'exam_year': mcq.exam_year or 2024,
        'question_number': mcq.question_number,
        'source_file': mcq.source_file or '',
        
        # Explanation sections - modifying existing ones
        'conceptual_foundation': 'Updated conceptual foundation text',
        'option_analysis': 'Updated option analysis text',
        'clinical_context': 'Updated clinical context text',
        'key_insight': 'New key insight text',
        'quick_reference': 'New quick reference text',
        'application_and_recall': 'New application and recall text',
    }
    
    # Create form instance
    form = MCQAdminForm(data=form_data, instance=mcq)
    
    if form.is_valid():
        # Save the form
        mcq_updated = form.save(commit=False)
        
        print("\nAfter save:")
        print(f"explanation_sections keys: {list(mcq_updated.explanation_sections.keys())}")
        print(f"explanation_sections content preview:")
        for key, value in mcq_updated.explanation_sections.items():
            print(f"  {key}: {value[:50]}...")
        
        print("\nForm save successful!")
    else:
        print("\nForm errors:")
        print(form.errors)
else:
    print("No MCQ with explanation_sections found.")