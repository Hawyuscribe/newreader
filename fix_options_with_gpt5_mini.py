#!/usr/bin/env python3
"""
Fix options editing by copying the working question editing approach.
Uses GPT-5-mini and direct calls (no async/modal), exactly like question editing.
"""

import os
import sys
import shutil
from datetime import datetime


def backup_file(file_path):
    """Create a backup of the original file"""
    backup_path = f"{file_path}.backup.{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    shutil.copy2(file_path, backup_path)
    print(f"✓ Created backup: {backup_path}")
    return backup_path


def patch_openai_integration():
    """Add new ai_edit_options_direct function that works like ai_edit_question"""

    file_path = "django_neurology_mcq/mcq/openai_integration.py"

    if not os.path.exists(file_path):
        print(f"❌ Error: {file_path} not found")
        return False

    print(f"Patching {file_path} with new options editing function...")

    # Create backup
    backup_path = backup_file(file_path)

    try:
        # Read the file
        with open(file_path, 'r') as f:
            content = f.read()

        # Check if already patched
        if "def ai_edit_options_direct" in content:
            print("✓ File already contains the new function")
            return True

        # Find where to add the new function (after ai_edit_question)
        insert_pos = content.find("def ai_improve_all_options(")
        if insert_pos < 0:
            # Try another location
            insert_pos = content.find("def ai_edit_options(")

        if insert_pos < 0:
            print("❌ Could not find insertion point")
            return False

        # New function that works like ai_edit_question but for options
        new_function = '''

def ai_edit_options_direct(mcq, mode: str = "fill_missing", custom_instructions: str = "") -> dict:
    """
    Direct AI-powered options editing using GPT-5-mini (no async/modal).
    Works exactly like ai_edit_question but for options.

    Args:
        mcq: The MCQ object
        mode: 'fill_missing', 'improve_all', or 'regenerate_all'
        custom_instructions: Optional custom instructions

    Returns:
        dict: Improved options dictionary
    """
    if not api_key or not client:
        logger.info("Using original options due to unavailable OpenAI API")
        return mcq.get_options_dict() if hasattr(mcq, 'get_options_dict') else {}

    mcq_id = getattr(mcq, "id", "unknown")
    question_text = getattr(mcq, "question_text", "")
    current_options = mcq.get_options_dict() if hasattr(mcq, "get_options_dict") else {}
    correct_answer = getattr(mcq, "correct_answer", "A")
    explanation = getattr(mcq, "explanation", "")[:500]

    logger.info(f"AI editing options for MCQ #{mcq_id}, mode: {mode} using GPT-5-mini")

    # Determine what we need to do based on mode
    if mode == "fill_missing":
        # Find missing options
        missing = []
        for letter in ["A", "B", "C", "D"]:
            if letter not in current_options or not current_options[letter].strip():
                missing.append(letter)

        if not missing:
            logger.info(f"All options already present for MCQ #{mcq_id}")
            return current_options

        task_description = f"Generate ONLY the missing options: {', '.join(missing)}"

    elif mode == "improve_all":
        task_description = "Improve ALL options while keeping the correct answer unchanged"

    else:  # regenerate_all
        task_description = "Completely regenerate ALL options with high quality distractors"

    # Build the prompt (similar to ai_edit_question but for options)
    system_prompt = """You are a board-certified neurologist and medical educator.
Generate or improve MCQ answer options that are educationally valuable.
The correct answer must remain medically accurate.
Wrong options should be plausible but clearly incorrect."""

    # Format current options if available
    current_text = ""
    if current_options:
        current_text = "\\nCurrent options:\\n"
        for letter in ["A", "B", "C", "D"]:
            if letter in current_options and current_options[letter].strip():
                current_text += f"{letter}) {current_options[letter]}\\n"
            else:
                current_text += f"{letter}) [MISSING]\\n"

    user_prompt = f"""Question: {question_text}

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

    messages = [
        {"role": "system", "content": [{"type": "text", "text": system_prompt}]},
        {"role": "user", "content": [{"type": "text", "text": user_prompt}]}
    ]

    try:
        # Use GPT-5-mini like ai_edit_question does (DEFAULT_MODEL)
        response = _responses_create(
            DEFAULT_MODEL,  # This is GPT-5-mini!
            messages,
            response_format={"type": "text"},  # Simple text, no JSON schema
            max_output_tokens=500,
            temperature=0.3,  # Low for consistency
            top_p=0.85,
            use_vector=False,  # No vector store needed for options
            timeout=20,
        )

        response_text = _extract_response_text(response)

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
            logger.warning(f"Parsed {len(improved)} options, expected 4. Using fallback.")
            # Fill in missing options
            for letter in ["A", "B", "C", "D"]:
                if letter not in improved:
                    if letter in current_options and current_options[letter].strip():
                        improved[letter] = current_options[letter]
                    else:
                        # Generate a simple fallback
                        if letter == correct_answer:
                            improved[letter] = current_options.get(letter, "Correct answer (see explanation)")
                        else:
                            improved[letter] = f"Alternative option {letter}"

        # Ensure correct answer is preserved if it existed
        if correct_answer in current_options and current_options[correct_answer].strip():
            if mode != "regenerate_all":
                improved[correct_answer] = current_options[correct_answer]

        logger.info(f"Successfully edited options for MCQ #{mcq_id} using GPT-5-mini")
        return improved

    except Exception as e:
        logger.error(f"Error in ai_edit_options_direct: {str(e)}")
        return current_options

'''

        # Insert the new function
        content = content[:insert_pos] + new_function + "\n\n" + content[insert_pos:]

        # Write the patched file
        with open(file_path, 'w') as f:
            f.write(content)

        print("✓ Added ai_edit_options_direct function to openai_integration.py")
        return True

    except Exception as e:
        print(f"❌ Error during patching: {e}")
        print(f"Restoring from backup: {backup_path}")
        shutil.copy2(backup_path, file_path)
        return False


