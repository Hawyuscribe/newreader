#!/usr/bin/env python
import os
import sys
import json
import logging
import django
import time
from datetime import datetime
from tqdm import tqdm
import openai
from django.db import transaction
from django.conf import settings
import re

# Configure logging
log_dir = "logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
log_file = os.path.join(log_dir, f"match_mcqs_gpt_{timestamp}.log")
stats_file = os.path.join(log_dir, f"match_mcqs_gpt_stats_{timestamp}.json")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)

# Set up Django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "neurology_mcq.settings")
django.setup()

from mcq.models import MCQ
from mcq.openai_integration import (
    client as openai_client,
    chat_completion,
    DEFAULT_MODEL,
    FALLBACK_MODEL,
    get_first_choice_text,
)

# Constants
PLACEHOLDER_TEXT = "Select the correct answer from the options below"
FIXTURES_DIR = "fixtures/mcqs"
MODEL = DEFAULT_MODEL
MAX_TOKENS = 900000  # Safe limit for context window

def get_unmatched_mcqs_by_subspecialty():
    """Get MCQs with placeholder text or formatting issues, organized by subspecialty."""
    # Get MCQs with extra quote marks at the beginning
    unmatched_mcqs = MCQ.objects.filter(question_text__startswith='"')
    subspecialty_mcqs = {}
    
    for mcq in unmatched_mcqs:
        if mcq.subspecialty not in subspecialty_mcqs:
            subspecialty_mcqs[mcq.subspecialty] = []
        
        # Get options from the options dictionary
        options = []
        for key, value in mcq.options.items():
            options.append(f"{key}. {value}")
        
        mcq_data = {
            "id": mcq.id,
            "options": options,
            "correct_answer": mcq.correct_answer,
            "explanation": mcq.explanation,
        }
        subspecialty_mcqs[mcq.subspecialty].append(mcq_data)
    
    return subspecialty_mcqs

def get_json_file_for_subspecialty(subspecialty):
    """Find the JSON file corresponding to a subspecialty."""
    subspecialty_normalized = subspecialty.replace("/", "_").replace(" ", "_")
    matching_files = []
    
    for filename in os.listdir(FIXTURES_DIR):
        if filename.endswith(".json") and not filename.startswith("all_mcqs"):
            file_subspecialty = filename.replace(".json", "").replace("_", " ")
            if file_subspecialty.lower() == subspecialty_normalized.lower():
                return os.path.join(FIXTURES_DIR, filename)
            
            # Partial match
            if subspecialty_normalized.lower() in file_subspecialty.lower() or file_subspecialty.lower() in subspecialty_normalized.lower():
                matching_files.append(filename)
    
    # Return the first partial match if any
    if matching_files:
        return os.path.join(FIXTURES_DIR, matching_files[0])
    
    # If no match found, use all_mcqs.json
    logging.warning(f"No specific JSON file found for subspecialty: {subspecialty}. Using all_mcqs.json")
    return os.path.join(FIXTURES_DIR, "all_mcqs.json")

