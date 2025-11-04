#!/usr/bin/env python3
"""Verify the fixed JSON file and see what's actually in it"""

import json

def verify_json_file(file_path):
    """Check what's actually in the fixed JSON file"""
    
    # Read the file
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    print(f"File: {file_path}")
    print(f"Type of data: {type(data)}")
    
    if isinstance(data, list):
        print(f"Number of top-level items: {len(data)}")
        
        # Check if first item has questions
        if len(data) > 0 and isinstance(data[0], dict):
            print(f"\nFirst item structure:")
            print(f"Keys: {list(data[0].keys())}")
            
            if 'questions' in data[0]:
                print(f"Number of questions in first item: {len(data[0]['questions'])}")
                
                # Count total questions
                total_questions = 0
                for i, item in enumerate(data):
                    if 'questions' in item:
                        num_q = len(item['questions'])
                        total_questions += num_q
                        print(f"Item {i} ({item.get('title', 'No title')}): {num_q} questions")
                
                print(f"\nTotal questions: {total_questions}")
    
    # Let's also check the file size
    import os
    file_size = os.path.getsize(file_path)
    print(f"\nFile size: {file_size:,} bytes ({file_size/1024/1024:.2f} MB)")
    
    # Sample the beginning of the file
    with open(file_path, 'r', encoding='utf-8') as f:
        first_500_chars = f.read(500)
        print(f"\nFirst 500 characters of file:")
        print(first_500_chars)

if __name__ == "__main__":
    fixed_file = "/Users/tariqalmatrudi/Downloads/movement_disorders_mcqs_fixed.json"
    verify_json_file(fixed_file)