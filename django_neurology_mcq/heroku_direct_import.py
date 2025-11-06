#!/usr/bin/env python
"""
Direct import script to load MCQs from consolidated JSON file.
This script reads from the all_mcqs_consolidated.json file and imports directly.
"""
import os
import sys
import django
import json
from datetime import datetime

# Setup Django
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_neurology_mcq.settings')
django.setup()

from mcq.models import MCQ, Flashcard, IncorrectAnswer, Bookmark
from django.db import transaction

# The consolidated MCQ data
CONSOLIDATED_MCQS = '''
{
  "mcqs": [
    {
      "question": "A 65-year-old man presents with sudden onset of right-sided weakness and difficulty speaking. His symptoms began 2 hours ago. CT scan shows no hemorrhage. What is the most appropriate immediate treatment?",
      "options": {
        "A": "Aspirin 325 mg",
        "B": "Intravenous tissue plasminogen activator (tPA)",
        "C": "Heparin infusion",
        "D": "Warfarin",
        "E": "Clopidogrel 300 mg"
      },
      "correct_answer": "B",
      "explanation": "For acute ischemic stroke within 4.5 hours of symptom onset and no contraindications, IV tPA is the treatment of choice.",
      "specialty": "Neurology",
      "subspecialty": "Vascular Neurology/Stroke"
    }
  ]
}
'''

def main():
    print(f"\n{'='*60}")
    print(f"MCQ Direct Import - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*60}")
    
    # Clear existing data
    with transaction.atomic():
        print("\nClearing existing data...")
        Flashcard.objects.all().delete()
        IncorrectAnswer.objects.all().delete()
        Bookmark.objects.all().delete()
        deleted = MCQ.objects.all().delete()[0]
        print(f"Deleted {deleted} existing MCQs")
    
    # First, let's check what files are available
    print("\nChecking for available JSON files...")
    import glob
    
    # Try different locations
    locations = [
        '/app/*.json',
        '/app/django_neurology_mcq/*.json',
        '*.json',
        '../*.json',
        '/tmp/*.json'
    ]
    
    json_files_found = []
    for loc in locations:
        files = glob.glob(loc)
        if files:
            print(f"\nFound in {loc}:")
            for f in sorted(files)[:5]:
                print(f"  - {f}")
                json_files_found.extend(files)
    
    # Look for specific consolidated file
    consolidated_paths = [
        '/app/all_mcqs_consolidated.json',
        '/app/django_neurology_mcq/all_mcqs_consolidated.json',
        'all_mcqs_consolidated.json',
        '../all_mcqs_consolidated.json',
        '/app/final_rere_fixtures.json',
        'final_rere_fixtures.json'
    ]
    
    data = None
    loaded_from = None
    
    for path in consolidated_paths:
        if os.path.exists(path):
            print(f"\n✅ Found consolidated file: {path}")
            try:
                with open(path, 'r') as f:
                    data = json.load(f)
                loaded_from = path
                break
            except Exception as e:
                print(f"   Error loading {path}: {e}")
    
    if data is None:
        print("\n⚠️  No consolidated file found. Creating a sample MCQ...")
        # Create at least one sample MCQ
        sample_mcq = MCQ(
            question="Sample: A patient presents with acute stroke symptoms. What is the time window for IV tPA?",
            option_a="1.5 hours",
            option_b="3 hours", 
            option_c="4.5 hours",
            option_d="6 hours",
            option_e="12 hours",
            correct_answer="C",
            explanation="IV tPA can be given within 4.5 hours of symptom onset in eligible patients.",
            specialty="Neurology",
            subspecialty="Vascular Neurology/Stroke",
            exam_name="Sample",
            year=2024
        )
        sample_mcq.save()
        print("Created 1 sample MCQ")
    else:
        # Process the loaded data
        print(f"\nProcessing data from {loaded_from}...")
        
        mcq_count = 0
        if isinstance(data, dict) and 'mcqs' in data:
            # Format 1: {"mcqs": [...]}
            mcqs = data['mcqs']
        elif isinstance(data, list):
            # Format 2: Django fixtures format
            mcqs = [item for item in data if item.get('model') == 'mcq.mcq']
        else:
            print(f"Unknown data format: {type(data)}")
            return
        
        print(f"Found {len(mcqs)} MCQs to import")
        
        # Import in batches
        batch_size = 100
        with transaction.atomic():
            for i in range(0, len(mcqs), batch_size):
                batch = mcqs[i:i+batch_size]
                for mcq_data in batch:
                    try:
                        if 'fields' in mcq_data:
                            # Django fixture format
                            fields = mcq_data['fields']
                            mcq = MCQ(
                                id=mcq_data.get('pk'),
                                question=fields['question'],
                                option_a=fields['option_a'],
                                option_b=fields['option_b'],
                                option_c=fields['option_c'],
                                option_d=fields['option_d'],
                                option_e=fields.get('option_e', ''),
                                correct_answer=fields['correct_answer'],
                                explanation=fields.get('explanation', ''),
                                explanation_sections=fields.get('explanation_sections', {}),
                                specialty=fields.get('specialty', 'Neurology'),
                                subspecialty=fields.get('subspecialty', 'General Neurology'),
                                exam_name=fields.get('exam_name', ''),
                                year=fields.get('year')
                            )
                        else:
                            # Direct format
                            mcq = MCQ(
                                question=mcq_data['question'],
                                option_a=mcq_data.get('option_a') or mcq_data.get('options', {}).get('A', ''),
                                option_b=mcq_data.get('option_b') or mcq_data.get('options', {}).get('B', ''),
                                option_c=mcq_data.get('option_c') or mcq_data.get('options', {}).get('C', ''),
                                option_d=mcq_data.get('option_d') or mcq_data.get('options', {}).get('D', ''),
                                option_e=mcq_data.get('option_e') or mcq_data.get('options', {}).get('E', ''),
                                correct_answer=mcq_data['correct_answer'],
                                explanation=mcq_data.get('explanation', ''),
                                explanation_sections=mcq_data.get('explanation_sections', {}),
                                specialty=mcq_data.get('specialty', 'Neurology'),
                                subspecialty=mcq_data.get('subspecialty', 'General Neurology'),
                                exam_name=mcq_data.get('exam_name', ''),
                                year=mcq_data.get('year')
                            )
                        mcq.save()
                        mcq_count += 1
                    except Exception as e:
                        print(f"Error importing MCQ: {e}")
                        continue
                
                print(f"Imported {mcq_count} MCQs...")
    
    # Final verification
    total = MCQ.objects.count()
    print(f"\n{'='*60}")
    print(f"Import Complete!")
    print(f"Total MCQs in database: {total}")
    
    # Show subspecialty breakdown
    from django.db.models import Count
    subspecialties = MCQ.objects.values('subspecialty').annotate(
        count=Count('id')
    ).order_by('-count')[:10]
    
    print(f"\nTop subspecialties:")
    for spec in subspecialties:
        print(f"  {spec['subspecialty']}: {spec['count']}")
    
    print(f"{'='*60}\n")

if __name__ == '__main__':
    main()