#!/usr/bin/env python
"""
Fix the specific MCQ and debug why it wasn't updated.
"""

import json
import psycopg2
import urllib.parse
import re

# Heroku Database URL
DATABASE_URL = "postgres://u9t1erngd4qunq:p2d2c51c149348e343682db224b056b6e26a79b06574aa5f7ca4bea27ccf78e54@c5hilnj7pn10vb.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/dceesh1rcupf4o"

def parse_correct_answer_improved(option_analysis):
    """
    Improved parsing of option analysis to find correct answer.
    """
    if not option_analysis:
        return None
    
    # Pattern 1: "Option X: ... – Correct." (with various dashes)
    pattern1 = r'Option ([A-D]):\s*[^–—-]*[–—-]\s*Correct'
    
    matches = re.findall(pattern1, option_analysis, re.IGNORECASE | re.MULTILINE)
    
    if matches:
        return matches[0].upper()
    
    # Pattern 2: Look for lines with "Option X" and "Correct" but not "Incorrect"
    lines = option_analysis.split('\n')
    for line in lines:
        # Check if line contains an option and "Correct" but not "Incorrect" or "Partially correct"
        if re.search(r'Option ([A-D])', line, re.IGNORECASE):
            if ('Correct' in line or 'correct' in line) and \
               ('Incorrect' not in line and 'incorrect' not in line) and \
               ('Partially' not in line and 'partially' not in line):
                option_match = re.search(r'Option ([A-D])', line, re.IGNORECASE)
                if option_match:
                    return option_match.group(1).upper()
    
    return None

def fix_mcq():
    """Fix the specific MCQ and check why it wasn't updated."""
    try:
        print("Connecting to Heroku PostgreSQL database...")
        
        # Parse the database URL
        result = urllib.parse.urlparse(DATABASE_URL)
        username = result.username
        password = result.password
        database = result.path[1:]
        hostname = result.hostname
        port = result.port
        
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            database=database,
            user=username,
            password=password,
            host=hostname,
            port=port
        )
        
        cursor = conn.cursor()
        print("Connected successfully!")
        
        # Get the specific MCQ
        mcq_id = 99992893
        
        query = """
        SELECT id, question_text, correct_answer, explanation_sections
        FROM mcq_mcq
        WHERE id = %s;
        """
        
        cursor.execute(query, (mcq_id,))
        result = cursor.fetchone()
        
        if result:
            mcq_id, question_text, current_correct, explanation_sections = result
            
            print(f"\nCurrent state:")
            print(f"MCQ ID: {mcq_id}")
            print(f"Question: {question_text[:100]}...")
            print(f"Current correct answer: {current_correct}")
            
            if explanation_sections and isinstance(explanation_sections, dict):
                option_analysis = explanation_sections.get('option_analysis', '')
                if option_analysis:
                    parsed_correct = parse_correct_answer_improved(option_analysis)
                    print(f"Parsed correct answer: {parsed_correct}")
                    
                    if parsed_correct and parsed_correct != current_correct:
                        # Update the MCQ
                        update_query = """
                        UPDATE mcq_mcq 
                        SET correct_answer = %s 
                        WHERE id = %s;
                        """
                        cursor.execute(update_query, (parsed_correct, mcq_id))
                        conn.commit()
                        print(f"Updated MCQ {mcq_id}: {current_correct} → {parsed_correct}")
                    else:
                        print("No update needed or couldn't parse correct answer")
                else:
                    print("No option analysis found")
            else:
                print("No explanation sections found")
        
        # Now check all MCQs that still have wrong answers
        print("\nChecking for other MCQs with similar issues...")
        
        query = """
        SELECT id, correct_answer, explanation_sections
        FROM mcq_mcq
        WHERE explanation_sections IS NOT NULL
        AND explanation_sections::text LIKE '%Option D%Irritability%Correct%'
        AND correct_answer != 'D';
        """
        
        cursor.execute(query)
        similar_mcqs = cursor.fetchall()
        
        print(f"Found {len(similar_mcqs)} MCQs with similar pattern")
        
        for mcq_id, current_correct, explanation_sections in similar_mcqs:
            if isinstance(explanation_sections, dict):
                option_analysis = explanation_sections.get('option_analysis', '')
                if option_analysis:
                    parsed_correct = parse_correct_answer_improved(option_analysis)
                    if parsed_correct and parsed_correct != current_correct:
                        update_query = """
                        UPDATE mcq_mcq 
                        SET correct_answer = %s 
                        WHERE id = %s;
                        """
                        cursor.execute(update_query, (parsed_correct, mcq_id))
                        print(f"Updated MCQ {mcq_id}: {current_correct} → {parsed_correct}")
        
        conn.commit()
        
        # Close the connection
        cursor.close()
        conn.close()
        
    except Exception as e:
        print(f"Database error: {e}")

if __name__ == "__main__":
    print("Fixing specific MCQ and similar ones...")
    fix_mcq()