#!/usr/bin/env python3
"""
Test AI Features on Heroku with Real Authentication
Tests all Edit with AI features end-to-end
"""

import requests
import json
import time
from datetime import datetime
import getpass

# Heroku configuration
HEROKU_URL = "https://enigmatic-hamlet-38937-db49bd5e9821.herokuapp.com"

# Test MCQ IDs (these exist in your database)
TEST_MCQ_IDS = [1, 36752, 141058, 214633, 219752]

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    END = '\033[0m'
    BOLD = '\033[1m'

def log(message, color=None, indent=0):
    """Print colored log message"""
    timestamp = datetime.now().strftime("%H:%M:%S")
    prefix = "  " * indent
    if color:
        print(f"{color}[{timestamp}] {prefix}{message}{Colors.END}")
    else:
        print(f"[{timestamp}] {prefix}{message}")

def login_to_heroku(session):
    """Login to Heroku app and get authenticated session"""
    log("\n" + "="*70, Colors.BOLD)
    log("AUTHENTICATION", Colors.BOLD)
    log("="*70, Colors.BOLD)
    
    # Get login page to obtain CSRF token
    log("Getting login page...", Colors.YELLOW)
    response = session.get(f"{HEROKU_URL}/login/", timeout=30)
    
    if response.status_code != 200:
        log(f"❌ Failed to get login page: HTTP {response.status_code}", Colors.RED)
        return False
    
    # Extract CSRF token from cookies
    csrf_token = session.cookies.get('csrftoken', '')
    if not csrf_token:
        log("⚠️  No CSRF token found in cookies", Colors.YELLOW)
        # Try to extract from HTML
        import re
        match = re.search(r'name=["\']csrfmiddlewaretoken["\'] value=["\']([^"\']+)["\']', response.text)
        if match:
            csrf_token = match.group(1)
            log(f"✅ Extracted CSRF token from HTML", Colors.GREEN)
        else:
            log("❌ Could not find CSRF token", Colors.RED)
            return False
    else:
        log(f"✅ Got CSRF token from cookies", Colors.GREEN)
    
    # Get credentials
    print(f"\n{Colors.BLUE}Enter your Heroku admin credentials:{Colors.END}")
    username = input("Username: ").strip()
    password = getpass.getpass("Password: ")
    
    # Attempt login
    log("\nLogging in...", Colors.YELLOW)
    login_data = {
        'username': username,
        'password': password,
        'csrfmiddlewaretoken': csrf_token
    }
    
    response = session.post(
        f"{HEROKU_URL}/login/",
        data=login_data,
        headers={
            'Referer': f"{HEROKU_URL}/login/"
        },
        timeout=30,
        allow_redirects=True
    )
    
    # Check if login was successful
    if 'sessionid' in session.cookies and response.status_code == 200:
        # Verify we're actually logged in by checking a protected page
        test_response = session.get(f"{HEROKU_URL}/dashboard/", timeout=30)
        if test_response.status_code == 200 and 'login' not in test_response.url:
            log("✅ Login successful!", Colors.GREEN)
            return True
    
    log("❌ Login failed - please check credentials", Colors.RED)
    return False

def test_ai_edit_question(session, mcq_id, custom_instructions="", test_num=1):
    """Test AI edit question endpoint"""
    log(f"\n{'─'*70}", Colors.CYAN)
    log(f"TEST {test_num}: AI Edit Question (MCQ #{mcq_id})", Colors.BOLD)
    if custom_instructions:
        log(f"Custom instructions: '{custom_instructions}'", Colors.BLUE, 1)
    else:
        log("No custom instructions", Colors.BLUE, 1)
    
    url = f"{HEROKU_URL}/mcq/{mcq_id}/ai/edit/question/"
    
    # Get CSRF token
    csrf_token = session.cookies.get('csrftoken', '')
    
    payload = {
        'custom_instructions': custom_instructions
    }
    
    try:
        log("Calling API...", Colors.YELLOW, 1)
        start_time = time.time()
        
        response = session.post(
            url,
            json=payload,
            headers={
                'X-CSRFToken': csrf_token,
                'Referer': f"{HEROKU_URL}/mcq/{mcq_id}/"
            },
            timeout=120
        )
        
        duration = time.time() - start_time
        log(f"Response time: {duration:.2f}s | Status: {response.status_code}", Colors.CYAN, 1)
        
        if response.status_code == 200:
            try:
                data = response.json()
                if data.get('success'):
                    improved = data.get('improved_text', '')
                    log(f"✅ SUCCESS - Generated {len(improved)} chars", Colors.GREEN, 1)
                    log(f"Preview: {improved[:150]}...", Colors.GREEN, 2)
                    return True, "Success"
                else:
                    error = data.get('error', 'Unknown error')
                    log(f"❌ API returned error: {error}", Colors.RED, 1)
                    return False, error
            except json.JSONDecodeError:
                log(f"❌ Invalid JSON response", Colors.RED, 1)
                return False, "Invalid JSON"
        else:
            log(f"❌ HTTP {response.status_code}", Colors.RED, 1)
            try:
                error_data = response.json()
                log(f"Error details: {error_data}", Colors.RED, 2)
            except:
                log(f"Response preview: {response.text[:200]}", Colors.RED, 2)
            return False, f"HTTP {response.status_code}"
            
    except requests.Timeout:
        log("❌ Request timeout (>120s)", Colors.RED, 1)
        return False, "Timeout"
    except Exception as e:
        log(f"❌ Exception: {str(e)}", Colors.RED, 1)
        return False, str(e)

