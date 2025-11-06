#!/usr/bin/env python3
"""
Script to prepare MCQs with "# Classification" placeholders for explanation generation.
This script finds MCQs that need explanations, extracts useful content from the classification,
and sets them up with a better placeholder that guides explanation generation.
"""

import os
import sys
import django
import json
from django.db import transaction
from datetime import datetime

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
django.setup()

from mcq.models import MCQ

def find_mcqs_needing_explanations():
    """
    Find MCQs that need explanations based on the has_explanation property.
    """
    # Get all MCQs
    all_mcqs = MCQ.objects.all()
    
    # Find MCQs needing explanations
    mcqs_needing_explanations = []
    for mcq in all_mcqs:
        if not mcq.has_explanation:
            mcqs_needing_explanations.append(mcq)
    
    return mcqs_needing_explanations

def extract_classification_content(explanation_text):
    """
    Extract useful content from the classification section.
    """
    # Remove the header
    if "# Classification" in explanation_text:
        content = explanation_text.replace("# Classification", "").strip()
    else:
        content = explanation_text.strip()
    
    # Remove duplicate fragments
    content = content.replace("Duplicate of", "").strip()
    content = content.replace("Duplicate/Partial of", "").strip()
    
    # If the content is very short or empty, return None
    if len(content) < 10:
        return None
    
    return content

@transaction.atomic
def prepare_for_explanation_generation(mcqs):
    """
    Prepare MCQs for explanation generation by enhancing their placeholders.
    """
    better_template = """# Explanation Needed

This MCQ requires a detailed explanation. You can generate one using the "Generate Explanation" button below.

## Topic and Classification
{classification_content}

## What Should Be Included
The explanation should cover:
- Key pathophysiological concepts relevant to this question
- Diagnostic criteria or management principles involved
- Why the correct answer is right with evidence-based support
- Why each incorrect option is wrong
- Clinical pearls and high-yield points
"""
    
    prepared_mcqs = []
    
    for mcq in mcqs:
        try:
            # Extract useful content from the classification
            classification_content = extract_classification_content(mcq.explanation)
            
            # Create an enhanced placeholder
            if classification_content:
                enhanced_placeholder = better_template.format(
                    classification_content=classification_content
                )
            else:
                # If no useful content is extracted, use a simpler template
                enhanced_placeholder = better_template.format(
                    classification_content="No classification information available."
                )
            
            # Update the MCQ with the enhanced placeholder
            mcq.explanation = enhanced_placeholder
            mcq.save()
            
            prepared_mcqs.append({
                "id": mcq.id,
                "question_number": mcq.question_number,
                "subspecialty": mcq.subspecialty
            })
            
        except Exception as e:
            print(f"Error preparing MCQ {mcq.id}: {str(e)}")
    
    return prepared_mcqs

def main():
    print("Finding MCQs that need explanations...")
    mcqs_needing_explanations = find_mcqs_needing_explanations()
    
    if not mcqs_needing_explanations:
        print("No MCQs need explanations. Great work!")
        return
    
    print(f"Found {len(mcqs_needing_explanations)} MCQs that need explanations.")
    
    # Group by subspecialty for reporting
    subspecialty_counts = {}
    for mcq in mcqs_needing_explanations:
        if mcq.subspecialty not in subspecialty_counts:
            subspecialty_counts[mcq.subspecialty] = 0
        subspecialty_counts[mcq.subspecialty] += 1
    
    print("\nBreakdown by subspecialty:")
    for subspecialty, count in sorted(subspecialty_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"- {subspecialty}: {count} MCQs")
    
    # Prepare MCQs for explanation generation
    print("\nPreparing MCQs for explanation generation...")
    prepared_mcqs = prepare_for_explanation_generation(mcqs_needing_explanations)
    
    print(f"\nSuccessfully prepared {len(prepared_mcqs)} MCQs for explanation generation.")
    
    # Save list of prepared MCQs to file
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    output = {
        "timestamp": datetime.now().isoformat(),
        "total_prepared": len(prepared_mcqs),
        "prepared_mcqs": prepared_mcqs
    }
    
    filename = os.path.join(output_dir, f"prepared_for_explanation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
    with open(filename, 'w') as f:
        json.dump(output, f, indent=2)
    
    print(f"List of prepared MCQs saved to {filename}")
    print("\nThese MCQs are now ready for explanation generation.")
    print("Users will see a 'Generate Explanation' button that will create detailed, professionally formatted explanations.")

if __name__ == "__main__":
    main()