#!/usr/bin/env python
"""Find MCQs with text explanations"""

import os
import sys
import django
import json

# Setup Django
sys.path.insert(0, '/Users/tariqalmatrudi/NEWreader/django_neurology_mcq')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
django.setup()

from mcq.models import MCQ

# Find MCQs with explanations
print("Analyzing MCQ explanations...")

# Check different patterns
patterns = [
    "Conceptual Foundation",
    "Pathophysiology",
    "Clinical Correlation",
    "Acute ischemic stroke"
]

for pattern in patterns:
    print(f"\nSearching for '{pattern}':")
    
    # In explanation field
    in_explanation = MCQ.objects.filter(explanation__contains=pattern).count()
    print(f"  In explanation field: {in_explanation}")
    
    # In explanation_sections as JSON text
    in_sections_json = MCQ.objects.filter(explanation_sections__icontains=pattern).count()
    print(f"  In explanation_sections (JSON): {in_sections_json}")
    
    # Get samples
    if in_explanation > 0:
        sample = MCQ.objects.filter(explanation__contains=pattern).first()
        print(f"  Sample MCQ: #{sample.question_number}")
        print(f"  explanation preview: {sample.explanation[:100]}...")
        print(f"  explanation_sections: {sample.explanation_sections}")

# Also check for large explanations
print("\n\nLarge explanations:")
large_explanations = MCQ.objects.filter(explanation__regex=r'.{1000,}').count()
print(f"MCQs with explanations > 1000 chars: {large_explanations}")

# Get one sample of large explanation
large_sample = MCQ.objects.filter(explanation__regex=r'.{1000,}').first()
if large_sample:
    print(f"\nSample large explanation MCQ: #{large_sample.question_number}")
    print(f"Length: {len(large_sample.explanation)} chars")
    print(f"First 200 chars: {large_sample.explanation[:200]}...")
    print(f"Contains 'Conceptual Foundation': {'Conceptual Foundation' in large_sample.explanation}")
    
    # Check if it's JSON
    try:
        parsed = json.loads(large_sample.explanation)
        print(f"Is JSON: Yes, type: {type(parsed)}")
        if isinstance(parsed, dict):
            print(f"Keys: {list(parsed.keys())[:5]}")
    except:
        print("Is JSON: No")
    
    print(f"explanation_sections: {large_sample.explanation_sections}")