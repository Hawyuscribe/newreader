#!/usr/bin/env python3
"""
Test GPT-5-nano options editing with correct API endpoint
Tests the real API with proper authentication
"""

import os
import sys
import json
import time
import requests
import re
from typing import Dict, Any, Optional, List
import getpass

# Configuration
HEROKU_URL = "https://enigmatic-hamlet-38937-db49bd5e9821.herokuapp.com"

# Get credentials - prompt if not set
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "tariq")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "")

if not ADMIN_PASSWORD:
    print("\n" + "="*60)
    print("Authentication Required")
    print("="*60)
    print(f"Username: {ADMIN_USERNAME}")
    ADMIN_PASSWORD = getpass.getpass("Password: ")

# Test MCQ IDs that exist in the database
TEST_MCQ_IDS = [100420848, 36752, 1]

# Poll settings
POLL_INTERVAL = 2  # seconds
MAX_WAIT_TIME = 120  # seconds


def login_to_site(session: requests.Session) -> bool:
    """Login to the Django site"""
    print("\n🔐 Authenticating...")

    # Get login page for CSRF token
    login_response = session.get(f"{HEROKU_URL}/accounts/login/")
    if login_response.status_code != 200:
        print(f"  ❌ Failed to get login page: {login_response.status_code}")
        return False

    # Extract CSRF token
    csrf_match = re.search(r'<input[^>]*name=["\']csrfmiddlewaretoken["\'][^>]*value=["\']([^"\']+)["\']', login_response.text)
    if not csrf_match:
        print("  ❌ Failed to find CSRF token")
        return False

    csrf_token = csrf_match.group(1)

    # Attempt login
    login_data = {
        "username": ADMIN_USERNAME,
        "password": ADMIN_PASSWORD,
        "csrfmiddlewaretoken": csrf_token,
    }

    response = session.post(
        f"{HEROKU_URL}/accounts/login/",
        data=login_data,
        headers={"Referer": f"{HEROKU_URL}/accounts/login/"},
        allow_redirects=True
    )

    # Check if login was successful
    if response.status_code == 200 and "/accounts/login/" not in response.url:
        print(f"  ✓ Logged in as {ADMIN_USERNAME}")
        return True
    else:
        print(f"  ❌ Login failed - please check credentials")
        return False


def test_options_editing(session: requests.Session, mcq_id: int) -> Dict[str, Any]:
    """Test the options editing with AI using correct endpoint"""
    print(f"\n📋 Testing MCQ #{mcq_id}...")

    # Get CSRF token from MCQ page
    mcq_page = session.get(f"{HEROKU_URL}/mcq/{mcq_id}/")
    if mcq_page.status_code != 200:
        print(f"  ❌ MCQ not found: HTTP {mcq_page.status_code}")
        return {"success": False, "error": f"MCQ {mcq_id} not found"}

    csrf_match = re.search(r'<input[^>]*name=["\']csrfmiddlewaretoken["\'][^>]*value=["\']([^"\']+)["\']', mcq_page.text)
    if not csrf_match:
        # Try to get from meta tag
        csrf_match = re.search(r'<meta name=["\']csrf-token["\'] content=["\']([^"\']+)["\']', mcq_page.text)

    if not csrf_match:
        print("  ❌ Failed to get CSRF token")
        return {"success": False, "error": "No CSRF token"}

    csrf_token = csrf_match.group(1)
    print(f"  ✓ Got CSRF token")

    # Prepare the request payload
    # Using the correct format expected by ai_edit_mcq_options view
    payload = {
        "mode": "improve_all",  # or "fill_missing"
        "custom_instructions": "Improve all options to be more medically accurate and detailed",
        "auto_regenerate_explanations": False,  # Don't regenerate explanations for this test
        "auto_apply": False,  # Don't auto-apply changes
        "use_async": True  # Use async to avoid timeouts
    }

    headers = {
        "X-CSRFToken": csrf_token,
        "Content-Type": "application/json",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": f"{HEROKU_URL}/mcq/{mcq_id}/",
    }

    # Call the correct endpoint: /mcq/<id>/ai/edit/options/
    print(f"  🚀 Calling GPT-5-nano to improve options...")
    start_time = time.time()

    try:
        # Using the CORRECT endpoint from urls.py
        response = session.post(
            f"{HEROKU_URL}/mcq/{mcq_id}/ai/edit/options/",  # Correct endpoint!
            json=payload,
            headers=headers,
            timeout=30
        )

        if response.status_code == 403:
            print(f"  ❌ Access denied - staff privileges required")
            return {"success": False, "error": "Staff access required"}

        if response.status_code != 200:
            print(f"  ❌ API call failed: HTTP {response.status_code}")
            print(f"     Response: {response.text[:200]}")
            return {"success": False, "error": f"HTTP {response.status_code}"}

        result = response.json()

        # Handle async job response
        if result.get("job_id"):
            job_id = result["job_id"]
            print(f"  ⏳ Async job started: {job_id}")

            # Poll for job completion
            poll_start = time.time()
            last_status = None

            while time.time() - poll_start < MAX_WAIT_TIME:
                time.sleep(POLL_INTERVAL)

                poll_response = session.get(
                    f"{HEROKU_URL}/mcq/job-status/{job_id}/",
                    headers={"X-Requested-With": "XMLHttpRequest"}
                )

                if poll_response.status_code == 200:
                    status_data = poll_response.json()
                    current_status = status_data.get("status")

                    if current_status != last_status:
                        elapsed = int(time.time() - poll_start)
                        print(f"    [{elapsed:3d}s] Status: {current_status}")
                        last_status = current_status

                    if current_status == "completed":
                        result = status_data.get("result", {})
                        break
                    elif current_status == "failed":
                        error = status_data.get("error", "Unknown error")
                        print(f"  ❌ Job failed: {error}")
                        return {"success": False, "error": error}

        processing_time = time.time() - start_time

        # Check the results
        if result.get("success"):
            print(f"\n  ✅ Success! Processed in {processing_time:.1f}s")

            # Extract improved options
            improved_options = result.get("improved_options", [])
            model_used = result.get("model_used", "Unknown")

            print(f"  🤖 Model: {model_used}")

            # Check if GPT-5-nano was used
            if "gpt-5-nano" in model_used.lower():
                print("     ✓ Confirmed: Using GPT-5-nano for fast processing!")
            else:
                print(f"     ⚠️ Expected GPT-5-nano but got: {model_used}")

            # Display improved options
            if improved_options:
                print("\n  Improved Options:")
                for i, opt in enumerate(improved_options[:3], 1):
                    text = opt.get('text', '')[:80]
                    correct = "✓" if opt.get('is_correct') else "✗"
                    print(f"    {i}. [{correct}] {text}...")

                # Show improvement metrics
                if result.get("original_options") and improved_options:
                    orig_length = sum(len(o.get('text', '')) for o in result.get("original_options", []))
                    imp_length = sum(len(o.get('text', '')) for o in improved_options)
                    if orig_length > 0:
                        print(f"\n  📊 Improvement: {imp_length/orig_length:.1f}x longer")

            return {
                "success": True,
                "model_used": model_used,
                "processing_time": processing_time,
                "improved_count": len(improved_options)
            }
        else:
            error_msg = result.get("error", "Unknown error")
            print(f"  ❌ Failed: {error_msg}")
            return {"success": False, "error": error_msg}

    except json.JSONDecodeError as e:
        print(f"  ❌ Invalid JSON response: {e}")
        return {"success": False, "error": "Invalid JSON response"}
    except requests.exceptions.Timeout:
        print(f"  ❌ Request timed out")
        return {"success": False, "error": "Request timeout"}
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return {"success": False, "error": str(e)}


