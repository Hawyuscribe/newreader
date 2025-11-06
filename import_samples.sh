#!/bin/bash

# Script to import sample MCQs to Heroku
# This script uses the sample import option which works reliably

APP_NAME="radiant-gorge-35079"
REPEAT_COUNT=10  # Number of sample imports to run
LOG_FILE="sample_import_$(date +%Y%m%d_%H%M%S).log"

echo "Starting sample MCQ import to Heroku app $APP_NAME..."
echo "Will run $REPEAT_COUNT sample imports"
echo "Import started at $(date)" | tee -a "$LOG_FILE"
echo "----------------------------------------" | tee -a "$LOG_FILE"

# Run the sample import multiple times
for ((i=1; i<=$REPEAT_COUNT; i++)); do
    echo "[$i/$REPEAT_COUNT] Running sample import..." | tee -a "$LOG_FILE"
    
    # Run the sample import 
    heroku run python django_neurology_mcq/update_heroku_directly.py sample -a $APP_NAME > /tmp/sample_import_$i.log
    
    # Extract the import result summary
    if [ -f "/tmp/sample_import_$i.log" ]; then
        grep "Total MCQs imported:" "/tmp/sample_import_$i.log" | tee -a "$LOG_FILE"
    fi
    
    echo "[$i/$REPEAT_COUNT] Sample import completed" | tee -a "$LOG_FILE"
    echo "----------------------------------------" | tee -a "$LOG_FILE"
    
    # Add a delay between imports
    sleep 5
done

echo "Import process completed at $(date)" | tee -a "$LOG_FILE"

# Final validation
echo "Running final validation..." | tee -a "$LOG_FILE"
heroku run python django_neurology_mcq/update_heroku_directly.py validate -a $APP_NAME | tee -a "$LOG_FILE"