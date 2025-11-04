#!/usr/bin/env python3
"""
Local AI Feature Testing Script
Tests all AI editing features with real MCQs
"""

import os
import sys
import django

# Setup Django environment
sys.path.insert(0, '/Users/tariqalmatrudi/NEWreader/django_neurology_mcq')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
os.environ['SECRET_KEY'] = 'django-insecure-dev-key-for-testing-only'
django.setup()

import json
from django.test import Client
from django.contrib.auth.models import User
from mcq.models import MCQ
from datetime import datetime
import time

# Test MCQ IDs from our database
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

def test_ai_edit_question(client, mcq_id, custom_instructions="", test_name=""):
    """Test AI edit question"""
    mcq = MCQ.objects.get(id=mcq_id)
    log(f"\n{'─'*70}", Colors.CYAN)
    log(f"TEST: {test_name}", Colors.BOLD)
    log(f"MCQ ID: {mcq_id} | Subspecialty: {mcq.subspecialty}", Colors.BLUE, 1)
    log(f"Question: {mcq.question_text[:80]}...", Colors.BLUE, 1)
    log(f"Custom instructions: '{custom_instructions}'", Colors.BLUE, 1)
    
    url = f'/mcq/{mcq_id}/ai/edit/question/'
    payload = json.dumps({
        'custom_instructions': custom_instructions
    })
    
    try:
        log("Calling API...", Colors.YELLOW, 1)
        start_time = time.time()
        
        response = client.post(
            url,
            data=payload,
            content_type='application/json'
        )
        
        duration = time.time() - start_time
        log(f"Response time: {duration:.2f}s | Status: {response.status_code}", Colors.CYAN, 1)
        
        if response.status_code == 200:
            data = json.loads(response.content)
            if data.get('success'):
                improved = data.get('improved_text', '')
                log(f"✅ SUCCESS - Generated {len(improved)} chars", Colors.GREEN, 1)
                log(f"Preview: {improved[:150]}...", Colors.GREEN, 2)
                return True, "Success", improved
            else:
                error = data.get('error', 'Unknown error')
                log(f"❌ FAILED: {error}", Colors.RED, 1)
                return False, error, None
        elif response.status_code == 503:
            log(f"⚠️  OpenAI API not configured (expected in local)", Colors.YELLOW, 1)
            return None, "API not configured", None
        else:
            log(f"❌ HTTP {response.status_code}: {response.content[:200]}", Colors.RED, 1)
            return False, f"HTTP {response.status_code}", None
            
    except Exception as e:
        log(f"❌ EXCEPTION: {str(e)}", Colors.RED, 1)
        import traceback
        traceback.print_exc()
        return False, str(e), None

def test_ai_edit_options(client, mcq_id, mode="fill_missing", custom_instructions="", test_name=""):
    """Test AI edit options"""
    mcq = MCQ.objects.get(id=mcq_id)
    log(f"\n{'─'*70}", Colors.CYAN)
    log(f"TEST: {test_name}", Colors.BOLD)
    log(f"MCQ ID: {mcq_id} | Mode: {mode}", Colors.BLUE, 1)
    log(f"Custom instructions: '{custom_instructions}'", Colors.BLUE, 1)
    
    url = f'/mcq/{mcq_id}/ai/edit/options/'
    payload = json.dumps({
        'mode': mode,
        'custom_instructions': custom_instructions,
        'auto_regenerate_explanations': False,
        'auto_apply': False
    })
    
    try:
        log("Calling API...", Colors.YELLOW, 1)
        start_time = time.time()
        
        response = client.post(
            url,
            data=payload,
            content_type='application/json'
        )
        
        duration = time.time() - start_time
        log(f"Response time: {duration:.2f}s | Status: {response.status_code}", Colors.CYAN, 1)
        
        if response.status_code == 200:
            data = json.loads(response.content)
            if data.get('success'):
                options = data.get('improved_options', {})
                log(f"✅ SUCCESS - Generated options: {list(options.keys())}", Colors.GREEN, 1)
                for key, val in options.items():
                    log(f"{key}: {val[:80]}...", Colors.GREEN, 2)
                return True, "Success", options
            else:
                error = data.get('error', 'Unknown error')
                log(f"❌ FAILED: {error}", Colors.RED, 1)
                return False, error, None
        elif response.status_code == 503:
            log(f"⚠️  OpenAI API not configured (expected in local)", Colors.YELLOW, 1)
            return None, "API not configured", None
        else:
            log(f"❌ HTTP {response.status_code}: {response.content[:200]}", Colors.RED, 1)
            return False, f"HTTP {response.status_code}", None
            
    except Exception as e:
        log(f"❌ EXCEPTION: {str(e)}", Colors.RED, 1)
        import traceback
        traceback.print_exc()
        return False, str(e), None

