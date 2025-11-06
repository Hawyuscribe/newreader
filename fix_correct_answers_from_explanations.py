#!/usr/bin/env python3
"""
Fix the 'correct' field in MCQs by parsing the Option Analysis section
to find which option is marked as "Correct".
"""

import json
import re
import psycopg2
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database configuration - using the actual Heroku database URL
DATABASE_URL = os.getenv('DATABASE_URL')
if not DATABASE_URL:
    # Try the Heroku-specific environment variable
    DATABASE_URL = os.getenv('HEROKU_POSTGRESQL_COPPER_URL')
    if not DATABASE_URL:
        raise Exception("No database URL found. Make sure DATABASE_URL is set.")

def parse_correct_answer(option_analysis):
    """
    Parse the option analysis text to find the correct answer.
    Returns the correct answer letter (A, B, C, or D).
    """
    if not option_analysis:
        return None
    
    # Pattern to match "Option X: ... - Correct."
    pattern = r'Option ([A-D]):\s*[^–-]+[–-]\s*Correct[^\w]'
    
    matches = re.findall(pattern, option_analysis, re.IGNORECASE | re.MULTILINE)
    
    if matches:
        return matches[0]  # Return the first match
    
    # Alternative pattern for different formatting
    # Look for lines that contain "Option X" and "Correct" on the same line
    lines = option_analysis.split('\n')
    for line in lines:
        if 'Correct' in line and not ('Incorrect' in line or 'Partially correct' in line):
            # Extract the option letter
            option_match = re.search(r'Option ([A-D])', line, re.IGNORECASE)
            if option_match:
                return option_match.group(1)
    
    return None

def update_correct_answers():
    """Update the correct answers for all MCQs based on their option analysis."""
    try:
        # Connect to the database
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        cursor = conn.cursor()
        
        # Get all MCQs with their explanations
        query = """
        SELECT id, correct, explanation 
        FROM mcq_multiplechoicequestion
        ORDER BY id;
        """
        
        cursor.execute(query)
        mcqs = cursor.fetchall()
        
        print(f"Found {len(mcqs)} MCQs to process")
        
        updated_count = 0
        no_analysis_count = 0
        no_correct_found = 0
        already_correct = 0
        
        for mcq_id, current_correct, explanation in mcqs:
            if not explanation:
                no_analysis_count += 1
                continue
            
            try:
                # Parse the explanation JSON
                if isinstance(explanation, str):
                    explanation_dict = json.loads(explanation)
                else:
                    explanation_dict = explanation
                
                # Get the option analysis section
                option_analysis = explanation_dict.get('option_analysis', '')
                
                if not option_analysis:
                    no_analysis_count += 1
                    continue
                
                # Find the correct answer from the option analysis
                parsed_correct = parse_correct_answer(option_analysis)
                
                if parsed_correct:
                    if current_correct != parsed_correct:
                        # Update the MCQ with the correct answer
                        update_query = """
                        UPDATE mcq_multiplechoicequestion 
                        SET correct = %s 
                        WHERE id = %s;
                        """
                        cursor.execute(update_query, (parsed_correct, mcq_id))
                        updated_count += 1
                        print(f"Updated MCQ {mcq_id}: {current_correct} → {parsed_correct}")
                    else:
                        already_correct += 1
                else:
                    no_correct_found += 1
                    print(f"Could not find correct answer in MCQ {mcq_id}")
                    
            except json.JSONDecodeError:
                print(f"Error parsing explanation for MCQ {mcq_id}")
                continue
            except Exception as e:
                print(f"Error processing MCQ {mcq_id}: {e}")
                continue
        
        # Commit the changes
        conn.commit()
        
        # Print summary
        print(f"\nSummary:")
        print(f"Total MCQs processed: {len(mcqs)}")
        print(f"MCQs updated: {updated_count}")
        print(f"MCQs already correct: {already_correct}")
        print(f"MCQs with no option analysis: {no_analysis_count}")
        print(f"MCQs where correct answer not found: {no_correct_found}")
        
        # Close the connection
        cursor.close()
        conn.close()
        
        # Save a log of the updates
        log_data = {
            'timestamp': datetime.now().isoformat(),
            'total_mcqs': len(mcqs),
            'updated': updated_count,
            'already_correct': already_correct,
            'no_analysis': no_analysis_count,
            'not_found': no_correct_found
        }
        
        with open('correct_answer_update_log.json', 'w') as f:
            json.dump(log_data, f, indent=2)
        
        print(f"\nLog saved to correct_answer_update_log.json")
        
    except Exception as e:
        print(f"Database error: {e}")

if __name__ == "__main__":
    print("Fixing correct answers from Option Analysis sections...")
    update_correct_answers()