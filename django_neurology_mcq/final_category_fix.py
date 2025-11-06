#!/usr/bin/env python3
"""Final fix for remaining unclassified MCQs based on their content."""
import os
import sys
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from mcq.models import MCQ

def final_category_fix():
    print("Final Category Fix for Remaining Unclassified MCQs")
    print("=" * 50)
    
    # Specific fixes based on the analysis
    specific_fixes = {
        # Question number -> subspecialty
        '8': 'Headache',  # Cluster headache / trigeminal autonomic cephalalgia
        '112': 'Neurogenetics',  # X-linked adrenomyeloneuropathy
        '114': 'Neurogenetics',  # Urea cycle disorder (metabolic/genetic)
        '191': 'Neurotoxicology',  # Xeroderma pigmentosum (DNA repair disorder)
        '192': 'Neurogenetics',  # Tuberous Sclerosis complex
        '193': 'Neurogenetics',  # Neurofibromatosis (neurocutaneous syndrome)
        '93': 'Neurogenetics',  # Leigh disease (mitochondrial disorder)
        '95': 'Neurogenetics',  # Wilson disease (copper metabolism disorder)
        '101': 'Neurogenetics',  # Oculomotor apraxia (genetic ataxia)
    }
    
    # Also fix based on key concepts
    keyword_fixes = {
        'cluster headache': 'Headache',
        'trigeminal autonomic': 'Headache',
        'x-linked adrenomyeloneuropathy': 'Neurogenetics',
        'urea cycle disorder': 'Neurogenetics',
        'xeroderma pigmentosum': 'Neurogenetics',  # Or Neurotoxicology
        'tuberous sclerosis': 'Neurogenetics',
        'neurofibromatosis': 'Neurogenetics',
        'neurocutaneous': 'Neurogenetics',
        'phakomatoses': 'Neurogenetics',
        'leigh disease': 'Neurogenetics',
        'mitochondrial': 'Neurogenetics',
        'wilson disease': 'Neurogenetics',
        'copper metabolism': 'Neurogenetics',
        'oculomotor apraxia': 'Neurogenetics',
        'genetic ataxia': 'Neurogenetics',
        'inborn errors': 'Neurogenetics',
        'hereditary': 'Neurogenetics',
    }
    
    # Get remaining unclassified MCQs
    unclassified_mcqs = MCQ.objects.filter(
        exam_type='Part II', 
        exam_year=2022,
        subspecialty='Other/Unclassified'
    )
    
    total_count = unclassified_mcqs.count()
    print(f"\nRemaining unclassified MCQs to fix: {total_count}")
    
    fixed_count = 0
    details = []
    
    for mcq in unclassified_mcqs:
        new_subspecialty = None
        
        # First try specific fixes by question number
        if mcq.question_number in specific_fixes:
            new_subspecialty = specific_fixes[mcq.question_number]
        
        # If not found, check key concept and question text
        if not new_subspecialty:
            search_text = ''
            if mcq.key_concept:
                search_text += mcq.key_concept.lower() + ' '
            if mcq.question_text:
                search_text += mcq.question_text.lower()
            
            for keyword, subspecialty in keyword_fixes.items():
                if keyword in search_text:
                    new_subspecialty = subspecialty
                    break
        
        # Apply the fix
        if new_subspecialty:
            old_subspecialty = mcq.subspecialty
            mcq.subspecialty = new_subspecialty
            mcq.save()
            fixed_count += 1
            
            details.append({
                'question_number': mcq.question_number or 'Unknown',
                'old_subspecialty': old_subspecialty,
                'new_subspecialty': new_subspecialty,
                'question_snippet': mcq.question_text[:60] + '...',
                'key_concept': mcq.key_concept[:50] + '...' if mcq.key_concept else None
            })
    
    print(f"\nFixed {fixed_count} MCQs")
    
    # Show what was fixed
    if details:
        print("\nDetailed fixes:")
        for i, detail in enumerate(details, 1):
            print(f"\n{i}. Q{detail['question_number']}")
            print(f"   {detail['old_subspecialty']} → {detail['new_subspecialty']}")
            print(f"   {detail['question_snippet']}")
            if detail['key_concept']:
                print(f"   Key: {detail['key_concept']}")
    
    # Final summary
    print("\n" + "=" * 50)
    print("FINAL SUBSPECIALTY DISTRIBUTION:")
    
    from collections import Counter
    all_mcqs = MCQ.objects.filter(exam_type='Part II', exam_year=2022)
    subspecialty_counts = Counter(all_mcqs.values_list('subspecialty', flat=True))
    
    for subspecialty, count in subspecialty_counts.most_common():
        print(f"  {subspecialty}: {count}")
    
    # Check if any still unclassified
    remaining_unclassified = subspecialty_counts.get('Other/Unclassified', 0)
    print(f"\nREMAINING UNCLASSIFIED: {remaining_unclassified}")
    
    if remaining_unclassified > 0:
        print("\nFinal unclassified MCQs:")
        final_unclassified = MCQ.objects.filter(
            exam_type='Part II', 
            exam_year=2022,
            subspecialty='Other/Unclassified'
        )
        for mcq in final_unclassified:
            print(f"  Q{mcq.question_number}: {mcq.question_text[:50]}...")

if __name__ == "__main__":
    final_category_fix()