#!/bin/bash
# Script to test uploading a single vascular MCQ chunk to Heroku
# Testing with chunk 1

# Dynamically determine the current directory
CURRENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
APP_NAME="radiant-gorge-35079"
CHUNK_DIR="${CURRENT_DIR}/chunks"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
LOG_FILE="${CURRENT_DIR}/test_chunk_${TIMESTAMP}.log"

# Initialize log
echo "Testing Vascular MCQ Upload - Started at $(date)" > "$LOG_FILE"

# Function to log messages
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> "$LOG_FILE"
}

# Check current MCQ count
log "Checking current MCQ count on Heroku..."
heroku run "cd django_neurology_mcq && python manage.py shell -c \"from mcq.models import MCQ; print(f'Total MCQs: {MCQ.objects.count()}'); subspecialty='vascular_neurology'; print(f'Vascular MCQs: {MCQ.objects.filter(subspecialty=subspecialty).count()}')\"" --app "$APP_NAME" 2>&1 | tee -a "$LOG_FILE"

# Create import script directly
log "Creating import script..."
cat > "/tmp/import_mcqs.py" << 'EOF'
import sys
import json
import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
django.setup()

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
print(f"\nRESULTS:")
print(f"Successfully imported: {success_count} MCQs")
print(f"Failed to import: {error_count} MCQs")

if errors:
    print("\nErrors:")
    for error in errors[:5]:
        print(f" - {error}")
    if len(errors) > 5:
        print(f" - ...and {len(errors) - 5} more errors")
EOF

# Upload the import script
log "Uploading import script to Heroku..."
cat "/tmp/import_mcqs.py" | heroku run "cat > /tmp/import_mcqs.py" --app "$APP_NAME" 2>&1 | tee -a "$LOG_FILE"

# Process chunk 1
CHUNK_FILE="${CHUNK_DIR}/vascular_chunk_01_of_21.json"
CHUNK_NAME=$(basename "$CHUNK_FILE")
log "Processing chunk: $CHUNK_NAME"

# Upload chunk file
log "Uploading chunk file..."
cat "$CHUNK_FILE" | heroku run "cat > /tmp/$CHUNK_NAME" --app "$APP_NAME" 2>&1 | tee -a "$LOG_FILE"

# Import MCQs
log "Importing MCQs from $CHUNK_NAME..."
heroku run "cd django_neurology_mcq && python /tmp/import_mcqs.py /tmp/$CHUNK_NAME" --app "$APP_NAME" 2>&1 | tee -a "$LOG_FILE"

# Verify final MCQ count
log "Checking final MCQ count on Heroku..."
heroku run "cd django_neurology_mcq && python manage.py shell -c \"from mcq.models import MCQ; print(f'Final Total MCQs: {MCQ.objects.count()}'); subspecialty='vascular_neurology'; print(f'Final Vascular MCQs: {MCQ.objects.filter(subspecialty=subspecialty).count()}')\"" --app "$APP_NAME" 2>&1 | tee -a "$LOG_FILE"

log "Test upload process complete!"
echo "=================================================="
echo "Test vascular MCQ upload has finished!"
echo "Check the log file for details: $LOG_FILE"
echo "=================================================="