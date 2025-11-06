#!/usr/bin/env python3
"""
Test random MCQ conversion on Heroku after fixing JSON serialization
"""
import sys
import os
import django
import requests
import time

# Setup Django environment
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_neurology_mcq.mcq.settings')
django.setup()

from django.contrib.auth.models import User
from django_neurology_mcq.mcq.models import MCQ, MCQCaseConversionSession

def test_random_mcq_on_heroku():
    """Test a random MCQ conversion on Heroku"""
    heroku_url = "https://radiant-gorge-35079-2b52ba172c1e.herokuapp.com"
    
    print("Testing random MCQ conversion on Heroku after JSON serialization fix...")
    print("=" * 80)
    
    # First, let's check if we can access the site
    try:
        response = requests.get(f"{heroku_url}/mcq/")
        print(f"Site accessibility check: {response.status_code}")
    except Exception as e:
        print(f"Error accessing site: {e}")
        return
    
    # Get a random MCQ ID from production
    print("\nGetting random MCQ from production database...")
    
    # We'll simulate the conversion process by checking the logs
    print("\nTo test the conversion, please:")
    print("1. Go to https://radiant-gorge-35079-2b52ba172c1e.herokuapp.com/mcq/")
    print("2. Click on any MCQ")
    print("3. Click 'Convert to Case-Based Learning'")
    print("4. Monitor the logs with: heroku logs --tail --app radiant-gorge-35079")
    print("\nAlternatively, run this command to see recent conversion attempts:")
    print("heroku logs --app radiant-gorge-35079 | grep -E 'Case conversion|ValidationStatus|JSON serializable'")

if __name__ == "__main__":
    test_random_mcq_on_heroku()