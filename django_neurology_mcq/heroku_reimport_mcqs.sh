#!/bin/bash

echo "Starting Heroku MCQ reimport process..."
echo "======================================"

# First, check current counts
echo -e "\n1. Checking current MCQ counts on Heroku..."
heroku run python check_heroku_mcq_counts.py --app neurology-mcq-bank

# Ask for confirmation
echo -e "\n2. This will DELETE ALL MCQs and reimport them. Continue? (y/n)"
read -r response
if [[ ! "$response" =~ ^[Yy]$ ]]; then
    echo "Aborting reimport."
    exit 1
fi

# Upload the reimport script
echo -e "\n3. Uploading reimport script to Heroku..."
cat reliable_mcq_reimport.py | heroku run -a neurology-mcq-bank "cat > reliable_mcq_reimport.py"

# Check if we have fixture files on Heroku
echo -e "\n4. Checking for fixture files on Heroku..."
heroku run ls -la rere_fixtures.json rere_chunks/ fixtures/ --app neurology-mcq-bank

# If no fixtures on Heroku, we need to upload them
echo -e "\n5. Uploading fixture files..."

# Create a combined fixture file locally first
echo "Creating combined fixture file..."
python3 << 'EOF'
import json
import os

all_fixtures = []

# Load rere_fixtures.json
if os.path.exists('rere_fixtures.json'):
    with open('rere_fixtures.json', 'r') as f:
        data = json.load(f)
        all_fixtures.extend(data)
        print(f"Loaded {len(data)} items from rere_fixtures.json")

# Load from rere_chunks
if os.path.exists('rere_chunks'):
    for chunk_file in sorted(os.listdir('rere_chunks')):
        if chunk_file.endswith('.json'):
            with open(os.path.join('rere_chunks', chunk_file), 'r') as f:
                data = json.load(f)
                all_fixtures.extend(data)
                print(f"Loaded {len(data)} items from {chunk_file}")

# Save combined file
with open('combined_fixtures_for_heroku.json', 'w') as f:
    json.dump(all_fixtures, f)
    print(f"\nSaved {len(all_fixtures)} total items to combined_fixtures_for_heroku.json")
EOF

# Upload to GitHub Gist and import
echo -e "\n6. Uploading fixtures via GitHub Gist..."
python3 upload_via_gist.py combined_fixtures_for_heroku.json

# Get the gist URL from the output
echo -e "\n7. Please enter the Gist raw URL from above:"
read -r gist_url

# Run the import on Heroku
echo -e "\n8. Running import on Heroku..."
heroku run -a neurology-mcq-bank python << EOF
import json
import urllib.request
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mcq.settings')
django.setup()

from django.db import transaction
from mcq.models import MCQ, Subspecialty

print("Downloading fixtures from Gist...")
response = urllib.request.urlopen('$gist_url')
fixtures = json.loads(response.read().decode('utf-8'))

print(f"Downloaded {len(fixtures)} fixture items")

# Clear existing MCQs
print("\nClearing existing MCQs...")
deleted = MCQ.objects.all().delete()[0]
print(f"Deleted {deleted} MCQs")

# Import new MCQs
print("\nImporting MCQs...")
subspecialties = {sub.name: sub for sub in Subspecialty.objects.all()}
imported = 0

with transaction.atomic():
    for item in fixtures:
        if item['model'] == 'mcq.mcq':
            fields = item['fields']
            
            subspecialty = None
            if 'subspecialty' in fields and fields['subspecialty']:
                sub_name = fields['subspecialty']
                if isinstance(sub_name, list):
                    sub_name = sub_name[0] if sub_name else None
                if sub_name in subspecialties:
                    subspecialty = subspecialties[sub_name]
            
            MCQ.objects.create(
                question=fields['question'],
                option_a=fields.get('option_a', ''),
                option_b=fields.get('option_b', ''),
                option_c=fields.get('option_c', ''),
                option_d=fields.get('option_d', ''),
                option_e=fields.get('option_e', ''),
                correct_answer=fields.get('correct_answer', 'A'),
                explanation=fields.get('explanation', ''),
                exam_type=fields.get('exam_type', ''),
                year=fields.get('year'),
                subspecialty=subspecialty,
                difficulty=fields.get('difficulty', 'medium'),
                topic=fields.get('topic', ''),
                subtopic=fields.get('subtopic', ''),
                clinical_vignette=fields.get('clinical_vignette', False),
                image_question=fields.get('image_question', False),
                requires_calculator=fields.get('requires_calculator', False)
            )
            imported += 1
            
            if imported % 100 == 0:
                print(f"Imported {imported} MCQs...")

print(f"\nImport complete! Imported {imported} MCQs")
print(f"Total MCQs in database: {MCQ.objects.count()}")
EOF

# Final verification
echo -e "\n9. Final verification..."
heroku run python check_heroku_mcq_counts.py --app neurology-mcq-bank

echo -e "\nReimport process completed!"