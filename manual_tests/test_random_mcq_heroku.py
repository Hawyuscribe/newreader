#!/usr/bin/env python3
"""
Test a random MCQ conversion on Heroku production
"""
import requests
import json
import time
from bs4 import BeautifulSoup

BASE_URL = "https://radiant-gorge-35079-2b52ba172c1e.herokuapp.com"

def test_random_mcq():
    """Test a random MCQ from the website"""
    print("Testing Random MCQ Conversion on Heroku")
    print("=" * 80)
    
    session = requests.Session()
    
    # Step 1: Get the MCQ list page
    print("\n1. Accessing MCQ list page...")
    mcq_list_url = f"{BASE_URL}/mcq/"
    
    try:
        response = session.get(mcq_list_url)
        
        if response.status_code == 200:
            print(f"✓ MCQ list page accessible (Status: {response.status_code})")
            
            # Check if login is required
            if "login" in response.url.lower() or "/login" in response.text[:1000]:
                print("\n❌ Login is still required. Please disable authentication temporarily.")
                print(f"   Redirected to: {response.url}")
                return
            
            # Parse the page to find MCQ links
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Look for MCQ links - adjust selector based on actual HTML structure
            mcq_links = []
            
            # Common patterns for MCQ links
            for link in soup.find_all('a', href=True):
                href = link['href']
                if '/mcq/' in href and href != '/mcq/':
                    # Extract MCQ ID from URL
                    parts = href.strip('/').split('/')
                    if parts[-1].isdigit():
                        mcq_id = int(parts[-1])
                        mcq_links.append(mcq_id)
            
            if mcq_links:
                # Pick a different MCQ (not the problematic 100420848)
                test_mcq_id = None
                for mcq_id in mcq_links[:10]:  # Check first 10
                    if mcq_id != 100420848:
                        test_mcq_id = mcq_id
                        break
                
                if test_mcq_id:
                    print(f"\n2. Selected MCQ ID: {test_mcq_id}")
                    test_specific_mcq(session, test_mcq_id)
                else:
                    print("✗ Could not find a suitable MCQ to test")
            else:
                print("✗ No MCQ links found on the page")
                print("   Page might require authentication or has a different structure")
                
                # Try to find any indication of MCQs
                if "subspecialty" in response.text.lower():
                    print("   Found 'subspecialty' in page - site seems accessible")
                    # Try a known MCQ ID
                    print("\n2. Testing with a different known MCQ ID...")
                    test_specific_mcq(session, 100443668)  # Different MCQ from logs
                
        else:
            print(f"✗ Failed to access MCQ list (Status: {response.status_code})")
            
    except Exception as e:
        print(f"✗ Error accessing MCQ list: {e}")

def test_specific_mcq(session, mcq_id):
    """Test a specific MCQ conversion"""
    print(f"\nTesting MCQ {mcq_id}...")
    
    try:
        # Access the MCQ page
        mcq_url = f"{BASE_URL}/mcq/{mcq_id}/"
        response = session.get(mcq_url)
        
        if response.status_code == 200:
            print(f"✓ MCQ page accessible")
            
            # Extract MCQ details from page
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Look for question text
            question_preview = "N/A"
            for elem in soup.find_all(['p', 'div', 'h3', 'h4']):
                text = elem.get_text().strip()
                if len(text) > 50 and "?" in text:
                    question_preview = text[:150] + "..."
                    break
            
            print(f"   Question preview: {question_preview}")
            
            # Look for the conversion button/link
            conversion_triggered = False
            
            # Check for AJAX endpoints in page scripts
            if "convert" in response.text.lower() or "case-based" in response.text.lower():
                print("\n3. Found case conversion elements in page")
                
                # Extract CSRF token
                csrf_token = None
                csrf_input = soup.find('input', {'name': 'csrfmiddlewaretoken'})
                if csrf_input:
                    csrf_token = csrf_input.get('value')
                elif 'csrftoken' in session.cookies:
                    csrf_token = session.cookies['csrftoken']
                
                print(f"   CSRF Token: {'Found' if csrf_token else 'Not found'}")
                
                # Look for conversion URL in JavaScript
                if "startConversion" in response.text or "mcq-conversion" in response.text:
                    print("\n4. Attempting to trigger conversion...")
                    
                    # Try the conversion endpoint
                    conversion_url = f"{BASE_URL}/mcq-conversion/convert/"
                    headers = {
                        'X-Requested-With': 'XMLHttpRequest',
                        'Content-Type': 'application/x-www-form-urlencoded',
                    }
                    if csrf_token:
                        headers['X-CSRFToken'] = csrf_token
                    
                    data = {'mcq_id': mcq_id}
                    
                    conv_response = session.post(conversion_url, data=data, headers=headers)
                    print(f"   Conversion response status: {conv_response.status_code}")
                    
                    if conv_response.status_code == 200:
                        try:
                            result = conv_response.json()
                            print(f"   Conversion result: {json.dumps(result, indent=2)}")
                            conversion_triggered = True
                        except:
                            print(f"   Response text: {conv_response.text[:200]}")
            
            if not conversion_triggered:
                print("\n   ℹ️  Could not trigger conversion automatically.")
                print("   Please manually test by:")
                print(f"   1. Navigate to {mcq_url}")
                print("   2. Click 'Convert to Case-Based Learning'")
                print("   3. Check browser console for errors")
                
        else:
            print(f"✗ Failed to access MCQ {mcq_id} (Status: {response.status_code})")
            
    except Exception as e:
        print(f"✗ Error testing MCQ {mcq_id}: {e}")
        import traceback
        traceback.print_exc()

def check_logs_for_errors():
    """Instruction to check logs"""
    print("\n" + "=" * 80)
    print("IMPORTANT: Check Heroku logs for any errors:")
    print("heroku logs --app radiant-gorge-35079 --num 50 | grep -E 'ERROR|error|Error|failed|Failed|JSON serializable|ValidationStatus'")
    print("\nOr monitor live:")
    print("heroku logs --tail --app radiant-gorge-35079")

if __name__ == "__main__":
    # Test with requests
    test_random_mcq()
    
    # Show log checking instructions
    check_logs_for_errors()
    
    print("\n" + "=" * 80)
    print("TEST COMPLETE")
    print("\nIf login is still required, please:")
    print("1. Temporarily disable authentication, OR")
    print("2. Add the test endpoint from create_test_endpoint.py")
    print("3. Test manually through the browser while monitoring logs")