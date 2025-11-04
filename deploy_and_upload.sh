#!/bin/bash
# Script to deploy the app to Heroku and upload vascular MCQs

# Set variables
APP_NAME="mcq-reader"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
LOG_FILE="heroku_deploy_${TIMESTAMP}.log"

# Function to log messages
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> "$LOG_FILE"
}

# Create log file
echo "Heroku Deploy and Upload Log - $(date)" > "$LOG_FILE"

# Step 1: Fix the Procfile
log "Fixing Procfile..."
mv Procfile.new Procfile
log "Procfile updated"

# Step 2: Make sure we have the correct Heroku remote
log "Setting up Heroku remote..."
heroku git:remote -a $APP_NAME

# Step 3: Check if PostgreSQL is provisioned
log "Checking PostgreSQL..."
if ! heroku addons --app $APP_NAME | grep -q "heroku-postgresql"; then
    log "PostgreSQL not found. Provisioning..."
    heroku addons:create heroku-postgresql:hobby-dev --app $APP_NAME
else
    log "PostgreSQL already provisioned"
fi

# Step 4: Set necessary config vars
log "Setting config vars..."
heroku config:set DJANGO_SETTINGS_MODULE=neurology_mcq.settings --app $APP_NAME
heroku config:set PYTHONPATH=django_neurology_mcq --app $APP_NAME

# Step 5: Commit and push changes
log "Committing changes..."
git add Procfile
git commit -m "Fix Procfile for Heroku deployment"

log "Pushing to Heroku..."
git push heroku stable_version:main

# Step 6: Scale dynos
log "Scaling web dyno..."
heroku ps:scale web=1 --app $APP_NAME

# Step 7: Run migrations
log "Running migrations..."
heroku run "cd django_neurology_mcq && python manage.py migrate" --app $APP_NAME

# Step a: Make the uploader executable
log "Preparing uploader script..."
chmod +x deploy_and_upload_vascular_mcqs.py

# Step 9: Run the MCQ uploader in the background
log "Starting MCQ upload in background..."
nohup python3 deploy_and_upload_vascular_mcqs.py > "vascular_upload_${TIMESTAMP}.log" 2>&1 &

# Get the process ID
PID=$!
log "Upload process started with PID: $PID"
echo $PID > "vascular_upload_pid.txt"

log "Deployment and upload setup complete"
log "You can monitor the upload with: tail -f vascular_upload_${TIMESTAMP}.log"
log "To check if the process is still running: ps -p $PID"

echo "Deployment complete. MCQ upload is running in the background (PID: $PID)."
echo "Monitor progress with: tail -f vascular_upload_${TIMESTAMP}.log"