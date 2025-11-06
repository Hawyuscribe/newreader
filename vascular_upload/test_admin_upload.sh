#!/bin/bash
# Script to test Django admin-based upload with a single chunk

CURRENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CHUNK_FILE="${CURRENT_DIR}/chunks/vascular_chunk_01_of_21.json"

echo "Starting Django admin-based upload test with chunk 1..."
python3 "${CURRENT_DIR}/admin_upload.py" "$CHUNK_FILE"
echo "Admin upload test complete!"