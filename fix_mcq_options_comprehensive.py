#!/usr/bin/env python3
"""
Comprehensive fix for MCQ options formatting issues
Handles both local and Heroku environments
"""

import os
import sys
import django
import json
import ast

# Add the Django project path
sys.path.append('/Users/tariqalmatrudi/NEWreader/django_neurology_mcq')

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_neurology_mcq.settings')
django.setup()

from mcq.models import MCQ

def fix_mcq_options():
    """Find and fix all MCQs with improperly formatted options"""
    
    print("🔍 Comprehensive MCQ Options Format Analysis and Fix")
    print("=" * 60)
    
    # Get all MCQs
    all_mcqs = MCQ.objects.all()
    print(f"📊 Total MCQs in database: {all_mcqs.count()}")
    
    # Analyze current options formats
    problematic_mcqs = []
    json_format_mcqs = 0
    empty_options_mcqs = 0
    other_format_mcqs = []
    
    for mcq in all_mcqs:
        if not mcq.options:
            empty_options_mcqs += 1
            continue
            
        options_str = str(mcq.options)
        
        # Check if it's a Python list string representation
        if options_str.startswith("['") and options_str.endswith("']"):
            problematic_mcqs.append(mcq)
            print(f"❌ MCQ #{mcq.id}: {mcq.question_text[:50]}...")
            print(f"   Current: {options_str}")
            continue
            
        # Check if it's proper JSON format
        if options_str.startswith('{') and 'A' in options_str:
            json_format_mcqs += 1
            continue
            
        # Other formats
        other_format_mcqs.append((mcq.id, options_str[:100]))
    
    # Report analysis
    print(f"\n📈 Format Analysis:")
    print(f"   ✅ Proper JSON format: {json_format_mcqs}")
    print(f"   ❌ Python list format: {len(problematic_mcqs)}")
    print(f"   ⚪ Empty options: {empty_options_mcqs}")
    print(f"   ❓ Other formats: {len(other_format_mcqs)}")
    
    if other_format_mcqs:
        print(f"\n🔍 Other format examples:")
        for mcq_id, format_sample in other_format_mcqs[:5]:
            print(f"   MCQ #{mcq_id}: {format_sample}...")
    
    # Fix problematic MCQs
    if problematic_mcqs:
        print(f"\n🔧 Fixing {len(problematic_mcqs)} MCQs with Python list format...")
        fixed_count = 0
        
        for mcq in problematic_mcqs:
            try:
                # Convert string representation of list to actual list
                options_str = str(mcq.options)
                print(f"\n   Fixing MCQ #{mcq.id}")
                print(f"   Before: {options_str}")
                
                # Parse the Python list string
                options_list = ast.literal_eval(options_str)
                
                # Convert to proper JSON format (A, B, C, D, E)
                option_letters = ['A', 'B', 'C', 'D', 'E']
                options_dict = {}
                
                for i, option_text in enumerate(options_list):
                    if i < len(option_letters):
                        options_dict[option_letters[i]] = str(option_text).strip()
                
                # Update the MCQ with proper JSON format
                mcq.options = options_dict
                mcq.save()
                
                print(f"   After:  {json.dumps(options_dict, indent=2)}")
                print(f"   ✅ MCQ #{mcq.id} fixed successfully")
                fixed_count += 1
                
            except Exception as e:
                print(f"   ❌ Error fixing MCQ #{mcq.id}: {e}")
        
        print(f"\n🎉 Successfully fixed {fixed_count}/{len(problematic_mcqs)} MCQs")
    else:
        print(f"\n✅ No MCQs found with Python list format!")
    
    # Create Heroku deployment script
    heroku_script_content = f'''
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
                options_dict = {{}}
                
                for i, option_text in enumerate(options_list):
                    if i < len(option_letters):
                        options_dict[option_letters[i]] = str(option_text).strip()
                
                mcq.options = options_dict
                mcq.save()
                fixed_count += 1
                print(f"✅ Fixed MCQ #{{mcq.id}}")
                
            except Exception as e:
                print(f"❌ Error fixing MCQ #{{mcq.id}}: {{e}}")

print(f"\\n📊 Results:")
print(f"   Found: {{problematic_count}} problematic MCQs")
print(f"   Fixed: {{fixed_count}} MCQs")
print("🎉 Heroku fix complete!")
'''
    
    # Write Heroku script
    with open('/Users/tariqalmatrudi/NEWreader/heroku_fix_options.py', 'w') as f:
        f.write(heroku_script_content)
    
    print(f"\n📝 Created Heroku deployment script: heroku_fix_options.py")
    print(f"   Run on Heroku with: heroku run python heroku_fix_options.py")
    
    print(f"\n✅ MCQ options formatting fix complete!")

if __name__ == "__main__":
    fix_mcq_options()