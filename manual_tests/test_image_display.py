#!/usr/bin/env python
import os
import sys
import django

# Add the Django project directory to the Python path
django_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'django_neurology_mcq')
sys.path.insert(0, django_dir)

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
django.setup()

from mcq.models import MCQ

def test_image_url(mcq_id=99993398):
    """Test what image URL is stored for an MCQ"""
    try:
        mcq = MCQ.objects.get(id=mcq_id)
        print(f"MCQ ID: {mcq.id}")
        print(f"Question: {mcq.question_text[:50]}...")
        print(f"Image URL: '{mcq.image_url}'")
        print(f"URL Type: {type(mcq.image_url)}")
        print(f"URL Length: {len(mcq.image_url) if mcq.image_url else 0}")
        
        # Check if it's a Google Drive URL
        if mcq.image_url and 'drive.google.com' in mcq.image_url:
            print("This is a Google Drive URL")
            if 'uc?export=view' in mcq.image_url:
                print("URL is already in direct view format")
            else:
                print("URL needs conversion to direct view format")
                
    except MCQ.DoesNotExist:
        print(f"MCQ with ID {mcq_id} not found")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Test with the specific MCQ
    test_image_url(99993398)