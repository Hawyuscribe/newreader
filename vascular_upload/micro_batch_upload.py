#!/usr/bin/env python3
"""
Script to upload MCQs to Heroku in very small batches
This approach sends just a few MCQs at a time to avoid timeouts
"""

import os
import json
import sys
import subprocess
import tempfile
import time
from datetime import datetime

def upload_mcqs_micro_batches(file_path, batch_size=5, app_name="radiant-gorge-35079"):
    """
    Uploads MCQs to Heroku in very small batches
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = f"micro_batch_upload_{timestamp}.log"
    
    # Log function
    def log(message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"[{timestamp}] {message}"
        print(log_message)
        with open(log_file, "a") as f:
            f.write(log_message + "\n")
    
    log(f"Starting MCQ upload in micro-batches of {batch_size} for {file_path}")
    
    # Read MCQs from file
    try:
        with open(file_path, 'r') as f:
            mcqs = json.load(f)
        log(f"Loaded {len(mcqs)} MCQs from {file_path}")
    except Exception as e:
        log(f"Error reading file: {str(e)}")
        return False
    
    # Check current MCQ count
    log("Checking initial MCQ count...")
    result = subprocess.run(
        ["heroku", "run", "python -c \"from mcq.models import MCQ; print(f'Total MCQs: {MCQ.objects.count()}'); print(f'Vascular MCQs: {MCQ.objects.filter(subspecialty=\\\"vascular_neurology\\\").count()}');\"", "--app", app_name],
        capture_output=True,
        text=True
    )
    if result.stdout:
        log(f"Initial MCQ count: {result.stdout}")
    
    # Split MCQs into micro-batches
    batches = []
    for i in range(0, len(mcqs), batch_size):
        batches.append(mcqs[i:i+batch_size])
    log(f"Split into {len(batches)} micro-batches")
    
    # Create a simple Django script to import MCQs
    script_template = """
import json
import os
from django.db import transaction
from mcq.models import MCQ

# MCQs data as a string - will be replaced for each batch
mcqs_json = '''
{mcqs_json}
'''

# Parse MCQs from JSON
mcqs_data = json.loads(mcqs_json)
print(f"Processing {len(mcqs_data)} MCQs")

# Track success and errors
created_count = 0
updated_count = 0
error_count = 0

# Import MCQs
with transaction.atomic():
    for i, mcq_data in enumerate(mcqs_data):
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
            print(f"Error processing MCQ #{i+1}: {str(e)}")

# Print summary
print("\\nRESULTS:")
print(f"MCQs created: {created_count}")
print(f"MCQs updated: {updated_count}")
print(f"MCQs failed: {error_count}")
"""
    
    # Process each batch
    success_count = 0
    error_count = 0
    
    for i, batch in enumerate(batches):
        log(f"Processing batch {i+1}/{len(batches)} with {len(batch)} MCQs...")
        
        # Create script with this batch's MCQs
        batch_json = json.dumps(batch, indent=2).replace("'", "\\'")
        script = script_template.replace("{mcqs_json}", batch_json)
        
        # Create a temporary file for the script
        temp_dir = tempfile.mkdtemp()
        script_file = os.path.join(temp_dir, "batch_import.py")
        with open(script_file, 'w') as f:
            f.write(script)
        
        # Upload script to Heroku
        log(f"Uploading batch {i+1} script to Heroku...")
        with open(script_file, 'r') as f:
            result = subprocess.run(
                ["heroku", "run", "cat > /tmp/batch_import.py", "--app", app_name],
                stdin=f,
                capture_output=True,
                text=True
            )
        if result.returncode != 0:
            log(f"Error uploading script for batch {i+1}: {result.stderr}")
            error_count += 1
            continue
        
        # Run the script
        log(f"Running batch {i+1} import...")
        result = subprocess.run(
            ["heroku", "run", "python -c 'exec(open(\"/tmp/batch_import.py\").read())'", "--app", app_name],
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            log(f"Error running import for batch {i+1}: {result.stderr}")
            error_count += 1
        else:
            log(f"Batch {i+1} import complete")
            if result.stdout:
                log("Output:")
                for line in result.stdout.splitlines():
                    log(f"  {line}")
            success_count += 1
        
        # Clean up
        os.remove(script_file)
        os.rmdir(temp_dir)
        
        # Wait between batches
        if i < len(batches) - 1:
            log("Waiting 2 seconds before next batch...")
            time.sleep(2)
    
    # Check final MCQ count
    log("Checking final MCQ count...")
    result = subprocess.run(
        ["heroku", "run", "python -c \"from mcq.models import MCQ; print(f'Total MCQs: {MCQ.objects.count()}'); print(f'Vascular MCQs: {MCQ.objects.filter(subspecialty=\\\"vascular_neurology\\\").count()}');\"", "--app", app_name],
        capture_output=True,
        text=True
    )
    if result.stdout:
        log(f"Final MCQ count: {result.stdout}")
    
    log(f"Upload process completed: {success_count} batches succeeded, {error_count} batches failed")
    log(f"Log file saved to: {log_file}")
    return True

def upload_all_chunks(directory, batch_size=5, app_name="radiant-gorge-35079"):
    """
    Uploads all chunk files one by one using micro-batches
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = f"all_chunks_micro_{timestamp}.log"
    
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
        success = upload_mcqs_micro_batches(chunk_file, batch_size, app_name)
        if success:
            log(f"Successfully uploaded chunk {i+1}")
        else:
            log(f"Failed to upload chunk {i+1}")
        
        # Small delay between chunks
        if i < len(chunk_files) - 1:
            log("Waiting 10 seconds before next chunk...")
            time.sleep(10)
    
    log("All chunks processed")
    log(f"Log file saved to: {log_file}")
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  Single file: python micro_batch_upload.py <file_path> [batch_size]")
        print("  All chunks: python micro_batch_upload.py --all <directory> [batch_size]")
        sys.exit(1)
    
    # Default batch size
    batch_size = 5
    
    if sys.argv[1] == "--all":
        if len(sys.argv) < 3:
            print("Usage for all mode: python micro_batch_upload.py --all <directory> [batch_size]")
            sys.exit(1)
        directory = sys.argv[2]
        if len(sys.argv) >= 4:
            batch_size = int(sys.argv[3])
        upload_all_chunks(directory, batch_size)
    else:
        file_path = sys.argv[1]
        if len(sys.argv) >= 3:
            batch_size = int(sys.argv[2])
        upload_mcqs_micro_batches(file_path, batch_size)