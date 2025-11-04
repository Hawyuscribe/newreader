#!/usr/bin/env python3
"""
Test script for MCQ-to-Case conversion on Heroku
Tests if the same MCQ generates varied cases and if different MCQs generate different cases
"""

import requests
import json
import time
from datetime import datetime
import hashlib
from collections import defaultdict

# Configuration
HEROKU_URL = "https://radiant-gorge-35079-2b52ba172c1e.herokuapp.com"
MCQ_IDS_TO_TEST = [100, 200, 150, 300]  # Test multiple MCQs
CONVERSIONS_PER_MCQ = 5  # Convert each MCQ this many times
DELAY_BETWEEN_REQUESTS = 2  # Seconds between requests to avoid rate limiting

def get_case_hash(case_content):
    """Generate a hash of the case content for easy comparison"""
    # Extract key parts of the case for comparison
    case_str = json.dumps(case_content, sort_keys=True)
    return hashlib.md5(case_str.encode()).hexdigest()[:8]

def test_mcq_conversion(mcq_id, session):
    """Test converting a single MCQ to a case"""
    url = f"{HEROKU_URL}/mcq/{mcq_id}/convert-to-case/"
    
    try:
        response = session.get(url, timeout=30)
        
        if response.status_code == 200:
            try:
                data = response.json()
                return {
                    'success': True,
                    'case_data': data,
                    'case_hash': get_case_hash(data),
                    'response_time': response.elapsed.total_seconds()
                }
            except json.JSONDecodeError:
                return {
                    'success': False,
                    'error': 'Invalid JSON response',
                    'content': response.text[:200]
                }
        else:
            return {
                'success': False,
                'status_code': response.status_code,
                'error': response.text[:200]
            }
    except requests.exceptions.RequestException as e:
        return {
            'success': False,
            'error': f'Request failed: {str(e)}'
        }

