#!/bin/bash
# Script to continue importing MCQs from the source directory to Heroku
# This script will check the current count of MCQs and import the next batch
# Handles non-standard subspecialties by categorizing them as Other/Unclassified

# Default values
SOURCE_DIR="/Users/tariqalmatrudi/Documents/MCQs for the board/Previous MCQs/json explained"
APP_NAME="radiant-gorge-35079"
BATCH_SIZE=22  # How many files to process per run
START_BATCH=0  # Which batch to start with (0-based)
LOG_FILE="mcq_upload_continue_$(date +%Y%m%d_%H%M%S).log"

# Standard subspecialties list - ONLY these will be kept, everything else will be categorized as Other/Unclassified
VALID_SUBSPECIALTIES=(
    "Cerebrovascular/Stroke"
    "Vascular Neurology_Stroke"
    "Vascular Neurology/Stroke"
    "Neuromuscular"
    "Epilepsy"
    "Epilepsy/Seizure Disorders"
    "Movement Disorders"
    "Neurointensive Care/Neurocritical Care"
    "Critical Care Neurology"
    "Neuroimmunology"
    "Neuroimmunology/Autoimmune Neurology"
    "Neuro-otology"
    "Neurotoxicology"
    "Headache"
    "Headache Medicine"
    "Neuropsychiatry"
    "Neurogenetics"
    "Neuro-infectious"
    "Neuroinfectious Disease"
    "Neuro-oncology"
    "Neuro-ophthalmology"
    "Demyelinating/Multiple Sclerosis"
    "Sleep Neurology"
    "Cognitive/Behavioral Neurology"
    "Dementia"
    "Neuroanatomy"
    "Pediatric Neurology"
    "Other/Unclassified"
)

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case "$1" in
        --source-dir)
            SOURCE_DIR="$2"
            shift 2
            ;;
        --app)
            APP_NAME="$2"
            shift 2
            ;;
        --batch-size)
            BATCH_SIZE="$2"
            shift 2
            ;;
        --start-batch)
            START_BATCH="$2"
            shift 2
            ;;
        *)
            echo "Unknown option: $1"
            echo "Usage: $0 [--source-dir DIR] [--app APP_NAME] [--batch-size SIZE] [--start-batch INDEX]"
            exit 1
            ;;
    esac
done

# Function to print to both console and log file
log() {
    echo "$1" | tee -a "$LOG_FILE"
}

# Function to check if a subspecialty is valid
is_valid_subspecialty() {
    local subspecialty="$1"
    for valid in "${VALID_SUBSPECIALTIES[@]}"; do
        if [[ "$subspecialty" == "$valid" ]]; then
            return 0  # True, subspecialty is valid
        fi
    done
    return 1  # False, subspecialty is not valid
}

# Check if directory exists
if [ ! -d "$SOURCE_DIR" ]; then
    log "Error: Source directory not found: $SOURCE_DIR"
    exit 1
fi

# Start logging
log "=== MCQ Import Continuation ==="
log "Started at $(date)"
log "Source directory: $SOURCE_DIR"
log "App name: $APP_NAME"
log "Batch size: $BATCH_SIZE"
log "Starting with batch: $START_BATCH"
log "==========================="

# Find all JSON files in the source directory and save to a temp file
log "Finding JSON files in source directory..."
TEMP_FILES_LIST=$(mktemp)
find "$SOURCE_DIR" -name "*.json" | sort > "$TEMP_FILES_LIST"
TOTAL_FILES=$(wc -l < "$TEMP_FILES_LIST")
log "Found $TOTAL_FILES JSON files in total"

# Calculate batch information
TOTAL_BATCHES=$((($TOTAL_FILES + $BATCH_SIZE - 1) / $BATCH_SIZE))
START_INDEX=$(($START_BATCH * $BATCH_SIZE + 1))
END_INDEX=$(($START_INDEX + $BATCH_SIZE - 1))
if [ $END_INDEX -gt $TOTAL_FILES ]; then
    END_INDEX=$TOTAL_FILES
fi
CURRENT_BATCH_SIZE=$(($END_INDEX - $START_INDEX + 1))

log "Total batches: $TOTAL_BATCHES"
log "Current batch: $START_BATCH (files $START_INDEX to $END_INDEX)"
log "Current batch size: $CURRENT_BATCH_SIZE"

