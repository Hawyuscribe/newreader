#!/bin/bash

echo "Checking MCQ counts on Heroku..."
echo "================================"

# Run the check script on Heroku
heroku run python check_heroku_mcq_counts.py --app mcq-reader

echo -e "\n\nChecking recent Heroku logs for import errors..."
echo "================================================"

# Check logs for import-related errors
heroku logs --tail -n 500 --app mcq-reader | grep -E "(import|MCQ|error|Error|failed|Failed)" | tail -50