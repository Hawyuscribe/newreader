#!/usr/bin/env python
"""
Check and analyze MCQs in the output_by_specialty folder.
"""

import os
import json
from pathlib import Path
from collections import Counter

# Path to the output_by_specialty folder
SOURCE_FOLDER = "/Users/tariqalmatrudi/Documents/FFF/output_by_specialty"

def analyze_folder():
    """Analyze the MCQs in the output_by_specialty folder."""
    source_path = Path(SOURCE_FOLDER)
    
    if not source_path.exists():
        print(f"❌ Source folder not found: {SOURCE_FOLDER}")
        return
    
    # Get all JSON files
    json_files = list(source_path.glob("*.json"))
    
    if not json_files:
        print(f"❌ No JSON files found in {SOURCE_FOLDER}")
        return
    
    print(f"✅ Found {len(json_files)} JSON files:\n")
    
    total_mcqs = 0
    subspecialty_counts = Counter()
    exam_type_counts = Counter()
    exam_year_counts = Counter()
    
    for json_file in sorted(json_files):
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                mcqs_data = json.load(f)
            
            if isinstance(mcqs_data, list):
                file_mcq_count = len(mcqs_data)
                total_mcqs += file_mcq_count
                print(f"📄 {json_file.name}: {file_mcq_count} MCQs")
                
                # Count subspecialties, exam types, and years
                for mcq in mcqs_data:
                    subspecialty_counts[mcq.get('subspecialty', 'Unknown')] += 1
                    exam_type_counts[mcq.get('exam_type', 'Unknown')] += 1
                    exam_year_counts[mcq.get('exam_year', 'Unknown')] += 1
                
                # Show sample MCQ structure from first file
                if json_file == json_files[0] and mcqs_data:
                    print(f"\n📋 Sample MCQ structure from {json_file.name}:")
                    sample = mcqs_data[0]
                    print(f"   - Keys: {list(sample.keys())}")
                    if 'explanation' in sample and isinstance(sample['explanation'], dict):
                        print(f"   - Explanation sections: {list(sample['explanation'].keys())}")
            else:
                print(f"⚠️  {json_file.name}: Invalid format (not a list)")
                
        except Exception as e:
            print(f"❌ Error reading {json_file.name}: {str(e)}")
    
    # Summary statistics
    print(f"\n{'='*60}")
    print(f"📊 SUMMARY STATISTICS")
    print(f"{'='*60}")
    print(f"Total MCQs: {total_mcqs}")
    
    print(f"\n📚 Subspecialties:")
    for subspecialty, count in subspecialty_counts.most_common():
        print(f"   - {subspecialty}: {count}")
    
    print(f"\n📝 Exam Types:")
    for exam_type, count in exam_type_counts.most_common():
        print(f"   - {exam_type}: {count}")
    
    print(f"\n📅 Exam Years:")
    for year, count in sorted(exam_year_counts.items()):
        print(f"   - {year}: {count}")

if __name__ == "__main__":
    analyze_folder()