# Check current MCQ count
log "Checking current MCQ count on Heroku..."
MCQ_COUNT=$(heroku run --app "$APP_NAME" "python django_neurology_mcq/manage.py shell -c 'from mcq.models import MCQ; print(MCQ.objects.count())'" 2>/dev/null)
MCQ_COUNT=$(echo "$MCQ_COUNT" | head -n 1)
log "Current MCQ count: $MCQ_COUNT"

# Create custom Python script to modify JSON files
TEMP_SCRIPT=$(mktemp)
cat > "$TEMP_SCRIPT" << 'EOF'
#!/usr/bin/env python3
import json
import sys

# Standard subspecialties list
VALID_SUBSPECIALTIES = [
    "Cerebrovascular/Stroke",
    "Vascular Neurology_Stroke",
    "Vascular Neurology/Stroke",
    "Neuromuscular",
    "Epilepsy",
    "Epilepsy/Seizure Disorders",
    "Movement Disorders",
    "Neurointensive Care/Neurocritical Care",
    "Critical Care Neurology",
    "Neuroimmunology",
    "Neuroimmunology/Autoimmune Neurology",
    "Neuro-otology",
    "Neurotoxicology",
    "Headache",
    "Headache Medicine",
    "Neuropsychiatry",
    "Neurogenetics",
    "Neuro-infectious",
    "Neuroinfectious Disease",
    "Neuro-oncology",
    "Neuro-ophthalmology",
    "Demyelinating/Multiple Sclerosis",
    "Sleep Neurology",
    "Cognitive/Behavioral Neurology",
    "Dementia",
    "Neuroanatomy",
    "Pediatric Neurology",
    "Other/Unclassified"
]

