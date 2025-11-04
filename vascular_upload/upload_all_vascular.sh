#!/bin/bash
# Script to combine all vascular chunks and upload them at once

CURRENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CHUNKS_DIR="${CURRENT_DIR}/chunks"

echo "Starting combined upload of all vascular MCQs..."
python3 "${CURRENT_DIR}/api_upload.py" --combine "$CHUNKS_DIR"
echo "Combined upload complete!"