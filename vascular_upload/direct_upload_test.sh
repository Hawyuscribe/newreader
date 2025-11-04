#!/bin/bash
# Simple script to test direct upload via Python API client

CURRENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CHUNK_FILE="${CURRENT_DIR}/chunks/vascular_chunk_01_of_21.json"

echo "Starting direct upload test of chunk 1..."

# Run the Python script
python3 "${CURRENT_DIR}/direct_heroku_upload.py" "$CHUNK_FILE"

echo "Direct upload test complete!"