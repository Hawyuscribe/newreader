#!/usr/bin/env python3
"""
Test script to diagnose MCQ case conversion repetition issue
"""

import requests
import json
import time
from datetime import datetime

def test_mcq_conversion_issue():
    """Test MCQ conversion to identify why cases are repeating"""
    
    base_url = "https://radiant-gorge-35079-2b52ba172c1e.herokuapp.com"
    
    # Test with different MCQ IDs
    test_mcqs = [100, 200, 300, 500, 1000]
    
    print("🔍 Testing MCQ-to-Case conversion for repetition issues...")
    print(f"🌐 Base URL: {base_url}")
    print(f"⏰ Test started at: {datetime.now()}")
    print("=" * 60)
    
    results = {}
    
    for mcq_id in test_mcqs:
        print(f"\n📋 Testing MCQ #{mcq_id}")
        
        # Test the same MCQ 3 times
        mcq_results = []
        
        for attempt in range(3):
            print(f"  Attempt {attempt + 1}/3...")
            
            try:
                # Make request to conversion endpoint
                url = f"{base_url}/mcq/{mcq_id}/convert-to-case/"
                
                # We need to simulate a logged-in user request
                response = requests.post(url, timeout=30)
                
                if response.status_code == 200:
                    # Try to extract case data from response
                    if response.headers.get('content-type', '').startswith('application/json'):
                        case_data = response.json()
                        mcq_results.append({
                            'attempt': attempt + 1,
                            'status': 'success',
                            'case_content': case_data.get('clinical_presentation', 'No content'),
                            'case_hash': hash(str(case_data.get('clinical_presentation', '')))
                        })
                    else:
                        # HTML response - might be redirected to login
                        mcq_results.append({
                            'attempt': attempt + 1,
                            'status': 'html_response',
                            'content_length': len(response.text),
                            'contains_login': 'login' in response.text.lower()
                        })
                elif response.status_code == 302:
                    mcq_results.append({
                        'attempt': attempt + 1,
                        'status': 'redirect',
                        'location': response.headers.get('location', 'Unknown')
                    })
                else:
                    mcq_results.append({
                        'attempt': attempt + 1,
                        'status': f'error_{response.status_code}',
                        'response': response.text[:200]
                    })
                    
            except Exception as e:
                mcq_results.append({
                    'attempt': attempt + 1,
                    'status': 'exception',
                    'error': str(e)
                })
            
            time.sleep(2)  # Wait between attempts
        
        results[mcq_id] = mcq_results
    
    # Analyze results
    print("\n" + "=" * 60)
    print("📊 ANALYSIS RESULTS")
    print("=" * 60)
    
    for mcq_id, attempts in results.items():
        print(f"\n📋 MCQ #{mcq_id}:")
        
        successful_attempts = [a for a in attempts if a['status'] == 'success']
        
        if successful_attempts:
            # Check if cases are identical
            case_hashes = [a['case_hash'] for a in successful_attempts]
            unique_hashes = set(case_hashes)
            
            print(f"  ✅ Successful conversions: {len(successful_attempts)}/3")
            print(f"  🔄 Unique cases generated: {len(unique_hashes)}")
            
            if len(unique_hashes) == 1:
                print("  ❌ ISSUE: All cases are identical!")
            elif len(unique_hashes) == len(successful_attempts):
                print("  ✅ GOOD: All cases are unique!")
            else:
                print(f"  ⚠️  PARTIAL: {len(unique_hashes)} unique out of {len(successful_attempts)}")
                
            # Show first case content preview
            if successful_attempts:
                preview = successful_attempts[0]['case_content'][:100] + "..."
                print(f"  📝 Case preview: {preview}")
        else:
            print("  ❌ No successful conversions")
            for attempt in attempts:
                print(f"    Attempt {attempt['attempt']}: {attempt['status']}")
    
    # Cross-MCQ analysis
    print(f"\n🔍 CROSS-MCQ ANALYSIS")
    all_successful = []
    for mcq_id, attempts in results.items():
        for attempt in attempts:
            if attempt['status'] == 'success':
                all_successful.append({
                    'mcq_id': mcq_id,
                    'case_hash': attempt['case_hash'],
                    'content': attempt['case_content']
                })
    
    if all_successful:
        all_hashes = [a['case_hash'] for a in all_successful]
        unique_across_mcqs = set(all_hashes)
        
        print(f"  📊 Total successful conversions: {len(all_successful)}")
        print(f"  🔄 Unique cases across all MCQs: {len(unique_across_mcqs)}")
        
        if len(unique_across_mcqs) == 1:
            print("  🚨 CRITICAL ISSUE: All MCQs generate the SAME case!")
        elif len(unique_across_mcqs) < len(all_successful):
            print("  ⚠️  WARNING: Some MCQs generate identical cases!")
            
            # Find duplicates
            hash_to_mcqs = {}
            for result in all_successful:
                hash_val = result['case_hash']
                if hash_val not in hash_to_mcqs:
                    hash_to_mcqs[hash_val] = []
                hash_to_mcqs[hash_val].append(result['mcq_id'])
            
            for hash_val, mcq_ids in hash_to_mcqs.items():
                if len(mcq_ids) > 1:
                    print(f"    🔄 MCQs {mcq_ids} generate identical cases")
        else:
            print("  ✅ EXCELLENT: All cases are unique across different MCQs!")
    
    print("\n" + "=" * 60)
    print("🏁 Test completed!")
    return results

if __name__ == "__main__":
    test_mcq_conversion_issue()