#!/bin/bash
# Script to fix Heroku app issues and configure for MCQ import
# Generated on 2025-05-20 18:42:59

APP_NAME="mcq-reader"
LOG_FILE="/Users/tariqalmatrudi/Desktop/vascular_mcq_upload/heroku_fix.log"

# Initialize log
echo "Heroku App Fix - Started at $(date)" > "$LOG_FILE"

# Function to log messages
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> "$LOG_FILE"
}

# Check app status
log "Checking Heroku app status..."
heroku apps:info --app "$APP_NAME" 2>&1 | tee -a "$LOG_FILE"

# Check if PostgreSQL is provisioned
log "Checking PostgreSQL..."
if ! heroku addons --app "$APP_NAME" | grep -q "postgresql"; then
    log "PostgreSQL not found. Attempting to provision..."
    heroku addons:create heroku-postgresql:mini --app "$APP_NAME" 2>&1 | tee -a "$LOG_FILE"
else
    log "PostgreSQL already provisioned"
fi

# Set environment variables
log "Setting environment variables..."
heroku config:set DJANGO_SETTINGS_MODULE=neurology_mcq.settings --app "$APP_NAME" 2>&1 | tee -a "$LOG_FILE"
heroku config:set PYTHONPATH=django_neurology_mcq --app "$APP_NAME" 2>&1 | tee -a "$LOG_FILE"

# Scale dynos
log "Attempting to scale dynos..."
heroku ps:scale web=1 --app "$APP_NAME" 2>&1 | tee -a "$LOG_FILE"

# Run migrations
log "Running migrations..."
heroku run "cd django_neurology_mcq && python manage.py migrate" --app "$APP_NAME" 2>&1 | tee -a "$LOG_FILE"

log "Heroku app setup complete!"
echo "=================================================="
echo "Heroku app setup complete!"
echo "Check the log file for details: $LOG_FILE"
echo "Next step: Run the upload script to import MCQs"
echo "=================================================="
