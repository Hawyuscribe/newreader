#!/bin/bash

# Script to upload MCQs to Heroku using Django management command
# This creates a temporary management command on Heroku to import MCQs

APP_NAME="radiant-gorge-35079"
SOURCE_DIR="/Users/tariqalmatrudi/Documents/MCQs for the board/Previous MCQs/json explained"
LOG_FILE="direct_upload_$(date +%Y%m%d_%H%M%S).log"

echo "Starting direct upload of MCQs to Heroku app $APP_NAME..." | tee -a "$LOG_FILE"
echo "Total files to process: $(ls -1 "$SOURCE_DIR"/*.json | wc -l | xargs)" | tee -a "$LOG_FILE"
echo "Started at $(date)" | tee -a "$LOG_FILE"
echo "-------------------------------------------------" | tee -a "$LOG_FILE"

# First, run the sample import to get familiar data
echo "Running initial sample import..." | tee -a "$LOG_FILE"
heroku run python django_neurology_mcq/update_heroku_directly.py sample -a $APP_NAME > /tmp/sample_output.log
if [ $? -eq 0 ]; then
    echo "Sample import successful" | tee -a "$LOG_FILE"
else
    echo "Sample import failed. Check connection to Heroku" | tee -a "$LOG_FILE"
    exit 1
fi

# Create a simple import management command on Heroku
echo "Creating import management command on Heroku..." | tee -a "$LOG_FILE"

# Use a temporary script file
TEMP_SCRIPT=$(mktemp)

cat > $TEMP_SCRIPT << 'EOF'
import os
import json
from django.core.management.base import BaseCommand
from django.db import transaction
from mcq.models import MCQ

