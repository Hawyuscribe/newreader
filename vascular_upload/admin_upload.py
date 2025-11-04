#!/usr/bin/env python3
"""
Script to upload MCQs to Heroku via the Django shell
This approach uses the Heroku CLI which should be authenticated already
"""

import os
import json
import sys
import subprocess
import tempfile
from datetime import datetime

def upload_mcqs(file_path, app_name="radiant-gorge-35079"):
    """
    Uploads MCQs to Heroku app via Django shell
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = f"admin_upload_{timestamp}.log"
    
    # Log function
    def log(message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"[{timestamp}] {message}"
        print(log_message)
        with open(log_file, "a") as f:
            f.write(log_message + "\n")
    
    log(f"Starting MCQ upload via Django shell for {file_path}")
    
    # Read MCQs from file
    try:
        with open(file_path, 'r') as f:
            mcqs = json.load(f)
        log(f"Loaded {len(mcqs)} MCQs from {file_path}")
    except Exception as e:
        log(f"Error reading file: {str(e)}")
        return False
    
    # Create a temporary file to hold the MCQs
    temp_dir = tempfile.mkdtemp()
    temp_file = os.path.join(temp_dir, "mcqs.json")
    with open(temp_file, 'w') as f:
        json.dump(mcqs, f)
    log(f"Created temporary file at {temp_file}")
    
    # Create a Django shell script to import the MCQs
    shell_script = """
import json
import sys
from django.db import transaction
from mcq.models import MCQ

# Load MCQs from the temp file
with open('/tmp/mcqs.json', 'r') as f:
    mcqs = json.load(f)

print(f"Processing {len(mcqs)} MCQs")

# Track success and errors
created_count = 0
updated_count = 0
error_count = 0
errors = []

# Import MCQs
with transaction.atomic():
    for i, mcq_data in enumerate(mcqs):
        try:
            # Extract fields
            question_text = mcq_data.get('question_text', '')
            if not question_text:
                print(f"MCQ #{i+1} missing question text, skipping")
                error_count += 1
                continue
                
            options = mcq_data.get('options', {})
            correct_answer = mcq_data.get('correct_answer', '')
            explanation = mcq_data.get('explanation', '')
            subspecialty = mcq_data.get('subspecialty', 'vascular_neurology')
            exam_year = mcq_data.get('exam_year', '')
            exam_type = mcq_data.get('exam_type', '')
            
            # Check if MCQ already exists
            existing_mcqs = MCQ.objects.filter(question_text=question_text)
            
            if existing_mcqs.exists():
                # Update existing MCQ
                existing_mcq = existing_mcqs.first()
                existing_mcq.options = options
                existing_mcq.correct_answer = correct_answer
                existing_mcq.explanation = explanation
                existing_mcq.subspecialty = subspecialty
                existing_mcq.exam_year = exam_year
                existing_mcq.exam_type = exam_type
                existing_mcq.save()
                updated_count += 1
                print(f"Updated MCQ #{i+1}: {question_text[:30]}...")
            else:
                # Create new MCQ
                mcq = MCQ(
                    question_text=question_text,
                    options=options,
                    correct_answer=correct_answer,
                    explanation=explanation,
                    subspecialty=subspecialty,
                    exam_year=exam_year,
                    exam_type=exam_type
                )
                mcq.save()
                created_count += 1
                print(f"Created MCQ #{i+1}: {question_text[:30]}...")
        
        except Exception as e:
            error_count += 1
            error_msg = f"Error processing MCQ #{i+1}: {str(e)}"
            errors.append(error_msg)
            print(error_msg)

# Print summary
print("\\nRESULTS:")
print(f"MCQs created: {created_count}")
print(f"MCQs updated: {updated_count}")
print(f"MCQs failed: {error_count}")

