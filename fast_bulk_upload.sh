#!/bin/bash

# Fast bulk upload script

echo "Uploading import script to Heroku..."
heroku run --app radiant-gorge-35079 "cat > /tmp/direct_import.py" < direct_import_script.py

echo "Processing fixtures..."
for file in fixtures_chunk_*.json; do
    echo "Uploading $file..."
    heroku run --app radiant-gorge-35079 "cd /app/django_neurology_mcq && python /tmp/direct_import.py" < "$file"
    sleep 2
done

echo "Complete!"