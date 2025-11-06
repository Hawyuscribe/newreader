#!/bin/bash
# Script to upload all vascular chunks via Django loaddata

CURRENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CHUNKS_DIR="${CURRENT_DIR}/chunks"

echo "Starting upload of all vascular MCQ chunks via Django loaddata..."
python3 "${CURRENT_DIR}/loaddata_upload.py" --all "$CHUNKS_DIR"
echo "All chunks upload complete!"