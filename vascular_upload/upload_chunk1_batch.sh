#!/bin/bash
# Upload a tiny batch from the first chunk
# This is the most reliable way to upload MCQs to Heroku

CURRENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CHUNK_FILE="${CURRENT_DIR}/chunks/vascular_chunk_01_of_21.json"

# Process just 3 MCQs at a time, starting from the beginning
python3 "${CURRENT_DIR}/final_uploader.py" chunk "$CHUNK_FILE" 0 3