#!/usr/bin/env python3
"""
Final verification script to ensure ALL MCQs have correct explanations.
This script uses a more thorough matching algorithm and manual verification options.
"""

import os
import sys
import json
import sqlite3
import re
from difflib import SequenceMatcher
from datetime import datetime

# Path to the database
DB_PATH = "/Users/tariqalmatrudi/NEWreader/django_neurology_mcq/neurology_mcq.db"
# Path to the original explanations
SOURCE_DIR = "/Users/tariqalmatrudi/Documents/MCQs for the board/Classified MCQs/with explanation"

def normalize_text(text):
    """Clean text for better comparison."""
    if not text:
        return ""
    
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', ' ', text)
    # Convert to lowercase
    text = text.lower()
    # Replace punctuation and special chars with spaces
    text = re.sub(r'[^\w\s]', ' ', text)
    # Replace multiple spaces with single space
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

def extract_key_terms(text):
    """Extract key medical terms from text."""
    if not text:
        return []
    
    # Normalize text
    text = normalize_text(text)
    
    # List of important medical terms to look for
    medical_terms = [
        "epilepsy", "seizure", "stroke", "dementia", "alzheimer", "parkinson",
        "multiple sclerosis", "ms", "als", "myasthenia", "myopathy", "neuropathy",
        "migraine", "headache", "vertigo", "ataxia", "dystonia", "tremor", 
        "meningitis", "encephalitis", "tumor", "glioma", "encephalopathy",
        "hemorrhage", "thrombosis", "aneurysm", "syncope", "trauma", "concussion",
        "mri", "eeg", "csf", "antibody", "genetic", "mutation", "cerebral", "spinal",
        "axonal", "myelin", "neuron", "brain", "atrophy", "lesion", "edema"
    ]
    
    # Find terms in the text
    found_terms = []
    for term in medical_terms:
        if term in text:
            found_terms.append(term)
    
    return found_terms

def get_mcqs_from_database():
    """Get all MCQs from the database."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT id, question_number, question_text, correct_answer, explanation, subspecialty
        FROM mcq_mcq
    """)
    
    mcqs = [dict(row) for row in cursor.fetchall()]
    conn.close()
    
    print(f"Retrieved {len(mcqs)} MCQs from database")
    
    # Add key terms extraction
    for mcq in mcqs:
        mcq['question_terms'] = extract_key_terms(mcq['question_text'])
        mcq['explanation_terms'] = extract_key_terms(mcq['explanation'])
    
    return mcqs

def normalize_subspecialty(file_name):
    """
    Convert file name to database subspecialty name format.
    """
    # Map of file names to subspecialty names in the database
    subspecialty_map = {
        "Critical_Care_Neurology": "Critical Care Neurology",
        "Dementia": "Dementia",
        "Epilepsy": "Epilepsy",
        "Headache": "Headache",
        "Movement_Disorders": "Movement Disorders",
        "Neuro_infectious": "Neuro-infectious",
        "Neuro_oncology": "Neuro-oncology",
        "Neuro_otology": "Neuro-otology",
        "Neuroanatomy": "Neuroanatomy",
        "Neurogenetics": "Neurogenetics",
        "Neuroimmunology": "Neuroimmunology",
        "Neuromuscular": "Neuromuscular",
        "Neuroophthalmology": "Neuroophthalmology",
        "Neuropsychiatry": "Neuropsychiatry",
        "Neurotoxicology": "Neurotoxicology",
        "Other_Unclassified": "Other/Unclassified",
        "Pediatric_Neurology": "Pediatric Neurology",
        "Sleep_Neurology": "Sleep Neurology",
        "Vascular_neurology_stroke": "Vascular Neurology/Stroke"
    }
    
    # Remove .json extension if present
    if file_name.endswith('.json'):
        file_name = file_name[:-5]
    
    return subspecialty_map.get(file_name, file_name)

