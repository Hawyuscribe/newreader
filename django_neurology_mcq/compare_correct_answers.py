#!/usr/bin/env python
"""
Script to compare the correct answers in the database with the implied correct answers
from the "Incorrect Options Analysis" section in the explanations.

This script:
1. Extracts all MCQs from the database
2. For each MCQ, checks if it has an explanation with an "Incorrect Options Analysis" section
3. Extracts the options listed in that section
4. Determines which option is missing (implied to be the correct answer)
5. Compares with the database's correct_answer field
6. Reports discrepancies for review and correction
"""

import os
import sys
import re
import json
import django
import logging
from datetime import datetime

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
django.setup()

from mcq.models import MCQ

# Configure logging
log_filename = f"logs/answer_verification_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def extract_incorrect_options(explanation):
    """
    Extract the incorrect options listed in the "Incorrect Options Analysis" section.
    Returns a list of option letters (A, B, C, D, E).
    """
    # Check if explanation exists
    if not explanation:
        return []
    
    # Try to find the "Incorrect Options Analysis" section
    pattern = r'Incorrect Options Analysis.*?(?=<div class="explanation-section">|$)'
    match = re.search(pattern, explanation, re.DOTALL | re.IGNORECASE)
    if not match:
        return []
    
    # Extract the section content
    section = match.group(0)
    
    # Extract option letters (A, B, C, D, E)
    option_pattern = r'([A-E])\.\s+'
    options = re.findall(option_pattern, section)
    
    return options

def get_all_options():
    """Return a list of all possible option letters."""
    return ['A', 'B', 'C', 'D', 'E']

def get_implied_correct_answer(incorrect_options):
    """
    Determine the implied correct answer based on which option is missing
    from the list of incorrect options.
    """
    all_options = get_all_options()
    missing_options = [opt for opt in all_options if opt not in incorrect_options]
    
    # If exactly one option is missing, that's likely the correct answer
    if len(missing_options) == 1:
        return missing_options[0]
    
    # If multiple options are missing or all are present, we can't determine
    return None

def main():
    """Main function to compare correct answers."""
    mcqs = MCQ.objects.all()
    logger.info(f"Found {mcqs.count()} MCQs in the database")
    
    discrepancies = []
    inconsistent_explanations = []
    no_explanations = []
    
    total_checked = 0
    
    for mcq in mcqs:
        if not mcq.explanation:
            no_explanations.append({
                'mcq_id': mcq.id,
                'question_number': mcq.question_number,
                'correct_answer': mcq.correct_answer
            })
            continue
        
        incorrect_options = extract_incorrect_options(mcq.explanation)
        if not incorrect_options:
            inconsistent_explanations.append({
                'mcq_id': mcq.id,
                'question_number': mcq.question_number,
                'correct_answer': mcq.correct_answer
            })
            continue
        
        implied_correct = get_implied_correct_answer(incorrect_options)
        if not implied_correct:
            inconsistent_explanations.append({
                'mcq_id': mcq.id,
                'question_number': mcq.question_number,
                'correct_answer': mcq.correct_answer,
                'incorrect_options': incorrect_options
            })
            continue
        
        total_checked += 1
        
        # Check if the database's correct answer matches the implied correct answer
        if mcq.correct_answer != implied_correct:
            discrepancies.append({
                'mcq_id': mcq.id,
                'question_number': mcq.question_number,
                'subspecialty': mcq.subspecialty,
                'db_correct_answer': mcq.correct_answer,
                'implied_correct_answer': implied_correct,
                'incorrect_options': incorrect_options,
                'options': mcq.get_options_dict()
            })
    
    # Save results to a log file
    results = {
        'total_mcqs': mcqs.count(),
        'total_checked': total_checked,
        'discrepancies_count': len(discrepancies),
        'inconsistent_explanations_count': len(inconsistent_explanations),
        'no_explanations_count': len(no_explanations),
        'discrepancies': discrepancies,
        'inconsistent_explanations': inconsistent_explanations,
        'no_explanations': no_explanations
    }
    
    with open(log_filename, 'w') as f:
        json.dump(results, f, indent=4)
    
    # Print summary
    logger.info(f"Total MCQs: {mcqs.count()}")
    logger.info(f"MCQs checked: {total_checked}")
    logger.info(f"Discrepancies found: {len(discrepancies)}")
    logger.info(f"Inconsistent explanations: {len(inconsistent_explanations)}")
    logger.info(f"No explanations: {len(no_explanations)}")
    logger.info(f"Results saved to {log_filename}")
    
    return results

if __name__ == "__main__":
    results = main()
    
    # If we have discrepancies, prompt for automatic fixing
    if results['discrepancies']:
        print("\nDiscrepancies found between database correct answers and explanation implied answers.")
        print("Would you like to automatically update the database with the implied correct answers? (y/n)")
        response = input().strip().lower()
        
        if response == 'y':
            count = 0
            for disc in results['discrepancies']:
                try:
                    mcq = MCQ.objects.get(id=disc['mcq_id'])
                    old_answer = mcq.correct_answer
                    mcq.correct_answer = disc['implied_correct_answer']
                    mcq.save()
                    count += 1
                    logger.info(f"Updated MCQ {mcq.id}: {old_answer} -> {mcq.correct_answer}")
                except Exception as e:
                    logger.error(f"Error updating MCQ {disc['mcq_id']}: {str(e)}")
            
            print(f"Updated {count} MCQs with implied correct answers.")