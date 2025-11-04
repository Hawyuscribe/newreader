#!/bin/bash
# Simple script to upload chunk 1 using the robust upload method

CURRENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CHUNK_FILE="${CURRENT_DIR}/chunks/vascular_chunk_01_of_21.json"

echo "Starting robust upload of chunk 1..."
python3 "${CURRENT_DIR}/robust_upload.py" "$CHUNK_FILE"
echo "Upload script has completed."