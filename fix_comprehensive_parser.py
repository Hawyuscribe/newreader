#!/usr/bin/env python
"""
Fix MCQs with more comprehensive parsing patterns for option analysis.
"""

import json
import re
import psycopg2
import urllib.parse
from datetime import datetime
import time

# Heroku Database URL
DATABASE_URL = "postgres://u9t1erngd4qunq:p2d2c51c149348e343682db224b056b6e26a79b06574aa5f7ca4bea27ccf78e54@c5hilnj7pn10vb.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/dceesh1rcupf4o"

def parse_correct_answer_advanced(option_analysis):
    """
    Advanced parsing of option analysis to find correct answer.
    Handles multiple formatting patterns including:
    - "This is the correct answer"
    - "making Option X the best choice"
    - Various bullet points and formatting
    """
    if not option_analysis:
        return None
    
    # Clean up the text - replace various Unicode characters
    option_analysis = option_analysis.replace('–', '-').replace('—', '-').replace('‐', '-')
    option_analysis = option_analysis.replace('"', '"').replace('"', '"')
    option_analysis = option_analysis.replace(''', "'").replace(''', "'")
    
    # Keep track of which option is mentioned as correct
    correct_option = None
    
    # Method 1: Look for explicit "This is the correct answer"
    lines = option_analysis.split('\n')
    for i, line in enumerate(lines):
        if "this is the correct answer" in line.lower():
            # Look backwards to find which option this refers to
            for j in range(i, max(-1, i-5), -1):
                if j < len(lines):
                    prev_line = lines[j]
                    option_match = re.search(r'Option ([A-D])', prev_line, re.IGNORECASE)
                    if option_match:
                        correct_option = option_match.group(1).upper()
                        break
            if correct_option:
                return correct_option
    
    # Method 2: Look for "making Option X the best choice"
    pattern_best = r'making Option ([A-D]) the (?:best|correct) choice'
    matches = re.findall(pattern_best, option_analysis, re.IGNORECASE)
    if matches:
        return matches[0].upper()
    
    # Method 3: Look for "Option X is (the) correct"
    pattern_is_correct = r'Option ([A-D])[:\s\)][^\.]*is (?:the )?correct'
    matches = re.findall(pattern_is_correct, option_analysis, re.IGNORECASE)
    if matches:
        return matches[0].upper()
    
    # Method 4: Look for bullet points or dashes followed by "Correct"
    for line in lines:
        # Pattern: "- Option X ... - Correct"
        if re.search(r'^[-•*]\s*Option ([A-D])', line, re.IGNORECASE):
            if re.search(r'[-–]\s*Correct[^\w]', line, re.IGNORECASE):
                option_match = re.search(r'Option ([A-D])', line, re.IGNORECASE)
                if option_match:
                    return option_match.group(1).upper()
    
    # Method 5: Look for "Option X: ... - Correct"
    pattern_correct = r'Option ([A-D])[:\s\(][^-]*[-–]\s*Correct[^\w]'
    matches = re.findall(pattern_correct, option_analysis, re.IGNORECASE | re.MULTILINE)
    if matches:
        return matches[0].upper()
    
    # Method 6: Check if any line has both Option X and "Correct" but not "Incorrect"
    for line in lines:
        if 'Correct' in line and not ('Incorrect' in line or 'incorrect' in line):
            option_match = re.search(r'Option ([A-D])', line, re.IGNORECASE)
            if option_match:
                # Make sure this line is actually about this option being correct
                if not re.search(r'Option [A-D].*(?:In)?correct', line, re.IGNORECASE):
                    return option_match.group(1).upper()
    
    # Method 7: Look for parenthetical statements
    pattern_paren = r'Option ([A-D]) \([^)]*\):\s*Correct'
    matches = re.findall(pattern_paren, option_analysis, re.IGNORECASE)
    if matches:
        return matches[0].upper()
    
    # Method 8: Sometimes correct answer is stated differently
    # "The correct answer is Option X"
    pattern_answer_is = r'(?:The )?correct answer is Option ([A-D])'
    matches = re.findall(pattern_answer_is, option_analysis, re.IGNORECASE)
    if matches:
        return matches[0].upper()
    
    return None

