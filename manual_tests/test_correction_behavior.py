#!/usr/bin/env python3
"""
Test script to demonstrate MCQ correction behavior
Shows how the processor handles correct vs incorrect MCQs
"""

import json
import os
import sys
from pathlib import Path
import tempfile

# Set API key
os.environ['OPENAI_API_KEY'] = "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"

from mcq_processor import MCQProcessor


def create_test_mcqs():
    """Create test MCQs with different scenarios."""
    return {
        "specialty": "Test Cases",
        "total_mcqs": 3,
        "mcqs": [
            {
                "question_number": "1",
                "question": "A patient with sudden onset severe headache, neck stiffness, and photophobia. CT shows blood in subarachnoid space. Diagnosis?",
                "options": [
                    "Migraine headache",
                    "Subarachnoid hemorrhage",
                    "Bacterial meningitis",
                    "Tension headache"
                ],
                "correct_answer": "A",  # WRONG - should be B
                "correct_answer_text": "Migraine headache",
                "explanation": {
                    "option_analysis": "Migraine is the correct answer because it causes severe headaches.",  # WRONG explanation
                    "conceptual_foundation": "Headaches have many causes",
                    "pathophysiology": "Unknown mechanism",
                    "clinical_manifestation": "Severe headache",
                    "diagnostic_approach": "Clinical diagnosis",
                    "management_principles": "Pain relief",
                    "follow_up_guidelines": "As needed",
                    "clinical_pearls": ["Headaches are common"],
                    "references": "General neurology textbook"
                }
            },
            {
                "question_number": "2",
                "question": "What medicaton is first-line for absence seizures in children?",  # Intentional typo
                "options": [
                    "Phenytoin",
                    "Carbamazepine",
                    "Ethosuximide",
                    "Phenobarbital"
                ],
                "correct_answer": "C",  # CORRECT
                "correct_answer_text": "Ethosuximide",
                "explanation": {
                    "option_analysis": "Ethosuximide is the first-line treatment for absence seizures, with 70% efficacy. Phenytoin and carbamazepine can worsen absence seizures. Phenobarbital is second-line.",
                    "conceptual_foundation": "Absence seizures are generalized seizures with 3Hz spike-wave on EEG. T-type calcium channels are involved in their pathophysiology.",
                    "pathophysiology": "Thalamocortical circuit dysfunction with abnormal T-type calcium channel activity leads to synchronized 3Hz discharges.",
                    "clinical_manifestation": "Brief episodes of staring, unresponsiveness lasting 5-10 seconds, multiple times daily. No postictal confusion.",
                    "diagnostic_approach": "EEG showing 3Hz generalized spike-wave discharges. Hyperventilation can provoke absence seizures during EEG.",
                    "management_principles": "Ethosuximide 20mg/kg/day divided BID. Valproate is alternative if ethosuximide fails.",
                    "follow_up_guidelines": "Monitor seizure frequency, EEG at 6 months, check for side effects (GI upset, drowsiness).",
                    "clinical_pearls": [
                        "Ethosuximide specifically blocks T-type calcium channels",
                        "Never use phenytoin or carbamazepine for absence seizures",
                        "Most children outgrow absence epilepsy by adolescence"
                    ],
                    "references": "ILAE Guidelines 2017; Glauser et al, Epilepsia 2013"
                }
            },
            {
                "question_number": "3",
                "question": "Explain the pathophysiology of Parkinson's disease",
                # No options - explanation only
                "explanation": {
                    "option_analysis": "Not applicable - no options provided",
                    "conceptual_foundation": "Parkinson's disease is a neurodegenerative disorder affecting dopaminergic neurons in the substantia nigra pars compacta.",
                    "pathophysiology": "Progressive loss of dopaminergic neurons leads to decreased dopamine in the striatum, disrupting basal ganglia circuits. Alpha-synuclein aggregates form Lewy bodies.",
                    "clinical_manifestation": "Cardinal features: resting tremor, bradykinesia, rigidity, postural instability. Non-motor symptoms include REM sleep behavior disorder, constipation, hyposmia.",
                    "diagnostic_approach": "Clinical diagnosis based on motor features. DaTscan can help in unclear cases. Response to levodopa supports diagnosis.",
                    "management_principles": "Levodopa/carbidopa for motor symptoms. MAO-B inhibitors, dopamine agonists as alternatives. Deep brain stimulation for advanced cases.",
                    "follow_up_guidelines": "Regular assessment every 3-6 months. Monitor for motor fluctuations, dyskinesias. Screen for non-motor symptoms.",
                    "clinical_pearls": [
                        "REM sleep behavior disorder may precede motor symptoms by years",
                        "Tremor is typically 4-6 Hz, pill-rolling, and improves with movement",
                        "Micrographia is an early sign"
                    ],
                    "references": "MDS Clinical Diagnostic Criteria 2015; Postuma et al, Movement Disorders 2015"
                }
            }
        ]
    }


def test_correction_behavior():
    """Test the processor with different MCQ scenarios."""
    print("Testing MCQ Processor Correction Behavior")
    print("=" * 70)
    
    test_data = create_test_mcqs()
    
    print("Test MCQs:")
    print("1. MCQ with WRONG answer and explanation - should be corrected")
    print("2. MCQ with CORRECT answer but typo in question - should NOT change question")
    print("3. MCQ without options (explanation only) - should handle gracefully")
    print("=" * 70)
    
    # Create temporary directories
    with tempfile.TemporaryDirectory() as temp_dir:
        input_dir = Path(temp_dir) / "input"
        output_dir = Path(temp_dir) / "output"
        input_dir.mkdir()
        output_dir.mkdir()
        
        # Save test MCQs
        test_file = input_dir / "test_corrections.json"
        with open(test_file, 'w') as f:
            json.dump(test_data, f, indent=2)
        
        print("\nProcessing MCQs...\n")
        
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
            print(f"Verified (no changes): {result.get('verified', 0)}")
            print(f"Corrected: {result.get('corrected', 0)}")
            
            # Load and display results
            output_file = output_dir / "test_corrections.json"
            if output_file.exists():
                with open(output_file, 'r') as f:
                    processed_data = json.load(f)
                
                print(f"\n{'=' * 70}")
                print("Detailed Results:\n")
                
                for i, (original, processed) in enumerate(zip(test_data['mcqs'], processed_data['mcqs']), 1):
                    print(f"MCQ {i}:")
                    print(f"Original Question: {original['question']}")
                    print(f"Processed Question: {processed['question']}")
                    print(f"Question Changed: {'YES' if original['question'] != processed['question'] else 'NO (preserved typo)'}")
                    
                    if 'options' in original:
                        print(f"\nOriginal Answer: {original['correct_answer']} - {original['correct_answer_text']}")
                        print(f"Processed Answer: {processed['correct_answer']} - {processed['correct_answer_text']}")
                        print(f"Answer Changed: {'YES' if original['correct_answer'] != processed['correct_answer'] else 'NO'}")
                    
                    print(f"\nMetadata:")
                    print(f"- ai_verified: {processed.get('ai_verified', False)}")
                    print(f"- ai_corrected: {processed.get('ai_corrected', False)}")
                    if processed.get('ai_corrected'):
                        print(f"- correction_details: {processed.get('correction_details', 'N/A')}")
                    
                    print("-" * 70)
                
                # Save for review
                review_file = Path("test_correction_results.json")
                with open(review_file, 'w') as f:
                    json.dump(processed_data, f, indent=2)
                print(f"\n✓ Full results saved to: {review_file}")
                
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
    test_correction_behavior()