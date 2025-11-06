#!/usr/bin/env python3
"""
Direct API test for GPT-5-nano options editing functionality
Tests the live Heroku deployment without needing UI login
"""

import requests
import time
import json
import sys
from typing import Optional, Dict, Any

# Configuration
HEROKU_URL = "https://enigmatic-hamlet-38937-db49bd5e9821.herokuapp.com"
TEST_MCQ_ID = 99988010
POLL_INTERVAL = 2  # seconds
MAX_WAIT_TIME = 120  # seconds

def get_csrf_token(session: requests.Session) -> Optional[str]:
    """Get CSRF token from the MCQ page"""
    response = session.get(f"{HEROKU_URL}/mcq/{TEST_MCQ_ID}/")
    if response.status_code != 200:
        print(f"Failed to get MCQ page: {response.status_code}")
        return None

    # Extract CSRF token from response
    import re
    match = re.search(r"csrfmiddlewaretoken['\"]:\s*['\"]([^'\"]+)['\"]", response.text)
    if not match:
        # Try meta tag
        match = re.search(r"<meta name=['\"]csrf-token['\"] content=['\"]([^'\"]+)['\"]", response.text)
    if not match:
        # Try input field
        match = re.search(r"<input[^>]*name=['\"]csrfmiddlewaretoken['\"][^>]*value=['\"]([^'\"]+)['\"]", response.text)

    if match:
        return match.group(1)
    return None

def test_options_api():
    """Test the options editing API with GPT-5-nano"""
    print(f"Testing GPT-5-nano options editing on {HEROKU_URL}")
    print("-" * 60)

    session = requests.Session()

    # Step 1: Get CSRF token
    print("Step 1: Getting CSRF token...")
    csrf_token = get_csrf_token(session)
    if not csrf_token:
        print("❌ Failed to get CSRF token")
        return False
    print(f"✓ Got CSRF token: {csrf_token[:10]}...")

    # Step 2: Start the options editing job
    print(f"\nStep 2: Starting options editing job for MCQ {TEST_MCQ_ID}...")

    headers = {
        "X-CSRFToken": csrf_token,
        "Content-Type": "application/json",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": f"{HEROKU_URL}/mcq/{TEST_MCQ_ID}/",
    }

    # Create the request payload
    payload = {
        "mcq_id": TEST_MCQ_ID,
        "current_options": [
            {"id": 1, "text": "Option A", "is_correct": False},
            {"id": 2, "text": "Option B", "is_correct": True},
            {"id": 3, "text": "Option C", "is_correct": False},
            {"id": 4, "text": "Option D", "is_correct": False},
        ],
        "question_stem": "Test question for GPT-5-nano options editing",
        "explanation": "Test explanation"
    }

    try:
        response = session.post(
            f"{HEROKU_URL}/mcq/{TEST_MCQ_ID}/edit-options-with-ai/",
            json=payload,
            headers=headers,
            timeout=30
        )

        if response.status_code == 401:
            print("❌ Authentication required - need to be logged in as staff")
            print("   The endpoint requires staff authentication")
            return False

        if response.status_code != 200:
            print(f"❌ Failed to start job: HTTP {response.status_code}")
            print(f"   Response: {response.text[:500]}")
            return False

        try:
            result = response.json()
        except json.JSONDecodeError:
            print(f"❌ Invalid JSON response: {response.text[:500]}")
            return False

        if result.get("status") == "error":
            print(f"❌ API error: {result.get('message', 'Unknown error')}")
            return False

        job_id = result.get("job_id")
        if not job_id:
            print("❌ No job_id in response")
            print(f"   Response: {json.dumps(result, indent=2)}")
            return False

        print(f"✓ Job started with ID: {job_id}")

    except requests.RequestException as e:
        print(f"❌ Request failed: {e}")
        return False

    # Step 3: Poll for job completion
    print(f"\nStep 3: Polling for job completion (max {MAX_WAIT_TIME}s)...")

    start_time = time.time()
    last_status = None

    while time.time() - start_time < MAX_WAIT_TIME:
        time.sleep(POLL_INTERVAL)

        try:
            poll_response = session.get(
                f"{HEROKU_URL}/mcq/job-status/{job_id}/",
                headers={"X-Requested-With": "XMLHttpRequest"},
                timeout=10
            )

            if poll_response.status_code != 200:
                print(f"   Poll failed: HTTP {poll_response.status_code}")
                continue

            status_data = poll_response.json()
            current_status = status_data.get("status")

            if current_status != last_status:
                elapsed = int(time.time() - start_time)
                print(f"   [{elapsed:3d}s] Status: {current_status}")
                last_status = current_status

            if current_status == "completed":
                print(f"\n✓ Job completed successfully!")

                # Check the result
                result_data = status_data.get("result", {})
                if result_data:
                    print("\nResult summary:")
                    print(f"  - Success: {result_data.get('success', False)}")

                    if result_data.get("improved_options"):
                        print(f"  - Improved options count: {len(result_data['improved_options'])}")
                        print("\n  First improved option:")
                        first_option = result_data["improved_options"][0]
                        print(f"    Text: {first_option.get('text', '')[:100]}...")
                        print(f"    Is Correct: {first_option.get('is_correct', False)}")

                    if result_data.get("model_used"):
                        print(f"\n  - Model used: {result_data['model_used']}")
                        if "gpt-5-nano" in result_data["model_used"].lower():
                            print("  ✓ Confirmed using GPT-5-nano as configured!")
                        else:
                            print("  ⚠ Warning: Not using GPT-5-nano model")

                return True

            elif current_status == "failed":
                error_msg = status_data.get("error", "Unknown error")
                print(f"\n❌ Job failed: {error_msg}")
                return False

        except Exception as e:
            print(f"   Poll error: {e}")
            continue

    print(f"\n❌ Timeout after {MAX_WAIT_TIME} seconds")
    return False

def main():
    """Main test runner"""
    print("\n" + "="*60)
    print("GPT-5-nano Options Editing API Test")
    print("="*60 + "\n")

    success = test_options_api()

    print("\n" + "="*60)
    if success:
        print("✅ TEST PASSED - GPT-5-nano options editing is working!")
    else:
        print("❌ TEST FAILED - See errors above")
        print("\nNote: This test requires staff authentication.")
        print("The actual Playwright test with login would provide full coverage.")
    print("="*60 + "\n")

    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main())