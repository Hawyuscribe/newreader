#!/usr/bin/env python3
"""
Final, ultra-reliable script to upload vascular MCQs to Heroku
Uploads a single tiny batch at a time to avoid all connection issues
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
HEROKU_TIMEOUT = 60  # Timeout in seconds for Heroku commands

def upload_single_batch(mcqs, app_name=APP_NAME):
    """Upload a single MCQ batch (must be small, just 1-3 MCQs)"""
    print(f"Uploading batch of {len(mcqs)} MCQs...")
    
    # Create a temp directory
    temp_dir = tempfile.mkdtemp()
    batch_file = os.path.join(temp_dir, "batch.json")
    
    # Save MCQs to temp file
    with open(batch_file, 'w') as f:
        json.dump(mcqs, f, indent=2)
    
    # First check if we can connect to Heroku
    try:
        result = subprocess.run(
            ["heroku", "apps:info", "--app", app_name],
            capture_output=True,
            text=True,
            timeout=HEROKU_TIMEOUT
        )
        if result.returncode != 0:
            print(f"Error connecting to Heroku: {result.stderr}")
            return False
        print("Successfully connected to Heroku app")
    except Exception as e:
        print(f"Connection test failed: {str(e)}")
        return False
    
    try:
        # Upload the batch file to Heroku
        print("Uploading batch file...")
        with open(batch_file, 'r') as f:
            result = subprocess.run(
                ["heroku", "run", "cat > /tmp/current_batch.json", "--app", app_name],
                stdin=f,
                capture_output=True,
                text=True,
                timeout=HEROKU_TIMEOUT
            )
        
        if result.returncode != 0:
            print(f"Error uploading batch file: {result.stderr}")
            return False
        
        # Create an import script that can safely handle duplicates
        import_script = """
import json
import os
from django.db import transaction
from mcq.models import MCQ

# Load MCQs from file
try:
    with open('/tmp/current_batch.json', 'r') as f:
        mcqs = json.load(f)
    
    print(f"Processing {len(mcqs)} MCQs")
    
    # Track imports
    created = 0
    updated = 0
    skipped = 0
    
    # Process each MCQ
    for mcq_data in mcqs:
        question = mcq_data.get('question_text', '')
        if not question:
            print("Skipping MCQ with no question text")
            skipped += 1
            continue
        
        # Check if MCQ already exists
        existing = MCQ.objects.filter(question_text=question).first()
        
        if existing:
            # Only update if subspecialty is vascular_neurology
            if existing.subspecialty != 'vascular_neurology' and mcq_data.get('subspecialty') == 'vascular_neurology':
                existing.subspecialty = 'vascular_neurology'
                existing.options = mcq_data.get('options', {})
                existing.correct_answer = mcq_data.get('correct_answer', '')
                existing.explanation = mcq_data.get('explanation', '')
                existing.exam_year = mcq_data.get('exam_year', '')
                existing.exam_type = mcq_data.get('exam_type', '')
                existing.save()
                updated += 1
                print(f"Updated: {question[:30]}...")
            else:
                print(f"Skipped (already exists): {question[:30]}...")
                skipped += 1
        else:
            # Create new MCQ
            new_mcq = MCQ(
                question_text=question,
                options=mcq_data.get('options', {}),
                correct_answer=mcq_data.get('correct_answer', ''),
                explanation=mcq_data.get('explanation', ''),
                subspecialty=mcq_data.get('subspecialty', 'vascular_neurology'),
                exam_year=mcq_data.get('exam_year', ''),
                exam_type=mcq_data.get('exam_type', '')
            )
            new_mcq.save()
            created += 1
            print(f"Created: {question[:30]}...")
    
    print(f"Results: Created {created}, Updated {updated}, Skipped {skipped}")
except Exception as e:
    print(f"Error: {str(e)}")
