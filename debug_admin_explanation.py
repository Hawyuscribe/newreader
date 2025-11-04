#!/usr/bin/env python
"""Debug explanation display in admin"""

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
from django.db import models

# Find MCQs with explanations
print("Checking MCQs with explanations...")
mcqs_with_explanations = MCQ.objects.filter(
    models.Q(explanation_sections__isnull=False) | 
    models.Q(explanation__isnull=False)
).exclude(
    models.Q(explanation_sections={}) & 
    models.Q(explanation='')
)[:5]

for i, mcq in enumerate(mcqs_with_explanations):
    print(f"\nMCQ {i+1} (#{mcq.question_number}):")
    print(f"  Has explanation_sections: {bool(mcq.explanation_sections)}")
    print(f"  Has explanation: {bool(mcq.explanation)}")
    
    if mcq.explanation_sections:
        print(f"  explanation_sections type: {type(mcq.explanation_sections)}")
        print(f"  explanation_sections keys: {list(mcq.explanation_sections.keys())}")
    
    if mcq.explanation:
        print(f"  explanation type: {type(mcq.explanation)}")
        print(f"  explanation preview: {mcq.explanation[:100]}...")
        
    # Create form to see what gets populated
    form = MCQAdminForm(instance=mcq)
    print(f"  Form fields populated:")
    for field in ['conceptual_foundation', 'option_analysis', 'clinical_context', 'key_insight', 'quick_reference', 'application_and_recall']:
        initial_value = form.fields[field].initial
        if initial_value:
            print(f"    {field}: {initial_value[:50]}...")
        else:
            print(f"    {field}: (empty)")

# Check for any import statements we need
print("\nChecking imports...")
from django.db import models