def test_ai_edit_options(session, mcq_id, mode="fill_missing", custom_instructions="", test_num=1):
    """Test AI edit options endpoint"""
    log(f"\n{'─'*70}", Colors.CYAN)
    log(f"TEST {test_num}: AI Edit Options - {mode} (MCQ #{mcq_id})", Colors.BOLD)
    if custom_instructions:
        log(f"Custom instructions: '{custom_instructions}'", Colors.BLUE, 1)
    else:
        log("No custom instructions", Colors.BLUE, 1)
    
    url = f"{HEROKU_URL}/mcq/{mcq_id}/ai/edit/options/"
    
    # Get CSRF token
    csrf_token = session.cookies.get('csrftoken', '')
    
    payload = {
        'mode': mode,
        'custom_instructions': custom_instructions,
        'auto_regenerate_explanations': False,
        'auto_apply': False
    }
    
    try:
        log("Calling API...", Colors.YELLOW, 1)
        start_time = time.time()
        
        response = session.post(
            url,
            json=payload,
            headers={
                'X-CSRFToken': csrf_token,
                'Referer': f"{HEROKU_URL}/mcq/{mcq_id}/"
            },
            timeout=120
        )
        
        duration = time.time() - start_time
        log(f"Response time: {duration:.2f}s | Status: {response.status_code}", Colors.CYAN, 1)
        
        if response.status_code == 200:
            try:
                data = response.json()
                if data.get('success'):
                    options = data.get('improved_options', {})
                    log(f"✅ SUCCESS - Generated options: {list(options.keys())}", Colors.GREEN, 1)
                    for key, val in list(options.items())[:2]:  # Show first 2
                        log(f"{key}: {val[:80]}...", Colors.GREEN, 2)
                    return True, "Success"
                else:
                    error = data.get('error', 'Unknown error')
                    log(f"❌ API returned error: {error}", Colors.RED, 1)
                    return False, error
            except json.JSONDecodeError:
                log(f"❌ Invalid JSON response", Colors.RED, 1)
                return False, "Invalid JSON"
        else:
            log(f"❌ HTTP {response.status_code}", Colors.RED, 1)
            try:
                error_data = response.json()
                log(f"Error details: {error_data}", Colors.RED, 2)
            except:
                log(f"Response preview: {response.text[:200]}", Colors.RED, 2)
            return False, f"HTTP {response.status_code}"
            
    except requests.Timeout:
        log("❌ Request timeout (>120s)", Colors.RED, 1)
        return False, "Timeout"
    except Exception as e:
        log(f"❌ Exception: {str(e)}", Colors.RED, 1)
        return False, str(e)

