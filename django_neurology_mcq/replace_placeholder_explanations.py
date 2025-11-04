#!/usr/bin/env python3
"""
Script to replace placeholder explanations with detailed ones for Headache and Sleep Neurology MCQs.
This generates proper explanations using the shared GPT-5-mini integration and updates the database.
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
log_file = os.path.join(log_dir, f'replace_placeholder_explanations_{timestamp}.log')
stats_file = os.path.join(log_dir, f'replace_placeholder_explanations_stats_{timestamp}.json')

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
    if not api_key or not openai_client:
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

def identify_placeholders():
    """Identify MCQs with placeholder explanations in target subspecialties."""
    target_subspecialties = ['Headache', 'Sleep Neurology']
    placeholder_mcqs = []
    
    for subspecialty in target_subspecialties:
        mcqs = MCQ.objects.filter(subspecialty=subspecialty)
        logger.info(f"Found {mcqs.count()} MCQs for {subspecialty}")
        
        for mcq in mcqs:
            # Check if the explanation contains generic template language
            generic_phrases = [
                "This MCQ tests understanding of key concepts",
                "The clinical scenario involves a clinical presentation",
                "Current evidence-based practice does not support",
                "The correct answer is",
                "because it aligns with current clinical evidence"
            ]
            
            if mcq.explanation and any(phrase in mcq.explanation for phrase in generic_phrases):
                placeholder_mcqs.append(mcq)
                logger.info(f"Found placeholder for MCQ {mcq.id} in {subspecialty}")
    
    return placeholder_mcqs

def replace_explanations(placeholder_mcqs, batch_size=5):
    """Replace placeholder explanations with detailed ones."""
    updated_count = 0
    total_mcqs = len(placeholder_mcqs)
    
    for i in range(0, total_mcqs, batch_size):
        batch = placeholder_mcqs[i:i+batch_size]
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
                        logger.info(f"Updated MCQ {mcq.id} ({mcq.question_number})")
                    else:
                        logger.warning(f"Failed to generate meaningful explanation for MCQ {mcq.id}")
                except Exception as e:
                    logger.error(f"Error updating explanation for MCQ {mcq.id}: {str(e)}")
        
        # Add a delay between batches to avoid rate limiting
        if i + batch_size < total_mcqs:
            time.sleep(2)
    
    return updated_count

def main():
    """Main function to replace placeholder explanations."""
    logger.info("Starting to replace placeholder explanations")
    
    # Check if API key and client are available
    if not api_key or not client:
        logger.error("OpenAI API client not available. Please set the OPENAI_API_KEY environment variable.")
        return
    else:
        logger.info("OpenAI API client is available and ready")
    
    # Identify MCQs with placeholder explanations
    placeholder_mcqs = identify_placeholders()
    logger.info(f"Found {len(placeholder_mcqs)} MCQs with placeholder explanations")
    
    # Replace explanations
    updated_count = replace_explanations(placeholder_mcqs)
    logger.info(f"Updated {updated_count}/{len(placeholder_mcqs)} MCQs")
    
    # Record stats
    stats = {
        'total_placeholder_mcqs': len(placeholder_mcqs),
        'updated_mcqs': updated_count,
        'timestamp': timestamp
    }
    
    # Write stats to file
    with open(stats_file, 'w') as f:
        json.dump(stats, f, indent=2)
    
    logger.info(f"Statistics saved to {stats_file}")
    logger.info("Please restart the Django server to see the changes.")

if __name__ == "__main__":
    start_time = time.time()
    main()
    logger.info(f"Script completed in {time.time() - start_time:.2f} seconds.")
