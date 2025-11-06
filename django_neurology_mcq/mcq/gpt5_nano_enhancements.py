#!/usr/bin/env python3
"""
GPT-5-nano specific enhancements for MCQ options editing
Provides medical terminology database and intelligent fallbacks
"""

import re
import json
import logging
from typing import Dict, List, Optional, Tuple, Any
from functools import lru_cache
import hashlib
from django.core.cache import cache

logger = logging.getLogger(__name__)

# Medical terminology database optimized for neurology
NEUROLOGY_TERMINOLOGY = {
    "conditions": {
        "myopathy": {
            "terms": ["proximal weakness", "elevated CK", "muscle biopsy", "EMG findings"],
            "subtypes": ["inflammatory", "metabolic", "toxic", "genetic", "endocrine"]
        },
        "neuropathy": {
            "terms": ["distal weakness", "sensory loss", "nerve conduction", "denervation"],
            "subtypes": ["axonal", "demyelinating", "mixed", "small fiber", "large fiber"]
        },
        "movement_disorders": {
            "terms": ["bradykinesia", "tremor", "rigidity", "dystonia", "chorea"],
            "subtypes": ["parkinsonian", "hyperkinetic", "hypokinetic", "ataxic"]
        },
        "epilepsy": {
            "terms": ["seizure", "EEG", "ictal", "post-ictal", "aura"],
            "subtypes": ["focal", "generalized", "absence", "tonic-clonic", "myoclonic"]
        },
        "stroke": {
            "terms": ["hemiparesis", "aphasia", "neglect", "visual field defect"],
            "subtypes": ["ischemic", "hemorrhagic", "embolic", "thrombotic", "lacunar"]
        }
    },
    "clinical_patterns": [
        "acute onset", "subacute progression", "chronic course",
        "fluctuating symptoms", "progressive decline", "stepwise deterioration",
        "symmetric involvement", "asymmetric presentation", "proximal predominance",
        "distal distribution", "length-dependent pattern", "multifocal involvement"
    ],
    "diagnostic_modifiers": [
        "confirmed by", "suggested by", "consistent with", "characteristic of",
        "typical for", "diagnostic of", "pathognomonic for", "indicative of"
    ]
}

# Cache configuration
CACHE_CONFIG = {
    "enabled": True,
    "ttl": 3600,  # 1 hour
    "prefix": "gpt5_nano_options"
}


def get_cache_key(mcq_id: Any, mode: str, instructions: str = "") -> str:
    """Generate a cache key for storing API results"""
    content = f"{mcq_id}_{mode}_{instructions[:50]}"
    return f"{CACHE_CONFIG['prefix']}_{hashlib.md5(content.encode()).hexdigest()}"


def get_cached_result(mcq_id: Any, mode: str, instructions: str = "") -> Optional[Dict]:
    """Retrieve cached result if available"""
    if not CACHE_CONFIG["enabled"]:
        return None

    cache_key = get_cache_key(mcq_id, mode, instructions)
    cached = cache.get(cache_key)

    if cached:
        logger.info(f"Cache hit for MCQ #{mcq_id}, mode: {mode}")
        return cached

    return None


def cache_result(result: Dict, mcq_id: Any, mode: str, instructions: str = "") -> None:
    """Cache the API result"""
    if not CACHE_CONFIG["enabled"] or not result.get("success"):
        return

    cache_key = get_cache_key(mcq_id, mode, instructions)
    cache.set(cache_key, result, CACHE_CONFIG["ttl"])
    logger.info(f"Cached result for MCQ #{mcq_id}, mode: {mode}")


@lru_cache(maxsize=128)
def identify_medical_context(question_text: str) -> str:
    """Identify the medical context from question text"""
    question_lower = question_text.lower()

    # Check for specific conditions
    for condition, details in NEUROLOGY_TERMINOLOGY["conditions"].items():
        for term in details["terms"]:
            if term.lower() in question_lower:
                return condition

    # Default context
    if "weakness" in question_lower:
        return "myopathy" if "proximal" in question_lower else "neuropathy"
    elif "seizure" in question_lower or "epilep" in question_lower:
        return "epilepsy"
    elif "tremor" in question_lower or "bradykinesia" in question_lower:
        return "movement_disorders"
    elif "stroke" in question_lower or "hemiparesis" in question_lower:
        return "stroke"

    return "general_neurology"


