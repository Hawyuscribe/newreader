#!/usr/bin/env python3
"""Delete all existing MCQs from Heroku database."""
import os
import sys
import django

# Django setup
sys.path.append('/app/django_neurology_mcq')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
django.setup()

from mcq.models import MCQ

def delete_all_mcqs():
    """Delete all MCQs and provide confirmation."""
    try:
        initial_count = MCQ.objects.count()
        print(f"Found {initial_count} MCQs in database")
        
        if initial_count > 0:
            MCQ.objects.all().delete()
            print("✓ All MCQs deleted successfully")
        else:
            print("No MCQs to delete")
            
        final_count = MCQ.objects.count()
        print(f"Final count: {final_count} MCQs")
        
    except Exception as e:
        print(f"Error deleting MCQs: {e}")
        sys.exit(1)

if __name__ == "__main__":
    delete_all_mcqs()