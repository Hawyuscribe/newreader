#!/usr/bin/env python3
"""
Deep Debug: MCQ Case Generation to Display Flow

This script will trace the exact data flow from case generation to frontend display
to identify where the mismatch occurs.
"""

import sys
import os
import django
import json
import hashlib
from datetime import datetime

# Set up Django environment
sys.path.append('/Users/tariqalmatrudi/NEWreader/django_neurology_mcq')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_neurology_mcq.settings')
django.setup()

from mcq.models import MCQ, MCQCaseConversionSession
from mcq.mcq_case_converter import convert_mcq_to_case
from mcq.end_to_end_integrity import e2e_integrity
from django.contrib.auth import get_user_model
from django.test import RequestFactory
from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.sessions.models import Session

User = get_user_model()

def debug_case_flow():
    """Debug the complete case flow from generation to display"""
    
    print("🔍 DEEP DEBUG: MCQ Case Generation to Display Flow")
    print("=" * 60)
    
    # Get a test MCQ
    try:
        mcq = MCQ.objects.filter(subspecialty__isnull=False).first()
        if not mcq:
            print("❌ No MCQs found for testing")
            return
        
        user = User.objects.first()
        if not user:
            print("❌ No users found for testing")
            return
        
        print(f"🧪 Testing with MCQ {mcq.id}: {mcq.question_text[:100]}...")
        print(f"👤 User: {user.username} (ID: {user.id})")
        print()
        
        # STEP 1: Clean up existing sessions for this MCQ+User
        print("🧹 STEP 1: Cleaning up existing sessions...")
        
        # Delete existing conversion sessions
        existing_sessions = MCQCaseConversionSession.objects.filter(mcq=mcq, user=user)
        print(f"   Found {existing_sessions.count()} existing conversion sessions")
        for session in existing_sessions:
            print(f"   - Session {session.id}: Status {session.status}")
            session.delete()
        
        # Create mock request for session handling
        factory = RequestFactory()
        request = factory.get('/')
        request.user = user
        
        # Add session middleware
        middleware = SessionMiddleware(lambda req: None)
        middleware.process_request(request)
        request.session.save()
        
        # Clear any existing Django session data for this MCQ+User
        session_keys_to_clear = []
        for key in list(request.session.keys()):
            if f'case_session_mcq_{mcq.id}_' in key and f'_{user.id}' in key:
                session_keys_to_clear.append(key)
        
        for key in session_keys_to_clear:
            del request.session[key]
            print(f"   Cleared Django session key: {key}")
        
        print("   ✅ Cleanup complete")
        print()
        
        # STEP 2: Generate new case using the converter
        print("🎯 STEP 2: Generating new case...")
        
        try:
            case_data = convert_mcq_to_case(mcq, include_debug=True)
            print(f"   ✅ Case generation successful!")
            print(f"   📋 Generated case preview:")
            print(f"      Source MCQ ID: {case_data.get('source_mcq_id')}")
            print(f"      Patient: {case_data.get('patient_demographics', 'Unknown')}")
            print(f"      Clinical: {case_data.get('clinical_presentation', '')[:100]}...")
            print(f"      Concept: {case_data.get('core_concept_type', 'Unknown')}")
            
            # Generate a fingerprint of the case content
            case_fingerprint = hashlib.md5(
                str(case_data.get('clinical_presentation', '')).encode()
            ).hexdigest()[:10]
            print(f"      Content Fingerprint: {case_fingerprint}")
            print()
            
        except Exception as e:
            print(f"   ❌ Case generation failed: {e}")
            return
        
        # STEP 3: Simulate the MCQ-to-case learning view flow
        print("🔄 STEP 3: Simulating MCQ-to-case conversion view...")
        
        # Create a new conversion session (like the view does)
        conversion_session = e2e_integrity.create_secure_conversion_session(mcq, user)
        print(f"   Created conversion session: {conversion_session.id}")
        
        # Store the case data (like the background task does)
        conversion_session.case_data = case_data
        conversion_session.status = MCQCaseConversionSession.READY
        conversion_session.save()
        
        e2e_integrity.store_case_with_integrity(conversion_session, case_data)
        print(f"   ✅ Case data stored in conversion session")
        print()
        
        # STEP 4: Simulate Django session transfer
        print("🔗 STEP 4: Transferring to Django session...")
        
        success, django_session_key, error = e2e_integrity.transfer_to_django_session(request, conversion_session)
        
        if not success:
            print(f"   ❌ Django session transfer failed: {error}")
            return
        
        print(f"   ✅ Django session transfer successful")
        print(f"   🔑 Django session key: {django_session_key}")
        print()
        
        # STEP 5: Verify what's actually stored in Django session
        print("🔍 STEP 5: Verifying Django session contents...")
        
        django_session_data = request.session.get(django_session_key)
        if not django_session_data:
            print(f"   ❌ No data found for Django session key: {django_session_key}")
            return
        
        stored_case_data = django_session_data.get('case_data', {})
        stored_fingerprint = hashlib.md5(
            str(stored_case_data.get('clinical_presentation', '')).encode()
        ).hexdigest()[:10]
        
        print(f"   ✅ Django session data found")
        print(f"   📋 Stored case preview:")
        print(f"      Source MCQ ID: {stored_case_data.get('source_mcq_id')}")
        print(f"      Patient: {stored_case_data.get('patient_demographics', 'Unknown')}")
        print(f"      Clinical: {stored_case_data.get('clinical_presentation', '')[:100]}...")
        print(f"      Concept: {stored_case_data.get('core_concept_type', 'Unknown')}")
        print(f"      Content Fingerprint: {stored_fingerprint}")
        print()
        
        # STEP 6: Compare fingerprints
        print("🔍 STEP 6: Data integrity verification...")
        
        if case_fingerprint == stored_fingerprint:
            print("   ✅ INTEGRITY CHECK PASSED: Generated and stored cases match")
        else:
            print("   ❌ INTEGRITY CHECK FAILED: Generated and stored cases differ!")
            print(f"      Generated fingerprint: {case_fingerprint}")
            print(f"      Stored fingerprint: {stored_fingerprint}")
        print()
        
        # STEP 7: Simulate the resume_case_session view
        print("🎬 STEP 7: Simulating case session resume...")
        
        from mcq.end_to_end_integrity import e2e_integrity
        is_valid, retrieved_case_data, error_message = e2e_integrity.validate_case_before_serving(
            request, django_session_key, mcq.id, user
        )
        
        if not is_valid:
            print(f"   ❌ Case validation failed: {error_message}")
            return
        
        retrieved_fingerprint = hashlib.md5(
            str(retrieved_case_data.get('clinical_presentation', '')).encode()
        ).hexdigest()[:10]
        
        print(f"   ✅ Case validation successful")
        print(f"   📋 Retrieved case preview:")
        print(f"      Source MCQ ID: {retrieved_case_data.get('source_mcq_id')}")
        print(f"      Patient: {retrieved_case_data.get('patient_demographics', 'Unknown')}")
        print(f"      Clinical: {retrieved_case_data.get('clinical_presentation', '')[:100]}...")
        print(f"      Concept: {retrieved_case_data.get('core_concept_type', 'Unknown')}")
        print(f"      Content Fingerprint: {retrieved_fingerprint}")
        print()
        
        # STEP 8: Final integrity check
        print("🎯 STEP 8: Final end-to-end integrity check...")
        
        all_fingerprints = [case_fingerprint, stored_fingerprint, retrieved_fingerprint]
        unique_fingerprints = set(all_fingerprints)
        
        print(f"   Generated case fingerprint:  {case_fingerprint}")
        print(f"   Stored case fingerprint:     {stored_fingerprint}")
        print(f"   Retrieved case fingerprint:  {retrieved_fingerprint}")
        print()
        
        if len(unique_fingerprints) == 1:
            print("   ✅ PERFECT INTEGRITY: All cases identical throughout the flow")
        else:
            print("   ❌ INTEGRITY BREACH: Cases differ at some point in the flow")
            print(f"   🔍 Unique fingerprints found: {unique_fingerprints}")
        
        # STEP 9: Generate multiple cases to check for repetition
        print()
        print("🔄 STEP 9: Testing for case repetition...")
        
        fingerprints = []
        for i in range(5):
            try:
                test_case = convert_mcq_to_case(mcq, include_debug=False)
                test_fingerprint = hashlib.md5(
                    str(test_case.get('clinical_presentation', '')).encode()
                ).hexdigest()[:10]
                fingerprints.append(test_fingerprint)
                print(f"   Test case {i+1}: {test_fingerprint} - {test_case.get('clinical_presentation', '')[:50]}...")
            except Exception as e:
                print(f"   Test case {i+1}: FAILED - {e}")
        
        unique_test_fingerprints = set(fingerprints)
        print(f"   📊 Generated {len(fingerprints)} cases, {len(unique_test_fingerprints)} unique")
        
        if len(unique_test_fingerprints) == len(fingerprints):
            print("   ✅ EXCELLENT: All generated cases are unique")
        elif len(unique_test_fingerprints) > len(fingerprints) * 0.8:
            print("   ⚠️  GOOD: Most generated cases are unique")
        else:
            print("   ❌ POOR: Many generated cases are repetitive")
        
        print()
        print("🎯 SUMMARY:")
        print(f"   MCQ ID: {mcq.id}")
        print(f"   Django Session Key: {django_session_key}")
        print(f"   Case Integrity: {'✅ PERFECT' if len(unique_fingerprints) == 1 else '❌ COMPROMISED'}")
        print(f"   Case Uniqueness: {len(unique_test_fingerprints)}/{len(fingerprints)} unique")
        
        return {
            'mcq_id': mcq.id,
            'django_session_key': django_session_key,
            'integrity_perfect': len(unique_fingerprints) == 1,
            'uniqueness_ratio': len(unique_test_fingerprints) / len(fingerprints) if fingerprints else 0,
            'all_fingerprints': all_fingerprints,
            'test_fingerprints': fingerprints
        }
        
    except Exception as e:
        print(f"❌ Debug failed: {e}")
        import traceback
        print(traceback.format_exc())
        return None

if __name__ == "__main__":
    debug_case_flow()