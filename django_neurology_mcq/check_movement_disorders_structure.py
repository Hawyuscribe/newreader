#!/usr/bin/env python3
"""Check the structure of movement disorders MCQs JSON file"""

import json
import re

def check_json_structure(input_file):
    """Check the structure and count MCQs in the JSON file"""
    
    # Read the file content
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace NaN with null first
    fixed_content = re.sub(r'\bNaN\b', 'null', content)
    
    # Parse the JSON
    try:
        data = json.loads(fixed_content)
    except json.JSONDecodeError as e:
        print(f"JSON parsing error: {e}")
        return
    
    print(f"Top level: {type(data)}")
    
    if isinstance(data, list):
        print(f"List contains {len(data)} items")
        
        # Check structure of each item
        total_questions = 0
        for i, item in enumerate(data):
            if isinstance(item, dict):
                if 'questions' in item:
                    num_questions = len(item['questions'])
                    total_questions += num_questions
                    print(f"Item {i}: {item.get('title', 'No title')} - {num_questions} questions")
                else:
                    print(f"Item {i}: No 'questions' field")
                    print(f"  Keys: {list(item.keys())}")
        
        print(f"\nTotal questions across all items: {total_questions}")
    
    elif isinstance(data, dict):
        print(f"Dictionary with keys: {list(data.keys())}")
        if 'questions' in data:
            print(f"Questions count: {len(data['questions'])}")

if __name__ == "__main__":
    input_file = "/Users/tariqalmatrudi/Downloads/movement_disorders_mcqs_processed_full.json"
    check_json_structure(input_file)