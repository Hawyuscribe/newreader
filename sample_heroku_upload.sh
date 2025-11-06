#!/bin/bash

# Import a sample MCQ file to Heroku

APP_NAME="radiant-gorge-35079"
MCQ_FILE="/Users/tariqalmatrudi/Documents/MCQs for the board/Previous MCQs/json explained/Promotion 2022_mcqs_20250515_085747.json"

echo "Testing MCQ import to Heroku app $APP_NAME..."
echo "Using file: $MCQ_FILE"

# First, run the sample import to test the script
echo "Running sample import to test the script..."
heroku run python django_neurology_mcq/update_heroku_directly.py sample -a $APP_NAME

# Then, validate to see the current state
echo "Validating current MCQs..."
heroku run python django_neurology_mcq/update_heroku_directly.py validate -a $APP_NAME

echo "Import test completed."