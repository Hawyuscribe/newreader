#!/usr/bin/env python
"""
Fix MCQs where the correct_answer case doesn't match the options keys.
Convert all correct_answer values to uppercase to match the standard A, B, C, D format.
"""

import json
import psycopg2
import urllib.parse
from datetime import datetime

# Heroku Database URL
DATABASE_URL = "postgres://u9t1erngd4qunq:p2d2c51c149348e343682db224b056b6e26a79b06574aa5f7ca4bea27ccf78e54@c5hilnj7pn10vb.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/dceesh1rcupf4o"

def fix_case_mismatches():
    """Fix case mismatches between correct_answer and options."""
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
        
        # First, let's identify all MCQs with case mismatches
        query = """
        SELECT id, correct_answer, options
        FROM mcq_mcq
        WHERE options IS NOT NULL
        ORDER BY id;
        """
        
        cursor.execute(query)
        mcqs = cursor.fetchall()
        
        print(f"Checking {len(mcqs)} MCQs for case mismatches...")
        
        case_mismatch_count = 0
        invalid_answer_count = 0
        fixed_count = 0
        updates = []
        
        for mcq_id, correct_answer, options in mcqs:
            if not correct_answer or not options:
                continue
            
            # Check if correct_answer matches any option key
            if correct_answer not in options:
                # Check if lowercase version exists
                if correct_answer.lower() in options:
                    # Case mismatch - correct_answer is uppercase but options are lowercase
                    case_mismatch_count += 1
                    updates.append((correct_answer.upper(), mcq_id))
                    print(f"Case mismatch: MCQ {mcq_id} has correct_answer '{correct_answer}' but options have lowercase keys")
                
                # Check if uppercase version exists
                elif correct_answer.upper() in options:
                    # correct_answer is lowercase but options are uppercase
                    case_mismatch_count += 1
                    updates.append((correct_answer.upper(), mcq_id))
                    print(f"Case mismatch: MCQ {mcq_id} has correct_answer '{correct_answer}' but options have uppercase keys")
                
                # Check for other mismatches
                else:
                    # Try to find the correct option based on option analysis
                    invalid_answer_count += 1
                    if invalid_answer_count <= 10:  # Show first 10
                        print(f"Invalid answer: MCQ {mcq_id} has correct_answer '{correct_answer}' not in options: {list(options.keys())}")
        
        print(f"\nFound {case_mismatch_count} case mismatches")
        print(f"Found {invalid_answer_count} invalid answers")
        
        # Fix all case mismatches
        if updates:
            print(f"\nFixing {len(updates)} MCQs...")
            cursor.executemany(
                "UPDATE mcq_mcq SET correct_answer = %s WHERE id = %s",
                updates
            )
            conn.commit()
            fixed_count = len(updates)
            print(f"Fixed {fixed_count} MCQs")
        
        # Now fix the specific MCQ 99992898
        print("\nFixing specific MCQ 99992898...")
        query = """
        SELECT id, correct_answer, options, explanation_sections
        FROM mcq_mcq
        WHERE id = 99992898;
        """
        
        cursor.execute(query)
        result = cursor.fetchone()
        
        if result:
            mcq_id, correct_answer, options, explanation_sections = result
            
            # The correct answer should be 'a' (lowercase) based on the options
            if correct_answer == 'A' and 'a' in options:
                cursor.execute(
                    "UPDATE mcq_mcq SET correct_answer = %s WHERE id = %s",
                    ('a', mcq_id)
                )
                conn.commit()
                print(f"Fixed MCQ {mcq_id}: 'A' → 'a'")
            else:
                print(f"MCQ {mcq_id} has unexpected format: correct_answer={correct_answer}, options={list(options.keys())}")
        
        # Check for MCQs with non-standard correct_answer values
        print("\nChecking for non-standard correct_answer values...")
        query = """
        SELECT DISTINCT correct_answer, COUNT(*)
        FROM mcq_mcq
        WHERE correct_answer IS NOT NULL
        GROUP BY correct_answer
        ORDER BY correct_answer;
        """
        
        cursor.execute(query)
        answer_types = cursor.fetchall()
        
        print("\nDistinct correct_answer values:")
        for answer, count in answer_types:
            print(f"'{answer}': {count} MCQs")
        
        cursor.close()
        conn.close()
        
        # Save log
        log_data = {
            'timestamp': datetime.now().isoformat(),
            'case_mismatches_found': case_mismatch_count,
            'invalid_answers_found': invalid_answer_count,
            'mcqs_fixed': fixed_count
        }
        
        with open('case_mismatch_fix_log.json', 'w') as f:
            json.dump(log_data, f, indent=2)
        
        print(f"\nLog saved to case_mismatch_fix_log.json")
        
    except Exception as e:
        print(f"Database error: {e}")

if __name__ == "__main__":
    print("Fixing case mismatch issues in MCQs...")
    fix_case_mismatches()