def test_ai_edit_explanation(session, mcq_id, section_name="clinical_context", custom_instructions="", test_num=1):
    """Test AI edit explanation endpoint"""
    log(f"\n{'─'*70}", Colors.CYAN)
    log(f"TEST {test_num}: AI Edit Explanation - {section_name} (MCQ #{mcq_id})", Colors.BOLD)
    if custom_instructions:
        log(f"Custom instructions: '{custom_instructions}'", Colors.BLUE, 1)
    else:
        log("No custom instructions", Colors.BLUE, 1)
    
    url = f"{HEROKU_URL}/mcq/{mcq_id}/ai/edit/explanation/"
    
    # Get CSRF token
    csrf_token = session.cookies.get('csrftoken', '')
    
    payload = {
        'section_name': section_name,
        'current_content': 'Test content to be improved by AI',
        'custom_instructions': custom_instructions
    }
    
    try:
        log("Calling API...", Colors.YELLOW, 1)
        start_time = time.time()
        
        response = session.post(
            url,
            json=payload,
            headers={
                'X-CSRFToken': csrf_token,
                'Referer': f"{HEROKU_URL}/mcq/{mcq_id}/"
            },
            timeout=120
        )
        
        duration = time.time() - start_time
        log(f"Response time: {duration:.2f}s | Status: {response.status_code}", Colors.CYAN, 1)
        
        if response.status_code == 200:
            try:
                data = response.json()
                if data.get('success'):
                    content = data.get('enhanced_content', '')
                    log(f"✅ SUCCESS - Generated {len(content)} chars", Colors.GREEN, 1)
                    log(f"Preview: {content[:150]}...", Colors.GREEN, 2)
                    return True, "Success"
                else:
                    error = data.get('error', 'Unknown error')
                    log(f"❌ API returned error: {error}", Colors.RED, 1)
                    return False, error
            except json.JSONDecodeError:
                log(f"❌ Invalid JSON response", Colors.RED, 1)
                return False, "Invalid JSON"
        else:
            log(f"❌ HTTP {response.status_code}", Colors.RED, 1)
            try:
                error_data = response.json()
                log(f"Error details: {error_data}", Colors.RED, 2)
            except:
                log(f"Response preview: {response.text[:200]}", Colors.RED, 2)
            return False, f"HTTP {response.status_code}"
            
    except requests.Timeout:
        log("❌ Request timeout (>120s)", Colors.RED, 1)
        return False, "Timeout"
    except Exception as e:
        log(f"❌ Exception: {str(e)}", Colors.RED, 1)
        return False, str(e)

