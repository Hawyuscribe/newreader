#!/usr/bin/env python
"""
Analyze why the resource allocation MCQ was marked incorrectly and fix the issue.
"""

import json
import re
import psycopg2
import urllib.parse

# Heroku Database URL
DATABASE_URL = "postgres://u9t1erngd4qunq:p2d2c51c149348e343682db224b056b6e26a79b06574aa5f7ca4bea27ccf78e54@c5hilnj7pn10vb.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/dceesh1rcupf4o"

def analyze_mcq():
    """Analyze the specific MCQ to understand why it was parsed incorrectly."""
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
        
        # Find the resource allocation MCQ
        query = """
        SELECT id, question_text, correct_answer, options, explanation_sections
        FROM mcq_mcq
        WHERE question_text LIKE '%resources allocation%children hospital%'
        LIMIT 1;
        """
        
        cursor.execute(query)
        result = cursor.fetchone()
        
        if result:
            mcq_id, question_text, correct_answer, options, explanation_sections = result
            
            print(f"\nFound MCQ:")
            print(f"ID: {mcq_id}")
            print(f"Question: {question_text}")
            print(f"Current correct answer: {correct_answer}")
            print(f"Options: {json.dumps(options, indent=2)}")
            
            if explanation_sections and isinstance(explanation_sections, dict):
                option_analysis = explanation_sections.get('option_analysis', '')
                if option_analysis:
                    print(f"\nOption Analysis (first 500 chars):")
                    print(option_analysis[:500])
                    
                    # Test different patterns to see why it's not catching it
                    print("\n--- Testing different patterns ---")
                    
                    # Pattern 1: Look for explicit statement
                    if "This is the correct answer" in option_analysis:
                        lines = option_analysis.split('\n')
                        for i, line in enumerate(lines):
                            if "This is the correct answer" in line:
                                # Find which option this refers to
                                for j in range(max(0, i-3), i):
                                    if j < len(lines):
                                        prev_line = lines[j]
                                        option_match = re.search(r'Option ([A-D])', prev_line, re.IGNORECASE)
                                        if option_match:
                                            print(f"Pattern 1: Found correct answer: {option_match.group(1)}")
                                            print(f"Context: {prev_line[:100]}")
                                            break
                    
                    # Pattern 2: Look for ": This is the correct answer"
                    pattern2 = r'Option ([A-D])[:\s\(].*:\s*This is the correct answer'
                    matches = re.findall(pattern2, option_analysis, re.IGNORECASE | re.DOTALL)
                    if matches:
                        print(f"Pattern 2: Found: {matches}")
                    
                    # Pattern 3: Check line by line
                    lines = option_analysis.split('\n')
                    for i, line in enumerate(lines):
                        if re.search(r'Option C', line, re.IGNORECASE):
                            # Check this line and next few lines
                            context = line
                            for j in range(1, 4):
                                if i + j < len(lines):
                                    context += " " + lines[i + j]
                            
                            if "correct answer" in context.lower():
                                print(f"\nPattern 3: Option C context:")
                                print(context[:200])
                    
                    # Pattern 4: Look for the discriminating feature
                    if "making Option C the best choice" in option_analysis:
                        print("\nPattern 4: Found 'making Option C the best choice'")
                else:
                    print("No option analysis found")
            else:
                print("No explanation sections found")
        else:
            print("MCQ not found")
        
        # Close the connection
        cursor.close()
        conn.close()
        
    except Exception as e:
        print(f"Database error: {e}")

if __name__ == "__main__":
    print("Analyzing resource allocation MCQ...")
    analyze_mcq()