#!/bin/bash

# Deployment script with preloaded MCQ fixtures for Heroku
# This script converts MCQs to fixtures, commits them to the repository,
# and deploys the application to Heroku with fixtures included

# Configuration
SOURCE_DIR="/Users/tariqalmatrudi/Documents/MCQs for the board/Classified MCQs/reclassified"
FIXTURES_DIR="./django_neurology_mcq/fixtures/mcqs"
APP_DIR="./django_neurology_mcq"
LOG_FILE="deployment_$(date +%Y%m%d%H%M%S).log"
HEROKU_APP="radiant-gorge-35079"  # Replace with your actual Heroku app name

# Echo with timestamps
log() {
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

log "Starting deployment with MCQ fixtures..."
log "Source directory: $SOURCE_DIR"
log "Fixtures directory: $FIXTURES_DIR"
log "Log file: $LOG_FILE"

# Step 1: Set up the fixtures directory
log "Step 1: Setting up fixtures directory..."
mkdir -p "$FIXTURES_DIR"

# Step 2: Run the Python converter script
log "Step 2: Converting MCQs to JSON fixtures..."
python mcq_to_json_converter.py

if [ $? -ne 0 ]; then
    log "Error: Failed to convert MCQs to JSON fixtures"
    exit 1
fi

# Make sure fixtures directory exists and contains files
if [ ! -d "$FIXTURES_DIR" ] || [ -z "$(ls -A "$FIXTURES_DIR")" ]; then
    log "Error: Fixtures directory not found or empty: $FIXTURES_DIR"
    exit 1
fi

# Count the number of MCQs in the fixtures
FIXTURE_COUNT=$(python -c "import json; f=open('$FIXTURES_DIR/all_mcqs.json'); data=json.load(f); print(len(data)); f.close()")
log "Found $FIXTURE_COUNT MCQs in fixtures"

# Step 3: Verify the application works locally with fixtures
log "Step 3: Testing local application with fixtures..."
cd "$APP_DIR"
log "Clearing existing MCQs..."
python manage.py load_mcq_fixtures --clear --all
if [ $? -ne 0 ]; then
    log "Error: Failed to load fixtures locally"
    exit 1
fi
cd ..

# Step 4: Prepare for Heroku deployment
log "Step 4: Preparing for Heroku deployment..."

# Check if Git is already initialized
if [ ! -d ".git" ]; then
    log "Initializing Git repository..."
    git init
    git add .
    git commit -m "Initial commit with MCQ fixtures"
else
    log "Git repository already exists. Adding fixtures to repository..."
    git add "$FIXTURES_DIR"
    git commit -m "Add MCQ fixtures for preloaded data"
fi

# Step 5: Deploy to Heroku
log "Step 5: Deploying to Heroku..."
if heroku apps:info "$HEROKU_APP" >/dev/null 2>&1; then
    log "Deploying to existing Heroku app: $HEROKU_APP"
    git push heroku master
else
    log "Creating new Heroku app..."
    heroku create "$HEROKU_APP"
    git push heroku master
fi

# Step 6: Set up environment variables
log "Step 6: Setting up environment variables..."
heroku config:set AUTO_LOAD_FIXTURES=true --app "$HEROKU_APP"
heroku config:set DEBUG=false --app "$HEROKU_APP"

# Step 7: Run migrations and load fixtures if needed
log "Step 7: Running migrations on Heroku..."
heroku run "python manage.py migrate" --app "$HEROKU_APP"

# Step 8: Verify deployment
log "Step 8: Verifying deployment..."
MCQ_COUNT=$(heroku run "python manage.py shell -c 'from mcq.models import MCQ; print(MCQ.objects.count())'" --app "$HEROKU_APP" 2>/dev/null | grep -o '[0-9]\+' | tail -1)
if [ -n "$MCQ_COUNT" ]; then
    log "SUCCESS: Deployed application has $MCQ_COUNT MCQs!"
    echo ""
    echo "=================== DEPLOYMENT COMPLETED ==================="
    echo "Your application is now deployed to Heroku with $MCQ_COUNT MCQs!"
    echo "App URL: https://$HEROKU_APP.herokuapp.com"
    echo "See $LOG_FILE for details"
    echo "======================================================"
else
    log "WARNING: Could not verify MCQ count on Heroku."
    echo ""
    echo "=================== DEPLOYMENT COMPLETED ==================="
    echo "Deployment process has finished, but final verification failed."
    echo "Please check manually if all MCQs were loaded."
    echo "App URL: https://$HEROKU_APP.herokuapp.com"
    echo "See $LOG_FILE for details"
    echo "======================================================"
fi