#!/usr/bin/env python3
"""
Script to convert JSON MCQs to Django fixtures and upload to Heroku.
This script handles:
1. Converting source JSON to Django fixtures format
2. Uploading fixtures to Heroku
3. Running loaddata to import fixtures into the database
"""
import os
import json
import subprocess
import tempfile
import time
import re
from pathlib import Path
import argparse
import sys

# Configuration
HEROKU_APP = "radiant-gorge-35079"
DEFAULT_MCQ_DIR = "/Users/tariqalmatrudi/Documents/MCQs for the board/test/json f"
FIXTURES_DIR = "/tmp/mcq_fixtures"

# Subspecialty mapping
SUBSPECIALTY_MAPPING = {
    'critical_care_neurology': 'Critical Care Neurology',
    'dementia': 'Dementia',
    'epilepsy': 'Epilepsy',
    'headache': 'Headache',
    'movement_disorders': 'Movement Disorders',
    'neuro-otology': 'Neuro-otology',
    'neuroanatomy': 'Neuroanatomy',
    'neurogenetics': 'Neurogenetics',
    'neuroimmunology': 'Neuroimmunology',
    'neuroinfectious': 'Neuro-infectious',
    'neuro_infectious': 'Neuro-infectious',
    'neuromuscular': 'Neuromuscular',
    'neurooncology': 'Neuro-oncology',
    'neuro-oncology': 'Neuro-oncology',
    'neuroophthalmology': 'Neuroophthalmology',
    'neuropsychiatry': 'Neuropsychiatry',
    'neurotoxicology': 'Neurotoxicology',
    'other': 'Other/Unclassified',
    'other_unclassified': 'Other/Unclassified',
    'pediatric_neurology': 'Pediatric Neurology',
    'sleep_neurology': 'Sleep Neurology',
    'vascular_neurology': 'Vascular Neurology/Stroke',
    'vascular': 'Vascular Neurology/Stroke',
}


def run_heroku_command(command, capture_output=True):
    """Run a command on Heroku and return its output."""
    print(f"Running on Heroku: {command[:80]}...")
    full_command = f"heroku run --app {HEROKU_APP} '{command}'"
    
    if capture_output:
        result = subprocess.run(full_command, shell=True, capture_output=True, text=True)
        return result.stdout
    else:
        subprocess.run(full_command, shell=True)
        return None


def upload_file_to_heroku(local_path, remote_path):
    """Upload a file to Heroku."""
    print(f"Uploading {os.path.basename(local_path)} to Heroku...")
    upload_command = f"cat '{local_path}' | heroku run --app {HEROKU_APP} 'cat > {remote_path}'"
    subprocess.run(upload_command, shell=True)


def extract_subspecialty_from_filename(filename):
    """Extract subspecialty from filename."""
    for key in SUBSPECIALTY_MAPPING.keys():
        if key in filename.lower():
            return SUBSPECIALTY_MAPPING[key]
    
    # Default fallback
    return "Other/Unclassified"


def convert_options_to_dict(mcq_data):
    """Convert options from the JSON format to a dictionary."""
    options = {}
    
    # Check for Option A, Option B, etc. fields
    for letter in ['A', 'B', 'C', 'D', 'E', 'F']:
        key = f'Option {letter}'
        if key in mcq_data and mcq_data[key]:
            options[letter] = mcq_data[key]
    
    return options


def convert_to_fixture(json_file, output_file):
    """Convert a JSON file to Django fixtures format."""
    print(f"Converting {os.path.basename(json_file)} to fixture format...")
    
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError:
        print(f"Error: Could not parse JSON file {json_file}")
        return 0
    
    # Handle the JSON structure - it should have a "mcqs" key
    if 'mcqs' not in data:
        print(f"Error: No 'mcqs' key found in {json_file}")
        return 0
    
    # Get subspecialty from filename
    subspecialty = extract_subspecialty_from_filename(os.path.basename(json_file))
    
    # Convert to Django fixtures format
    fixtures = []
    
    for mcq_data in data['mcqs']:
        try:
            # Extract data from the MCQ
            mcq_id = mcq_data.get('ID')
            
            # If ID is missing, skip this MCQ
            if not mcq_id:
                continue
            
            question_number = mcq_data.get('Question Number')
            question_text = mcq_data.get('Question Text', '')
            exam_type = mcq_data.get('Exam Type', 'Other')
            
            # Parse exam year
            exam_year = None
            if 'Exam Year' in mcq_data and mcq_data['Exam Year']:
                try:
                    exam_year = int(mcq_data['Exam Year'])
                except (ValueError, TypeError):
                    pass
            
            # Convert options to the expected format
            options = convert_options_to_dict(mcq_data)
            
            # Get correct answer
            correct_answer = mcq_data.get('Correct Answer', '')
            
            # Extract explanation sections
            explanation_sections = {}
            explanation_fields = [
                'Conceptual Foundation', 'Pathophysiology', 'Clinical Correlation',
                'Diagnostic Approach', 'Classification and Neurology', 'Classification & Nosology',
                'Management Principles', 'Option Analysis', 'Clinical Pearls',
                'Current Evidence'
            ]
            
            for field in explanation_fields:
                if field in mcq_data and mcq_data[field]:
                    key = field.lower().replace(' ', '_').replace('&', 'and')
                    explanation_sections[key] = mcq_data[field]
            
            # Create fixture entry
            fixture_entry = {
                "model": "mcq.mcq",
                "pk": mcq_id,
                "fields": {
                    "question_number": question_number,
                    "question_text": question_text,
                    "options": options,
                    "correct_answer": correct_answer,
                    "subspecialty": subspecialty,
                    "exam_type": exam_type,
                    "exam_year": exam_year,
                    "explanation_sections": explanation_sections,
                    "source_file": os.path.basename(json_file)
                }
            }
            
            # Add image URL if present
            if 'Image URL' in mcq_data and mcq_data['Image URL']:
                fixture_entry["fields"]["image_url"] = mcq_data['Image URL']
            
            fixtures.append(fixture_entry)
            
        except Exception as e:
            print(f"Error processing MCQ {mcq_data.get('ID', 'unknown')}: {str(e)}")
    
    # Write fixtures to file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(fixtures, f, indent=2, ensure_ascii=False)
    
    print(f"Converted {len(fixtures)} MCQs to fixture format")
    return len(fixtures)


