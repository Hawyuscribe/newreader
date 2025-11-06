#!/bin/bash
# Script to upload MCQs to Heroku by subspecialty

APP_NAME="radiant-gorge-35079"
FIXTURES_DIR="fixtures"

echo "===== HEROKU MCQ UPLOAD ====="
echo "Started at: $(date)"
echo ""

# Create fixtures directory if it doesn't exist
mkdir -p $FIXTURES_DIR

# Clear all existing MCQs on Heroku
echo "Clearing existing MCQs on Heroku..."
heroku run --app $APP_NAME "cd /app/django_neurology_mcq && python manage.py shell -c 'from mcq.models import MCQ; count = MCQ.objects.count(); print(f\"Deleting {count} MCQs...\"); MCQ.objects.all().delete(); print(\"Done\")'"

# Get list of subspecialties
echo "Getting list of subspecialties..."
python -c "
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
django.setup()
from mcq.models import MCQ
from django.db.models import Count
subspecialties = MCQ.objects.values('subspecialty').annotate(count=Count('id')).order_by('-count')
for item in subspecialties:
    print(f'{item[\"subspecialty\"]}|{item[\"count\"]}')
" > subspecialties.txt

# Process each subspecialty
cat subspecialties.txt | while IFS='|' read -r subspecialty count; do
    echo ""
    echo "Processing $subspecialty ($count MCQs)..."
    
    # Create fixture file for this subspecialty
    FIXTURE_FILE="$FIXTURES_DIR/${subspecialty// /_}.json"
    
    # Export MCQs for this subspecialty
    echo "Exporting to $FIXTURE_FILE..."
    python -c "
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
django.setup()
from mcq.models import MCQ
from django.core import serializers
import json

mcqs = MCQ.objects.filter(subspecialty='$subspecialty')
fixture_data = serializers.serialize('json', mcqs)
with open('$FIXTURE_FILE', 'w') as f:
    f.write(fixture_data)
print(f'Exported {mcqs.count()} MCQs to $FIXTURE_FILE')
"
    
    # Upload and import on Heroku
    echo "Uploading to Heroku..."
    cat $FIXTURE_FILE | heroku run --app $APP_NAME "cat > /tmp/import_data.json"
    
    echo "Importing on Heroku..."
    heroku run --app $APP_NAME "cd /app/django_neurology_mcq && python manage.py shell -c '
import json
from django.core import serializers
from mcq.models import MCQ
from django.db import transaction

# Count before
print(\"Before import: \", MCQ.objects.filter(subspecialty=\"$subspecialty\").count())

# Load data
with open(\"/tmp/import_data.json\", \"r\") as f:
    data = f.read()

# Import
objects = serializers.deserialize(\"json\", data)
with transaction.atomic():
    count = 0
    for obj in objects:
        obj.save()
        count += 1
    print(f\"Imported {count} MCQs for $subspecialty\")

# Count after
print(\"After import: \", MCQ.objects.filter(subspecialty=\"$subspecialty\").count())
'"
done

# Verify import
echo ""
echo "Verifying import..."
heroku run --app $APP_NAME "cd /app/django_neurology_mcq && python manage.py shell -c '
from mcq.models import MCQ
from django.db.models import Count

total = MCQ.objects.count()
print(f\"Total MCQs: {total}\")

print(\"\\nMCQs by Subspecialty:\")
subspecialties = MCQ.objects.values(\"subspecialty\").annotate(count=Count(\"id\")).order_by(\"-count\")
for item in subspecialties:
    print(f\"  {item[\"subspecialty\"]}: {item[\"count\"]}\")
'"

echo ""
echo "Import completed at: $(date)"
echo "==========================="