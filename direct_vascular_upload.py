#!/usr/bin/env python3
import json
import os
import subprocess
import sys
import time
import tempfile
from datetime import datetime

# Configuration
JSON_FILE = '/Users/tariqalmatrudi/Documents/MCQs for the board/test/json f/vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json'
APP_NAME = 'mcq-reader'
CHUNK_SIZE = 20
LOG_FILE = f'vascular_upload_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'

# Set up logging
def log(message):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    line = f"[{timestamp}] {message}"
    print(line)
    with open(LOG_FILE, 'a') as f:
        f.write(line + '\n')

def run_command(cmd):
    """Run a shell command and return its output."""
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return result.stdout
    except Exception as e:
        log(f"Error running command: {e}")
        return None

def load_mcqs():
    """Load MCQs from the source JSON file."""
    log(f"Loading MCQs from {JSON_FILE}")
    try:
        with open(JSON_FILE, 'r') as f:
            data = json.load(f)
        
        # Check different JSON structures
        if isinstance(data, dict) and 'mcqs' in data:
            mcqs = data['mcqs']
        elif isinstance(data, list):
            mcqs = data
        else:
            log(f"Unknown JSON structure in {JSON_FILE}")
            return []
        
        log(f"Successfully loaded {len(mcqs)} MCQs")
        return mcqs
    except Exception as e:
        log(f"Error loading MCQs: {e}")
        return []

def format_mcq(mcq):
    """Format MCQ for Django model."""
    return {
        'question_text': mcq.get('Question Text', ''),
        'options': {
            'option_a': mcq.get('Option A', ''),
            'option_b': mcq.get('Option B', ''),
            'option_c': mcq.get('Option C', ''),
            'option_d': mcq.get('Option D', ''),
            'option_e': mcq.get('Option E', '')
        },
        'correct_answer': mcq.get('Correct Answer', 'A'),
        'explanation': mcq.get('Explanation', ''),
        'subspecialty': 'vascular_neurology',
        'exam_year': mcq.get('Exam Year', '2025'),
        'exam_type': mcq.get('Exam Type', 'Unknown')
    }

def setup_heroku():
    """Configure Heroku app for MCQ uploads."""
    log("Setting up Heroku app")
    
    # Set environment variables
    run_command(f"heroku config:set DJANGO_SETTINGS_MODULE=neurology_mcq.settings --app {APP_NAME}")
    run_command(f"heroku config:set PYTHONPATH=django_neurology_mcq --app {APP_NAME}")
    
    # Check current state
    log("Checking current MCQ count")
    output = run_command(f"heroku run \"python -c 'import sys; sys.path.append(\\\".\\\")\; from mcq.models import MCQ\; print(MCQ.objects.count())'\" --app {APP_NAME}")
    if output:
        log(f"Current MCQ count: {output.strip()}")
    
    return True

def upload_mcq_chunk(chunk, chunk_num, total_chunks):
    """Upload a chunk of MCQs to Heroku."""
    log(f"Uploading chunk {chunk_num} of {total_chunks} ({len(chunk)} MCQs)")
    
    # Create a temporary file for the script
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.py') as script_file:
        script_file.write("""
import json
import sys
import os
import django

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
django.setup()

# Import the model
from mcq.models import MCQ

# Load the chunk from command line argument
chunk_data = json.loads(sys.argv[1])
print(f"Processing {len(chunk_data)} MCQs")

# Track results
success_count = 0
error_count = 0
errors = []

# Process each MCQ
for i, mcq_data in enumerate(chunk_data):
    try:
        # Get fields
        question_text = mcq_data.get('question_text', '')
        options = mcq_data.get('options', {})
        correct_answer = mcq_data.get('correct_answer', '')
        explanation = mcq_data.get('explanation', '')
        subspecialty = mcq_data.get('subspecialty', 'vascular_neurology')
        exam_year = mcq_data.get('exam_year', '')
        exam_type = mcq_data.get('exam_type', '')
        
        # Check if MCQ already exists
        if MCQ.objects.filter(question_text=question_text).exists():
            print(f"MCQ already exists: {question_text[:30]}...")
            error_count += 1
            errors.append(f"Duplicate: {question_text[:30]}...")
            continue
        
        # Create MCQ
        mcq = MCQ(
            question_text=question_text,
            options=options,
            correct_answer=correct_answer,
            explanation=explanation,
            subspecialty=subspecialty,
            exam_year=exam_year,
            exam_type=exam_type
        )
        
        # Save MCQ
        mcq.save()
        success_count += 1
        print(f"Saved MCQ {i+1}: {question_text[:30]}...")
    
    except Exception as e:
        error_count += 1
        errors.append(str(e))
        print(f"Error: {str(e)}")

# Print results
print("\\nResults:")
print(f"Successfully imported: {success_count} MCQs")
print(f"Failed to import: {error_count} MCQs")

if errors:
    print("\\nErrors:")
    for error in errors[:5]:
        print(f" - {error}")
    if len(errors) > 5:
        print(f" - ...and {len(errors) - 5} more errors")

print(f"RESULT_MARKER:{success_count},{error_count}")
""")
        script_path = script_file.name
    
    # Convert chunk to JSON string
    chunk_json = json.dumps(chunk)
    
    # Run the script on Heroku
    cmd = f"heroku run \"python -c \\\"$(cat {script_path})\\\" '{chunk_json}'\" --app {APP_NAME}"
    output = run_command(cmd)
    
    # Clean up
    os.unlink(script_path)
    
    # Process output
    if output:
        log(output)
        # Extract results
        for line in output.splitlines():
            if "RESULT_MARKER:" in line:
                parts = line.split("RESULT_MARKER:")[1].split(",")
                if len(parts) == 2:
                    return int(parts[0]), int(parts[1])
    
    log("Could not determine import results")
    return 0, len(chunk)