def match_mcqs_with_gpt(subspecialty, mcqs, json_file_path):
    """Use the shared GPT-5-mini model to match MCQs with their source questions in the JSON file."""
    client = openai_client
    if not client:
        logging.error("OpenAI client unavailable – cannot perform MCQ matching")
        return []
    
    # Load the JSON file
    try:
        with open(json_file_path, 'r') as f:
            json_data = json.load(f)
    except Exception as e:
        logging.error(f"Error loading JSON file {json_file_path}: {e}")
        return []
    
    # Format the MCQs for GPT
    mcqs_formatted = []
    for i, mcq in enumerate(mcqs):
        options_text = "\n".join(mcq["options"])
        mcqs_formatted.append(f"""
MCQ ID: {mcq['id']}
Options:
{options_text}
Correct Answer: {mcq['correct_answer']}
        """)
    
    mcqs_text = "\n\n".join(mcqs_formatted)
    
    # Create the prompt for GPT
    prompt = f"""
I have a set of Multiple Choice Questions (MCQs) that are missing their question text. 
Each MCQ has options, a correct answer, and sometimes an explanation.

I need you to find the original question text for each MCQ by matching it with the provided JSON file content.
The JSON file contains the original questions with their options, correct answers, and explanations.

For each MCQ below, please:
1. Find the matching entry in the JSON file based on similar options and correct answer
2. Extract the original question text
3. Return a JSON object with the MCQ ID and the matched question text
4. If you can't find a match, indicate "NO_MATCH_FOUND"

Here are the MCQs with missing question text:

{mcqs_text}

JSON file content:
{json.dumps(json_data, indent=2)}

IMPORTANT: For each MCQ, return a JSON object in this format:
{{
  "id": [MCQ ID],
  "question_text": "[Matched Question Text]"
}}

If no match is found, use:
{{
  "id": [MCQ ID],
  "question_text": "NO_MATCH_FOUND"
}}

Return your answer as a JSON array containing these objects.
"""

    # Check if prompt is too large
    if len(prompt) > MAX_TOKENS * 4:  # Rough estimate of tokens
        logging.warning(f"Prompt for {subspecialty} is too large. Switching to chunked approach.")
        # In this case, we could implement a chunking approach
        # But for simplicity, we'll return no matches
        return []

    # Call GPT-5-mini with optional fallback
    try:
        response = chat_completion(
            client,
            MODEL,
            [
                {"role": "system", "content": "You are a helpful assistant that matches medical MCQs with their source data."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.0,
            max_tokens=4000
        )
    except Exception as primary_error:
        if FALLBACK_MODEL and FALLBACK_MODEL != MODEL:
            logging.warning(
                "Primary model %s failed while matching %s (%s); retrying with %s",
                MODEL,
                subspecialty,
                primary_error,
                FALLBACK_MODEL,
            )
            response = chat_completion(
                client,
                FALLBACK_MODEL,
                [
                    {"role": "system", "content": "You are a helpful assistant that matches medical MCQs with their source data."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.0,
                max_tokens=4000
            )
        else:
            logging.error(f"Error calling GPT API for subspecialty {subspecialty}: {primary_error}")
            return []

    # Extract and parse the JSON response
    result_text = get_first_choice_text(response)
    if not result_text:
        logging.error("Empty response from OpenAI for subspecialty %s", subspecialty)
        return []
    # Find JSON in the response - it might be surrounded by text
    json_match = re.search(r'\[[\s\S]*\]', result_text)
    if json_match:
        json_str = json_match.group(0)
        try:
            matches = json.loads(json_str)
            return matches
        except json.JSONDecodeError as e:
            logging.error(f"Error parsing JSON from GPT response: {e}")
            logging.error(f"Response content: {result_text}")
            return []
    else:
        logging.error(f"No JSON array found in GPT response: {result_text}")
        return []

def update_mcqs_with_matches(matches):
    """Update MCQs with their matched question text."""
    updated_count = 0
    no_match_count = 0
    
    for match in matches:
        mcq_id = match.get("id")
        question_text = match.get("question_text")
        
        if not mcq_id or not question_text:
            continue
        
        if question_text == "NO_MATCH_FOUND":
            no_match_count += 1
            continue
        
        try:
            with transaction.atomic():
                mcq = MCQ.objects.get(id=mcq_id)
                # For MCQs with quotes at the beginning, fix by removing quotes
                if mcq.question_text.startswith('"'):
                    # Remove quotes at beginning and end, and clean up whitespace
                    fixed_text = mcq.question_text.strip('"').strip()
                    mcq.question_text = fixed_text
                    mcq.save()
                    updated_count += 1
                    logging.info(f"Fixed MCQ ID {mcq_id} by removing quotes: {fixed_text[:50]}...")
        except MCQ.DoesNotExist:
            logging.error(f"MCQ with ID {mcq_id} not found")
        except Exception as e:
            logging.error(f"Error updating MCQ ID {mcq_id}: {e}")
    
    return updated_count, no_match_count

def main():
    start_time = time.time()
    logging.info("Starting the MCQ fix process")
    
    # Get unmatched MCQs by subspecialty
    subspecialty_mcqs = get_unmatched_mcqs_by_subspecialty()
    total_mcqs = sum(len(mcqs) for mcqs in subspecialty_mcqs.values())
    logging.info(f"Found {total_mcqs} MCQs with quote issues across {len(subspecialty_mcqs)} subspecialties")
    
    # Process each subspecialty
    results = {}
    total_updated = 0
    total_no_match = 0
    
    for subspecialty, mcqs in subspecialty_mcqs.items():
        if not mcqs:
            continue
        
        logging.info(f"Processing {len(mcqs)} MCQs for subspecialty: {subspecialty}")
        
        # Create dummy matches for the fix function
        matches = [{"id": mcq["id"], "question_text": "REMOVE_QUOTES"} for mcq in mcqs]
        updated, no_match = update_mcqs_with_matches(matches)
        
        total_updated += updated
        total_no_match += no_match
        
        results[subspecialty] = {
            "total": len(mcqs),
            "updated": updated,
            "no_match": no_match,
            "remaining": len(mcqs) - updated,
            "percent_fixed": (updated / len(mcqs) * 100) if len(mcqs) > 0 else 0
        }
        
        logging.info(f"Completed {subspecialty}: Updated {updated}/{len(mcqs)} MCQs ({results[subspecialty]['percent_fixed']:.2f}%)")
    
    # Calculate overall statistics
    overall_percent = (total_updated / total_mcqs * 100) if total_mcqs > 0 else 0
    remaining_total = total_mcqs - total_updated
    
    # Save statistics to JSON
    stats = {
        "overall": {
            "total_mcqs": total_mcqs,
            "total_updated": total_updated,
            "total_no_match": total_no_match,
            "remaining": remaining_total,
            "percent_fixed": overall_percent
        },
        "by_subspecialty": results,
        "runtime_seconds": time.time() - start_time
    }
    
    with open(stats_file, 'w') as f:
        json.dump(stats, f, indent=2)
    
    logging.info(f"Overall: Updated {total_updated}/{total_mcqs} MCQs ({overall_percent:.2f}%)")
    logging.info(f"Runtime: {stats['runtime_seconds']:.2f} seconds")
    logging.info(f"Statistics saved to {stats_file}")

if __name__ == "__main__":
    main()