def enhance_option_text(
    option_text: str,
    is_correct: bool,
    medical_context: str,
    target_length: int = 80
) -> str:
    """
    Enhance option text with medical terminology and clinical details

    Args:
        option_text: Original option text
        is_correct: Whether this is the correct answer
        medical_context: Medical context identified from question
        target_length: Target character length for enhancement

    Returns:
        Enhanced option text
    """

    # Don't modify if already detailed
    if len(option_text) >= target_length:
        return option_text

    # Handle very short or vague options
    if len(option_text) < 20:
        # Map common vague options to specific medical terms
        vague_mappings = {
            "other": "Alternative neurological condition",
            "none": "No specific neurological diagnosis",
            "something else": "Different etiology to consider",
            "unknown": "Idiopathic condition of unclear origin",
            "normal": "Normal neurological examination",
            "abnormal": "Abnormal neurological findings"
        }

        for vague, replacement in vague_mappings.items():
            if vague in option_text.lower():
                option_text = replacement
                break

    # Get relevant terminology for the medical context
    context_terms = NEUROLOGY_TERMINOLOGY["conditions"].get(medical_context, {})

    # For correct answers, ensure accuracy and add confirming details
    if is_correct:
        # Add diagnostic confirmation
        modifiers = NEUROLOGY_TERMINOLOGY["diagnostic_modifiers"]
        if not any(mod in option_text.lower() for mod in modifiers):
            import random
            modifier = random.choice(modifiers[:4])  # Use more confident modifiers
            option_text = f"{option_text}, {modifier} this diagnosis"

    else:
        # For distractors, make plausible but distinguishable
        if medical_context in NEUROLOGY_TERMINOLOGY["conditions"]:
            subtypes = context_terms.get("subtypes", [])
            if subtypes and not any(sub in option_text.lower() for sub in subtypes):
                import random
                subtype = random.choice(subtypes)
                pattern = random.choice(NEUROLOGY_TERMINOLOGY["clinical_patterns"])
                option_text = f"{subtype.capitalize()} {medical_context} with {pattern}"

    # Ensure minimum length
    while len(option_text) < 40:
        option_text += " requiring further evaluation"
        break

    return option_text


def validate_gpt5_response(response_text: str) -> Tuple[bool, Optional[Dict], List[str]]:
    """
    Validate and extract options from GPT-5-nano response

    Returns:
        Tuple of (is_valid, extracted_options, error_messages)
    """
    errors = []

    if not response_text:
        errors.append("Empty response received")
        return False, None, errors

    # Try to extract JSON
    extracted = None

    # Method 1: Direct JSON parsing
    try:
        extracted = json.loads(response_text)
    except json.JSONDecodeError:
        pass

    # Method 2: Extract from markdown code block
    if not extracted:
        code_block_match = re.search(r'```(?:json)?\s*(\{.*?\})\s*```', response_text, re.DOTALL)
        if code_block_match:
            try:
                extracted = json.loads(code_block_match.group(1))
            except json.JSONDecodeError:
                errors.append("Failed to parse JSON from code block")

    # Method 3: Find JSON object in text
    if not extracted:
        json_match = re.search(r'\{[^{}]*"[ABC]"\s*:\s*"[^"]+.*?\}', response_text, re.DOTALL)
        if json_match:
            try:
                extracted = json.loads(json_match.group(0))
            except json.JSONDecodeError:
                errors.append("Failed to parse embedded JSON")

    # Method 4: Extract individual options
    if not extracted:
        extracted = {}
        for letter in ['A', 'B', 'C', 'D']:
            # Multiple patterns to match different formats
            patterns = [
                rf'"{letter}"\s*:\s*"([^"]+)"',
                rf'{letter}\.\s*([^\n]+)',
                rf'\({letter}\)\s*([^\n]+)',
                rf'{letter}:\s*([^\n]+)'
            ]

            for pattern in patterns:
                match = re.search(pattern, response_text)
                if match:
                    extracted[letter] = match.group(1).strip()
                    break

    # Validate extracted options
    if extracted:
        # Check all required options are present
        missing = [letter for letter in ['A', 'B', 'C', 'D'] if letter not in extracted]
        if missing:
            errors.append(f"Missing options: {', '.join(missing)}")

        # Check option lengths
        for letter, text in extracted.items():
            if len(text) < 5:
                errors.append(f"Option {letter} too short: '{text}'")
            elif len(text) > 500:
                errors.append(f"Option {letter} too long: {len(text)} chars")

        # Check for duplicates
        texts = list(extracted.values())
        if len(texts) != len(set(texts)):
            errors.append("Duplicate options detected")

        is_valid = len(errors) == 0
        return is_valid, extracted if is_valid else None, errors

    errors.append("Could not extract options from response")
    return False, None, errors


