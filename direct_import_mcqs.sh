#!/bin/bash
# Script to directly import MCQs to Heroku

# Make sure we're in the right directory
cd "$(dirname "$0")"

# Make the Python script executable
chmod +x direct_import_mcqs.py

# Run the Python script
python3 direct_import_mcqs.py "$@"