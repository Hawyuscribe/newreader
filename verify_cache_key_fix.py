#!/usr/bin/env python3
"""
Simple verification that the cache key fix was applied correctly.
No Django setup required - just checks the code.
"""

import re


def verify_fix():
    """Check that the cache key fix was applied to views.py"""
    print("\n" + "="*60)
    print("VERIFYING CACHE KEY FIX IN views.py")
    print("="*60)

    file_path = "django_neurology_mcq/mcq/views.py"

    with open(file_path, 'r') as f:
        content = f.read()

    print("\nChecking cache key patterns in options editing code...")

    # Find the ai_edit_mcq_options function area (around line 4100-4200)
    # Look for cache.set patterns
    cache_set_patterns = re.findall(r"cache\.set\(f['\"]ai_job[_:]\{job_id\}", content)

    underscore_count = 0
    colon_count = 0

    for pattern in cache_set_patterns:
        if "ai_job_{job_id}" in pattern:
            underscore_count += 1
            print(f"  ❌ Found underscore pattern: {pattern}")
        elif "ai_job:{job_id}" in pattern:
            colon_count += 1
            print(f"  ✓ Found colon pattern: {pattern}")

    # Check job status functions use colon
    job_status_patterns = re.findall(r'cache\.get\(f["\']ai_job[_:]\{job_id\}', content)

    print("\nChecking job status retrieval patterns...")
    for pattern in job_status_patterns:
        if "ai_job_{job_id}" in pattern:
            print(f"  ❌ Job status uses underscore: {pattern}")
        elif "ai_job:{job_id}" in pattern:
            print(f"  ✓ Job status uses colon: {pattern}")

    # Final verdict
    print("\n" + "="*60)
    print("RESULTS:")
    print("="*60)

    if underscore_count == 0 and colon_count > 0:
        print("✅ FIX VERIFIED SUCCESSFULLY!")
        print(f"   • All cache.set calls use colon format (found {colon_count})")
        print("   • No underscore patterns remaining")
        print("\nThe 503 error should now be resolved because:")
        print("  1. Options editing stores with: ai_job:{job_id}")
        print("  2. Job status retrieves with: ai_job:{job_id}")
        print("  3. Keys now match perfectly!")
        return True
    else:
        print("⚠️ POTENTIAL ISSUES:")
        if underscore_count > 0:
            print(f"   • Still has {underscore_count} underscore patterns")
        if colon_count == 0:
            print("   • No colon patterns found")
        return False

    print("\n" + "="*60)


def check_specific_lines():
    """Check the specific lines that were problematic"""
    print("\nChecking specific problematic lines...")

    file_path = "django_neurology_mcq/mcq/views.py"

    with open(file_path, 'r') as f:
        lines = f.readlines()

    # Check around line 4172 (successful result storage)
    for i in range(4165, min(4180, len(lines))):
        if "cache.set" in lines[i] and "ai_job" in lines[i]:
            if "ai_job_{job_id}" in lines[i]:
                print(f"  ❌ Line {i+1}: Still uses underscore")
            elif "ai_job:{job_id}" in lines[i]:
                print(f"  ✓ Line {i+1}: Correctly uses colon")

    # Check around line 4190 (error result storage)
    for i in range(4183, min(4195, len(lines))):
        if "cache.set" in lines[i] and "ai_job" in lines[i]:
            if "ai_job_{job_id}" in lines[i]:
                print(f"  ❌ Line {i+1}: Still uses underscore")
            elif "ai_job:{job_id}" in lines[i]:
                print(f"  ✓ Line {i+1}: Correctly uses colon")


def main():
    """Run verification"""
    success = verify_fix()
    check_specific_lines()

    print("\n" + "="*60)
    if success:
        print("✅ Cache key fix has been successfully applied!")
        print("\nNext step: Deploy to Heroku to resolve the 503 error")
        print("  git add .")
        print("  git commit -m 'Fix 503 error: Correct cache key mismatch'")
        print("  git push heroku main")
        return 0
    else:
        print("❌ Fix may need additional work")
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(main())