def patch_views():
    """Update views.py to use the new direct function instead of async"""

    file_path = "django_neurology_mcq/mcq/views.py"

    if not os.path.exists(file_path):
        print(f"❌ Error: {file_path} not found")
        return False

    print(f"Patching {file_path} to use direct options editing...")

    # Create backup
    backup_path = backup_file(file_path)

    try:
        # Read the file
        with open(file_path, 'r') as f:
            lines = f.readlines()

        # Find and replace the ai_edit_mcq_options function
        in_function = False
        function_start = -1
        function_end = -1
        indent_level = 0

        for i, line in enumerate(lines):
            if "def ai_edit_mcq_options(request, mcq_id):" in line:
                function_start = i
                in_function = True
                indent_level = len(line) - len(line.lstrip())
            elif in_function:
                current_indent = len(line) - len(line.lstrip())
                # Check if we've reached the next function at the same indent level
                if line.strip().startswith("def ") and current_indent == indent_level:
                    function_end = i
                    break

        if function_start < 0:
            print("❌ Could not find ai_edit_mcq_options function")
            return False

        if function_end < 0:
            function_end = len(lines)

        # Create the new function (similar to ai_edit_mcq_question)
        new_function_lines = [
            "@staff_required_json\n",
            "@require_POST\n",
            "def ai_edit_mcq_options(request, mcq_id):\n",
            '    """Use AI to improve MCQ options (direct call like question editing)"""\n',
            "    import logging\n",
            "    logger = logging.getLogger(__name__)\n",
            "    \n",
            "    mcq = get_object_or_404(MCQ, id=mcq_id)\n",
            "    \n",
            "    try:\n",
            "        data = json.loads(request.body)\n",
            "        mode = data.get('mode', 'fill_missing')\n",
            "        custom_instructions = data.get('custom_instructions', '').strip()\n",
            "        \n",
            "        logger.info(f\"AI edit options request for MCQ #{mcq_id}, mode: {mode}\")\n",
            "        \n",
            "        # Import the new direct function\n",
            "        from .openai_integration import ai_edit_options_direct, api_key, client\n",
            "        \n",
            "        # Check if OpenAI is available\n",
            "        if not api_key or not client:\n",
            "            return JsonResponse({\n",
            "                'success': False,\n",
            "                'error': 'OpenAI API is not configured.'\n",
            "            }, status=503)\n",
            "        \n",
            "        # Get AI-improved options (direct call, no async)\n",
            "        improved_options = ai_edit_options_direct(mcq, mode, custom_instructions)\n",
            "        \n",
            "        # Check for auto-regenerate explanations\n",
            "        auto_regenerate = data.get('auto_regenerate_explanations', True)\n",
            "        improved_explanations = None\n",
            "        \n",
            "        if auto_regenerate:\n",
            "            from .openai_integration import regenerate_unified_explanation\n",
            "            try:\n",
            "                # Update MCQ options temporarily for explanation generation\n",
            "                original_options = mcq.options\n",
            "                mcq.options = json.dumps(improved_options)\n",
            "                \n",
            "                improved_explanations = regenerate_unified_explanation(mcq)\n",
            "                \n",
            "                # Restore original options\n",
            "                mcq.options = original_options\n",
            "                \n",
            "                logger.info(f\"Regenerated explanations for MCQ #{mcq_id}\")\n",
            "            except Exception as e:\n",
            "                logger.warning(f\"Failed to regenerate explanations: {e}\")\n",
            "        \n",
            "        logger.info(f\"AI edit options successful for MCQ #{mcq_id}\")\n",
            "        \n",
            "        return JsonResponse({\n",
            "            'success': True,\n",
            "            'improved_options': improved_options,\n",
            "            'improved_explanations': improved_explanations,\n",
            "            'message': f'AI has improved options using mode: {mode}'\n",
            "        })\n",
            "        \n",
            "    except json.JSONDecodeError as e:\n",
            "        logger.error(f\"JSON decode error in ai_edit_mcq_options: {e}\")\n",
            "        return JsonResponse({'error': 'Invalid JSON data'}, status=400)\n",
            "    except ValueError as e:\n",
            "        logger.error(f\"Value error in ai_edit_mcq_options for MCQ #{mcq_id}: {e}\")\n",
            "        return JsonResponse({'success': False, 'error': str(e)})\n",
            "    except Exception as e:\n",
            "        logger.error(f\"Error in ai_edit_mcq_options for MCQ #{mcq_id}: {e}\", exc_info=True)\n",
            "        return JsonResponse({'error': f'Error: {str(e)}'}, status=500)\n",
            "\n\n"
        ]

        # Replace the function
        new_lines = lines[:function_start-2] + new_function_lines + lines[function_end:]

        # Write the patched file
        with open(file_path, 'w') as f:
            f.writelines(new_lines)

        print("✓ Updated ai_edit_mcq_options in views.py to use direct calls")
        return True

    except Exception as e:
        print(f"❌ Error during patching: {e}")
        print(f"Restoring from backup: {backup_path}")
        shutil.copy2(backup_path, file_path)
        return False


def main():
    """Main function"""
    print("="*60)
    print("FIXING OPTIONS EDITING WITH GPT-5-MINI")
    print("="*60)
    print("\nThis fix:")
    print("  • Uses GPT-5-mini (like question editing)")
    print("  • Direct calls (no async/modal)")
    print("  • Simple text response (no JSON schema)")
    print("  • Same approach as working question editing")
    print()

    # Patch openai_integration.py
    success1 = patch_openai_integration()

    # Patch views.py
    success2 = patch_views()

    if success1 and success2:
        print("\n✅ Successfully patched both files!")
        print("\nNext steps:")
        print("  1. Test locally: python test_gpt5_mini_options.py")
        print("  2. Commit: git add . && git commit -m 'Fix options editing with GPT-5-mini'")
        print("  3. Deploy: git push heroku main")
        print("  4. Restart workers: heroku ps:restart --process-type worker --app enigmatic-hamlet-38937")
        return 0
    else:
        print("\n⚠️ Partial patching completed. Check errors above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())