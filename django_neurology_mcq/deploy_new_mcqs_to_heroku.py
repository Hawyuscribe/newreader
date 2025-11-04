#!/usr/bin/env python
"""
Deploy newly imported MCQs to Heroku
"""

import os
import sys
import json
import subprocess
from pathlib import Path

# Add the django project to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')

import django
django.setup()

from mcq.models import MCQ
from django.core import serializers

def export_mcqs_to_fixtures():
    """Export all MCQs to fixtures for Heroku deployment"""
    print("Exporting MCQs to fixtures...")
    
    # Get all MCQs
    mcqs = MCQ.objects.all()
    print(f"Total MCQs to export: {mcqs.count()}")
    
    # Serialize to JSON
    data = serializers.serialize('json', mcqs, indent=2)
    
    # Save to file
    fixture_path = Path('mcq_fixtures_complete.json')
    with open(fixture_path, 'w', encoding='utf-8') as f:
        f.write(data)
    
    print(f"Exported {mcqs.count()} MCQs to {fixture_path}")
    return fixture_path

def deploy_to_heroku(fixture_path):
    """Deploy fixtures to Heroku"""
    print("\nDeploying to Heroku...")
    
    # First, clear existing MCQs on Heroku
    print("Clearing existing MCQs on Heroku...")
    clear_cmd = [
        'heroku', 'run', 
        'python', 'manage.py', 'shell', 
        '--app', 'radiant-gorge-35079',
        '-c', '"from mcq.models import MCQ; MCQ.objects.all().delete(); print(f\'Deleted {MCQ.objects.count()} MCQs\')"'
    ]
    
    # Create a Python script to run on Heroku
    clear_script = """
from mcq.models import MCQ
count = MCQ.objects.count()
MCQ.objects.all().delete()
print(f'Deleted {count} MCQs')
print(f'Remaining MCQs: {MCQ.objects.count()}')
"""
    
    with open('clear_mcqs_heroku.py', 'w') as f:
        f.write(clear_script)
    
    # Run the clear script
    subprocess.run(['heroku', 'run', 'python', 'clear_mcqs_heroku.py', '--app', 'radiant-gorge-35079'])
    
    # Load fixtures
    print("\nLoading fixtures to Heroku...")
    load_cmd = [
        'heroku', 'run',
        'python', 'manage.py', 'loaddata', str(fixture_path),
        '--app', 'radiant-gorge-35079'
    ]
    
    subprocess.run(load_cmd)
    
    # Verify
    print("\nVerifying deployment...")
    verify_script = """
from mcq.models import MCQ
print(f'Total MCQs in Heroku: {MCQ.objects.count()}')

# Count by subspecialty
from django.db.models import Count
subspecialty_counts = MCQ.objects.values('subspecialty').annotate(count=Count('id')).order_by('-count')
print("\\nMCQs by subspecialty:")
for item in subspecialty_counts[:10]:
    print(f"  {item['subspecialty']}: {item['count']}")
"""
    
    with open('verify_mcqs_heroku.py', 'w') as f:
        f.write(verify_script)
    
    subprocess.run(['heroku', 'run', 'python', 'verify_mcqs_heroku.py', '--app', 'radiant-gorge-35079'])

def main():
    """Main deployment function"""
    print("Starting MCQ deployment to Heroku...")
    
    # Export MCQs
    fixture_path = export_mcqs_to_fixtures()
    
    # Deploy to Heroku
    deploy_to_heroku(fixture_path)
    
    print("\nDeployment complete!")

if __name__ == "__main__":
    main()