def main():
    """Main test runner"""
    print("\n" + "="*80)
    print(" "*20 + "GPT-5-NANO OPTIONS EDITING TEST")
    print("="*80)
    print("\nTesting GPT-5-nano model for MCQ options improvement")
    print(f"Target: {HEROKU_URL}")

    session = requests.Session()

    # Login
    if not login_to_site(session):
        print("\n❌ Authentication failed")
        print("\nPlease ensure:")
        print("  1. The username and password are correct")
        print("  2. The user has staff privileges")
        return 1

    # Test results storage
    results = []
    successful = 0
    gpt5_nano_confirmed = 0

    print("\n" + "="*80)
    print("RUNNING TESTS")
    print("="*80)

    # Test each MCQ
    for mcq_id in TEST_MCQ_IDS[:2]:  # Test first 2 MCQs
        result = test_options_editing(session, mcq_id)
        results.append(result)

        if result["success"]:
            successful += 1
            if "gpt-5-nano" in result.get("model_used", "").lower():
                gpt5_nano_confirmed += 1

        # Small delay between tests
        time.sleep(1)

    # Display summary
    print("\n" + "="*80)
    print("TEST RESULTS SUMMARY")
    print("="*80)

    total = len(results)
    print(f"\n📊 Overall Results:")
    print(f"  • Tests run: {total}")
    print(f"  • Successful: {successful}/{total}")
    print(f"  • Success rate: {(successful/total*100):.0f}%" if total > 0 else "N/A")

    print(f"\n🤖 Model Verification:")
    print(f"  • GPT-5-nano confirmed: {gpt5_nano_confirmed}/{successful} successful tests")

    # Processing times
    times = [r["processing_time"] for r in results if r.get("processing_time")]
    if times:
        print(f"\n⏱️ Performance Metrics:")
        print(f"  • Average time: {sum(times)/len(times):.1f}s")
        print(f"  • Fastest: {min(times):.1f}s")
        print(f"  • Slowest: {max(times):.1f}s")

    # Final verdict
    print("\n" + "="*80)
    if successful == total and gpt5_nano_confirmed == successful:
        print("✅ ALL TESTS PASSED WITH GPT-5-NANO!")
        print("\nThe system is correctly configured:")
        print("  • GPT-5-nano model is being used for options editing")
        print("  • Async processing is working to prevent timeouts")
        print("  • Options are being successfully improved")
        print("  • JSON responses are properly formatted (no empty responses)")
    elif successful > 0:
        print(f"⚠️ PARTIAL SUCCESS: {successful}/{total} tests passed")
        if gpt5_nano_confirmed < successful:
            print(f"\n⚠️ Model Issue: Only {gpt5_nano_confirmed}/{successful} tests used GPT-5-nano")
            print("Please check the model configuration in openai_integration.py")
    else:
        print("❌ ALL TESTS FAILED")
        print("\nPlease check:")
        print("  1. OpenAI API key is configured")
        print("  2. Staff privileges are granted")
        print("  3. The endpoints are accessible")

    print("="*80 + "\n")

    return 0 if successful == total else 1


if __name__ == "__main__":
    sys.exit(main())