def main():
    print(f"Testing MCQ-to-Case conversion on Heroku")
    print(f"URL: {HEROKU_URL}")
    print(f"Testing MCQs: {MCQ_IDS_TO_TEST}")
    print(f"Conversions per MCQ: {CONVERSIONS_PER_MCQ}")
    print("=" * 80)
    
    # Create a session to reuse connections
    session = requests.Session()
    
    # Store results
    results = defaultdict(list)
    all_case_hashes = []
    
    # Test each MCQ multiple times
    for mcq_id in MCQ_IDS_TO_TEST:
        print(f"\nTesting MCQ #{mcq_id}:")
        print("-" * 40)
        
        for attempt in range(CONVERSIONS_PER_MCQ):
            print(f"  Attempt {attempt + 1}/{CONVERSIONS_PER_MCQ}...", end='', flush=True)
            
            result = test_mcq_conversion(mcq_id, session)
            results[mcq_id].append(result)
            
            if result['success']:
                case_hash = result['case_hash']
                all_case_hashes.append((mcq_id, case_hash))
                print(f" Success! Case hash: {case_hash} (Response time: {result['response_time']:.2f}s)")
                
                # Print case preview if it's the first conversion
                if attempt == 0 and 'case_data' in result:
                    case_data = result['case_data']
                    if isinstance(case_data, dict):
                        print(f"    Case preview:")
                        if 'presentation' in case_data:
                            print(f"    - Presentation: {case_data['presentation'][:100]}...")
                        if 'questions' in case_data and case_data['questions']:
                            print(f"    - Number of questions: {len(case_data['questions'])}")
                            if case_data['questions']:
                                first_q = case_data['questions'][0]
                                print(f"    - First question: {first_q.get('question', 'N/A')[:100]}...")
            else:
                print(f" Failed! Error: {result.get('error', 'Unknown error')}")
            
            # Delay between requests
            if attempt < CONVERSIONS_PER_MCQ - 1:
                time.sleep(DELAY_BETWEEN_REQUESTS)
    
    print("\n" + "=" * 80)
    print("ANALYSIS RESULTS:")
    print("=" * 80)
    
    # Analyze results for each MCQ
    for mcq_id in MCQ_IDS_TO_TEST:
        mcq_results = results[mcq_id]
        successful_results = [r for r in mcq_results if r['success']]
        
        print(f"\nMCQ #{mcq_id}:")
        print(f"  - Total attempts: {len(mcq_results)}")
        print(f"  - Successful conversions: {len(successful_results)}")
        
        if successful_results:
            hashes = [r['case_hash'] for r in successful_results]
            unique_hashes = set(hashes)
            
            print(f"  - Unique cases generated: {len(unique_hashes)}")
            print(f"  - Case hashes: {', '.join(sorted(unique_hashes))}")
            
            if len(unique_hashes) == 1:
                print(f"  ⚠️  WARNING: Same case generated every time!")
            elif len(unique_hashes) == len(successful_results):
                print(f"  ✅ Good: Different case generated each time!")
            else:
                print(f"  ⚠️  Partial variation: Some repeated cases")
    
    # Check for cross-MCQ duplicates
    print("\n" + "-" * 80)
    print("CROSS-MCQ ANALYSIS:")
    print("-" * 80)
    
    # Group hashes by MCQ
    hash_to_mcqs = defaultdict(list)
    for mcq_id, case_hash in all_case_hashes:
        hash_to_mcqs[case_hash].append(mcq_id)
    
    # Find hashes that appear across different MCQs
    cross_mcq_duplicates = {
        hash_val: mcq_list 
        for hash_val, mcq_list in hash_to_mcqs.items() 
        if len(set(mcq_list)) > 1
    }
    
    if cross_mcq_duplicates:
        print("⚠️  CRITICAL BUG DETECTED: Different MCQs generated the same case!")
        for case_hash, mcq_list in cross_mcq_duplicates.items():
            unique_mcqs = set(mcq_list)
            print(f"  - Case hash {case_hash} generated by MCQs: {sorted(unique_mcqs)}")
    else:
        print("✅ Good: No cross-MCQ duplicates found - different MCQs generate different cases")
    
    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY:")
    print("=" * 80)
    
    total_attempts = sum(len(r) for r in results.values())
    total_successes = sum(1 for r in results.values() for result in r if result['success'])
    total_unique_cases = len(set(hash_val for _, hash_val in all_case_hashes))
    
    print(f"Total conversion attempts: {total_attempts}")
    print(f"Successful conversions: {total_successes}")
    print(f"Total unique cases generated: {total_unique_cases}")
    
    if total_unique_cases == total_successes:
        print("\n✅ EXCELLENT: Every conversion generated a unique case!")
    elif cross_mcq_duplicates:
        print("\n❌ CRITICAL: Different MCQs are generating the same cases!")
    elif total_unique_cases < total_successes:
        print("\n⚠️  WARNING: Some repeated cases detected within same MCQ")
    
    # Save detailed results
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_filename = f"case_conversion_test_report_{timestamp}.json"
    
    report_data = {
        'test_timestamp': timestamp,
        'heroku_url': HEROKU_URL,
        'test_config': {
            'mcq_ids': MCQ_IDS_TO_TEST,
            'conversions_per_mcq': CONVERSIONS_PER_MCQ
        },
        'results': {
            str(mcq_id): [
                {
                    'attempt': i,
                    'success': r['success'],
                    'case_hash': r.get('case_hash'),
                    'error': r.get('error'),
                    'response_time': r.get('response_time')
                }
                for i, r in enumerate(results[mcq_id])
            ]
            for mcq_id in MCQ_IDS_TO_TEST
        },
        'analysis': {
            'total_attempts': total_attempts,
            'total_successes': total_successes,
            'total_unique_cases': total_unique_cases,
            'cross_mcq_duplicates': [
                {'hash': h, 'mcqs': list(set(m))} 
                for h, m in cross_mcq_duplicates.items()
            ] if cross_mcq_duplicates else []
        }
    }
    
    with open(report_filename, 'w') as f:
        json.dump(report_data, f, indent=2)
    
    print(f"\nDetailed report saved to: {report_filename}")

if __name__ == "__main__":
    main()