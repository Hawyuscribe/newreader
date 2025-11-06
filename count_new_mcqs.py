#!/usr/bin/env python3

import json
import glob
import os

directory_path = '/Users/tariqalmatrudi/Documents/FFF/output_by_specialty'
json_files = glob.glob(os.path.join(directory_path, '*.json'))

total_mcqs = 0
specialty_counts = {}

for json_file in json_files:
    filename = os.path.basename(json_file)
    
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if 'mcqs' in data:
            specialty = data.get('specialty', 'Unknown')
            count = len(data['mcqs'])
            specialty_counts[specialty] = count
            total_mcqs += count
    except:
        pass

print(f"Total MCQs in new files: {total_mcqs}")
print(f"Total specialties: {len(specialty_counts)}")
print("\nBreakdown by specialty:")
for specialty, count in sorted(specialty_counts.items()):
    print(f"  - {specialty}: {count}")