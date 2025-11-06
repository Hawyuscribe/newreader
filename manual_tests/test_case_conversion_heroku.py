#!/usr/bin/env python3
"""
Efficient test script for MCQ case conversion on Heroku
This uses requests to simulate the conversion process
"""
import requests
import json
import time
from urllib.parse import urljoin

# Your Heroku app URL
BASE_URL = "https://radiant-gorge-35079-2b52ba172c1e.herokuapp.com"

def test_case_conversion_api():
    """Test case conversion through API-like approach"""
    print("Testing MCQ Case Conversion on Heroku")
    print("=" * 80)
    
    # Test MCQ IDs - including the problematic one
    test_mcq_ids = [100420848]  # The one that showed peripheral neuropathy instead of Parkinson's
    
    session = requests.Session()
    
    for mcq_id in test_mcq_ids:
        print(f"\nTesting MCQ {mcq_id}...")
        
        try:
            # Step 1: Access the MCQ page
            mcq_url = urljoin(BASE_URL, f"/mcq/{mcq_id}/")
            response = session.get(mcq_url)
            
            if response.status_code == 200:
                print(f"✓ MCQ page accessible (Status: {response.status_code})")
                
                # Check if login is required
                if "login" in response.url or "Login" in response.text[:1000]:
                    print("❌ Login required - please disable authentication temporarily")
                    return
                
                # Step 2: Trigger case conversion
                # This would typically be a POST request to the conversion endpoint
                conversion_url = urljoin(BASE_URL, f"/mcq-conversion/convert/")
                
                # Get CSRF token if needed
                csrf_token = None
                if 'csrftoken' in session.cookies:
                    csrf_token = session.cookies['csrftoken']
                
                headers = {
                    'X-Requested-With': 'XMLHttpRequest',
                    'Content-Type': 'application/x-www-form-urlencoded',
                }
                if csrf_token:
                    headers['X-CSRFToken'] = csrf_token
                
                # Attempt conversion
                data = {'mcq_id': mcq_id}
                print("Attempting case conversion...")
                
                # Note: The actual endpoint might be different
                # This is a common pattern for AJAX requests
                
            else:
                print(f"✗ Failed to access MCQ page (Status: {response.status_code})")
                
        except Exception as e:
            print(f"✗ Error testing MCQ {mcq_id}: {e}")

def test_with_curl_commands():
    """Generate curl commands for manual testing"""
    print("\nCurl Commands for Manual Testing:")
    print("=" * 80)
    
    mcq_id = 100420848
    
    print(f"""
1. Check if MCQ page is accessible (without login):
   curl -I {BASE_URL}/mcq/{mcq_id}/

2. Check conversion status endpoint:
   curl -X GET {BASE_URL}/mcq-conversion/status/[session_id]/

3. Monitor Heroku logs in another terminal:
   heroku logs --tail --app radiant-gorge-35079 | grep -E "Case conversion|ValidationStatus|JSON"

4. Use browser developer tools:
   - Open Chrome/Safari DevTools (F12)
   - Go to Network tab
   - Navigate to {BASE_URL}/mcq/{mcq_id}/
   - Click "Convert to Case-Based Learning"
   - Watch the network requests to see the exact endpoints and data
""")

def test_with_selenium_approach():
    """Alternative approach using selenium (requires chrome driver)"""
    print("\nSelenium Approach (Most Comprehensive):")
    print("=" * 80)
    print("""
To fully automate the testing, you could:

1. Install selenium and chrome driver:
   pip install selenium
   
2. Use headless Chrome to:
   - Navigate to the MCQ page
   - Click the conversion button
   - Wait for the result
   - Extract and verify the case content

This would be the most accurate simulation of real user behavior.
""")

if __name__ == "__main__":
    print("MCQ Case Conversion Testing Options\n")
    
    # Try the API approach first
    test_case_conversion_api()
    
    # Show curl commands
    test_with_curl_commands()
    
    # Suggest selenium approach
    test_with_selenium_approach()
    
    print("\n" + "=" * 80)
    print("RECOMMENDATION: The most efficient approach is to:")
    print("1. Temporarily add a test endpoint that doesn't require login")
    print("2. Use the browser DevTools to capture the exact conversion flow")
    print("3. Monitor Heroku logs in real-time during testing"