#!/usr/bin/env python3
"""
Fix MCQ options formatting issue
Converts Python list format to proper JSON format for options
"""

import os
import sys
import django
import json

# Add the Django project path
sys.path.append('/Users/tariqalmatrudi/NEWreader/django_neurology_mcq')

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_neurology_mcq.settings')
django.setup()

from mcq.models import MCQ

def fix_mcq_options():
    """Find and fix MCQs with improperly formatted options"""
    
    print("🔍 Searching for MCQs with formatting issues...")
    
    # Find MCQs where options is stored as a string representation of a list
    problematic_mcqs = []
    
    for mcq in MCQ.objects.all():
        if mcq.options:
            options_str = str(mcq.options)
            # Check if it looks like a Python list string representation
            if options_str.startswith("['") and options_str.endswith("']"):
                problematic_mcqs.append(mcq)
                print(f"Found problematic MCQ #{mcq.id}: {mcq.question_text[:50]}...")
    
    print(f"\n📊 Found {len(problematic_mcqs)} MCQs with formatting issues")
    
    if not problematic_mcqs:
        print("✅ No formatting issues found!")
        return
    
    # Fix each problematic MCQ
    for mcq in problematic_mcqs:
        try:
            # Convert string representation of list to actual list
            options_str = str(mcq.options)
            print(f"\n🔧 Fixing MCQ #{mcq.id}")
            print(f"   Current: {options_str}")
            
            # Parse the Python list string
            import ast
            options_list = ast.literal_eval(options_str)
            
            # Convert to proper JSON format (A, B, C, D)
            option_letters = ['A', 'B', 'C', 'D', 'E']
            options_dict = {}
            
            for i, option_text in enumerate(options_list):
                if i < len(option_letters):
                    options_dict[option_letters[i]] = option_text
            
            # Update the MCQ with proper JSON format
            mcq.options = options_dict
            mcq.save()
            
            print(f"   Fixed:   {json.dumps(options_dict, indent=2)}")
            print(f"   ✅ MCQ #{mcq.id} fixed successfully")
            
        except Exception as e:
            print(f"   ❌ Error fixing MCQ #{mcq.id}: {e}")
    
    print(f"\n🎉 Completed fixing {len(problematic_mcqs)} MCQs")

if __name__ == "__main__":
    fix_mcq_options()