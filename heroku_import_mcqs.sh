#!/bin/bash

# Comprehensive MCQ Import Script for Heroku
# This script deletes all existing MCQs and imports all MCQs from text files to Heroku.

# Usage:
# ./heroku_import_mcqs.sh [path_to_mcq_directory]

# Get source directory from arguments or use default
SOURCE_DIR="${1:-/Users/tariqalmatrudi/Documents/MCQs for the board/Classified MCQs/reclassified}"
TIMESTAMP=$(date +%Y%m%d%H%M%S)
LOG_FILE="heroku_import_${TIMESTAMP}.log"

# Echo with timestamps
log() {
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

# Check if source directory exists
if [ ! -d "$SOURCE_DIR" ]; then
    log "Error: Source directory does not exist: $SOURCE_DIR"
    exit 1
fi

log "Starting Heroku MCQ import process..."
log "Source directory: $SOURCE_DIR"
log "Log file: $LOG_FILE"

# Make import script executable
chmod +x import_all_mcqs.py

# Step 1: Delete all existing MCQs on Heroku using direct database access
log "Step 1: Deleting all existing MCQs from Heroku..."
heroku run "python django_neurology_mcq/manage.py shell -c 'from mcq.models import MCQ, Bookmark, Flashcard, Note, ReasoningSession; print(f\"Deleting {Bookmark.objects.count()} bookmarks, {Flashcard.objects.count()} flashcards, {Note.objects.count()} notes, {ReasoningSession.objects.count()} reasoning sessions, and {MCQ.objects.count()} MCQs\"); Bookmark.objects.all().delete(); Flashcard.objects.all().delete(); Note.objects.all().delete(); ReasoningSession.objects.all().delete(); MCQ.objects.all().delete(); print(\"All MCQs and related data deleted\")'" | tee -a "$LOG_FILE"

# Step 2: Upload script to Heroku (using a temporary file to avoid large output)
log "Step 2: Uploading import script to Heroku..."
heroku run "cat > import_all_mcqs.py" < import_all_mcqs.py > /dev/null 2>&1

if [ $? -ne 0 ]; then
    log "Error: Failed to upload import script to Heroku"
    exit 1
else
    log "Successfully uploaded import_all_mcqs.py to Heroku"
fi

# Check MCQ files count
mcq_count=$(find "$SOURCE_DIR" -name "*.txt" | grep -v "debug\|reclassification" | wc -l)
log "Found $mcq_count MCQ files in source directory"

# Process files by subspecialty
log "Step 3: Processing MCQ files by subspecialty..."

# Create a temporary directory for processed files
TEMP_DIR="./temp_processed_mcqs"
mkdir -p "$TEMP_DIR"

# Copy and preprocess files to temp directory
log "Preprocessing MCQ files..."
for file in "$SOURCE_DIR"/*.txt; do
    if [[ ! $(basename "$file") =~ ^(debug|reclassification) ]]; then
        subspecialty=$(basename "$file" .txt)
        log "Processing: $subspecialty"
        
        # Remove classification reasons before uploading
        sed '/^\*Classification Reason:/d' "$file" > "$TEMP_DIR/$subspecialty.txt"
    fi
done

# Create directory on Heroku first (do this only once)
log "Creating mcq_files directory on Heroku..."
heroku run "mkdir -p mcq_files" | tee -a "$LOG_FILE"

# Upload each preprocessed file to Heroku
log "Uploading MCQ files to Heroku..."
for file in "$TEMP_DIR"/*.txt; do
    subspecialty=$(basename "$file" .txt)
    log "Uploading: $subspecialty.txt"
    
    # Upload the file (redirecting output to avoid large responses)
    heroku run "cat > mcq_files/$subspecialty.txt" < "$file" > /dev/null 2>&1
    
    if [ $? -ne 0 ]; then
        log "Warning: Failed to upload $subspecialty.txt, retrying..."
        sleep 2
        heroku run "cat > mcq_files/$subspecialty.txt" < "$file" > /dev/null 2>&1
    fi
    
    # Verify upload
    heroku run "ls -l mcq_files/$subspecialty.txt" | tee -a "$LOG_FILE"
    
    # Brief pause to avoid overwhelming Heroku
    sleep 1
done

# Step 4: Run import on Heroku with larger timeout
log "Step 4: Running MCQ import on Heroku..."
heroku run:detached "python import_all_mcqs.py mcq_files --log-file heroku_import.log --batch-size 20"
log "Import started as a detached process on Heroku. This may take some time."
log "Waiting for import to complete (this could take 10-15 minutes)..."

# Wait for a while to allow the import to complete
sleep 300  # Wait 5 minutes

# Step 5: Check progress a few times
for i in {1..5}; do
    log "Checking import progress (check $i of 5)..."
    heroku run "python django_neurology_mcq/manage.py shell -c 'from mcq.models import MCQ; print(f\"Current MCQs in database: {MCQ.objects.count()}\")'" | tee -a "$LOG_FILE"
    
    # If we have a significant number of MCQs, consider it successful
    MCQ_COUNT=$(heroku run "python django_neurology_mcq/manage.py shell -c 'from mcq.models import MCQ; print(MCQ.objects.count())'" 2>/dev/null | grep -o '[0-9]\+' | tail -1)
    if [ -n "$MCQ_COUNT" ] && [ "$MCQ_COUNT" -gt 1000 ]; then
        log "Import appears to be successful with $MCQ_COUNT MCQs imported!"
        break
    fi
    
    # Wait before checking again
    log "Waiting another 2 minutes..."
    sleep 120
done

# Step 6: Verify final import
log "Step 6: Verifying final import results..."
heroku run "python django_neurology_mcq/manage.py shell -c 'from mcq.models import MCQ; print(f\"Total MCQs in database: {MCQ.objects.count()}\"); from django.db.models import Count; for item in MCQ.objects.values(\"subspecialty\").annotate(count=Count(\"id\")).order_by(\"subspecialty\"): print(f\"{item[\"subspecialty\"]}: {item[\"count\"]} MCQs\")'" | tee -a "$LOG_FILE"

# Step 7: Try to retrieve logs
log "Step 7: Attempting to download logs from Heroku..."
heroku run "if [ -f heroku_import.log ]; then cat heroku_import.log; else echo 'Log file not found'; fi" >> "$LOG_FILE" 2>/dev/null

# Cleanup
log "Cleaning up temporary files..."
rm -rf "$TEMP_DIR"

log "Import process completed!"
log "Check $LOG_FILE for detailed information."

# Final verification and user message
FINAL_COUNT=$(heroku run "python django_neurology_mcq/manage.py shell -c 'from mcq.models import MCQ; print(MCQ.objects.count())'" 2>/dev/null | grep -o '[0-9]\+' | tail -1)
if [ -n "$FINAL_COUNT" ]; then
    log "SUCCESS: Your database now contains $FINAL_COUNT MCQs!"
    echo ""
    echo "=================== IMPORT COMPLETED ==================="
    echo "Your database now contains $FINAL_COUNT MCQs!"
    echo "See $LOG_FILE for details"
    echo "======================================================"
else
    log "WARNING: Could not verify final MCQ count."
    echo ""
    echo "=================== IMPORT COMPLETED ==================="
    echo "Import process has finished, but final verification failed."
    echo "Please check manually if all MCQs were imported."
    echo "See $LOG_FILE for details"
    echo "======================================================"
fi

