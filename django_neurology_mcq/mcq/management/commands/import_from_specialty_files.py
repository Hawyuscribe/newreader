from django.core.management.base import BaseCommand
from mcq.models import MCQ, Flashcard, IncorrectAnswer, Bookmark
from django.db import transaction
import json
import os
from pathlib import Path
from datetime import datetime

class Command(BaseCommand):
    help = 'Import MCQs from specialty JSON files in /Users/tariqalmatrudi/Documents/FFF/output_by_specialty'

    def handle(self, *args, **options):
        self.stdout.write(f"\n{'='*60}")
        self.stdout.write(f"MCQ Import from Specialty Files - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        self.stdout.write(f"{'='*60}\n")
        
        # Clear existing data
        with transaction.atomic():
            self.stdout.write("Clearing existing data...")
            Flashcard.objects.all().delete()
            IncorrectAnswer.objects.all().delete()
            Bookmark.objects.all().delete()
            deleted = MCQ.objects.all().delete()[0]
            self.stdout.write(f"Deleted {deleted} existing MCQs\n")
        
        # Define the source directory
        source_dir = Path('/Users/tariqalmatrudi/Documents/FFF/output_by_specialty')
        
        # Get all JSON files in the directory
        json_files = sorted(source_dir.glob('*.json'))
        self.stdout.write(f"Found {len(json_files)} JSON files in {source_dir}\n")
        
        total_imported = 0
        
        # Process each specialty file
        for file_path in json_files:
            filename = file_path.name
            self.stdout.write(f"\nProcessing {filename}...")
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                mcqs = data.get('mcqs', [])
                imported_from_file = 0
                
                with transaction.atomic():
                    for mcq_data in mcqs:
                        try:
                            # Extract options
                            options = mcq_data.get('options', [])
                            option_a = options[0] if len(options) > 0 else ''
                            option_b = options[1] if len(options) > 1 else ''
                            option_c = options[2] if len(options) > 2 else ''
                            option_d = options[3] if len(options) > 3 else ''
                            option_e = options[4] if len(options) > 4 else ''
                            
                            # Get explanation sections
                            explanation_data = mcq_data.get('explanation', {})
                            
                            # Build explanation sections matching the template structure
                            explanation_sections = {}
                            
                            if isinstance(explanation_data, dict):
                                # Map the fields to our template sections
                                if 'option_analysis' in explanation_data:
                                    explanation_sections['option_analysis'] = explanation_data['option_analysis']
                                if 'clinical_manifestation' in explanation_data:
                                    explanation_sections['clinical_manifestation'] = explanation_data['clinical_manifestation']
                                if 'diagnostic_approach' in explanation_data:
                                    explanation_sections['diagnostic_approach'] = explanation_data['diagnostic_approach']
                                if 'management_principles' in explanation_data:
                                    explanation_sections['management_principles'] = explanation_data['management_principles']
                                if 'follow_up_guidelines' in explanation_data:
                                    explanation_sections['follow_up_guidelines'] = explanation_data['follow_up_guidelines']
                                if 'conceptual_foundation' in explanation_data:
                                    explanation_sections['conceptual_foundation'] = explanation_data['conceptual_foundation']
                                if 'pathophysiology' in explanation_data:
                                    explanation_sections['pathophysiology'] = explanation_data['pathophysiology']
                                if 'clinical_pearls' in explanation_data:
                                    explanation_sections['clinical_pearls'] = explanation_data['clinical_pearls']
                                if 'references' in explanation_data:
                                    explanation_sections['references'] = explanation_data['references']
                            
                            # Create unified explanation from all sections
                            unified_explanation = mcq_data.get('unified_explanation', '')
                            if not unified_explanation and explanation_sections:
                                # Build from sections if no unified explanation
                                unified_explanation = '\n\n'.join([
                                    f"{k.replace('_', ' ').title()}: {v}"
                                    for k, v in explanation_sections.items()
                                    if v and v not in ['This section information is included within the unified explanation.']
                                ])
                            
                            # Get exam info
                            exam_name = mcq_data.get('exam_type', '')
                            if mcq_data.get('exam_year'):
                                exam_name = f"{exam_name} {mcq_data['exam_year']}" if exam_name else str(mcq_data['exam_year'])
                            
                            # Create MCQ
                            mcq = MCQ(
                                question=mcq_data['question'],
                                option_a=option_a,
                                option_b=option_b,
                                option_c=option_c,
                                option_d=option_d,
                                option_e=option_e,
                                correct_answer=mcq_data.get('correct_answer', ''),
                                explanation=unified_explanation,
                                explanation_sections=explanation_sections,
                                specialty='Neurology',
                                subspecialty=mcq_data.get('subspecialty', data.get('specialty', 'General Neurology')),
                                exam_name=exam_name,
                                year=mcq_data.get('exam_year'),
                                topic='',  # Not in source data
                                difficulty=3,  # Default
                                cognitive_level='Recall',  # Default
                                references=explanation_sections.get('references', ''),
                                high_yield=False,  # Default
                                image_url=''  # Not in source data
                            )
                            mcq.save()
                            imported_from_file += 1
                            total_imported += 1
                            
                        except Exception as e:
                            self.stdout.write(f"  Error importing MCQ: {str(e)[:100]}")
                            continue
                
                self.stdout.write(f"  Imported {imported_from_file} MCQs from {filename}")
                
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"  Error processing {filename}: {e}"))
        
        # Final verification
        total_in_db = MCQ.objects.count()
        self.stdout.write(f"\n{'='*60}")
        self.stdout.write(self.style.SUCCESS(f"Import Complete!"))
        self.stdout.write(f"Total MCQs imported: {total_imported}")
        self.stdout.write(f"Total MCQs in database: {total_in_db}")
        
        # Show subspecialty breakdown
        from django.db.models import Count
        subspecialties = MCQ.objects.values('subspecialty').annotate(
            count=Count('id')
        ).order_by('-count')[:15]
        
        self.stdout.write(f"\nSubspecialty breakdown:")
        expected = {
            'Neuromuscular': 483,
            'Vascular Neurology/Stroke': 439,
            'Neuroimmunology': 299,
            'Epilepsy': 284,
            'Movement Disorders': 269,
            'Critical Care Neurology': 199,
            'Neuro-Oncology': 193,
            'Headache Medicine': 157,
            'Dementia': 156,
            'Neuro-Infectious Diseases': 152,
            'Pediatric Neurology': 122,
            'General Neurology': 74,
            'Neuropharmacology': 15,
            'Neurogenetics': 6,
            'Behavioral Neurology': 5
        }
        
        for spec in subspecialties:
            name = spec['subspecialty']
            count = spec['count']
            expected_count = expected.get(name, 0)
            status = "✅" if count == expected_count else "❌"
            self.stdout.write(f"  {name}: {count} (expected {expected_count}) {status}")
        
        if total_in_db == 2853:
            self.stdout.write(self.style.SUCCESS(f"\n✅ Success! MCQ count matches expected total."))
        else:
            self.stdout.write(self.style.WARNING(f"\n⚠️  Expected 2853 MCQs, got {total_in_db}"))
        
        self.stdout.write(f"{'='*60}\n")