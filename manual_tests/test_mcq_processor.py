#!/usr/bin/env python3
"""
Test script for MCQ Processor
Tests the MCQ processing functionality with a sample MCQ.
"""

import json
import os
import sys
from pathlib import Path
import tempfile

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from mcq_processor import MCQProcessor


def create_test_mcq():
    """Create a test MCQ file."""
    test_mcq = {
        "specialty": "Test",
        "total_mcqs": 1,
        "mcqs": [
            {
                "question_number": "1",
                "question": "A 45-year-old patient presents with sudden onset severe headache, neck stiffness, and photophobia. CT scan shows blood in the subarachnoid space. What is the most likely diagnosis?",
                "options": [
                    "Migraine headache",
                    "Subarachnoid hemorrhage",
                    "Meningitis",
                    "Tension headache"
                ],
                "correct_answer": "A",  # Intentionally wrong for testing
                "correct_answer_text": "Migraine headache",
                "explanation": {
                    "option_analysis": "This explanation incorrectly states migraine is correct.",
                    "conceptual_foundation": "Needs updating",
                    "pathophysiology": "Incomplete",
                    "clinical_manifestation": "Missing key features",
                    "diagnostic_approach": "Needs revision",
                    "management_principles": "Outdated",
                    "follow_up_guidelines": "Insufficient",
                    "clinical_pearls": ["Needs updating"],
                    "references": "Old references"
                }
            }
        ]
    }
    
    return test_mcq


def test_processor():
    """Test the MCQ processor."""
    print("MCQ Processor Test Script")
    print("=" * 50)
    
    # Check API key
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("ERROR: Please set OPENAI_API_KEY environment variable")
        print("Example: export OPENAI_API_KEY='your-key-here'")
        return
    
    print("✓ API key found")
    
    # Create temporary directories
    with tempfile.TemporaryDirectory() as temp_dir:
        input_dir = Path(temp_dir) / "input"
        output_dir = Path(temp_dir) / "output"
        input_dir.mkdir()
        output_dir.mkdir()
        
        # Create test MCQ file
        test_file = input_dir / "test_mcqs.json"
        test_data = create_test_mcq()
        
        with open(test_file, 'w') as f:
            json.dump(test_data, f, indent=2)
        
        print(f"✓ Created test MCQ file: {test_file}")
        print("\nTest MCQ Details:")
        print(f"  Question: {test_data['mcqs'][0]['question'][:80]}...")
        print(f"  Current Answer: {test_data['mcqs'][0]['correct_answer']} - {test_data['mcqs'][0]['correct_answer_text']}")
        print("  (This is intentionally wrong to test correction)")
        
        # Initialize processor
        print("\n" + "=" * 50)
        print("Initializing MCQ Processor...")
        
        try:
            processor = MCQProcessor(api_key, str(input_dir), str(output_dir))
            print("✓ Processor initialized")
            
            # Process test file
            print("\nProcessing test MCQ with O3-mini high reasoning mode...")
            print("This may take a moment...")
            
            result = processor.process_file(test_file)
            
            print("\n" + "=" * 50)
            print("Processing Results:")
            print(f"  Status: {result['status']}")
            print(f"  Total MCQs: {result.get('total', 0)}")
            print(f"  Corrected: {result.get('corrected', 0)}")
            
            # Check output
            output_file = output_dir / "test_mcqs.json"
            if output_file.exists():
                with open(output_file, 'r') as f:
                    processed_data = json.load(f)
                
                processed_mcq = processed_data['mcqs'][0]
                
                print("\nProcessed MCQ:")
                print(f"  Correct Answer: {processed_mcq['correct_answer']} - {processed_mcq['correct_answer_text']}")
                print(f"  Was Corrected: {processed_mcq.get('ai_corrected', False)}")
                
                if processed_mcq.get('ai_corrected'):
                    print(f"  Correction Details: {processed_mcq.get('correction_details', 'N/A')}")
                
                print("\nUpdated Explanation Sections:")
                for section, content in processed_mcq['explanation'].items():
                    if isinstance(content, list):
                        print(f"  {section}: {len(content)} items")
                    else:
                        print(f"  {section}: {len(str(content))} characters")
                
                print("\n✓ Test completed successfully!")
                
                # Save example output
                example_output = Path("test_output_example.json")
                with open(example_output, 'w') as f:
                    json.dump(processed_data, f, indent=2)
                print(f"\n✓ Example output saved to: {example_output}")
                
            else:
                print("\n✗ Output file not found")
                
        except Exception as e:
            print(f"\n✗ Error during processing: {str(e)}")
            import traceback
            traceback.print_exc()
    
    print("\n" + "=" * 50)
    print("Test complete!")


def check_dependencies():
    """Check if required dependencies are installed."""
    print("Checking dependencies...")
    
    required = ['openai', 'tiktoken', 'backoff']
    missing = []
    
    for package in required:
        try:
            __import__(package)
            print(f"✓ {package} installed")
        except ImportError:
            print(f"✗ {package} not installed")
            missing.append(package)
    
    if missing:
        print(f"\nInstalling missing packages: {', '.join(missing)}")
        os.system(f"{sys.executable} -m pip install {' '.join(missing)}")
        print("✓ Dependencies installed")
    
    return len(missing) == 0


if __name__ == "__main__":
    print("MCQ Processor Test Script")
    print("=" * 50 + "\n")
    
    # Check dependencies
    if not check_dependencies():
        print("\nDependencies were installed. Please run the script again.")
        sys.exit(1)
    
    print()
    
    # Run test
    test_processor()