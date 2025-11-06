#!/usr/bin/env python3
"""
Script to generate questions for MCQs that still have placeholder text.
Uses GPT-5-mini to generate appropriate questions based on the options and answer.
"""

import os
import sys
import json
import logging
import time
from datetime import datetime
from pathlib import Path

# Set up Django environment
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')

import django
django.setup()

from django.db import transaction
from mcq.models import MCQ
from mcq.openai_integration import (
    client as openai_client,
    chat_completion,
    DEFAULT_MODEL,
    FALLBACK_MODEL,
    get_first_choice_text,
)

# Set up logging
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
log_file = LOG_DIR / f"generate_missing_questions_{timestamp}.log"
stats_file = LOG_DIR / f"generate_missing_questions_stats_{timestamp}.json"

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)

# Placeholder text to identify problematic MCQs
PLACEHOLDER_TEXT = "Select the correct answer from the options below"

def generate_question_with_openai(mcq):
    """
    Generate a question for the MCQ using OpenAI's API.
    Returns the generated question text.
    """
    if not openai_client:
        logging.error("OpenAI client unavailable – cannot generate question")
        return None
    
    # Format the options and correct answer
    options = mcq.get_options_dict()
    options_text = "\n".join([f"{key}. {value}" for key, value in options.items()])
    
    # Create the prompt
    prompt = f"""
You are a neurology professor creating a multiple-choice question for residents studying for board exams.

I have a neurology MCQ with the following options and I need you to create a clear, specific question that would have these options as possible answers.

MCQ subspecialty: {mcq.subspecialty}
Correct answer: {mcq.correct_answer}

Options:
{options_text}

Please write ONLY a single, clear question (1-3 sentences) that would make the correct answer ({mcq.correct_answer}) the right choice.
Do not include option letters or labels in the question. Do not explain your reasoning. Just write the question text.
"""

    try:
        try:
            response = chat_completion(
                openai_client,
                DEFAULT_MODEL,
                [
                    {"role": "system", "content": "You are a board-certified neurologist skilled at writing clear medical questions."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=150,
                temperature=0.2
            )
        except Exception as primary_error:
            if FALLBACK_MODEL and FALLBACK_MODEL != DEFAULT_MODEL:
                logging.warning(
                    "Primary model %s failed for MCQ %s (%s); retrying with %s",
                    DEFAULT_MODEL,
                    mcq.id,
                    primary_error,
                    FALLBACK_MODEL,
                )
                response = chat_completion(
                    openai_client,
                    FALLBACK_MODEL,
                    [
                        {"role": "system", "content": "You are a board-certified neurologist skilled at writing clear medical questions."},
                        {"role": "user", "content": prompt}
                    ],
                    max_tokens=150,
                    temperature=0.2
                )
            else:
                raise
        
        # Extract and clean up the generated question
        generated_question = get_first_choice_text(response)
        if not generated_question:
            raise RuntimeError("OpenAI returned empty content for generated question")
        
        # Remove any option labels that might have been included
        for letter in ['A', 'B', 'C', 'D', 'E']:
            generated_question = generated_question.replace(f"{letter}. ", "")
            generated_question = generated_question.replace(f"{letter}) ", "")
        
        # Remove any quotes around the question
        generated_question = generated_question.strip('"\'')
        
        return generated_question
    
    except Exception as e:
        logging.error(f"Error generating question for MCQ {mcq.id}: {e}")
        return None

@transaction.atomic
def generate_missing_questions(test_mode=False, limit=None, batch_size=10):
    """
    Generate questions for MCQs with placeholder text.
    
    Args:
        test_mode (bool): If True, don't save changes to database
        limit (int): Limit processing to this many MCQs (for testing)
        batch_size (int): Number of MCQs to process in a batch before sleeping
    """
    logging.info("Starting to generate questions for MCQs with placeholder text...")
    
    # Find all MCQs with placeholder text
    placeholder_mcqs = MCQ.objects.filter(question_text__icontains=PLACEHOLDER_TEXT)
    
    if limit:
        placeholder_mcqs = placeholder_mcqs[:limit]
    
    total_placeholder_mcqs = placeholder_mcqs.count()
    
    # Statistics
    stats = {
        "total_mcqs": MCQ.objects.count(),
        "placeholder_mcqs": total_placeholder_mcqs,
        "generated_questions": 0,
        "failed_generations": 0,
        "by_subspecialty": {}
    }
    
    # Track issues by subspecialty
    subspecialty_stats = {}
    
    # Process each MCQ
    for i, mcq in enumerate(placeholder_mcqs):
        # Initialize subspecialty stats if needed
        if mcq.subspecialty not in subspecialty_stats:
            subspecialty_stats[mcq.subspecialty] = {
                "total": 0,
                "generated": 0,
                "failed": 0
            }
        
        subspecialty_stats[mcq.subspecialty]["total"] += 1
        
        logging.info(f"Processing MCQ {mcq.id} ({i+1}/{total_placeholder_mcqs}) - Subspecialty: {mcq.subspecialty}")
        
        # Generate question
        new_question_text = generate_question_with_openai(mcq)
        
        if new_question_text:
            logging.info(f"MCQ {mcq.id} ({mcq.subspecialty}): Generated question")
            logging.info(f"  Old: {mcq.question_text}")
            logging.info(f"  New: {new_question_text}")
            
            # Update the MCQ if not in test mode
            if not test_mode:
                mcq.question_text = new_question_text
                mcq.save()
            
            stats["generated_questions"] += 1
            subspecialty_stats[mcq.subspecialty]["generated"] += 1
        else:
            logging.warning(f"MCQ {mcq.id} ({mcq.subspecialty}): Failed to generate question")
            stats["failed_generations"] += 1
            subspecialty_stats[mcq.subspecialty]["failed"] += 1
        
        # Sleep after each batch to avoid rate limiting
        if (i + 1) % batch_size == 0:
            logging.info(f"Processed {i+1}/{total_placeholder_mcqs} MCQs. Sleeping for 5 seconds...")
            time.sleep(5)
    
    # Finalize subspecialty stats
    for subspecialty, counts in subspecialty_stats.items():
        stats["by_subspecialty"][subspecialty] = {
            "total": counts["total"],
            "generated": counts["generated"],
            "generated_percentage": round(counts["generated"] / counts["total"] * 100, 2) if counts["total"] > 0 else 0,
            "failed": counts["failed"],
            "failed_percentage": round(counts["failed"] / counts["total"] * 100, 2) if counts["total"] > 0 else 0
        }
    
    # Log summary
    logging.info("\n===== SUMMARY =====")
    logging.info(f"Total MCQs in database: {stats['total_mcqs']}")
    logging.info(f"MCQs with placeholder text: {stats['placeholder_mcqs']} ({stats['placeholder_mcqs']/stats['total_mcqs']*100:.2f}%)")
    logging.info(f"MCQs with generated questions: {stats['generated_questions']} ({stats['generated_questions']/stats['placeholder_mcqs']*100:.2f}% of placeholders)")
    logging.info(f"MCQs with failed generations: {stats['failed_generations']}")
    
    # Log subspecialty breakdown
    logging.info("\n===== GENERATIONS BY SUBSPECIALTY =====")
    for subspecialty, data in sorted(stats["by_subspecialty"].items(), key=lambda x: x[1]["total"], reverse=True):
        logging.info(f"{subspecialty}: {data['generated']} generated out of {data['total']} placeholders ({data['generated_percentage']}%)")
    
    # Save stats to file
    with open(stats_file, 'w') as f:
        json.dump(stats, f, indent=2)
    
    logging.info(f"Statistics saved to {stats_file}")
    return stats

def main():
    """
    Main function that processes command line arguments and runs the generation.
    """
    import argparse
    
    parser = argparse.ArgumentParser(description='Generate questions for MCQs with placeholder text')
    parser.add_argument('--test', action='store_true', help='Run in test mode (no changes saved to database)')
    parser.add_argument('--limit', type=int, help='Limit processing to this many MCQs (for testing)')
    parser.add_argument('--batch_size', type=int, default=10, help='Number of MCQs to process in a batch before sleeping')
    args = parser.parse_args()
    
    if args.test:
        logging.info("Running in TEST MODE - no changes will be saved")
    
    generate_missing_questions(test_mode=args.test, limit=args.limit, batch_size=args.batch_size)

if __name__ == "__main__":
    main()
