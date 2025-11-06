#!/usr/bin/env python3
"""
Script to examine the structure of explanation JSON files.
"""

import os
import json
import sys

def examine_json_file(filepath):
    print(f"Examining {os.path.basename(filepath)}...")
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        print(f"  - Successfully loaded as valid JSON")
        print(f"  - Data type: {type(data)}")
        
        if isinstance(data, dict):
            print(f"  - Top-level keys: {list(data.keys())}")
            
            if 'questions' in data:
                questions = data['questions']
                print(f"  - Questions array type: {type(questions)}")
                print(f"  - Number of questions: {len(questions)}")
                
                if questions and len(questions) > 0:
                    first_question = questions[0]
                    print(f"  - First question type: {type(first_question)}")
                    
                    if isinstance(first_question, dict):
                        print(f"  - First question keys: {list(first_question.keys())}")
                        
                        if 'explanation' in first_question:
                            explanation = first_question['explanation']
                            print(f"  - Explanation type: {type(explanation)}")
                            
                            if isinstance(explanation, dict):
                                print(f"  - Explanation keys: {list(explanation.keys())}")
                            elif isinstance(explanation, str):
                                print(f"  - Explanation is a string, first 50 chars: {explanation[:50]}...")
                    else:
                        print(f"  - First question content: {first_question}")
                else:
                    print("  - No questions found in the array")
            else:
                print("  - No 'questions' key found")
        elif isinstance(data, list):
            print(f"  - Top-level is a list with {len(data)} items")
            if data and len(data) > 0:
                first_item = data[0]
                print(f"  - First item type: {type(first_item)}")
                if isinstance(first_item, dict):
                    print(f"  - First item keys: {list(first_item.keys())}")
                else:
                    print(f"  - First item content: {first_item}")
    
    except json.JSONDecodeError as e:
        print(f"  - Failed to parse as JSON: {str(e)}")
    except Exception as e:
        print(f"  - Error examining file: {str(e)}")

if __name__ == "__main__":
    # Check if filepath was provided
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
        examine_json_file(filepath)
    else:
        print("Please provide a filepath to examine")
        sys.exit(1)