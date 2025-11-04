#!/usr/bin/env python3
"""Flatten the movement disorders JSON to a single list of all questions"""

import json

def flatten_json_structure(input_file, output_file):
    """Convert nested structure to flat list of all questions"""
    
    # Read the file
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Extract all questions into a single list
    all_questions = []
    
    for section in data:
        if 'questions' in section:
            section_title = section.get('title', 'Unknown')
            for question in section['questions']:
                # Add the section title to each question
                question['exam_section'] = section_title
                all_questions.append(question)
    
    print(f"Extracted {len(all_questions)} questions from {len(data)} sections")
    
    # Write the flattened structure
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_questions, f, indent=2, ensure_ascii=False)
    
    print(f"Flattened JSON written to {output_file}")
    
    # Also create a simple text summary
    summary_file = output_file.replace('.json', '_summary.txt')
    with open(summary_file, 'w', encoding='utf-8') as f:
        f.write(f"Total questions: {len(all_questions)}\n\n")
        for i, q in enumerate(all_questions):
            f.write(f"{i+1}. [{q.get('exam_section', 'Unknown')}] Q{q.get('question_number', '?')}: {q.get('question_text', 'No text')[:100]}...\n")
    
    print(f"Summary written to {summary_file}")

if __name__ == "__main__":
    input_file = "/Users/tariqalmatrudi/Downloads/movement_disorders_mcqs_fixed.json"
    output_file = "/Users/tariqalmatrudi/Downloads/movement_disorders_mcqs_flattened.json"
    flatten_json_structure(input_file, output_file)