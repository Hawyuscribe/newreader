#!/bin/bash
# Script to upload a single vascular MCQ chunk to Heroku
# Usage: ./upload_chunk.sh <chunk_number>
# Example: ./upload_chunk.sh 7

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <chunk_number>"
    echo "Example: $0 7"
    exit 1
fi

CHUNK_NUM=$1

# Dynamically determine the current directory
CURRENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
APP_NAME="radiant-gorge-35079"  # Updated to correct app name
CHUNK_DIR="${CURRENT_DIR}/chunks"
SCRIPT_FILE="${CURRENT_DIR}/heroku_import_script.py"  # Updated script
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
LOG_FILE="${CURRENT_DIR}/vascular_chunk_${CHUNK_NUM}_${TIMESTAMP}.log"

# Format chunk number with leading zero if needed
if [ $CHUNK_NUM -lt 10 ]; then
    CHUNK_NUM_FMT="0$CHUNK_NUM"
else
    CHUNK_NUM_FMT="$CHUNK_NUM"
fi

CHUNK_FILE="${CHUNK_DIR}/vascular_chunk_${CHUNK_NUM_FMT}_of_21.json"

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

# Check current MCQ count
log "Checking current MCQ count on Heroku..."
heroku run "python -c \"from mcq.models import MCQ; print(f'Total MCQs: {MCQ.objects.count()}'); print(f'Vascular MCQs: {MCQ.objects.filter(subspecialty=\\\"vascular_neurology\\\").count()}');\"" --app "$APP_NAME" 2>&1 | tee -a "$LOG_FILE"

# Create temp directory on Heroku
log "Creating temporary directory on Heroku..."
heroku run "mkdir -p /tmp/mcq_upload" --app "$APP_NAME" 2>&1 | tee -a "$LOG_FILE"

# Upload chunk file to a temp location first
TEMP_CHUNK="/tmp/vascular_chunk.json"
log "Creating temporary chunk file: $TEMP_CHUNK"
cat "$CHUNK_FILE" > "$TEMP_CHUNK"

# Upload import script
log "Uploading import script..."
cat "$SCRIPT_FILE" | heroku run "cat > /tmp/mcq_upload/import_script.py" --app "$APP_NAME" 2>&1 | tee -a "$LOG_FILE"

# Process the specified chunk
CHUNK_NAME=$(basename "$CHUNK_FILE")
log "Processing chunk: $CHUNK_NAME"

# Upload chunk file
log "Uploading chunk file..."
cat "$TEMP_CHUNK" | heroku run "cat > /tmp/vascular_chunk.json" --app "$APP_NAME" 2>&1 | tee -a "$LOG_FILE"

# Import MCQs
log "Importing MCQs from $CHUNK_NAME..."
heroku run "python /tmp/mcq_upload/import_script.py" --app "$APP_NAME" 2>&1 | tee -a "$LOG_FILE"

log "Finished processing $CHUNK_NAME"

# Verify final MCQ count
log "Checking MCQ count after import..."
heroku run "python -c \"from mcq.models import MCQ; print(f'Total MCQs: {MCQ.objects.count()}'); print(f'Vascular MCQs: {MCQ.objects.filter(subspecialty=\\\"vascular_neurology\\\").count()}');\"" --app "$APP_NAME" 2>&1 | tee -a "$LOG_FILE"

# Clean up temporary files
rm -f "$TEMP_CHUNK"
log "Cleaned up temporary files"

log "Chunk upload process complete!"
echo "=================================================="
echo "Vascular MCQ chunk $CHUNK_NUM upload has finished!"
echo "Check the log file for details: $LOG_FILE"
echo "=================================================="