def normalize_subspecialty(subspecialty):
    """Normalize subspecialty to one of the valid ones or return Other/Unclassified."""
    if not subspecialty:
        return "Other/Unclassified"
        
    # Standardize format by removing special characters and extra spaces
    normalized_input = subspecialty.lower()
    normalized_input = normalized_input.replace('-', '')
    normalized_input = normalized_input.replace('_', '')
    normalized_input = normalized_input.replace('/', '')
    normalized_input = normalized_input.replace('  ', ' ')
    normalized_input = normalized_input.strip()
    
    # Check each valid subspecialty with standardized formatting
    for valid in VALID_SUBSPECIALTIES:
        valid_normalized = valid.lower()
        valid_normalized = valid_normalized.replace('-', '')
        valid_normalized = valid_normalized.replace('_', '')
        valid_normalized = valid_normalized.replace('/', '')
        valid_normalized = valid_normalized.replace('  ', ' ')
        valid_normalized = valid_normalized.strip()
        
        # If the normalized strings match, return the properly formatted valid subspecialty
        if normalized_input == valid_normalized:
            return valid
            
    # Check specific variations that might be common
    variations = {
        # Cerebrovascular/Stroke variations
        'cerebrovascular': 'Cerebrovascular/Stroke',
        'cerebro vascular': 'Cerebrovascular/Stroke',
        'stroke': 'Cerebrovascular/Stroke',
        'vascular neurology': 'Cerebrovascular/Stroke',
        'vascularneurology': 'Cerebrovascular/Stroke',
        
        # Neuromuscular variations
        'neuromuscular': 'Neuromuscular',
        'neuro muscular': 'Neuromuscular',
        'neuropathy': 'Neuromuscular',
        'myopathy': 'Neuromuscular',
        'nmd': 'Neuromuscular',
        
        # Epilepsy variations
        'epilepsy': 'Epilepsy/Seizure Disorders',
        'seizure': 'Epilepsy/Seizure Disorders',
        'seizure disorder': 'Epilepsy/Seizure Disorders',
        
        # Movement Disorders variations
        'movement': 'Movement Disorders',
        'movement disorder': 'Movement Disorders',
        'parkinsons': 'Movement Disorders',
        'parkinson': 'Movement Disorders',
        'dystonia': 'Movement Disorders',
        'tremor': 'Movement Disorders',
        
        # Critical Care variations
        'critical care': 'Critical Care Neurology',
        'neurointensive': 'Critical Care Neurology',
        'neuro intensive': 'Critical Care Neurology',
        'neurocritical': 'Critical Care Neurology',
        'neuro critical': 'Critical Care Neurology',
        'intensive care': 'Critical Care Neurology',
        
        # Neuroimmunology variations
        'neuroimmunology': 'Neuroimmunology',
        'neuro immunology': 'Neuroimmunology',
        'autoimmune': 'Neuroimmunology',
        'immunology': 'Neuroimmunology',
        
        # Neuro-otology variations
        'neurootology': 'Neuro-otology',
        'neuro otology': 'Neuro-otology',
        'otology': 'Neuro-otology',
        'vestibular': 'Neuro-otology',
        
        # Neurotoxicology variations
        'neurotoxicology': 'Neurotoxicology',
        'neuro toxicology': 'Neurotoxicology',
        'toxicology': 'Neurotoxicology',
        
        # Headache variations
        'headache': 'Headache Medicine',
        'migraine': 'Headache Medicine',
        
        # Neuropsychiatry variations
        'neuropsychiatry': 'Neuropsychiatry',
        'neuro psychiatry': 'Neuropsychiatry',
        'psychiatry': 'Neuropsychiatry',
        
        # Neurogenetics variations
        'neurogenetics': 'Neurogenetics',
        'neuro genetics': 'Neurogenetics',
        'genetics': 'Neurogenetics',
        
        # Neuroinfectious variations
        'neuroinfectious': 'Neuroinfectious Disease',
        'neuro infectious': 'Neuroinfectious Disease',
        'infectious': 'Neuroinfectious Disease',
        'infection': 'Neuroinfectious Disease',
        'cns infection': 'Neuroinfectious Disease',
        
        # Neuro-oncology variations
        'neurooncology': 'Neuro-oncology',
        'neuro oncology': 'Neuro-oncology',
        'oncology': 'Neuro-oncology',
        'brain tumor': 'Neuro-oncology',
        'tumor': 'Neuro-oncology',
        'cancer': 'Neuro-oncology',
        
        # Neuro-ophthalmology variations
        'neuroophthalmology': 'Neuro-ophthalmology',
        'neuro ophthalmology': 'Neuro-ophthalmology',
        'ophthalmology': 'Neuro-ophthalmology',
        'eye': 'Neuro-ophthalmology',
        'visual': 'Neuro-ophthalmology',
        'vision': 'Neuro-ophthalmology',
        
        # Demyelinating/MS variations
        'demyelinating': 'Demyelinating/Multiple Sclerosis',
        'multiple sclerosis': 'Demyelinating/Multiple Sclerosis',
        'ms': 'Demyelinating/Multiple Sclerosis',
        'myelitis': 'Demyelinating/Multiple Sclerosis',
        
        # Sleep Neurology variations
        'sleep': 'Sleep Neurology',
        'sleep disorder': 'Sleep Neurology',
        'sleep medicine': 'Sleep Neurology',
        
        # Cognitive/Behavioral variations
        'cognitive': 'Cognitive/Behavioral Neurology',
        'behavioral': 'Cognitive/Behavioral Neurology',
        'behavior': 'Cognitive/Behavioral Neurology',
        'memory': 'Cognitive/Behavioral Neurology',
        
        # Dementia variations
        'dementia': 'Dementia',
        'alzheimers': 'Dementia',
        'alzheimer': 'Dementia',
        
        # Neuroanatomy variations
        'neuroanatomy': 'Neuroanatomy',
        'neuro anatomy': 'Neuroanatomy',
        'anatomy': 'Neuroanatomy',
        
        # Pediatric Neurology variations
        'pediatric': 'Pediatric Neurology',
        'pediatrics': 'Pediatric Neurology',
        'child': 'Pediatric Neurology',
        'children': 'Pediatric Neurology',
        'infant': 'Pediatric Neurology',
    }
    
    # Check for direct match in variations
    if normalized_input in variations:
        return variations[normalized_input]
    
    # Try to find a partial match in variations
    for key, value in variations.items():
        if key in normalized_input:
            return value
            
    # Default to Other/Unclassified if no match found
    return "Other/Unclassified"

