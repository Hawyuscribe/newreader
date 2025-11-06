#!/usr/bin/env python3
"""
A script to upload vascular MCQs to Heroku using the Heroku CLI
which is already authenticated in the current environment.
"""

import os
import json
import subprocess
import sys
import time

def upload_chunk(chunk_file_path, app_name="radiant-gorge-35079"):
    """
    Upload a single chunk of MCQs to the Heroku app using the CLI
    """
    # Ensure the chunk file exists
    if not os.path.exists(chunk_file_path):
        print(f"Error: File not found - {chunk_file_path}")
        return False
    
    # Read the MCQ data from the chunk file
    try:
        with open(chunk_file_path, 'r') as f:
            mcqs = json.load(f)
        print(f"Found {len(mcqs)} MCQs in the chunk file")
    except Exception as e:
        print(f"Error reading the chunk file: {e}")
        return False
    
    # Create a temporary file on the local system
    temp_file = "/tmp/current_chunk.json"
    with open(temp_file, 'w') as f:
        json.dump(mcqs, f)
    print(f"Created temporary file at {temp_file}")
    
    # Create a temp directory on Heroku
    print("Creating temporary directory on Heroku...")
    result = subprocess.run(
        ["heroku", "run", "mkdir -p /tmp", "--app", app_name],
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        print(f"Error creating temp directory: {result.stderr}")
        return False
    
    # Upload the chunk file to Heroku
    print("Uploading chunk file to Heroku...")
    with open(temp_file, 'r') as f:
        result = subprocess.run(
            ["heroku", "run", "cat > /tmp/vascular_chunk.json", "--app", app_name],
            stdin=f,
            capture_output=True,
            text=True
        )
    if result.returncode != 0:
        print(f"Error uploading chunk file: {result.stderr}")
        return False
    
    # Create the import script
    import_script = """
import json
import os
from django.db import transaction
from mcq.models import MCQ

# Load MCQ data from temp file
with open('/tmp/vascular_chunk.json', 'r') as f:
    mcqs_data = json.load(f)

print(f"Importing {len(mcqs_data)} vascular MCQs")

# Track success and errors
success_count = 0
update_count = 0
error_count = 0

# Import MCQs
with transaction.atomic():
    for i, mcq_data in enumerate(mcqs_data):
        try:
            # Ensure required fields
            if 'question_text' not in mcq_data:
                print(f"Missing question_text, skipping")
                error_count += 1
                continue
                
            # Create or update MCQ
            defaults = {
                'subspecialty': mcq_data.get('subspecialty', 'vascular_neurology'),
                'question_text': mcq_data.get('question_text', ''),
                'options': mcq_data.get('options', {}),
                'correct_answer': mcq_data.get('correct_answer', ''),
                'explanation': mcq_data.get('explanation', ''),
                'exam_year': mcq_data.get('exam_year', ''),
                'exam_type': mcq_data.get('exam_type', ''),
            }
            
            # Add image URL if present
            if 'image_url' in mcq_data:
                defaults['image_url'] = mcq_data['image_url']
            
            # Use question_text as unique identifier
            mcq, created = MCQ.objects.update_or_create(
                question_text=mcq_data.get('question_text'),
                defaults=defaults
            )
            
            if created:
                success_count += 1
                print(f"Created new MCQ #{i+1}: {mcq_data.get('question_text')[:30]}...")
            else:
                update_count += 1
                print(f"Updated existing MCQ #{i+1}: {mcq_data.get('question_text')[:30]}...")
                
        except Exception as e:
            error_count += 1
            print(f"Error processing MCQ #{i+1}: {str(e)}")

print("\\nRESULTS:")
print(f"Successfully created: {success_count} MCQs")
print(f"Successfully updated: {update_count} MCQs")
print(f"Failed to import: {error_count} MCQs")
print("Import completed successfully")
    """
    
    # Write the import script to a temporary file
    script_file = "/tmp/import_script.py"
    with open(script_file, 'w') as f:
        f.write(import_script)
    print(f"Created import script at {script_file}")
    
    # Upload the import script to Heroku
    print("Uploading import script to Heroku...")
    with open(script_file, 'r') as f:
        result = subprocess.run(
            ["heroku", "run", "cat > /tmp/import_script.py", "--app", app_name],
            stdin=f,
            capture_output=True,
            text=True
        )
    if result.returncode != 0:
        print(f"Error uploading import script: {result.stderr}")
        return False
    
    # Run the import script on Heroku
    print("Running import script on Heroku...")
    result = subprocess.run(
        ["heroku", "run", "python /tmp/import_script.py", "--app", app_name],
        capture_output=True,
        text=True
    )
    print(result.stdout)
    if result.returncode != 0:
        print(f"Error running import script: {result.stderr}")
        return False
    
    # Check the MCQ count after import
    print("Checking MCQ count after import...")
    result = subprocess.run(
        ["heroku", "run", "python -c \"from mcq.models import MCQ; print(f'Total MCQs: {MCQ.objects.count()}'); print(f'Vascular MCQs: {MCQ.objects.filter(subspecialty=\\\"vascular_neurology\\\").count()}');\"", "--app", app_name],
        capture_output=True,
        text=True
    )
    print(result.stdout)
    
    # Clean up temporary files
    os.unlink(temp_file)
    os.unlink(script_file)
    print("Cleaned up temporary files")
    
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python cli_upload.py <path_to_chunk_file>")
        sys.exit(1)
    
    chunk_file = sys.argv[1]
    if upload_chunk(chunk_file):
        print("Upload completed successfully!")
    else:
        print("Upload failed.")
        sys.exit(1)