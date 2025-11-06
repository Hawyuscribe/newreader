#!/usr/bin/env python3
"""Combine all JSON files from RERE directory into a single combined JSON file."""

import json
import os
from pathlib import Path

# Source directory
RERE_DIR = Path('/Users/tariqalmatrudi/Documents/MCQs for the board/Previous MCQs/json explained/reclass/RERE')
OUTPUT_FILE = Path('/Users/tariqalmatrudi/NEWreader/rere_combined.json')

# Subspecialty mapping (from filename to proper database name)
SUBSPECIALTY_MAPPING = {
    'anatomy': 'Neuroanatomy',
    'critical_care_neurology': 'Critical Care Neurology',
    'dementia': 'Dementia',
    'epilepsy': 'Epilepsy',
    'headache': 'Headache',
    'movement_disorders': 'Movement Disorders',
    'neuro-otology': 'Neuro-otology',
    'neurogenetics': 'Neurogenetics',
    'neuroimmunology': 'Neuroimmunology',
    'neuroinfectious': 'Neuro-infectious',
    'neuromuscular': 'Neuromuscular',
    'neurooncology': 'Neuro-oncology',
    'neuroophthalmology': 'Neuroophthalmology',
    'neuropsychiatry': 'Neuropsychiatry',
    'neurotoxicology': 'Neurotoxicology',
    'other': 'Other/Unclassified',
    'pediatric_neurology': 'Pediatric Neurology',
    'sleep_neurology': 'Sleep Neurology',
    'vascular_neurology': 'Vascular Neurology/Stroke'
}

def main():
    combined_data = []
    total_mcqs = 0
    file_stats = {}
    
    print(f"Loading JSON files from: {RERE_DIR}")
    
    # Get all JSON files in the directory
    json_files = sorted(RERE_DIR.glob('*.json'))
    
    for json_file in json_files:
        # Extract subspecialty from filename
        filename = json_file.stem
        subspecialty = SUBSPECIALTY_MAPPING.get(filename, filename)
        
        try:
            print(f"Processing: {json_file.name}")
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            # Handle different possible JSON structures
            if isinstance(data, list):
                mcqs = data
            elif isinstance(data, dict) and 'mcqs' in data:
                mcqs = data['mcqs']
            elif isinstance(data, dict) and 'questions' in data:
                mcqs = data['questions']
            else:
                # Assume the dict contains MCQs directly
                mcqs = [data] if data else []
            
            # Process each MCQ
            for mcq in mcqs:
                # Ensure subspecialty is properly set
                if 'subspecialty' not in mcq or not mcq['subspecialty']:
                    mcq['subspecialty'] = subspecialty
                
                # If subspecialty doesn't match expected mapping, fix it
                if mcq['subspecialty'] != subspecialty and filename in SUBSPECIALTY_MAPPING:
                    mcq['original_subspecialty'] = mcq['subspecialty']
                    mcq['subspecialty'] = subspecialty
                
                combined_data.append(mcq)
            
            file_count = len(mcqs)
            total_mcqs += file_count
            file_stats[json_file.name] = file_count
            print(f"  - Loaded {file_count} MCQs from {json_file.name}")
            
        except Exception as e:
            print(f"Error processing {json_file.name}: {e}")
            continue
    
    # Save combined data
    print(f"\nSaving combined data to: {OUTPUT_FILE}")
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(combined_data, f, indent=2, ensure_ascii=False)
    
    # Print summary
    print(f"\n=== Summary ===")
    print(f"Total MCQs combined: {total_mcqs}")
    print(f"Output file: {OUTPUT_FILE}")
    print(f"\nBreakdown by file:")
    for filename, count in file_stats.items():
        print(f"  {filename}: {count} MCQs")
    
    # Verify subspecialty distribution
    subspecialty_counts = {}
    for mcq in combined_data:
        subspecialty = mcq.get('subspecialty', 'Unknown')
        subspecialty_counts[subspecialty] = subspecialty_counts.get(subspecialty, 0) + 1
    
    print(f"\nSubspecialty distribution:")
    for subspecialty, count in sorted(subspecialty_counts.items()):
        print(f"  {subspecialty}: {count} MCQs")
    
    return total_mcqs

if __name__ == "__main__":
    total = main()
    print(f"\nCombined file created successfully with {total} MCQs!")