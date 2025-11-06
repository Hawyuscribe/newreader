#!/usr/bin/env python3
"""
Comprehensive AI Feature Testing Script
Tests all Edit with AI features on Heroku
"""

import requests
import json
import time
import sys
from datetime import datetime

# Configuration
HEROKU_URL = "https://enigmatic-hamlet-38937-db49bd5e9821.herokuapp.com"
TEST_MCQ_ID = 1  # We'll test with MCQ #1, adjust if needed

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'
    BOLD = '\033[1m'

def log(message, color=None):
    """Print colored log message"""
    timestamp = datetime.now().strftime("%H:%M:%S")
    if color:
        print(f"{color}[{timestamp}] {message}{Colors.END}")
    else:
        print(f"[{timestamp}] {message}")

def test_ai_edit_question(session, mcq_id, custom_instructions=""):
    """Test AI edit question endpoint"""
    log(f"\n{'='*60}", Colors.BOLD)
    log("TEST 1: AI Edit Question", Colors.BOLD)
    log(f"{'='*60}", Colors.BOLD)
    
    url = f"{HEROKU_URL}/mcq/{mcq_id}/ai/edit/question/"
    payload = {
        "custom_instructions": custom_instructions
    }
    
    log(f"URL: {url}", Colors.BLUE)
    log(f"Custom instructions: '{custom_instructions}'", Colors.BLUE)
    log("Sending request...", Colors.YELLOW)
    
    try:
        start_time = time.time()
        response = session.post(url, json=payload, timeout=120)
        duration = time.time() - start_time
        
        log(f"Response time: {duration:.2f}s", Colors.BLUE)
        log(f"Status code: {response.status_code}", Colors.BLUE)
        
        if response.status_code == 200:
            data = response.json()
            if data.get('success'):
                log("✅ SUCCESS", Colors.GREEN)
                improved_text = data.get('improved_text', '')
                log(f"Improved text length: {len(improved_text)} chars", Colors.GREEN)
                log(f"Preview: {improved_text[:200]}...", Colors.GREEN)
                return True, data
            else:
                error = data.get('error', 'Unknown error')
                log(f"❌ FAILED: {error}", Colors.RED)
                return False, data
        else:
            log(f"❌ HTTP ERROR: {response.status_code}", Colors.RED)
            log(f"Response: {response.text[:500]}", Colors.RED)
            return False, None
            
    except requests.Timeout:
        log("❌ TIMEOUT: Request took longer than 120s", Colors.RED)
        return False, None
    except Exception as e:
        log(f"❌ EXCEPTION: {str(e)}", Colors.RED)
        return False, None

def test_ai_edit_options(session, mcq_id, mode="fill_missing", custom_instructions=""):
    """Test AI edit options endpoint"""
    log(f"\n{'='*60}", Colors.BOLD)
    log(f"TEST 2: AI Edit Options (mode: {mode})", Colors.BOLD)
    log(f"{'='*60}", Colors.BOLD)
    
    url = f"{HEROKU_URL}/mcq/{mcq_id}/ai/edit/options/"
    payload = {
        "mode": mode,
        "custom_instructions": custom_instructions,
        "auto_regenerate_explanations": False,  # Don't auto-regenerate for testing
        "auto_apply": False
    }
    
    log(f"URL: {url}", Colors.BLUE)
    log(f"Mode: {mode}", Colors.BLUE)
    log(f"Custom instructions: '{custom_instructions}'", Colors.BLUE)
    log("Sending request...", Colors.YELLOW)
    
    try:
        start_time = time.time()
        response = session.post(url, json=payload, timeout=120)
        duration = time.time() - start_time
        
        log(f"Response time: {duration:.2f}s", Colors.BLUE)
        log(f"Status code: {response.status_code}", Colors.BLUE)
        
        if response.status_code == 200:
            data = response.json()
            if data.get('success'):
                log("✅ SUCCESS", Colors.GREEN)
                improved_options = data.get('improved_options', {})
                log(f"Options returned: {list(improved_options.keys())}", Colors.GREEN)
                for key, value in improved_options.items():
                    log(f"  {key}: {value[:80]}...", Colors.GREEN)
                return True, data
            else:
                error = data.get('error', 'Unknown error')
                log(f"❌ FAILED: {error}", Colors.RED)
                return False, data
        else:
            log(f"❌ HTTP ERROR: {response.status_code}", Colors.RED)
            log(f"Response: {response.text[:500]}", Colors.RED)
            return False, None
            
    except requests.Timeout:
        log("❌ TIMEOUT: Request took longer than 120s", Colors.RED)
        return False, None
    except Exception as e:
        log(f"❌ EXCEPTION: {str(e)}", Colors.RED)
        return False, None