def clear_existing_mcqs():
    """Clear all existing MCQs from the Heroku database."""
    print("Clearing existing MCQs...")
    clear_command = "cd /app/django_neurology_mcq && python manage.py shell -c 'from mcq.models import MCQ, Bookmark, Flashcard, Note, ReasoningSession; "\
                    "bookmark_count = Bookmark.objects.count(); print(f\"Deleting {bookmark_count} bookmarks...\"); Bookmark.objects.all().delete(); "\
                    "flashcard_count = Flashcard.objects.count(); print(f\"Deleting {flashcard_count} flashcards...\"); Flashcard.objects.all().delete(); "\
                    "note_count = Note.objects.count(); print(f\"Deleting {note_count} notes...\"); Note.objects.all().delete(); "\
                    "reasoning_count = ReasoningSession.objects.count(); print(f\"Deleting {reasoning_count} reasoning sessions...\"); ReasoningSession.objects.all().delete(); "\
                    "count = MCQ.objects.count(); print(f\"Deleting {count} MCQs...\"); MCQ.objects.all().delete(); print(\"Done\")'"
    
    output = run_heroku_command(clear_command)
    print(output)


def upload_and_import_fixture(fixture_file):
    """Upload a fixture file to Heroku and import it."""
    print(f"\nUploading and importing {os.path.basename(fixture_file)}...")
    
    # Upload the fixture to Heroku
    remote_path = f'/tmp/{os.path.basename(fixture_file)}'
    upload_file_to_heroku(fixture_file, remote_path)
    
    # Run loaddata command
    import_command = f"cd /app/django_neurology_mcq && python manage.py loaddata {remote_path}"
    output = run_heroku_command(import_command)
    print(output)
    
    # Extract import count if possible
    match = re.search(r'Installed (\d+) object', output)
    if match:
        return int(match.group(1))
    else:
        return 0


def verify_import():
    """Verify the import by checking MCQ counts."""
    print("\nVerifying import...")
    verify_command = "cd /app/django_neurology_mcq && python manage.py shell -c 'from mcq.models import MCQ; from django.db.models import Count; "\
                    "total=MCQ.objects.count(); print(f\"Total MCQs: {total}\"); print(\"\\nMCQs by Subspecialty:\"); "\
                    "for item in MCQ.objects.values(\"subspecialty\").annotate(count=Count(\"id\")).order_by(\"-count\"): "\
                    "print(f\"  {item[\"subspecialty\"]}: {item[\"count\"]}\")'"
    
    output = run_heroku_command(verify_command)
    print(output)


def main():
    """Main function to run the import process."""
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Import MCQs to Heroku from JSON files')
    parser.add_argument('--mcq-dir', default=DEFAULT_MCQ_DIR, help='Directory containing MCQ JSON files')
    parser.add_argument('--fixtures-dir', default=FIXTURES_DIR, help='Directory for generated fixtures')
    parser.add_argument('--no-clear', action='store_true', help='Do not clear existing MCQs')
    parser.add_argument('--file', help='Import a specific file only')
    
    args = parser.parse_args()
    
    print("====== HEROKU MCQ IMPORT ======")
    print(f"Started at: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Target Heroku app: {HEROKU_APP}")
    print(f"MCQ directory: {args.mcq_dir}")
    print(f"Fixtures directory: {args.fixtures_dir}")
    
    # Create fixtures directory if it doesn't exist
    os.makedirs(args.fixtures_dir, exist_ok=True)
    
    # Clear existing MCQs if requested
    if not args.no_clear:
        clear_existing_mcqs()
    
    # Get JSON files
    if args.file:
        json_files = [Path(args.file)]
    else:
        json_dir = Path(args.mcq_dir)
        # Find all JSON files in the directory
        json_files = list(json_dir.glob("*.json"))
        # Exclude backup files
        json_files = [f for f in json_files if "bak_" not in f.name]
    
    print(f"Found {len(json_files)} JSON files to process")
    
    # Process each file
    total_converted = 0
    total_imported = 0
    
    for i, json_file in enumerate(json_files):
        print(f"\n[{i+1}/{len(json_files)}] Processing {json_file.name}")
        
        # Convert to fixture format
        fixture_file = os.path.join(args.fixtures_dir, f"{json_file.stem}_fixture.json")
        converted_count = convert_to_fixture(str(json_file), fixture_file)
        total_converted += converted_count
        
        if converted_count > 0:
            # Upload and import the fixture
            imported_count = upload_and_import_fixture(fixture_file)
            total_imported += imported_count
            
            print(f"✅ Successfully imported {imported_count} MCQs from {json_file.name}")
        else:
            print(f"❌ No MCQs converted from {json_file.name}")
    
    # Verify the import
    verify_import()
    
    print("\n====== IMPORT COMPLETED ======")
    print(f"Total MCQs converted: {total_converted}")
    print(f"Total MCQs imported: {total_imported}")
    print(f"Completed at: {time.strftime('%Y-%m-%d %H:%M:%S')}")


if __name__ == "__main__":
    main()