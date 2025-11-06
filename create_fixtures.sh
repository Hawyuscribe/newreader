#!/bin/bash
# Script to create Django fixtures from MCQ JSON files

# Make sure we're in the right directory
cd "$(dirname "$0")"

# Make the Python script executable
chmod +x create_django_fixtures.py

# Run the Python script
python3 create_django_fixtures.py "$@"