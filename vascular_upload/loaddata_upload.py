#!/usr/bin/env python3
"""
Script to upload MCQs to Heroku using Django loaddata command
This is a simpler approach that uses Django's built-in fixtures capability
"""

import os
import json
import sys
import subprocess
import tempfile
from datetime import datetime

def convert_to_fixture(mcqs, app_name="mcq", model_name="MCQ"):
    """
    Converts MCQs to Django fixture format
    """
    fixtures = []
    for i, mcq in enumerate(mcqs):
        fixture = {
            "model": f"{app_name}.{model_name}",
            "pk": i + 1,  # This will be ignored for new objects
            "fields": {
                "question_text": mcq.get("question_text", ""),
                "options": mcq.get("options", {}),
                "correct_answer": mcq.get("correct_answer", ""),
                "explanation": mcq.get("explanation", ""),
                "subspecialty": mcq.get("subspecialty", "vascular_neurology"),
                "exam_year": mcq.get("exam_year", ""),
                "exam_type": mcq.get("exam_type", "")
            }
        }
        # Add image_url if present
        if "image_url" in mcq:
            fixture["fields"]["image_url"] = mcq["image_url"]
        
        fixtures.append(fixture)
    
    return fixtures

def upload_mcqs(file_path, app_name="radiant-gorge-35079"):
    """
    Uploads MCQs to Heroku app via Django loaddata command
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = f"loaddata_upload_{timestamp}.log"
    
    # Log function
    def log(message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"[{timestamp}] {message}"
        print(log_message)
        with open(log_file, "a") as f:
            f.write(log_message + "\n")
    
    log(f"Starting MCQ upload via Django loaddata for {file_path}")
    
    # Read MCQs from file
    try:
        with open(file_path, 'r') as f:
            mcqs = json.load(f)
        log(f"Loaded {len(mcqs)} MCQs from {file_path}")
    except Exception as e:
        log(f"Error reading file: {str(e)}")
        return False
    
    # Convert to fixture format
    fixtures = convert_to_fixture(mcqs)
    log(f"Converted {len(fixtures)} MCQs to fixture format")
    
    # Create a temporary file to hold the fixtures
    temp_dir = tempfile.mkdtemp()
    temp_file = os.path.join(temp_dir, "fixtures.json")
    with open(temp_file, 'w') as f:
        json.dump(fixtures, f, indent=2)
    log(f"Created temporary fixtures file at {temp_file}")
    
    # Upload fixtures file to Heroku
    log("Uploading fixtures file to Heroku...")
    with open(temp_file, 'r') as f:
        result = subprocess.run(
            ["heroku", "run", "cat > /tmp/vascular_fixtures.json", "--app", app_name],
            stdin=f,
            capture_output=True,
            text=True
        )
    if result.returncode != 0:
        log(f"Error uploading fixtures file: {result.stderr}")
        return False
    log("Fixtures file uploaded successfully")
    
    # Run loaddata command
    log("Running Django loaddata command...")
    result = subprocess.run(
        ["heroku", "run", "python manage.py loaddata /tmp/vascular_fixtures.json", "--app", app_name],
        capture_output=True,
        text=True
    )
    log("Loaddata command execution completed")
    
    if result.stdout:
        log("Command output:")
        for line in result.stdout.splitlines():
            log(f"  {line}")
    
    if result.stderr:
        log("Command errors:")
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
    os.rmdir(temp_dir)
    
    log("Upload process completed")
    log(f"Log file saved to: {log_file}")
    return True

def upload_all_chunks(directory, app_name="radiant-gorge-35079"):
    """
    Combines all chunks into a single fixture and uploads
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = f"all_chunks_loaddata_{timestamp}.log"
    
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
    
    # Combine all MCQs
    all_mcqs = []
    for chunk_file in chunk_files:
        with open(chunk_file, 'r') as f:
            mcqs = json.load(f)
            all_mcqs.extend(mcqs)
    log(f"Combined {len(all_mcqs)} MCQs from all chunks")
    
    # Convert to fixture format
    fixtures = convert_to_fixture(all_mcqs)
    log(f"Converted {len(fixtures)} MCQs to fixture format")
    
    # Create a temporary file to hold the fixtures
    temp_dir = tempfile.mkdtemp()
    temp_file = os.path.join(temp_dir, "fixtures.json")
    with open(temp_file, 'w') as f:
        json.dump(fixtures, f, indent=2)
    log(f"Created temporary fixtures file at {temp_file}")
    
    # Upload fixtures file to Heroku
    log("Uploading fixtures file to Heroku...")
    with open(temp_file, 'r') as f:
        result = subprocess.run(
            ["heroku", "run", "cat > /tmp/all_vascular_fixtures.json", "--app", app_name],
            stdin=f,
            capture_output=True,
            text=True
        )
    if result.returncode != 0:
        log(f"Error uploading fixtures file: {result.stderr}")
        return False
    log("Fixtures file uploaded successfully")
    
    # Run loaddata command
    log("Running Django loaddata command...")
    result = subprocess.run(
        ["heroku", "run", "python manage.py loaddata /tmp/all_vascular_fixtures.json", "--app", app_name],
        capture_output=True,
        text=True
    )
    log("Loaddata command execution completed")
    
    if result.stdout:
        log("Command output:")
        for line in result.stdout.splitlines():
            log(f"  {line}")
    
    if result.stderr:
        log("Command errors:")
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
    os.rmdir(temp_dir)
    
    log("Upload process completed")
    log(f"Log file saved to: {log_file}")
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  Single file: python loaddata_upload.py <file_path>")
        print("  All chunks: python loaddata_upload.py --all <directory>")
        sys.exit(1)
    
    if sys.argv[1] == "--all":
        if len(sys.argv) < 3:
            print("Usage for all mode: python loaddata_upload.py --all <directory>")
            sys.exit(1)
        directory = sys.argv[2]
        upload_all_chunks(directory)
    else:
        file_path = sys.argv[1]
        upload_mcqs(file_path)