from django.core.management.base import BaseCommand
from mcq.models import MCQ, Flashcard, IncorrectAnswer, Bookmark
from django.db import transaction
import json
import os
from pathlib import Path
from datetime import datetime

class Command(BaseCommand):
    help = 'Import MCQs from consolidated JSON file'

    def handle(self, *args, **options):
        self.stdout.write(f"\n{'='*60}")
        self.stdout.write(f"MCQ Import - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        self.stdout.write(f"{'='*60}\n")
        
        # Clear existing data
        with transaction.atomic():
            self.stdout.write("Clearing existing data...")
            Flashcard.objects.all().delete()
            IncorrectAnswer.objects.all().delete()
            Bookmark.objects.all().delete()
            deleted = MCQ.objects.all().delete()[0]
            self.stdout.write(f"Deleted {deleted} existing MCQs\n")
        
        # Find the consolidated JSON file
        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        
        # Try different paths
        json_paths = [
            base_dir / 'all_mcqs_consolidated.json',
            base_dir.parent / 'all_mcqs_consolidated.json',
            base_dir / 'final_rere_fixtures.json',
            Path('/app/all_mcqs_consolidated.json'),
            Path('/app/django_neurology_mcq/all_mcqs_consolidated.json')
        ]
        
        data = None
        source_file = None
        
        for path in json_paths:
            if path.exists():
                self.stdout.write(f"Found: {path}")
                try:
                    with open(path, 'r') as f:
                        data = json.load(f)
                    source_file = path
                    break
                except Exception as e:
                    self.stdout.write(f"Error reading {path}: {e}")
        
        if data is None:
            # Import from the MCQ data directly
            self.stdout.write("Loading MCQ data from embedded source...")
            data = self.get_mcq_data()
        
        # Process the data
        if isinstance(data, dict) and 'mcqs' in data:
            mcqs = data['mcqs']
        elif isinstance(data, list):
            # Handle fixture format
            mcqs = []
            for item in data:
                if item.get('model') == 'mcq.mcq':
                    fields = item['fields']
                    # Remove fields that don't exist in model
                    fields.pop('keywords', None)
                    fields.pop('tags', None)
                    fields.pop('notes', None)
                    fields.pop('is_active', None)
                    fields.pop('review_status', None)
                    mcqs.append(fields)
        else:
            self.stdout.write(self.style.ERROR("Unknown data format"))
            return
        
        self.stdout.write(f"\nImporting {len(mcqs)} MCQs...")
        
        # Import MCQs in batches
        imported = 0
        batch_size = 100
        
        with transaction.atomic():
            for i in range(0, len(mcqs), batch_size):
                batch = mcqs[i:i+batch_size]
                
                for mcq_data in batch:
                    try:
                        mcq = MCQ(
                            question=mcq_data['question'],
                            option_a=mcq_data.get('option_a', ''),
                            option_b=mcq_data.get('option_b', ''),
                            option_c=mcq_data.get('option_c', ''),
                            option_d=mcq_data.get('option_d', ''),
                            option_e=mcq_data.get('option_e', ''),
                            correct_answer=mcq_data['correct_answer'],
                            explanation=mcq_data.get('explanation', ''),
                            explanation_sections=mcq_data.get('explanation_sections', {}),
                            specialty=mcq_data.get('specialty', 'Neurology'),
                            subspecialty=mcq_data.get('subspecialty', 'General Neurology'),
                            exam_name=mcq_data.get('exam_name', ''),
                            year=mcq_data.get('year'),
                            topic=mcq_data.get('topic', ''),
                            difficulty=mcq_data.get('difficulty', 3),
                            cognitive_level=mcq_data.get('cognitive_level', 'Recall'),
                            references=mcq_data.get('references', ''),
                            high_yield=mcq_data.get('high_yield', False),
                            image_url=mcq_data.get('image_url', '')
                        )
                        mcq.save()
                        imported += 1
                    except Exception as e:
                        self.stdout.write(f"Error importing MCQ: {e}")
                        continue
                
                if imported % 100 == 0:
                    self.stdout.write(f"  Imported {imported} MCQs...")
        
        # Final verification
        total = MCQ.objects.count()
        self.stdout.write(f"\n{'='*60}")
        self.stdout.write(self.style.SUCCESS(f"Import Complete!"))
        self.stdout.write(f"Total MCQs imported: {imported}")
        self.stdout.write(f"Total MCQs in database: {total}")
        
        # Show subspecialty breakdown
        from django.db.models import Count
        subspecialties = MCQ.objects.values('subspecialty').annotate(
            count=Count('id')
        ).order_by('-count')[:10]
        
        self.stdout.write(f"\nTop subspecialties:")
        for spec in subspecialties:
            self.stdout.write(f"  {spec['subspecialty']}: {spec['count']}")
        
        if total == 2853:
            self.stdout.write(self.style.SUCCESS(f"\n✅ Success! MCQ count matches expected."))
        else:
            self.stdout.write(self.style.WARNING(f"\n⚠️  Expected 2853 MCQs, got {total}"))
        
        self.stdout.write(f"{'='*60}\n")
    
    def get_mcq_data(self):
        # This will contain a subset of MCQs to ensure the import works
        return {
            "mcqs": [
                {
                    "question": "A 45-year-old woman presents with sudden onset severe headache, photophobia, and neck stiffness. CT scan is negative. What is the most appropriate next step?",
                    "option_a": "MRI brain",
                    "option_b": "Lumbar puncture",
                    "option_c": "CT angiography",
                    "option_d": "Start empiric antibiotics",
                    "option_e": "Discharge home with analgesics",
                    "correct_answer": "B",
                    "explanation": "With clinical suspicion of subarachnoid hemorrhage and negative CT, lumbar puncture is indicated to look for xanthochromia.",
                    "specialty": "Neurology",
                    "subspecialty": "Vascular Neurology/Stroke",
                    "exam_name": "Sample",
                    "year": 2024
                },
                {
                    "question": "Which medication is most effective for preventing migraine headaches?",
                    "option_a": "Sumatriptan",
                    "option_b": "Propranolol",
                    "option_c": "Acetaminophen",
                    "option_d": "Prednisone",
                    "option_e": "Morphine",
                    "correct_answer": "B",
                    "explanation": "Propranolol is a beta-blocker that is effective for migraine prophylaxis. Sumatriptan is for acute treatment.",
                    "specialty": "Neurology",
                    "subspecialty": "Headache Medicine",
                    "exam_name": "Sample",
                    "year": 2024
                }
            ]
        }