# Print detailed errors
if errors:
    print("\\nErrors:")
    for error in errors[:10]:
        print(f" - {error}")
    if len(errors) > 10:
        print(f" - ...and {len(errors) - 10} more errors")
    """
    
    shell_script_file = os.path.join(temp_dir, "import_script.py")
    with open(shell_script_file, 'w') as f:
        f.write(shell_script)
    log(f"Created Django shell script at {shell_script_file}")
    
    # Upload MCQs file to Heroku
    log("Uploading MCQs file to Heroku...")
    with open(temp_file, 'r') as f:
        result = subprocess.run(
            ["heroku", "run", "cat > /tmp/mcqs.json", "--app", app_name],
            stdin=f,
            capture_output=True,
            text=True
        )
    if result.returncode != 0:
        log(f"Error uploading MCQs file: {result.stderr}")
        return False
    log("MCQs file uploaded successfully")
    
    # Upload shell script to Heroku
    log("Uploading Django shell script to Heroku...")
    with open(shell_script_file, 'r') as f:
        result = subprocess.run(
            ["heroku", "run", "cat > /tmp/import_script.py", "--app", app_name],
            stdin=f,
            capture_output=True,
            text=True
        )
    if result.returncode != 0:
        log(f"Error uploading shell script: {result.stderr}")
        return False
    log("Shell script uploaded successfully")
    
    # Run the Django shell script on Heroku
    log("Running Django shell script on Heroku...")
    result = subprocess.run(
        ["heroku", "run", "python manage.py shell < /tmp/import_script.py", "--app", app_name],
        capture_output=True,
        text=True
    )
    log("Django shell execution completed")
    
    if result.stdout:
        log("Script output:")
        for line in result.stdout.splitlines():
            log(f"  {line}")
    
    if result.stderr:
        log("Script errors:")
        for line in result.stderr.splitlines():
            log(f"  {line}")
    
    # Check MCQ count after import
    log("Checking MCQ count after import...")
    result = subprocess.run(
        ["heroku", "run", "python -c \"from mcq.models import MCQ; print(f'Total MCQs: {MCQ.objects.count()}'); print(f'Vascular MCQs: {MCQ.objects.filter(subspecialty=\\\"vascular_neurology\\\").count()}');\"", "--app", app_name],
        capture_output=True,
        text=True
    )
    if result.stdout:
        log(f"Current MCQ count: {result.stdout}")
    
    # Clean up temporary files
    log("Cleaning up temporary files...")
    os.remove(temp_file)
    os.remove(shell_script_file)
    os.rmdir(temp_dir)
    
    log("Upload process completed")
    log(f"Log file saved to: {log_file}")
    return True

def upload_all_chunks(directory, app_name="radiant-gorge-35079"):
    """
    Uploads all chunk files one by one
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = f"all_chunks_upload_{timestamp}.log"
    
    # Log function
    def log(message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"[{timestamp}] {message}"
        print(log_message)
        with open(log_file, "a") as f:
            f.write(log_message + "\n")
    
    log(f"Starting upload of all chunks from {directory}")
    
    # Get all chunk files
    chunk_files = []
    for filename in os.listdir(directory):
        if filename.startswith("vascular_chunk_") and filename.endswith(".json") and "manifest" not in filename:
            chunk_files.append(os.path.join(directory, filename))
    
    # Sort chunk files numerically
    chunk_files.sort()
    log(f"Found {len(chunk_files)} chunk files")
    
    # Process each chunk
    for i, chunk_file in enumerate(chunk_files):
        log(f"Processing chunk {i+1}/{len(chunk_files)}: {os.path.basename(chunk_file)}")
        success = upload_mcqs(chunk_file, app_name)
        if success:
            log(f"Successfully uploaded chunk {i+1}")
        else:
            log(f"Failed to upload chunk {i+1}")
        
        # Small delay between chunks
        if i < len(chunk_files) - 1:
            log("Waiting 10 seconds before next chunk...")
            import time
            time.sleep(10)
    
    log("All chunks processed")
    log(f"Log file saved to: {log_file}")
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  Single file: python admin_upload.py <file_path>")
        print("  All chunks: python admin_upload.py --all <directory>")
        sys.exit(1)
    
    if sys.argv[1] == "--all":
        if len(sys.argv) < 3:
            print("Usage for all mode: python admin_upload.py --all <directory>")
            sys.exit(1)
        directory = sys.argv[2]
        upload_all_chunks(directory)
    else:
        file_path = sys.argv[1]
        upload_mcqs(file_path)