def test_ai_edit_explanation(session, mcq_id, section_name="clinical_context", custom_instructions=""):
    """Test AI edit explanation endpoint"""
    log(f"\n{'='*60}", Colors.BOLD)
    log(f"TEST 3: AI Edit Explanation (section: {section_name})", Colors.BOLD)
    log(f"{'='*60}", Colors.BOLD)
    
    url = f"{HEROKU_URL}/mcq/{mcq_id}/ai/edit/explanation/"
    payload = {
        "section_name": section_name,
        "current_content": "This is test content for the section.",
        "custom_instructions": custom_instructions
    }
    
    log(f"URL: {url}", Colors.BLUE)
    log(f"Section: {section_name}", Colors.BLUE)
    log(f"Custom instructions: '{custom_instructions}'", Colors.BLUE)
    log("Sending request...", Colors.YELLOW)
    
    try:
        start_time = time.time()
        response = session.post(url, json=payload, timeout=120)
        duration = time.time() - start_time
        
        log(f"Response time: {duration:.2f}s", Colors.BLUE)
        log(f"Status code: {response.status_code}", Colors.BLUE)
        
        if response.status_code == 200:
            data = response.json()
            if data.get('success'):
                log("✅ SUCCESS", Colors.GREEN)
                enhanced_content = data.get('enhanced_content', '')
                log(f"Enhanced content length: {len(enhanced_content)} chars", Colors.GREEN)
                log(f"Preview: {enhanced_content[:200]}...", Colors.GREEN)
                return True, data
            else:
                error = data.get('error', 'Unknown error')
                log(f"❌ FAILED: {error}", Colors.RED)
                return False, data
        else:
            log(f"❌ HTTP ERROR: {response.status_code}", Colors.RED)
            log(f"Response: {response.text[:500]}", Colors.RED)
            return False, None
            
    except requests.Timeout:
        log("❌ TIMEOUT: Request took longer than 120s", Colors.RED)
        return False, None
    except Exception as e:
        log(f"❌ EXCEPTION: {str(e)}", Colors.RED)
        return False, None

def get_csrf_token_and_login(session):
    """Login to get authenticated session"""
    log("\n" + "="*60, Colors.BOLD)
    log("AUTHENTICATION", Colors.BOLD)
    log("="*60, Colors.BOLD)
    
    # Get CSRF token from login page
    log("Getting CSRF token...", Colors.YELLOW)
    response = session.get(f"{HEROKU_URL}/login/")
    
    if 'csrftoken' in session.cookies:
        csrf_token = session.cookies['csrftoken']
        log(f"✅ CSRF token obtained: {csrf_token[:20]}...", Colors.GREEN)
    else:
        log("⚠️  No CSRF token in cookies, trying from HTML", Colors.YELLOW)
        # Try to extract from HTML if not in cookies
        import re
        match = re.search(r'name=["\']csrfmiddlewaretoken["\'] value=["\']([^"\']+)["\']', response.text)
        if match:
            csrf_token = match.group(1)
            log(f"✅ CSRF token from HTML: {csrf_token[:20]}...", Colors.GREEN)
        else:
            csrf_token = ""
            log("⚠️  Could not find CSRF token", Colors.YELLOW)
    
    # Prompt for credentials
    print("\n" + Colors.BLUE + "Please enter your admin credentials:" + Colors.END)
    username = input("Username: ")
    password = input("Password (hidden): ")
    
    # Login
    log("\nLogging in...", Colors.YELLOW)
    login_data = {
        'username': username,
        'password': password,
        'csrfmiddlewaretoken': csrf_token
    }
    
    response = session.post(
        f"{HEROKU_URL}/login/",
        data=login_data,
        headers={'Referer': f"{HEROKU_URL}/login/"}
    )
    
    if response.status_code == 200 and 'sessionid' in session.cookies:
        log("✅ Login successful", Colors.GREEN)
        return True
    else:
        log("❌ Login failed", Colors.RED)
        log(f"Status: {response.status_code}", Colors.RED)
        return False

