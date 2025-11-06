#!/bin/bash
# Script to generate Python commands for manually importing MCQs

# Make sure we're in the right directory
cd "$(dirname "$0")"

# Make the Python script executable
chmod +x generate_import_commands.py

# Run the Python script
python3 generate_import_commands.py "$@"