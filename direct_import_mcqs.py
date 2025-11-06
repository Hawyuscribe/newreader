#!/usr/bin/env python3
"""
Direct MCQ import script that handles one specialty at a time 
and uses direct imports on Heroku rather than fixtures.
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

# Subspecialty mapping (lowercase key to proper name)
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

def clear_all_mcqs():
    """Clear all existing MCQs from the database."""
    print("Clearing all existing MCQs...")
    clear_command = "cd /app/django_neurology_mcq && python manage.py shell -c 'from mcq.models import MCQ, Bookmark, Flashcard, Note, ReasoningSession; "\
                    "bookmark_count = Bookmark.objects.count(); print(f\"Deleting {bookmark_count} bookmarks...\"); Bookmark.objects.all().delete(); "\
                    "flashcard_count = Flashcard.objects.count(); print(f\"Deleting {flashcard_count} flashcards...\"); Flashcard.objects.all().delete(); "\
                    "note_count = Note.objects.count(); print(f\"Deleting {note_count} notes...\"); Note.objects.all().delete(); "\
                    "reasoning_count = ReasoningSession.objects.count(); print(f\"Deleting {reasoning_count} reasoning sessions...\"); ReasoningSession.objects.all().delete(); "\
                    "count = MCQ.objects.count(); print(f\"Deleting {count} MCQs...\"); MCQ.objects.all().delete(); print(\"Done\")'"
    
    output = run_heroku_command(clear_command)
    print(output)

def clear_subspecialty_mcqs(subspecialty):
    """Clear MCQs for a specific subspecialty."""
    print(f"Clearing existing MCQs for subspecialty: {subspecialty}")
    clear_command = f"cd /app/django_neurology_mcq && python manage.py shell -c 'from mcq.models import MCQ; "\
                   f"count = MCQ.objects.filter(subspecialty=\"{subspecialty}\").count(); "\
                   f"print(f\"Deleting {{count}} MCQs for {subspecialty}...\"); "\
                   f"MCQ.objects.filter(subspecialty=\"{subspecialty}\").delete(); "\
                   f"print(\"Done\")'"
    
    output = run_heroku_command(clear_command)
    print(output)

def create_import_script():
    """Create the direct import script to run on Heroku."""
    script = """
import json
import sys
import os

# Set DJANGO environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "neurology_mcq.settings")

# Initialize Django
import django
django.setup()

from django.db import transaction
from mcq.models import MCQ

def import_mcqs_from_json(json_path, subspecialty=None):
    print(f"Reading {json_path}")
    
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error reading JSON file: {str(e)}")
        return 0
    
    # Handle the JSON structure - it should have a "mcqs" key
    if 'mcqs' not in data:
        print("Error: No 'mcqs' key found in the JSON file")
        return 0
    
    mcqs = data['mcqs']
    print(f"Found {len(mcqs)} MCQs to import")
    
    # Process MCQs
    imported = 0
    
    with transaction.atomic():
        for mcq_data in mcqs:
            try:
                # Extract data from the MCQ
                mcq_id = mcq_data.get('ID')
                question_number = mcq_data.get('Question Number')
                question_text = mcq_data.get('Question Text', '')
                
                # Skip if critical data is missing
                if not question_text or not mcq_id:
                    continue
                
                # Get exam type and year
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
                
                # Use provided subspecialty or get from MCQ data
                if subspecialty:
                    mcq_subspecialty = subspecialty
                else:
                    mcq_subspecialty = mcq_data.get('Subspecialty', 'Other/Unclassified')
                
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
                
                # Create or update the MCQ object
                mcq, created = MCQ.objects.update_or_create(
                    id=mcq_id,
                    defaults={
                        'question_number': question_number,
                        'question_text': question_text,
                        'options': options,
                        'correct_answer': correct_answer,
                        'subspecialty': mcq_subspecialty,
                        'exam_type': exam_type,
                        'exam_year': exam_year,
                        'explanation_sections': explanation_sections,
                        'source_file': os.path.basename(json_path)
                    }
                )
                
                # Add image URL if present
                if 'Image URL' in mcq_data and mcq_data['Image URL']:
                    mcq.image_url = mcq_data['Image URL']
                    mcq.save()
                
                imported += 1
                
                # Print progress
                if imported % 20 == 0:
                    print(f"Imported {imported} MCQs...")
            
            except Exception as e:
                print(f"Error importing MCQ {mcq_data.get('ID', 'unknown')}: {str(e)}")
    
    print(f"Import complete: {imported} MCQs imported")
    return imported

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python import_script.py <json_file> [subspecialty]")
        sys.exit(1)
    
    json_file = sys.argv[1]
    subspecialty = None
    if len(sys.argv) > 2:
        subspecialty = sys.argv[2]
    
    count = import_mcqs_from_json(json_file, subspecialty)
    print(f"Successfully imported {count} MCQs")
