#!/usr/bin/env python
"""Test admin interface directly"""

import os
import sys
import django

# Setup Django
sys.path.insert(0, '/Users/tariqalmatrudi/NEWreader/django_neurology_mcq')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
django.setup()

from django.test import RequestFactory
from django.contrib.admin.sites import AdminSite
from django.contrib.auth.models import User
from mcq.admin import MCQAdmin
from mcq.models import MCQ

# Create a mock request
request_factory = RequestFactory()
request = request_factory.get('/admin/mcq/mcq/1/change/')

# Create a superuser (needed for admin)
user = User.objects.filter(is_superuser=True).first()
if not user:
    user = User.objects.create_superuser('admin', 'admin@test.com', 'admin')
request.user = user

# Get an MCQ with explanations
mcq = MCQ.objects.filter(
    explanation_sections__isnull=False
).first()

if mcq:
    print(f"Testing with MCQ #{mcq.question_number}")
    
    # Create admin instance
    admin_site = AdminSite()
    mcq_admin = MCQAdmin(MCQ, admin_site)
    
    # Get the form
    form_class = mcq_admin.get_form(request, mcq)
    form = form_class(instance=mcq)
    
    # Check fields
    print("\nForm fields available:")
    for field_name in form.fields:
        print(f"  {field_name}")
    
    print("\nExplanation section fields:")
    section_fields = [
        'conceptual_foundation',
        'option_analysis', 
        'clinical_context',
        'key_insight',
        'quick_reference',
        'application_and_recall'
    ]
    
    for field_name in section_fields:
        if field_name in form.fields:
            field = form.fields[field_name]
            print(f"\n{field_name}:")
            print(f"  Widget: {type(field.widget).__name__}")
            print(f"  Required: {field.required}")
            print(f"  Initial value: {field.initial[:50] if field.initial else '(empty)'}...")
            
            # Check bound data if available
            if hasattr(form, 'data') and form.data.get(field_name):
                print(f"  Current value: {form.data[field_name][:50]}...")
        else:
            print(f"\n{field_name}: NOT FOUND IN FORM")
    
    # Check if the explanation field is hidden
    if 'explanation' in form.fields:
        explanation_field = form.fields['explanation']
        print(f"\nexplanation field:")
        print(f"  Widget: {type(explanation_field.widget).__name__}")
        print(f"  Hidden: {'HiddenInput' in str(type(explanation_field.widget))}")
else:
    print("No MCQ with explanation_sections found")