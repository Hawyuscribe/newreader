#!/bin/bash

echo "Starting MCQ replacement process on Heroku..."

# Navigate to project directory
cd /Users/tariqalmatrudi/NEWreader

# First, let's create a temporary directory with just a few MCQ files to test
echo "Creating temporary MCQ data directory..."
mkdir -p temp_mcq_data

# Copy all MCQ files to temp directory
echo "Copying MCQ files..."
cp /Users/tariqalmatrudi/Documents/FFF/output_by_specialty/*.json temp_mcq_data/

# Count the files
file_count=$(ls -1 temp_mcq_data/*.json | wc -l)
echo "Found $file_count MCQ files to upload"

# Add the management command and temp data to git
echo "Adding files to git..."
git add django_neurology_mcq/mcq/management/commands/replace_all_mcqs.py
git add temp_mcq_data/
git commit -m "Add MCQ replacement command and data files"

# Push to Heroku
echo "Pushing to Heroku..."
git push heroku stable_version:main --force

# Run the replacement command on Heroku
echo "Running MCQ replacement on Heroku..."
heroku run "cd django_neurology_mcq && python manage.py replace_all_mcqs --source-dir /app/temp_mcq_data --confirm" --app radiant-gorge-35079

# Clean up temp files
echo "Cleaning up temporary files..."
rm -rf temp_mcq_data/
git rm -rf temp_mcq_data/
git commit -m "Remove temporary MCQ data files"
git push heroku stable_version:main --force

echo "MCQ replacement process complete!"
echo "Checking final MCQ count..."
heroku run "cd django_neurology_mcq && python manage.py check_mcqs" --app radiant-gorge-35079