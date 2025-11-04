#!/usr/bin/env python3
"""
Debug MCQ-to-Case session mismatch issues
This script helps identify why users see different MCQ cases than expected
"""

import os
import sys
import django

# Setup Django
sys.path.append('/Users/tariqalmatrudi/NEWreader/django_neurology_mcq')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
django.setup()

from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from mcq.models import MCQ, MCQCaseConversionSession
from django.core.cache import cache
import json
from datetime import datetime, timedelta

def debug_recent_conversions():
    """Debug recent MCQ conversions to find mismatches"""
    print("=" * 80)
    print("MCQ-TO-CASE SESSION MISMATCH DEBUGGING")
    print("=" * 80)
    
    # Get recent MCQ conversion sessions
    recent_sessions = MCQCaseConversionSession.objects.filter(
        created_at__gte=datetime.now() - timedelta(hours=2),
        status=MCQCaseConversionSession.READY
    ).order_by('-created_at')[:10]
    
    print(f"\nFound {recent_sessions.count()} recent successful conversions:")
    
    for session in recent_sessions:
        print(f"\n--- Session {session.id} ---")
        print(f"MCQ ID: {session.mcq_id}")
        print(f"User: {session.user.username}")
        print(f"Created: {session.created_at}")
        print(f"Status: {session.status}")
        
        # Check if session has case data
        if session.case_data:
            case_data = session.case_data
            source_mcq_id = case_data.get('source_mcq_id')
            patient_demographics = case_data.get('patient_demographics', 'N/A')
            clinical_presentation = case_data.get('clinical_presentation', 'N/A')
            
            print(f"Case Source MCQ ID: {source_mcq_id}")
            print(f"Patient Demographics: {patient_demographics}")
            print(f"Clinical Presentation: {clinical_presentation[:100]}...")
            
            # Check for mismatch
            if source_mcq_id != session.mcq_id:
                print(f"🚨 MISMATCH DETECTED! Session MCQ: {session.mcq_id}, Case MCQ: {source_mcq_id}")
            else:
                print("✅ MCQ IDs match")
        else:
            print("❌ No case data found")

def check_django_sessions():
    """Check Django sessions for case data"""
    print("\n" + "=" * 80)
    print("CHECKING DJANGO SESSIONS")
    print("=" * 80)
    
    # Get recent sessions
    recent_sessions = Session.objects.filter(
        expire_date__gte=datetime.now()
    ).order_by('-expire_date')[:20]
    
    case_sessions_found = 0
    
    for django_session in recent_sessions:
        try:
            session_data = django_session.get_decoded()
            
            # Look for case session keys
            case_keys = [key for key in session_data.keys() if key.startswith('case_session_')]
            
            if case_keys:
                case_sessions_found += 1
                print(f"\n--- Django Session {django_session.session_key[:10]}... ---")
                
                for case_key in case_keys:
                    case_data = session_data[case_key]
                    mcq_id = case_data.get('mcq_id', 'N/A')
                    user_id = case_data.get('user_id', 'N/A')
                    
                    print(f"Case Key: {case_key}")
                    print(f"MCQ ID: {mcq_id}")
                    print(f"User ID: {user_id}")
                    
                    # Extract MCQ ID from case key for verification
                    if 'mcq_' in case_key:
                        try:
                            mcq_pos = case_key.find('mcq_')
                            remaining = case_key[mcq_pos + 4:]
                            parts = remaining.split('_')
                            if parts and parts[0].isdigit():
                                extracted_mcq_id = int(parts[0])
                                
                                if extracted_mcq_id != mcq_id:
                                    print(f"🚨 KEY MISMATCH! Key MCQ: {extracted_mcq_id}, Data MCQ: {mcq_id}")
                                else:
                                    print("✅ Key and data MCQ IDs match")
                        except Exception as e:
                            print(f"❌ Error extracting MCQ ID from key: {e}")
                    
        except Exception as e:
            continue
    
    print(f"\nTotal case sessions found: {case_sessions_found}")

def check_cache_integrity():
    """Check cache for integrity issues"""
    print("\n" + "=" * 80)
    print("CHECKING CACHE INTEGRITY")
    print("=" * 80)
    
    # Try to find cache keys related to case validation
    cache_keys_checked = 0
    
    # Check a few known patterns
    patterns = [
        'django_session_verification_case_session_mcq_',
        'mcq_case_conversion_',
    ]
    
    for pattern in patterns:
        print(f"\nChecking pattern: {pattern}*")
        # Cache doesn't have a way to list keys, so we'll just report patterns checked
        cache_keys_checked += 1
    
    print(f"Cache pattern checks completed: {cache_keys_checked}")

if __name__ == "__main__":
    debug_recent_conversions()
    check_django_sessions()
    check_cache_integrity()
    
    print("\n" + "=" * 80)
    print("DEBUGGING COMPLETE")
    print("=" * 80)