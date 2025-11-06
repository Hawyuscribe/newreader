#!/bin/bash
# Script to specifically import MCQs from the reclassified folder to Heroku database

# Configuration
APP_NAME="radiant-gorge-35079"
SOURCE_DIR="/Users/tariqalmatrudi/Documents/MCQs for the board/Classified MCQs/reclassified"
LOCAL_TEMP_DIR="/Users/tariqalmatrudi/NEWreader/temp_mcqs_chunks"
BATCH_SIZE=50  # Number of MCQs per JSON chunk

echo "=== Reclassified MCQ Import to Heroku Database ==="
echo "This script will import reclassified MCQs to the Heroku database."
echo "Source directory: $SOURCE_DIR"
echo "App name: $APP_NAME"
echo ""

# Check if the source directory exists
if [ ! -d "$SOURCE_DIR" ]; then
    echo "Error: Source directory does not exist."
    exit 1
fi

# Create local temp directory if it doesn't exist
mkdir -p "$LOCAL_TEMP_DIR"

# Step 1: Ensure management commands are pushed to Heroku
echo "Step 1: Pushing management commands to Heroku..."
git add django_neurology_mcq/mcq/management/commands/import_mcqs_chunked.py
git commit -m "Update MCQ import commands" || echo "No changes to commit"
git push heroku master

# Step 2: Create a simple Python script to convert a single text file to JSON
cat > "$LOCAL_TEMP_DIR/convert_file_to_json.py" << 'PYTHON_SCRIPT'
import os
import re
import json
import sys

