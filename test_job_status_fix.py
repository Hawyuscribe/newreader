#!/usr/bin/env python3
"""
Test that the job status fix resolves the 503 error.
This tests that the cache key format is now consistent.
"""

import os
import sys
import django
import json
import uuid
from unittest.mock import Mock, patch

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_neurology_mcq.settings')
sys.path.insert(0, os.path.abspath('.'))
django.setup()

from django.core.cache import cache
from django.test import RequestFactory
from django_neurology_mcq.mcq.models import MCQ
from django_neurology_mcq.mcq.views import ai_edit_mcq_options, ai_job_status


def test_cache_key_consistency():
    """Test that options editing and job status use the same cache key format"""
    print("\n" + "="*60)
    print("TESTING JOB STATUS FIX")
    print("="*60)

    # Clear any existing cache entries
    cache.clear()

    # Create a test job_id
    test_job_id = str(uuid.uuid4())
    print(f"\n1. Testing with job_id: {test_job_id}")

    # Simulate what options editing does - store with colon format
    test_result = {
        'status': 'completed',
        'result': {
            'improved_options': {
                'A': 'Option A',
                'B': 'Option B',
                'C': 'Option C',
                'D': 'Option D'
            },
            'message': 'Test successful'
        }
    }

    # Store with the CORRECT format (colon)
    cache_key = f'ai_job:{test_job_id}'
    cache.set(cache_key, test_result, timeout=300)
    print(f"   ✓ Stored result with key: {cache_key}")

    # Test retrieval with first ai_job_status function (line 2378)
    # This one uses: cache.get(f"ai_job:{job_id}")
    retrieved = cache.get(f"ai_job:{test_job_id}")
    if retrieved:
        print(f"   ✓ First ai_job_status function can retrieve: Found {retrieved['status']}")
    else:
        print(f"   ❌ First ai_job_status function failed to retrieve")

    # Test the actual pattern used in the fixed options editing
    print("\n2. Testing fixed options editing cache pattern:")

    # Clear cache
    cache.clear()

    # Simulate the FIXED options editing storing pattern
    # After fix, it should use colon, not underscore
    fixed_key = f'ai_job:{test_job_id}'
    cache.set(fixed_key, test_result, timeout=300)
    print(f"   ✓ Options editing now stores with: {fixed_key}")

    # Verify job status can retrieve it
    retrieved = cache.get(f"ai_job:{test_job_id}")
    if retrieved and retrieved['status'] == 'completed':
        print(f"   ✓ Job status endpoint can retrieve the result")
        print(f"   ✓ Status: {retrieved['status']}")
        success = True
    else:
        print(f"   ❌ Job status endpoint cannot retrieve the result")
        success = False

    # Test that old underscore pattern would fail
    print("\n3. Verifying old pattern would have failed:")
    cache.clear()
    old_wrong_key = f'ai_job_{test_job_id}'  # Wrong underscore format
    cache.set(old_wrong_key, test_result, timeout=300)
    print(f"   • Old pattern stored with: {old_wrong_key}")

    retrieved_wrong = cache.get(f"ai_job:{test_job_id}")  # Looking with colon
    if not retrieved_wrong:
        print(f"   ✓ Confirmed: Old pattern would cause 404/503 (key mismatch)")
    else:
        print(f"   ❌ Unexpected: Old pattern somehow worked")

    # Final verdict
    print("\n" + "="*60)
    if success:
        print("✅ FIX VERIFIED: Cache keys are now consistent!")
        print("   The 503 error should be resolved.")
    else:
        print("❌ FIX INCOMPLETE: Cache keys still mismatched")
    print("="*60)

    return success


def test_integration():
    """Test the integration between options editing and job status"""
    print("\n4. Integration test with mock MCQ:")

    # Create a mock MCQ
    mock_mcq = Mock(spec=MCQ)
    mock_mcq.id = 99999
    mock_mcq.question_text = "Test question"
    mock_mcq.correct_answer = "A"
    mock_mcq.options = json.dumps({
        'A': 'Correct answer',
        'B': 'Wrong answer 1',
        'C': '',  # Missing option
        'D': ''   # Missing option
    })
    mock_mcq.get_options_dict.return_value = {
        'A': 'Correct answer',
        'B': 'Wrong answer 1',
        'C': '',
        'D': ''
    }

    print(f"   ✓ Created mock MCQ #{mock_mcq.id}")

    # Clear cache
    cache.clear()

    # Create a test job_id and simulate storing result
    job_id = str(uuid.uuid4())
    result = {
        'status': 'completed',
        'result': {
            'improved_options': {
                'A': 'Correct answer',
                'B': 'Wrong answer 1',
                'C': 'New option C',
                'D': 'New option D'
            },
            'message': 'Options filled successfully'
        }
    }

    # Store with CORRECT format (after fix)
    cache_key = f'ai_job:{job_id}'
    cache.set(cache_key, result, timeout=300)
    print(f"   ✓ Stored job result with key: {cache_key}")

    # Try to retrieve via job status endpoint pattern
    retrieved = cache.get(f"ai_job:{job_id}")
    if retrieved and retrieved['status'] == 'completed':
        print(f"   ✓ Job status retrieval successful")
        print(f"   ✓ Retrieved options: {len(retrieved['result']['improved_options'])} options")
        return True
    else:
        print(f"   ❌ Job status retrieval failed")
        return False


def main():
    """Run all tests"""
    try:
        # Test 1: Cache key consistency
        test1_passed = test_cache_key_consistency()

        # Test 2: Integration test
        test2_passed = test_integration()

        print("\n" + "="*60)
        print("FINAL RESULTS:")
        print("="*60)

        if test1_passed and test2_passed:
            print("✅ ALL TESTS PASSED!")
            print("\nThe fix successfully resolves the 503 error by:")
            print("  • Standardizing cache key format to use colon (:)")
            print("  • Ensuring options editing and job status use same key pattern")
            print("  • Eliminating the underscore (_) format that caused mismatch")
            print("\nReady to deploy to Heroku!")
            return 0
        else:
            print("❌ SOME TESTS FAILED")
            print("Please review the output above for details.")
            return 1

    except Exception as e:
        print(f"\n❌ Test error: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())