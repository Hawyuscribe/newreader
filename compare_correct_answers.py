#!/usr/bin/env python3
"""
Script to compare the stored correct answer for each MCQ with the deduced correct answer
from explanations. The deduced answer is the one option not mentioned as incorrect in the
explanation.
"""

import os
import sys
import sqlite3
import re
import json
from datetime import datetime
import time

# Database path
DB_PATH = "/Users/tariqalmatrudi/NEWreader/django_neurology_mcq/neurology_mcq.db"

# Regular expressions for finding options in explanations
OPTION_A_PATTERN = r"(?:option|choice|answer)(?:\s+|\s*[:-]\s*)A\b|(?:^|\W)A(?:\s+|\s*[:-]\s*)(?:is|was)(?:\s+incorrect|\\s+wrong|\\s+not correct)"
OPTION_B_PATTERN = r"(?:option|choice|answer)(?:\s+|\s*[:-]\s*)B\b|(?:^|\W)B(?:\s+|\s*[:-]\s*)(?:is|was)(?:\s+incorrect|\\s+wrong|\\s+not correct)"
OPTION_C_PATTERN = r"(?:option|choice|answer)(?:\s+|\s*[:-]\s*)C\b|(?:^|\W)C(?:\s+|\s*[:-]\s*)(?:is|was)(?:\s+incorrect|\\s+wrong|\\s+not correct)"
OPTION_D_PATTERN = r"(?:option|choice|answer)(?:\s+|\s*[:-]\s*)D\b|(?:^|\W)D(?:\s+|\s*[:-]\s*)(?:is|was)(?:\s+incorrect|\\s+wrong|\\s+not correct)"

def get_mcqs_from_database():
    """Get all MCQs from the database."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT id, question_number, question_text, correct_answer, explanation, 
               option_a, option_b, option_c, option_d
        FROM mcq_mcq
    """)
    
    mcqs = []
    for row in cursor.fetchall():
        mcq = dict(row)
        mcqs.append(mcq)
    
    conn.close()
    
    return mcqs

def deduce_correct_answer(explanation):
    """
    Analyze the explanation to deduce the correct answer.
    The correct answer is the one not mentioned as incorrect in the explanation.
    """
    # Check for each option mentioned as incorrect
    a_incorrect = bool(re.search(OPTION_A_PATTERN, explanation, re.IGNORECASE))
    b_incorrect = bool(re.search(OPTION_B_PATTERN, explanation, re.IGNORECASE))
    c_incorrect = bool(re.search(OPTION_C_PATTERN, explanation, re.IGNORECASE))
    d_incorrect = bool(re.search(OPTION_D_PATTERN, explanation, re.IGNORECASE))
    
    # Count how many options are identified as incorrect
    incorrect_count = sum([a_incorrect, b_incorrect, c_incorrect, d_incorrect])
    
    # Only deduce if exactly 3 options are mentioned as incorrect
    if incorrect_count == 3:
        if not a_incorrect:
            return "A"
        if not b_incorrect:
            return "B"
        if not c_incorrect:
            return "C"
        if not d_incorrect:
            return "D"
    
    return None  # Cannot deduce with confidence

def analyze_explanations(mcqs):
    """
    Analyze all MCQ explanations to identify discrepancies between
    stored correct answers and deduced correct answers.
    """
    results = {
        "total_mcqs": len(mcqs),
        "analyzed": 0,
        "matched": 0,
        "mismatched": 0,
        "inconclusive": 0,
        "mismatches": []
    }
    
    for mcq in mcqs:
        results["analyzed"] += 1
        
        # Get stored correct answer
        stored_answer = mcq["correct_answer"]
        
        # Deduce correct answer from explanation
        deduced_answer = deduce_correct_answer(mcq["explanation"])
        
        if deduced_answer is None:
            results["inconclusive"] += 1
            continue
        
        if stored_answer == deduced_answer:
            results["matched"] += 1
        else:
            results["mismatched"] += 1
            results["mismatches"].append({
                "id": mcq["id"],
                "question_number": mcq["question_number"],
                "question_text": mcq["question_text"][:100] + "..." if len(mcq["question_text"]) > 100 else mcq["question_text"],
                "stored_answer": stored_answer,
                "deduced_answer": deduced_answer,
                "option_a": mcq["option_a"][:50] + "..." if len(mcq["option_a"]) > 50 else mcq["option_a"],
                "option_b": mcq["option_b"][:50] + "..." if len(mcq["option_b"]) > 50 else mcq["option_b"],
                "option_c": mcq["option_c"][:50] + "..." if len(mcq["option_c"]) > 50 else mcq["option_c"],
                "option_d": mcq["option_d"][:50] + "..." if len(mcq["option_d"]) > 50 else mcq["option_d"]
            })
        
        # Print progress every 100 MCQs
        if results["analyzed"] % 100 == 0:
            print(f"Analyzed {results['analyzed']} of {results['total_mcqs']} MCQs...")
    
    return results

