#!/bin/bash

# Script to test uploading a single fixture file to Heroku

APP_NAME="radiant-gorge-35079"
TEST_FIXTURE="/Users/tariqalmatrudi/NEWreader/django_fixtures/mcq_fixture_1_of_31.json"
TEMP_DIR="/tmp/fixture_test"
LOG_FILE="test_fixture_upload_$(date +%Y%m%d_%H%M%S).log"

echo "Testing Django fixture upload to Heroku app $APP_NAME..." | tee -a "$LOG_FILE"
echo "Using fixture file: $TEST_FIXTURE" | tee -a "$LOG_FILE"
echo "Started at $(date)" | tee -a "$LOG_FILE"
echo "----------------------------------------" | tee -a "$LOG_FILE"

# First, check current MCQ count
echo "Checking current MCQ count on Heroku..." | tee -a "$LOG_FILE"
heroku run "python django_neurology_mcq/manage.py shell -c 'from mcq.models import MCQ; print(f\"Current MCQ count: {MCQ.objects.count()}\")'" -a $APP_NAME | tee -a "$LOG_FILE"

# Create a temporary directory on Heroku
echo "Creating temporary directory on Heroku..." | tee -a "$LOG_FILE"
heroku run "mkdir -p $TEMP_DIR" -a $APP_NAME

# Upload the fixture file to Heroku
echo "Uploading fixture file to Heroku..." | tee -a "$LOG_FILE"
cat "$TEST_FIXTURE" | heroku run "cat > $TEMP_DIR/test_fixture.json" -a $APP_NAME

# Load the fixture
echo "Loading fixture file on Heroku..." | tee -a "$LOG_FILE"
heroku run "python django_neurology_mcq/manage.py loaddata $TEMP_DIR/test_fixture.json" -a $APP_NAME | tee -a "$LOG_FILE"

# Check MCQ count after import
echo "Checking MCQ count after import..." | tee -a "$LOG_FILE"
heroku run "python django_neurology_mcq/manage.py shell -c 'from mcq.models import MCQ; print(f\"Updated MCQ count: {MCQ.objects.count()}\")'" -a $APP_NAME | tee -a "$LOG_FILE"

# Clean up
echo "Cleaning up temporary files on Heroku..." | tee -a "$LOG_FILE"
heroku run "rm -rf $TEMP_DIR" -a $APP_NAME

echo "Test upload completed at $(date)" | tee -a "$LOG_FILE"
echo "See $LOG_FILE for details."