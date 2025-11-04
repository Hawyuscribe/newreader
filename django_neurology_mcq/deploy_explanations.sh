#!/bin/bash
# Deploy explanations to Heroku
# This script uploads the exported explanations file to Heroku and runs the import script

set -e  # Exit on error

# Default values
EXPLANATION_FILE=""
DRY_RUN=false
BATCH_SIZE=100

# Parse arguments
while [[ $# -gt 0 ]]; do
  key="$1"
  case $key in
    -f|--file)
      EXPLANATION_FILE="$2"
      shift
      shift
      ;;
    --dry-run)
      DRY_RUN=true
      shift
      ;;
    -b|--batch-size)
      BATCH_SIZE="$2"
      shift
      shift
      ;;
    *)
      echo "Unknown option: $1"
      exit 1
      ;;
  esac
done

# Check if file specified
if [ -z "$EXPLANATION_FILE" ]; then
  # Find the most recent export file
  EXPLANATION_FILE=$(ls -t explanations_export_*.json | head -1)
  if [ -z "$EXPLANATION_FILE" ]; then
    echo "Error: No explanation file found. Please run export_explanations.py first."
    exit 1
  fi
  echo "Using most recent export file: $EXPLANATION_FILE"
fi

# Check if file exists
if [ ! -f "$EXPLANATION_FILE" ]; then
  echo "Error: File $EXPLANATION_FILE does not exist"
  exit 1
fi

# Check file size
FILE_SIZE=$(du -m "$EXPLANATION_FILE" | cut -f1)
echo "File size: ${FILE_SIZE}MB"

if [ $FILE_SIZE -gt 100 ]; then
  echo "Warning: File is large (${FILE_SIZE}MB), this may take a while to upload"
  read -p "Continue? (y/n) " -n 1 -r
  echo
  if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    exit 1
  fi
fi

echo "Committing import script to git..."
git add import_explanations_heroku.py
git commit -m "Add script to import explanations on Heroku" || echo "No changes to commit"
git push heroku stable_version:main

echo "Uploading explanation file to Heroku..."
UPLOAD_NAME="explanations.json"
heroku run --no-tty "cat > $UPLOAD_NAME" < "$EXPLANATION_FILE"

echo "Running import script on Heroku..."
DRY_RUN_FLAG=""
if [ "$DRY_RUN" = true ]; then
  DRY_RUN_FLAG="--dry-run"
fi

heroku run "python import_explanations_heroku.py $UPLOAD_NAME $DRY_RUN_FLAG --batch-size $BATCH_SIZE"

echo "Done!"