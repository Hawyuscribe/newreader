#!/bin/bash
# Script to upload all chunks one by one using the robust method

CURRENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CHUNKS_DIR="${CURRENT_DIR}/chunks"

# Get all chunk files
CHUNK_FILES=($(find "$CHUNKS_DIR" -name "vascular_chunk_*.json" | sort))

echo "Found ${#CHUNK_FILES[@]} chunk files to process"

# Process each chunk
for (( i=0; i<${#CHUNK_FILES[@]}; i++ )); do
    CHUNK="${CHUNK_FILES[$i]}"
    CHUNK_NAME=$(basename "$CHUNK")
    
    echo "=========================================="
    echo "Processing chunk $((i+1))/${#CHUNK_FILES[@]}: $CHUNK_NAME"
    echo "=========================================="
    
    # Upload the chunk
    python3 "${CURRENT_DIR}/robust_upload.py" "$CHUNK"
    
    # Wait between chunks
    if [ $i -lt $((${#CHUNK_FILES[@]}-1)) ]; then
        echo "Waiting 30 seconds before processing next chunk..."
        sleep 30
    fi
done

echo "All chunks have been processed!"