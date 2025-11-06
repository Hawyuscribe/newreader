#!/usr/bin/env python3
"""
Script to upload MCQs to Heroku using Django management commands
This approach uses Heroku CLI which should already be authenticated
"""

import os
import json
import sys
import subprocess
import tempfile
from datetime import datetime

def upload_mcqs(file_path, app_name="radiant-gorge-35079"):
    """
    Uploads MCQs to Heroku app via Django management command
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = f"django_upload_{timestamp}.log"
    
    # Log function
    def log(message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"[{timestamp}] {message}"
        print(log_message)
        with open(log_file, "a") as f:
            f.write(log_message + "\n")
    
    log(f"Starting MCQ upload via Django management command for {file_path}")
    
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
    
    # Create a custom management command to import the MCQs
    management_script = """
import json
import os
from django.core.management.base import BaseCommand
from mcq.models import MCQ
from django.db import transaction

class Command(BaseCommand):
    help = 'Import MCQs from a JSON file'

    def handle(self, *args, **options):
        file_path = '/tmp/mcqs.json'
        self.stdout.write(self.style.SUCCESS(f'Starting import from {file_path}'))
        
        try:
            with open(file_path, 'r') as f:
                mcqs_data = json.load(f)
            
            self.stdout.write(f'Found {len(mcqs_data)} MCQs to import')
            
            created_count = 0
            updated_count = 0
            error_count = 0
            
            with transaction.atomic():
                for i, mcq_data in enumerate(mcqs_data):
                    try:
                        # Extract fields
                        question_text = mcq_data.get('question_text', '')
                        if not question_text:
                            self.stdout.write(self.style.ERROR(f'MCQ #{i+1} missing question text, skipping'))
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
                            if (i+1) % 10 == 0:
                                self.stdout.write(f'Updated {updated_count} MCQs so far...')
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
                            if (i+1) % 10 == 0:
                                self.stdout.write(f'Created {created_count} MCQs so far...')
                    
                    except Exception as e:
                        error_count += 1
                        self.stdout.write(self.style.ERROR(f'Error processing MCQ #{i+1}: {str(e)}'))
            
            # Print summary
            self.stdout.write('\\nRESULTS:')
            self.stdout.write(self.style.SUCCESS(f'MCQs created: {created_count}'))
            self.stdout.write(self.style.SUCCESS(f'MCQs updated: {updated_count}'))
            self.stdout.write(self.style.ERROR(f'MCQs failed: {error_count}'))
            
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {str(e)}'))
"""
    
    # Create directory for management command
    log("Creating management command on Heroku...")
    cmds = [
        "mkdir -p /tmp/mcq/management/commands",
        "touch /tmp/mcq/management/__init__.py",
        "touch /tmp/mcq/management/commands/__init__.py"
    ]
    for cmd in cmds:
        result = subprocess.run(
            ["heroku", "run", cmd, "--app", app_name],
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            log(f"Error creating management command structure: {result.stderr}")
            return False
    
    # Upload management command
    command_file = os.path.join(temp_dir, "import_mcqs.py")
    with open(command_file, 'w') as f:
        f.write(management_script)
    
    log("Uploading management command script...")
    with open(command_file, 'r') as f:
        result = subprocess.run(
            ["heroku", "run", "cat > /tmp/mcq/management/commands/import_mcqs.py", "--app", app_name],
            stdin=f,
            capture_output=True,
            text=True
        )
    if result.returncode != 0:
        log(f"Error uploading management command: {result.stderr}")
        return False
    log("Management command uploaded successfully")
    
    # Run the management command
    log("Running Django management command...")
    result = subprocess.run(
        ["heroku", "run", "python manage.py import_mcqs", "--app", app_name],
        capture_output=True,
        text=True
    )
    log("Management command execution completed")
    
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
    os.remove(command_file)
    os.rmdir(temp_dir)
    
    log("Upload process completed")
    log(f"Log file saved to: {log_file}")
    return True

def upload_all_chunks(directory, app_name="radiant-gorge-35079"):
    """
    Uploads all chunk files one by one
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = f"all_chunks_django_{timestamp}.log"
    
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
        print("  Single file: python heroku_django_upload.py <file_path>")
        print("  All chunks: python heroku_django_upload.py --all <directory>")
        sys.exit(1)
    
    if sys.argv[1] == "--all":
        if len(sys.argv) < 3:
            print("Usage for all mode: python heroku_django_upload.py --all <directory>")
            sys.exit(1)
        directory = sys.argv[2]
        upload_all_chunks(directory)
    else:
        file_path = sys.argv[1]
        upload_mcqs(file_path)