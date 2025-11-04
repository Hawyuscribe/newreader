#!/bin/bash

echo "Deploying MCQ analysis command to Heroku..."

# Create the management command directory structure
mkdir -p django_neurology_mcq/mcq/management/commands

# Copy the analysis script to the Django management commands
cp analyze_and_reclassify_mcqs.py django_neurology_mcq/mcq/management/commands/analyze_unclassified.py

# Add __init__.py files if they don't exist
touch django_neurology_mcq/mcq/management/__init__.py
touch django_neurology_mcq/mcq/management/commands/__init__.py

echo "Files prepared for deployment."
echo ""
echo "To deploy and run the analysis:"
echo "1. Commit the changes: git add . && git commit -m 'Add MCQ analysis command'"
echo "2. Push to Heroku: git push heroku main"
echo "3. Run analysis (dry run): heroku run python manage.py analyze_unclassified"
echo "4. Run and apply fixes: heroku run python manage.py analyze_unclassified --fix"
echo ""
echo "To download the report after running:"
echo "heroku run cat unclassified_analysis_report.json > local_report.json"