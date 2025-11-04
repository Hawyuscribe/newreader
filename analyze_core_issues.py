#!/usr/bin/env python3
"""
Analyze the core issues with MCQ-to-case conversion
"""

import os
import sys
import django

# Setup Django
sys.path.append('/Users/tariqalmatrudi/NEWreader/django_neurology_mcq')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
django.setup()

from mcq.models import MCQ
from mcq.mcq_case_converter import detect_question_type

def analyze_question_type_accuracy():
    """Analyze question type detection accuracy"""
    
    # Test sample questions
    test_questions = [
        "Which of the following is considered a red flag in multiple sclerosis?",
        "A patient with relapsing-remitting multiple sclerosis (RRMS) received 5 days of intravenous methylprednisolone (IVMP) without improvement. What should be done next?",
        "A patient with multiple sclerosis (MS) presented with shortness of breath (SOB) and an allergic reaction during the third infusion of natalizumab. What is the most appropriate action to take next?",
        "A newly diagnosed Huntington's disease patient states that he does not want to inform his employer. What should you do?",
        "An elderly patient is intubated with intact level of consciousness but is only able to move his extraocular muscles. What is the next step in workup?",
        "A patient presents with a small area of headache associated with hair loss. What is the treatment?",
        "A 45-year-old female patient diagnosed with epilepsy is currently on Lacosamide 200 mg BID and Levetiracetam 1500 mg BID. She presented to the epilepsy outpatient clinic for evaluation. She reported a history of generalized seizure preceded by feelings of fear and palpitations. While in the clinic, she had a seizure episode that started with chewing spells and right hand automatism followed by bilateral generalized tonic-clonic seizure. She doesn't recall the event. Which of the following is the next step in management?"
    ]
    
    print("🔍 ANALYZING QUESTION TYPE DETECTION")
    print("=" * 80)
    
    for i, question in enumerate(test_questions, 1):
        print(f"\n{i}. Question: {question}")
        
        # Create mock MCQ object
        class MockMCQ:
            def __init__(self, question_text):
                self.question_text = question_text
        
        mcq = MockMCQ(question)
        detected_type = detect_question_type(mcq)
        
        # Manual analysis
        q_lower = question.lower()
        
        # Expected type based on question structure
        if 'what should be done next' in q_lower or 'next step' in q_lower:
            expected = 'management' if 'treatment' in q_lower or 'management' in q_lower else 'investigation'
        elif 'what is the treatment' in q_lower:
            expected = 'management'
        elif 'what is' in q_lower or 'which of the following is' in q_lower:
            expected = 'diagnosis'
        elif 'what should you do' in q_lower:
            expected = 'management'
        else:
            expected = 'unclear'
        
        print(f"   Detected: {detected_type}")
        print(f"   Expected: {expected}")
        print(f"   Match: {'✅' if detected_type == expected else '❌'}")

if __name__ == "__main__":
    analyze_question_type_accuracy()