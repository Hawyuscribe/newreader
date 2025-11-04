#!/bin/bash
# Script to update all subspecialty explanations on Heroku

# Configuration
EXPORTS_DIR="explanation_exports"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BATCH_SIZE=20
PAUSE_SECONDS=3
LOG_DIR="logs"
STATS_FILE="${LOG_DIR}/update_all_subspecialties_stats_${TIMESTAMP}.json"

# Ensure log directory exists
mkdir -p "$LOG_DIR"

# Initialize stats file
echo "{\"timestamp\": \"$TIMESTAMP\", \"subspecialties\": {}}" > "$STATS_FILE"

# Get the latest export files
cd "$(dirname "$0")"
LATEST_EXPORT=$(ls -t ${EXPORTS_DIR}/export_stats_*.json | head -1)

if [ -z "$LATEST_EXPORT" ]; then
    echo "ERROR: No export stats file found in ${EXPORTS_DIR}/"
    exit 1
fi

echo "Using export stats from $LATEST_EXPORT"

# Process each subspecialty
for EXPORT_FILE in ${EXPORTS_DIR}/*_explanations_*.json; do
    # Extract subspecialty name from filename
    SUBSPECIALTY=$(basename "$EXPORT_FILE" | sed -E 's/(.+)_explanations_.+\.json/\1/' | tr '_' ' ')
    
    echo "============================================================"
    echo "Processing $SUBSPECIALTY"
    echo "============================================================"
    
    # Run the update script for this subspecialty
    LOG_FILE="${LOG_DIR}/update_stats_${SUBSPECIALTY//[[:space:]]/_}_${TIMESTAMP}.json"
    
    python update_heroku_explanations.py --file "$EXPORT_FILE" --subspecialty "$SUBSPECIALTY" --batch-size $BATCH_SIZE --pause $PAUSE_SECONDS
    
    # Update the stats file with the results of this subspecialty
    COUNT=$(jq length "$EXPORT_FILE")
    
    # Update the stats JSON
    TMP_FILE=$(mktemp)
    jq --arg subspec "$SUBSPECIALTY" --arg count "$COUNT" --arg file "$EXPORT_FILE" '.subspecialties[$subspec] = {"count": $count|tonumber, "file": $file}' "$STATS_FILE" > "$TMP_FILE"
    mv "$TMP_FILE" "$STATS_FILE"
    
    echo "Completed $SUBSPECIALTY"
    echo ""
done

echo "All subspecialties processed. Stats saved to $STATS_FILE"