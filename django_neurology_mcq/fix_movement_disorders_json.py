#!/usr/bin/env python3
"""Fix syntax errors in movement disorders MCQs JSON file"""

import json
import re

def fix_json_syntax(input_file, output_file):
    """Fix JSON syntax errors like NaN values"""
    
    # Read the file content
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace NaN with null (valid JSON)
    fixed_content = re.sub(r'\bNaN\b', 'null', content)
    
    # Try to parse the JSON to verify it's valid
    try:
        data = json.loads(fixed_content)
        print(f"Successfully parsed JSON with {len(data)} items")
    except json.JSONDecodeError as e:
        print(f"JSON parsing error: {e}")
        # Try to identify other potential issues
        lines = fixed_content.split('\n')
        error_line = e.lineno - 1
        print(f"Error around line {e.lineno}:")
        for i in range(max(0, error_line - 5), min(len(lines), error_line + 5)):
            print(f"{i+1}: {lines[i]}")
        return
    
    # Write the fixed content
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"Fixed JSON written to {output_file}")

if __name__ == "__main__":
    input_file = "/Users/tariqalmatrudi/Downloads/movement_disorders_mcqs_processed_full.json"
    output_file = "/Users/tariqalmatrudi/Downloads/movement_disorders_mcqs_fixed.json"
    fix_json_syntax(input_file, output_file)