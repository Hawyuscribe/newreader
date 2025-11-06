#!/usr/bin/env python3
"""Script to fix unclassified MCQs with proper subspecialty mapping."""
import os
import sys
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from mcq.models import MCQ

def fix_unclassified_mcqs():
    print("Fixing Unclassified MCQs Categories")
    print("=" * 40)
    
    # Enhanced mapping to include missing categories
    category_mapping = {
        # Neuro-infectious variants
        'neuro-infectious': 'Neuro-infectious',
        'neuroinfectious': 'Neuro-infectious', 
        'neuro infectious': 'Neuro-infectious',
        'bacterial': 'Neuro-infectious',
        'parasitic': 'Neuro-infectious',
        'viral': 'Neuro-infectious',
        
        # Other common patterns
        'other-unclassified': 'Other/Unclassified',
        'other unclassified': 'Other/Unclassified',
        
        # Metabolic/Genetic patterns
        'mitochondrial': 'Neurogenetics',
        'metabolic': 'Neurogenetics',
        'genetic': 'Neurogenetics',
        
        # Anatomical localization
        'anatomy': 'Neuroanatomy',
        'localization': 'Neuroanatomy',
        
        # Autonomic
        'autonomic': 'Other/Unclassified',  # Could be a separate category
    }
    
    # Get unclassified MCQs
    unclassified_mcqs = MCQ.objects.filter(
        exam_type='Part II', 
        exam_year=2022,
        subspecialty='Other/Unclassified'
    )
    
    total_count = unclassified_mcqs.count()
    print(f"\nTotal unclassified MCQs to fix: {total_count}")
    
    fixed_count = 0
    details = []
    
    for mcq in unclassified_mcqs:
        primary_cat = mcq.primary_category
        old_subspecialty = mcq.subspecialty
        
        if primary_cat:
            primary_clean = primary_cat.lower().strip()
            
            # Check for direct mapping
            new_subspecialty = None
            for key, value in category_mapping.items():
                if key in primary_clean or primary_clean == key:
                    new_subspecialty = value
                    break
            
            # If still unclassified, check question content for hints
            if new_subspecialty == 'Other/Unclassified' or not new_subspecialty:
                question_lower = mcq.question_text.lower()
                
                # Specific patterns based on content
                if any(word in question_lower for word in ['meningitis', 'encephalitis', 'hiv', 'tb', 'tuberculosis', 'infection', 'bacterial', 'viral', 'parasitic', 'cysticercosis']):
                    new_subspecialty = 'Neuro-infectious'
                elif any(word in question_lower for word in ['melas', 'merrf', 'mitochondrial', 'metabolic', 'genetic', 'inherited']):
                    new_subspecialty = 'Neurogenetics'
                elif any(word in question_lower for word in ['localization', 'anatomy', 'lesion location']):
                    new_subspecialty = 'Neuroanatomy'
                elif any(word in question_lower for word in ['autonomic', 'pupil', 'sweating']):
                    new_subspecialty = 'Other/Unclassified'  # Keep as unclassified or create new category
                elif any(word in question_lower for word in ['seizure', 'epilepsy', 'myoclonus']):
                    new_subspecialty = 'Epilepsy'
                elif any(word in question_lower for word in ['stroke', 'infarct', 'hemorrhage', 'cerebrovascular']):
                    new_subspecialty = 'Vascular Neurology/Stroke'
                elif any(word in question_lower for word in ['neuropathy', 'muscle', 'weakness', 'axonal']):
                    new_subspecialty = 'Neuromuscular'
                elif any(word in question_lower for word in ['dementia', 'cognitive', 'alzheimer']):
                    new_subspecialty = 'Dementia'
                elif any(word in question_lower for word in ['ataxia', 'cerebellum', 'coordination']):
                    new_subspecialty = 'Movement Disorders'
            
            # Apply the fix if we found a better category
            if new_subspecialty and new_subspecialty != old_subspecialty:
                mcq.subspecialty = new_subspecialty
                mcq.save()
                fixed_count += 1
                details.append({
                    'question_number': mcq.question_number or 'Unknown',
                    'primary_category': primary_cat,
                    'old_subspecialty': old_subspecialty,
                    'new_subspecialty': new_subspecialty,
                    'question_snippet': mcq.question_text[:50] + '...'
                })
    
    print(f"\nFixed {fixed_count} MCQs")
    
    # Show what was fixed
    if details:
        print("\nDetailed fixes:")
        for i, detail in enumerate(details[:10], 1):
            print(f"\n{i}. Q{detail['question_number']} ({detail['primary_category']})")
            print(f"   {detail['old_subspecialty']} → {detail['new_subspecialty']}")
            print(f"   {detail['question_snippet']}")
        
        if len(details) > 10:
            print(f"\n... and {len(details) - 10} more fixes")
    
    # Show final distribution
    print("\nFinal subspecialty distribution:")
    from collections import Counter
    all_mcqs = MCQ.objects.filter(exam_type='Part II', exam_year=2022)
    subspecialty_counts = Counter(all_mcqs.values_list('subspecialty', flat=True))
    
    for subspecialty, count in subspecialty_counts.most_common():
        print(f"  {subspecialty}: {count}")
    
    # Show remaining unclassified
    remaining_unclassified = MCQ.objects.filter(
        exam_type='Part II', 
        exam_year=2022,
        subspecialty='Other/Unclassified'
    ).count()
    
    print(f"\nRemaining unclassified: {remaining_unclassified}")

if __name__ == "__main__":
    fix_unclassified_mcqs()