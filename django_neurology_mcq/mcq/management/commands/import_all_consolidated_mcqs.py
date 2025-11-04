from django.core.management.base import BaseCommand
from mcq.models import MCQ, Flashcard, IncorrectAnswer, Bookmark
from django.db import transaction
import json
import os
from pathlib import Path
from datetime import datetime

class Command(BaseCommand):
    help = 'Import all MCQs from consolidated JSON file'

    def handle(self, *args, **options):
        self.stdout.write(f"\n{'='*60}")
        self.stdout.write(f"🚀 COMPLETE MCQ IMPORT - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        self.stdout.write(f"{'='*60}\n")
        
        # Clear existing data
        with transaction.atomic():
            self.stdout.write("🧹 Clearing existing data...")
            Flashcard.objects.all().delete()
            IncorrectAnswer.objects.all().delete()
            Bookmark.objects.all().delete()
            deleted = MCQ.objects.all().delete()[0]
            self.stdout.write(f"   Deleted {deleted} existing MCQs\n")
        
        # Try to find the consolidated file
        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        
        possible_paths = [
            base_dir / 'consolidated_all_mcqs.json',
            base_dir.parent / 'consolidated_all_mcqs.json',
            Path('/app/consolidated_all_mcqs.json'),
            Path('/app/django_neurology_mcq/consolidated_all_mcqs.json')
        ]
        
        consolidated_data = None
        source_file = None
        
        for path in possible_paths:
            if path.exists():
                self.stdout.write(f"📁 Found consolidated file: {path}")
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        consolidated_data = json.load(f)
                    source_file = path
                    break
                except Exception as e:
                    self.stdout.write(f"   ❌ Error loading {path}: {e}")
        
        if consolidated_data is None:
            self.stdout.write(self.style.ERROR("❌ No consolidated MCQ file found. Creating from embedded data..."))
            # Fall back to embedded sample data
            consolidated_data = self.get_embedded_mcq_data()
        
        # Extract MCQs and metadata
        mcqs_to_import = consolidated_data.get('mcqs', [])
        metadata = consolidated_data.get('metadata', {})
        file_stats = consolidated_data.get('file_stats', {})
        
        self.stdout.write(f"📊 Data Overview:")
        self.stdout.write(f"   Total MCQs to import: {len(mcqs_to_import)}")
        self.stdout.write(f"   Source files: {len(file_stats)}")
        self.stdout.write(f"   Generated: {metadata.get('generated_date', 'Unknown')}")
        
        if file_stats:
            self.stdout.write(f"\n📋 Source file breakdown:")
            for filename, stats in list(file_stats.items())[:10]:  # Show first 10
                self.stdout.write(f"   {stats['specialty']:<30} {stats['mcq_count']:>4} MCQs")
            if len(file_stats) > 10:
                self.stdout.write(f"   ... and {len(file_stats) - 10} more files")
        
        # Import MCQs in batches
        self.stdout.write(f"\n🔄 Starting import process...")
        total_imported = 0
        batch_size = 100
        total_batches = (len(mcqs_to_import) + batch_size - 1) // batch_size
        
        for batch_num in range(0, len(mcqs_to_import), batch_size):
            batch = mcqs_to_import[batch_num:batch_num + batch_size]
            current_batch = (batch_num // batch_size) + 1
            
            self.stdout.write(f"   📦 Processing batch {current_batch}/{total_batches} ({len(batch)} MCQs)...")
            
            with transaction.atomic():
                for mcq_data in batch:
                    try:
                        # Get explanation sections
                        explanation_data = mcq_data.get('explanation', {})
                        explanation_sections = {}
                        
                        if isinstance(explanation_data, dict):
                            # Map the explanation sections
                            for key in ['option_analysis', 'clinical_manifestation', 'diagnostic_approach', 
                                       'management_principles', 'follow_up_guidelines', 'conceptual_foundation',
                                       'pathophysiology', 'clinical_pearls', 'references']:
                                if key in explanation_data:
                                    explanation_sections[key] = explanation_data[key]
                        
                        # Create unified explanation
                        unified_explanation = mcq_data.get('unified_explanation', '')
                        if not unified_explanation and explanation_sections:
                            # Build from sections if no unified explanation
                            sections_text = []
                            for k, v in explanation_sections.items():
                                if v and 'included within the unified explanation' not in v:
                                    sections_text.append(f"{k.replace('_', ' ').title()}: {v}")
                            unified_explanation = '\n\n'.join(sections_text)
                        
                        # Create MCQ with correct field mapping
                        mcq = MCQ(
                            question_number=mcq_data.get('question_number', ''),
                            question_text=mcq_data.get('question', ''),
                            options=mcq_data.get('options', []),
                            correct_answer=mcq_data.get('correct_answer', ''),
                            correct_answer_text=mcq_data.get('correct_answer_text', ''),
                            subspecialty=mcq_data.get('subspecialty', 'General Neurology'),
                            source_file=mcq_data.get('source_file', ''),
                            exam_type=mcq_data.get('exam_type', ''),
                            exam_year=mcq_data.get('exam_year', ''),
                            ai_generated=mcq_data.get('ai_generated', False),
                            unified_explanation=unified_explanation,
                            explanation=unified_explanation,
                            explanation_sections=explanation_sections,
                            image_url=mcq_data.get('image_url', '')
                        )
                        mcq.save()
                        total_imported += 1
                        
                    except Exception as e:
                        self.stdout.write(f"      ❌ Error importing MCQ: {str(e)[:100]}")
                        continue
            
            # Progress update
            progress = (total_imported / len(mcqs_to_import)) * 100
            self.stdout.write(f"      ✅ Imported {total_imported} MCQs ({progress:.1f}%)")
        
        # Final verification and report
        final_count = MCQ.objects.count()
        self.stdout.write(f"\n{'='*60}")
        self.stdout.write(self.style.SUCCESS(f"🎉 IMPORT COMPLETE!"))
        self.stdout.write(f"{'='*60}")
        self.stdout.write(f"✅ Total MCQs imported: {total_imported}")
        self.stdout.write(f"✅ Total MCQs in database: {final_count}")
        
        # Show subspecialty breakdown
        from django.db.models import Count
        subspecialties = MCQ.objects.values('subspecialty').annotate(
            count=Count('id')
        ).order_by('-count')
        
        self.stdout.write(f"\n📊 Subspecialty breakdown:")
        
        # Expected counts for verification
        expected_counts = {
            'Neuromuscular': 483,
            'Vascular Neurology/Stroke': 439,
            'Neuroimmunology': 299,
            'Epilepsy': 284,
            'Movement Disorders': 269,
            'Neuro-infectious': 200,
            'Headache': 166,
            'Dementia': 151,
            'Neuro-Oncology': 102,
            'Neuroophthalmology': 101,
            'Critical Care Neurology': 93,
            'Pediatric Neurology': 82,
            'Neurotoxicology': 40,
            'Sleep Neurology': 33,
            'Neuropsychiatry': 33,
            'Neuroanatomy': 27,
            'Other/Unclassified': 26,
            'Neuro-Otology': 23,
            'Multiple Sclerosis': 2
        }
        
        total_expected = sum(expected_counts.values())
        
        for spec in subspecialties:
            name = spec['subspecialty']
            count = spec['count']
            expected = expected_counts.get(name, 0)
            
            if count == expected and expected > 0:
                status = "✅"
            elif expected > 0:
                status = f"❌ (exp: {expected})"
            else:
                status = "ℹ️  (new)"
            
            self.stdout.write(f"   {name:<35} {count:>4} MCQs {status}")
        
        self.stdout.write(f"\n📈 Summary:")
        self.stdout.write(f"   Expected total: {total_expected}")
        self.stdout.write(f"   Actual total:   {final_count}")
        
        if final_count == total_expected:
            self.stdout.write(self.style.SUCCESS(f"   🎯 Perfect match! All MCQs imported correctly."))
        else:
            diff = final_count - total_expected
            self.stdout.write(self.style.WARNING(f"   ⚠️  Difference: {diff:+d} MCQs"))
        
        self.stdout.write(f"\n🌐 Your Heroku dashboard should now show the correct MCQ counts!")
        self.stdout.write(f"{'='*60}\n")
    
    def get_embedded_mcq_data(self):
        """Fallback embedded data if consolidated file not found"""
        self.stdout.write("⚠️  Using embedded sample data (limited set)")
        
        return {
            'metadata': {
                'total_mcqs': 10,
                'source_files': 5,
                'generated_date': datetime.now().isoformat(),
                'note': 'Embedded sample data'
            },
            'mcqs': [
                {
                    "question_number": "1",
                    "question": "A 65-year-old man presents with sudden onset of right-sided weakness and difficulty speaking. His symptoms began 2 hours ago. CT scan shows no hemorrhage. What is the most appropriate immediate treatment?",
                    "options": ["Aspirin 325 mg", "Intravenous tissue plasminogen activator (tPA)", "Heparin infusion", "Warfarin", "Clopidogrel 300 mg"],
                    "correct_answer": "B",
                    "correct_answer_text": "Intravenous tissue plasminogen activator (tPA)",
                    "subspecialty": "Vascular Neurology/Stroke",
                    "exam_year": "2024",
                    "exam_type": "Part II",
                    "ai_generated": True,
                    "explanation": {
                        "option_analysis": "IV tPA is the gold standard for acute ischemic stroke within 4.5 hours.",
                        "clinical_manifestation": "Acute focal neurological deficits with hemiparesis and aphasia.",
                        "management_principles": "Time is brain - administer IV tPA after excluding hemorrhage."
                    },
                    "source_file": "vascular_neurology_stroke_mcqs.json"
                }
                # Add 9 more sample MCQs here if needed...
            ]
        }