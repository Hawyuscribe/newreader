#!/usr/bin/env python3
"""
Script to create Django fixtures from MCQ JSON files.
This script prepares files for manual upload to Heroku.
"""
import os
import json
import argparse
from pathlib import Path

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

def get_file_subspecialty(filename):
    """Extract subspecialty from the filename."""
    for key in SUBSPECIALTY_MAPPING.keys():
        if key in filename.lower():
            return SUBSPECIALTY_MAPPING[key]
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

def create_fixtures_from_mcqs(mcqs, subspecialty, source_file):
    """Create Django fixtures from a list of MCQs."""
    fixtures = []
    
    for mcq_data in mcqs:
        # Extract data from the MCQ
        mcq_id = mcq_data.get('ID')
        
        # Skip if ID is missing
        if not mcq_id:
            continue
        
        question_number = mcq_data.get('Question Number')
        question_text = mcq_data.get('Question Text', '')
        
        # Skip if question text is missing
        if not question_text:
            continue
            
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
        
        # Skip if there's no correct answer
        if not correct_answer:
            continue
            
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
                "source_file": os.path.basename(source_file)
            }
        }
        
        # Add image URL if present
        if 'Image URL' in mcq_data and mcq_data['Image URL']:
            fixture_entry["fields"]["image_url"] = mcq_data['Image URL']
        
        fixtures.append(fixture_entry)
    
    return fixtures

def process_json_file(json_file, output_dir, chunk_size=50):
    """Process a JSON file and create Django fixtures."""
    print(f"\nProcessing {os.path.basename(json_file)}")
    
    # Extract subspecialty from filename
    subspecialty = get_file_subspecialty(os.path.basename(json_file))
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
    
    # Split into chunks
    num_chunks = (total_mcqs + chunk_size - 1) // chunk_size
    print(f"Splitting into {num_chunks} chunks of up to {chunk_size} MCQs")
    
    # Create output directory for subspecialty
    subspecialty_dir = os.path.join(output_dir, subspecialty.replace('/', '_').replace(' ', '_'))
    os.makedirs(subspecialty_dir, exist_ok=True)
    
    # Process each chunk
    fixtures_created = 0
    
    for i in range(num_chunks):
        chunk_start = i * chunk_size
        chunk_end = min((i + 1) * chunk_size, total_mcqs)
        
        print(f"Processing chunk {i+1}/{num_chunks} (MCQs {chunk_start+1}-{chunk_end})...")
        
        # Extract MCQs for this chunk
        chunk_mcqs = mcqs[chunk_start:chunk_end]
        
        # Create fixtures
        fixtures = create_fixtures_from_mcqs(chunk_mcqs, subspecialty, json_file)
        
        if fixtures:
            # Create fixture file
            fixture_file = os.path.join(subspecialty_dir, f"chunk_{i+1}_of_{num_chunks}.json")
            with open(fixture_file, 'w', encoding='utf-8') as f:
                json.dump(fixtures, f, indent=2, ensure_ascii=False)
            
            fixtures_created += len(fixtures)
            print(f"✅ Created fixture with {len(fixtures)} MCQs: {os.path.basename(fixture_file)}")
        else:
            print(f"❌ No valid MCQs in chunk {i+1}")
    
    print(f"\nFinished processing {os.path.basename(json_file)}")
    print(f"Total fixtures created: {fixtures_created} out of {total_mcqs} MCQs")
    
    return fixtures_created

def main():
    """Main function to create fixtures."""
    parser = argparse.ArgumentParser(description='Create Django fixtures from MCQ JSON files')
    parser.add_argument('--mcq-dir', default="/Users/tariqalmatrudi/Documents/MCQs for the board/test/json f", 
                      help='Directory containing MCQ JSON files')
    parser.add_argument('--output-dir', default="/Users/tariqalmatrudi/NEWreader/fixtures",
                      help='Directory to save the fixture files')
    parser.add_argument('--chunk-size', type=int, default=50, 
                      help='Number of MCQs per chunk')
    parser.add_argument('--file', help='Process a specific file only')
    parser.add_argument('--subspecialty', help='Only process files for this subspecialty')
    
    args = parser.parse_args()
    
    print("====== DJANGO FIXTURE CREATION ======")
    
    # Create output directory
    os.makedirs(args.output_dir, exist_ok=True)
    
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
    total_fixtures = 0
    
    for i, json_file in enumerate(json_files):
        print(f"\n[{i+1}/{len(json_files)}] Processing {json_file.name}")
        fixtures_created = process_json_file(
            str(json_file), 
            args.output_dir,
            chunk_size=args.chunk_size
        )
        total_fixtures += fixtures_created
    
    # Create manifest file
    manifest = {
        "total_mcqs": total_fixtures,
        "subspecialties": []
    }
    
    # List all fixture files for the manifest
    for subdir in os.listdir(args.output_dir):
        subdir_path = os.path.join(args.output_dir, subdir)
        if os.path.isdir(subdir_path):
            fixture_files = [f for f in os.listdir(subdir_path) if f.endswith('.json')]
            manifest["subspecialties"].append({
                "subspecialty": subdir.replace('_', ' '),
                "fixture_count": len(fixture_files),
                "fixture_files": fixture_files
            })
    
    # Write manifest
    manifest_file = os.path.join(args.output_dir, "manifest.json")
    with open(manifest_file, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    
    print("\n====== FIXTURE CREATION COMPLETED ======")
    print(f"Total fixtures created: {total_fixtures} MCQs")
    print(f"Fixtures saved to: {args.output_dir}")
    print(f"Manifest file: {manifest_file}")
    print("\nTo upload these fixtures to Heroku:")
    print("1. Open the Heroku dashboard (https://dashboard.heroku.com)")
    print("2. Select your app: radiant-gorge-35079")
    print("3. Go to the 'More' dropdown and select 'Run Console'")
    print("4. Upload the fixtures using the Django management command:")
    print("   python manage.py loaddata /path/to/fixture.json")
    print("   or use the command: python import_fixtures.py to import all fixtures")


if __name__ == "__main__":
    main()