def test_ai_edit_explanation(client, mcq_id, section_name="clinical_context", custom_instructions="", test_name=""):
    """Test AI edit explanation"""
    mcq = MCQ.objects.get(id=mcq_id)
    log(f"\n{'─'*70}", Colors.CYAN)
    log(f"TEST: {test_name}", Colors.BOLD)
    log(f"MCQ ID: {mcq_id} | Section: {section_name}", Colors.BLUE, 1)
    log(f"Custom instructions: '{custom_instructions}'", Colors.BLUE, 1)
    
    url = f'/mcq/{mcq_id}/ai/edit/explanation/'
    payload = json.dumps({
        'section_name': section_name,
        'current_content': 'Test content for improvement',
        'custom_instructions': custom_instructions
    })
    
    try:
        log("Calling API...", Colors.YELLOW, 1)
        start_time = time.time()
        
        response = client.post(
            url,
            data=payload,
            content_type='application/json'
        )
        
        duration = time.time() - start_time
        log(f"Response time: {duration:.2f}s | Status: {response.status_code}", Colors.CYAN, 1)
        
        if response.status_code == 200:
            data = json.loads(response.content)
            if data.get('success'):
                content = data.get('enhanced_content', '')
                log(f"✅ SUCCESS - Generated {len(content)} chars", Colors.GREEN, 1)
                log(f"Preview: {content[:150]}...", Colors.GREEN, 2)
                return True, "Success", content
            else:
                error = data.get('error', 'Unknown error')
                log(f"❌ FAILED: {error}", Colors.RED, 1)
                return False, error, None
        elif response.status_code == 503:
            log(f"⚠️  OpenAI API not configured (expected in local)", Colors.YELLOW, 1)
            return None, "API not configured", None
        else:
            log(f"❌ HTTP {response.status_code}: {response.content[:200]}", Colors.RED, 1)
            return False, f"HTTP {response.status_code}", None
            
    except Exception as e:
        log(f"❌ EXCEPTION: {str(e)}", Colors.RED, 1)
        import traceback
        traceback.print_exc()
        return False, str(e), None

