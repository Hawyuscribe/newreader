#!/usr/bin/env python3
import json
import os
import subprocess
import tempfile
import sys
from datetime import datetime

# Configure paths and settings
JSON_FILE = '/Users/tariqalmatrudi/Documents/MCQs for the board/test/json f/vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json'
OUTPUT_DIR = os.path.expanduser("~/Desktop/vascular_mcq_upload")
HEROKU_APP = "mcq-reader"
CHUNK_SIZE = 20

# Make sure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Initialize logging
log_file = os.path.join(OUTPUT_DIR, f"preparation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

def log(message):
    """Write message to log file and print to console."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"{timestamp} - {message}"
    print(log_message)
    with open(log_file, 'a') as f:
        f.write(log_message + '\n')

def load_mcqs():
    """Load MCQs from the source JSON file."""
    log(f"Loading MCQs from: {JSON_FILE}")
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

def format_mcqs(mcqs):
    """Format MCQs for Django model."""
    formatted = []
    for mcq in mcqs:
        formatted.append({
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
        })
    log(f"Formatted {len(formatted)} MCQs for Django")
    return formatted

def create_chunks(mcqs):
    """Split MCQs into manageable chunks."""
    chunks = []
    for i in range(0, len(mcqs), CHUNK_SIZE):
        chunks.append(mcqs[i:i+CHUNK_SIZE])
    log(f"Created {len(chunks)} chunks of up to {CHUNK_SIZE} MCQs each")
    return chunks

def save_chunks(chunks):
    """Save MCQ chunks to JSON files."""
    chunk_dir = os.path.join(OUTPUT_DIR, "chunks")
    os.makedirs(chunk_dir, exist_ok=True)
    
    for i, chunk in enumerate(chunks):
        chunk_file = os.path.join(chunk_dir, f"vascular_chunk_{i+1:02d}_of_{len(chunks):02d}.json")
        with open(chunk_file, 'w') as f:
            json.dump(chunk, f, indent=2)
        log(f"Saved chunk {i+1}/{len(chunks)} ({len(chunk)} MCQs) to {os.path.basename(chunk_file)}")
    
    # Create manifest
    manifest = {
        "total_chunks": len(chunks),
        "total_mcqs": sum(len(chunk) for chunk in chunks),
        "chunks": [f"vascular_chunk_{i+1:02d}_of_{len(chunks):02d}.json" for i in range(len(chunks))]
    }
    
    manifest_file = os.path.join(chunk_dir, "manifest.json")
    with open(manifest_file, 'w') as f:
        json.dump(manifest, f, indent=2)
    
    log(f"Saved chunk manifest to {os.path.basename(manifest_file)}")
    return chunk_dir

def create_import_script():
    """Create Python script for importing MCQs on Heroku."""
    script = """
import json
import sys
from mcq.models import MCQ

# Load MCQs from JSON file
with open(sys.argv[1], 'r') as f:
    mcqs = json.load(f)

print(f"Processing {len(mcqs)} MCQs")

# Track success and errors
success_count = 0
error_count = 0
errors = []

for i, mcq_data in enumerate(mcqs):
    try:
        # Extract fields
        question_text = mcq_data.get('question_text', '')
        options = mcq_data.get('options', {})
        correct_answer = mcq_data.get('correct_answer', '')
        explanation = mcq_data.get('explanation', '')
        subspecialty = mcq_data.get('subspecialty', 'vascular_neurology')
        exam_year = mcq_data.get('exam_year', '')
        exam_type = mcq_data.get('exam_type', '')
        
        # Check if the MCQ already exists
        if MCQ.objects.filter(question_text=question_text).exists():
            print(f"MCQ already exists: {question_text[:30]}...")
            error_count += 1
            errors.append(f"Duplicate: {question_text[:30]}...")
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
        print(f"Saved MCQ {i+1}: {question_text[:30]}...")
    
    except Exception as e:
        error_count += 1
        errors.append(str(e))
        print(f"Error processing MCQ {i+1}: {str(e)}")

# Print summary
print(f"\\nRESULTS:")
print(f"Successfully imported: {success_count} MCQs")
print(f"Failed to import: {error_count} MCQs")

if errors:
    print("\\nErrors:")
    for error in errors[:5]:
        print(f" - {error}")
    if len(errors) > 5:
        print(f" - ...and {len(errors) - 5} more errors")
"""
    
    script_file = os.path.join(OUTPUT_DIR, "import_mcqs.py")
    with open(script_file, 'w') as f:
        f.write(script)
    
    log(f"Created import script: {os.path.basename(script_file)}")
    return script_file

def create_upload_script(chunk_dir):
    """Create bash script for uploading MCQs to Heroku."""
    script = f"""#!/bin/bash
# Script to upload vascular MCQs to Heroku
# Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

APP_NAME="{HEROKU_APP}"
CHUNK_DIR="{chunk_dir}"
SCRIPT_FILE="{os.path.join(OUTPUT_DIR, 'import_mcqs.py')}"
LOG_FILE="{os.path.join(OUTPUT_DIR, 'upload.log')}"

# Initialize log
echo "Vascular MCQ Upload to Heroku - Started at $(date)" > "$LOG_FILE"

# Function to log messages
log() {{
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> "$LOG_FILE"
}}

# Check current MCQ count
log "Checking current MCQ count on Heroku..."
heroku run "cd django_neurology_mcq && python -c \\"from mcq.models import MCQ; print(f'Total MCQs: {{MCQ.objects.count()}}'); print(f'Vascular MCQs: {{MCQ.objects.filter(subspecialty=\\\\\\"vascular_neurology\\\\\\").count()}}');\\"" --app "$APP_NAME" 2>&1 | tee -a "$LOG_FILE"

# Create temp directory on Heroku
log "Creating temporary directory on Heroku..."
heroku run "mkdir -p /tmp/mcq_upload" --app "$APP_NAME" 2>&1 | tee -a "$LOG_FILE"

# Upload import script
log "Uploading import script..."
cat "$SCRIPT_FILE" | heroku run "cat > /tmp/mcq_upload/import_mcqs.py" --app "$APP_NAME" 2>&1 | tee -a "$LOG_FILE"

# Process each chunk
for CHUNK_FILE in "$CHUNK_DIR"/*.json; do
    if [[ "$CHUNK_FILE" == *manifest.json ]]; then
        continue
    fi
    
    CHUNK_NAME=$(basename "$CHUNK_FILE")
    log "Processing chunk: $CHUNK_NAME"
    
    # Upload chunk file
    log "Uploading chunk file..."
    cat "$CHUNK_FILE" | heroku run "cat > /tmp/mcq_upload/$CHUNK_NAME" --app "$APP_NAME" 2>&1 | tee -a "$LOG_FILE"
    
    # Import MCQs
    log "Importing MCQs from $CHUNK_NAME..."
    heroku run "cd django_neurology_mcq && python /tmp/mcq_upload/import_mcqs.py /tmp/mcq_upload/$CHUNK_NAME" --app "$APP_NAME" 2>&1 | tee -a "$LOG_FILE"
    
    log "Finished processing $CHUNK_NAME"
    log "Waiting 5 seconds before next chunk..."
    sleep 5
done

# Verify final MCQ count
log "Checking final MCQ count on Heroku..."
heroku run "cd django_neurology_mcq && python -c \\"from mcq.models import MCQ; print(f'Final Total MCQs: {{MCQ.objects.count()}}'); print(f'Final Vascular MCQs: {{MCQ.objects.filter(subspecialty=\\\\\\"vascular_neurology\\\\\\").count()}}');\\"" --app "$APP_NAME" 2>&1 | tee -a "$LOG_FILE"

log "Upload process complete!"
echo "=================================================="
echo "Vascular MCQ upload script has finished!"
echo "Check the log file for details: $LOG_FILE"
echo "=================================================="
"""
    
    script_file = os.path.join(OUTPUT_DIR, "upload_to_heroku.sh")
    with open(script_file, 'w') as f:
        f.write(script)
    
    # Make executable
    os.chmod(script_file, 0o755)
    
    log(f"Created upload script: {os.path.basename(script_file)}")
    return script_file

def create_quick_fix_script():
    """Create a script to fix Heroku app issues."""
    script = f"""#!/bin/bash
# Script to fix Heroku app issues and configure for MCQ import
# Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

APP_NAME="{HEROKU_APP}"
LOG_FILE="{os.path.join(OUTPUT_DIR, 'heroku_fix.log')}"

# Initialize log
echo "Heroku App Fix - Started at $(date)" > "$LOG_FILE"

# Function to log messages
log() {{
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> "$LOG_FILE"
}}

# Check app status
log "Checking Heroku app status..."
heroku apps:info --app "$APP_NAME" 2>&1 | tee -a "$LOG_FILE"

# Check if PostgreSQL is provisioned
log "Checking PostgreSQL..."
if ! heroku addons --app "$APP_NAME" | grep -q "postgresql"; then
    log "PostgreSQL not found. Attempting to provision..."
    heroku addons:create heroku-postgresql:mini --app "$APP_NAME" 2>&1 | tee -a "$LOG_FILE"
else
    log "PostgreSQL already provisioned"
fi

# Set environment variables
log "Setting environment variables..."
heroku config:set DJANGO_SETTINGS_MODULE=neurology_mcq.settings --app "$APP_NAME" 2>&1 | tee -a "$LOG_FILE"
heroku config:set PYTHONPATH=django_neurology_mcq --app "$APP_NAME" 2>&1 | tee -a "$LOG_FILE"

# Scale dynos
log "Attempting to scale dynos..."
heroku ps:scale web=1 --app "$APP_NAME" 2>&1 | tee -a "$LOG_FILE"

# Run migrations
log "Running migrations..."
heroku run "cd django_neurology_mcq && python manage.py migrate" --app "$APP_NAME" 2>&1 | tee -a "$LOG_FILE"

log "Heroku app setup complete!"
echo "=================================================="
echo "Heroku app setup complete!"
echo "Check the log file for details: $LOG_FILE"
echo "Next step: Run the upload script to import MCQs"
echo "=================================================="
"""
    
    script_file = os.path.join(OUTPUT_DIR, "fix_heroku_app.sh")
    with open(script_file, 'w') as f:
        f.write(script)
    
    # Make executable
    os.chmod(script_file, 0o755)
    
    log(f"Created Heroku fix script: {os.path.basename(script_file)}")
    return script_file

def create_readme():
    """Create README file with instructions."""
    readme = f"""# Vascular MCQ Upload to Heroku

This package contains scripts and data for uploading vascular neurology MCQs to the Heroku app.

## Files

- `chunks/`: Directory containing MCQ chunks in JSON format
- `import_mcqs.py`: Python script for importing MCQs into Django
- `fix_heroku_app.sh`: Script to fix and configure the Heroku app
- `upload_to_heroku.sh`: Script to upload MCQs to Heroku
- `preparation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log`: Log file from the preparation process

## Instructions

1. First, run the fix script to ensure the Heroku app is properly configured:

```bash
./fix_heroku_app.sh
```

2. Then, run the upload script to import the MCQs:

```bash
./upload_to_heroku.sh
```

3. Monitor the progress in the terminal or check the log files:

```bash
tail -f upload.log
```

## Details

- Total MCQs: {len(load_mcqs())}
- Chunk size: {CHUNK_SIZE} MCQs per chunk
- Heroku app: {HEROKU_APP}

## Notes

- The upload script processes one chunk at a time
- There's a 5-second pause between chunks to avoid overloading the server
- If the upload is interrupted, you can restart it, and duplicate MCQs will be skipped

Created on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
    
    readme_file = os.path.join(OUTPUT_DIR, "README.md")
    with open(readme_file, 'w') as f:
        f.write(readme)
    
    log(f"Created README file")
    return readme_file

def main():
    """Main function to create the uploader package."""
    start_time = datetime.now()
    log(f"=== Starting uploader preparation at {start_time} ===")
    
    # Load and format MCQs
    mcqs_raw = load_mcqs()
    if not mcqs_raw:
        log("Error: No MCQs loaded. Exiting.")
        return 1
    
    mcqs = format_mcqs(mcqs_raw)
    
    # Create chunks
    chunks = create_chunks(mcqs)
    
    # Save chunks
    chunk_dir = save_chunks(chunks)
    
    # Create import script
    import_script = create_import_script()
    
    # Create upload script
    upload_script = create_upload_script(chunk_dir)
    
    # Create fix script
    fix_script = create_quick_fix_script()
    
    # Create README
    readme = create_readme()
    
    # Finished
    end_time = datetime.now()
    duration = end_time - start_time
    log(f"=== Uploader preparation completed at {end_time} ===")
    log(f"Duration: {duration}")
    log(f"Created uploader package at: {OUTPUT_DIR}")
    log(f"To use, run:")
    log(f"  1. ./fix_heroku_app.sh")
    log(f"  2. ./upload_to_heroku.sh")
    
    print("\n================================================")
    print(f"Uploader package created at: {OUTPUT_DIR}")
    print(f"To upload the vascular MCQs to Heroku:")
    print(f"  1. cd {OUTPUT_DIR}")
    print(f"  2. ./fix_heroku_app.sh")
    print(f"  3. ./upload_to_heroku.sh")
    print("================================================")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())