#!/usr/bin/env python3
"""Script to fix the imported MCQs from Part II 2022."""
import os
import sys
import django
import re

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from mcq.models import MCQ

# Enhanced subspecialty mapping
SUBSPECIALTY_MAPPING = {
    'anatomy': 'Neuroanatomy',
    'critical_care_neurology': 'Critical Care Neurology',
    'critical care neurology': 'Critical Care Neurology',
    'dementia': 'Dementia',
    'demyelinating': 'Neuroimmunology',
    'demyelinating/multiple sclerosis': 'Neuroimmunology',
    'epilepsy': 'Epilepsy',
    'headache': 'Headache',
    'movement_disorders': 'Movement Disorders',
    'movement disorders': 'Movement Disorders',
    'neuro-otology': 'Neuro-otology',
    'neuro otology': 'Neuro-otology',
    'neuro-ophthalmology': 'Neuroophthalmology',
    'neuroophthalmology': 'Neuroophthalmology',
    'neurogenetics': 'Neurogenetics',
    'neuroimmunology': 'Neuroimmunology',
    'neuroimmunology/autoimmune neurology': 'Neuroimmunology',
    'neuroinfectious': 'Neuro-infectious',
    'neuroinfectious diseases': 'Neuro-infectious',
    'neuromuscular': 'Neuromuscular',
    'neurooncology': 'Neuro-oncology',
    'neuro-oncology': 'Neuro-oncology',
    'neuropsychiatry': 'Neuropsychiatry',
    'neurotoxicology': 'Neurotoxicology',
    'other': 'Other/Unclassified',
    'other-unclassified': 'Other/Unclassified',
    'pediatric_neurology': 'Pediatric Neurology',
    'pediatric neurology': 'Pediatric Neurology',
    'sleep_neurology': 'Sleep Neurology',
    'sleep neurology': 'Sleep Neurology',
    'vascular_neurology': 'Vascular Neurology/Stroke',
    'vascular neurology': 'Vascular Neurology/Stroke',
    'vascular neurology/stroke': 'Vascular Neurology/Stroke',
    'vascular neurology / stroke': 'Vascular Neurology/Stroke',
    'cerebrovascular/stroke': 'Vascular Neurology/Stroke',
    'stroke': 'Vascular Neurology/Stroke',
}

def extract_correct_answer(option_analysis):
    """Extract correct answer from option_analysis text."""
    if not option_analysis:
        return None
    
    patterns = [
        r'Option\s+([A-Z]):\s*.*?[–—-]\s*(?:Correct|CORRECT)',
        r'Option\s+([A-Z])\s*.*?\((?:Correct|CORRECT)\)',
        r'Option\s+([A-Z]):\s*(?:Correct|CORRECT)',
        r'Option\s+([A-Z]).*?(?:is|appears)\s+(?:correct|best)',
        r'Option\s+([A-Z])[:\s]+[^.]*?(?:—|–)\s*(?:Correct|CORRECT)',
        r'([A-Z])\.\s*.*?[–—-]\s*(?:Correct|CORRECT)',
        r'([A-Z])\)\s*.*?[–—-]\s*(?:Correct|CORRECT)',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, option_analysis, re.IGNORECASE | re.MULTILINE | re.DOTALL)
        if match:
            return match.group(1).upper()
    
    return None

def map_subspecialty(primary_category):
    """Map primary_category to proper subspecialty name."""
    if not primary_category:
        return 'Other/Unclassified'
    
    # Clean the input
    category_clean = primary_category.lower().replace('_', ' ').strip()
    
    # Direct mapping
    if category_clean in SUBSPECIALTY_MAPPING:
        return SUBSPECIALTY_MAPPING[category_clean]
    
    # Try with underscores
    category_underscore = category_clean.replace(' ', '_')
    if category_underscore in SUBSPECIALTY_MAPPING:
        return SUBSPECIALTY_MAPPING[category_underscore]
    
    # Try replacing slashes with spaces
    if '/' in category_clean:
        category_slash = category_clean.replace('/', ' ')
        if category_slash in SUBSPECIALTY_MAPPING:
            return SUBSPECIALTY_MAPPING[category_slash]
    
    return 'Other/Unclassified'

def fix_mcqs():
    print("Fixing Part II 2022 MCQs")
    print("=" * 40)
    
    # Get Part II 2022 MCQs
    part_ii_2022_mcqs = MCQ.objects.filter(exam_type='Part II', exam_year=2022)
    total_count = part_ii_2022_mcqs.count()
    
    print(f"\nTotal Part II 2022 MCQs to fix: {total_count}")
    
    fixed_subspecialties = 0
    fixed_answers = 0
    
    for mcq in part_ii_2022_mcqs:
        updated = False
        
        # Fix subspecialty
        if mcq.subspecialty == 'Other/Unclassified' and mcq.primary_category:
            new_subspecialty = map_subspecialty(mcq.primary_category)
            if new_subspecialty != 'Other/Unclassified':
                mcq.subspecialty = new_subspecialty
                fixed_subspecialties += 1
                updated = True
        
        # Fix correct answer from option_analysis
        if mcq.correct_answer and (
            len(mcq.correct_answer) > 1 or 
            mcq.correct_answer.islower() or 
            mcq.correct_answer.isdigit() or
            mcq.correct_answer == 'None'
        ):
            if mcq.explanation_sections and 'option_analysis' in mcq.explanation_sections:
                option_analysis = mcq.explanation_sections['option_analysis']
                if isinstance(option_analysis, str):
                    new_answer = extract_correct_answer(option_analysis)
                    if new_answer:
                        mcq.correct_answer = new_answer
                        fixed_answers += 1
                        updated = True
        
        # Fix uppercase for lowercase answers
        if mcq.correct_answer and mcq.correct_answer.islower() and len(mcq.correct_answer) == 1:
            mcq.correct_answer = mcq.correct_answer.upper()
            fixed_answers += 1
            updated = True
        
        if updated:
            mcq.save()
    
    print(f"\nFixed {fixed_subspecialties} subspecialties")
    print(f"Fixed {fixed_answers} correct answers")
    
    # Show final stats
    part_ii_2022_mcqs = MCQ.objects.filter(exam_type='Part II', exam_year=2022)
    
    from collections import Counter
    subspecialty_counts = Counter(part_ii_2022_mcqs.values_list('subspecialty', flat=True))
    print("\nFinal MCQs by Subspecialty:")
    for subspecialty, count in subspecialty_counts.most_common():
        print(f"  {subspecialty}: {count}")
    
    correct_answer_counts = Counter(part_ii_2022_mcqs.values_list('correct_answer', flat=True))
    print("\nFinal Correct Answer Distribution:")
    for answer, count in sorted(correct_answer_counts.items()):
        if answer and (len(answer) == 1 and answer.isupper()):
            print(f"  {answer}: {count}")
        else:
            print(f"  {answer}: {count} ⚠️  (needs fixing)")

if __name__ == "__main__":
    fix_mcqs()