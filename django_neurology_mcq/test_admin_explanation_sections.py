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

# Get a superuser to simulate admin access
try:
    admin_user = User.objects.filter(is_superuser=True).first()
    if not admin_user:
        print("No superuser found to test with")
        exit(1)
except Exception as e:
    print(f"Error getting admin user: {e}")
    exit(1)

# Test loading an MCQ with new format sections
print("Testing MCQ admin form loading with new sections...")
test_mcq = MCQ.objects.get(id=100025249)  # This has all sections

# Create form instance to test loading
form = MCQAdminForm(instance=test_mcq)

# Check that all new fields are populated
expected_fields = [
    'conceptual_foundation',
    'pathophysiology',
    'clinical_correlation',
    'diagnostic_approach',
    'classification_neurology',
    'management_principles',
    'option_analysis',
    'clinical_pearls',
    'current_evidence'
]

print("\nChecking field mappings:")
for field in expected_fields:
    if field in form.fields:
        initial_value = form.fields[field].initial
        if initial_value:
            print(f"✓ {field}: {len(initial_value)} chars loaded")
        else:
            print(f"✗ {field}: No data loaded")
    else:
        print(f"✗ {field}: Field not found in form!")

# Show the actual section keys in the MCQ
print("\nActual sections in MCQ.explanation_sections:")
if test_mcq.explanation_sections:
    for key, value in test_mcq.explanation_sections.items():
        if value:
            print(f"  - {key}: {len(value)} chars")
else:
    print("No explanation_sections found!")

# Test remapping logic
print("\nTesting field remapping:")
if test_mcq.explanation_sections:
    # pathophysiological_mechanisms should map to pathophysiology
    if 'pathophysiological_mechanisms' in test_mcq.explanation_sections:
        content = test_mcq.explanation_sections['pathophysiological_mechanisms']
        if form.fields['pathophysiology'].initial == content:
            print("✓ pathophysiological_mechanisms correctly mapped to pathophysiology field")
        else:
            print("✗ pathophysiological_mechanisms mapping failed")
    
    # classification_and_nosology should map to classification_neurology
    if 'classification_and_nosology' in test_mcq.explanation_sections:
        content = test_mcq.explanation_sections['classification_and_nosology']
        if form.fields['classification_neurology'].initial == content:
            print("✓ classification_and_nosology correctly mapped to classification_neurology field")
        else:
            print("✗ classification_and_nosology mapping failed")