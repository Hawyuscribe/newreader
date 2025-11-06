#!/bin/bash
# Script to import all MCQs from the source directory to Heroku

# Set up logging
LOG_FILE="mcq_import_$(date +%Y%m%d_%H%M%S).log"
echo "Starting MCQ import process at $(date)" | tee -a "$LOG_FILE"

# Step 1: Make scripts executable
echo "Making scripts executable..." | tee -a "$LOG_FILE"
chmod +x copy_mcqs_to_project.py
chmod +x upload_all_mcqs_to_heroku.py

# Step 2: Copy MCQs from source directory to project directory
echo "Step 1: Copying MCQs from source directory..." | tee -a "$LOG_FILE"
python3 copy_mcqs_to_project.py | tee -a "$LOG_FILE"

if [ $? -ne 0 ]; then
    echo "Error: Failed to copy MCQs from source directory" | tee -a "$LOG_FILE"
    exit 1
fi

# Step 3: Upload and import MCQs to Heroku
echo "Step 2: Uploading MCQs to Heroku..." | tee -a "$LOG_FILE"
python3 upload_all_mcqs_to_heroku.py | tee -a "$LOG_FILE"

if [ $? -ne 0 ]; then
    echo "Warning: Some MCQs may have failed to upload" | tee -a "$LOG_FILE"
fi

# Print completion message
echo "MCQ import process completed at $(date)" | tee -a "$LOG_FILE"
echo "Check $LOG_FILE for details"
echo "Visit https://radiant-gorge-35079-2b52ba172c1e.herokuapp.com/ to verify the import"