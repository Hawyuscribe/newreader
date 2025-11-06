"""
Script to clean up and format all extracted questions from the PDF.
"""

import os
import json
from datetime import datetime

def main():
    # Input file path
    input_path = '/tmp/questions_for_openai.json'
    
    # Output file path
    output_path = f'/Users/tariqalmatrudi/NEWreader/django_neurology_mcq/all_extracted_questions_{datetime.now().strftime("%Y%m%d_%H%M%S")}.txt'
    
    # Load the extracted questions
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            extracted_questions = data.get('extracted_questions', [])
    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"Error loading extracted questions: {e}")
        return
    
    print(f"Found {len(extracted_questions)} extracted questions")
    
    # Create readable text format
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(f"EXTRACTED QUESTIONS FROM 'PART I - 2024 - KSMC Revision.pdf'\n")
        f.write(f"Total Questions: {len(extracted_questions)}\n\n")
        f.write("=" * 80 + "\n\n")
        
        for i, q in enumerate(extracted_questions):
            question_text = q.get('question_text', '').strip()
            options = q.get('options', {})
            
            f.write(f"Question {i+1}:\n")
            f.write(f"{question_text}\n\n")
            
            f.write("Options:\n")
            for key, value in options.items():
                f.write(f"{key}. {value}\n")
            
            f.write("\n" + "-" * 40 + "\n\n")
    
    print(f"Successfully created readable format of all extracted questions at {output_path}")

if __name__ == "__main__":
    main()