def load_source_mcqs():
    """Load all MCQs from source JSON files."""
    source_mcqs = []
    
    for file_name in os.listdir(SOURCE_DIR):
        if not file_name.endswith('.json'):
            continue
        
        file_path = os.path.join(SOURCE_DIR, file_name)
        subspecialty = normalize_subspecialty(file_name[:-5])  # Remove .json extension
        
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
            
            # Handle different JSON structures
            questions = []
            if isinstance(data, dict) and "questions" in data:
                questions = data["questions"]
            elif isinstance(data, list):
                # Skip metadata if first item has specific keys
                if data and isinstance(data[0], dict) and "source_file" in data[0]:
                    questions = data[1:]
                else:
                    questions = data
            
            print(f"Loaded {len(questions)} questions from {file_name}")
            
            # Process each question
            for q in questions:
                # Skip if no explanation
                if not q.get("explanation"):
                    continue
                
                # Get question text
                question_text = q.get("processed_question", q.get("original_question", ""))
                
                # Skip if no question text
                if not question_text:
                    continue
                
                # Format the explanation
                if isinstance(q["explanation"], dict):
                    explanation_parts = []
                    for section, content in q["explanation"].items():
                        if content:
                            explanation_parts.append(f"{section}: {content}")
                    explanation_text = "\n\n".join(explanation_parts)
                else:
                    explanation_text = q["explanation"]
                
                # Create a source MCQ entry
                source_mcq = {
                    "subspecialty": subspecialty,
                    "question_number": q.get("question_number", ""),
                    "question_text": question_text,
                    "correct_answer": q.get("correct_answer", ""),
                    "explanation": explanation_text,
                    "question_terms": extract_key_terms(question_text),
                    "explanation_terms": extract_key_terms(explanation_text)
                }
                
                source_mcqs.append(source_mcq)
        
        except Exception as e:
            print(f"Error loading {file_name}: {str(e)}")
    
    return source_mcqs

def calculate_term_overlap(terms1, terms2):
    """Calculate the overlap between two sets of terms."""
    if not terms1 or not terms2:
        return 0
    
    common_terms = set(terms1).intersection(set(terms2))
    all_terms = set(terms1).union(set(terms2))
    
    if not all_terms:
        return 0
    
    return len(common_terms) / len(all_terms)

def check_explanation_relevance(mcq):
    """
    Check if the explanation seems relevant to the question.
    Returns a score and list of issues found.
    """
    issues = []
    
    # Calculate overlap between question and explanation terms
    question_terms = mcq['question_terms']
    explanation_terms = mcq['explanation_terms']
    
    term_overlap = calculate_term_overlap(question_terms, explanation_terms)
    
    # Check for key terms in question not in explanation
    if len(question_terms) > 3:
        missing_terms = [term for term in question_terms if term not in explanation_terms]
        if len(missing_terms) > 0.5 * len(question_terms):
            issues.append(f"Explanation missing key terms from question: {', '.join(missing_terms[:5])}")
    
    # Check if explanation is empty or very short
    if not mcq['explanation'] or len(mcq['explanation']) < 100:
        issues.append("Explanation is empty or very short")
    
    # Check if explanation mentions different disease than question
    diseases = ["epilepsy", "seizure", "stroke", "dementia", "alzheimer", "parkinson", 
               "multiple sclerosis", "myasthenia", "migraine", "meningitis", "tumor"]
    
    for disease in diseases:
        if disease in ' '.join(question_terms) and disease not in ' '.join(explanation_terms):
            issues.append(f"Question mentions {disease} but explanation doesn't")
    
    # Calculate final relevance score
    # Weight term overlap heavily but also consider issues found
    relevance_score = term_overlap * 0.8 - 0.1 * len(issues)
    
    return max(0, relevance_score), issues

