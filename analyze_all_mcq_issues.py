#!/usr/bin/env python
"""
Comprehensive analysis of all MCQ issues to understand why they show all options as incorrect.
"""

import json
import psycopg2
import urllib.parse

# Heroku Database URL
DATABASE_URL = "postgres://u9t1erngd4qunq:p2d2c51c149348e343682db224b056b6e26a79b06574aa5f7ca4bea27ccf78e54@c5hilnj7pn10vb.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/dceesh1rcupf4o"

def analyze_all_issues():
    """Analyze all remaining MCQ issues."""
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
        
        # 1. Check MCQs where correct_answer doesn't match any option
        print("\n1. MCQs where correct_answer doesn't match any option:")
        query = """
        SELECT id, correct_answer, options
        FROM mcq_mcq
        WHERE options IS NOT NULL
        AND correct_answer IS NOT NULL
        AND NOT (correct_answer = ANY(SELECT jsonb_object_keys(options)))
        ORDER BY id
        LIMIT 10;
        """
        
        cursor.execute(query)
        mismatches = cursor.fetchall()
        
        print(f"Found {len(mismatches)} examples of mismatches:")
        for mcq_id, correct_answer, options in mismatches:
            print(f"MCQ {mcq_id}: correct='{correct_answer}', options={list(options.keys())}")
        
        # 2. Check MCQs with empty or null options
        print("\n2. MCQs with empty or null options:")
        query = """
        SELECT COUNT(*)
        FROM mcq_mcq
        WHERE options IS NULL OR options = '{}';
        """
        
        cursor.execute(query)
        empty_options_count = cursor.fetchone()[0]
        print(f"MCQs with empty/null options: {empty_options_count}")
        
        # 3. Group by correct_answer to see patterns
        print("\n3. Distribution of correct_answer values:")
        query = """
        SELECT correct_answer, COUNT(*) as count
        FROM mcq_mcq
        WHERE correct_answer NOT IN ('A', 'B', 'C', 'D', 'a', 'b', 'c', 'd')
        GROUP BY correct_answer
        ORDER BY count DESC
        LIMIT 20;
        """
        
        cursor.execute(query)
        distributions = cursor.fetchall()
        
        for answer, count in distributions:
            print(f"  '{answer}': {count} MCQs")
        
        # 4. Check MCQs with non-standard options structure
        print("\n4. MCQs with non-standard options structure:")
        query = """
        SELECT id, options
        FROM mcq_mcq
        WHERE options IS NOT NULL
        AND NOT (
            options ? 'A' OR options ? 'B' OR options ? 'C' OR options ? 'D' OR
            options ? 'a' OR options ? 'b' OR options ? 'c' OR options ? 'd'
        )
        LIMIT 5;
        """
        
        cursor.execute(query)
        nonstandard = cursor.fetchall()
        
        for mcq_id, options in nonstandard:
            print(f"MCQ {mcq_id}: options={list(options.keys())}")
        
        # 5. Specific check for the problematic MCQ
        print("\n5. Detailed check of MCQ 99992898:")
        query = """
        SELECT id, question_text, correct_answer, options, 
               (correct_answer = ANY(SELECT jsonb_object_keys(options))) as answer_matches
        FROM mcq_mcq
        WHERE id = 99992898;
        """
        
        cursor.execute(query)
        result = cursor.fetchone()
        
        if result:
            mcq_id, question, correct_answer, options, matches = result
            print(f"ID: {mcq_id}")
            print(f"Question: {question[:50]}...")
            print(f"Correct answer: '{correct_answer}'")
            print(f"Options: {json.dumps(options, indent=2)}")
            print(f"Answer matches option: {matches}")
        
        cursor.close()
        conn.close()
        
    except Exception as e:
        print(f"Database error: {e}")

if __name__ == "__main__":
    print("Analyzing all MCQ issues...")
    analyze_all_issues()