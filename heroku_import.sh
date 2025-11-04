#!/bin/bash
# Script to import MCQs to Heroku using Heroku API

# Check if HEROKU_API_TOKEN is set
if [ -z "$HEROKU_API_TOKEN" ]; then
    echo "HEROKU_API_TOKEN not set. Setting it now..."
    export HEROKU_API_TOKEN=$(heroku auth:token)
fi

# Make sure we're in the right directory
cd "$(dirname "$0")"

# Make the Python script executable
chmod +x clear_and_import_mcqs.py

# Run the Python script
python3 clear_and_import_mcqs.py "$@"