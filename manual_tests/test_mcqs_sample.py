#!/usr/bin/env python3
"""
Test MCQ Processor with sample MCQs from the actual dataset
"""

import json
import os
import sys
from pathlib import Path
import tempfile

# Set API key
os.environ['OPENAI_API_KEY'] = "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"

from mcq_processor import MCQProcessor


def extract_sample_mcqs():
    """Extract a couple of MCQs from the actual files for testing."""
    # Read epilepsy MCQs file
    epilepsy_file = Path("/Users/tariqalmatrudi/Documents/FFF/output_by_specialty/epilepsy_mcqs.json")
    
    if not epilepsy_file.exists():
        print(f"Error: File not found: {epilepsy_file}")
        return None
    
    with open(epilepsy_file, 'r') as f:
        data = json.load(f)
    
    # Extract first 2 MCQs for testing
    sample_mcqs = {
        "specialty": data["specialty"],
        "total_mcqs": 2,
        "source_files": data.get("source_files", []),
        "mcqs": data["mcqs"][:2]  # Get first 2 MCQs
    }
    
    return sample_mcqs


def test_sample_mcqs():
    """Test the processor with real MCQs."""
    print("Testing MCQ Processor with Sample MCQs")
    print("=" * 70)
    
    # Extract sample MCQs
    sample_data = extract_sample_mcqs()
    if not sample_data:
        return
    
    print(f"Extracted {len(sample_data['mcqs'])} MCQs from {sample_data['specialty']} specialty")
    
    # Display the MCQs we're testing
    for i, mcq in enumerate(sample_data['mcqs'], 1):
        print(f"\nMCQ {i}:")
        print(f"Question: {mcq['question'][:100]}...")
        print(f"Current Answer: {mcq['correct_answer']} - {mcq['correct_answer_text']}")
    
    # Create temporary directories
    with tempfile.TemporaryDirectory() as temp_dir:
        input_dir = Path(temp_dir) / "input"
        output_dir = Path(temp_dir) / "output"
        input_dir.mkdir()
        output_dir.mkdir()
        
        # Save sample MCQs
        test_file = input_dir / "epilepsy_test_sample.json"
        with open(test_file, 'w') as f:
            json.dump(sample_data, f, indent=2)
        
        print(f"\n{'=' * 70}")
        print("Processing MCQs with O3-mini high reasoning mode...")
        print("This may take a moment...\n")
        
        try:
            # Initialize processor
            processor = MCQProcessor(
                api_key=os.environ['OPENAI_API_KEY'],
                input_dir=str(input_dir),
                output_dir=str(output_dir)
            )
            
            # Process the test file
            result = processor.process_file(test_file)
            
            print(f"\n{'=' * 70}")
            print("Processing Results:")
            print(f"Status: {result['status']}")
            print(f"Total MCQs: {result.get('total', 0)}")
            print(f"Corrected: {result.get('corrected', 0)}")
            
            # Load and display results
            output_file = output_dir / "epilepsy_test_sample.json"
            if output_file.exists():
                with open(output_file, 'r') as f:
                    processed_data = json.load(f)
                
                print(f"\n{'=' * 70}")
                print("Detailed Results:\n")
                
                for i, mcq in enumerate(processed_data['mcqs'], 1):
                    print(f"MCQ {i}:")
                    print(f"Question: {mcq['question'][:100]}...")
                    print(f"Original Answer: {sample_data['mcqs'][i-1]['correct_answer']} - {sample_data['mcqs'][i-1]['correct_answer_text']}")
                    print(f"Processed Answer: {mcq['correct_answer']} - {mcq['correct_answer_text']}")
                    print(f"Was Corrected: {mcq.get('ai_corrected', False)}")
                    
                    if mcq.get('ai_corrected'):
                        print(f"Correction Details: {mcq.get('correction_details', 'N/A')}")
                    
                    print(f"\nUpdated Explanation Preview:")
                    print(f"- Option Analysis: {mcq['explanation']['option_analysis'][:150]}...")
                    print(f"- Clinical Pearls: {len(mcq['explanation'].get('clinical_pearls', []))} items")
                    print("-" * 70)
                
                # Save output for review
                review_file = Path("processed_sample_mcqs.json")
                with open(review_file, 'w') as f:
                    json.dump(processed_data, f, indent=2)
                print(f"\n✓ Full processed output saved to: {review_file}")
                
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
    test_sample_mcqs()