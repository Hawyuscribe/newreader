#!/bin/bash

# Download CSV file
echo "Downloading CSV file..."
heroku run --app radiant-gorge-35079 'cd django_neurology_mcq && cat heroku_vascular_mcqs.csv' > vascular_mcqs_from_heroku.csv

# Download JSON file
echo "Downloading JSON file..."
heroku run --app radiant-gorge-35079 'cd django_neurology_mcq && cat heroku_vascular_mcqs.json' > vascular_mcqs_from_heroku.json

# Download Excel file (this will be binary, so we need to use base64)
echo "Creating download script for Excel file..."
heroku run --app radiant-gorge-35079 'cd django_neurology_mcq && python -c "import base64; print(base64.b64encode(open(\"heroku_vascular_mcqs.xlsx\", \"rb\").read()).decode())"' > vascular_mcqs_base64.txt

# Decode the base64 Excel file
echo "Decoding Excel file..."
python3 -c "import base64; open('vascular_mcqs_from_heroku.xlsx', 'wb').write(base64.b64decode(open('vascular_mcqs_base64.txt').read()))"

# Clean up
rm vascular_mcqs_base64.txt

echo "Download complete!"
echo "Files downloaded:"
echo "- vascular_mcqs_from_heroku.csv"
echo "- vascular_mcqs_from_heroku.json"
echo "- vascular_mcqs_from_heroku.xlsx"