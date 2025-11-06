#!/usr/bin/env python3
"""
Patch the options editing functions to use text-based approach
This fixes the empty JSON issue with GPT-5-nano
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


def patch_options_editing():
    """Apply the text-based patch to options editing functions"""

    file_path = "django_neurology_mcq/mcq/openai_integration.py"

    if not os.path.exists(file_path):
        print(f"❌ Error: {file_path} not found")
        return False

    print(f"Patching {file_path} to fix options editing...")

    # Create backup
    backup_path = backup_file(file_path)

    try:
        # Read the file
        with open(file_path, 'r') as f:
            content = f.read()

        # Check if already patched
        if "# PATCHED: Using text-based approach" in content:
            print("✓ File already patched")
            return True

        # Find the _improve_all_options_with_model function
        import_section = """import time
import re
from .options_editing_fix import parse_text_options, create_fallback_options
"""

        # Add imports at the top if not present
        if "from .options_editing_fix import" not in content:
            # Find a good place to add the import
            import_pos = content.find("from typing import")
            if import_pos > 0:
                # Find the end of the import block
                next_line = content.find("\n\n", import_pos)
                if next_line > 0:
                    content = content[:next_line] + "\n" + import_section + content[next_line:]
                    print("✓ Added import for options_editing_fix")

        # Now patch the _improve_all_options_with_model function
        patch_code = '''

# PATCHED: Using text-based approach for GPT-5-nano compatibility
def _improve_all_options_with_model_patched(mcq, custom_instructions: str, model_name: str) -> dict:
    """
    PATCHED VERSION: Uses text response instead of JSON schema to avoid empty responses.
    """
    if not api_key or not client:
        logger.info("Using original options due to unavailable OpenAI API")
        return mcq.get_options_dict() if hasattr(mcq, 'get_options_dict') else {}

    try:
        mcq_id = getattr(mcq, "id", "unknown")
        logger.info("AI improving options for MCQ #%s using %s (TEXT mode)", mcq_id, model_name)

        question_text = getattr(mcq, "question_text", "")
        current_options = mcq.get_options_dict() if hasattr(mcq, "get_options_dict") else {}
        correct_answer = getattr(mcq, "correct_answer", "A")
        explanation = getattr(mcq, "explanation", "")[:300]

        # Build TEXT-BASED prompt (not JSON schema)
        system_prompt = "You are a medical educator. Improve MCQ options to be educationally valuable. Output exactly 4 options in format: A) text, B) text, C) text, D) text"

        current_text = "\\n".join(f"{k}) {v}" for k, v in sorted(current_options.items()))

        user_prompt = f"""Question: {question_text}

Current options:
{current_text}

Correct answer: {correct_answer}
Context: {explanation[:200] if explanation else 'Medical MCQ'}

Task: Improve all options. Keep option {correct_answer} unchanged. Make wrong options plausible but incorrect.
{f"Instructions: {custom_instructions}" if custom_instructions else ""}

Output improved options:"""

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]

        # Use TEXT response, not JSON schema
        response = _responses_create(
            model_name,
            messages,
            response_format={"type": "text"},  # TEXT not JSON!
            max_output_tokens=300,
            temperature=0.3,
            top_p=0.8,
            use_vector=False,
            timeout=OPTION_REQUEST_TIMEOUT,
        )

        response_text = _extract_response_text(response)

        if not response_text:
            logger.warning(f"Empty response from {model_name} for MCQ #{mcq_id}")
            return create_fallback_options(question_text, correct_answer, current_options.get(correct_answer, ""))

        # Parse text into options
        improved = parse_text_options(response_text, current_options, correct_answer)

        logger.info(f"Successfully improved options for MCQ #{mcq_id}")
        return improved

    except Exception as e:
        logger.error(f"Error in patched options improvement: {str(e)}")
        return mcq.get_options_dict() if hasattr(mcq, 'get_options_dict') else {}

# Replace the original function
_improve_all_options_with_model = _improve_all_options_with_model_patched
'''

        # Add the patched function
        if "_improve_all_options_with_model_patched" not in content:
            # Find where to add it (after the original function)
            pos = content.find("def ai_improve_all_options(")
            if pos > 0:
                # Find the start of this function
                content = content[:pos] + patch_code + "\n\n" + content[pos:]
                print("✓ Added patched options improvement function")

        # Write the patched file
        with open(file_path, 'w') as f:
            f.write(content)

        print("\n✅ Successfully patched options editing!")
        print("\nChanges made:")
        print("  • Added text-based response instead of JSON schema")
        print("  • Added robust text parsing")
        print("  • Added fallback options generation")
        print("  • Reduced temperature to 0.3 for consistency")
        print("  • Simplified prompts for GPT-5-nano")

        return True

    except Exception as e:
        print(f"\n❌ Error during patching: {e}")
        print(f"Restoring from backup: {backup_path}")
        shutil.copy2(backup_path, file_path)
        return False


def verify_patch():
    """Verify the patch was applied correctly"""
    file_path = "django_neurology_mcq/mcq/openai_integration.py"

    with open(file_path, 'r') as f:
        content = f.read()

    checks = [
        ("Text-based approach", "PATCHED: Using text-based approach" in content),
        ("Parse function import", "parse_text_options" in content or "_improve_all_options_with_model_patched" in content),
        ("Text response format", '"type": "text"' in content),
    ]

    print("\nVerification:")
    all_good = True
    for check_name, result in checks:
        if result:
            print(f"  ✓ {check_name}")
        else:
            print(f"  ❌ {check_name}")
            all_good = False

    return all_good


def main():
    """Main function"""
    print("="*60)
    print("OPTIONS EDITING PATCH FOR GPT-5-NANO")
    print("="*60)
    print("\nThis patch fixes the empty JSON issue by:")
    print("  • Using TEXT response instead of JSON schema")
    print("  • Parsing options from text manually")
    print("  • Adding robust fallback mechanisms")
    print()

    # Apply the patch
    success = patch_options_editing()

    if success:
        # Verify
        if verify_patch():
            print("\n✅ Patch applied and verified successfully!")
            print("\nNext steps:")
            print("  1. Test locally: python test_gpt5_nano_fixed.py")
            print("  2. Commit: git add . && git commit -m 'Fix options editing empty JSON'")
            print("  3. Deploy: git push heroku main")
            return 0
        else:
            print("\n⚠️ Patch applied but verification failed")
            return 1
    else:
        print("\n❌ Patch failed")
        return 1


if __name__ == "__main__":
    sys.exit(main())