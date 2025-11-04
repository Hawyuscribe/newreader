#!/bin/bash
# Script to directly import MCQs from JSON files to Heroku

APP_NAME="radiant-gorge-35079"
JSON_DIR="/Users/tariqalmatrudi/Documents/MCQs for the board/test"

echo "===== DIRECT HEROKU MCQ IMPORT ====="
echo "Started at: $(date)"
echo ""

# Clear all existing MCQs on Heroku first
echo "Clearing existing MCQs on Heroku..."
heroku run --app $APP_NAME "cd /app/django_neurology_mcq && python manage.py shell -c 'from mcq.models import MCQ; count = MCQ.objects.count(); print(f\"Deleting {count} MCQs...\"); MCQ.objects.all().delete(); print(\"Done\")'"

# Find all JSON files (excluding backups)
echo "Finding JSON files to import..."
JSON_FILES=$(find "$JSON_DIR" -name "*.json" | grep -v "bak_" | sort)
TOTAL_FILES=$(echo "$JSON_FILES" | wc -l)
echo "Found $TOTAL_FILES JSON files to import"

# Function to extract subspecialty from filename
extract_subspecialty() {
    local filename=$(basename "$1")
    # Extract the part before _mcqs
    local subspecialty=$(echo "$filename" | sed -E 's/(.*)_mcqs.*/\1/')
    echo "$subspecialty"
}

# Create upload script for Heroku
cat > /tmp/heroku_mcq_importer.py << 'EOF'
import json
import sys
import os
from django.db import transaction
from django.conf import settings
from mcq.models import MCQ

def import_mcqs_from_json(json_file_path, subspecialty_override=None):
    """Import MCQs from a JSON file."""
    print(f"Reading JSON file: {json_file_path}")
    
    try:
        with open(json_file_path, 'r') as f:
            mcq_data = json.load(f)
        
        # Two possible formats:
        # 1. A list of MCQs
        # 2. A dict with 'mcqs' key containing a list
        if isinstance(mcq_data, list):
            mcqs = mcq_data
        elif isinstance(mcq_data, dict) and 'mcqs' in mcq_data:
            mcqs = mcq_data['mcqs']
            # Use specialty from file if no override provided
            if subspecialty_override is None and 'specialty' in mcq_data:
                subspecialty_override = mcq_data['specialty']
        else:
            print("Invalid JSON format - expected list or dict with 'mcqs' key")
            return 0
        
        print(f"Found {len(mcqs)} MCQs to import")
        
        # Start a transaction
        imported_count = 0
        error_count = 0
        
        with transaction.atomic():
            for mcq_item in mcqs:
                try:
                    # Handle subspecialty - use override if provided
                    if subspecialty_override:
                        mcq_item['subspecialty'] = normalize_subspecialty(subspecialty_override)
                    elif 'subspecialty' not in mcq_item:
                        mcq_item['subspecialty'] = 'Other/Unclassified'
                    
                    # Convert options to proper format
                    options = mcq_item.get('options', {})
                    if not isinstance(options, dict):
                        options_dict = {}
                        for i, option in enumerate(options):
                            if isinstance(option, dict):
                                letter = option.get('letter', chr(65 + i))
                                text = option.get('text', '')
                                options_dict[letter] = text
                            elif isinstance(option, str):
                                letter = chr(65 + i)
                                options_dict[letter] = option
                        mcq_item['options'] = options_dict
                    
                    # Create the MCQ
                    MCQ.objects.create(
                        id=mcq_item.get('id'),
                        question_number=mcq_item.get('question_number'),
                        question_text=mcq_item.get('question_text', ''),
                        options=mcq_item.get('options', {}),
                        correct_answer=mcq_item.get('correct_answer', ''),
                        subspecialty=mcq_item.get('subspecialty'),
                        exam_type=mcq_item.get('exam_type', 'Other'),
                        exam_year=mcq_item.get('exam_year'),
                        explanation=mcq_item.get('explanation', mcq_item.get('answer_explanation', '')),
                        explanation_sections=mcq_item.get('explanation_sections', {}),
                        source_file=os.path.basename(json_file_path),
                        image_url=mcq_item.get('image_url', mcq_item.get('source_image')),
                        verification_confidence=mcq_item.get('verification_confidence'),
                        primary_category=mcq_item.get('primary_category'),
                        secondary_category=mcq_item.get('secondary_category'),
                        key_concept=mcq_item.get('key_concept'),
                        difficulty_level=mcq_item.get('difficulty_level'),
                    )
                    imported_count += 1
                    
                    # Progress display
                    if imported_count % 50 == 0:
                        print(f"Imported {imported_count} MCQs...")
                        
                except Exception as e:
                    error_count += 1
                    print(f"Error importing MCQ: {str(e)[:100]}")
        
        print(f"Import completed: {imported_count} imported, {error_count} errors")
        return imported_count
    
    except Exception as e:
        print(f"Error opening or parsing JSON file: {e}")
        return 0