def fix_mcqs_comprehensive():
    """Fix all MCQs using the advanced parser."""
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
        
        # First, fix the specific resource allocation MCQ
        print("\nFixing the resource allocation MCQ...")
        query = """
        SELECT id, correct_answer, explanation_sections
        FROM mcq_mcq
        WHERE id = 99992894;
        """
        
        cursor.execute(query)
        result = cursor.fetchone()
        
        if result:
            mcq_id, current_correct, explanation_sections = result
            if isinstance(explanation_sections, dict):
                option_analysis = explanation_sections.get('option_analysis', '')
                if option_analysis:
                    parsed_correct = parse_correct_answer_advanced(option_analysis)
                    if parsed_correct and parsed_correct != current_correct:
                        update_query = "UPDATE mcq_mcq SET correct_answer = %s WHERE id = %s"
                        cursor.execute(update_query, (parsed_correct, mcq_id))
                        conn.commit()
                        print(f"Fixed resource allocation MCQ: {current_correct} → {parsed_correct}")
        
        # Now process all MCQs with the advanced parser
        print("\nProcessing all MCQs with advanced parser...")
        
        # Get total count
        count_query = """
        SELECT COUNT(*) 
        FROM mcq_mcq
        WHERE explanation_sections IS NOT NULL
        AND (explanation_sections->>'option_analysis') IS NOT NULL;
        """
        
        cursor.execute(count_query)
        total_count = cursor.fetchone()[0]
        print(f"Total MCQs to check: {total_count}")
        
        # Process in batches
        batch_size = 1000
        offset = 0
        
        updated_count = 0
        no_correct_found = 0
        already_correct = 0
        
        start_time = time.time()
        
        while offset < total_count:
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
            
            batch_updates = []
            
            for mcq_id, current_correct, explanation_sections in mcqs:
                try:
                    if isinstance(explanation_sections, dict):
                        option_analysis = explanation_sections.get('option_analysis', '')
                        
                        if option_analysis:
                            parsed_correct = parse_correct_answer_advanced(option_analysis)
                            
                            if parsed_correct:
                                if current_correct != parsed_correct:
                                    batch_updates.append((parsed_correct, mcq_id))
                                    updated_count += 1
                                    
                                    # Print some examples
                                    if updated_count <= 10:
                                        print(f"Will update MCQ {mcq_id}: {current_correct} → {parsed_correct}")
                                else:
                                    already_correct += 1
                            else:
                                no_correct_found += 1
                        
                except Exception as e:
                    print(f"Error processing MCQ {mcq_id}: {e}")
            
            # Execute batch updates
            if batch_updates:
                cursor.executemany(
                    "UPDATE mcq_mcq SET correct_answer = %s WHERE id = %s",
                    batch_updates
                )
                conn.commit()
                print(f"Updated {len(batch_updates)} MCQs in this batch")
            
            offset += batch_size
            elapsed_time = time.time() - start_time
            processed_count = min(offset, total_count)
            progress = (processed_count / total_count) * 100
            
            print(f"Progress: {processed_count}/{total_count} ({progress:.1f}%) - "
                  f"Updated: {updated_count}")
        
        # Final summary
        print(f"\nFinal Summary:")
        print(f"Total MCQs processed: {total_count}")
        print(f"MCQs updated: {updated_count}")
        print(f"MCQs already correct: {already_correct}")
        print(f"MCQs where correct answer not found: {no_correct_found}")
        print(f"Total time: {time.time() - start_time:.1f} seconds")
        
        cursor.close()
        conn.close()
        
        # Save log
        log_data = {
            'timestamp': datetime.now().isoformat(),
            'total_processed': total_count,
            'updated': updated_count,
            'already_correct': already_correct,
            'not_found': no_correct_found
        }
        
        with open('advanced_parser_fix_log.json', 'w') as f:
            json.dump(log_data, f, indent=2)
        
    except Exception as e:
        print(f"Database error: {e}")

if __name__ == "__main__":
    print("Running comprehensive fix with advanced parser...")
    fix_mcqs_comprehensive()