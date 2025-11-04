#!/usr/bin/env python3
"""Script to upload and import Part II 2022 MCQs to Heroku."""
import os
import sys
import json
import requests
import subprocess

# Read the MCQ file
mcq_file = "/Users/tariqalmatrudi/NEWreader/django_neurology_mcq/Part_II_2022.json"
print(f"Reading MCQ file: {mcq_file}")

with open(mcq_file, 'r') as f:
    mcq_data = json.load(f)

print(f"Found {len(mcq_data.get('mcqs', []))} MCQs")

# First, let's upload the JSON to Heroku as a gist
print("Creating GitHub gist...")
gist_data = {
    "description": "Part II 2022 MCQs",
    "public": False,
    "files": {
        "Part_II_2022.json": {
            "content": json.dumps(mcq_data)
        }
    }
}

# Create gist using curl
import subprocess
gist_command = [
    'curl',
    '-X', 'POST',
    'https://api.github.com/gists',
    '-H', 'Accept: application/vnd.github.v3+json',
    '-d', json.dumps(gist_data)
]

result = subprocess.run(gist_command, capture_output=True, text=True)
if result.returncode != 0:
    print(f"Error creating gist: {result.stderr}")
    sys.exit(1)

gist_response = json.loads(result.stdout)
raw_url = gist_response['files']['Part_II_2022.json']['raw_url']
print(f"Gist created: {raw_url}")

# Now run the import command on Heroku
print("Running import on Heroku...")
heroku_command = f"""
cd django_neurology_mcq && \
python -c "
import urllib.request
import json
from mcq.management.commands.import_part_ii_2022 import Command

# Download the file
print('Downloading MCQ data...')
with urllib.request.urlopen('{raw_url}') as response:
    data = json.loads(response.read().decode())

# Save to temporary file
with open('/tmp/part_ii_2022.json', 'w') as f:
    json.dump(data, f)

# Run the import command
print('Starting import...')
cmd = Command()
cmd.handle(file='/tmp/part_ii_2022.json')
print('Import complete!')
"
"""

# Run on Heroku
heroku_cmd = ['heroku', 'run', '--app', 'radiant-gorge-35079', heroku_command]
print("Executing Heroku command...")
subprocess.run(heroku_cmd)