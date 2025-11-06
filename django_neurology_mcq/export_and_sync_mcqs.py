#!/usr/bin/env python
"""
Export all MCQs and create sync script for Heroku
"""

import os
import sys
import json
from pathlib import Path

# Add the django project to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')

import django
django.setup()

from mcq.models import MCQ
from django.core import serializers

def export_mcqs_in_chunks():
    """Export MCQs in chunks for Heroku deployment"""
    print("Exporting MCQs in chunks...")
    
    # Get all MCQs
    mcqs = MCQ.objects.all().order_by('id')
    total_count = mcqs.count()
    print(f"Total MCQs to export: {total_count}")
    
    # Calculate chunk size (200 MCQs per chunk)
    chunk_size = 200
    num_chunks = (total_count + chunk_size - 1) // chunk_size
    
    chunk_files = []
    
    for i in range(num_chunks):
        start_idx = i * chunk_size
        end_idx = min(start_idx + chunk_size, total_count)
        
        # Get chunk of MCQs
        chunk_mcqs = mcqs[start_idx:end_idx]
        
        # Serialize to JSON
        data = serializers.serialize('json', chunk_mcqs, indent=2)
        
        # Save to file
        chunk_num = str(i + 1).zfill(3)
        total_chunks = str(num_chunks).zfill(3)
        filename = f'heroku_sync_chunk_{chunk_num}_of_{total_chunks}.json'
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(data)
        
        chunk_files.append(filename)
        print(f"Created {filename} with {len(chunk_mcqs)} MCQs")
    
    return chunk_files, num_chunks

def create_sync_script(chunk_files, num_chunks):
    """Create bash script to sync MCQs to Heroku"""
    script_content = """#!/bin/bash
# Heroku MCQ sync script - Generated automatically
echo "Starting MCQ sync to Heroku..."

# First, commit and push the fixture files to Heroku
echo "Adding fixture files to git..."
"""
    
    # Add git commands to stage all chunk files
    for chunk_file in chunk_files:
        script_content += f"git add {chunk_file}\n"
    
    script_content += """
git commit -m "Add MCQ fixture chunks for sync"
git push heroku stable_version:main

# Wait for deployment
echo "Waiting for deployment to complete..."
sleep 30

# Clear existing MCQs first
echo "Clearing existing MCQs..."
heroku run "cd django_neurology_mcq && python manage.py shell -c 'from mcq.models import MCQ; count = MCQ.objects.count(); MCQ.objects.all().delete(); print(f\"Cleared {count} MCQs\")'" --app radiant-gorge-35079

# Load each chunk
"""
    
    for i, chunk_file in enumerate(chunk_files, 1):
        script_content += f"""
echo "Loading chunk {i}/{num_chunks}..."
heroku run "cd django_neurology_mcq && python manage.py loaddata {chunk_file}" --app radiant-gorge-35079
"""
    
    script_content += """
echo "Verifying final count..."
heroku run "cd django_neurology_mcq && python manage.py shell -c 'from mcq.models import MCQ; from django.db.models import Count; total = MCQ.objects.count(); print(f\"Final count: {total} MCQs\"); subspecialties = MCQ.objects.values(\"subspecialty\").annotate(count=Count(\"id\")).order_by(\"-count\"); print(\"\\nTop subspecialties:\"); [print(f\"  {s[\\\"subspecialty\\\"]}: {s[\\\"count\\\"]}\") for s in subspecialties[:5]]'" --app radiant-gorge-35079

echo "MCQ sync complete!"
"""
    
    # Save script
    script_path = 'sync_mcqs_to_heroku.sh'
    with open(script_path, 'w') as f:
        f.write(script_content)
    
    # Make script executable
    os.chmod(script_path, 0o755)
    
    print(f"\nCreated sync script: {script_path}")
    return script_path

def main():
    """Main export function"""
    print("MCQ Export and Sync Script Generator")
    print("=" * 50)
    
    # Export MCQs in chunks
    chunk_files, num_chunks = export_mcqs_in_chunks()
    
    # Create sync script
    script_path = create_sync_script(chunk_files, num_chunks)
    
    print(f"\nExport complete!")
    print(f"Created {num_chunks} chunk files")
    print(f"\nTo sync MCQs to Heroku, run:")
    print(f"  ./{script_path}")

if __name__ == "__main__":
    main()