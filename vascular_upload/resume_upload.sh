#!/bin/bash
# Script to resume uploading vascular MCQs to Heroku
# Starting from chunk 7 (since chunks 1-6 appear to have been processed)

# Dynamically determine the current directory
CURRENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
APP_NAME="mcq-reader"
CHUNK_DIR="${CURRENT_DIR}/chunks"
SCRIPT_FILE="${CURRENT_DIR}/import_mcqs.py"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
LOG_FILE="${CURRENT_DIR}/vascular_resume_${TIMESTAMP}.log"
RESUME_FROM=7  # Starting from chunk 7

# Initialize log
echo "Vascular MCQ Upload to Heroku (RESUMED) - Started at $(date)" > "$LOG_FILE"

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

# Process remaining chunks
for ((i=RESUME_FROM; i<=21; i++)); do
    # Format chunk number with leading zero
    if [ $i -lt 10 ]; then
        CHUNK_NUM="0$i"
    else
        CHUNK_NUM="$i"
    fi
    
    CHUNK_FILE="${CHUNK_DIR}/vascular_chunk_${CHUNK_NUM}_of_21.json"
    
    if [ ! -f "$CHUNK_FILE" ]; then
        log "WARNING: Could not find chunk file: $CHUNK_FILE"
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

log "Resume upload process complete!"
echo "=================================================="
echo "Vascular MCQ upload script has finished!"
echo "Check the log file for details: $LOG_FILE"
echo "=================================================="