def process_file(input_file):
    """Process a JSON file to normalize subspecialties."""
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    modified = False
    
    if 'mcqs' in data:
        for mcq in data['mcqs']:
            if 'subspecialty' in mcq:
                original = mcq['subspecialty']
                normalized = normalize_subspecialty(original)
                if original != normalized:
                    mcq['subspecialty'] = normalized
                    modified = True
                    print(f"Changed subspecialty from '{original}' to '{normalized}'")
    
    if modified:
        with open(input_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
        print(f"Updated {input_file} with normalized subspecialties")
    else:
        print(f"No changes needed for {input_file}")
    
    return modified

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python normalize_subspecialties.py <json_file>")
        sys.exit(1)
    
    process_file(sys.argv[1])
EOF

chmod +x "$TEMP_SCRIPT"
log "Created temporary script for normalizing subspecialties"

# Start importing files one by one for this batch
log "Starting import process for batch $START_BATCH..."
SUCCESSFUL=0
FAILED=0

# Process current batch
for ((i=START_INDEX; i<=END_INDEX; i++)); do
    # Read the file path, handling spaces correctly
    FILE=$(sed "${i}q;d" "$TEMP_FILES_LIST")
    FILENAME=$(basename "$FILE")
    TEMP_FILENAME="mcq_import_$(date +%Y%m%d_%H%M%S).json"
    
    log ""
    log "=== Processing file $i of $TOTAL_FILES (batch $START_BATCH, file $(($i - $START_INDEX + 1)) of $CURRENT_BATCH_SIZE): $FILENAME ==="
    log "Source file: $FILE"
    
    # Normalize subspecialties in the file
    log "Normalizing subspecialties in the file..."
    python3 "$TEMP_SCRIPT" "$FILE" | tee -a "$LOG_FILE"
    
    log "Temporary file name: $TEMP_FILENAME"
    
    # Upload the file to Heroku
    log "Uploading file to Heroku..."
    if cat "$FILE" | heroku run --app "$APP_NAME" "cat > $TEMP_FILENAME" 2>&1 | tee -a "$LOG_FILE"; then
        log "File uploaded successfully"
        
        # Import the file
        log "Importing file..."
        if heroku run --app "$APP_NAME" "python django_neurology_mcq/update_heroku_directly.py file $TEMP_FILENAME" 2>&1 | tee -a "$LOG_FILE"; then
            log "File imported successfully"
            SUCCESSFUL=$((SUCCESSFUL+1))
        else
            log "Error importing file"
            FAILED=$((FAILED+1))
        fi
        
        # Clean up temporary file
        log "Cleaning up temporary file..."
        heroku run --app "$APP_NAME" "rm -f $TEMP_FILENAME" 2>&1 | tee -a "$LOG_FILE"
    else
        log "Error uploading file to Heroku"
        FAILED=$((FAILED+1))
    fi
    
    # Print progress
    PROGRESS=$(( ($i - $START_INDEX + 1) * 100 / $CURRENT_BATCH_SIZE ))
    OVERALL_PROGRESS=$(( $i * 100 / $TOTAL_FILES ))
    log "Batch progress: $PROGRESS% ($(($i - $START_INDEX + 1))/$CURRENT_BATCH_SIZE)"
    log "Overall progress: $OVERALL_PROGRESS% ($i/$TOTAL_FILES)"
    log "Successful: $SUCCESSFUL, Failed: $FAILED"
    
    # Sleep between files to avoid overwhelming Heroku
    if [ $i -lt $END_INDEX ]; then
        SLEEP_TIME=30
        log "Sleeping for $SLEEP_TIME seconds before next file..."
        sleep $SLEEP_TIME
    fi
done

# Clean up temp files
rm -f "$TEMP_FILES_LIST"
rm -f "$TEMP_SCRIPT"

# Check updated MCQ count
log ""
log "Checking updated MCQ count on Heroku..."
UPDATED_MCQ_COUNT=$(heroku run --app "$APP_NAME" "python django_neurology_mcq/manage.py shell -c 'from mcq.models import MCQ; print(MCQ.objects.count())'" 2>/dev/null)
UPDATED_MCQ_COUNT=$(echo "$UPDATED_MCQ_COUNT" | head -n 1)
log "Updated MCQ count: $UPDATED_MCQ_COUNT"
log "MCQs added in this batch: $(($UPDATED_MCQ_COUNT - $MCQ_COUNT))"

# Print summary
log ""
log "=== Batch Import Summary ==="
log "Batch $START_BATCH ($START_INDEX to $END_INDEX) of $TOTAL_BATCHES completed"
log "Total files in batch: $CURRENT_BATCH_SIZE"
log "Successful imports: $SUCCESSFUL"
log "Failed imports: $FAILED"
log "Import completed at $(date)"
log "MCQ count increased from $MCQ_COUNT to $UPDATED_MCQ_COUNT"
log "See $LOG_FILE for details"

# Instructions for continuing
NEXT_BATCH=$(($START_BATCH + 1))
if [ $NEXT_BATCH -lt $TOTAL_BATCHES ]; then
    log ""
    log "To continue with the next batch, run:"
    log "./continue_mcq_import_fixed.sh --start-batch $NEXT_BATCH"
else
    log ""
    log "All batches completed!"
fi

log ""
log "Visit the site to check imported MCQs:"
log "https://$APP_NAME.herokuapp.com/"

exit 0