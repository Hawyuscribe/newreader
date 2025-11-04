#!/usr/bin/env python3
"""Script to analyze unclassified MCQs from Part II 2022."""
import os
import sys
import django
from collections import Counter

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from mcq.models import MCQ

def analyze_unclassified():
    print("Analysis of Unclassified Part II 2022 MCQs")
    print("=" * 40)
    
    # Get unclassified Part II 2022 MCQs
    unclassified_mcqs = MCQ.objects.filter(
        exam_type='Part II', 
        exam_year=2022,
        subspecialty='Other/Unclassified'
    )
    
    total_count = unclassified_mcqs.count()
    print(f"\nTotal unclassified MCQs: {total_count}")
    
    # Analyze primary_category values
    primary_categories = Counter(unclassified_mcqs.values_list('primary_category', flat=True))
    print("\nPrimary Categories of Unclassified MCQs:")
    for category, count in primary_categories.most_common():
        print(f"  {category}: {count}")
    
    # Analyze patterns in categories
    categories_with_details = {}
    
    for mcq in unclassified_mcqs:
        category = mcq.primary_category or 'None'
        if category not in categories_with_details:
            categories_with_details[category] = {
                'count': 0,
                'examples': [],
                'question_numbers': []
            }
        
        categories_with_details[category]['count'] += 1
        categories_with_details[category]['question_numbers'].append(mcq.question_number or 'Unknown')
        
        # Add up to 3 examples
        if len(categories_with_details[category]['examples']) < 3:
            categories_with_details[category]['examples'].append({
                'question_number': mcq.question_number or 'Unknown',
                'question_text': mcq.question_text[:100] + '...' if len(mcq.question_text) > 100 else mcq.question_text,
                'key_concept': mcq.key_concept,
                'secondary_category': mcq.secondary_category
            })
    
    # Print detailed analysis
    print("\nDetailed Analysis by Category:")
    for category, details in sorted(categories_with_details.items()):
        print(f"\n'{category}' ({details['count']} MCQs):")
        print(f"  Question Numbers: {', '.join(details['question_numbers'][:10])}" + 
              (" ..." if len(details['question_numbers']) > 10 else ""))
        print("  Examples:")
        for i, example in enumerate(details['examples'], 1):
            print(f"    {i}. Q{example['question_number']}: {example['question_text']}")
            if example['key_concept']:
                print(f"       Key Concept: {example['key_concept']}")
            if example['secondary_category']:
                print(f"       Secondary Category: {example['secondary_category']}")
    
    # Look for patterns in question text that might indicate subspecialty
    print("\nAnalyzing Question Content for Subspecialty Hints:")
    keyword_patterns = {
        'seizure|epileptic|epilepsy': 'Epilepsy',
        'stroke|cerebrovascular|ischemic|hemorrhage': 'Vascular Neurology/Stroke',
        'dementia|alzheimer|cognitive': 'Dementia',
        'parkinson|tremor|movement': 'Movement Disorders',
        'headache|migraine': 'Headache',
        'muscle|weakness|myopathy|neuropathy': 'Neuromuscular',
        'multiple sclerosis|MS|demyelinating': 'Neuroimmunology',
        'infection|meningitis|encephalitis': 'Neuro-infectious',
        'tumor|cancer|oncology': 'Neuro-oncology',
        'sleep|insomnia|REM': 'Sleep Neurology',
        'psychiatry|anxiety|depression': 'Neuropsychiatry',
        'visual|optic|eye': 'Neuroophthalmology',
        'hearing|vertigo|dizziness': 'Neuro-otology',
        'pediatric|child|infant': 'Pediatric Neurology',
        'genetic|inherited|familial': 'Neurogenetics',
        'toxin|poison|drug': 'Neurotoxicology',
        'ICU|intensive care|critical': 'Critical Care Neurology'
    }
    
    suggested_mappings = {}
    for mcq in unclassified_mcqs:
        question_lower = mcq.question_text.lower()
        for pattern, subspecialty in keyword_patterns.items():
            if any(keyword in question_lower for keyword in pattern.split('|')):
                if subspecialty not in suggested_mappings:
                    suggested_mappings[subspecialty] = []
                suggested_mappings[subspecialty].append({
                    'question_number': mcq.question_number,
                    'primary_category': mcq.primary_category,
                    'question_snippet': mcq.question_text[:50] + '...'
                })
                break
    
    if suggested_mappings:
        print("\nSuggested Subspecialty Mappings Based on Question Content:")
        for subspecialty, suggestions in suggested_mappings.items():
            print(f"\n{subspecialty}:")
            for i, suggestion in enumerate(suggestions[:3], 1):
                print(f"  {i}. Q{suggestion['question_number']} ({suggestion['primary_category']})")
                print(f"     {suggestion['question_snippet']}")
    
    # Check for empty or null primary categories
    empty_categories = unclassified_mcqs.filter(primary_category__in=['', None, 'None'])
    if empty_categories.exists():
        print(f"\nMCQs with empty/null primary_category: {empty_categories.count()}")

if __name__ == "__main__":
    analyze_unclassified()