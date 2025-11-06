#!/bin/bash
# Script to import MCQs to Heroku

# Make sure we're in the right directory
cd "$(dirname "$0")"

# Make the Python script executable
chmod +x import_mcqs_to_heroku.py

# Default options
MCQ_DIR="/Users/tariqalmatrudi/Documents/MCQs for the board/test/json f"
FIXTURES_DIR="/tmp/mcq_fixtures"
CLEAR=true
SPECIFIC_FILE=""

# Parse arguments
while [[ $# -gt 0 ]]; do
    case "$1" in
        --mcq-dir)
            MCQ_DIR="$2"
            shift 2
            ;;
        --fixtures-dir)
            FIXTURES_DIR="$2"
            shift 2
            ;;
        --no-clear)
            CLEAR=false
            shift
            ;;
        --file)
            SPECIFIC_FILE="$2"
            shift 2
            ;;
        --help)
            echo "Usage: ./import_mcqs_heroku.sh [options]"
            echo "Options:"
            echo "  --mcq-dir DIR      Directory containing MCQ JSON files (default: /Users/tariqalmatrudi/Documents/MCQs for the board/test/json f)"
            echo "  --fixtures-dir DIR Directory for generated fixtures (default: /tmp/mcq_fixtures)"
            echo "  --no-clear         Do not clear existing MCQs"
            echo "  --file FILE        Import a specific file only"
            echo "  --help             Show this help message"
            exit 0
            ;;
        *)
            echo "Unknown option: $1"
            echo "Use --help for usage information"
            exit 1
            ;;
    esac
done

# Build command
CMD="python3 import_mcqs_to_heroku.py --mcq-dir \"$MCQ_DIR\" --fixtures-dir \"$FIXTURES_DIR\""

if [[ "$CLEAR" == "false" ]]; then
    CMD="$CMD --no-clear"
fi

if [[ -n "$SPECIFIC_FILE" ]]; then
    CMD="$CMD --file \"$SPECIFIC_FILE\""
fi

# Run the command
echo "Running: $CMD"
eval "$CMD"