def create_fallback_options(
    mcq,
    mode: str = "improve_all"
) -> Dict[str, str]:
    """
    Create fallback options when API fails
    Uses medical terminology database for intelligent generation
    """
    logger.info(f"Creating fallback options for MCQ #{getattr(mcq, 'id', 'unknown')}")

    question_text = getattr(mcq, "question_text", "")
    current_options = mcq.get_options_dict() if hasattr(mcq, "get_options_dict") else {}
    correct_answer = getattr(mcq, "correct_answer", "A")

    # Identify medical context
    medical_context = identify_medical_context(question_text)

    # Create or enhance options
    fallback_options = {}

    for letter in ['A', 'B', 'C', 'D']:
        current_text = current_options.get(letter, f"Option {letter}")
        is_correct = (letter == correct_answer)

        # Enhance the option text
        enhanced_text = enhance_option_text(
            current_text,
            is_correct,
            medical_context,
            target_length=60
        )

        fallback_options[letter] = enhanced_text

    return fallback_options


def post_process_options(
    options: Dict[str, str],
    correct_answer: str,
    original_options: Dict[str, str]
) -> Dict[str, str]:
    """
    Post-process GPT-5-nano generated options for quality assurance

    Args:
        options: Generated options
        correct_answer: The correct answer letter
        original_options: Original options for comparison

    Returns:
        Post-processed options
    """

    processed = dict(options)

    # Ensure correct answer hasn't changed dramatically
    if correct_answer in processed and correct_answer in original_options:
        original = original_options[correct_answer]
        generated = processed[correct_answer]

        # Check similarity
        if len(original) > 20:  # Only check substantial options
            original_words = set(original.lower().split())
            generated_words = set(generated.lower().split())

            overlap = len(original_words & generated_words) / len(original_words) if original_words else 0

            if overlap < 0.3:  # Less than 30% overlap
                logger.warning(
                    f"Correct answer changed significantly (overlap: {overlap:.1%}), "
                    f"restoring original"
                )
                processed[correct_answer] = original

    # Ensure all options have minimum quality
    for letter in ['A', 'B', 'C', 'D']:
        if letter not in processed or not processed[letter]:
            # Use original or create placeholder
            processed[letter] = original_options.get(
                letter,
                f"Option {letter} - requires medical review"
            )
        elif len(processed[letter]) < 10:
            # Enhance very short options
            is_correct = (letter == correct_answer)
            medical_context = identify_medical_context(
                getattr(options, "question_text", "neurology")
            )
            processed[letter] = enhance_option_text(
                processed[letter],
                is_correct,
                medical_context
            )

    return processed


def calculate_improvement_metrics(
    original: Dict[str, str],
    improved: Dict[str, str]
) -> Dict[str, Any]:
    """Calculate detailed metrics about the improvement"""

    metrics = {
        "original_total_chars": sum(len(text) for text in original.values()),
        "improved_total_chars": sum(len(text) for text in improved.values()),
        "improvement_ratio": 0,
        "options_expanded": 0,
        "medical_terms_added": 0,
        "average_option_length": 0
    }

    if metrics["original_total_chars"] > 0:
        metrics["improvement_ratio"] = (
            metrics["improved_total_chars"] / metrics["original_total_chars"]
        )

    # Count expanded options
    for letter in ['A', 'B', 'C', 'D']:
        orig_len = len(original.get(letter, ""))
        imp_len = len(improved.get(letter, ""))
        if imp_len > orig_len * 1.5:
            metrics["options_expanded"] += 1

    # Count medical terms
    medical_keywords = [
        "syndrome", "disease", "disorder", "neuropathy", "myopathy",
        "inflammatory", "chronic", "acute", "bilateral", "unilateral",
        "diagnostic", "pathognomonic", "characteristic", "typical"
    ]

    for text in improved.values():
        text_lower = text.lower()
        for keyword in medical_keywords:
            if keyword in text_lower:
                metrics["medical_terms_added"] += 1

    metrics["average_option_length"] = (
        metrics["improved_total_chars"] / 4 if improved else 0
    )

    return metrics


# Export main enhancement functions
__all__ = [
    'get_cached_result',
    'cache_result',
    'identify_medical_context',
    'enhance_option_text',
    'validate_gpt5_response',
    'create_fallback_options',
    'post_process_options',
    'calculate_improvement_metrics',
    'NEUROLOGY_TERMINOLOGY',
    'CACHE_CONFIG'
]