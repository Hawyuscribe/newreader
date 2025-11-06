#!/bin/bash

echo "Deploying explanation structure updates to Heroku..."

# Add and commit changes
git add -A
git commit -m "Update explanation display structure to match MCQ data format

- Updated MCQ template to display structured explanation sections
- Added CSS styling for explanation sections with icons
- Standardized explanation section keys across the application
- Updated admin interface to handle new section mappings
- Sections now include: conceptual_foundation, pathophysiological_mechanisms, 
  clinical_correlation, classification_and_nosology, diagnostic_approach,
  management_principles, option_analysis, clinical_pearls, current_evidence"

# Push to Heroku
git push heroku stable_version:main

echo "Running migrations on Heroku..."
heroku run python manage.py migrate

echo "Running explanation structure update on Heroku..."
heroku run python manage.py update_explanation_structure

echo "Deployment complete!"