#!/bin/bash
# Script to split MCQs into batches and upload to Heroku

# Make sure we're in the right directory
cd "$(dirname "$0")"

# Make the Python script executable
chmod +x split_and_upload_mcqs.py

# Run the Python script
python3 split_and_upload_mcqs.py "$@"