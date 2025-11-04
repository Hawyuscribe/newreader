#!/usr/bin/env python
"""Find the specific explanation text"""

import os
import sys
import django
import json

# Setup Django
sys.path.insert(0, '/Users/tariqalmatrudi/NEWreader/django_neurology_mcq')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
django.setup()

from mcq.models import MCQ
from django.db.models import Q

# Search for the specific text in all fields
search_text = "Acute ischemic stroke occurs when a cerebral artery is occluded"

print("Searching for the specific explanation text...")
print(f"Search text: {search_text}")

# Search in explanation field
in_explanation = MCQ.objects.filter(explanation__contains=search_text)
print(f"\nIn explanation field: {in_explanation.count()}")
if in_explanation.exists():
    mcq = in_explanation.first()
    print(f"  MCQ: #{mcq.question_number}")
    print(f"  Explanation length: {len(mcq.explanation)}")
    print(f"  Preview: {mcq.explanation[:200]}...")

# Search in explanation_sections as string
from django.contrib.postgres.search import SearchQuery, SearchVector
try:
    # Try PostgreSQL text search
    in_sections = MCQ.objects.annotate(
        sections_text=SearchVector('explanation_sections')
    ).filter(sections_text=SearchQuery(search_text[:30]))
    print(f"\nIn explanation_sections (text search): {in_sections.count()}")
except:
    # Fallback to basic search
    in_sections = MCQ.objects.filter(explanation_sections__icontains=search_text[:30])
    print(f"\nIn explanation_sections (contains): {in_sections.count()}")

# Direct search in conceptual_foundation
in_conceptual = MCQ.objects.filter(
    Q(explanation_sections__conceptual_foundation__contains=search_text[:30]) |
    Q(explanation_sections__has_key='conceptual_foundation')
)
print(f"\nIn conceptual_foundation field: {in_conceptual.count()}")

# Search for the specific pattern
pattern = "Acute ischemic stroke occurs"
for mcq in MCQ.objects.all()[:100]:  # Check first 100
    if mcq.explanation_sections:
        for key, value in mcq.explanation_sections.items():
            if pattern in str(value):
                print(f"\nFound in MCQ #{mcq.question_number}")
                print(f"  Field: {key}")
                print(f"  Content preview: {value[:100]}...")
                break