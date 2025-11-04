#!/usr/bin/env python3
"""
Heroku MCQ Options Fix Script
Direct deployment to fix Python list format options
"""

import os
import django
import sys
import json
import ast

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_neurology_mcq.settings')
django.setup()

from mcq.models import MCQ

print("🔧 Heroku MCQ Options Fix")
print("=" * 30)

# Find and fix problematic MCQs
problematic_count = 0
fixed_count = 0

for mcq in MCQ.objects.all():
    if mcq.options:
        options_str = str(mcq.options)
        if options_str.startswith("['") and options_str.endswith("']"):
            problematic_count += 1
            try:
                # Parse and convert
                options_list = ast.literal_eval(options_str)
                option_letters = ['A', 'B', 'C', 'D', 'E']
                options_dict = {}
                
                for i, option_text in enumerate(options_list):
                    if i < len(option_letters):
                        options_dict[option_letters[i]] = str(option_text).strip()
                
                mcq.options = options_dict
                mcq.save()
                fixed_count += 1
                print(f"✅ Fixed MCQ #{mcq.id}: {mcq.question_text[:50]}...")
                
            except Exception as e:
                print(f"❌ Error fixing MCQ #{mcq.id}: {e}")

print(f"\n📊 Results:")
print(f"   Found: {problematic_count} problematic MCQs")
print(f"   Fixed: {fixed_count} MCQs")
print("🎉 Heroku fix complete!")