#!/bin/bash

echo "Starting MCQ deployment and import process..."

# Navigate to project directory
cd /Users/tariqalmatrudi/NEWreader

# First, copy the MCQ files to the project directory
echo "Copying MCQ files to project..."
mkdir -p mcq_data_to_import
cp -r /Users/tariqalmatrudi/Documents/FFF/output_by_specialty/*.json mcq_data_to_import/

# Add and commit the import script and data
echo "Adding files to git..."
git add direct_mcq_import_heroku.py
git add mcq_data_to_import/
git commit -m "Add MCQ import script and data files"

# Push to Heroku
echo "Pushing to Heroku..."
git push heroku stable_version:main --force

# Run the import script on Heroku
echo "Running import script on Heroku..."
heroku run python direct_mcq_import_heroku.py

# Clean up local data files
echo "Cleaning up temporary files..."
rm -rf mcq_data_to_import/
git rm -rf mcq_data_to_import/
git commit -m "Remove temporary MCQ data files"
git push heroku stable_version:main --force

echo "MCQ import process complete!"