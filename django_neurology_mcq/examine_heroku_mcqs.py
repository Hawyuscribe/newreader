#!/usr/bin/env python
"""
Script to examine MCQs in the Heroku database to better understand their structure.
"""

import psycopg2
import urllib.parse

# Heroku Database URL
DATABASE_URL = "postgres://u9t1erngd4qunq:p2d2c51c149348e343682db224b056b6e26a79b06574aa5f7ca4bea27ccf78e54@c5hilnj7pn10vb.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/dceesh1rcupf4o"

def main():
    print("Connecting to PostgreSQL database...")
    
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
    
    # Create a cursor
    cursor = conn.cursor()
    
    # Get total count of MCQs
    cursor.execute("SELECT COUNT(*) FROM mcq_mcq")
    total_count = cursor.fetchone()[0]
    print(f"Total MCQs in Heroku database: {total_count}")
    
    # Get MCQs with explanations that have "Conceptual Framework"
    cursor.execute("SELECT COUNT(*) FROM mcq_mcq WHERE explanation LIKE '%Conceptual Framework%'")
    conceptual_count = cursor.fetchone()[0]
    print(f"MCQs with 'Conceptual Framework' in explanation: {conceptual_count}")
    
    # Get MCQs with "Classification Reason" in explanation
    cursor.execute("SELECT COUNT(*) FROM mcq_mcq WHERE explanation LIKE '%Classification Reason%'")
    classification_count = cursor.fetchone()[0]
    print(f"MCQs with 'Classification Reason' in explanation: {classification_count}")
    
    # Get MCQs with no explanation
    cursor.execute("SELECT COUNT(*) FROM mcq_mcq WHERE explanation IS NULL OR explanation = ''")
    no_explanation_count = cursor.fetchone()[0]
    print(f"MCQs with no explanation: {no_explanation_count}")
    
    # Sample some MCQs to understand the structure better
    print("\nSampling MCQs for analysis:")
    
    # Sample MCQ with explanation
    cursor.execute("SELECT id, question_number, subspecialty, explanation FROM mcq_mcq WHERE explanation IS NOT NULL AND explanation != '' LIMIT 1")
    sample = cursor.fetchone()
    
    if sample:
        mcq_id, question_number, subspecialty, explanation = sample
        print(f"\nSample MCQ with explanation:")
        print(f"ID: {mcq_id}")
        print(f"Question Number: {question_number}")
        print(f"Subspecialty: {subspecialty}")
        print(f"Explanation (first 100 chars): {explanation[:100] if explanation else ''}")
    
    # Sample MCQ with "Classification Reason"
    cursor.execute("SELECT id, question_number, subspecialty, explanation FROM mcq_mcq WHERE explanation LIKE '%Classification Reason%' LIMIT 1")
    sample = cursor.fetchone()
    
    if sample:
        mcq_id, question_number, subspecialty, explanation = sample
        print(f"\nSample MCQ with 'Classification Reason':")
        print(f"ID: {mcq_id}")
        print(f"Question Number: {question_number}")
        print(f"Subspecialty: {subspecialty}")
        print(f"Explanation (first 100 chars): {explanation[:100] if explanation else ''}")
    
    # Get the range of IDs in the database
    cursor.execute("SELECT MIN(id), MAX(id) FROM mcq_mcq")
    min_id, max_id = cursor.fetchone()
    print(f"\nID range in Heroku database: {min_id} to {max_id}")
    
    # Get range of IDs for question numbers
    cursor.execute("SELECT MIN(question_number), MAX(question_number) FROM mcq_mcq WHERE question_number IS NOT NULL")
    min_qnum, max_qnum = cursor.fetchone()
    print(f"Question number range in Heroku database: {min_qnum} to {max_qnum}")
    
    # Close the connection
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()