#!/bin/bash
# Script to process all subspecialties using the question-matching approach

# Configuration
EXPORTS_DIR="explanation_exports"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
LOG_DIR="logs"
SUMMARY_FILE="${LOG_DIR}/update_all_subspecialties_stats_${TIMESTAMP}.json"

# Ensure log directory exists
mkdir -p "$LOG_DIR"

# Initialize stats file
echo "{\"timestamp\": \"$TIMESTAMP\", \"subspecialties\": {}}" > "$SUMMARY_FILE"

# List of subspecialties to process
subspecialties=(
  "Critical Care Neurology"
  "Sleep Neurology"
  "Epilepsy"
  "Dementia"
  "Headache"
  "Movement Disorders"
  "Neuro-infectious"
  "Neuroanatomy"
  "Neurogenetics"
  "Neuroimmunology"
  "Neuro oncology"
  "Neuro otology"
  "Neuroophthalmology"
  "Neuropsychiatry"
  "Neurotoxicology"
  "Neuromuscular"
  "Other Unclassified"
  "Pediatric Neurology"
  "Vascular Neurology Stroke"
)

# Function to find the latest export file for a subspecialty
function find_export_file() {
  local subspec="$1"
  local safe_name="${subspec// /_}"
  local latest_file=$(ls -t ${EXPORTS_DIR}/${safe_name}_explanations_*.json 2>/dev/null | head -1)
  echo "$latest_file"
}

# Function to determine batch size and pause time based on file size
function get_batch_config() {
  local file_size="$1"
  local result=""
  
  if [ "$file_size" -gt 5000000 ]; then
    # Large files (5MB+)
    echo "10 5"  # batch size 10, pause 5s
  elif [ "$file_size" -gt 1000000 ]; then
    # Medium files (1MB-5MB)
    echo "15 3"  # batch size 15, pause 3s
  else
    # Small files (<1MB)
    echo "20 2"  # batch size 20, pause 2s
  fi
}

# Process each subspecialty
for subspecialty in "${subspecialties[@]}"; do
  echo "============================================================"
  echo "Processing $subspecialty"
  echo "============================================================"
  
  # Find the export file
  export_file=$(find_export_file "$subspecialty")
  if [ -z "$export_file" ]; then
    echo "WARNING: No export file found for $subspecialty, skipping"
    continue
  fi
  
  echo "Using export file: $export_file"
  
  # Determine batch size based on subspecialty size
  file_size=$(wc -c < "$export_file")
  echo "File size: $file_size bytes"
  
  # Get batch size and pause time
  batch_config=$(get_batch_config "$file_size")
  batch_size=$(echo "$batch_config" | cut -d' ' -f1)
  pause_seconds=$(echo "$batch_config" | cut -d' ' -f2)
  
  # Safe subspecialty name for filenames
  safe_name="${subspecialty// /_}"
  log_file="${LOG_DIR}/update_stats_${safe_name}_${TIMESTAMP}.json"
  
  # Execute the update script
  echo "Running update for $subspecialty with batch size $batch_size and pause $pause_seconds seconds"
  python update_by_question.py --file "$export_file" --subspecialty "$subspecialty" \
    --batch-size "$batch_size" --pause "$pause_seconds" --log-file "$log_file"
  
  # Update the summary file
  if [ -f "$log_file" ]; then
    tmp_file=$(mktemp)
    jq --arg subspec "$subspecialty" --slurpfile stats "$log_file" '.subspecialties[$subspec] = $stats[0]' "$SUMMARY_FILE" > "$tmp_file"
    mv "$tmp_file" "$SUMMARY_FILE"
  fi
  
  echo "Completed $subspecialty"
  echo ""
  
  # Wait a bit between subspecialties to let the system rest
  sleep 5
done

echo "All subspecialties processed. Summary saved to $SUMMARY_FILE"

# Run verification at the end
echo "Running verification to check updated explanation status..."
python verify_heroku_explanations.py