def main():
    """Main test runner"""
    log(f"\n{'='*70}", Colors.BOLD)
    log("AI FEATURES LOCAL COMPREHENSIVE TEST", Colors.BOLD)
    log(f"{'='*70}\n", Colors.BOLD)
    
    # Create test client and login as staff
    client = Client()
    
    # Get or create admin user
    try:
        admin_user = User.objects.get(username='admin')
        log(f"Using existing admin user", Colors.GREEN)
    except User.DoesNotExist:
        admin_user = User.objects.create_superuser('admin', 'admin@test.com', 'testpass123')
        log(f"Created admin user", Colors.GREEN)
    
    # Login
    client.force_login(admin_user)
    log(f"Logged in as: {admin_user.username} (staff: {admin_user.is_staff})\n", Colors.GREEN)
    
    # Test counter
    results = {
        'passed': 0,
        'failed': 0,
        'skipped': 0,
        'details': []
    }
    
    # ================== QUESTION EDITING TESTS ==================
    log(f"\n{'#'*70}", Colors.MAGENTA)
    log("SECTION 1: QUESTION EDITING TESTS", Colors.MAGENTA)
    log(f"{'#'*70}", Colors.MAGENTA)
    
    # Test 1-5: Basic question editing (no custom instructions)
    for i, mcq_id in enumerate(TEST_MCQ_IDS, 1):
        success, msg, data = test_ai_edit_question(
            client, mcq_id, "",
            f"Question Edit Basic #{i}"
        )
        if success is True:
            results['passed'] += 1
        elif success is False:
            results['failed'] += 1
        else:
            results['skipped'] += 1
        results['details'].append(('question_basic', mcq_id, success, msg))
        time.sleep(0.5)
    
    # Test 6-10: Question editing WITH custom instructions
    custom_instr = "Make it more concise and add specific lab values"
    for i, mcq_id in enumerate(TEST_MCQ_IDS, 1):
        success, msg, data = test_ai_edit_question(
            client, mcq_id, custom_instr,
            f"Question Edit Custom #{i}"
        )
        if success is True:
            results['passed'] += 1
        elif success is False:
            results['failed'] += 1
        else:
            results['skipped'] += 1
        results['details'].append(('question_custom', mcq_id, success, msg))
        time.sleep(0.5)
    
    # ================== OPTIONS EDITING TESTS ==================
    log(f"\n{'#'*70}", Colors.MAGENTA)
    log("SECTION 2: OPTIONS EDITING TESTS", Colors.MAGENTA)
    log(f"{'#'*70}", Colors.MAGENTA)
    
    # Test 11-15: Fill missing options
    for i, mcq_id in enumerate(TEST_MCQ_IDS, 1):
        success, msg, data = test_ai_edit_options(
            client, mcq_id, "fill_missing", "",
            f"Options Fill Missing #{i}"
        )
        if success is True:
            results['passed'] += 1
        elif success is False:
            results['failed'] += 1
        else:
            results['skipped'] += 1
        results['details'].append(('options_fill', mcq_id, success, msg))
        time.sleep(0.5)
    
    # Test 16-20: Improve all options
    for i, mcq_id in enumerate(TEST_MCQ_IDS, 1):
        success, msg, data = test_ai_edit_options(
            client, mcq_id, "improve_all", "",
            f"Options Improve All #{i}"
        )
        if success is True:
            results['passed'] += 1
        elif success is False:
            results['failed'] += 1
        else:
            results['skipped'] += 1
        results['details'].append(('options_improve', mcq_id, success, msg))
        time.sleep(0.5)
    
    # Test 21-25: Options with custom instructions
    custom_instr = "Make options more specific with exact values"
    for i, mcq_id in enumerate(TEST_MCQ_IDS, 1):
        success, msg, data = test_ai_edit_options(
            client, mcq_id, "improve_all", custom_instr,
            f"Options Custom #{i}"
        )
        if success is True:
            results['passed'] += 1
        elif success is False:
            results['failed'] += 1
        else:
            results['skipped'] += 1
        results['details'].append(('options_custom', mcq_id, success, msg))
        time.sleep(0.5)
    
    # ================== EXPLANATION EDITING TESTS ==================
    log(f"\n{'#'*70}", Colors.MAGENTA)
    log("SECTION 3: EXPLANATION EDITING TESTS", Colors.MAGENTA)
    log(f"{'#'*70}", Colors.MAGENTA)
    
    # Test 26-30: Basic explanation editing
    sections = ["clinical_context", "differential_diagnosis", "key_facts", "clinical_pearls", "guidelines"]
    for i, (mcq_id, section) in enumerate(zip(TEST_MCQ_IDS, sections), 1):
        success, msg, data = test_ai_edit_explanation(
            client, mcq_id, section, "",
            f"Explanation Basic #{i} ({section})"
        )
        if success is True:
            results['passed'] += 1
        elif success is False:
            results['failed'] += 1
        else:
            results['skipped'] += 1
        results['details'].append(('explanation_basic', mcq_id, success, msg))
        time.sleep(0.5)
    
    # Test 31-35: Explanation with custom instructions
    custom_instr = "Focus on recent guidelines and evidence-based medicine"
    for i, (mcq_id, section) in enumerate(zip(TEST_MCQ_IDS, sections), 1):
        success, msg, data = test_ai_edit_explanation(
            client, mcq_id, section, custom_instr,
            f"Explanation Custom #{i} ({section})"
        )
        if success is True:
            results['passed'] += 1
        elif success is False:
            results['failed'] += 1
        else:
            results['skipped'] += 1
        results['details'].append(('explanation_custom', mcq_id, success, msg))
        time.sleep(0.5)
    
    # ================== SUMMARY ==================
    log(f"\n{'='*70}", Colors.BOLD)
    log("TEST SUMMARY", Colors.BOLD)
    log(f"{'='*70}\n", Colors.BOLD)
    
    log(f"Total Tests: {results['passed'] + results['failed'] + results['skipped']}", Colors.BOLD)
    log(f"✅ Passed: {results['passed']}", Colors.GREEN)
    log(f"❌ Failed: {results['failed']}", Colors.RED)
    log(f"⚠️  Skipped (API not configured): {results['skipped']}", Colors.YELLOW)
    
    # Detailed results by category
    log(f"\n{'─'*70}", Colors.CYAN)
    log("DETAILED RESULTS BY CATEGORY", Colors.BOLD)
    log(f"{'─'*70}", Colors.CYAN)
    
    categories = {}
    for category, mcq_id, success, msg in results['details']:
        if category not in categories:
            categories[category] = {'passed': 0, 'failed': 0, 'skipped': 0}
        if success is True:
            categories[category]['passed'] += 1
        elif success is False:
            categories[category]['failed'] += 1
        else:
            categories[category]['skipped'] += 1
    
    for category, stats in categories.items():
        total = stats['passed'] + stats['failed'] + stats['skipped']
        log(f"\n{category}:", Colors.BOLD)
        log(f"  ✅ {stats['passed']}/{total} passed", Colors.GREEN if stats['passed'] == total else Colors.YELLOW)
        if stats['failed'] > 0:
            log(f"  ❌ {stats['failed']}/{total} failed", Colors.RED)
        if stats['skipped'] > 0:
            log(f"  ⚠️  {stats['skipped']}/{total} skipped", Colors.YELLOW)
    
    # Show failures
    failures = [d for d in results['details'] if d[2] is False]
    if failures:
        log(f"\n{'─'*70}", Colors.RED)
        log("FAILURES DETAIL", Colors.RED)
        log(f"{'─'*70}", Colors.RED)
        for category, mcq_id, success, msg in failures:
            log(f"MCQ {mcq_id} ({category}): {msg}", Colors.RED)
    
    # Final verdict
    log(f"\n{'='*70}", Colors.BOLD)
    if results['failed'] == 0:
        if results['skipped'] > 0:
            log("⚠️  ALL FUNCTIONAL TESTS PASSED (some skipped due to API config)", Colors.YELLOW)
            return 0
        else:
            log("🎉 ALL TESTS PASSED!", Colors.GREEN)
            return 0
    else:
        log(f"❌ {results['failed']} TEST(S) FAILED", Colors.RED)
        return 1

if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        log("\n\n⚠️  Tests interrupted by user", Colors.YELLOW)
        sys.exit(130)
    except Exception as e:
        log(f"\n\n❌ Fatal error: {e}", Colors.RED)
        import traceback
        traceback.print_exc()
        sys.exit(1)

