#!/usr/bin/env python3
"""
Complete refactor of options editing to fix empty JSON responses
This replaces the problematic JSON schema approach with a simpler text-based approach
that works reliably with GPT-5-nano
"""

import re
import json
import logging
from typing import Dict, List, Optional, Any

logger = logging.getLogger(__name__)


def create_refactored_options_functions():
    """Create the refactored options editing functions"""

    code = '''
# =============================================================================
# REFACTORED OPTIONS EDITING FUNCTIONS FOR GPT-5-NANO
# =============================================================================

def _improve_all_options_with_model_refactored(mcq, custom_instructions: str, model_name: str) -> dict:
    """
    REFACTORED: AI-powered option improvement using TEXT response instead of JSON schema.
    This avoids the empty JSON issue with GPT-5-nano.
    """
    if not api_key or not client:
        logger.info("Using original options due to unavailable OpenAI API")
        return mcq.get_options_dict() if hasattr(mcq, 'get_options_dict') else {}

    try:
        mcq_id = getattr(mcq, "id", "unknown")
        logger.info("AI improving all options for MCQ #%s using model %s (REFACTORED)", mcq_id, model_name)

        question_text = getattr(mcq, "question_text", "")
        current_options = mcq.get_options_dict() if hasattr(mcq, "get_options_dict") else {}
        correct_answer = getattr(mcq, "correct_answer", "A")
        explanation = getattr(mcq, "explanation", "")[:500]  # Truncate for prompt
        subspecialty = getattr(mcq, "subspecialty", "General Neurology")

        # Build a text-based prompt instead of using JSON schema
        system_prompt = """You are a medical expert specializing in neurology MCQs.
Your task is to improve MCQ answer options to make them educationally valuable.
Keep the correct answer unchanged but improve all incorrect options to be plausible distractors.
Format your response as a simple list with each option on a new line."""

        user_prompt = f"""Question: {question_text}

Current Options:
A) {current_options.get('A', '')}
B) {current_options.get('B', '')}
C) {current_options.get('C', '')}
D) {current_options.get('D', '')}

Correct Answer: {correct_answer}
Subspecialty: {subspecialty}

{f"Additional context: {explanation[:200]}" if explanation else ""}
{f"Custom instructions: {custom_instructions}" if custom_instructions else ""}

Please provide improved options in this exact format:
A) [improved option A text]
B) [improved option B text]
C) [improved option C text]
D) [improved option D text]

Rules:
- Keep the correct answer ({correct_answer}) exactly the same
- Make incorrect options plausible but wrong
- Add medical detail and terminology
- Each option should be 20-100 characters"""

        messages = [
            {"role": "system", "content": [{"type": "text", "text": system_prompt}]},
            {"role": "user", "content": [{"type": "text", "text": user_prompt}]}
        ]

        # Use text response with GPT-5-nano
        start_time = time.monotonic()

        # Call the API with TEXT response (not JSON schema)
        response = _responses_create(
            model_name,
            messages,
            response_format={"type": "text"},  # TEXT not JSON!
            max_output_tokens=400,  # Reduced for faster response
            temperature=0.3,  # Lower for consistency
            top_p=0.8,  # More focused
            use_vector=False,  # Simpler without vector store
            timeout=OPTION_REQUEST_TIMEOUT,
        )

        elapsed = time.monotonic() - start_time
        logger.info(f"GPT-5-nano response received in {elapsed:.1f}s for MCQ #{mcq_id}")

        # Extract text from response
        response_text = _extract_response_text(response)

        if not response_text:
            logger.warning(f"Empty response from {model_name} for MCQ #{mcq_id}")
            raise ValueError("Empty response received")

        # Parse the text response into options
        improved_options = _parse_options_from_text(response_text, current_options, correct_answer)

        if not improved_options:
            logger.warning(f"Failed to parse options from response for MCQ #{mcq_id}")
            raise ValueError("Could not parse options from response")

        logger.info(f"Successfully improved options for MCQ #{mcq_id} using {model_name}")
        return improved_options

    except Exception as e:
        logger.error(f"Error in refactored options improvement for MCQ #{getattr(mcq, 'id', 'unknown')}: {str(e)}")
        # Return original options as fallback
        return mcq.get_options_dict() if hasattr(mcq, 'get_options_dict') else {}


def _parse_options_from_text(text: str, original_options: dict, correct_answer: str) -> dict:
    """
    Parse options from text response.
    Robust parsing that handles various formats.
    """
    if not text:
        return {}

    parsed_options = {}

    # Method 1: Look for "A) text" or "A. text" or "A: text" patterns
    patterns = [
        r'([A-D])\)\s*(.+?)(?=\\n[A-D][\)\.\:]|$)',  # A) text
        r'([A-D])\.\s*(.+?)(?=\\n[A-D][\)\.\:]|$)',   # A. text
        r'([A-D]):\s*(.+?)(?=\\n[A-D][\)\.\:]|$)',    # A: text
        r'Option ([A-D]):\s*(.+?)(?=\\nOption [A-D]|$)',  # Option A: text
    ]

    for pattern in patterns:
        matches = re.findall(pattern, text, re.MULTILINE | re.DOTALL)
        if matches:
            for letter, option_text in matches:
                option_text = option_text.strip()
                # Clean up the text
                option_text = option_text.replace('\\n', ' ')
                option_text = option_text.replace('[', '').replace(']', '')
                option_text = re.sub(r'\\s+', ' ', option_text)  # Normalize whitespace

                if option_text:
                    parsed_options[letter] = option_text

            if len(parsed_options) == 4:
                break

    # Method 2: If pattern matching failed, try line-by-line parsing
    if len(parsed_options) < 4:
        lines = text.strip().split('\\n')
        for line in lines:
            line = line.strip()
            for letter in ['A', 'B', 'C', 'D']:
                if letter not in parsed_options and line.startswith(letter):
                    # Extract text after the letter and separator
                    text_match = re.match(rf'{letter}[\)\.\:]\\s*(.+)', line)
                    if text_match:
                        option_text = text_match.group(1).strip()
                        if option_text:
                            parsed_options[letter] = option_text

    # Ensure we have all 4 options
    for letter in ['A', 'B', 'C', 'D']:
        if letter not in parsed_options:
            # Use original option as fallback
            parsed_options[letter] = original_options.get(letter, f"Option {letter}")

    # Preserve the correct answer exactly as it was
    if correct_answer in original_options and correct_answer in parsed_options:
        parsed_options[correct_answer] = original_options[correct_answer]

    # Validate option quality
    for letter, text in parsed_options.items():
        # Ensure minimum length
        if len(text) < 5:
            parsed_options[letter] = original_options.get(letter, f"Option {letter} - needs review")
        # Ensure not too long
        elif len(text) > 200:
            parsed_options[letter] = text[:197] + "..."

    return parsed_options


def ai_improve_all_options_refactored(mcq, custom_instructions: str = "") -> dict:
    """
    REFACTORED: Main entry point for options improvement.
    Uses text-based approach instead of JSON schema.
    """
    last_error: Optional[Exception] = None

    # Try each model in priority order
    for model_name in _option_model_priority():
        try:
            logger.info(f"Attempting options improvement with {model_name}")
            result = _improve_all_options_with_model_refactored(mcq, custom_instructions, model_name)

            # Validate result
            if result and len(result) == 4:
                return result
            else:
                raise ValueError("Invalid result structure")

        except Exception as exc:
            last_error = exc
            logger.warning(
                "ai_improve_all_options_refactored failed for MCQ #%s using model %s: %s",
                getattr(mcq, "id", "unknown"),
                model_name,
                exc,
            )
            continue

    # If all models failed, return original options
    logger.error(f"All models failed for options improvement: {last_error}")
    return mcq.get_options_dict() if hasattr(mcq, 'get_options_dict') else {
        'A': 'Option A',
        'B': 'Option B',
        'C': 'Option C',
        'D': 'Option D'
    }


def ai_edit_options_refactored(mcq, custom_instructions: str = "") -> dict:
    """
    REFACTORED: Fill missing options using text-based approach.
    """
    last_error: Optional[Exception] = None

    for model_name in _option_model_priority():
        try:
            logger.info(f"Attempting to fill missing options with {model_name}")

            # Get current options
            current_options = mcq.get_options_dict() if hasattr(mcq, "get_options_dict") else {}

            # Identify missing options
            missing = []
            for letter in ['A', 'B', 'C', 'D']:
                if letter not in current_options or not current_options[letter] or len(current_options[letter]) < 3:
                    missing.append(letter)

            if not missing:
                logger.info("No missing options to fill")
                return current_options

            # Use the refactored improvement function
            result = _improve_all_options_with_model_refactored(mcq, custom_instructions, model_name)

            if result and len(result) == 4:
                return result
            else:
                raise ValueError("Invalid result structure")

        except Exception as exc:
            last_error = exc
            logger.warning(
                "ai_edit_options_refactored failed for MCQ #%s using model %s: %s",
                getattr(mcq, "id", "unknown"),
                model_name,
                exc,
            )
            continue

    # Return original options as fallback
    logger.error(f"All models failed for filling options: {last_error}")
    return mcq.get_options_dict() if hasattr(mcq, 'get_options_dict') else {}

'''

    return code


