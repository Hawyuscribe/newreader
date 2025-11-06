#!/usr/bin/env python3
"""
Fix the 503 error in job status checking by correcting the cache key mismatch.

The issue: Options editing stores cache with underscore (ai_job_) but
job status endpoint looks for colon (ai_job:).
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


def fix_cache_key_mismatch():
    """Fix the cache key format mismatch in views.py"""

    file_path = "django_neurology_mcq/mcq/views.py"

    if not os.path.exists(file_path):
        print(f"❌ Error: {file_path} not found")
        return False

    print(f"Fixing cache key mismatch in {file_path}...")

    # Create backup
    backup_path = backup_file(file_path)

    try:
        with open(file_path, 'r') as f:
            content = f.read()

        # Track replacements
        replacements_made = 0

        # Fix cache key format in options editing (underscore to colon)
        # Line 4172: cache.set(f'ai_job_{job_id}', result, timeout=300)
        old_pattern1 = "cache.set(f'ai_job_{job_id}'"
        new_pattern1 = "cache.set(f'ai_job:{job_id}'"
        if old_pattern1 in content:
            content = content.replace(old_pattern1, new_pattern1)
            replacements_made += 1
            print(f"✓ Fixed cache key format for successful job storage")

        # Line 4190: cache.set(f'ai_job_{job_id}', error_result, timeout=300)
        old_pattern2 = "cache.set(f'ai_job_{job_id}', error_result"
        new_pattern2 = "cache.set(f'ai_job:{job_id}', error_result"
        if old_pattern2 in content:
            content = content.replace(old_pattern2, new_pattern2)
            replacements_made += 1
            print(f"✓ Fixed cache key format for error job storage")

        if replacements_made == 0:
            print("⚠️ No cache key mismatches found - may already be fixed")

        # Write the fixed content back
        with open(file_path, 'w') as f:
            f.write(content)

        print(f"✓ Successfully fixed {replacements_made} cache key patterns")
        return True

    except Exception as e:
        print(f"❌ Error during fixing: {e}")
        print(f"Restoring from backup: {backup_path}")
        shutil.copy2(backup_path, file_path)
        return False


def verify_fix():
    """Verify that the fix was applied correctly"""

    file_path = "django_neurology_mcq/mcq/views.py"

    with open(file_path, 'r') as f:
        content = f.read()

    # Check that underscore pattern is gone
    has_underscore = "ai_job_{job_id}" in content
    # Check that colon pattern exists in options editing area
    has_colon = "ai_job:{job_id}" in content

    print("\nVerification:")
    if has_underscore:
        print("  ❌ Still has underscore pattern (ai_job_)")
        return False
    else:
        print("  ✓ Underscore pattern removed")

    if has_colon:
        print("  ✓ Colon pattern present (ai_job:)")
    else:
        print("  ⚠️ Colon pattern not found")

    return not has_underscore


def main():
    """Main function"""
    print("="*60)
    print("FIXING JOB STATUS 503 ERROR")
    print("="*60)
    print("\nProblem: Cache key mismatch causing job status lookup failure")
    print("  • Options editing stores: ai_job_{job_id}")
    print("  • Job status looks for: ai_job:{job_id}")
    print("\nSolution: Standardize to use colon format")
    print()

    # Apply the fix
    if fix_cache_key_mismatch():
        # Verify
        if verify_fix():
            print("\n✅ Fix applied and verified successfully!")
            print("\nThe 503 error should now be resolved.")
            print("\nNext steps:")
            print("  1. Test locally to confirm the fix")
            print("  2. Deploy to Heroku:")
            print("     git add .")
            print("     git commit -m 'Fix 503 error: Correct cache key mismatch in job status'")
            print("     git push heroku main")
            return 0
        else:
            print("\n⚠️ Fix applied but verification shows issues")
            return 1
    else:
        print("\n❌ Failed to apply fix")
        return 1


if __name__ == "__main__":
    sys.exit(main())