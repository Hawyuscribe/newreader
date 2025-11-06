#!/usr/bin/env python3
"""
Robust script to upload vascular MCQs to Heroku, one batch at a time
Handles connection issues and provides resume capability
"""

import os
import sys
import json
import time
import subprocess
import tempfile
from datetime import datetime

# Configuration
APP_NAME = "radiant-gorge-35079"
BATCH_SIZE = 5  # Number of MCQs per batch

def log(message, log_file):
    """Log a message to both console and log file"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"[{timestamp}] {message}"
    print(log_message)
    with open(log_file, "a") as f:
        f.write(log_message + "\n")

def upload_batch(batch, log_file, batch_num, total_batches):
    """Upload a single batch of MCQs"""
    log(f"Processing batch {batch_num}/{total_batches} with {len(batch)} MCQs...", log_file)
    
    # Create a simple import script
    script = """
import json
from django.db import transaction
from mcq.models import MCQ

# MCQs to import
mcqs_data = {mcqs_json}

# Track counts
created = 0
updated = 0
failed = 0

# Import in a transaction
with transaction.atomic():
    for mcq_data in mcqs_data:
        try:
            # Get key fields
            question = mcq_data.get('question_text', '')
            subspecialty = mcq_data.get('subspecialty', 'vascular_neurology')
            
            # Try to find existing MCQ
            existing = MCQ.objects.filter(question_text=question).first()
            
            if existing:
                # Update existing
                existing.options = mcq_data.get('options', {})
                existing.correct_answer = mcq_data.get('correct_answer', '')
                existing.explanation = mcq_data.get('explanation', '')
                existing.subspecialty = subspecialty
                existing.exam_year = mcq_data.get('exam_year', '')
                existing.exam_type = mcq_data.get('exam_type', '')
                existing.save()
                updated += 1
                print(f"Updated MCQ: {question[:30]}...")
            else:
                # Create new
                MCQ.objects.create(
                    question_text=question,
                    options=mcq_data.get('options', {}),
                    correct_answer=mcq_data.get('correct_answer', ''),
                    explanation=mcq_data.get('explanation', ''),
                    subspecialty=subspecialty,
                    exam_year=mcq_data.get('exam_year', ''),
                    exam_type=mcq_data.get('exam_type', '')
                )
                created += 1
                print(f"Created MCQ: {question[:30]}...")
        except Exception as e:
            failed += 1
            print(f"Error with MCQ: {str(e)}")

print(f"RESULTS: Created {created}, Updated {updated}, Failed {failed}")
"""
    
    # Replace the MCQs placeholder with actual data
    script = script.replace("{mcqs_json}", json.dumps(batch))
    
    # Write script to temp file
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.py')
    try:
        temp_file.write(script.encode('utf-8'))
        temp_file.close()
        
        # Upload script to Heroku
        log("Uploading import script to Heroku...", log_file)
        with open(temp_file.name, 'r') as f:
            result = subprocess.run(
                ["heroku", "run", f"cat > /tmp/mcq_import_{batch_num}.py", "--app", APP_NAME],
                stdin=f,
                capture_output=True,
                text=True,
                timeout=60  # 1 minute timeout
            )
        
        if result.returncode != 0:
            log(f"Error uploading script: {result.stderr}", log_file)
            return False
        
        # Execute script on Heroku
        log("Running import script on Heroku...", log_file)
        result = subprocess.run(
            ["heroku", "run", f"python -c 'exec(open(\"/tmp/mcq_import_{batch_num}.py\").read())'", "--app", APP_NAME],
            capture_output=True,
            text=True,
            timeout=90  # 1.5 minute timeout
        )
        
        if result.stdout:
            log(f"Output: {result.stdout}", log_file)
        
        if result.stderr:
            log(f"Errors: {result.stderr}", log_file)
        
        if result.returncode != 0:
            log("Import failed", log_file)
            return False
        
        log("Batch import successful", log_file)
        return True
        
    except subprocess.TimeoutExpired:
        log("Command timed out - connection issue", log_file)
        return False
    except Exception as e:
        log(f"Unexpected error: {str(e)}", log_file)
        return False
    finally:
        # Clean up temp file
        if os.path.exists(temp_file.name):
            os.unlink(temp_file.name)

def main():
    if len(sys.argv) < 2:
        print("Usage: python robust_upload.py <chunk_file> [start_pos]")
        print("  chunk_file: Path to the MCQ chunk file to upload")
        print("  start_pos: Optional starting position (to resume an interrupted upload)")
        sys.exit(1)
    
    chunk_file = sys.argv[1]
    start_pos = 0
    
    # If provided, use the starting position
    if len(sys.argv) >= 3:
        try:
            start_pos = int(sys.argv[2])
        except ValueError:
            print(f"Invalid start position: {sys.argv[2]}")
            sys.exit(1)
    
    # Set up logging
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = f"upload_{os.path.basename(chunk_file)}_{timestamp}.log"
    
    # Load MCQs from the chunk file
    try:
        with open(chunk_file, 'r') as f:
            mcqs = json.load(f)
        
        log(f"Loaded {len(mcqs)} MCQs from {chunk_file}", log_file)
        
        # Split into batches
        batches = []
        for i in range(0, len(mcqs), BATCH_SIZE):
            batches.append(mcqs[i:i+BATCH_SIZE])
        
        log(f"Split into {len(batches)} batches of approximately {BATCH_SIZE} MCQs each", log_file)
        
        # Process batches from the starting position
        if start_pos > 0:
            log(f"Resuming from batch {start_pos+1}", log_file)
        
        for i in range(start_pos, len(batches)):
            log(f"Starting batch {i+1} of {len(batches)}", log_file)
            
            # Try multiple times if needed
            max_retries = 3
            success = False
            
            for retry in range(max_retries):
                if retry > 0:
                    log(f"Retry {retry} for batch {i+1}", log_file)
                
                success = upload_batch(batches[i], log_file, i+1, len(batches))
                if success:
                    break
                
                # Wait between retries
                if retry < max_retries - 1:
                    retry_wait = 10  # seconds
                    log(f"Waiting {retry_wait} seconds before retry...", log_file)
                    time.sleep(retry_wait)
            
            if not success:
                log(f"Failed to upload batch {i+1} after {max_retries} attempts", log_file)
                log(f"To resume from this point later, run:", log_file)
                log(f"python robust_upload.py {chunk_file} {i}", log_file)
                return
            
            # Wait between batches
            if i < len(batches) - 1:
                batch_wait = 5  # seconds
                log(f"Waiting {batch_wait} seconds before next batch...", log_file)
                time.sleep(batch_wait)
        
        log("All batches processed successfully!", log_file)
        
    except Exception as e:
        log(f"Error: {str(e)}", log_file)
        return

if __name__ == "__main__":
    main()