# Usage: python convert_file_to_json.py <input_file> <output_file>
def main():
    if len(sys.argv) != 3:
        print("Usage: python convert_file_to_json.py <input_file> <output_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    # Extract subspecialty from filename
    filename = os.path.basename(input_file)
    subspecialty = os.path.splitext(filename)[0].replace('_', ' ')
    
    # Map of subspecialty adjustments
    subspecialty_map = {
        "Critical Care Neurology": "Critical Care Neurology",
        "Dementia": "Dementia", 
        "Epilepsy": "Epilepsy",
        "Headache": "Headache",
        "Movement Disorders": "Movement Disorders",
        "Neuro infectious": "Neuro infectious",
        "Neuro oncology": "Neuro oncology",
        "Neuro otology": "Neuro otology",
        "Neuroanatomy": "Neuroanatomy",
        "Neurogenetics": "Neurogenetics",
        "Neuroimmunology": "Neuroimmunology",
        "Neuromuscular": "Neuromuscular",
        "Neuroophthalmology": "Neuroophthalmology", 
        "Neuropsychiatry": "Neuropsychiatry",
        "Neurotoxicology": "Neurotoxicology",
        "Other Unclassified": "Other/Unclassified",
        "Pediatric Neurology": "Pediatric Neurology",
        "Sleep Neurology": "Sleep Neurology",
        "Vascular neurology stroke": "Vascular neurology stroke"
    }
    
    if subspecialty in subspecialty_map:
        subspecialty = subspecialty_map[subspecialty]
    
    print(f"Processing file: {input_file}")
    print(f"Detected subspecialty: {subspecialty}")
    
    # Read the file content
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Define our separator pattern
    separator = '--------------------------------------------------'
    
    # Skip the header (first line or two)
    if "==" in content.split('\n')[0]:
        content = '\n'.join(content.split('\n')[1:])
    
    # Split by the separator
    mcq_blocks = content.split(separator)
    
    # Parse all MCQ blocks
    mcqs = []
    for mcq_block in mcq_blocks:
        if not mcq_block.strip():
            continue
        
        mcq_data = parse_mcq_block(mcq_block, subspecialty)
        if mcq_data:
            mcqs.append(mcq_data)
    
    print(f"Found {len(mcqs)} MCQs in file")
    
    # Write to output file
    with open(output_file, 'w') as f:
        json.dump(mcqs, f)
    
    print(f"Saved {len(mcqs)} MCQs to {output_file}")

def parse_mcq_block(mcq_block, file_subspecialty=None):
    """Parse an MCQ block to extract its data."""
    if not mcq_block.strip():
        return None
        
    lines = mcq_block.strip().split('\n')
    if not lines:
        return None
    
    # Initialize MCQ data
    mcq_data = {
        "question_number": None,
        "question_text": "",
        "options": {},
        "correct_answer": None,
        "source_file": "",
        "exam_type": None,
        "exam_year": None,
        "subspecialty": file_subspecialty or "Other/Unclassified",
        "explanation": ""
    }
    
    # Extract question number and source
    question_match = re.search(r'Q(\d+)\.?\s*(?:\(Source:\s*(.*?)\))?', lines[0])
    if not question_match:
        # Try alternative formats
        alt_match = re.search(r'Q\.?\s*(\d+)|Question\s*(\d+)', lines[0], re.IGNORECASE)
        if alt_match:
            question_num = alt_match.group(1) or alt_match.group(2)
            mcq_data["question_number"] = f"Q{question_num}"
            # Look for source in the first few lines
            for i in range(min(3, len(lines))):
                source_search = re.search(r'Source:\s*(.*?)(?:\s|$)', lines[i], re.IGNORECASE)
                if source_search:
                    mcq_data["source_file"] = source_search.group(1).strip()
                    break
        else:
            # If we still can't find a question number, skip this block
            return None
    else:
        mcq_data["question_number"] = f"Q{question_match.group(1)}"
        mcq_data["source_file"] = question_match.group(2).strip() if question_match.group(2) else ""
    
    # Extract exam type and year from source
    source_file = mcq_data["source_file"]
    
    # More comprehensive pattern matching for exam type
    if re.search(r'Part\s*I\b|Part\s*1\b', source_file, re.IGNORECASE):
        mcq_data["exam_type"] = "Part I"
    elif re.search(r'Part\s*II\b|Part\s*2\b|part\s*2\b|part\s*II\b', source_file, re.IGNORECASE):
        mcq_data["exam_type"] = "Part II"
    elif re.search(r'Promotion', source_file, re.IGNORECASE):
        mcq_data["exam_type"] = "Promotion"
    elif re.search(r'ABPN', source_file, re.IGNORECASE):
        mcq_data["exam_type"] = "ABPN Board"
    
    # Extract year with improved pattern
    year_match = re.search(r'20\d{2}', source_file)
    if year_match:
        mcq_data["exam_year"] = int(year_match.group(0))
    
    # Extract question text with improved handling for different formats
    question_text = ""
    line_index = 1
    
    # Skip any empty lines at the beginning
    while line_index < len(lines) and not lines[line_index].strip():
        line_index += 1
    
    # Read until we hit something that looks like an option (A., A:, etc.)
    while line_index < len(lines):
        line = lines[line_index].strip()
        # Stop if we hit an option line
        if re.match(r'^[A-E][\.\)\-:\s]', line):
            break
        # Add non-empty lines to question text
        if line:
            question_text += line + " "
        line_index += 1
    
    mcq_data["question_text"] = question_text.strip()
    
    # Extract options and correct answer with improved handling
    options = {}
    correct_answer = None
    
    while line_index < len(lines) and lines[line_index].strip() and not lines[line_index].strip().startswith('*'):
        line = lines[line_index].strip()
        
        # Match various option formats: A., A), A-, etc.
        option_match = re.match(r'^([A-E])[\.\)\-:\s]\s*(.*)', line)
        
        if option_match:
            option_letter = option_match.group(1)
            option_text = option_match.group(2).strip()
            
            # Check for [CORRECT] marker in different formats
            if re.search(r'\[CORRECT\]|\(CORRECT\)|CORRECT', option_text, re.IGNORECASE):
                correct_answer = option_letter
                # Remove any correct markers with different bracket types
                option_text = re.sub(r'\s*[\[\(]CORRECT[\]\)]|\s*CORRECT', '', option_text, flags=re.IGNORECASE).strip()
            
            options[option_letter] = option_text
        elif line and line_index > 0 and options:
            # This might be a continuation of the previous option
            last_option = list(options.keys())[-1]
            options[last_option] += " " + line
        
        line_index += 1
    
    # If no correct answer was found but there's a CORRECT ANSWER: line, check for that
    if not correct_answer:
        for line in lines:
            correct_match = re.search(r'CORRECT\s+ANSWER\s*:\s*([A-E])', line, re.IGNORECASE)
            if correct_match:
                correct_answer = correct_match.group(1)
                break
    
    # Convert options to JSON string for storage
    mcq_data["options"] = options
    mcq_data["correct_answer"] = correct_answer or "A"  # Default to A if no correct answer found
    
    return mcq_data

if __name__ == "__main__":
    main()
PYTHON_SCRIPT

# Step 3: Create a JSON file locally with the MCQs for direct DB import
echo "Step 3: Creating one large JSON file with all MCQs..."

# Get the list of text files in the source directory, excluding logs and backup
txt_files=()
for file in "$SOURCE_DIR"/*.txt; do
    # Skip backup directory, debug logs, and reclassification logs
    if [[ "$file" != *"debug_log.txt"* && "$file" != *"reclassification_log.txt"* ]]; then
        txt_files+=("$file")
    fi
done

total_files=${#txt_files[@]}
echo "Found $total_files text files to process"

# Create a directory for the all MCQs
ALL_MCQS_DIR="$LOCAL_TEMP_DIR/all_mcqs"
mkdir -p "$ALL_MCQS_DIR"

# Process each file to generate JSON
for ((i=0; i<total_files; i++)); do
    file="${txt_files[$i]}"
    filename=$(basename "$file")
    json_filename="${filename%.txt}.json"
    json_path="$ALL_MCQS_DIR/$json_filename"
    
    echo "Processing file $((i+1))/$total_files: $filename"
    
    # Convert to JSON
    python "$LOCAL_TEMP_DIR/convert_file_to_json.py" "$file" "$json_path"
done

# Create a main export file of all MCQs
echo "Combining all MCQs into a single JSON file..."
all_mcqs_file="$LOCAL_TEMP_DIR/mcqs_export.json"

# Combine all JSON files into one array
echo "[" > "$all_mcqs_file"
first_file=true

for json_file in "$ALL_MCQS_DIR"/*.json; do
    if [ "$first_file" = true ]; then
        first_file=false
    else
        echo "," >> "$all_mcqs_file"
    fi
    
    # Get file content without the outer brackets and append
    cat "$json_file" | sed '1s/^\[//' | sed '$s/\]$//' >> "$all_mcqs_file"
done

echo "]" >> "$all_mcqs_file"
echo "Created combined JSON file with all MCQs"

# Step 4: Break the large file into smaller chunks
echo "Step 4: Breaking into smaller chunks for upload..."
CHUNK_SIZE=100
CHUNKS_DIR="$LOCAL_TEMP_DIR/chunks"
mkdir -p "$CHUNKS_DIR"

# Create a Python script to split the file
cat > "$LOCAL_TEMP_DIR/split_json.py" << 'PYTHON_SCRIPT'
import json
import sys
import os
import math

def main():
    if len(sys.argv) != 4:
        print("Usage: python split_json.py <input_file> <output_dir> <chunk_size>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_dir = sys.argv[2]
    chunk_size = int(sys.argv[3])
    
    with open(input_file, 'r') as f:
        mcqs = json.load(f)
    
    total_mcqs = len(mcqs)
    total_chunks = math.ceil(total_mcqs / chunk_size)
    
    print(f"Splitting {total_mcqs} MCQs into {total_chunks} chunks")
    
    # Create manifest
    manifest = {
        'total_mcqs': total_mcqs,
        'total_chunks': total_chunks,
        'chunk_files': []
    }
    
    for i in range(total_chunks):
        start_idx = i * chunk_size
        end_idx = min((i + 1) * chunk_size, total_mcqs)
        
        chunk = mcqs[start_idx:end_idx]
        chunk_file = f"mcqs_chunk_{i+1}_of_{total_chunks}.json"
        chunk_path = os.path.join(output_dir, chunk_file)
        
        with open(chunk_path, 'w') as f:
            json.dump(chunk, f)
        
        manifest['chunk_files'].append(chunk_file)
        print(f"Created chunk {i+1}/{total_chunks} with {len(chunk)} MCQs")
    
    # Write manifest
    manifest_path = os.path.join(output_dir, "export_manifest.json")
    with open(manifest_path, 'w') as f:
        json.dump(manifest, f, indent=2)
    
    print(f"Created export manifest at {manifest_path}")

if __name__ == "__main__":
    main()
PYTHON_SCRIPT

# Split the file
python "$LOCAL_TEMP_DIR/split_json.py" "$all_mcqs_file" "$CHUNKS_DIR" "$CHUNK_SIZE"

# Step 5: Upload and import the chunks to Heroku
echo "Step 5: Uploading and importing chunks to Heroku..."

# First copy our exports to a place that will be saved in git
EXPORTS_DIR="/Users/tariqalmatrudi/NEWreader/mcq_exports"
mkdir -p "$EXPORTS_DIR"
cp "$CHUNKS_DIR"/*.json "$EXPORTS_DIR/"

# Commit and push the files
echo "Adding export files to git..."
git add "$EXPORTS_DIR"
git commit -m "Add MCQ export files for import"
git push heroku master

# Run the import command on Heroku for each chunk
echo "Running import command on Heroku..."
heroku run "cd django_neurology_mcq && python manage.py import_mcqs_chunked /app/mcq_exports --batch-size 25" --app $APP_NAME

# Step 6: Verify the import
echo "Step 6: Verifying the import..."
heroku run "cd django_neurology_mcq && python manage.py shell -c 'from mcq.models import MCQ; print(f\"Total MCQs in database: {MCQ.objects.count()}\"); for s in MCQ.objects.values(\"subspecialty\").distinct(): print(f\"{s[\"subspecialty\"]}: {MCQ.objects.filter(subspecialty=s[\"subspecialty\"]).count()}\")'" --app $APP_NAME

echo "Import process complete!"