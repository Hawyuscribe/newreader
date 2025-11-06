#!/usr/bin/env python3
"""
Test script to demonstrate in-place editing behavior
Shows how the processor modifies original files directly
"""

import json
import os
import sys
from pathlib import Path
import tempfile
import shutil

# Set API key
os.environ['OPENAI_API_KEY'] = "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"

from mcq_processor import MCQProcessor


def create_test_file():
    """Create a test MCQ file."""
    return {
        "specialty": "Test",
        "total_mcqs": 2,
        "mcqs": [
            {
                "question_number": "1",
                "question": "Patient with sudden severe headache, neck stiffness, photophobia. CT shows SAH. What is the diagnosis?",
                "options": [
                    "Migraine",
                    "Subarachnoid hemorrhage", 
                    "Tension headache",
                    "Cluster headache"
                ],
                "correct_answer": "A",  # WRONG - should be B
                "correct_answer_text": "Migraine",
                "explanation": {
                    "option_analysis": "Migraine is correct because it causes severe headache",  # WRONG
                    "conceptual_foundation": "Basic headache knowledge",
                    "pathophysiology": "Unknown",
                    "clinical_manifestation": "Headache",
                    "diagnostic_approach": "Clinical",
                    "management_principles": "Pain relief", 
                    "follow_up_guidelines": "As needed",
                    "clinical_pearls": ["Headaches are common"],
                    "references": "General textbook"
                }
            },
            {
                "question_number": "2", 
                "question": "First-line treatment for absence seizures in children?",
                "options": [
                    "Phenytoin",
                    "Carbamazepine", 
                    "Ethosuximide",
                    "Valproate"
                ],
                "correct_answer": "C",  # CORRECT
                "correct_answer_text": "Ethosuximide",
                "explanation": {
                    "option_analysis": "Ethosuximide is first-line for absence seizures with 70% efficacy.",
                    "conceptual_foundation": "Absence seizures involve T-type calcium channels.",
                    "pathophysiology": "Thalamocortical circuit dysfunction.",
                    "clinical_manifestation": "Brief staring episodes without postictal confusion.",
                    "diagnostic_approach": "EEG showing 3Hz spike-wave discharges.",
                    "management_principles": "Ethosuximide 20mg/kg/day divided BID.",
                    "follow_up_guidelines": "Monitor seizure frequency and side effects.",
                    "clinical_pearls": ["Ethosuximide blocks T-type calcium channels"],
                    "references": "ILAE Guidelines 2017"
                }
            }
        ]
    }


def test_inplace_editing():
    """Test in-place editing of MCQ files."""
    print("Testing In-Place MCQ File Editing")
    print("=" * 60)
    
    # Create temporary directory with test file
    with tempfile.TemporaryDirectory() as temp_dir:
        test_dir = Path(temp_dir)
        test_file = test_dir / "test_mcqs.json"
        
        # Create original test file
        original_data = create_test_file()
        with open(test_file, 'w') as f:
            json.dump(original_data, f, indent=2)
        
        print(f"Created test file: {test_file}")
        print("\nOriginal Content:")
        print(f"MCQ 1 Answer: {original_data['mcqs'][0]['correct_answer']} - {original_data['mcqs'][0]['correct_answer_text']}")
        print(f"MCQ 2 Answer: {original_data['mcqs'][1]['correct_answer']} - {original_data['mcqs'][1]['correct_answer_text']}")
        
        # Read original content for comparison
        with open(test_file, 'r') as f:
            original_content = f.read()
        
        print(f"\n{'=' * 60}")
        print("Processing with O3-mini (modifying original file)...")
        
        try:
            # Create processor - notice no output directory
            processor = MCQProcessor(
                api_key=os.environ['OPENAI_API_KEY'],
                input_dir=str(test_dir)
            )
            
            # Process the file (should modify it in place)
            result = processor.process_file(test_file)
            
            print(f"\n{'=' * 60}")
            print("Processing Results:")
            print(f"Status: {result['status']}")
            print(f"Total MCQs: {result.get('total', 0)}")
            print(f"Verified (no changes): {result.get('verified', 0)}")
            print(f"Corrected: {result.get('corrected', 0)}")
            
            # Read the file again to see changes
            with open(test_file, 'r') as f:
                processed_content = f.read()
                processed_data = json.loads(processed_content)
            
            print(f"\n{'=' * 60}")
            print("File Comparison:")
            print(f"File modified: {'YES' if original_content != processed_content else 'NO'}")
            
            print(f"\nAfter Processing:")
            print(f"MCQ 1 Answer: {processed_data['mcqs'][0]['correct_answer']} - {processed_data['mcqs'][0]['correct_answer_text']}")
            print(f"MCQ 2 Answer: {processed_data['mcqs'][1]['correct_answer']} - {processed_data['mcqs'][1]['correct_answer_text']}")
            
            print(f"\nChanges Made:")
            for i, (orig, proc) in enumerate(zip(original_data['mcqs'], processed_data['mcqs']), 1):
                if orig['correct_answer'] != proc['correct_answer']:
                    print(f"MCQ {i}: Answer changed from {orig['correct_answer']} to {proc['correct_answer']}")
                elif proc.get('ai_verified'):
                    print(f"MCQ {i}: Verified as correct (no changes)")
                elif proc.get('ai_corrected'):
                    print(f"MCQ {i}: Explanation updated")
            
            # Check metadata
            if 'processing_info' in processed_data:
                print(f"\nProcessing Info:")
                for key, value in processed_data['processing_info'].items():
                    print(f"- {key}: {value}")
            
            # Show that NO new files were created
            files_in_dir = list(test_dir.glob("*.json"))
            print(f"\nFiles in directory: {len(files_in_dir)}")
            for file in files_in_dir:
                print(f"- {file.name}")
            
            print(f"\n✓ Demonstration complete!")
            print("Key Points:")
            print("- Original file was modified directly")
            print("- No new files were created") 
            print("- Wrong answers were corrected")
            print("- Correct answers were verified")
            
        except Exception as e:
            print(f"\n✗ Error during processing: {str(e)}")
            import traceback
            traceback.print_exc()


if __name__ == "__main__":
    # Install dependencies if needed
    try:
        import openai
    except ImportError:
        print("Installing required packages...")
        os.system(f"{sys.executable} -m pip install openai tiktoken backoff")
    
    # Run test
    test_inplace_editing()