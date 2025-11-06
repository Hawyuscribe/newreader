#!/usr/bin/env python
"""
Comprehensive fix for ALL case mismatches between correct_answer and options.
Ensures correct_answer matches the case of the options keys.
"""

import json
import psycopg2
import urllib.parse
from datetime import datetime

# Heroku Database URL
DATABASE_URL = "postgres://u9t1erngd4qunq:p2d2c51c149348e343682db224b056b6e26a79b06574aa5f7ca4bea27ccf78e54@c5hilnj7pn10vb.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/dceesh1rcupf4o"

def fix_all_case_mismatches():
    """Fix all case mismatches comprehensively."""
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
        
        # Get all MCQs with their options
        query = """
        SELECT id, correct_answer, options
        FROM mcq_mcq
        WHERE options IS NOT NULL
        AND correct_answer IS NOT NULL
        ORDER BY id;
        """
        
        cursor.execute(query)
        mcqs = cursor.fetchall()
        
        print(f"Checking {len(mcqs)} MCQs for case mismatches...")
        
        updates = []
        fixed_count = 0
        already_correct = 0
        
        for mcq_id, correct_answer, options in mcqs:
            if not options:
                continue
            
            # Check if correct_answer exists in options
            if correct_answer in options:
                already_correct += 1
                continue
            
            # Check if the case-changed version exists
            lower_answer = correct_answer.lower()
            upper_answer = correct_answer.upper()
            
            new_answer = None
            
            # If uppercase answer but lowercase options exist
            if upper_answer == correct_answer and lower_answer in options:
                new_answer = lower_answer
            # If lowercase answer but uppercase options exist
            elif lower_answer == correct_answer and upper_answer in options:
                new_answer = upper_answer
            # Check each option key to match the case
            elif correct_answer in ['A', 'B', 'C', 'D']:
                if correct_answer.lower() in options:
                    new_answer = correct_answer.lower()
            elif correct_answer in ['a', 'b', 'c', 'd']:
                if correct_answer.upper() in options:
                    new_answer = correct_answer.upper()
            
            if new_answer:
                updates.append((new_answer, mcq_id))
                fixed_count += 1
                if fixed_count <= 10:  # Show first 10
                    print(f"Will fix MCQ {mcq_id}: '{correct_answer}' → '{new_answer}' (options: {list(options.keys())})")
        
        # Apply all updates
        if updates:
            print(f"\nApplying {len(updates)} fixes...")
            cursor.executemany(
                "UPDATE mcq_mcq SET correct_answer = %s WHERE id = %s",
                updates
            )
            conn.commit()
            print(f"Fixed {fixed_count} MCQs")
        
        # Verify all MCQs now have matching answers
        print("\nVerifying all MCQs...")
        query = """
        SELECT COUNT(*)
        FROM mcq_mcq
        WHERE options IS NOT NULL
        AND correct_answer IS NOT NULL
        AND correct_answer IN ('A', 'B', 'C', 'D', 'a', 'b', 'c', 'd')
        AND NOT (
            correct_answer = ANY(SELECT jsonb_object_keys(options))
        );
        """
        
        cursor.execute(query)
        mismatch_count = cursor.fetchone()[0]
        print(f"Remaining MCQs with case mismatches: {mismatch_count}")
        
        # Check specific categories
        print("\nChecking specific categories of mismatches:")
        
        # MCQs with uppercase answers but lowercase options
        query = """
        SELECT COUNT(*)
        FROM mcq_mcq
        WHERE correct_answer IN ('A', 'B', 'C', 'D')
        AND options ? 'a'
        AND NOT options ? 'A';
        """
        
        cursor.execute(query)
        upper_lower_count = cursor.fetchone()[0]
        print(f"MCQs with uppercase answers but lowercase options: {upper_lower_count}")
        
        # MCQs with lowercase answers but uppercase options
        query = """
        SELECT COUNT(*)
        FROM mcq_mcq
        WHERE correct_answer IN ('a', 'b', 'c', 'd')
        AND options ? 'A'
        AND NOT options ? 'a';
        """
        
        cursor.execute(query)
        lower_upper_count = cursor.fetchone()[0]
        print(f"MCQs with lowercase answers but uppercase options: {lower_upper_count}")
        
        cursor.close()
        conn.close()
        
        # Save log
        log_data = {
            'timestamp': datetime.now().isoformat(),
            'total_checked': len(mcqs),
            'fixed': fixed_count,
            'already_correct': already_correct,
            'remaining_mismatches': mismatch_count
        }
        
        with open('comprehensive_case_fix_log.json', 'w') as f:
            json.dump(log_data, f, indent=2)
        
        print(f"\nLog saved to comprehensive_case_fix_log.json")
        
    except Exception as e:
        print(f"Database error: {e}")

if __name__ == "__main__":
    print("Running comprehensive case mismatch fix...")
    fix_all_case_mismatches()