#!/usr/bin/env python3
"""
Script to normalize JSON files to match the expected structure needed for import_explanations_direct.py.
"""

import os
import json
import glob
import re
from datetime import datetime

# Directories
INPUT_DIR = "/Users/tariqalmatrudi/Documents/MCQs for the board/Classified MCQs/with explanation"
OUTPUT_DIR = "/Users/tariqalmatrudi/Documents/MCQs for the board/Classified MCQs/with explanation/normalized"

# Make sure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

def normalize_json_file(input_path, output_path):
    """Normalize a JSON file to match the expected structure."""
    print(f"Processing {os.path.basename(input_path)}...")
    
    try:
        # Read the file
        with open(input_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Determine the structure
        if isinstance(data, dict) and 'questions' in data and isinstance(data['questions'], list):
            print("  - Already in the correct format.")
            normalized_data = data
        elif isinstance(data, list):
            print("  - Top level is a list, normalizing...")
            
            # Check if first item might be a header
            if len(data) > 0 and isinstance(data[0], dict) and 'questions' in data[0]:
                print("  - First item appears to be a header with questions field")
                
                # Extract questions from all items that might have them
                all_questions = []
                for item in data:
                    if isinstance(item, dict) and 'questions' in item and isinstance(item['questions'], (list, str)):
                        if isinstance(item['questions'], list):
                            all_questions.extend(item['questions'])
                        else:
                            # If questions is a string like "[", it's probably a malformed JSON
                            print(f"  - Found questions field that's a string: {item['questions']}")
                
                # Create normalized structure
                normalized_data = {
                    "source_file": os.path.basename(input_path),
                    "created": datetime.now().isoformat(),
                    "last_updated": datetime.now().isoformat(),
                    "question_count": len(all_questions),
                    "questions": all_questions
                }
            else:
                print("  - Treating entire list as questions")
                
                # Filter out items that don't look like questions
                questions = []
                for item in data:
                    if isinstance(item, dict) and ('original_question' in item or 'processed_question' in item or 'question_text' in item):
                        questions.append(item)
                
                # Create normalized structure
                normalized_data = {
                    "source_file": os.path.basename(input_path),
                    "created": datetime.now().isoformat(),
                    "last_updated": datetime.now().isoformat(),
                    "question_count": len(questions),
                    "questions": questions
                }
        else:
            print("  - Unknown structure, creating a skeleton")
            normalized_data = {
                "source_file": os.path.basename(input_path),
                "created": datetime.now().isoformat(),
                "last_updated": datetime.now().isoformat(),
                "question_count": 0,
                "questions": []
            }
        
        # Handle explanation format consistency
        if 'questions' in normalized_data and isinstance(normalized_data['questions'], list):
            for question in normalized_data['questions']:
                if isinstance(question, dict) and 'explanation' in question:
                    explanation = question['explanation']
                    
                    # If explanation is a string that looks like it might be JSON, try to parse it
                    if isinstance(explanation, str) and explanation.strip().startswith('{'):
                        try:
                            parsed_explanation = json.loads(explanation)
                            question['explanation'] = parsed_explanation
                            print("  - Converted string explanation to object")
                        except:
                            pass
        
        # Write the normalized data
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(normalized_data, f, indent=2)
        
        print(f"  - Successfully wrote normalized JSON with {normalized_data['question_count']} questions")
        return True
    
    except json.JSONDecodeError as e:
        print(f"  - Failed to parse as JSON: {str(e)}")
        return False
    except Exception as e:
        print(f"  - Error processing file: {str(e)}")
        return False

def main():
    """Normalize all JSON files in the input directory."""
    # Get all JSON files
    json_files = glob.glob(os.path.join(INPUT_DIR, "*.json"))
    
    # Exclude backup files and the output directory
    json_files = [f for f in json_files if not ('.bak' in f or 'original_bak' in f) and not os.path.dirname(f).endswith('normalized')]
    
    print(f"Found {len(json_files)} JSON files to process.")
    
    # Process each file
    successful = 0
    failed = 0
    
    for input_path in json_files:
        base_name = os.path.basename(input_path)
        output_path = os.path.join(OUTPUT_DIR, base_name)
        
        if normalize_json_file(input_path, output_path):
            successful += 1
        else:
            failed += 1
    
    print(f"\nResults: {successful} files normalized, {failed} files failed.")

if __name__ == "__main__":
    main()