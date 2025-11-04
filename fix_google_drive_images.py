#!/usr/bin/env python
"""
Fix Google Drive image URLs by providing instructions for migration to Imgur
"""

import os
import sys
import django

# Setup Django environment
sys.path.append(os.path.join(os.path.dirname(__file__), 'django_neurology_mcq'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
django.setup()

from mcq.models import MCQ

def main():
    # Find MCQs with Google Drive URLs
    google_drive_mcqs = MCQ.objects.filter(image_url__icontains='drive.google.com')
    
    print(f"Found {google_drive_mcqs.count()} MCQs with Google Drive URLs")
    print("\nGoogle Drive doesn't work for image embedding. Here's what to do:")
    print("="*60)
    
    for mcq in google_drive_mcqs:
        print(f"\nMCQ ID: {mcq.id}")
        print(f"Question: {mcq.question_text[:100]}...")
        print(f"Current URL: {mcq.image_url}")
        print("\nTo fix this:")
        print("1. Download the image from Google Drive")
        print("2. Upload to https://imgur.com")
        print("3. Right-click the uploaded image and 'Copy image address'")
        print("4. Update in admin: https://radiant-gorge-35079-2b52ba172c1e.herokuapp.com/admin/mcq/mcq/{}/change/".format(mcq.id))
        print("-"*60)
    
    # For the specific MCQ we were testing
    if google_drive_mcqs.filter(id=99993398).exists():
        print("\n" + "="*60)
        print("FOR YOUR TEST MCQ (ID: 99993398):")
        print("="*60)
        print("Here's a sample Imgur URL you can use for testing:")
        print("https://i.imgur.com/7j4RGnH.jpg")
        print("\nThis is a sample medical image for testing purposes.")
        
        response = input("\nWould you like to update this MCQ with the sample URL? (y/n): ")
        if response.lower() == 'y':
            test_mcq = MCQ.objects.get(id=99993398)
            test_mcq.image_url = "https://i.imgur.com/7j4RGnH.jpg"
            test_mcq.save()
            print("✅ Updated MCQ 99993398 with sample Imgur URL")
            print("Test it at: https://radiant-gorge-35079-2b52ba172c1e.herokuapp.com/mcq/99993398/test_image/")

if __name__ == '__main__':
    main()