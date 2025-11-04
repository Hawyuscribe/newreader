#!/usr/bin/env python3
"""
Script to split MCQ JSON files into smaller batches and upload to Heroku.
This script handles large MCQ files that might cause timeouts.
"""
import os
import json
import argparse
import subprocess
import tempfile
import time
from pathlib import Path

# Configuration
HEROKU_APP = "radiant-gorge-35079"
DEFAULT_MCQ_DIR = "/Users/tariqalmatrudi/Documents/MCQs for the board/test/json f"
BATCH_SIZE = 50  # Number of MCQs per batch

# Subspecialty mapping - same as in import_mcqs_to_heroku.py
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


def extract_subspecialty_from_filename(filename):
    """Extract subspecialty from filename."""
    for key in SUBSPECIALTY_MAPPING.keys():
        if key in filename.lower():
            return SUBSPECIALTY_MAPPING[key]
    
    # Default fallback
    return "Other/Unclassified"


def create_fixture_from_mcqs(mcqs, subspecialty):
    """Create a Django fixture from a list of MCQs."""
    fixtures = []
    
    for mcq_data in mcqs:
        # Extract data from the MCQ
        mcq_id = mcq_data.get('ID')
        
        # Skip if ID is missing
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
        options = {}
        for letter in ['A', 'B', 'C', 'D', 'E', 'F']:
            key = f'Option {letter}'
            if key in mcq_data and mcq_data[key]:
                options[letter] = mcq_data[key]
        
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
                "source_file": ""  # Will be set later
            }
        }
        
        # Add image URL if present
        if 'Image URL' in mcq_data and mcq_data['Image URL']:
            fixture_entry["fields"]["image_url"] = mcq_data['Image URL']
        
        fixtures.append(fixture_entry)
    
    return fixtures


