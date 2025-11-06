#!/bin/bash
# Script to test micro-batch upload with a single chunk

CURRENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CHUNK_FILE="${CURRENT_DIR}/chunks/vascular_chunk_01_of_21.json"
BATCH_SIZE=5

echo "Starting micro-batch upload test with chunk 1 (batch size: $BATCH_SIZE)..."
python3 "${CURRENT_DIR}/micro_batch_upload.py" "$CHUNK_FILE" $BATCH_SIZE
echo "Micro-batch upload test complete!"