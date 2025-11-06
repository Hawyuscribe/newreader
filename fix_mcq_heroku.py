#!/usr/bin/env python3
"""
Fix MCQ options formatting issue on Heroku
Creates a Django management command to fix options format
"""

import os

# Create the management command file
management_command = """
from django.core.management.base import BaseCommand
from mcq.models import MCQ
import json
import ast

class Command(BaseCommand):
    help = 'Fix MCQ options formatting issues'
    
    def handle(self, *args, **options):
        self.stdout.write('🔍 Searching for MCQs with formatting issues...')
        
        problematic_mcqs = []
        
        for mcq in MCQ.objects.all():
            if mcq.options:
                options_str = str(mcq.options)
                # Check if it looks like a Python list string representation
                if options_str.startswith("['") and options_str.endswith("']"):
                    problematic_mcqs.append(mcq)
        
        self.stdout.write(f'📊 Found {len(problematic_mcqs)} MCQs with formatting issues')
        
        if not problematic_mcqs:
            self.stdout.write(self.style.SUCCESS('✅ No formatting issues found!'))
            return
        
        # Fix each problematic MCQ
        fixed_count = 0
        for mcq in problematic_mcqs:
            try:
                # Convert string representation of list to actual list
                options_str = str(mcq.options)
                
                # Parse the Python list string
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
                
                self.stdout.write(f'✅ Fixed MCQ #{mcq.id}: {mcq.question_text[:50]}...')
                fixed_count += 1
                
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'❌ Error fixing MCQ #{mcq.id}: {e}')
                )
        
        self.stdout.write(
            self.style.SUCCESS(f'🎉 Successfully fixed {fixed_count} MCQs')
        )
"""

# Ensure the management command directory exists
os.makedirs('django_neurology_mcq/mcq/management', exist_ok=True)
os.makedirs('django_neurology_mcq/mcq/management/commands', exist_ok=True)

# Create __init__.py files
with open('django_neurology_mcq/mcq/management/__init__.py', 'w') as f:
    f.write('')

with open('django_neurology_mcq/mcq/management/commands/__init__.py', 'w') as f:
    f.write('')

# Write the management command
with open('django_neurology_mcq/mcq/management/commands/fix_mcq_options.py', 'w') as f:
    f.write(management_command)

print("✅ Created Django management command: fix_mcq_options")
print("📝 You can now run this on Heroku with:")
print("   heroku run python django_neurology_mcq/manage.py fix_mcq_options")