def update_correct_answers(mismatches):
    """Update the correct answers for mismatched MCQs in the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    updated_count = 0
    errors = []
    
    for mismatch in mismatches:
        try:
            cursor.execute(
                "UPDATE mcq_mcq SET correct_answer = ? WHERE id = ?",
                (mismatch["deduced_answer"], mismatch["id"])
            )
            updated_count += 1
        except Exception as e:
            errors.append({
                "id": mismatch["id"],
                "error": str(e)
            })
    
    conn.commit()
    conn.close()
    
    return {
        "updated": updated_count,
        "errors": errors
    }

def save_results(results, update_stats=None):
    """Save analysis results to files."""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    # Save detailed JSON report
    json_filename = f"answer_verification_{timestamp}.json"
    with open(json_filename, 'w') as f:
        json.dump(results, f, indent=2)
    
    # Save a more readable text report
    report_filename = f"answer_mismatch_report_{timestamp}.md"
    with open(report_filename, 'w') as f:
        f.write("# MCQ Answer Verification Report\n\n")
        f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        f.write("## Summary\n\n")
        f.write(f"- Total MCQs analyzed: {results['total_mcqs']}\n")
        f.write(f"- MCQs with matching answers: {results['matched']} ({results['matched']/results['total_mcqs']*100:.1f}%)\n")
        f.write(f"- MCQs with mismatched answers: {results['mismatched']} ({results['mismatched']/results['total_mcqs']*100:.1f}%)\n")
        f.write(f"- MCQs with inconclusive analysis: {results['inconclusive']} ({results['inconclusive']/results['total_mcqs']*100:.1f}%)\n")
        
        if update_stats:
            f.write("\n## Update Results\n\n")
            f.write(f"- MCQs updated: {update_stats['updated']}\n")
            f.write(f"- Errors encountered: {len(update_stats['errors'])}\n")
        
        if results["mismatched"] > 0:
            f.write("\n## Mismatched MCQs\n\n")
            for i, mismatch in enumerate(results["mismatches"], 1):
                f.write(f"### {i}. MCQ ID: {mismatch['id']} (Question {mismatch['question_number']})\n\n")
                f.write(f"**Question:** {mismatch['question_text']}\n\n")
                f.write(f"**Option A:** {mismatch['option_a']}\n\n")
                f.write(f"**Option B:** {mismatch['option_b']}\n\n")
                f.write(f"**Option C:** {mismatch['option_c']}\n\n")
                f.write(f"**Option D:** {mismatch['option_d']}\n\n")
                f.write(f"**Stored correct answer:** {mismatch['stored_answer']}\n\n")
                f.write(f"**Deduced correct answer:** {mismatch['deduced_answer']}\n\n")
                f.write("---\n\n")
    
    print(f"Detailed results saved to: {json_filename}")
    print(f"Report saved to: {report_filename}")
    
    return json_filename, report_filename

def main():
    print("Comparing stored correct answers with deduced answers from explanations...")
    print("Loading MCQs from database...")
    mcqs = get_mcqs_from_database()
    print(f"Loaded {len(mcqs)} MCQs")
    
    print("Analyzing explanations to deduce correct answers...")
    results = analyze_explanations(mcqs)
    
    print("\nAnalysis complete:")
    print(f"Total MCQs: {results['total_mcqs']}")
    print(f"MCQs with matching answers: {results['matched']} ({results['matched']/results['total_mcqs']*100:.1f}%)")
    print(f"MCQs with mismatched answers: {results['mismatched']} ({results['mismatched']/results['total_mcqs']*100:.1f}%)")
    print(f"MCQs with inconclusive analysis: {results['inconclusive']} ({results['inconclusive']/results['total_mcqs']*100:.1f}%)")
    
    # Save results before any updates
    json_file, report_file = save_results(results)
    
    if results["mismatched"] > 0:
        update_choice = input(f"\nDo you want to update {results['mismatched']} MCQs with the deduced correct answers? (y/n): ")
        if update_choice.lower() == 'y':
            print("Updating mismatched MCQs with deduced correct answers...")
            update_stats = update_correct_answers(results["mismatches"])
            
            print(f"Updated {update_stats['updated']} MCQs")
            if len(update_stats['errors']) > 0:
                print(f"Encountered {len(update_stats['errors'])} errors during update")
            
            # Save updated results
            save_results(results, update_stats)
            
            print("Update complete!")
        else:
            print("No changes made to the database.")
    else:
        print("No mismatches found. Database is already correct.")
    
    # Create a backup of the answers before any changes
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_filename = f"correct_answers_backup_{timestamp}.json"
    
    correct_answers = []
    for mcq in mcqs:
        correct_answers.append({
            "id": mcq["id"],
            "question_number": mcq["question_number"],
            "correct_answer": mcq["correct_answer"]
        })
    
    with open(backup_filename, 'w') as f:
        json.dump(correct_answers, f, indent=2)
    
    print(f"Backup of original correct answers saved to: {backup_filename}")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())