def main():
    """Main test runner"""
    log(f"\n{'='*70}", Colors.BOLD)
    log("HEROKU AI FEATURES COMPREHENSIVE TEST", Colors.BOLD)
    log(f"{'='*70}\n", Colors.BOLD)
    
    log(f"Target: {HEROKU_URL}", Colors.BLUE)
    log(f"Testing with {len(TEST_MCQ_IDS)} MCQs: {TEST_MCQ_IDS}", Colors.BLUE)
    
    # Create session
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
    })
    
    # Login
    if not login_to_heroku(session):
        log("\n❌ Cannot proceed without authentication", Colors.RED)
        return 1
    
    # Results tracking
    results = {
        'passed': 0,
        'failed': 0,
        'tests': []
    }
    
    test_counter = 1
    
    # ================== QUESTION EDITING TESTS ==================
    log(f"\n{'#'*70}", Colors.MAGENTA)
    log("SECTION 1: QUESTION EDITING (5 MCQs)", Colors.MAGENTA)
    log(f"{'#'*70}", Colors.MAGENTA)
    
    # Test without custom instructions
    for mcq_id in TEST_MCQ_IDS:
        success, msg = test_ai_edit_question(session, mcq_id, "", test_counter)
        results['tests'].append(('question_basic', mcq_id, success, msg))
        if success:
            results['passed'] += 1
        else:
            results['failed'] += 1
        test_counter += 1
        time.sleep(1)  # Rate limiting
    
    # Test WITH custom instructions (just 2 samples)
    log(f"\n{Colors.CYAN}Testing with custom instructions (2 samples)...{Colors.END}")
    custom_instr = "Make it more concise and add specific clinical values"
    for mcq_id in TEST_MCQ_IDS[:2]:
        success, msg = test_ai_edit_question(session, mcq_id, custom_instr, test_counter)
        results['tests'].append(('question_custom', mcq_id, success, msg))
        if success:
            results['passed'] += 1
        else:
            results['failed'] += 1
        test_counter += 1
        time.sleep(1)
    
    # ================== OPTIONS EDITING TESTS ==================
    log(f"\n{'#'*70}", Colors.MAGENTA)
    log("SECTION 2: OPTIONS EDITING (5 MCQs)", Colors.MAGENTA)
    log(f"{'#'*70}", Colors.MAGENTA)
    
    # Test fill_missing mode
    for mcq_id in TEST_MCQ_IDS:
        success, msg = test_ai_edit_options(session, mcq_id, "fill_missing", "", test_counter)
        results['tests'].append(('options_fill', mcq_id, success, msg))
        if success:
            results['passed'] += 1
        else:
            results['failed'] += 1
        test_counter += 1
        time.sleep(1)
    
    # Test improve_all mode (2 samples)
    log(f"\n{Colors.CYAN}Testing improve_all mode (2 samples)...{Colors.END}")
    for mcq_id in TEST_MCQ_IDS[:2]:
        success, msg = test_ai_edit_options(session, mcq_id, "improve_all", "", test_counter)
        results['tests'].append(('options_improve', mcq_id, success, msg))
        if success:
            results['passed'] += 1
        else:
            results['failed'] += 1
        test_counter += 1
        time.sleep(1)
    
    # ================== EXPLANATION EDITING TESTS ==================
    log(f"\n{'#'*70}", Colors.MAGENTA)
    log("SECTION 3: EXPLANATION EDITING (5 MCQs)", Colors.MAGENTA)
    log(f"{'#'*70}", Colors.MAGENTA)
    
    # Test different sections
    sections = ["clinical_context", "differential_diagnosis", "key_facts", "clinical_pearls", "guidelines"]
    for i, mcq_id in enumerate(TEST_MCQ_IDS):
        section = sections[i]
        success, msg = test_ai_edit_explanation(session, mcq_id, section, "", test_counter)
        results['tests'].append(('explanation', mcq_id, success, msg))
        if success:
            results['passed'] += 1
        else:
            results['failed'] += 1
        test_counter += 1
        time.sleep(1)
    
    # Test with custom instructions (2 samples)
    log(f"\n{Colors.CYAN}Testing with custom instructions (2 samples)...{Colors.END}")
    custom_instr = "Focus on recent guidelines and evidence levels"
    for i, mcq_id in enumerate(TEST_MCQ_IDS[:2]):
        section = sections[i]
        success, msg = test_ai_edit_explanation(session, mcq_id, section, custom_instr, test_counter)
        results['tests'].append(('explanation_custom', mcq_id, success, msg))
        if success:
            results['passed'] += 1
        else:
            results['failed'] += 1
        test_counter += 1
        time.sleep(1)
    
    # ================== SUMMARY ==================
    log(f"\n{'='*70}", Colors.BOLD)
    log("TEST SUMMARY", Colors.BOLD)
    log(f"{'='*70}\n", Colors.BOLD)
    
    total = results['passed'] + results['failed']
    log(f"Total Tests: {total}", Colors.BOLD)
    log(f"✅ Passed: {results['passed']} ({results['passed']/total*100:.1f}%)", Colors.GREEN)
    log(f"❌ Failed: {results['failed']} ({results['failed']/total*100:.1f}%)", Colors.RED)
    
    # Category breakdown
    log(f"\n{'─'*70}", Colors.CYAN)
    log("RESULTS BY CATEGORY", Colors.BOLD)
    log(f"{'─'*70}", Colors.CYAN)
    
    categories = {}
    for category, mcq_id, success, msg in results['tests']:
        if category not in categories:
            categories[category] = {'passed': 0, 'failed': 0}
        if success:
            categories[category]['passed'] += 1
        else:
            categories[category]['failed'] += 1
    
    for category, stats in categories.items():
        total_cat = stats['passed'] + stats['failed']
        status = "✅" if stats['failed'] == 0 else "⚠️"
        log(f"{status} {category:20} {stats['passed']}/{total_cat} passed", 
            Colors.GREEN if stats['failed'] == 0 else Colors.YELLOW)
    
    # Show failures
    failures = [t for t in results['tests'] if not t[2]]
    if failures:
        log(f"\n{'─'*70}", Colors.RED)
        log("FAILURES DETAIL", Colors.RED)
        log(f"{'─'*70}", Colors.RED)
        for category, mcq_id, success, msg in failures:
            log(f"MCQ {mcq_id} ({category}): {msg}", Colors.RED)
    
    # Final verdict
    log(f"\n{'='*70}", Colors.BOLD)
    if results['failed'] == 0:
        log("🎉 ALL TESTS PASSED!", Colors.GREEN)
        return 0
    elif results['passed'] > results['failed']:
        log(f"⚠️  MOSTLY WORKING - {results['failed']} failures out of {total}", Colors.YELLOW)
        return 0
    else:
        log(f"❌ MULTIPLE FAILURES - {results['failed']} out of {total}", Colors.RED)
        return 1

if __name__ == "__main__":
    try:
        exit(main())
    except KeyboardInterrupt:
        log("\n\n⚠️  Tests interrupted by user", Colors.YELLOW)
        exit(130)
    except Exception as e:
        log(f"\n\n❌ Fatal error: {e}", Colors.RED)
        import traceback
        traceback.print_exc()
        exit(1)

