#!/bin/bash
# Script to upload a specific chunk of vascular MCQs to Heroku
# Uses a simplified approach to avoid timeouts
# Usage: ./batch_upload.sh <chunk_number>

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <chunk_number>"
    echo "Example: $0 7"
    exit 1
fi

CHUNK_NUM=$1

# Dynamically determine the current directory
CURRENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
APP_NAME="radiant-gorge-35079"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
LOG_FILE="${CURRENT_DIR}/chunk_${CHUNK_NUM}_upload_${TIMESTAMP}.log"

# Format chunk number with leading zero if needed
if [ $CHUNK_NUM -lt 10 ]; then
    CHUNK_NUM_FMT="0$CHUNK_NUM"
else
    CHUNK_NUM_FMT="$CHUNK_NUM"
fi

CHUNK_FILE="${CURRENT_DIR}/chunks/vascular_chunk_${CHUNK_NUM_FMT}_of_21.json"

if [ ! -f "$CHUNK_FILE" ]; then
    echo "ERROR: Chunk file not found: $CHUNK_FILE"
    exit 1
fi

# Initialize log
echo "Vascular MCQ Upload to Heroku (Chunk $CHUNK_NUM) - Started at $(date)" > "$LOG_FILE"

# Function to log messages
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> "$LOG_FILE"
}

log "Using chunk file: $CHUNK_FILE"

# Check if jq is installed (for counting objects in JSON files)
if command -v jq &> /dev/null; then
    MCQ_COUNT=$(jq 'length' "$CHUNK_FILE")
    log "Chunk contains $MCQ_COUNT MCQs"
else
    log "jq not installed, cannot count MCQs in chunk file"
fi

# Create a temporary directory for processing
TEMP_DIR=$(mktemp -d)
log "Created temporary directory: $TEMP_DIR"

# Create the import script
cat > "${TEMP_DIR}/import_script.py" << 'EOF'
import json
import sys
from django.db import transaction
from mcq.models import MCQ

# Load MCQs from JSON file
chunk_file = sys.argv[1]
print(f"Reading MCQs from {chunk_file}")

with open(chunk_file, 'r') as f:
    mcqs = json.load(f)

print(f"Processing {len(mcqs)} MCQs")

# Track success and errors
success_count = 0
update_count = 0
error_count = 0
errors = []

with transaction.atomic():
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
            try:
                existing_mcq = MCQ.objects.get(question_text=question_text)
                # Update existing MCQ
                existing_mcq.options = options
                existing_mcq.correct_answer = correct_answer
                existing_mcq.explanation = explanation
                existing_mcq.subspecialty = subspecialty
                existing_mcq.exam_year = exam_year
                existing_mcq.exam_type = exam_type
                existing_mcq.save()
                update_count += 1
                print(f"Updated MCQ {i+1}: {question_text[:30]}...")
            except MCQ.DoesNotExist:
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
                success_count += 1
                print(f"Created MCQ {i+1}: {question_text[:30]}...")
        
        except Exception as e:
            error_count += 1
            errors.append(str(e))
            print(f"Error processing MCQ {i+1}: {str(e)}")

# Print summary
print(f"\nRESULTS:")
print(f"Successfully created: {success_count} MCQs")
print(f"Successfully updated: {update_count} MCQs")
print(f"Failed to import: {error_count} MCQs")

if errors:
    print("\nErrors:")
    for error in errors[:5]:
        print(f" - {error}")
    if len(errors) > 5:
        print(f" - ...and {len(errors) - 5} more errors")
EOF
log "Created import script"

# Copy chunk file to temp directory
cp "$CHUNK_FILE" "${TEMP_DIR}/chunk.json"
log "Copied chunk file to temp directory"

# Deploy the files to Heroku
log "Starting Heroku deployment..."

# Upload chunk file to Heroku
log "Uploading chunk file to Heroku..."
cat "${TEMP_DIR}/chunk.json" | heroku run "cat > /tmp/chunk.json" --app "$APP_NAME" > "${TEMP_DIR}/upload_chunk.log" 2>&1
if [ $? -ne 0 ]; then
    log "ERROR: Failed to upload chunk file to Heroku. See ${TEMP_DIR}/upload_chunk.log for details."
    cat "${TEMP_DIR}/upload_chunk.log" >> "$LOG_FILE"
    exit 1
fi
log "Chunk file uploaded successfully"

# Upload import script to Heroku
log "Uploading import script to Heroku..."
cat "${TEMP_DIR}/import_script.py" | heroku run "cat > /tmp/import_script.py" --app "$APP_NAME" > "${TEMP_DIR}/upload_script.log" 2>&1
if [ $? -ne 0 ]; then
    log "ERROR: Failed to upload import script to Heroku. See ${TEMP_DIR}/upload_script.log for details."
    cat "${TEMP_DIR}/upload_script.log" >> "$LOG_FILE"
    exit 1
fi
log "Import script uploaded successfully"

# Run the import script on Heroku
log "Running import script on Heroku..."
heroku run "python /tmp/import_script.py /tmp/chunk.json" --app "$APP_NAME" > "${TEMP_DIR}/import_result.log" 2>&1
if [ $? -ne 0 ]; then
    log "ERROR: Failed to run import script on Heroku. See ${TEMP_DIR}/import_result.log for details."
    cat "${TEMP_DIR}/import_result.log" >> "$LOG_FILE"
    exit 1
fi
log "Import script executed successfully"

# Log the import results
log "Import Results:"
cat "${TEMP_DIR}/import_result.log" >> "$LOG_FILE"
cat "${TEMP_DIR}/import_result.log"  # Display to user as well

# Clean up
log "Cleaning up temporary directory..."
rm -rf "$TEMP_DIR"

log "Chunk upload process complete!"
echo "=================================================="
echo "Vascular MCQ chunk $CHUNK_NUM upload has finished!"
echo "Check the log file for details: $LOG_FILE"
echo "=================================================="