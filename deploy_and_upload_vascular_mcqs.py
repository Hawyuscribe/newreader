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
CHUNK_SIZE = 20
HEROKU_APP_NAME = 'mcq-reader'
LOG_FILE = f'vascular_upload_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'

# Setup logging
def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"{timestamp} - {message}"
    print(log_message)
    with open(LOG_FILE, 'a') as f:
        f.write(log_message + '\n')

def run_command(command, description=None):
    """Run a shell command and return result."""
    if description:
        log(description)
    
    try:
        process = subprocess.run(
            command, 
            shell=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE,
            text=True
        )
        if process.returncode != 0:
            log(f"Command failed: {process.stderr}")
            return None
        return process.stdout
    except Exception as e:
        log(f"Error running command: {str(e)}")
        return None

def run_heroku_command(command, description=None):
    """Run a command on Heroku."""
    return run_command(f"heroku {command} --app {HEROKU_APP_NAME}", description)

def load_mcqs():
    """Load MCQs from JSON file."""
    log(f"Loading MCQs from {JSON_FILE}")
    try:
        with open(JSON_FILE, 'r') as f:
            data = json.load(f)
        
        # Handle different JSON structures
        if isinstance(data, dict) and 'mcqs' in data:
            mcqs = data['mcqs']
        elif isinstance(data, list):
            mcqs = data
        else:
            log(f"Unexpected JSON structure: {type(data)}")
            return []
        
        log(f"Successfully loaded {len(mcqs)} MCQs")
        return mcqs
    except Exception as e:
        log(f"Error loading MCQs: {str(e)}")
        return []

def format_mcq(mcq):
    """Format MCQ for Django model."""
    # Get fields from source format
    options = {
        'option_a': mcq.get('Option A', ''),
        'option_b': mcq.get('Option B', ''),
        'option_c': mcq.get('Option C', ''),
        'option_d': mcq.get('Option D', ''),
        'option_e': mcq.get('Option E', '')
    }
    
    # Create Django-compatible MCQ
    return {
        'question_text': mcq.get('Question Text', ''),
        'options': options,
        'correct_answer': mcq.get('Correct Answer', 'A'),
        'explanation': mcq.get('Explanation', ''),
        'subspecialty': 'vascular_neurology',
        'exam_year': mcq.get('Exam Year', '2025'),
        'exam_type': mcq.get('Exam Type', 'Unknown')
    }

def prepare_chunks(mcqs):
    """Split MCQs into manageable chunks."""
    formatted_mcqs = [format_mcq(mcq) for mcq in mcqs]
    chunks = [formatted_mcqs[i:i+CHUNK_SIZE] for i in range(0, len(formatted_mcqs), CHUNK_SIZE)]
    log(f"Prepared {len(chunks)} chunks of up to {CHUNK_SIZE} MCQs each")
    return chunks

def verify_app_setup():
    """Verify Heroku app is set up correctly."""
    log("Verifying Heroku app setup")
    
    # Check if app exists
    result = run_heroku_command("apps:info", "Checking app info")
    if not result:
        log("Error: Could not get app info")
        return False
    
    # Check if dynos are running
    result = run_heroku_command("ps", "Checking dynos")
    if "No dynos" in result:
        log("Warning: No dynos running. Attempting to scale web dyno...")
        run_heroku_command("ps:scale web=1", "Scaling web dyno to 1")
    
    # Check PostgreSQL
    result = run_heroku_command("pg:info", "Checking PostgreSQL")
    if not result or "Add-on not found" in result:
        log("Warning: PostgreSQL not found. Attempting to provision...")
        run_heroku_command("addons:create heroku-postgresql:hobby-dev", "Provisioning PostgreSQL")
    
    log("App verification complete")
    return True

def create_mcq_import_command(chunk, chunk_number):
    """Create a Python script to import a chunk of MCQs."""
    script = f"""
import json
from mcq.models import MCQ

# MCQs to import
mcqs_data = {json.dumps(chunk)}
print(f"Processing {len(mcqs_data)} MCQs in chunk {chunk_number}")

# Track results
success_count = 0
error_count = 0
errors = []

# Process each MCQ
for i, mcq_data in enumerate(mcqs_data):
    try:
        # Extract fields
        question_text = mcq_data['question_text']
        options = mcq_data['options']
        correct_answer = mcq_data['correct_answer']
        explanation = mcq_data['explanation']
        subspecialty = mcq_data['subspecialty']
        exam_year = mcq_data['exam_year']
        exam_type = mcq_data['exam_type']
        
        # Check if question already exists
        if MCQ.objects.filter(question_text=question_text).exists():
            print(f"MCQ already exists: {{question_text[:30]}}...")
            error_count += 1
            errors.append(f"Duplicate: {{question_text[:30]}}...")
            continue
        
        # Create and save MCQ
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
        success_count += 1
        print(f"Saved MCQ {{i+1}}/{{len(mcqs_data)}}: {{question_text[:30]}}...")
    
    except Exception as e:
        error_count += 1
        error_msg = f"Error: {{str(e)}}"
        errors.append(error_msg)
        print(error_msg)

# Print summary
print("\\nRESULTS:")
print(f"Successfully imported: {{success_count}} MCQs")
print(f"Failed to import: {{error_count}} MCQs")

if errors:
    print("\\nErrors:")
    for e in errors[:5]:
        print(f" - {{e}}")
    if len(errors) > 5:
        print(f" - ...and {{len(errors) - 5}} more errors")

# Print marker for parsing
print(f"IMPORT_MARKER:{{success_count}},{{error_count}}")
"""
    return script