def verify_results():
    """Verify the MCQ count in the database."""
    log("Verifying final MCQ count")
    
    # Get total MCQ count
    cmd_total = f"heroku run \"python -c 'import sys; sys.path.append(\\\".\\\")\; from mcq.models import MCQ\; print(MCQ.objects.count())'\" --app {APP_NAME}"
    output_total = run_command(cmd_total)
    if output_total:
        total = output_total.strip()
    else:
        total = "unknown"
    
    # Get vascular MCQ count
    cmd_vascular = f"heroku run \"python -c 'import sys; sys.path.append(\\\".\\\")\; from mcq.models import MCQ\; print(MCQ.objects.filter(subspecialty=\\\"vascular_neurology\\\").count())'\" --app {APP_NAME}"
    output_vascular = run_command(cmd_vascular)
    if output_vascular:
        vascular = output_vascular.strip()
    else:
        vascular = "unknown"
    
    log(f"Final counts - Total MCQs: {total}, Vascular MCQs: {vascular}")
    return total, vascular

def main():
    # Initialize log file
    with open(LOG_FILE, 'w') as f:
        f.write(f"Vascular MCQ Upload Log - Started at {datetime.now()}\n")
    
    log("Starting vascular MCQ upload process")
    
    # Set up Heroku
    setup_heroku()
    
    # Load MCQs
    mcqs = load_mcqs()
    if not mcqs:
        log("Error: No MCQs found. Exiting.")
        return 1
    
    # Format MCQs for Django
    formatted_mcqs = [format_mcq(mcq) for mcq in mcqs]
    log(f"Formatted {len(formatted_mcqs)} MCQs for Django")
    
    # Create chunks
    chunks = [formatted_mcqs[i:i+CHUNK_SIZE] for i in range(0, len(formatted_mcqs), CHUNK_SIZE)]
    log(f"Created {len(chunks)} chunks of up to {CHUNK_SIZE} MCQs each")
    
    # Upload each chunk
    total_success = 0
    total_errors = 0
    
    for i, chunk in enumerate(chunks):
        chunk_num = i + 1
        log(f"Processing chunk {chunk_num} of {len(chunks)}")
        
        # Upload chunk
        success, errors = upload_mcq_chunk(chunk, chunk_num, len(chunks))
        total_success += success
        total_errors += errors
        
        log(f"Chunk {chunk_num} results: {success} successful, {errors} failed")
        
        # Sleep between chunks to avoid overwhelming Heroku
        if i < len(chunks) - 1:
            log("Waiting 5 seconds before next chunk...")
            time.sleep(5)
    
    # Verify results
    final_total, final_vascular = verify_results()
    
    # Log summary
    log("Upload process completed")
    log(f"Total MCQs processed: {len(formatted_mcqs)}")
    log(f"Successfully uploaded: {total_success}")
    log(f"Failed to upload: {total_errors}")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())