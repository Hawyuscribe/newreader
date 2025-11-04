#!/usr/bin/env python3
"""Script to deploy RERE MCQs to Heroku using local file paths."""

import os
import json
import subprocess
import time
from pathlib import Path

# RERE directory path
RERE_DIR = "/Users/tariqalmatrudi/NEWreader/RERE"

# List of specialty files to import
SPECIALTY_FILES = [
    "Critical_Care_Neurology.json",
    "Dementia.json",
    "Epilepsy.json",
    "Headache.json",
    "Movement_Disorders.json",
    "Neuro-infectious.json",
    "Neuro-oncology.json",
    "Neuro-otology.json",
    "Neuroanatomy.json",
    "Neurogenetics.json",
    "Neuroimmunology.json",
    "Neuromuscular.json",
    "Neuroophthalmology.json",
    "Neuropharmacology.json",
    "Neuropsychiatry.json",
    "Neurotoxicology.json",
    "Pediatric_Neurology.json",
    "Sleep_Neurology.json",
    "Vascular_Neurology_Stroke.json"
]

def verify_file(filename):
    """Verify JSON file exists and count MCQs."""
    file_path = os.path.join(RERE_DIR, filename)
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        mcq_count = len(data.get('mcqs', []))
        specialty = data.get('specialty', 'unknown')
        print(f"  {filename}: {mcq_count} MCQs (specialty: {specialty})")
        return True, mcq_count
    except Exception as e:
        print(f"  ERROR processing {filename}: {e}")
        return False, 0

def run_import_command(filename):
    """Run the heroku import command for a specific file."""
    file_path = os.path.join(RERE_DIR, filename)
    
    # Copy file to Heroku temporarily
    cmd = [
        'heroku', 'run', 'bash', '-c',
        f'cat > /tmp/{filename}',
        '--app', 'mcq-bank'
    ]
    
    # Send file content to Heroku
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Import using the management command with local file path
    import_cmd = [
        'heroku', 'run',
        'python', 'django_neurology_mcq/manage.py', 'import_rere_mcqs',
        '--file', f'/app/RERE/{filename}',
        '--app', 'mcq-bank'
    ]
    
    print(f"\nImporting {filename}...")
    result = subprocess.run(import_cmd, capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"✓ Successfully imported {filename}")
        # Parse the output to get import stats
        output_lines = result.stdout.split('\n')
        for line in output_lines:
            if 'Created' in line or 'Updated' in line or 'IMPORTED' in line:
                print(f"  {line}")
    else:
        print(f"✗ Failed to import {filename}")
        print(f"  Error: {result.stderr}")
        print(f"  Output: {result.stdout}")
    
    return result.returncode == 0

def main():
    print("=== RERE MCQ Local Deployment Script ===\n")
    
    # Verify all files exist
    print("1. Verifying JSON files...")
    total_mcqs = 0
    valid_files = []
    
    for filename in SPECIALTY_FILES:
        valid, count = verify_file(filename)
        if valid:
            valid_files.append(filename)
            total_mcqs += count
    
    print(f"\nFound {len(valid_files)} valid files with {total_mcqs} total MCQs.")
    
    # Check current MCQ count
    print("\n2. Checking current database state...")
    count_cmd = ['heroku', 'run', 'python', 'django_neurology_mcq/manage.py', 'shell', '-c', 
                 '"from mcq.models import MCQ; print(f\'Current MCQs: {MCQ.objects.count()}\')"', 
                 '--app', 'mcq-bank']
    
    result = subprocess.run(count_cmd, capture_output=True, text=True)
    print(result.stdout)
    
    # Import each file
    print("\n3. Importing MCQs to Heroku...")
    success_count = 0
    
    for filename in valid_files:
        if run_import_command(filename):
            success_count += 1
        time.sleep(2)  # Small delay between imports
    
    # Verify final count
    print("\n4. Verifying final deployment...")
    result = subprocess.run(count_cmd, capture_output=True, text=True)
    print(result.stdout)
    
    print(f"\n=== Summary ===")
    print(f"Files processed: {len(valid_files)} / {len(SPECIALTY_FILES)}")
    print(f"Imports successful: {success_count} / {len(valid_files)}")
    print(f"Expected MCQs: {total_mcqs}")
    
    print("\nDeployment complete!")

if __name__ == "__main__":
    main()