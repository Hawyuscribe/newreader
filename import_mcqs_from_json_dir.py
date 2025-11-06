#!/usr/bin/env python3
"""
Import MCQs from JSON files in a directory to Heroku.
This script reads JSON files from the specified directory and imports them to Heroku.
"""
import os
import json
import subprocess
import tempfile
import glob
from pathlib import Path
import time
import re
import sys

# Constants
APP_NAME = "radiant-gorge-35079"
SOURCE_DIR = "/Users/tariqalmatrudi/Documents/MCQs for the board/test/json f"
CHUNK_SIZE = 50  # Smaller chunks to avoid timeouts

def clean_option_text(text):
    """Clean option text by trimming whitespace and removing trailing punctuation."""
    if not text:
        return ""
    if isinstance(text, float) or (isinstance(text, str) and text.lower() in ('nan', 'none', 'null', '')):
        return ""
    # Strip whitespace
    cleaned = str(text).strip()
    # Remove trailing punctuation (period, comma, semicolon)
    if cleaned and cleaned[-1] in ".,:;":
        cleaned = cleaned[:-1].strip()
    return cleaned

def normalize_subspecialty(subspecialty):
    """Normalize subspecialty names for consistency."""
    if not subspecialty:
        return "Other"
    
    mapping = {
        "vascular": "Vascular Neurology",
        "vascular neurology": "Vascular Neurology",
        "vascular neurology/stroke": "Vascular Neurology",
        "stroke": "Vascular Neurology",
        "epilepsy": "Epilepsy",
        "movement": "Movement Disorders",
        "movement disorder": "Movement Disorders",
        "movement disorders": "Movement Disorders",
        "neuroimmunology": "Neuroimmunology",
        "dementia": "Dementia",
        "neuromuscular": "Neuromuscular",
        "neuro-oncology": "Neurooncology",
        "neurooncology": "Neurooncology",
        "oncology": "Neurooncology",
        "neuro-otology": "Neuro-otology",
        "otology": "Neuro-otology",
        "neuro infectious": "Neuroinfectious",
        "neuroinfectious": "Neuroinfectious",
        "infectious": "Neuroinfectious",
        "neuropsychiatry": "Neuropsychiatry",
        "psychiatry": "Neuropsychiatry",
        "pediatric": "Pediatric Neurology",
        "pediatric neurology": "Pediatric Neurology",
        "child": "Pediatric Neurology",
        "sleep": "Sleep Neurology",
        "sleep neurology": "Sleep Neurology",
        "headache": "Headache",
        "critical care": "Critical Care Neurology",
        "critical care neurology": "Critical Care Neurology",
        "neuroanatomy": "Anatomy",
        "anatomy": "Anatomy",
        "neurogenetics": "Neurogenetics",
        "genetics": "Neurogenetics",
        "neuroophthalmology": "Neuroophthalmology",
        "ophthalmology": "Neuroophthalmology",
    }
    
    # Find the closest match
    normalized = subspecialty.strip().lower()
    for key, value in mapping.items():
        if key in normalized:
            return value
    
    # Default if no match found
    return subspecialty

def extract_subspecialty_from_filename(filename):
    """Extract subspecialty from the filename."""
    basename = os.path.basename(filename)
    # Extract subspecialty prefix from filename (before _mcqs_)
    match = re.match(r'(.+?)_mcqs_', basename)
    if match:
        subspecialty_raw = match.group(1)
        # Replace underscores with spaces and normalize
        subspecialty = subspecialty_raw.replace('_', ' ')
        return normalize_subspecialty(subspecialty)
    return "Other"

