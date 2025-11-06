#!/usr/bin/env python
import os
import json
import sys

def examine_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        print(f"File: {os.path.basename(file_path)}")
        
        # Check if it's a list or dictionary
        if isinstance(data, list):
            print(f"Data type: List with {len(data)} items")
            
            # Check the first item to see if it's metadata
            if len(data) > 0:
                first_item = data[0]
                if isinstance(first_item, dict):
                    print("First item keys:", list(first_item.keys()))
                    
                    # If we have questions in the first item
                    if "questions" in first_item:
                        print("Questions are embedded in the first item")
                
                # Now check a valid question item
                for i, item in enumerate(data):
                    if i == 0 and "source_file" in item:
                        continue  # Skip metadata item
                    
                    if isinstance(item, dict):
                        print("\nSample question structure (item", i, "):")
                        print("Keys:", list(item.keys()))
                        
                        # Check if explanation exists and what form it has
                        if "explanation" in item:
                            explanation = item["explanation"]
                            print("Explanation type:", type(explanation).__name__)
                            
                            if isinstance(explanation, dict):
                                print("Explanation keys:", list(explanation.keys()))
                            elif isinstance(explanation, str):
                                print("Explanation starts with:", explanation[:50] + "..." if len(explanation) > 50 else explanation)
                        else:
                            print("No explanation field found")
                            
                        # We only need to check one item
                        break
                        
        elif isinstance(data, dict):
            print("Data type: Dictionary")
            print("Root keys:", list(data.keys()))
            
            # Check if questions are in a key
            if "questions" in data:
                questions = data["questions"]
                print(f"Questions type: {type(questions).__name__} with {len(questions)} items")
                
                # Check a sample question
                if isinstance(questions, list) and len(questions) > 0:
                    sample = questions[0]
                    print("\nSample question structure:")
                    print("Keys:", list(sample.keys()))
                    
                    # Check if explanation exists and what form it has
                    if "explanation" in sample:
                        explanation = sample["explanation"]
                        print("Explanation type:", type(explanation).__name__)
                        
                        if isinstance(explanation, dict):
                            print("Explanation keys:", list(explanation.keys()))
                        elif isinstance(explanation, str):
                            print("Explanation starts with:", explanation[:50] + "..." if len(explanation) > 50 else explanation)
                    else:
                        print("No explanation field found")
            
        else:
            print("Unknown data structure")
            
    except Exception as e:
        print(f"Error examining file: {e}")

if __name__ == "__main__":
    # Problematic files
    base_dir = "/Users/tariqalmatrudi/Documents/MCQs for the board/Classified MCQs/with explanation"
    problematic_files = [
        os.path.join(base_dir, "Dementia.json"),
        os.path.join(base_dir, "Epilepsy.json"),
        os.path.join(base_dir, "Vascular_neurology_stroke.json"),
        os.path.join(base_dir, "Neurogenetics.json"),  # This worked
        os.path.join(base_dir, "Neuro_otology.json")   # This worked
    ]
    
    # Examine each file
    for file_path in problematic_files:
        examine_json_file(file_path)
        print("\n" + "="*50 + "\n")