#!/bin/bash
# Fixed script to upload MCQ chunks to Heroku

# Configuration
APP_NAME="radiant-gorge-35079"
LOCAL_EXPORT_DIR="mcq_exports"
REMOTE_IMPORT_DIR="/app/mcq_exports"

# Create the remote directory
echo "Creating remote directory..."
heroku run "mkdir -p $REMOTE_IMPORT_DIR" --app $APP_NAME

# Upload the manifest file
echo "Uploading manifest file..."
heroku run "cat > $REMOTE_IMPORT_DIR/export_manifest.json" --app $APP_NAME < $LOCAL_EXPORT_DIR/export_manifest.json

# Upload each chunk individually
for i in {1..6}; do
  echo "Uploading chunk $i of 6..."
  heroku run "cat > $REMOTE_IMPORT_DIR/mcqs_chunk_${i}_of_6.json" --app $APP_NAME < $LOCAL_EXPORT_DIR/mcqs_chunk_${i}_of_6.json
  
  # Brief pause between uploads
  sleep 2
done

# Verify the upload
echo "Verifying upload..."
heroku run "ls -la $REMOTE_IMPORT_DIR" --app $APP_NAME

# Import each chunk individually
for i in {1..6}; do
  echo "Importing chunk $i of 6..."
  heroku run "cd django_neurology_mcq && python manage.py import_mcqs_chunked $REMOTE_IMPORT_DIR --chunk-file mcqs_chunk_${i}_of_6.json --batch-size 25" --app $APP_NAME
  
  # Brief pause between imports
  sleep 2
done

# Verify the import
echo "Verifying import results..."
heroku run "cd django_neurology_mcq && python manage.py verify_mcq_import --detailed" --app $APP_NAME

echo "Process complete!"