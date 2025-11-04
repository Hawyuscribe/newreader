#!/bin/bash
# Script to test API-based upload with a single chunk

CURRENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CHUNK_FILE="${CURRENT_DIR}/chunks/vascular_chunk_01_of_21.json"

echo "Starting API-based upload test with chunk 1..."
python3 "${CURRENT_DIR}/api_upload.py" "$CHUNK_FILE"
echo "API upload test complete!"