def split_and_upload(json_file, batch_size=BATCH_SIZE, clear_existing=False):
    """Split a JSON file into batches and upload them to Heroku."""
    print(f"\nProcessing {os.path.basename(json_file)}")
    
    # Extract subspecialty from filename
    subspecialty = extract_subspecialty_from_filename(os.path.basename(json_file))
    print(f"Determined subspecialty: {subspecialty}")
    
    # Load JSON file
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        return 0
    
    # Verify structure
    if 'mcqs' not in data:
        print(f"Error: No 'mcqs' key found in {json_file}")
        return 0
    
    # Get MCQs
    mcqs = data['mcqs']
    total_mcqs = len(mcqs)
    print(f"Found {total_mcqs} MCQs in {os.path.basename(json_file)}")
    
    # Clear existing MCQs for this subspecialty if requested
    if clear_existing:
        print(f"Clearing existing MCQs for subspecialty: {subspecialty}")
        clear_command = f"cd /app/django_neurology_mcq && python manage.py shell -c 'from mcq.models import MCQ; count = MCQ.objects.filter(subspecialty=\"{subspecialty}\").count(); print(f\"Deleting {count} MCQs for {subspecialty}...\"); MCQ.objects.filter(subspecialty=\"{subspecialty}\").delete(); print(\"Done\")'"
        output = run_heroku_command(clear_command)
        print(output)
    
    # Split into batches
    num_batches = (total_mcqs + batch_size - 1) // batch_size
    print(f"Splitting into {num_batches} batches of up to {batch_size} MCQs")
    
    # Process each batch
    total_imported = 0
    
    for i in range(num_batches):
        batch_start = i * batch_size
        batch_end = min((i + 1) * batch_size, total_mcqs)
        
        print(f"\nProcessing batch {i+1}/{num_batches} (MCQs {batch_start+1}-{batch_end})...")
        
        # Extract MCQs for this batch
        batch_mcqs = mcqs[batch_start:batch_end]
        
        # Set source file
        source_file = os.path.basename(json_file)
        
        # Convert to fixture
        fixtures = create_fixture_from_mcqs(batch_mcqs, subspecialty)
        
        # Set source file for all fixtures
        for fixture in fixtures:
            fixture["fields"]["source_file"] = source_file
        
        # Create temporary fixture file
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as f:
            json.dump(fixtures, f, indent=2, ensure_ascii=False)
            fixture_file = f.name
        
        # Upload to Heroku
        remote_path = f'/tmp/batch_{i+1}_of_{num_batches}.json'
        try:
            # Upload file using curl or similar
            print(f"Uploading batch {i+1} to Heroku...")
            upload_command = f"curl -s -X POST --data-binary @{fixture_file} https://{HEROKU_APP}.herokuapp.com/upload_fixture/ -H 'Content-Type: application/json'"
            
            # Alternative: use cat and pipe to heroku run
            upload_command = f"cat {fixture_file} | heroku run --app {HEROKU_APP} 'cat > {remote_path}'"
            subprocess.run(upload_command, shell=True)
            
            # Run loaddata command
            import_command = f"cd /app/django_neurology_mcq && python manage.py loaddata {remote_path}"
            output = run_heroku_command(import_command)
            print(output)
            
            # Extract result
            import_count = len(fixtures)
            
            # Check if import was successful
            if "Installed" in output:
                total_imported += import_count
                print(f"✅ Successfully imported {import_count} MCQs in batch {i+1}")
            else:
                print(f"❌ Failed to import batch {i+1}")
        except Exception as e:
            print(f"Error uploading/importing batch {i+1}: {e}")
        finally:
            # Clean up temporary file
            os.unlink(fixture_file)
    
    print(f"\nFinished processing {os.path.basename(json_file)}")
    print(f"Total MCQs imported: {total_imported} out of {total_mcqs}")
    
    return total_imported


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
    parser = argparse.ArgumentParser(description='Split and upload MCQs to Heroku')
    parser.add_argument('--mcq-dir', default=DEFAULT_MCQ_DIR, help='Directory containing MCQ JSON files')
    parser.add_argument('--batch-size', type=int, default=BATCH_SIZE, help='Number of MCQs per batch')
    parser.add_argument('--clear-all', action='store_true', help='Clear all existing MCQs before import')
    parser.add_argument('--clear-subspecialty', action='store_true', help='Clear MCQs for each subspecialty before import')
    parser.add_argument('--file', help='Process a specific file only')
    parser.add_argument('--subspecialty', help='Only process files for this subspecialty')
    
    args = parser.parse_args()
    
    print("====== HEROKU MCQ IMPORT (BATCH MODE) ======")
    print(f"Started at: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Target Heroku app: {HEROKU_APP}")
    print(f"MCQ directory: {args.mcq_dir}")
    print(f"Batch size: {args.batch_size}")
    
    # Clear all existing MCQs if requested
    if args.clear_all:
        print("Clearing all existing MCQs...")
        clear_command = "cd /app/django_neurology_mcq && python manage.py shell -c 'from mcq.models import MCQ, Bookmark, Flashcard, Note, ReasoningSession; "\
                        "bookmark_count = Bookmark.objects.count(); print(f\"Deleting {bookmark_count} bookmarks...\"); Bookmark.objects.all().delete(); "\
                        "flashcard_count = Flashcard.objects.count(); print(f\"Deleting {flashcard_count} flashcards...\"); Flashcard.objects.all().delete(); "\
                        "note_count = Note.objects.count(); print(f\"Deleting {note_count} notes...\"); Note.objects.all().delete(); "\
                        "reasoning_count = ReasoningSession.objects.count(); print(f\"Deleting {reasoning_count} reasoning sessions...\"); ReasoningSession.objects.all().delete(); "\
                        "count = MCQ.objects.count(); print(f\"Deleting {count} MCQs...\"); MCQ.objects.all().delete(); print(\"Done\")'"
        
        output = run_heroku_command(clear_command)
        print(output)
    
    # Get JSON files
    if args.file:
        json_files = [Path(args.file)]
    else:
        json_dir = Path(args.mcq_dir)
        # Find all JSON files in the directory
        json_files = list(json_dir.glob("*.json"))
        # Exclude backup files
        json_files = [f for f in json_files if "bak_" not in f.name]
        
        # Filter by subspecialty if specified
        if args.subspecialty:
            json_files = [f for f in json_files if args.subspecialty.lower() in f.name.lower()]
    
    print(f"Found {len(json_files)} JSON files to process")
    
    # Process each file
    total_imported = 0
    
    for i, json_file in enumerate(json_files):
        print(f"\n[{i+1}/{len(json_files)}] Processing {json_file.name}")
        imported = split_and_upload(
            str(json_file), 
            batch_size=args.batch_size,
            clear_existing=args.clear_subspecialty
        )
        total_imported += imported
    
    # Verify the import
    verify_import()
    
    print("\n====== IMPORT COMPLETED ======")
    print(f"Total MCQs imported: {total_imported}")
    print(f"Completed at: {time.strftime('%Y-%m-%d %H:%M:%S')}")


if __name__ == "__main__":
    main()