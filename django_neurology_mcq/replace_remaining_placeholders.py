#!/usr/bin/env python3
"""
Script to replace remaining placeholder explanations with detailed ones for all MCQs.
This script uses the shared OpenAI integration (defaulting to GPT-5-mini) to generate explanations for MCQs that still have placeholder text.
"""

import os
import sys
import django
import json
import logging
import time
import datetime
from django.db import transaction

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
django.setup()

from mcq.models import MCQ
from mcq.openai_integration import (
    client as openai_client,
    chat_completion,
    DEFAULT_MODEL,
    FALLBACK_MODEL,
    api_key,
    get_first_choice_text,
)

# Setup logging
log_dir = 'logs'
os.makedirs(log_dir, exist_ok=True)
timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
log_file = os.path.join(log_dir, f'replace_remaining_placeholders_{timestamp}.log')
stats_file = os.path.join(log_dir, f'replace_remaining_placeholders_stats_{timestamp}.json')

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def generate_structured_explanation(mcq):
    """
    Generate a structured explanation for an MCQ using OpenAI API.
    
    Args:
        mcq: MCQ object to generate explanation for
        
    Returns:
        str: Structured explanation text
    """
    if not api_key or not client:
        logger.error("OpenAI client not available")
        return None
    
    # Get MCQ details
    question = mcq.question_text
    options = mcq.get_options_dict()
    correct_answer = mcq.correct_answer
    subspecialty = mcq.subspecialty
    
    # Format options for the prompt
    options_text = ""
    for option, text in options.items():
        options_text += f"{option}. {text}\n"
    
    # Create a detailed prompt
    prompt = f"""Create a detailed, evidence-based explanation for this neurology MCQ:

Question: {question}

Options:
{options_text}

Correct Answer: {correct_answer}

Subspecialty: {subspecialty}

Please provide a comprehensive explanation that includes:

1. Conceptual Framework & Clinical Context:
   - Key neurological principles being tested
   - Relevant pathophysiology
   - Clinical significance

2. Evidence-Based Analysis:
   - Why the correct answer is right (with evidence)
   - Current guidelines or best practices
   - Key research supporting this approach

3. Incorrect Options Analysis:
   - Why each incorrect option is wrong
   - Common misconceptions related to these options

4. Clinical Pearls:
   - Important points to remember
   - Differential diagnosis considerations
   - Practical clinical implications

Please format the explanation in Markdown with proper headings and structure.
"""

    if not openai_client:
        logger.error("OpenAI client unavailable – cannot generate explanation")
        return None

    try:
        try:
            response = chat_completion(
                openai_client,
                DEFAULT_MODEL,
                [
                    {"role": "system", "content": "You are a board-certified neurologist creating detailed explanations for neurology MCQs. Provide evidence-based, well-structured explanations with current guidelines and best practices."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=3000,
                temperature=0.3
            )
        except Exception as primary_error:
            if FALLBACK_MODEL and FALLBACK_MODEL != DEFAULT_MODEL:
                logger.warning(
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
                        {"role": "system", "content": "You are a board-certified neurologist creating detailed explanations for neurology MCQs. Provide evidence-based, well-structured explanations with current guidelines and best practices."},
                        {"role": "user", "content": prompt}
                    ],
                    max_tokens=3000,
                    temperature=0.3
                )
            else:
                raise

        content = get_first_choice_text(response)
        if not content:
            raise RuntimeError("OpenAI returned empty explanation content")
        return content
    except Exception as e:
        logger.error(f"Error generating explanation: {str(e)}")
        return None

def identify_remaining_placeholders(subspecialties=None):
    """Identify MCQs that still have placeholder explanations."""
    placeholder_text = "This MCQ tests understanding of key concepts"
    
    if subspecialties:
        mcqs = MCQ.objects.filter(
            explanation__contains=placeholder_text,
            subspecialty__in=subspecialties
        )
    else:
        mcqs = MCQ.objects.filter(explanation__contains=placeholder_text)
    
    logger.info(f"Found {mcqs.count()} MCQs with placeholder explanations")
    
    return mcqs

def replace_remaining_explanations(mcqs, batch_size=5, limit=None):
    """Replace placeholder explanations with AI-generated detailed ones."""
    updated_count = 0
    total_mcqs = len(mcqs)
    
    # Apply limit if specified
    if limit and limit < total_mcqs:
        mcqs = mcqs[:limit]
        total_mcqs = limit
        logger.info(f"Limiting to {limit} MCQs")
    
    for i in range(0, total_mcqs, batch_size):
        batch = mcqs[i:i+batch_size]
        logger.info(f"Processing batch {i//batch_size + 1}/{(total_mcqs-1)//batch_size + 1} ({len(batch)} MCQs)")
        
        with transaction.atomic():
            for mcq in batch:
                try:
                    # Generate a detailed explanation
                    explanation = generate_structured_explanation(mcq)
                    
                    if explanation and len(explanation) > 200:
                        mcq.explanation = explanation
                        mcq.save()
                        updated_count += 1
                        logger.info(f"Updated MCQ {mcq.id} ({mcq.question_number}) in {mcq.subspecialty}")
                    else:
                        logger.warning(f"Failed to generate meaningful explanation for MCQ {mcq.id}")
                except Exception as e:
                    logger.error(f"Error updating explanation for MCQ {mcq.id}: {str(e)}")
        
        # Add a delay between batches to avoid rate limiting
        if i + batch_size < total_mcqs:
            time.sleep(2)
    
    return updated_count

def main():
    """Main function to replace remaining placeholder explanations."""
    logger.info("Starting to replace remaining placeholder explanations")
    
    # Check if API key and client are available
    if not api_key or not client:
        logger.error("OpenAI API client not available. Please set the OPENAI_API_KEY environment variable.")
        return
    else:
        logger.info("OpenAI API client is available and ready")
    
    # Target subspecialties (Headache and Sleep Neurology)
    subspecialties = ['Headache', 'Sleep Neurology']
    
    # Identify MCQs with placeholder explanations
    placeholder_mcqs = identify_remaining_placeholders(subspecialties)
    
    # Get counts by subspecialty
    stats = {}
    for subspecialty in subspecialties:
        count = placeholder_mcqs.filter(subspecialty=subspecialty).count()
        stats[subspecialty] = {
            'placeholders_found': count,
            'updated': 0
        }
        logger.info(f"Found {count} MCQs with placeholder explanations in {subspecialty}")
    
    # Replace explanations
    updated_count = replace_remaining_explanations(placeholder_mcqs)
    
    # Update stats for each subspecialty
    for subspecialty in subspecialties:
        remaining = MCQ.objects.filter(
            explanation__contains="This MCQ tests understanding of key concepts",
            subspecialty=subspecialty
        ).count()
        stats[subspecialty]['updated'] = stats[subspecialty]['placeholders_found'] - remaining
    
    # Save stats
    stats['timestamp'] = timestamp
    stats['total_placeholders'] = placeholder_mcqs.count()
    stats['total_updated'] = updated_count
    
    with open(stats_file, 'w') as f:
        json.dump(stats, f, indent=2)
    
    logger.info(f"Statistics saved to {stats_file}")
    logger.info(f"Total MCQs updated: {updated_count}/{placeholder_mcqs.count()}")
    logger.info("Please restart the Django server to see the changes.")

if __name__ == "__main__":
    start_time = time.time()
    main()
    logger.info(f"Script completed in {time.time() - start_time:.2f} seconds.")
