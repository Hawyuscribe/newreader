#!/usr/bin/env python3
"""
Fix the import error in ai_edit_options_direct by removing the non-existent import
and using a simpler inline approach.
"""

import os
import sys
import shutil
from datetime import datetime


def fix_import_error():
    """Remove the problematic import and fix the function"""

    file_path = "django_neurology_mcq/mcq/openai_integration.py"

    if not os.path.exists(file_path):
        print(f"❌ Error: {file_path} not found")
        return False

    print(f"Fixing import error in {file_path}...")

    # Create backup
    backup_path = f"{file_path}.backup.{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    shutil.copy2(file_path, backup_path)
    print(f"✓ Created backup: {backup_path}")

    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()

        # Remove the problematic import line
        new_lines = []
        for line in lines:
            if "from .options_editing_fix import" in line:
                print("✓ Removed problematic import")
                continue  # Skip this line
            new_lines.append(line)

        # Write back
        with open(file_path, 'w') as f:
            f.writelines(new_lines)

        print("✓ Fixed import error")

        # Now update the ai_edit_options_direct function to not use those imports
        with open(file_path, 'r') as f:
            content = f.read()

        # Replace references to parse_text_options with inline parsing
        if "parse_text_options" in content:
            content = content.replace(
                "improved = parse_text_options(response_text, current_options, correct_answer)",
                """# Parse the text response into options inline
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
                    break"""
            )

        # Replace references to create_fallback_options
        if "create_fallback_options" in content:
            content = content.replace(
                "return create_fallback_options(question_text, correct_answer, current_options.get(correct_answer, \"\"))",
                "return current_options  # Return original options as fallback"
            )

        with open(file_path, 'w') as f:
            f.write(content)

        print("✓ Updated function to use inline parsing")
        return True

    except Exception as e:
        print(f"❌ Error: {e}")
        print(f"Restoring from backup: {backup_path}")
        shutil.copy2(backup_path, file_path)
        return False


def main():
    print("="*60)
    print("FIXING OPTIONS IMPORT ERROR")
    print("="*60)

    if fix_import_error():
        print("\n✅ Successfully fixed import error!")
        print("\nNext steps:")
        print("  1. Commit: git add . && git commit -m 'Fix import error in options editing'")
        print("  2. Deploy: git push heroku main")
        return 0
    else:
        print("\n❌ Failed to fix import error")
        return 1


if __name__ == "__main__":
    sys.exit(main())