def main():
    """Main test runner"""
    log(f"\n{'#'*60}", Colors.BOLD)
    log("AI FEATURES COMPREHENSIVE TEST SUITE", Colors.BOLD)
    log(f"{'#'*60}\n", Colors.BOLD)
    
    log(f"Target: {HEROKU_URL}", Colors.BLUE)
    log(f"Test MCQ ID: {TEST_MCQ_ID}", Colors.BLUE)
    
    # Create session
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'AI-Features-Test-Script/1.0'
    })
    
    # Login
    if not get_csrf_token_and_login(session):
        log("\n❌ Cannot proceed without authentication", Colors.RED)
        return
    
    # Run tests
    results = {}
    
    # Test 1: Edit Question without custom instructions
    success, data = test_ai_edit_question(session, TEST_MCQ_ID, "")
    results['question_basic'] = success
    
    # Test 2: Edit Question WITH custom instructions
    time.sleep(2)  # Small delay between tests
    success, data = test_ai_edit_question(
        session, TEST_MCQ_ID, 
        "Make the question more concise and add more clinical details"
    )
    results['question_custom'] = success
    
    # Test 3: Fill missing options
    time.sleep(2)
    success, data = test_ai_edit_options(session, TEST_MCQ_ID, mode="fill_missing", custom_instructions="")
    results['options_fill'] = success
    
    # Test 4: Improve all options
    time.sleep(2)
    success, data = test_ai_edit_options(
        session, TEST_MCQ_ID, 
        mode="improve_all", 
        custom_instructions="Make options more specific and clinically relevant"
    )
    results['options_improve'] = success
    
    # Test 5: Edit explanation section
    time.sleep(2)
    success, data = test_ai_edit_explanation(
        session, TEST_MCQ_ID,
        section_name="clinical_context",
        custom_instructions=""
    )
    results['explanation_basic'] = success
    
    # Test 6: Edit explanation with custom instructions
    time.sleep(2)
    success, data = test_ai_edit_explanation(
        session, TEST_MCQ_ID,
        section_name="differential_diagnosis",
        custom_instructions="Focus on common conditions and add diagnostic criteria"
    )
    results['explanation_custom'] = success
    
    # Summary
    log(f"\n{'='*60}", Colors.BOLD)
    log("TEST SUMMARY", Colors.BOLD)
    log(f"{'='*60}", Colors.BOLD)
    
    passed = sum(1 for v in results.values() if v)
    total = len(results)
    
    for test_name, success in results.items():
        status = "✅ PASS" if success else "❌ FAIL"
        color = Colors.GREEN if success else Colors.RED
        log(f"{test_name:25} {status}", color)
    
    log(f"\nTotal: {passed}/{total} tests passed", Colors.BOLD)
    
    if passed == total:
        log("\n🎉 ALL TESTS PASSED!", Colors.GREEN)
        return 0
    else:
        log(f"\n⚠️  {total - passed} test(s) failed", Colors.YELLOW)
        return 1

if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        log("\n\n⚠️  Tests interrupted by user", Colors.YELLOW)
        sys.exit(130)

