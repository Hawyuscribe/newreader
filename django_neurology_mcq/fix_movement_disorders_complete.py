#!/usr/bin/env python3
"""Fix syntax errors in movement disorders MCQs JSON file and preserve all questions"""

import json
import re

def fix_json_syntax(input_file, output_file):
    """Fix JSON syntax errors like NaN values and preserve all data"""
    
    # Read the file content
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace NaN with null (valid JSON)
    fixed_content = re.sub(r'\bNaN\b', 'null', content)
    
    # Try to parse the JSON to verify it's valid
    try:
        data = json.loads(fixed_content)
        print(f"Successfully parsed JSON")
    except json.JSONDecodeError as e:
        print(f"JSON parsing error: {e}")
        return
    
    # Count questions
    total_questions = 0
    if isinstance(data, list):
        for item in data:
            if isinstance(item, dict) and 'questions' in item:
                total_questions += len(item['questions'])
                print(f"{item.get('title', 'No title')}: {len(item['questions'])} questions")
    
    print(f"\nTotal questions: {total_questions}")
    
    # Write the fixed content with proper formatting
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"\nFixed JSON written to {output_file}")
    print(f"Preserved {len(data)} exam sections with {total_questions} total questions")

if __name__ == "__main__":
    input_file = "/Users/tariqalmatrudi/Downloads/movement_disorders_mcqs_processed_full.json"
    output_file = "/Users/tariqalmatrudi/Downloads/movement_disorders_mcqs_fixed.json"
    fix_json_syntax(input_file, output_file)