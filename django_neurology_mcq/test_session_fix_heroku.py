#!/usr/bin/env python
"""
Comprehensive test for MCQ-case session fix on Heroku
Run this with: heroku run python test_session_fix_heroku.py
"""

import os
import sys
import django
from datetime import datetime

# Django setup
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
django.setup()

from mcq.models import MCQ, MCQCaseConversionSession
from django.contrib.auth.models import User
from mcq.end_to_end_integrity import e2e_integrity
from django.test import RequestFactory
from django.contrib.sessions.middleware import SessionMiddleware
from mcq.views import mcq_to_case_learning
import json

def test_mcq_case_session_fix():
    """Test the complete MCQ to case conversion flow with session fix"""
    print("🧪 Testing MCQ-Case Session Fix on Heroku")
    print("=" * 60)
    
    try:
        # Test Case 1: Find a specific MCQ (like the one reported)
        test_mcq_ids = [100480663, 100484440, 100420848]  # MCQs from user reports
        
        mcq = None
        for mcq_id in test_mcq_ids:
            try:
                mcq = MCQ.objects.get(id=mcq_id)
                print(f"✅ Found test MCQ {mcq_id}")
                break
            except MCQ.DoesNotExist:
                continue
        
        if not mcq:
            # Fallback to any MCQ
            mcq = MCQ.objects.filter(subspecialty__isnull=False).first()
            if not mcq:
                print("❌ No suitable MCQs found in database")
                return False
        
        print(f"📝 Testing with MCQ {mcq.id}: {mcq.subspecialty}")
        print(f"📄 Question preview: {mcq.question_text[:100]}...")
        
        # Get admin user
        user = User.objects.filter(is_superuser=True).first()
        if not user:
            user = User.objects.first()
        
        print(f"👤 Using user: {user.username} (ID: {user.id})")
        
        # Test 1: Session Key Generation
        print("\n📋 Test 1: Session Key Format")
        print("-" * 40)
        
        # Create test session
        test_session = MCQCaseConversionSession.objects.create(
            mcq=mcq,
            user=user,
            status=MCQCaseConversionSession.READY,
            case_data={'test': True}
        )
        
        expected_key = f"case_session_mcq_{mcq.id}_{test_session.id}_{user.id}"
        generated_key = e2e_integrity._generate_secure_django_session_key(test_session)
        
        print(f"Expected: {expected_key}")
        print(f"Generated: {generated_key}")
        
        if expected_key == generated_key:
            print("✅ Session key format is correct!")
        else:
            print("❌ Session key format mismatch!")
            test_session.delete()
            return False
        
        test_session.delete()
        
        # Test 2: MCQ Conversion Endpoint
        print("\n📋 Test 2: MCQ Conversion Endpoint")
        print("-" * 40)
        
        # Clean up any existing sessions for this test
        MCQCaseConversionSession.objects.filter(
            mcq=mcq,
            user=user
        ).delete()
        
        # Create a mock request
        factory = RequestFactory()
        request = factory.post(f'/mcq/{mcq.id}/convert-to-case/')
        request.user = user
        
        # Add session middleware
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()
        
        # Test the conversion endpoint
        response = mcq_to_case_learning(request, mcq.id)
        response_data = json.loads(response.content)
        
        print(f"Response status: {response.status_code}")
        print(f"Response data: {json.dumps(response_data, indent=2)}")
        
        if response.status_code == 200 and response_data.get('success'):
            print("✅ Conversion endpoint working!")
            
            # Check for session_key in response
            if response_data.get('status') == 'ready':
                if 'session_key' in response_data:
                    print(f"✅ Session key included: {response_data['session_key']}")
                else:
                    print("❌ Session key missing from ready response!")
                    return False
        else:
            print("❌ Conversion endpoint failed!")
            return False
        
        # Test 3: Session Key Validation
        print("\n📋 Test 3: Session Key Validation")
        print("-" * 40)
        
        # Get the created session
        session = MCQCaseConversionSession.objects.filter(
            mcq=mcq,
            user=user
        ).order_by('-created_at').first()
        
        if session:
            print(f"Found session ID: {session.id}")
            print(f"Session status: {session.status}")
            
            # Test session transfer
            success, case_session_key, error = e2e_integrity.transfer_to_django_session(request, session)
            
            if success:
                print(f"✅ Session transfer successful!")
                print(f"Generated session key: {case_session_key}")
                
                # Verify key format
                if case_session_key.startswith('case_session_mcq_'):
                    parts = case_session_key.split('_')
                    if len(parts) >= 5:
                        extracted_mcq_id = parts[3]
                        extracted_session_id = parts[4]
                        extracted_user_id = parts[5] if len(parts) > 5 else 'unknown'
                        
                        print(f"  MCQ ID in key: {extracted_mcq_id} (expected: {mcq.id})")
                        print(f"  Session ID in key: {extracted_session_id} (expected: {session.id})")
                        print(f"  User ID in key: {extracted_user_id} (expected: {user.id})")
                        
                        if (str(mcq.id) == extracted_mcq_id and 
                            str(session.id) == extracted_session_id):
                            print("✅ Session key components match!")
                        else:
                            print("❌ Session key component mismatch!")
                            return False
                else:
                    print("❌ Session key has wrong format!")
                    return False
            else:
                print(f"❌ Session transfer failed: {error}")
                return False
        
        # Test 4: Case Content Verification
        print("\n📋 Test 4: Case Content Verification")
        print("-" * 40)
        
        if session and session.case_data:
            case_data = session.case_data
            print(f"Source MCQ ID in case: {case_data.get('source_mcq_id')}")
            print(f"Core concept: {case_data.get('core_concept_type', 'N/A')[:50]}...")
            
            if case_data.get('source_mcq_id') == mcq.id:
                print("✅ Case data linked to correct MCQ!")
            else:
                print("❌ Case data MCQ ID mismatch!")
                return False
            
            # Check clinical presentation
            clinical_pres = case_data.get('clinical_presentation', '')
            if clinical_pres:
                print(f"Clinical presentation preview: {clinical_pres[:100]}...")
                print("✅ Case has clinical presentation!")
            else:
                print("⚠️  No clinical presentation found")
        
        print("\n" + "=" * 60)
        print("🎯 CONCLUSION: Session fix is working correctly!")
        print("\nThe fix ensures:")
        print("1. Session keys use full format (case_session_mcq_X_Y_Z)")
        print("2. Immediate ready responses include session_key")
        print("3. Case data is properly linked to source MCQ")
        print("\n✅ MCQ-case mismatches should now be resolved!")
        
        # Cleanup
        if session:
            session.delete()
            print("\n🧹 Cleaned up test session")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    # Run the test
    success = test_mcq_case_session_fix()
    
    # Exit with appropriate code
    sys.exit(0 if success else 1)