def clean_mcq(mcq_data, subspecialty_override=None):
    """Clean and normalize MCQ data to match Django model format."""
    options = {}
    for letter in ['A', 'B', 'C', 'D', 'E', 'F']:
        key = f"Option {letter}"
        if key in mcq_data and mcq_data[key]:
            options[letter] = clean_option_text(mcq_data[key])
    
    # Use provided subspecialty or extract from data
    subspecialty = subspecialty_override
    if not subspecialty and "Subspecialty" in mcq_data and mcq_data["Subspecialty"]:
        subspecialty = normalize_subspecialty(mcq_data["Subspecialty"])
    
    # Handle correct answer
    correct_answer = None
    if "Correct Answer" in mcq_data and mcq_data["Correct Answer"]:
        correct_answer = mcq_data["Correct Answer"].strip().upper()
        # Ensure correct answer is a single letter
        if correct_answer and len(correct_answer) > 0:
            correct_answer = correct_answer[0]
    
    # Set defaults for missing fields
    question_text = mcq_data.get("Question Text", "").strip()
    if not question_text and "Question" in mcq_data:
        question_text = mcq_data["Question"].strip()
    
    # Build Django compatible MCQ object
    cleaned_mcq = {
        "model": "mcq.mcq",
        "fields": {
            "question_text": question_text,
            "options": options,
            "correct_answer": correct_answer,
            "subspecialty": subspecialty,
            "explanation": mcq_data.get("Option Analysis", ""),
            "exam_type": mcq_data.get("Exam Type", "Unknown"),
            "exam_year": mcq_data.get("Exam Year", "Unknown"),
            "question_number": mcq_data.get("Question Number", ""),
            "has_image": mcq_data.get("Has Image", "No").lower() == "yes",
            "image_url": mcq_data.get("Image URL", ""),
            "original_id": mcq_data.get("ID", ""),
        }
    }
    
    # Add additional explanation fields if available
    explanation_fields = [
        "Conceptual Foundation", "Pathophysiology", "Clinical Correlation",
        "Diagnostic Approach", "Management Principles", "Classification and Neurology",
        "Clinical Pearls", "Current Evidence", "Classification & Nosology"
    ]
    
    explanation_sections = {}
    for field in explanation_fields:
        if field in mcq_data and mcq_data[field]:
            # Convert field name to slug format for database
            section_key = field.lower().replace(" ", "_").replace("&", "and")
            explanation_sections[section_key] = mcq_data[field]
    
    if explanation_sections:
        cleaned_mcq["fields"]["explanation_sections"] = explanation_sections
    
    return cleaned_mcq

def process_json_file(json_path):
    """Process a single JSON file containing MCQs."""
    try:
        with open(json_path, 'r') as f:
            data = json.load(f)
        
        # Extract subspecialty from filename
        subspecialty = extract_subspecialty_from_filename(json_path)
        print(f"Processing {json_path} - Subspecialty: {subspecialty}")
        
        mcqs = []
        if "mcqs" in data and isinstance(data["mcqs"], list):
            # Format as Django fixtures
            for mcq_data in data["mcqs"]:
                cleaned_mcq = clean_mcq(mcq_data, subspecialty)
                mcqs.append(cleaned_mcq)
        
        print(f"Extracted {len(mcqs)} MCQs from {json_path}")
        return mcqs
    except Exception as e:
        print(f"Error processing {json_path}: {str(e)}")
        return []

def upload_chunks_to_heroku(mcqs, subspecialty):
    """Upload MCQs in chunks to avoid timeouts."""
    if not mcqs:
        print(f"No MCQs to upload for {subspecialty}")
        return
    
    # Split into chunks
    chunks = [mcqs[i:i + CHUNK_SIZE] for i in range(0, len(mcqs), CHUNK_SIZE)]
    print(f"Uploading {len(mcqs)} MCQs for {subspecialty} in {len(chunks)} chunks")
    
    for i, chunk in enumerate(chunks):
        print(f"Processing chunk {i+1}/{len(chunks)} for {subspecialty}")
        
        # Prepare JSON fixture
        fixture_data = json.dumps(chunk, indent=2)
        
        # Create temp file for fixture
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as f:
            f.write(fixture_data)
            temp_path = f.name
        
        # Create loaddata script for this chunk
        loaddata_script = f"""
import json
import tempfile
from django.core import serializers
from mcq.models import MCQ
from django.db import transaction

# Count MCQs before import
before_count = MCQ.objects.filter(subspecialty="{subspecialty}").count()
print(f"Before import: {{before_count}} MCQs for {subspecialty}")

# Load from file
with open('/tmp/import_data.json', 'r') as f:
    fixture_data = f.read()

# Parse JSON
mcq_objects = json.loads(fixture_data)
print(f"Loaded {{len(mcq_objects)}} MCQs from fixture")

# Import
success_count = 0
error_count = 0
with transaction.atomic():
    for mcq_data in mcq_objects:
        try:
            # Get fields
            fields = mcq_data['fields']
            
            # Check if MCQ with same question exists
            existing = MCQ.objects.filter(
                question_text=fields['question_text'],
                subspecialty=fields['subspecialty']
            ).first()
            
            if existing:
                # Update existing
                for key, value in fields.items():
                    setattr(existing, key, value)
                existing.save()
            else:
                # Create new MCQ
                mcq = MCQ(**fields)
                mcq.save()
            
            success_count += 1
        except Exception as e:
            print(f"Error importing MCQ: {{str(e)}}")
            error_count += 1

# Count MCQs after import
after_count = MCQ.objects.filter(subspecialty="{subspecialty}").count()
print(f"After import: {{after_count}} MCQs for {subspecialty}")
print(f"Imported: {{success_count}} successful, {{error_count}} failed")
"""
        
        # Create temp script file
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.py') as f:
            f.write(loaddata_script)
            script_path = f.name
        
        # Upload to Heroku and import
        try:
            print(f"Uploading chunk {i+1} for {subspecialty}...")
            
            # Upload fixture file
            upload_cmd = f"cat {temp_path} | heroku run --app {APP_NAME} \"cat > /tmp/import_data.json\""
            subprocess.run(upload_cmd, shell=True)
            
            # Upload script
            upload_script_cmd = f"cat {script_path} | heroku run --app {APP_NAME} \"cat > /tmp/import_script.py\""
            subprocess.run(upload_script_cmd, shell=True)
            
            # Run script
            run_cmd = f"heroku run --app {APP_NAME} \"cd /app/django_neurology_mcq && python manage.py shell -c 'exec(open(\\\"/tmp/import_script.py\\\").read())'\""
            subprocess.run(run_cmd, shell=True)
            
            print(f"Successfully imported chunk {i+1} for {subspecialty}")
            
            # Add delay between chunks to avoid rate limiting
            if i < len(chunks) - 1:
                print("Waiting 3 seconds before next chunk...")
                time.sleep(3)
                
        except Exception as e:
            print(f"Error importing chunk {i+1} for {subspecialty}: {str(e)}")
        finally:
            # Clean up
            os.unlink(temp_path)
            os.unlink(script_path)

