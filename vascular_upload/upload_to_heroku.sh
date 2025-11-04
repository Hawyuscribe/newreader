#!/bin/bash
# Script to upload vascular MCQs to Heroku
# Generated on 2025-05-20 18:42:59

APP_NAME="mcq-reader"
CHUNK_DIR="/Users/tariqalmatrudi/Desktop/vascular_mcq_upload/chunks"
SCRIPT_FILE="/Users/tariqalmatrudi/Desktop/vascular_mcq_upload/import_mcqs.py"
LOG_FILE="/Users/tariqalmatrudi/Desktop/vascular_mcq_upload/upload.log"

# Initialize log
echo "Vascular MCQ Upload to Heroku - Started at $(date)" > "$LOG_FILE"

# Function to log messages
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> "$LOG_FILE"
}

# Check current MCQ count
log "Checking current MCQ count on Heroku..."
heroku run "cd django_neurology_mcq && python -c \"from mcq.models import MCQ; print(f'Total MCQs: {MCQ.objects.count()}'); print(f'Vascular MCQs: {MCQ.objects.filter(subspecialty=\\\"vascular_neurology\\\").count()}');\"" --app "$APP_NAME" 2>&1 | tee -a "$LOG_FILE"

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
heroku run "cd django_neurology_mcq && python -c \"from mcq.models import MCQ; print(f'Final Total MCQs: {MCQ.objects.count()}'); print(f'Final Vascular MCQs: {MCQ.objects.filter(subspecialty=\\\"vascular_neurology\\\").count()}');\"" --app "$APP_NAME" 2>&1 | tee -a "$LOG_FILE"

log "Upload process complete!"
echo "=================================================="
echo "Vascular MCQ upload script has finished!"
echo "Check the log file for details: $LOG_FILE"
echo "=================================================="
