#!/usr/bin/env python
"""Check MCQ count on Heroku"""
from mcq.models import MCQ
from django.db.models import Count

total = MCQ.objects.count()
print(f"Total MCQs in database: {total}")

# Count by subspecialty
subspecialty_counts = MCQ.objects.values('subspecialty').annotate(count=Count('id')).order_by('-count')
print("\nTop 10 subspecialties:")
for item in subspecialty_counts[:10]:
    print(f"  {item['subspecialty']}: {item['count']}")

# Check for explanations with new format
mcqs_with_explanation_sections = MCQ.objects.exclude(explanation_sections__isnull=True).exclude(explanation_sections={}).count()
print(f"\nMCQs with explanation_sections: {mcqs_with_explanation_sections}")

# Sample MCQ to check format
sample_mcq = MCQ.objects.exclude(explanation_sections__isnull=True).exclude(explanation_sections={}).first()
if sample_mcq:
    print(f"\nSample MCQ (ID: {sample_mcq.id}):")
    print(f"  Question: {sample_mcq.question_text[:100]}...")
    print(f"  Subspecialty: {sample_mcq.subspecialty}")
    print(f"  Explanation sections: {list(sample_mcq.explanation_sections.keys())}")