class Command(BaseCommand):
    help = 'Import MCQs from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('json_data', type=str, help='JSON string containing MCQs')

    def handle(self, *args, **options):
        json_data = options['json_data']
        
        try:
            data = json.loads(json_data)
            
            if 'mcqs' not in data or not isinstance(data['mcqs'], list):
                self.stdout.write(self.style.ERROR('Invalid JSON format. Missing "mcqs" array.'))
                return
            
            mcqs_data = data['mcqs']
            self.stdout.write(f"Found {len(mcqs_data)} MCQs in the data")
            
            imported_count = 0
            
            with transaction.atomic():
                for mcq_data in mcqs_data:
                    # Extract required fields or set defaults
                    question_number = mcq_data.get('question_number', f"Q{imported_count+1}")
                    question_text = mcq_data.get('question_text', '')
                    options = mcq_data.get('options', {})
                    
                    # Handle options in list format
                    if isinstance(options, list):
                        options_dict = {}
                        for option in options:
                            if isinstance(option, dict) and 'letter' in option and 'text' in option:
                                options_dict[option['letter']] = option['text']
                        options = options_dict
                        
                    # Handle correct answers - prioritize verified answers
                    correct_answer = mcq_data.get('verified_answer', '') or mcq_data.get('correct_answer', '')
                    
                    # Get explanation sections or empty dict
                    explanation_sections = mcq_data.get('explanation_sections', {})
                    
                    # Get subspecialty or default
                    subspecialty = mcq_data.get('subspecialty', '')
                    if not subspecialty:
                        subspecialty = mcq_data.get('primary_category', 'Other/Unclassified')
                    
                    # Create and save the MCQ
                    mcq = MCQ(
                        question_number=question_number,
                        question_text=question_text,
                        options=options,
                        correct_answer=correct_answer,
                        explanation=mcq_data.get('answer_explanation', ''),
                        explanation_sections=explanation_sections,
                        subspecialty=subspecialty,
                        primary_category=mcq_data.get('primary_category', ''),
                        secondary_category=mcq_data.get('secondary_category', ''),
                        exam_type=mcq_data.get('exam_type', ''),
                        exam_year=mcq_data.get('exam_year', None),
                        source_file=mcq_data.get('source_file', ''),
                        verification_confidence=mcq_data.get('verification_confidence', '')
                    )
                    mcq.save()
                    imported_count += 1
                    
            self.stdout.write(self.style.SUCCESS(f"Successfully imported {imported_count} MCQs"))
            
        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR('Invalid JSON data format'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error importing MCQs: {str(e)}'))
EOF

# Create the management command on Heroku
heroku run bash -a $APP_NAME << HEROKUCMD
mkdir -p django_neurology_mcq/mcq/management/commands
cat > django_neurology_mcq/mcq/management/commands/import_json.py << 'CMDEOF'
$(cat $TEMP_SCRIPT)
CMDEOF

# Create __init__.py files
touch django_neurology_mcq/mcq/management/__init__.py
touch django_neurology_mcq/mcq/management/commands/__init__.py

# Show the created file
ls -la django_neurology_mcq/mcq/management/commands/
HEROKUCMD

# Process each MCQ file
for FILE in "$SOURCE_DIR"/*.json; do
    FILENAME=$(basename "$FILE")
    echo "Processing $FILENAME..." | tee -a "$LOG_FILE"
    
    # Extract exam info from filename
    EXAM_TYPE=""
    EXAM_YEAR=""
    
    if [[ $FILENAME =~ [Pp]art\ *[Ii]{1,2} ]]; then
        if [[ $FILENAME =~ [Pp]art\ *[Ii]{2} || $FILENAME =~ [Pp]art\ *2 ]]; then
            EXAM_TYPE="Part II"
        else
            EXAM_TYPE="Part I"
        fi
    elif [[ $FILENAME =~ [Pp]romotion ]]; then
        EXAM_TYPE="Promotion"
    fi
    
    if [[ $FILENAME =~ 20[0-9]{2} ]]; then
        EXAM_YEAR=$(echo $FILENAME | grep -o -E '20[0-9]{2}' | head -1)
    fi
    
    echo "  Detected: Exam Type=$EXAM_TYPE, Year=$EXAM_YEAR" | tee -a "$LOG_FILE"
    
    # Process the file in smaller batches
    python3 -c "
import json
import subprocess
import sys

# Load the file
with open('$FILE', 'r') as f:
    data = json.load(f)

# Add exam info to each MCQ if detected
if '$EXAM_TYPE' or '$EXAM_YEAR':
    for mcq in data['mcqs']:
        if '$EXAM_TYPE':
            mcq['exam_type'] = '$EXAM_TYPE'
        if '$EXAM_YEAR':
            mcq['exam_year'] = int('$EXAM_YEAR')
        mcq['source_file'] = '$FILENAME'

# Count MCQs
mcq_count = len(data['mcqs'])
print(f'Found {mcq_count} MCQs in {repr('$FILENAME')}')

# Process in batches of 20 MCQs
BATCH_SIZE = 20
for i in range(0, mcq_count, BATCH_SIZE):
    batch = {'mcqs': data['mcqs'][i:i+BATCH_SIZE]}
    batch_num = i // BATCH_SIZE + 1
    batch_count = (mcq_count + BATCH_SIZE - 1) // BATCH_SIZE
    print(f'Processing batch {batch_num}/{batch_count} with {len(batch['mcqs'])} MCQs')
    
    # Convert to JSON string for command line
    json_str = json.dumps(batch).replace('\"', '\\\"')
    
    # Run the import command on Heroku
    cmd = ['heroku', 'run', f'python manage.py import_json \"{json_str}\"', '-a', '$APP_NAME']
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f'Error importing batch {batch_num}: {result.stderr}')
        sys.exit(1)
    
    print(f'Batch {batch_num}/{batch_count} imported successfully')
    
    # Add a brief delay to avoid overwhelming Heroku
    import time
    time.sleep(2)

print(f'Successfully processed all {mcq_count} MCQs from {repr('$FILENAME')}')
" | tee -a "$LOG_FILE"
    
    echo "Completed processing $FILENAME" | tee -a "$LOG_FILE"
    echo "-------------------------------------------------" | tee -a "$LOG_FILE"
done

# Run final validation
echo "Upload process completed. Running final validation..." | tee -a "$LOG_FILE"
heroku run python django_neurology_mcq/update_heroku_directly.py validate -a $APP_NAME | tee -a "$LOG_FILE"

echo "Completed at $(date)" | tee -a "$LOG_FILE"
echo "See $LOG_FILE for detailed log."

# Clean up
rm $TEMP_SCRIPT