#!/bin/bash
# Simple script to test uploading a single vascular MCQ chunk

# Heroku app name
APP_NAME="radiant-gorge-35079" 

# Path to the chunk file
CHUNK_FILE="/Users/tariqalmatrudi/NEWreader/vascular_upload/chunks/vascular_chunk_01_of_21.json"

echo "Starting simple upload test..."

# Check current vascular MCQ count
echo "Checking current MCQ count..."
heroku run "python -c \"from mcq.models import MCQ; print(f'Vascular MCQs: {MCQ.objects.filter(subspecialty=\\\"vascular_neurology\\\").count()}');\"" --app "$APP_NAME"

# Create temp file
echo "Creating temporary upload file..."
TEMP_FILE="/tmp/vascular_test.json"
cp "$CHUNK_FILE" "$TEMP_FILE"

# Upload chunk to Heroku
echo "Uploading chunk to Heroku..."
cat "$TEMP_FILE" | heroku run "cat > /tmp/test_chunk.json" --app "$APP_NAME"

# Create import script
cat > /tmp/test_import.py << 'EOF'
import json
from django.db import transaction
from mcq.models import MCQ

# Load MCQ data from temp file
with open('/tmp/test_chunk.json', 'r') as f:
    mcqs_data = json.load(f)

print(f"Importing {len(mcqs_data)} vascular MCQs")

# Import MCQs
with transaction.atomic():
    for mcq_data in mcqs_data:
        # Ensure required fields
        if 'question_text' not in mcq_data:
            print(f"Missing question_text, skipping")
            continue
            
        # Create or update MCQ
        defaults = {
            'subspecialty': mcq_data.get('subspecialty', 'vascular_neurology'),
            'question_text': mcq_data.get('question_text', ''),
            'options': mcq_data.get('options', {}),
            'correct_answer': mcq_data.get('correct_answer', ''),
            'explanation': mcq_data.get('explanation', ''),
            'exam_year': mcq_data.get('exam_year', ''),
            'exam_type': mcq_data.get('exam_type', ''),
        }
        
        # Use question_text as unique identifier
        mcq, created = MCQ.objects.update_or_create(
            question_text=mcq_data.get('question_text'),
            defaults=defaults
        )
        if created:
            print(f"Created new MCQ: {mcq_data.get('question_text')[:30]}...")
        else:
            print(f"Updated existing MCQ: {mcq_data.get('question_text')[:30]}...")

print("Import completed successfully")
EOF

# Upload import script
echo "Uploading import script..."
cat /tmp/test_import.py | heroku run "cat > /tmp/test_import.py" --app "$APP_NAME"

# Run import script
echo "Running import script..."
heroku run "python /tmp/test_import.py" --app "$APP_NAME"

# Check vascular MCQ count after import
echo "Checking updated MCQ count..."
heroku run "python -c \"from mcq.models import MCQ; print(f'Vascular MCQs: {MCQ.objects.filter(subspecialty=\\\"vascular_neurology\\\").count()}');\"" --app "$APP_NAME"

echo "Import test complete!"