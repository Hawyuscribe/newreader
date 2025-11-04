#!/bin/bash
# Script to upload all vascular chunks in micro-batches of 10 MCQs

CURRENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CHUNKS_DIR="${CURRENT_DIR}/chunks"
BATCH_SIZE=10

echo "Starting upload of all vascular MCQ chunks in micro-batches of $BATCH_SIZE..."
python3 "${CURRENT_DIR}/micro_batch_upload.py" --all "$CHUNKS_DIR" $BATCH_SIZE
echo "All chunks upload complete!"