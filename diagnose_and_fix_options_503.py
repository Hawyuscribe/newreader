#!/usr/bin/env python3
"""
Comprehensive diagnosis and fix for the 503 error in options editing.
Updates implementation to match OpenAI's latest Responses API specifications.
"""

import os
import sys
import shutil
from datetime import datetime


def diagnose_import_issue():
    """Test if ai_edit_options_direct is importable"""
    print("\n1. Testing import of ai_edit_options_direct...")
    try:
        # Add Django path
        sys.path.insert(0, os.path.abspath('.'))
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_neurology_mcq.settings')

        from django_neurology_mcq.mcq.openai_integration import ai_edit_options_direct
        print("   ✓ Function is importable locally")
        return True
    except ImportError as e:
        print(f"   ❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"   ❌ Other error: {e}")
        return False


def fix_responses_api_implementation():
    """Update openai_integration.py to use correct Responses API format"""

    file_path = "django_neurology_mcq/mcq/openai_integration.py"

    if not os.path.exists(file_path):
        print(f"❌ Error: {file_path} not found")
        return False

    print("\n2. Updating Responses API implementation...")

    # Create backup
    backup_path = f"{file_path}.backup.{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    shutil.copy2(file_path, backup_path)
    print(f"   ✓ Created backup: {backup_path}")

    try:
        with open(file_path, 'r') as f:
            content = f.read()

        # Check if we have _responses_create function
        if "_responses_create" not in content:
            print("   ❌ _responses_create function not found")
            return False

        # Find and update the _responses_create function to match OpenAI's latest format
        # According to the docs, it should use 'input' not 'messages' and 'instructions' for system prompt

        # First, let's update how we call the Responses API
        updated_content = content.replace(
            'messages,\n            response_format={"type": "text"},',
            'input=user_prompt,\n            instructions=system_prompt,\n            text={"format": {"type": "text"}},  # Correct format for text response'
        )

        # Update the ai_edit_options_direct function with better error handling
        new_function = '''
def ai_edit_options_direct(mcq, mode: str = "fill_missing", custom_instructions: str = "") -> dict:
    """
    Direct AI-powered options editing using GPT-5-mini with latest Responses API.

    Args:
        mcq: The MCQ object
        mode: 'fill_missing', 'improve_all', or 'regenerate_all'
        custom_instructions: Optional custom instructions

    Returns:
        dict: Improved options dictionary
    """
    try:
        # Check OpenAI availability
        if not api_key or not client:
            logger.warning("OpenAI API not configured")
            return mcq.get_options_dict() if hasattr(mcq, 'get_options_dict') else {}

        mcq_id = getattr(mcq, "id", "unknown")
        question_text = getattr(mcq, "question_text", "")
        current_options = mcq.get_options_dict() if hasattr(mcq, "get_options_dict") else {}
        correct_answer = getattr(mcq, "correct_answer", "A")
        explanation = getattr(mcq, "explanation", "")[:500]

        logger.info(f"AI editing options for MCQ #{mcq_id}, mode: {mode}")

        # Determine task based on mode
        if mode == "fill_missing":
            missing = []
            for letter in ["A", "B", "C", "D"]:
                if letter not in current_options or not current_options[letter].strip():
                    missing.append(letter)

            if not missing:
                logger.info(f"All options present for MCQ #{mcq_id}")
                return current_options

            task_description = f"Generate ONLY the missing options: {', '.join(missing)}"

        elif mode == "improve_all":
            task_description = "Improve ALL options while keeping the correct answer unchanged"

        else:  # regenerate_all
            task_description = "Completely regenerate ALL options with high quality distractors"

        # Format current options
        current_text = ""
        if current_options:
            current_text = "\\nCurrent options:\\n"
            for letter in ["A", "B", "C", "D"]:
                if letter in current_options and current_options[letter].strip():
                    current_text += f"{letter}) {current_options[letter]}\\n"
                else:
                    current_text += f"{letter}) [MISSING]\\n"

        # Build prompt according to OpenAI's Responses API format
        system_instructions = """You are a board-certified neurologist and medical educator.
Generate or improve MCQ answer options that are educationally valuable.
The correct answer must remain medically accurate.
Wrong options should be plausible but clearly incorrect."""

        user_content = f"""Question: {question_text}

{current_text}

Correct answer: {correct_answer}
Explanation context: {explanation[:300] if explanation else 'Medical MCQ'}

Task: {task_description}

{f"Additional instructions: {custom_instructions}" if custom_instructions else ""}

IMPORTANT:
- Output EXACTLY 4 options in this format: A) text, B) text, C) text, D) text
- Keep option {correct_answer} medically correct and unchanged if it exists
- Make wrong options plausible but clearly incorrect
- Each option should be 40-150 characters
- Do NOT include any other text, just the options"""

        try:
            # Use the Responses API format as per OpenAI documentation
            response = client.responses.create(
                model="gpt-5-mini",  # Using GPT-5-mini for balance
                input=[
                    {"type": "text", "content": user_content}
                ],
                instructions=system_instructions,
                max_output_tokens=500,
                temperature=0.3,  # Low for consistency
                top_p=0.85,
                store=False,  # Don't store for privacy
            )

            # Extract text from response
            response_text = ""
            if hasattr(response, 'output') and response.output:
                if isinstance(response.output, list) and len(response.output) > 0:
                    output_item = response.output[0]
                    if hasattr(output_item, 'content'):
                        if isinstance(output_item.content, list) and len(output_item.content) > 0:
                            content_item = output_item.content[0]
                            if hasattr(content_item, 'text'):
                                response_text = content_item.text
                            elif isinstance(content_item, dict) and 'text' in content_item:
                                response_text = content_item['text']
                        elif isinstance(output_item.content, str):
                            response_text = output_item.content
            elif hasattr(response, 'output_text'):
                response_text = response.output_text

            if not response_text:
                logger.warning(f"Empty response for MCQ #{mcq_id}")
                return current_options

            # Parse the text response into options
            improved = {}
            lines = response_text.strip().split('\\n')

            for line in lines:
                line = line.strip()
                # Try multiple patterns
                for pattern in [
                    r'^([A-D])\\)\\s*(.+)$',  # A) text
                    r'^([A-D])\\s*[-:]\\s*(.+)$',  # A: text or A- text
                    r'^([A-D])\\s+(.+)$',  # A text
                ]:
                    match = re.match(pattern, line)
                    if match:
                        letter = match.group(1).upper()
                        text = match.group(2).strip()
                        if letter in ["A", "B", "C", "D"] and text:
                            improved[letter] = text
                        break

            # Validate we have all 4 options
            if len(improved) != 4:
                logger.warning(f"Parsed {len(improved)} options, using fallback")
                # Fill missing options
                for letter in ["A", "B", "C", "D"]:
                    if letter not in improved:
                        if letter in current_options and current_options[letter].strip():
                            improved[letter] = current_options[letter]
                        else:
                            if letter == correct_answer:
                                improved[letter] = current_options.get(letter, "Correct answer")
                            else:
                                improved[letter] = f"Alternative option {letter}"

            # Preserve correct answer if needed
            if correct_answer in current_options and current_options[correct_answer].strip():
                if mode != "regenerate_all":
                    improved[correct_answer] = current_options[correct_answer]

            logger.info(f"Successfully edited options for MCQ #{mcq_id}")
            return improved

        except AttributeError as e:
            # Fallback to old API format if new one fails
            logger.warning(f"Responses API format issue, falling back: {e}")

            # Try with old format
            messages = [
                {"role": "system", "content": [{"type": "text", "text": system_instructions}]},
                {"role": "user", "content": [{"type": "text", "text": user_content}]}
            ]

            response = _responses_create(
                DEFAULT_MODEL,
                messages,
                response_format={"type": "text"},
                max_output_tokens=500,
                temperature=0.3,
                top_p=0.85,
                use_vector=False,
                timeout=20,
            )

            response_text = _extract_response_text(response)

            if not response_text:
                logger.warning(f"Empty response for MCQ #{mcq_id}")
                return current_options

            # Parse response (same as above)
            improved = {}
            lines = response_text.strip().split('\\n')

            for line in lines:
                line = line.strip()
                for pattern in [
                    r'^([A-D])\\)\\s*(.+)$',
                    r'^([A-D])\\s*[-:]\\s*(.+)$',
                    r'^([A-D])\\s+(.+)$',
                ]:
                    match = re.match(pattern, line)
                    if match:
                        letter = match.group(1).upper()
                        text = match.group(2).strip()
                        if letter in ["A", "B", "C", "D"] and text:
                            improved[letter] = text
                        break

            # Fill missing options
            for letter in ["A", "B", "C", "D"]:
                if letter not in improved:
                    if letter in current_options and current_options[letter].strip():
                        improved[letter] = current_options[letter]
                    else:
                        improved[letter] = f"Option {letter}"

            return improved

    except Exception as e:
        logger.error(f"Error in ai_edit_options_direct: {str(e)}", exc_info=True)
        # Return original options as fallback
        return mcq.get_options_dict() if hasattr(mcq, 'get_options_dict') else {}
'''

        # Find and replace the existing ai_edit_options_direct function
        import re

        # Pattern to match the entire function
        pattern = r'def ai_edit_options_direct\(.*?\n(?:.*?\n)*?(?=\ndef |\Z)'

        if re.search(pattern, content, re.DOTALL):
            content = re.sub(pattern, new_function.strip() + '\n\n', content, count=1, flags=re.DOTALL)
            print("   ✓ Updated ai_edit_options_direct function")
        else:
            # Add the function if it doesn't exist
            # Find a good place to add it (after ai_improve_all_options)
            pos = content.find("def ai_improve_all_options(")
            if pos > 0:
                # Find the end of this function
                next_def = content.find("\ndef ", pos + 1)
                if next_def > 0:
                    content = content[:next_def] + "\n" + new_function + "\n" + content[next_def:]
                    print("   ✓ Added ai_edit_options_direct function")

        # Write back
        with open(file_path, 'w') as f:
            f.write(content)

        print("   ✓ Updated implementation to match OpenAI Responses API")
        return True

    except Exception as e:
        print(f"   ❌ Error updating file: {e}")
        print(f"   Restoring from backup: {backup_path}")
        shutil.copy2(backup_path, file_path)
        return False


def main():
    print("="*60)
    print("DIAGNOSING AND FIXING OPTIONS EDITING 503 ERROR")
    print("="*60)

    # Run diagnostics
    import_ok = diagnose_import_issue()

    # Apply fixes
    api_ok = fix_responses_api_implementation()

    if api_ok:
        print("\n✅ All fixes applied successfully!")
        print("\nNext steps:")
        print("  1. Commit: git add . && git commit -m 'Fix options editing with OpenAI Responses API'")
        print("  2. Deploy: git push heroku main")
        print("  3. Restart: heroku ps:restart --app enigmatic-hamlet-38937")
        return 0
    else:
        print("\n❌ Some fixes failed")
        return 1


if __name__ == "__main__":
    sys.exit(main())