def main():
    """Main function to process all JSON files and upload to Heroku."""
    print(f"Starting import from {SOURCE_DIR} to Heroku app {APP_NAME}")
    
    # Get all JSON files in the directory
    json_files = glob.glob(os.path.join(SOURCE_DIR, "*.json"))
    # Filter out backup files
    json_files = [f for f in json_files if not (".bak_" in f or ".options_bak_" in f)]
    
    print(f"Found {len(json_files)} JSON files to process")
    
    # Get specific file or subspecialty if provided in args
    target_file = None
    target_subspecialty = None
    if len(sys.argv) > 1:
        if sys.argv[1] == "--clear":
            # Skip the clear since it's timing out
            print("Skipping clear operation due to potential timeout issues")
        elif sys.argv[1] == "--file" and len(sys.argv) > 2:
            target_file = sys.argv[2]
            print(f"Processing only file: {target_file}")
            json_files = [f for f in json_files if target_file in f]
        elif sys.argv[1] == "--subspecialty" and len(sys.argv) > 2:
            target_subspecialty = sys.argv[2]
            print(f"Processing only subspecialty: {target_subspecialty}")
    
    # Process all files by subspecialty
    subspecialty_mcqs = {}
    
    for json_file in json_files:
        mcqs = process_json_file(json_file)
        
        # Group by subspecialty
        for mcq in mcqs:
            subspecialty = mcq["fields"]["subspecialty"]
            if target_subspecialty and not target_subspecialty.lower() in subspecialty.lower():
                continue
            if subspecialty not in subspecialty_mcqs:
                subspecialty_mcqs[subspecialty] = []
            subspecialty_mcqs[subspecialty].append(mcq)
    
    # Upload by subspecialty
    for subspecialty, mcqs in subspecialty_mcqs.items():
        print(f"\nProcessing {len(mcqs)} MCQs for {subspecialty}...")
        upload_chunks_to_heroku(mcqs, subspecialty)
    
    # Verify import
    print("\nVerifying import...")
    verify_cmd = 'heroku run --app ' + APP_NAME + ' "cd /app/django_neurology_mcq && python manage.py shell -c \'from mcq.models import MCQ; from django.db.models import Count; total=MCQ.objects.count(); print(f\"Total MCQs: {total}\"); subspecialties=MCQ.objects.values(\"subspecialty\").annotate(count=Count(\"id\")); print(\"MCQs by subspecialty:\"); [print(f\"  {s[\\\"subspecialty\\\"]}: {s[\\\"count\\\"]}\") for s in subspecialties]\'"'
    subprocess.run(verify_cmd, shell=True)
    
    print("Import completed!")

if __name__ == "__main__":
    main()