#!/bin/bash
# Script to test Django management command upload with a single chunk

CURRENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CHUNK_FILE="${CURRENT_DIR}/chunks/vascular_chunk_01_of_21.json"

echo "Starting Django management command upload test with chunk 1..."
python3 "${CURRENT_DIR}/heroku_django_upload.py" "$CHUNK_FILE"
echo "Django upload test complete!"