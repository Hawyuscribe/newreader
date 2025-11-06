#!/bin/bash

# Script to deploy Django fixtures to Heroku
# This script creates fixtures from MCQ files and deploys them to Heroku

APP_NAME="radiant-gorge-35079"
FIXTURES_DIR="/Users/tariqalmatrudi/NEWreader/django_fixtures"
LOG_FILE="fixtures_deployment_$(date +%Y%m%d_%H%M%S).log"

echo "Starting Django fixtures deployment to Heroku app $APP_NAME..." | tee -a "$LOG_FILE"
echo "Started at $(date)" | tee -a "$LOG_FILE"
echo "----------------------------------------" | tee -a "$LOG_FILE"

# Create the django fixtures
echo "Creating Django fixtures from MCQ files..." | tee -a "$LOG_FILE"
python3 /Users/tariqalmatrudi/NEWreader/create_django_fixtures.py | tee -a "$LOG_FILE"

# Check if fixtures were created successfully
if [ ! -d "$FIXTURES_DIR" ]; then
    echo "Error: Fixtures directory not found. Fixture creation might have failed." | tee -a "$LOG_FILE"
    exit 1
fi

# Count fixture files
FIXTURE_FILES=$(find "$FIXTURES_DIR" -name "*.json" -not -name "fixtures_manifest.json" | wc -l | xargs)
echo "Found $FIXTURE_FILES fixture files to deploy" | tee -a "$LOG_FILE"

# Create a temporary directory on Heroku to store fixtures
echo "Creating temporary directory on Heroku..." | tee -a "$LOG_FILE"
heroku run "mkdir -p /tmp/fixtures" -a $APP_NAME

# Upload each fixture file to Heroku and load it
echo "Uploading and loading fixture files..." | tee -a "$LOG_FILE"
COUNTER=0
for FIXTURE_FILE in "$FIXTURES_DIR"/mcq_fixture_*.json; do
    FILENAME=$(basename "$FIXTURE_FILE")
    COUNTER=$((COUNTER + 1))
    
    echo "[$COUNTER/$FIXTURE_FILES] Uploading $FILENAME..." | tee -a "$LOG_FILE"
    
    # Upload the fixture file to Heroku
    cat "$FIXTURE_FILE" | heroku run "cat > /tmp/fixtures/$FILENAME" -a $APP_NAME
    
    # Load the fixture
    echo "[$COUNTER/$FIXTURE_FILES] Loading $FILENAME..." | tee -a "$LOG_FILE"
    heroku run "python manage.py loaddata /tmp/fixtures/$FILENAME" -a $APP_NAME
    
    # Check if loading was successful
    if [ $? -eq 0 ]; then
        echo "[$COUNTER/$FIXTURE_FILES] Successfully loaded $FILENAME" | tee -a "$LOG_FILE"
    else
        echo "[$COUNTER/$FIXTURE_FILES] Failed to load $FILENAME" | tee -a "$LOG_FILE"
    fi
    
    echo "----------------------------------------" | tee -a "$LOG_FILE"
done

# Verify data was loaded
echo "Verifying data was loaded..." | tee -a "$LOG_FILE"
heroku run "python manage.py shell -c 'from mcq.models import MCQ; print(f\"Total MCQs: {MCQ.objects.count()}\")'" -a $APP_NAME | tee -a "$LOG_FILE"

# Clean up
echo "Cleaning up temporary files on Heroku..." | tee -a "$LOG_FILE"
heroku run "rm -rf /tmp/fixtures" -a $APP_NAME

echo "Deployment completed at $(date)" | tee -a "$LOG_FILE"
echo "See $LOG_FILE for details."