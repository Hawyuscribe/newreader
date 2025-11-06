#!/usr/bin/env python
"""
Comprehensive fix for all MCQs with incorrect answers by parsing various option analysis formats.
"""

import json
import re
import psycopg2
import urllib.parse
from datetime import datetime
import time

# Heroku Database URL
DATABASE_URL = "postgres://u9t1erngd4qunq:p2d2c51c149348e343682db224b056b6e26a79b06574aa5f7ca4bea27ccf78e54@c5hilnj7pn10vb.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/dceesh1rcupf4o"

def parse_correct_answer_comprehensive(option_analysis):
    """
    Comprehensive parsing of option analysis to find correct answer.
    Handles multiple formatting patterns.
    """
    if not option_analysis:
        return None
    
    # Clean up the text - replace various Unicode dashes with standard dash
    option_analysis = option_analysis.replace('–', '-').replace('—', '-').replace('‐', '-')
    
    # Pattern 1: "Option X: ... - Correct." or "Option X ... - Correct"
    patterns = [
        r'Option ([A-D])[:\s][^-]*[-]\s*Correct',
        r'Option ([A-D])[:\s][^-]*[-]\s*\*?\*?Correct',
        r'Option ([A-D])[:]\s*[^–]*[–]\s*Correct',
        r'Option ([A-D])\s*[-–]\s*Correct',
        r'^\s*Option ([A-D]).*Correct\.',
    ]
    
    for pattern in patterns:
        matches = re.findall(pattern, option_analysis, re.IGNORECASE | re.MULTILINE)
        if matches:
            return matches[0].upper()
    
    # Pattern 2: Look line by line for correct answers
    lines = option_analysis.split('\n')
    
    for i, line in enumerate(lines):
        # Clean the line
        line = line.strip()
        
        # Skip empty lines
        if not line:
            continue
            
        # Check if line mentions an option
        option_match = re.search(r'Option ([A-D])', line, re.IGNORECASE)
        if option_match:
            # Check if this line or the next few lines contain "Correct"
            # but not "Incorrect" or "Partially correct"
            text_to_check = line
            
            # Also check the next 2 lines
            for j in range(1, 3):
                if i + j < len(lines):
                    text_to_check += " " + lines[i + j].strip()
            
            # Check for correct answer indicators
            if (re.search(r'\bCorrect\b', text_to_check, re.IGNORECASE) and 
                not re.search(r'\bIncorrect\b', text_to_check, re.IGNORECASE) and
                not re.search(r'\bPartially\s+correct\b', text_to_check, re.IGNORECASE)):
                return option_match.group(1).upper()
    
    # Pattern 3: Sometimes the format is different - option on one line, verdict on next
    for i in range(len(lines) - 1):
        line = lines[i].strip()
        next_line = lines[i + 1].strip()
        
        option_match = re.search(r'^\s*Option ([A-D])', line, re.IGNORECASE)
        if option_match:
            if (re.search(r'^[-–]\s*Correct', next_line, re.IGNORECASE) or
                re.search(r'^\s*Correct', next_line, re.IGNORECASE)):
                return option_match.group(1).upper()
    
    return None

def fix_all_mcqs():
    """Fix all MCQs with incorrect answers."""
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
        
        # First, get total count of MCQs that need checking
        count_query = """
        SELECT COUNT(*) 
        FROM mcq_mcq
        WHERE explanation_sections IS NOT NULL
        AND (explanation_sections->>'option_analysis') IS NOT NULL;
        """
        
        cursor.execute(count_query)
        total_count = cursor.fetchone()[0]
        print(f"Total MCQs with option analysis to check: {total_count}")
        
        # Process in batches
        batch_size = 1000
        offset = 0
        
        updated_count = 0
        no_correct_found = 0
        already_correct = 0
        error_count = 0
        
        start_time = time.time()
        
        while offset < total_count:
            # Get a batch of MCQs
            query = """
            SELECT id, correct_answer, explanation_sections
            FROM mcq_mcq
            WHERE explanation_sections IS NOT NULL
            AND (explanation_sections->>'option_analysis') IS NOT NULL
            ORDER BY id
            LIMIT %s OFFSET %s;
            """
            
            cursor.execute(query, (batch_size, offset))
            mcqs = cursor.fetchall()
            
            if not mcqs:
                break
            
            # Process this batch
            batch_updates = []
            
            for mcq_id, current_correct, explanation_sections in mcqs:
                try:
                    if isinstance(explanation_sections, dict):
                        option_analysis = explanation_sections.get('option_analysis', '')
                        
                        if option_analysis:
                            # Parse the correct answer
                            parsed_correct = parse_correct_answer_comprehensive(option_analysis)
                            
                            if parsed_correct:
                                if current_correct != parsed_correct:
                                    batch_updates.append((parsed_correct, mcq_id))
                                    updated_count += 1
                                    
                                    # Print first few updates for verification
                                    if updated_count <= 5:
                                        print(f"Will update MCQ {mcq_id}: {current_correct} → {parsed_correct}")
                                else:
                                    already_correct += 1
                            else:
                                no_correct_found += 1
                                
                                # Print first few failures for debugging
                                if no_correct_found <= 3:
                                    print(f"Could not parse MCQ {mcq_id}. Option analysis:")
                                    print(option_analysis[:200] + "...")
                        
                except Exception as e:
                    error_count += 1
                    if error_count <= 3:
                        print(f"Error processing MCQ {mcq_id}: {e}")
            
            # Execute batch updates
            if batch_updates:
                cursor.executemany(
                    "UPDATE mcq_mcq SET correct_answer = %s WHERE id = %s",
                    batch_updates
                )
                conn.commit()
                print(f"Updated {len(batch_updates)} MCQs in this batch")
            
            # Update progress
            offset += batch_size
            elapsed_time = time.time() - start_time
            processed_count = min(offset, total_count)
            progress = (processed_count / total_count) * 100
            
            print(f"Progress: {processed_count}/{total_count} ({progress:.1f}%) - "
                  f"Elapsed: {elapsed_time:.1f}s - "
                  f"Updated: {updated_count} - "
                  f"Already correct: {already_correct}")
        
        # Final summary
        print(f"\nFinal Summary:")
        print(f"Total MCQs processed: {updated_count + already_correct + no_correct_found}")
        print(f"MCQs updated: {updated_count}")
        print(f"MCQs already correct: {already_correct}")
        print(f"MCQs where correct answer not found: {no_correct_found}")
        print(f"MCQs with errors: {error_count}")
        print(f"Total time: {time.time() - start_time:.1f} seconds")
        
        # Close the connection
        cursor.close()
        conn.close()
        
        # Save a log of the updates
        log_data = {
            'timestamp': datetime.now().isoformat(),
            'total_processed': updated_count + already_correct + no_correct_found,
            'updated': updated_count,
            'already_correct': already_correct,
            'not_found': no_correct_found,
            'errors': error_count
        }
        
        with open('heroku_comprehensive_fix_log.json', 'w') as f:
            json.dump(log_data, f, indent=2)
        
        print(f"\nLog saved to heroku_comprehensive_fix_log.json")
        
    except Exception as e:
        print(f"Database error: {e}")

if __name__ == "__main__":
    print("Running comprehensive fix for all MCQ correct answers...")
    fix_all_mcqs()