"""
    
    # Create temp file with the script
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.py') as f:
        f.write(script)
        script_path = f.name
    
    return script_path

def upload_file_to_heroku(local_path, remote_path):
    """Upload a file to Heroku."""
    print(f"Uploading {os.path.basename(local_path)} to Heroku...")
    upload_command = f"cat '{local_path}' | heroku run --app {HEROKU_APP} 'cat > {remote_path}'"
    subprocess.run(upload_command, shell=True)

def get_file_subspecialty(filename):
    """Extract subspecialty from the filename."""
    for key in SUBSPECIALTY_MAPPING.keys():
        if key in filename.lower():
            return SUBSPECIALTY_MAPPING[key]
    return "Other/Unclassified"

def import_subspecialty(json_file, clear_specialty=False):
    """Import MCQs for a specific subspecialty."""
    # Extract subspecialty from filename
    subspecialty = get_file_subspecialty(os.path.basename(json_file))
    print(f"\nImporting {os.path.basename(json_file)} for subspecialty: {subspecialty}")
    
    # Clear existing MCQs for this subspecialty if requested
    if clear_specialty:
        clear_subspecialty_mcqs(subspecialty)
    
    # Create and upload the import script
    script_path = create_import_script()
    remote_script_path = "/tmp/import_script.py"
    upload_file_to_heroku(script_path, remote_script_path)
    
    # Upload the JSON file
    remote_json_path = f"/tmp/{os.path.basename(json_file)}"
    upload_file_to_heroku(json_file, remote_json_path)
    
    # Run the import script
    run_command = f"cd /app/django_neurology_mcq && python {remote_script_path} {remote_json_path} '{subspecialty}'"
    output = run_heroku_command(run_command)
    print(output)
    
    # Clean up temporary script file
    os.unlink(script_path)
    
    # Parse output to find number of imported MCQs
    import_count = 0
    for line in output.split('\n'):
        if "Successfully imported" in line:
            try:
                import_count = int(line.split()[2])
            except (IndexError, ValueError):
                pass
    
    return import_count

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
    parser = argparse.ArgumentParser(description='Import MCQs to Heroku')
    parser.add_argument('--mcq-dir', default="/Users/tariqalmatrudi/Documents/MCQs for the board/test/json f", 
                        help='Directory containing MCQ JSON files')
    parser.add_argument('--clear-all', action='store_true', help='Clear all existing MCQs before import')
    parser.add_argument('--clear-subspecialty', action='store_true', help='Clear MCQs for each subspecialty before import')
    parser.add_argument('--file', help='Process a specific file only')
    parser.add_argument('--subspecialty', help='Only process files for this subspecialty')
    
    args = parser.parse_args()
    
    print("====== HEROKU MCQ DIRECT IMPORT ======")
    print(f"Started at: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Target Heroku app: {HEROKU_APP}")
    
    # Clear all existing MCQs if requested
    if args.clear_all:
        clear_all_mcqs()
    
    # Get JSON files
    if args.file:
        json_files = [Path(args.file)]
    else:
        json_dir = Path(args.mcq_dir)
        json_files = list(json_dir.glob("*.json"))
        json_files = [f for f in json_files if "bak_" not in f.name]
        
        # Filter by subspecialty if specified
        if args.subspecialty:
            json_files = [f for f in json_files if args.subspecialty.lower() in f.name.lower()]
    
    print(f"Found {len(json_files)} JSON files to process")
    
    # Process each file
    total_imported = 0
    
    for i, json_file in enumerate(json_files):
        print(f"\n[{i+1}/{len(json_files)}] Processing {json_file.name}")
        imported = import_subspecialty(str(json_file), args.clear_subspecialty)
        total_imported += imported
    
    # Verify the import
    verify_import()
    
    print("\n====== IMPORT COMPLETED ======")
    print(f"Total MCQs imported: {total_imported}")
    print(f"Completed at: {time.strftime('%Y-%m-%d %H:%M:%S')}")


if __name__ == "__main__":
    main()