def find_mismatch_candidates(db_mcqs):
    """Identify MCQs with potentially mismatched explanations."""
    mismatches = []
    
    print("Checking for explanation-question mismatches...")
    
    for i, mcq in enumerate(db_mcqs):
        # Calculate relevance of current explanation to question
        relevance_score, issues = check_explanation_relevance(mcq)
        
        # If relevance is low, flag as potential mismatch
        if relevance_score < 0.3 and issues:
            mismatches.append({
                "id": mcq["id"],
                "subspecialty": mcq["subspecialty"],
                "question_number": mcq["question_number"],
                "question_text": mcq["question_text"],
                "explanation": mcq["explanation"][:150] + "..." if len(mcq["explanation"]) > 150 else mcq["explanation"],
                "issues": issues,
                "relevance_score": relevance_score
            })
        
        # Progress indicator
        if (i + 1) % 500 == 0:
            print(f"Processed {i + 1} MCQs")
    
    print(f"Found {len(mismatches)} potential explanation mismatches")
    
    return mismatches

def find_explanation_for_mismatch(mcq, source_mcqs, match_threshold=0.6):
    """Find potential explanation matches for a mismatched MCQ."""
    matches = []

    # Extract terms if they don't exist
    if "question_terms" not in mcq:
        mcq["question_terms"] = extract_key_terms(mcq["question_text"])

    # Try to find good matches from source explanations
    for source_mcq in source_mcqs:
        # First check if the subspecialties match
        if source_mcq["subspecialty"] != mcq["subspecialty"]:
            continue

        # Try question number match
        if mcq["question_number"] and mcq["question_number"] == source_mcq["question_number"]:
            matches.append({
                "source_mcq": source_mcq,
                "match_reason": "question_number",
                "match_score": 0.95
            })
            continue

        # Try text similarity match
        text_similarity = SequenceMatcher(None,
                                       normalize_text(mcq["question_text"]),
                                       normalize_text(source_mcq["question_text"])).ratio()

        if text_similarity >= match_threshold:
            matches.append({
                "source_mcq": source_mcq,
                "match_reason": "text_similarity",
                "match_score": text_similarity
            })
            continue

        # Try term overlap match
        term_overlap = calculate_term_overlap(mcq["question_terms"], source_mcq["question_terms"])

        if term_overlap >= match_threshold:
            matches.append({
                "source_mcq": source_mcq,
                "match_reason": "term_overlap",
                "match_score": term_overlap
            })

    # Sort matches by score
    matches.sort(key=lambda x: x["match_score"], reverse=True)

    return matches[:5]  # Return top 5 matches

def update_mcq_explanation(mcq_id, explanation, conn):
    """Update the explanation for an MCQ in the database."""
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE mcq_mcq SET explanation = ? WHERE id = ?", (explanation, mcq_id))
        return True, None
    except Exception as e:
        return False, str(e)

