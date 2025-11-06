#!/bin/bash
# Script to process specific subspecialties that have large MCQ counts, using the update_fast.py script

# Configuration
EXPORTS_DIR="explanation_exports"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
LOG_DIR="logs"

# Subspecialties to process (ordered by priority)
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

# Ensure log directory exists
mkdir -p "$LOG_DIR"

# Summary file
SUMMARY_FILE="${LOG_DIR}/update_all_subspecialties_stats_${TIMESTAMP}.json"
echo "{\"timestamp\": \"$TIMESTAMP\", \"subspecialties\": {}}" > "$SUMMARY_FILE"

# Function to find the latest export file for a subspecialty
function find_export_file() {
  local subspec="$1"
  local safe_name="${subspec// /_}"
  local latest_file=$(ls -t ${EXPORTS_DIR}/${safe_name}_explanations_*.json 2>/dev/null | head -1)
  echo "$latest_file"
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
  
  if [ "$file_size" -gt 5000000 ]; then
    batch_size=10
    pause_seconds=5
    echo "Large file detected ($((file_size/1000000))MB), using smaller batch size ($batch_size) and longer pause ($pause_seconds)s"
  elif [ "$file_size" -gt 1000000 ]; then
    batch_size=20
    pause_seconds=3
    echo "Medium file detected ($((file_size/1000000))MB), using medium batch size ($batch_size) and pause ($pause_seconds)s"
  else
    batch_size=30
    pause_seconds=2
    echo "Small file detected ($(file_size/1000))KB), using larger batch size ($batch_size) and shorter pause ($pause_seconds)s"
  fi
  
  # Safe subspecialty name for filenames
  safe_name="${subspecialty// /_}"
  log_file="${LOG_DIR}/update_stats_${safe_name}_${TIMESTAMP}.json"
  
  # Execute the update script
  echo "Running update for $subspecialty with batch size $batch_size and pause $pause_seconds seconds"
  python update_fast.py --file "$export_file" --subspecialty "$subspecialty" --batch-size $batch_size --pause $pause_seconds --log-file "$log_file"
  
  # Update the summary file
  if [ -f "$log_file" ]; then
    tmp_file=$(mktemp)
    jq --arg subspec "$subspecialty" --slurpfile stats "$log_file" '.subspecialties[$subspec] = $stats[0]' "$SUMMARY_FILE" > "$tmp_file"
    mv "$tmp_file" "$SUMMARY_FILE"
  fi
  
  echo "Completed $subspecialty"
  echo ""
  
  # Small pause between subspecialties
  sleep 2
done

echo "All subspecialties processed. Summary saved to $SUMMARY_FILE"