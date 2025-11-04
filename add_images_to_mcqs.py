#!/usr/bin/env python
import os
import sys
import django

# Add the Django project directory to the Python path
django_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'django_neurology_mcq')
sys.path.insert(0, django_dir)

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq_bank.settings')
django.setup()

from mcq.models import MCQ

def add_image_to_mcq(mcq_id, image_url):
    """Add an image URL to a specific MCQ"""
    try:
        mcq = MCQ.objects.get(id=mcq_id)
        mcq.image_url = image_url
        mcq.save()
        print(f"✅ Added image to MCQ {mcq_id}: {mcq.question_text[:50]}...")
    except MCQ.DoesNotExist:
        print(f"❌ MCQ with ID {mcq_id} not found")
    except Exception as e:
        print(f"❌ Error updating MCQ {mcq_id}: {e}")

def bulk_add_images(image_mapping):
    """
    Add images to multiple MCQs at once
    image_mapping should be a dictionary: {mcq_id: image_url}
    """
    for mcq_id, image_url in image_mapping.items():
        add_image_to_mcq(mcq_id, image_url)

# Example usage:
if __name__ == "__main__":
    # Example 1: Add a single image
    # add_image_to_mcq(123, "https://i.imgur.com/example.jpg")
    
    # Example 2: Add multiple images
    images = {
        # MCQ_ID: "IMAGE_URL"
        # 123: "https://i.imgur.com/example1.jpg",
        # 124: "https://i.imgur.com/example2.jpg",
        # 125: "https://i.imgur.com/example3.jpg",
    }
    
    # Uncomment the line below and fill in the images dictionary
    # bulk_add_images(images)
    
    print("Script ready. Uncomment the example code and add your image mappings.")