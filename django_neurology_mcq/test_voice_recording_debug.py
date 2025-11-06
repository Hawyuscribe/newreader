#!/usr/bin/env python3
"""
Test script to debug voice recording issues in Clinical Reasoning modal
"""

import requests
import os
import tempfile
import json

def test_transcription_endpoint():
    """Test the /api/transcribe-audio/ endpoint directly"""
    print("🔍 Testing voice transcription endpoint...")
    
    # Create a small test audio file (empty for testing structure)
    with tempfile.NamedTemporaryFile(suffix='.webm', delete=False) as temp_file:
        # Write some basic bytes to simulate an audio file
        temp_file.write(b'mock_audio_data')
        temp_file_path = temp_file.name
    
    try:
        # Test the endpoint structure
        url = 'https://radiant-gorge-35079-2b52ba172c1e.herokuapp.com/api/transcribe-audio/'
        
        # Prepare form data as the JavaScript would
        files = {
            'audio': ('recording.webm', open(temp_file_path, 'rb'), 'audio/webm')
        }
        data = {
            'mimeType': 'audio/webm'
        }
        
        # Test without CSRF first to see if it's a permission issue
        print(f"🌐 Making request to: {url}")
        response = requests.post(url, files=files, data=data)
        
        print(f"📊 Status Code: {response.status_code}")
        print(f"📊 Headers: {dict(response.headers)}")
        
        try:
            response_data = response.json()
            print(f"📊 Response Data: {response_data}")
        except:
            print(f"📊 Response Text: {response.text[:500]}...")
            
        # Check if it's a CSRF issue
        if response.status_code == 403:
            print("🚨 CSRF token required - this is expected for authenticated endpoints")
        elif response.status_code == 405:
            print("🚨 Method not allowed - endpoint may not exist")
        elif response.status_code == 500:
            print("🚨 Server error - check server logs for details")
        elif response.status_code == 400:
            print("🚨 Bad request - check request format")
        
    except Exception as e:
        print(f"❌ Error testing endpoint: {e}")
    finally:
        # Clean up
        if os.path.exists(temp_file_path):
            os.unlink(temp_file_path)

def check_case_learning_endpoint():
    """Check if case-based learning endpoint is accessible"""
    print("\n🔍 Testing case-based learning page...")
    
    try:
        url = 'https://radiant-gorge-35079-2b52ba172c1e.herokuapp.com/case-based-learning/'
        response = requests.get(url)
        
        print(f"📊 Case Learning Status: {response.status_code}")
        
        if response.status_code == 200:
            # Check if the transcription endpoint is referenced in the page
            if '/api/transcribe-audio/' in response.text:
                print("✅ Transcription endpoint is referenced in case-based learning")
            else:
                print("❌ Transcription endpoint NOT found in case-based learning")
                
    except Exception as e:
        print(f"❌ Error checking case learning: {e}")

def analyze_javascript_implementation():
    """Analyze the JavaScript implementation differences"""
    print("\n🔍 Analyzing JavaScript implementation...")
    
    # Read the current mcq_detail.html to check the implementation
    try:
        mcq_detail_path = '/Users/tariqalmatrudi/NEWreader/django_neurology_mcq/templates/mcq/mcq_detail.html'
        with open(mcq_detail_path, 'r') as f:
            content = f.read()
            
        # Check for key implementation elements
        checks = [
            ('/api/transcribe-audio/', 'Transcription endpoint'),
            ('ClinicalReasoningAnalyzer', 'Clinical Reasoning class'),
            ('startRecording()', 'Start recording function'),
            ('processRecording()', 'Process recording function'),
            ('MediaRecorder', 'MediaRecorder API'),
            ("'audio/webm'", 'WebM MIME type'),
            ('X-CSRFToken', 'CSRF token header')
        ]
        
        for pattern, description in checks:
            if pattern in content:
                print(f"✅ {description}: Found")
            else:
                print(f"❌ {description}: Missing")
                
        # Check for potential issues
        if 'recordBtn' in content and 'start-recording-btn' in content:
            print("⚠️  Multiple button IDs detected - potential conflict")
            
    except Exception as e:
        print(f"❌ Error analyzing JavaScript: {e}")

if __name__ == "__main__":
    print("🚀 Starting voice recording debug analysis...\n")
    
    test_transcription_endpoint()
    check_case_learning_endpoint()
    analyze_javascript_implementation()
    
    print("\n✅ Debug analysis complete!")
    print("\n💡 Recommendations:")
    print("1. Check server logs for detailed error messages")
    print("2. Test with valid CSRF token from authenticated session")
    print("3. Verify OpenAI API key is properly configured")
    print("4. Test with actual audio file in supported format")