def process_mismatches(mismatches, source_mcqs, interactive=False, auto_fix=False):
    """Process mismatched MCQs."""
    if not mismatches:
        print("No mismatches to process")
        return []
    
    results = []
    
    # Connect to the database if we're going to make changes
    conn = None
    if auto_fix:
        conn = sqlite3.connect(DB_PATH)
    
    for i, mismatch in enumerate(mismatches):
        print(f"Processing mismatch {i+1}/{len(mismatches)}: MCQ {mismatch['id']}")
        
        # Find potential explanation matches
        matches = find_explanation_for_mismatch(mismatch, source_mcqs)
        
        result = {
            "id": mismatch["id"],
            "question_number": mismatch["question_number"],
            "subspecialty": mismatch["subspecialty"],
            "question_text": mismatch["question_text"],
            "issues": mismatch["issues"],
            "current_explanation": mismatch["explanation"],
            "potential_matches": matches,
            "action": "none"
        }
        
        if interactive:
            # Print current information
            print("\nQUESTION:")
            print(mismatch["question_text"])
            print("\nCURRENT EXPLANATION:")
            print(mismatch["explanation"])
            print("\nISSUES:")
            for issue in mismatch["issues"]:
                print(f"- {issue}")
            
            # Print potential matches
            if matches:
                print("\nPOTENTIAL MATCHES:")
                for j, match in enumerate(matches):
                    print(f"\n{j+1}. Match score: {match['match_score']:.2f} ({match['match_reason']})")
                    print(f"Question: {match['source_mcq']['question_text'][:150]}...")
                    print(f"Explanation: {match['source_mcq']['explanation'][:150]}...")
            else:
                print("\nNo potential matches found")
            
            # Ask for action
            action = input("\nAction (1-5 to select match, s to skip, m for manual, q to quit): ")
            
            if action == 'q':
                print("Quitting...")
                break
            elif action == 's':
                result["action"] = "skipped"
            elif action == 'm':
                # Manual entry
                print("Enter the explanation (end with a blank line):")
                lines = []
                while True:
                    line = input()
                    if not line:
                        break
                    lines.append(line)
                
                manual_explanation = "\n".join(lines)
                
                if manual_explanation and auto_fix:
                    success, error = update_mcq_explanation(mismatch["id"], manual_explanation, conn)
                    if success:
                        result["action"] = "manual_fix"
                        result["new_explanation"] = manual_explanation
                    else:
                        result["action"] = "error"
                        result["error"] = error
                else:
                    result["action"] = "manual_entry"
                    result["new_explanation"] = manual_explanation
            elif action.isdigit() and 1 <= int(action) <= len(matches):
                # Select a match
                match_index = int(action) - 1
                selected_match = matches[match_index]
                
                if auto_fix:
                    success, error = update_mcq_explanation(
                        mismatch["id"], 
                        selected_match["source_mcq"]["explanation"], 
                        conn
                    )
                    
                    if success:
                        result["action"] = "fixed"
                        result["match_index"] = match_index
                        result["new_explanation"] = selected_match["source_mcq"]["explanation"]
                    else:
                        result["action"] = "error"
                        result["error"] = error
                else:
                    result["action"] = "match_selected"
                    result["match_index"] = match_index
            else:
                print("Invalid action, skipping")
                result["action"] = "skipped"
        
        elif auto_fix and matches and matches[0]["match_score"] >= 0.9:
            # Automatically use the best match if score is very high
            success, error = update_mcq_explanation(
                mismatch["id"], 
                matches[0]["source_mcq"]["explanation"], 
                conn
            )
            
            if success:
                result["action"] = "auto_fixed"
                result["match_reason"] = matches[0]["match_reason"]
                result["match_score"] = matches[0]["match_score"]
            else:
                result["action"] = "error"
                result["error"] = error
        else:
            # Just record the information, no fix
            result["action"] = "needs_review"
        
        results.append(result)
    
    # Commit changes and close connection
    if conn:
        conn.commit()
        conn.close()
    
    return results

