#!/usr/bin/env python
"""
Analyze the specific MCQ that has issues with all options showing as incorrect.
"""

import json
import psycopg2
import urllib.parse

# Heroku Database URL
DATABASE_URL = "postgres://u9t1erngd4qunq:p2d2c51c149348e343682db224b056b6e26a79b06574aa5f7ca4bea27ccf78e54@c5hilnj7pn10vb.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/dceesh1rcupf4o"

def analyze_mcq_issue():
    """Analyze the specific MCQ with ID 99992898."""
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
        query = """
        SELECT id, question_text, correct_answer, options, explanation_sections
        FROM mcq_mcq
        WHERE id = 99992898;
        """
        
        cursor.execute(query)
        result = cursor.fetchone()
        
        if result:
            mcq_id, question_text, correct_answer, options, explanation_sections = result
            
            print(f"\nMCQ Analysis:")
            print(f"ID: {mcq_id}")
            print(f"Question: {question_text}")
            print(f"\nOptions:")
            print(json.dumps(options, indent=2))
            print(f"\nCurrent correct answer: '{correct_answer}'")
            print(f"Type of correct_answer: {type(correct_answer)}")
            print(f"Length of correct_answer: {len(correct_answer) if correct_answer else 0}")
            
            # Check if correct_answer is in options
            if correct_answer in options:
                print(f"✓ Correct answer '{correct_answer}' found in options")
            else:
                print(f"✗ Correct answer '{correct_answer}' NOT found in options")
                print(f"Available option keys: {list(options.keys())}")
            
            # Check for possible data issues
            print(f"\nDetailed correct_answer analysis:")
            print(f"repr(correct_answer): {repr(correct_answer)}")
            print(f"correct_answer == 'A': {correct_answer == 'A'}")
            print(f"correct_answer.strip() == 'A': {correct_answer.strip() == 'A' if correct_answer else False}")
            
            # Check explanation sections
            if explanation_sections and isinstance(explanation_sections, dict):
                option_analysis = explanation_sections.get('option_analysis', '')
                if option_analysis:
                    print(f"\nOption Analysis (first 500 chars):")
                    print(option_analysis[:500])
                    
                    # Look for correct answer in option analysis
                    lines = option_analysis.split('\n')
                    for line in lines:
                        if 'correct' in line.lower() and 'incorrect' not in line.lower():
                            print(f"\nPotential correct answer line:")
                            print(line[:150])
        else:
            print(f"MCQ with ID 99992898 not found")
        
        # Check for similar issues in other MCQs
        print("\n" + "="*50)
        print("Checking for similar issues in other MCQs...")
        
        query = """
        SELECT COUNT(*) 
        FROM mcq_mcq
        WHERE correct_answer IS NULL OR correct_answer = '' OR correct_answer NOT IN ('A', 'B', 'C', 'D');
        """
        
        cursor.execute(query)
        count = cursor.fetchone()[0]
        print(f"MCQs with invalid correct_answer: {count}")
        
        if count > 0:
            # Get some examples
            query = """
            SELECT id, correct_answer, options
            FROM mcq_mcq
            WHERE correct_answer IS NULL OR correct_answer = '' OR correct_answer NOT IN ('A', 'B', 'C', 'D')
            LIMIT 5;
            """
            
            cursor.execute(query)
            examples = cursor.fetchall()
            
            print("\nExamples of MCQs with invalid correct_answer:")
            for mcq_id, correct_answer, options in examples:
                print(f"ID: {mcq_id}, correct_answer: '{correct_answer}' (repr: {repr(correct_answer)}), options keys: {list(options.keys())}")
        
        cursor.close()
        conn.close()
        
    except Exception as e:
        print(f"Database error: {e}")

if __name__ == "__main__":
    print("Analyzing MCQ issue...")
    analyze_mcq_issue()