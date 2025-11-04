#!/usr/bin/env python
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
from django.contrib.auth.models import User
from django.db import transaction

def import_mcqs():
    print(f"\n{'='*50}")
    print(f"Direct MCQ Import - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*50}")
    
    # First, clear all existing data
    with transaction.atomic():
        print("\n1. Clearing existing data...")
        fc = Flashcard.objects.all().delete()[0]
        ia = IncorrectAnswer.objects.all().delete()[0]
        bm = Bookmark.objects.all().delete()[0]
        mcq = MCQ.objects.all().delete()[0]
        print(f"   Deleted: {fc} flashcards, {ia} incorrect answers, {bm} bookmarks, {mcq} MCQs")
    
    # Load the fixture file
    fixture_path = '/app/final_rere_fixtures.json'
    if not os.path.exists(fixture_path):
        # Try parent directory
        fixture_path = '../final_rere_fixtures.json'
    
    if not os.path.exists(fixture_path):
        print(f"\n❌ ERROR: Could not find final_rere_fixtures.json")
        print("Looking for fixture in current directory...")
        # List files in current directory
        import glob
        json_files = glob.glob('*.json')
        print(f"Found {len(json_files)} JSON files:")
        for f in sorted(json_files)[:10]:
            print(f"  - {f}")
        return
    
    print(f"\n2. Loading fixture from: {fixture_path}")
    
    try:
        with open(fixture_path, 'r') as f:
            data = json.load(f)
        
        print(f"   Loaded {len(data)} objects from fixture")
        
        # Import MCQs
        mcq_count = 0
        with transaction.atomic():
            for item in data:
                if item['model'] == 'mcq.mcq':
                    mcq_count += 1
                    fields = item['fields']
                    
                    # Create the MCQ
                    mcq = MCQ(
                        id=item['pk'],
                        question=fields['question'],
                        option_a=fields['option_a'],
                        option_b=fields['option_b'],
                        option_c=fields['option_c'],
                        option_d=fields['option_d'],
                        option_e=fields.get('option_e', ''),
                        correct_answer=fields['correct_answer'],
                        explanation=fields.get('explanation', ''),
                        explanation_sections=fields.get('explanation_sections', {}),
                        exam_name=fields.get('exam_name', ''),
                        year=fields.get('year'),
                        specialty=fields.get('specialty', 'Neurology'),
                        subspecialty=fields.get('subspecialty', 'General Neurology'),
                        topic=fields.get('topic', ''),
                        difficulty=fields.get('difficulty', 3),
                        cognitive_level=fields.get('cognitive_level', 'Recall'),
                        references=fields.get('references', ''),
                        high_yield=fields.get('high_yield', False),
                        image_url=fields.get('image_url', ''),
                        created_at=fields.get('created_at', '2024-01-01T00:00:00Z'),
                        updated_at=fields.get('updated_at', '2024-01-01T00:00:00Z')
                    )
                    mcq.save()
                    
                    if mcq_count % 100 == 0:
                        print(f"   Imported {mcq_count} MCQs...")
        
        print(f"\n3. Import complete!")
        print(f"   Total MCQs imported: {mcq_count}")
        
        # Verify the import
        total = MCQ.objects.count()
        print(f"\n4. Verification:")
        print(f"   Total MCQs in database: {total}")
        
        # Show subspecialty breakdown
        from django.db.models import Count
        subspecialties = MCQ.objects.values('subspecialty').annotate(
            count=Count('id')
        ).order_by('-count')[:10]
        
        print(f"\n5. Top subspecialties:")
        for spec in subspecialties:
            print(f"   {spec['subspecialty']}: {spec['count']}")
        
        if total == 2853:
            print(f"\n✅ SUCCESS! Expected MCQ count matches.")
        else:
            print(f"\n⚠️  WARNING: Expected 2853 MCQs, but got {total}")
            
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    import_mcqs()