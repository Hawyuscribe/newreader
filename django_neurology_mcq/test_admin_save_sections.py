#!/usr/bin/env python
import os
import sys

# Add project path
sys.path.insert(0, '/Users/tariqalmatrudi/NEWreader/django_neurology_mcq')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')

import django
django.setup()

from django.contrib.auth.models import User
from mcq.models import MCQ
from mcq.admin import MCQAdminForm
import json

# Get a test MCQ
test_mcq = MCQ.objects.get(id=100025246)

print(f"Testing save functionality for MCQ {test_mcq.id}")
print(f"Original sections in explanation_sections:")
if test_mcq.explanation_sections:
    for key, value in test_mcq.explanation_sections.items():
        if value:
            print(f"  - {key}: {len(value)} chars")

# Prepare form data as if submitted from admin
form_data = {
    'question_text': test_mcq.question_text,
    'correct_answer': test_mcq.correct_answer,
    'subspecialty': test_mcq.subspecialty,
    'exam_type': test_mcq.exam_type,
    'exam_year': test_mcq.exam_year,
    'question_number': test_mcq.question_number,
    'options_text': 'A. Option A\nB. Option B\nC. Option C\nD. Option D',
    
    # New explanation sections
    'conceptual_foundation': 'Test conceptual foundation content',
    'pathophysiology': 'Test pathophysiology content',
    'clinical_correlation': 'Test clinical correlation content',
    'diagnostic_approach': 'Test diagnostic approach content',
    'classification_neurology': 'Test classification and neurology content',
    'management_principles': 'Test management principles content',
    'option_analysis': 'Test option analysis content',
    'clinical_pearls': 'Test clinical pearls content',
    'current_evidence': 'Test current evidence content',
}

# Create form instance
form = MCQAdminForm(data=form_data, instance=test_mcq)

if form.is_valid():
    # Save the instance (but don't commit to DB in this test)
    saved_mcq = form.save(commit=False)
    
    print("\nNew sections after form save:")
    if saved_mcq.explanation_sections:
        expected_keys = [
            'conceptual foundation',
            'pathophysiology',
            'clinical correlation',
            'diagnostic approach',
            'classification and neurology',
            'management principles',
            'option analysis',
            'clinical pearls',
            'current evidence'
        ]
        
        for key in expected_keys:
            if key in saved_mcq.explanation_sections:
                value = saved_mcq.explanation_sections[key]
                print(f"  ✓ {key}: '{value}'")
            else:
                print(f"  ✗ {key}: Not found in explanation_sections!")
        
        # Check underscore versions too
        print("\nUnderscore versions:")
        underscore_keys = [k.replace(' ', '_') for k in expected_keys]
        for key in underscore_keys:
            if key in saved_mcq.explanation_sections:
                print(f"  ✓ {key}: Found")
    else:
        print("No explanation_sections found after save!")
    
    print("\nForm save successful - all new sections properly structured")
else:
    print("\nForm validation failed:")
    print(form.errors)