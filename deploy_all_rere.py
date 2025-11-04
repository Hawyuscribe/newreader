#!/usr/bin/env python3
"""
Deploy all RERE MCQs from chunks to Heroku in one command.
"""
import os
import json
import subprocess
import time
from pathlib import Path

# Configuration
APP_NAME = "radiant-gorge-35079"
CHUNK_DIR = Path("rere_chunks")

def run_heroku_command(command):
    """Run a command on Heroku."""
    full_command = f'heroku run "{command}" -a {APP_NAME}'
    print(f"Running: {full_command}")
    result = subprocess.run(full_command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    else:
        print(result.stdout)
    return result.returncode == 0

def main():
    print("Starting RERE MCQ deployment...")
    
    # Step 1: Clear existing MCQs
    print("\nStep 1: Clearing existing MCQs...")
    clear_cmd = """python django_neurology_mcq/manage.py shell --command="from mcq.models import MCQ; MCQ.objects.all().delete(); print(f'Cleared {MCQ.objects.count()} MCQs')" """
    run_heroku_command(clear_cmd)
    time.sleep(2)
    
    # Step 2: Load all chunks
    print("\nStep 2: Loading RERE chunks...")
    chunk_files = sorted(CHUNK_DIR.glob("rere_chunk_*.json"))
    
    for i, chunk_file in enumerate(chunk_files, 1):
        print(f"\nLoading chunk {i}/{len(chunk_files)}: {chunk_file.name}")
        load_cmd = f"python django_neurology_mcq/manage.py loaddata {chunk_file}"
        if not run_heroku_command(load_cmd):
            print(f"Failed to load {chunk_file.name}")
        time.sleep(1)
    
    # Step 3: Verification
    print("\nStep 3: Verifying deployment...")
    verify_cmd = """python django_neurology_mcq/manage.py shell --command="
from mcq.models import MCQ
from django.db.models import Count

total = MCQ.objects.count()
print(f'Total MCQs: {total}')

subspecialty_counts = MCQ.objects.values('subspecialty').annotate(count=Count('id')).order_by('subspecialty')
print('\\nMCQs by subspecialty:')
for sub in subspecialty_counts:
    print(f'  {sub[\"subspecialty\"]}: {sub[\"count\"]}')

mcqs_with_explanations = MCQ.objects.exclude(explanation_sections=None).exclude(explanation_sections={}).count()
print(f'\\nMCQs with explanation sections: {mcqs_with_explanations}')
" """
    run_heroku_command(verify_cmd)
    
    print("\nDeployment complete!")

if __name__ == "__main__":
    main()