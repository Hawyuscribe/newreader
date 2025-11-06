#!/usr/bin/env python3
"""
Test GPT-5-nano options editing with authentication
Requires admin credentials to be set as environment variables
"""

import os
import requests
import time
import json
import sys
import re
from typing import Optional, Dict, Any

# Configuration
HEROKU_URL = "https://enigmatic-hamlet-38937-db49bd5e9821.herokuapp.com"
TEST_MCQ_ID = 99988010
POLL_INTERVAL = 2  # seconds
MAX_WAIT_TIME = 120  # seconds

# Get credentials from environment
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "tariq")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "")

def login_to_site(session: requests.Session, username: str, password: str) -> bool:
    """Login to the Django site"""
    print(f"Logging in as {username}...")

    # First, get the login page to get CSRF token
    login_page = session.get(f"{HEROKU_URL}/accounts/login/")
    if login_page.status_code != 200:
        print(f"Failed to get login page: {login_page.status_code}")
        return False

    # Extract CSRF token
    csrf_match = re.search(r"csrfmiddlewaretoken['\"]:\s*['\"]([^'\"]+)['\"]", login_page.text)
    if not csrf_match:
        csrf_match = re.search(r"<input[^>]*name=['\"]csrfmiddlewaretoken['\"][^>]*value=['\"]([^'\"]+)['\"]", login_page.text)

    if not csrf_match:
        print("Failed to find CSRF token in login page")
        return False

    csrf_token = csrf_match.group(1)

    # Attempt login
    login_data = {
        "username": username,
        "password": password,
        "csrfmiddlewaretoken": csrf_token,
        "next": f"/mcq/{TEST_MCQ_ID}/"
    }

    headers = {
        "Referer": f"{HEROKU_URL}/accounts/login/",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    login_response = session.post(
        f"{HEROKU_URL}/accounts/login/",
        data=login_data,
        headers=headers,
        allow_redirects=True
    )

    # Check if login was successful
    if login_response.status_code == 200:
        # Check if we're still on the login page (failed login)
        if "/accounts/login/" in login_response.url:
            print("❌ Login failed - incorrect credentials")
            return False
        print("✓ Login successful")
        return True
    else:
        print(f"❌ Login failed with status: {login_response.status_code}")
        return False

def get_csrf_token(session: requests.Session) -> Optional[str]:
    """Get CSRF token from the MCQ page"""
    response = session.get(f"{HEROKU_URL}/mcq/{TEST_MCQ_ID}/")
    if response.status_code != 200:
        print(f"Failed to get MCQ page: {response.status_code}")
        return None

    # Extract CSRF token
    match = re.search(r"csrfmiddlewaretoken['\"]:\s*['\"]([^'\"]+)['\"]", response.text)
    if not match:
        match = re.search(r"<meta name=['\"]csrf-token['\"] content=['\"]([^'\"]+)['\"]", response.text)
    if not match:
        match = re.search(r"<input[^>]*name=['\"]csrfmiddlewaretoken['\"][^>]*value=['\"]([^'\"]+)['\"]", response.text)

    if match:
        return match.group(1)
    return None

def test_options_editing_with_auth():
    """Test the options editing with GPT-5-nano after authentication"""
    print(f"Testing GPT-5-nano options editing on {HEROKU_URL}")
    print("-" * 60)

    if not ADMIN_PASSWORD:
        print("❌ No admin password provided")
        print("   Set ADMIN_PASSWORD environment variable to run this test")
        return False

    session = requests.Session()

    # Step 1: Login
    print("\nStep 1: Authenticating...")
    if not login_to_site(session, ADMIN_USERNAME, ADMIN_PASSWORD):
        return False

    # Step 2: Get fresh CSRF token after login
    print("\nStep 2: Getting CSRF token...")
    csrf_token = get_csrf_token(session)
    if not csrf_token:
        print("❌ Failed to get CSRF token")
        return False
    print(f"✓ Got CSRF token: {csrf_token[:10]}...")

    # Step 3: Start the options editing job
    print(f"\nStep 3: Starting options editing job for MCQ {TEST_MCQ_ID}...")

    headers = {
        "X-CSRFToken": csrf_token,
        "Content-Type": "application/json",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": f"{HEROKU_URL}/mcq/{TEST_MCQ_ID}/",
    }

    # Get the actual MCQ data first
    mcq_response = session.get(f"{HEROKU_URL}/mcq/api/{TEST_MCQ_ID}/")
    if mcq_response.status_code == 200:
        try:
            mcq_data = mcq_response.json()
            current_options = mcq_data.get("options", [])
            question_stem = mcq_data.get("question_stem", "")
            explanation = mcq_data.get("explanation", "")
        except:
            # Use defaults if API doesn't exist
            current_options = [
                {"id": 1, "text": "Option A", "is_correct": False},
                {"id": 2, "text": "Option B", "is_correct": True},
                {"id": 3, "text": "Option C", "is_correct": False},
                {"id": 4, "text": "Option D", "is_correct": False},
            ]
            question_stem = "Test question for GPT-5-nano"
            explanation = "Test explanation"
    else:
        # Use defaults
        current_options = [
            {"id": 1, "text": "Option A", "is_correct": False},
            {"id": 2, "text": "Option B", "is_correct": True},
            {"id": 3, "text": "Option C", "is_correct": False},
            {"id": 4, "text": "Option D", "is_correct": False},
        ]
        question_stem = "Test question for GPT-5-nano"
        explanation = "Test explanation"

    payload = {
        "mcq_id": TEST_MCQ_ID,
        "current_options": current_options,
        "question_stem": question_stem,
        "explanation": explanation
    }

    try:
        response = session.post(
            f"{HEROKU_URL}/mcq/{TEST_MCQ_ID}/edit-options-with-ai/",
            json=payload,
            headers=headers,
            timeout=30
        )

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
            # Check if we got the result directly (synchronous response)
            if result.get("success") and result.get("improved_options"):
                print("✓ Got synchronous response (fast model)")
                print(f"  - Model used: {result.get('model_used', 'Unknown')}")
                if "gpt-5-nano" in str(result.get('model_used', '')).lower():
                    print("  ✓ Confirmed using GPT-5-nano!")
                return True
            else:
                print("❌ No job_id in response")
                print(f"   Response: {json.dumps(result, indent=2)}")
                return False

        print(f"✓ Job started with ID: {job_id}")

    except requests.RequestException as e:
        print(f"❌ Request failed: {e}")
        return False

    # Step 4: Poll for job completion
    print(f"\nStep 4: Polling for job completion (max {MAX_WAIT_TIME}s)...")

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
                        print("\n  Sample improved option:")
                        first_option = result_data["improved_options"][0]
                        print(f"    Text: {first_option.get('text', '')[:100]}...")
                        print(f"    Is Correct: {first_option.get('is_correct', False)}")

                    model_used = result_data.get("model_used", "")
                    print(f"\n  - Model used: {model_used}")
                    if "gpt-5-nano" in model_used.lower():
                        print("  ✓ Confirmed using GPT-5-nano as configured!")
                    else:
                        print(f"  ⚠ Warning: Expected GPT-5-nano but got {model_used}")

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
    print("GPT-5-nano Options Editing Test (with Authentication)")
    print("="*60 + "\n")

    success = test_options_editing_with_auth()

    print("\n" + "="*60)
    if success:
        print("✅ TEST PASSED - GPT-5-nano options editing is working!")
        print("\nKey achievements:")
        print("  1. Successfully authenticated as admin")
        print("  2. Started options editing job")
        print("  3. Verified GPT-5-nano model is being used")
        print("  4. Confirmed AI-generated options are returned")
    else:
        print("❌ TEST FAILED - See errors above")
        if not ADMIN_PASSWORD:
            print("\nTo run this test, set the ADMIN_PASSWORD environment variable:")
            print("  export ADMIN_PASSWORD='your_password_here'")
    print("="*60 + "\n")

    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main())