def create_patch_file():
    """Create a patch file to apply the refactored functions"""

    patch_content = '''#!/usr/bin/env python3
"""
Apply the refactored options editing functions to fix empty JSON issues
"""

import os
import sys
import time

def apply_refactor():
    """Apply the refactored options editing functions"""

    file_path = "django_neurology_mcq/mcq/openai_integration.py"

    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found")
        return False

    print(f"Applying refactored options editing to {file_path}")

    # Read the file
    with open(file_path, 'r') as f:
        lines = f.readlines()

    # Find and comment out the old functions
    changes_made = []

    # Add import for time if not present
    import_added = False
    for i, line in enumerate(lines):
        if "import time" in line:
            import_added = True
            break

    if not import_added:
        for i, line in enumerate(lines):
            if "import " in line and not import_added:
                lines.insert(i, "import time\\n")
                changes_made.append(f"Line {i+1}: Added time import")
                import_added = True
                break

    # Replace the functions
    for i, line in enumerate(lines):
        # Replace ai_improve_all_options
        if "def ai_improve_all_options(mcq" in line:
            # Find the end of the function
            indent = len(line) - len(line.lstrip())
            j = i + 1
            while j < len(lines):
                if lines[j].strip() and not lines[j].startswith(" " * (indent + 1)):
                    break
                j += 1

            # Comment out the old function
            for k in range(i, j):
                if not lines[k].strip().startswith("#"):
                    lines[k] = "# " + lines[k]

            # Add the refactored version
            lines.insert(j, "\\n# REFACTORED VERSION\\n")
            lines.insert(j + 1, "ai_improve_all_options = ai_improve_all_options_refactored\\n")
            changes_made.append(f"Line {i+1}-{j}: Replaced ai_improve_all_options with refactored version")

        # Replace ai_edit_options
        if "def ai_edit_options(mcq" in line:
            # Find the end of the function
            indent = len(line) - len(line.lstrip())
            j = i + 1
            while j < len(lines):
                if lines[j].strip() and not lines[j].startswith(" " * (indent + 1)):
                    break
                j += 1

            # Comment out the old function
            for k in range(i, j):
                if not lines[k].strip().startswith("#"):
                    lines[k] = "# " + lines[k]

            # Add the refactored version
            lines.insert(j, "\\n# REFACTORED VERSION\\n")
            lines.insert(j + 1, "ai_edit_options = ai_edit_options_refactored\\n")
            changes_made.append(f"Line {i+1}-{j}: Replaced ai_edit_options with refactored version")

    # Write the file
    if changes_made:
        print(f"\\nWriting {len(changes_made)} changes to {file_path}...")
        with open(file_path, 'w') as f:
            f.writelines(lines)

        print("\\nChanges applied:")
        for change in changes_made:
            print(f"  ✓ {change}")

        return True
    else:
        print("\\nNo changes needed")
        return True


if __name__ == "__main__":
    success = apply_refactor()
    sys.exit(0 if success else 1)
'''

    with open("apply_options_refactor.py", 'w') as f:
        f.write(patch_content)

    return "apply_options_refactor.py"


def main():
    """Main function to generate the refactored code"""

    print("="*60)
    print("OPTIONS EDITING REFACTOR")
    print("="*60)
    print()
    print("Problem identified:")
    print("  • Options editing uses JSON schema format")
    print("  • GPT-5-nano returns empty responses with JSON schema")
    print("  • Verbosity settings not working correctly")
    print()
    print("Solution:")
    print("  • Use TEXT response instead of JSON schema")
    print("  • Parse options manually from text")
    print("  • Similar approach to working question/explanation editing")
    print()

    # Generate the refactored code
    refactored_code = create_refactored_options_functions()

    # Save to file
    with open("options_editing_refactored.py", 'w') as f:
        f.write(refactored_code)

    print("Generated files:")
    print("  ✓ options_editing_refactored.py - Refactored functions")

    # Create patch file
    patch_file = create_patch_file()
    print(f"  ✓ {patch_file} - Apply patch script")

    print()
    print("To apply the fix:")
    print("  1. Review: cat options_editing_refactored.py")
    print("  2. Apply: python apply_options_refactor.py")
    print("  3. Deploy: git push heroku main")

    return 0


if __name__ == "__main__":
    sys.exit(main())
'''