def generate_report(mismatches, results):
    """Generate a report of the mismatch analysis."""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    report_file = f"final_mismatch_report_{timestamp}.md"
    
    with open(report_file, 'w') as f:
        f.write("# Final MCQ Explanation Mismatch Report\n\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        # Summary statistics
        action_counts = {}
        for result in results:
            action = result["action"]
            action_counts[action] = action_counts.get(action, 0) + 1
        
        f.write("## Summary\n\n")
        f.write(f"- Total MCQs analyzed: {len(mismatches)}\n")
        
        for action, count in sorted(action_counts.items()):
            f.write(f"- {action}: {count} ({count/len(mismatches)*100:.1f}%)\n")
        
        # Detailed results by subspecialty
        f.write("\n## Results by Subspecialty\n\n")
        
        subspecialties = set(result["subspecialty"] for result in results)
        
        for subspecialty in sorted(subspecialties):
            subspecialty_results = [r for r in results if r["subspecialty"] == subspecialty]
            
            f.write(f"### {subspecialty} ({len(subspecialty_results)} MCQs)\n\n")
            
            # Count by action for this subspecialty
            sub_action_counts = {}
            for result in subspecialty_results:
                action = result["action"]
                sub_action_counts[action] = sub_action_counts.get(action, 0) + 1
            
            for action, count in sorted(sub_action_counts.items()):
                f.write(f"- {action}: {count} ({count/len(subspecialty_results)*100:.1f}%)\n")
            
            f.write("\n")
        
        # MCQs that still need review
        needs_review = [r for r in results if r["action"] in ["needs_review", "skipped"]]
        
        if needs_review:
            f.write("\n## MCQs That Need Review\n\n")
            f.write(f"Total: {len(needs_review)}\n\n")
            
            for i, result in enumerate(needs_review, 1):
                f.write(f"### {i}. MCQ {result['id']} - {result['subspecialty']} - {result['question_number'] or 'No Number'}\n\n")
                
                f.write("**Question:**\n")
                f.write(f"{result['question_text']}\n\n")
                
                f.write("**Current Explanation:**\n")
                f.write(f"{result['current_explanation']}\n\n")
                
                f.write("**Issues:**\n")
                for issue in result["issues"]:
                    f.write(f"- {issue}\n")
                
                if result.get("potential_matches"):
                    f.write("\n**Potential Matches:**\n")
                    for j, match in enumerate(result["potential_matches"], 1):
                        f.write(f"{j}. Match score: {match['match_score']:.2f} ({match['match_reason']})\n")
                        f.write(f"   Question: {match['source_mcq']['question_text'][:150]}...\n")
                
                f.write("\n---\n\n")
        
        # Errors
        errors = [r for r in results if r["action"] == "error"]
        
        if errors:
            f.write("\n## Errors\n\n")
            f.write(f"Total: {len(errors)}\n\n")
            
            for i, result in enumerate(errors, 1):
                f.write(f"### {i}. MCQ {result['id']} - {result['subspecialty']}\n\n")
                f.write(f"Error: {result.get('error', 'Unknown error')}\n\n")
                f.write("---\n\n")
    
    print(f"Report written to {report_file}")
    return report_file

def main():
    """Main function."""
    # Parse command line arguments
    import argparse
    parser = argparse.ArgumentParser(
        description="Final verification script to ensure ALL MCQs have correct explanations."
    )
    parser.add_argument(
        "--interactive", "-i", 
        action="store_true", 
        help="Run in interactive mode to manually review mismatches"
    )
    parser.add_argument(
        "--auto-fix", "-a", 
        action="store_true", 
        help="Automatically fix high-confidence mismatches"
    )
    parser.add_argument(
        "--limit", "-l", 
        type=int, 
        default=None, 
        help="Limit the number of mismatches to process"
    )
    
    args = parser.parse_args()
    
    # Load data
    print("Loading MCQs from database...")
    db_mcqs = get_mcqs_from_database()
    
    print("Finding potential explanation mismatches...")
    mismatches = find_mismatch_candidates(db_mcqs)
    
    # Limit number of mismatches if requested
    if args.limit and len(mismatches) > args.limit:
        print(f"Limiting to {args.limit} mismatches (from {len(mismatches)} total)")
        mismatches = mismatches[:args.limit]
    
    if not mismatches:
        print("No mismatches found!")
        return 0
    
    # Load source MCQs if needed
    if args.interactive or args.auto_fix:
        print("Loading MCQs from source files for matching...")
        source_mcqs = load_source_mcqs()
        
        print("Processing mismatches...")
        results = process_mismatches(
            mismatches, 
            source_mcqs, 
            interactive=args.interactive, 
            auto_fix=args.auto_fix
        )
    else:
        # Just use mismatches for the report
        results = [{
            "id": m["id"],
            "question_number": m["question_number"],
            "subspecialty": m["subspecialty"],
            "question_text": m["question_text"],
            "current_explanation": m["explanation"],
            "issues": m["issues"],
            "action": "needs_review",
            "potential_matches": []
        } for m in mismatches]
    
    # Generate the report
    generate_report(mismatches, results)
    
    return 0

if __name__ == "__main__":
    sys.exit(main())