def upload_mcq_chunk(chunk, chunk_number):
    """Upload a chunk of MCQs to Heroku using Django shell."""
    log(f"Uploading chunk {chunk_number} ({len(chunk)} MCQs)")
    
    # Create temporary script file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as temp_file:
        temp_file.write(create_mcq_import_command(chunk, chunk_number))
        script_path = temp_file.name
    
    try:
        # Run the script on Heroku
        command = f"cat {script_path} | heroku run --app {HEROKU_APP_NAME} 'cd django_neurology_mcq && python manage.py shell'"
        result = run_command(command, f"Running import for chunk {chunk_number}")
        
        # Parse results
        if result:
            for line in result.splitlines():
                if "IMPORT_MARKER:" in line:
                    parts = line.split("IMPORT_MARKER:")[1].split(",")
                    if len(parts) == 2:
                        success = int(parts[0])
                        errors = int(parts[1])
                        log(f"Chunk {chunk_number} results: {success} successful, {errors} failed")
                        return success, errors
        
        log(f"Could not parse results for chunk {chunk_number}")
        return 0, len(chunk)
    finally:
        # Clean up temporary file
        if os.path.exists(script_path):
            os.unlink(script_path)

def verify_mcq_count():
    """Verify the number of MCQs in the database."""
    script = """
from mcq.models import MCQ

# Count MCQs
total_count = MCQ.objects.count()
vascular_count = MCQ.objects.filter(subspecialty='vascular_neurology').count()

print(f"Total MCQs in database: {total_count}")
print(f"Vascular neurology MCQs: {vascular_count}")

# Get sample
if vascular_count > 0:
    print("\\nSample vascular MCQs:")
    sample = MCQ.objects.filter(subspecialty='vascular_neurology').order_by('-id')[:3]
    for i, mcq in enumerate(sample):
        print(f"{i+1}. {mcq.question_text[:50]}...")
        print(f"   Answer: {mcq.correct_answer}")

print("COUNT_MARKER:{total_count},{vascular_count}")
"""
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as temp_file:
        temp_file.write(script)
        script_path = temp_file.name
    
    try:
        command = f"cat {script_path} | heroku run --app {HEROKU_APP_NAME} 'cd django_neurology_mcq && python manage.py shell'"
        result = run_command(command, "Verifying MCQ count")
        
        if result:
            log("\nVerification results:")
            for line in result.splitlines():
                if not line.startswith("Running") and not line.startswith("[G["):
                    log(line)
                if "COUNT_MARKER:" in line:
                    parts = line.split("COUNT_MARKER:")[1].split(",")
                    if len(parts) == 2:
                        total = int(parts[0])
                        vascular = int(parts[1])
                        log(f"Verified counts - Total: {total}, Vascular: {vascular}")
                        return total, vascular
        
        log("Could not verify MCQ count")
        return 0, 0
    finally:
        if os.path.exists(script_path):
            os.unlink(script_path)

def main():
    start_time = datetime.now()
    log(f"=== Starting Vascular MCQ Upload at {start_time} ===")
    
    # Create output log file
    with open(LOG_FILE, 'w') as f:
        f.write(f"Vascular MCQ Upload Log - Started at {start_time}\n")
    
    # Verify app setup
    if not verify_app_setup():
        log("App setup verification failed. Exiting.")
        return
    
    # Load MCQs
    mcqs = load_mcqs()
    if not mcqs:
        log("No MCQs to upload. Exiting.")
        return
    
    # Check initial MCQ count
    initial_total, initial_vascular = verify_mcq_count()
    log(f"Initial MCQ counts - Total: {initial_total}, Vascular: {initial_vascular}")
    
    # Prepare chunks
    chunks = prepare_chunks(mcqs)
    
    # Upload chunks
    total_success = 0
    total_errors = 0
    
    for i, chunk in enumerate(chunks):
        chunk_number = i + 1
        log(f"Processing chunk {chunk_number} of {len(chunks)}")
        
        # Upload chunk
        success, errors = upload_mcq_chunk(chunk, chunk_number)
        total_success += success
        total_errors += errors
        
        # Allow some time between chunks
        if i < len(chunks) - 1:
            log("Waiting 5 seconds before next chunk...")
            time.sleep(5)
    
    # Final verification
    final_total, final_vascular = verify_mcq_count()
    vascular_added = final_vascular - initial_vascular
    
    # Log summary
    end_time = datetime.now()
    duration = end_time - start_time
    log(f"=== Upload completed at {end_time} ===")
    log(f"Duration: {duration}")
    log(f"Total MCQs processed: {len(mcqs)}")
    log(f"Successfully uploaded: {total_success}")
    log(f"Failed to upload: {total_errors}")
    log(f"Vascular MCQs before: {initial_vascular}")
    log(f"Vascular MCQs after: {final_vascular}")
    log(f"Vascular MCQs added: {vascular_added}")

if __name__ == "__main__":
    main()