"""
        
        # Upload the import script
        script_file = os.path.join(temp_dir, "import.py")
        with open(script_file, 'w') as f:
            f.write(import_script)
        
        print("Uploading import script...")
        with open(script_file, 'r') as f:
            result = subprocess.run(
                ["heroku", "run", "cat > /tmp/import_mcq.py", "--app", app_name],
                stdin=f,
                capture_output=True,
                text=True,
                timeout=HEROKU_TIMEOUT
            )
        
        if result.returncode != 0:
            print(f"Error uploading import script: {result.stderr}")
            return False
        
        # Run the import script
        print("Running import script...")
        result = subprocess.run(
            ["heroku", "run", "python -c 'exec(open(\"/tmp/import_mcq.py\").read())'", "--app", app_name],
            capture_output=True,
            text=True,
            timeout=HEROKU_TIMEOUT
        )
        
        if result.stdout:
            print("Output:")
            for line in result.stdout.splitlines():
                print(f"  {line}")
        
        if result.stderr:
            print("Errors:")
            for line in result.stderr.splitlines():
                print(f"  {line}")
        
        if result.returncode != 0:
            print("Import failed")
            return False
        
        print("Import successful!")
        return True
        
    finally:
        # Clean up temp files
        if os.path.exists(batch_file):
            os.unlink(batch_file)
        if os.path.exists(script_file):
            os.unlink(script_file)
        os.rmdir(temp_dir)

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python final_uploader.py chunk <chunk_file> <start_index> <count>")
        print("    chunk_file: Path to the MCQ JSON file")
        print("    start_index: Index to start from (0-based)")
        print("    count: Number of MCQs to upload (default: 3)")
        print("")
        print("  python final_uploader.py chunks <chunks_dir> <chunk_number>")
        print("    chunks_dir: Directory containing chunk files")
        print("    chunk_number: Number of the chunk to process (1-based)")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "chunk":
        if len(sys.argv) < 4:
            print("Missing arguments for 'chunk' command")
            sys.exit(1)
        
        chunk_file = sys.argv[2]
        start_index = int(sys.argv[3])
        count = 3  # Default to 3 MCQs
        
        if len(sys.argv) >= 5:
            count = int(sys.argv[4])
        
        # Load MCQs from file
        with open(chunk_file, 'r') as f:
            all_mcqs = json.load(f)
        
        # Extract the batch
        end_index = min(start_index + count, len(all_mcqs))
        batch = all_mcqs[start_index:end_index]
        
        print(f"Processing {len(batch)} MCQs from {chunk_file} (indexes {start_index}-{end_index-1})")
        
        # Upload the batch
        success = upload_single_batch(batch)
        
        if success:
            print("Batch upload successful!")
            print(f"To continue, run: python final_uploader.py chunk {chunk_file} {end_index} {count}")
        else:
            print("Batch upload failed")
            print(f"To retry, run: python final_uploader.py chunk {chunk_file} {start_index} {count}")
    
    elif command == "chunks":
        if len(sys.argv) < 4:
            print("Missing arguments for 'chunks' command")
            sys.exit(1)
        
        chunks_dir = sys.argv[2]
        chunk_number = int(sys.argv[3])
        
        # Find the chunk file
        chunk_files = []
        for filename in os.listdir(chunks_dir):
            if filename.startswith("vascular_chunk_") and filename.endswith(".json") and "manifest" not in filename:
                chunk_files.append(os.path.join(chunks_dir, filename))
        
        # Sort chunk files
        chunk_files.sort()
        
        if chunk_number < 1 or chunk_number > len(chunk_files):
            print(f"Invalid chunk number. Must be between 1 and {len(chunk_files)}")
            sys.exit(1)
        
        # Get the specified chunk file
        chunk_file = chunk_files[chunk_number - 1]
        
        print(f"Processing chunk {chunk_number}/{len(chunk_files)}: {os.path.basename(chunk_file)}")
        
        # Load MCQs from the chunk file
        with open(chunk_file, 'r') as f:
            mcqs = json.load(f)
        
        print(f"Chunk contains {len(mcqs)} MCQs")
        print(f"To process this chunk in small batches, run:")
        print(f"python final_uploader.py chunk {chunk_file} 0 3")
    
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)

if __name__ == "__main__":
    main()