def normalize_subspecialty(specialty):
    """Map a subspecialty name to the standard format."""
    # Mapping based on the SUBSPECIALTY_MAPPING in import_rere_fixed.py
    mapping = {
        'anatomy': 'Neuroanatomy',
        'critical_care_neurology': 'Critical Care Neurology',
        'dementia': 'Dementia',
        'epilepsy': 'Epilepsy',
        'headache': 'Headache',
        'movement_disorders': 'Movement Disorders',
        'neuro-otology': 'Neuro-otology',
        'neurogenetics': 'Neurogenetics',
        'neuroimmunology': 'Neuroimmunology',
        'neuroinfectious': 'Neuro-infectious',
        'neuro_infectious': 'Neuro-infectious',
        'neuromuscular': 'Neuromuscular',
        'neurooncology': 'Neuro-oncology',
        'neuro-oncology': 'Neuro-oncology',
        'neuroophthalmology': 'Neuroophthalmology',
        'neuropsychiatry': 'Neuropsychiatry',
        'neurotoxicology': 'Neurotoxicology',
        'other': 'Other/Unclassified',
        'other_unclassified': 'Other/Unclassified',
        'pediatric_neurology': 'Pediatric Neurology',
        'sleep_neurology': 'Sleep Neurology',
        'vascular_neurology': 'Vascular Neurology/Stroke',
        'vascular neurology': 'Vascular Neurology/Stroke',
        'vascular_neurology_stroke': 'Vascular Neurology/Stroke',
        'vascular': 'Vascular Neurology/Stroke',
    }
    
    # Normalize the input
    specialty_key = specialty.lower().replace(' ', '_')
    
    # Return the mapped value or the original if not found
    return mapping.get(specialty_key, specialty)

# Main entry point
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python import_mcqs.py <json_file_path> [subspecialty_override]")
        sys.exit(1)
    
    json_file_path = sys.argv[1]
    subspecialty_override = None
    if len(sys.argv) > 2:
        subspecialty_override = sys.argv[2]
    
    import_count = import_mcqs_from_json(json_file_path, subspecialty_override)
    print(f"Successfully imported {import_count} MCQs")
EOF

# Upload the importer script to Heroku
echo "Uploading import script to Heroku..."
cat /tmp/heroku_mcq_importer.py | heroku run --app $APP_NAME "cat > /app/django_neurology_mcq/mcq_importer.py"

# Import each JSON file
counter=0
total_mcqs=0

echo "$JSON_FILES" | while read -r json_file; do
    counter=$((counter + 1))
    filename=$(basename "$json_file")
    subspecialty=$(extract_subspecialty "$json_file")
    
    echo ""
    echo "[$counter/$TOTAL_FILES] Processing $filename (Subspecialty: $subspecialty)..."
    
    # Upload JSON to Heroku
    echo "Uploading file to Heroku..."
    cat "$json_file" | heroku run --app $APP_NAME "cat > /tmp/import_data.json"
    
    # Run the import script
    echo "Importing MCQs..."
    import_result=$(heroku run --app $APP_NAME "cd /app/django_neurology_mcq && python -c 'import mcq_importer; mcq_importer.import_mcqs_from_json(\"/tmp/import_data.json\", \"$subspecialty\")'")
    
    # Extract the number of imported MCQs
    imported=$(echo "$import_result" | grep "Successfully imported" | grep -o '[0-9]\+')
    if [ -n "$imported" ]; then
        total_mcqs=$((total_mcqs + imported))
        echo "✓ Successfully imported $imported MCQs from $filename"
    else
        echo "✗ Failed to import MCQs from $filename"
        echo "$import_result"
    fi
done

# Verify import
echo ""
echo "Verifying import..."
heroku run --app $APP_NAME "cd /app/django_neurology_mcq && python manage.py shell -c '
from mcq.models import MCQ
from django.db.models import Count

total = MCQ.objects.count()
print(f\"\\nTotal MCQs: {total}\")

print(\"\\nMCQs by Subspecialty:\")
subspecialties = MCQ.objects.values(\"subspecialty\").annotate(count=Count(\"id\")).order_by(\"-count\")
for item in subspecialties:
    print(f\"  {item[\"subspecialty\"]}: {item[\"count\"]}\")

# Check correct answers
with_correct = MCQ.objects.exclude(correct_answer=\"\").count()
print(f\"\\nMCQs with correct answers: {with_correct} ({with_correct/total*100:.1f}% if total > 0 else 0}%)\")

# Check explanations
with_exp = MCQ.objects.exclude(explanation=\"\").count()
print(f\"MCQs with explanations: {with_exp} ({with_exp/total*100:.1f}% if total > 0 else 0}%)\")
'"

echo ""
echo "===== IMPORT COMPLETED ====="
echo "Total MCQs imported: $total_mcqs"
echo "Completed at: $(date)"