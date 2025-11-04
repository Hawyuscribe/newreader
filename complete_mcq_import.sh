#!/bin/bash
# Script to ensure complete import of all MCQs from the reclassified folder to Heroku database

# Configuration
APP_NAME="radiant-gorge-35079"
SOURCE_DIR="/Users/tariqalmatrudi/Documents/MCQs for the board/Classified MCQs/reclassified"
LOCAL_TEMP_DIR="/Users/tariqalmatrudi/NEWreader/temp_mcqs_chunks"
FORCE_BATCH_SIZE=25  # Smaller batch size for more reliable imports

echo "=== Complete MCQ Import to Heroku Database ==="
echo "This script will ensure ALL MCQs are imported to the Heroku database."
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

# Create a Python script to directly read MCQs and output JSON with verification
cat > "$LOCAL_TEMP_DIR/convert_all_mcqs.py" << 'PYTHON_SCRIPT'
import os
import re
import json
import sys
import glob
from pathlib import Path

def main():
    if len(sys.argv) < 3:
        print("Usage: python convert_all_mcqs.py <source_directory> <output_directory>")
        sys.exit(1)
    
    source_dir = sys.argv[1]
    output_dir = sys.argv[2]
    batch_size = int(sys.argv[3]) if len(sys.argv) > 3 else 50
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Mapping of subspecialty keywords to their standardized names
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
    
    # Get all txt files in the source directory
    txt_files = glob.glob(os.path.join(source_dir, "*.txt"))
    txt_files = [f for f in txt_files if not os.path.basename(f).startswith("debug") and 
                                        not os.path.basename(f).startswith("reclassification")]
    txt_files.sort()  # Sort for deterministic ordering
    
    if not txt_files:
        print(f"No text files found in {source_dir}")
        return
    
    print(f"Processing {len(txt_files)} text files...")
    
    # Process each file and collect all MCQs
    all_mcqs = []
    file_stats = {}
    
    for txt_file in txt_files:
        file_basename = os.path.basename(txt_file)
        subspecialty = os.path.splitext(file_basename)[0].replace('_', ' ')
        
        # Map subspecialty name to standard format
        if subspecialty in subspecialty_map:
            subspecialty = subspecialty_map[subspecialty]
        
        print(f"Processing {file_basename} - subspecialty: {subspecialty}")
        
        # Read the file content
        with open(txt_file, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Define our separator pattern
        separator = '--------------------------------------------------'
        
        # Skip the header (first line or two)
        if "==" in content.split('\n')[0]:
            content = '\n'.join(content.split('\n')[1:])
        
        # Split by the separator
        mcq_blocks = content.split(separator)
        file_mcqs = []
        
        # Process each MCQ block
        for mcq_block in mcq_blocks:
            if not mcq_block.strip():
                continue
            
            mcq_data = parse_mcq_block(mcq_block, subspecialty)
            if mcq_data:
                file_mcqs.append(mcq_data)
                all_mcqs.append(mcq_data)
        
        # Save stats for verification
        file_stats[file_basename] = len(file_mcqs)
        print(f"  Found {len(file_mcqs)} MCQs in {file_basename}")
        
        # Also save individual file's MCQs
        with open(os.path.join(output_dir, f"{os.path.splitext(file_basename)[0]}.json"), 'w') as f:
            json.dump(file_mcqs, f, indent=2)
    
    # Save the complete collection of MCQs
    with open(os.path.join(output_dir, "all_mcqs.json"), 'w') as f:
        json.dump(all_mcqs, f, indent=2)
    
    # Write stats for verification
    with open(os.path.join(output_dir, "mcq_stats.json"), 'w') as f:
        stats = {
            "total_mcqs": len(all_mcqs),
            "total_files": len(txt_files),
            "file_counts": file_stats
        }
        json.dump(stats, f, indent=2)
    
    # Break into smaller batches for more reliable upload
    batches_dir = os.path.join(output_dir, "batches")
    os.makedirs(batches_dir, exist_ok=True)
    
    # Create batches
    num_batches = (len(all_mcqs) + batch_size - 1) // batch_size
    print(f"Creating {num_batches} batches with batch size {batch_size}...")
    
    batch_files = []
    for i in range(num_batches):
        start_idx = i * batch_size
        end_idx = min((i + 1) * batch_size, len(all_mcqs))
        batch = all_mcqs[start_idx:end_idx]
        
        batch_file = f"batch_{i}.json"
        batch_path = os.path.join(batches_dir, batch_file)
        batch_files.append(batch_file)
        
        with open(batch_path, 'w') as f:
            json.dump(batch, f, indent=2)
        
        print(f"  Created batch {i+1}/{num_batches} with {len(batch)} MCQs")
    
    # Write a manifest for batch processing
    with open(os.path.join(batches_dir, "batch_manifest.json"), 'w') as f:
        manifest = {
            "total_mcqs": len(all_mcqs),
            "batch_size": batch_size,
            "total_batches": num_batches,
            "batch_files": batch_files
        }
        json.dump(manifest, f, indent=2)
    
    print(f"""
Processing complete!
Total MCQs processed: {len(all_mcqs)}
Total files processed: {len(txt_files)}
Files saved to: {output_dir}
    """)

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
    
    # Convert options to correct format
    mcq_data["options"] = options
    mcq_data["correct_answer"] = correct_answer or "A"  # Default to A if no correct answer found
    
    return mcq_data

if __name__ == "__main__":
    main()
PYTHON_SCRIPT

# Make it executable
chmod +x "$LOCAL_TEMP_DIR/convert_all_mcqs.py"

# Step 1: Run the new converter to generate JSON files with all MCQs
echo "Step 1: Processing all MCQ files..."
python "$LOCAL_TEMP_DIR/convert_all_mcqs.py" "$SOURCE_DIR" "$LOCAL_TEMP_DIR/full_export" "$FORCE_BATCH_SIZE"

# Get the stats 
echo "MCQ Statistics:"
cat "$LOCAL_TEMP_DIR/full_export/mcq_stats.json"

# Step 2: Move the batches to a Git-tracked directory
EXPORTS_DIR="/Users/tariqalmatrudi/NEWreader/mcq_exports"
mkdir -p "$EXPORTS_DIR"
echo "Step 2: Copying batch files to Git-tracked directory..."
cp -r "$LOCAL_TEMP_DIR/full_export/batches/"* "$EXPORTS_DIR/"

# Step 3: Commit and push the files to Heroku
echo "Step 3: Committing and pushing files to Heroku..."
git add "$EXPORTS_DIR"
git commit -m "Add complete set of MCQ files for import"
git push heroku master

# Step 4: Run the import on Heroku
echo "Step 4: Running import on Heroku..."
heroku run "cd django_neurology_mcq && python manage.py import_mcqs_chunked /app/mcq_exports/batches --batch-size 20" --app $APP_NAME

# Step 5: Verify the import
echo "Step 5: Verifying the import..."
heroku run "cd django_neurology_mcq && python manage.py shell -c 'from mcq.models import MCQ; print(\"Total MCQs in database:\", MCQ.objects.count()); import json; print(json.dumps({s[\"subspecialty\"]: MCQ.objects.filter(subspecialty=s[\"subspecialty\"]).count() for s in MCQ.objects.values(\"subspecialty\").distinct()}, indent=2))'" --app $APP_NAME

echo "Import process complete!"