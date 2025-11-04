#!/usr/bin/env python
"""
Fix MCQs with non-standard correct_answer values by parsing their option analysis.
"""

import json
import re
import psycopg2
import urllib.parse
from datetime import datetime

# Heroku Database URL
DATABASE_URL = "postgres://u9t1erngd4qunq:p2d2c51c149348e343682db224b056b6e26a79b06574aa5f7ca4bea27ccf78e54@c5hilnj7pn10vb.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/dceesh1rcupf4o"

def parse_correct_answer_from_analysis(option_analysis, options):
    """
    Parse the option analysis to find the correct answer.
    Also checks if the found answer exists in the options.
    """
    if not option_analysis:
        return None
    
    # Clean up the text
    option_analysis = option_analysis.replace('–', '-').replace('—', '-').replace('‐', '-')
    
    # Method 1: Look for explicit correct statements
    lines = option_analysis.split('\n')
    for i, line in enumerate(lines):
        if "correct" in line.lower() and "incorrect" not in line.lower():
            # Check for option letter in same line
            option_match = re.search(r'Option ([A-Da-d])', line, re.IGNORECASE)
            if option_match:
                letter = option_match.group(1).upper()
                # Check if this option exists in the MCQ options
                if letter in options or letter.lower() in options:
                    return letter if letter in options else letter.lower()
        
        # Look for patterns like "A is correct" or "A: correct"
        if re.search(r'^[A-Da-d][:)]\s*correct', line, re.IGNORECASE):
            letter = line[0].upper()
            if letter in options or letter.lower() in options:
                return letter if letter in options else letter.lower()
    
    # Method 2: Look for "This is the correct answer" and find which option it refers to
    for i, line in enumerate(lines):
        if "this is the correct answer" in line.lower():
            # Look backwards to find which option this refers to
            for j in range(i, max(-1, i-5), -1):
                if j < len(lines):
                    prev_line = lines[j]
                    option_match = re.search(r'Option ([A-Da-d])', prev_line, re.IGNORECASE)
                    if option_match:
                        letter = option_match.group(1).upper()
                        if letter in options or letter.lower() in options:
                            return letter if letter in options else letter.lower()
    
    return None

def fix_nonstandard_answers():
    """Fix MCQs with non-standard correct answers."""
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
        
        # Get MCQs with non-standard correct answers
        query = """
        SELECT id, correct_answer, options, explanation_sections
        FROM mcq_mcq
        WHERE correct_answer IS NOT NULL
        AND correct_answer NOT IN ('A', 'B', 'C', 'D', 'a', 'b', 'c', 'd')
        ORDER BY id;
        """
        
        cursor.execute(query)
        mcqs = cursor.fetchall()
        
        print(f"Found {len(mcqs)} MCQs with non-standard correct answers")
        
        fixed_count = 0
        cannot_fix_count = 0
        updates = []
        
        # Process each MCQ
        for mcq_id, current_correct, options, explanation_sections in mcqs:
            if not options:
                cannot_fix_count += 1
                continue
            
            # Try to find correct answer from option analysis
            correct_answer = None
            
            if explanation_sections and isinstance(explanation_sections, dict):
                option_analysis = explanation_sections.get('option_analysis', '')
                if option_analysis:
                    correct_answer = parse_correct_answer_from_analysis(option_analysis, options)
            
            if correct_answer:
                updates.append((correct_answer, mcq_id))
                fixed_count += 1
                if fixed_count <= 10:  # Show first 10
                    print(f"Will fix MCQ {mcq_id}: '{current_correct}' → '{correct_answer}'")
            else:
                cannot_fix_count += 1
                if cannot_fix_count <= 5:  # Show first 5
                    print(f"Cannot fix MCQ {mcq_id}: '{current_correct}', options: {list(options.keys())}")
        
        # Apply updates
        if updates:
            print(f"\nApplying {len(updates)} fixes...")
            cursor.executemany(
                "UPDATE mcq_mcq SET correct_answer = %s WHERE id = %s",
                updates
            )
            conn.commit()
            print(f"Fixed {fixed_count} MCQs")
        
        # Now check for MCQs with empty/null correct answers
        print("\nChecking for MCQs with empty/null correct answers...")
        query = """
        SELECT COUNT(*)
        FROM mcq_mcq
        WHERE correct_answer IS NULL OR correct_answer = '';
        """
        
        cursor.execute(query)
        empty_count = cursor.fetchone()[0]
        print(f"MCQs with empty/null correct answers: {empty_count}")
        
        # Summary
        print(f"\nFinal Summary:")
        print(f"MCQs with non-standard answers: {len(mcqs)}")
        print(f"MCQs fixed: {fixed_count}")
        print(f"MCQs that couldn't be fixed: {cannot_fix_count}")
        
        cursor.close()
        conn.close()
        
        # Save log
        log_data = {
            'timestamp': datetime.now().isoformat(),
            'nonstandard_answers_found': len(mcqs),
            'fixed': fixed_count,
            'cannot_fix': cannot_fix_count
        }
        
        with open('nonstandard_answers_fix_log.json', 'w') as f:
            json.dump(log_data, f, indent=2)
        
    except Exception as e:
        print(f"Database error: {e}")

if __name__ == "__main__":
    print("Fixing non-standard correct answers...")
    fix_nonstandard_answers()