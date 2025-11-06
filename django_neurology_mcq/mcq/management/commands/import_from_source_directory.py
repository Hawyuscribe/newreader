from django.core.management.base import BaseCommand
from mcq.models import MCQ, Flashcard, IncorrectAnswer, Bookmark
from django.db import transaction
import json
import os
from pathlib import Path
from datetime import datetime

class Command(BaseCommand):
    help = 'Import all MCQs directly from source specialty JSON files'

    def handle(self, *args, **options):
        self.stdout.write(f"\n{'='*60}")
        self.stdout.write(f"🚀 DIRECT SOURCE MCQ IMPORT - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        self.stdout.write(f"{'='*60}\n")
        
        # Clear existing data
        with transaction.atomic():
            self.stdout.write("🧹 Clearing existing data...")
            Flashcard.objects.all().delete()
            IncorrectAnswer.objects.all().delete()
            Bookmark.objects.all().delete()
            deleted = MCQ.objects.all().delete()[0]
            self.stdout.write(f"   Deleted {deleted} existing MCQs\n")
        
        # Source directory
        source_dir = Path('/Users/tariqalmatrudi/Documents/FFF/output_by_specialty')
        
        if not source_dir.exists():
            self.stdout.write(self.style.ERROR(f"❌ Source directory not found: {source_dir}"))
            return
        
        # Get all JSON files
        json_files = list(source_dir.glob('*.json'))
        self.stdout.write(f"📁 Found {len(json_files)} JSON files in source directory")
        
        total_imported = 0
        file_stats = {}
        
        # Process each file
        for json_file in sorted(json_files):
            self.stdout.write(f"\n📄 Processing: {json_file.name}")
            
            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                specialty = data.get('specialty', 'Unknown')
                mcqs = data.get('mcqs', [])
                
                self.stdout.write(f"   Specialty: {specialty}")
                self.stdout.write(f"   MCQs in file: {len(mcqs)}")
                
                file_imported = 0
                
                with transaction.atomic():
                    for mcq_data in mcqs:
                        try:
                            # Map explanation sections correctly
                            explanation_data = mcq_data.get('explanation', {})
                            explanation_sections = {}
                            
                            if isinstance(explanation_data, dict):
                                # Direct mapping of sections
                                field_mapping = {
                                    'option_analysis': 'option_analysis',
                                    'conceptual_foundation': 'conceptual_foundation',
                                    'pathophysiology': 'pathophysiological_mechanisms',
                                    'pathophysiological_mechanisms': 'pathophysiological_mechanisms',
                                    'clinical_manifestation': 'clinical_correlation',
                                    'clinical_correlation': 'clinical_correlation',
                                    'diagnostic_approach': 'diagnostic_approach',
                                    'classification_and_nosology': 'classification_and_nosology',
                                    'management_principles': 'management_principles',
                                    'follow_up_guidelines': 'follow_up_guidelines',
                                    'clinical_pearls': 'clinical_pearls',
                                    'references': 'current_evidence',
                                    'current_evidence': 'current_evidence'
                                }
                                
                                for source_key, target_key in field_mapping.items():
                                    if source_key in explanation_data:
                                        explanation_sections[target_key] = explanation_data[source_key]
                            
                            # Create MCQ
                            mcq = MCQ(
                                question_number=mcq_data.get('question_number', ''),
                                question_text=mcq_data.get('question', ''),  # Note: 'question' not 'question_text'
                                options=mcq_data.get('options', []),
                                correct_answer=mcq_data.get('correct_answer', ''),
                                correct_answer_text=mcq_data.get('correct_answer_text', ''),
                                subspecialty=mcq_data.get('subspecialty', specialty),  # Use file specialty as fallback
                                source_file=mcq_data.get('source_file', json_file.name),
                                exam_type=mcq_data.get('exam_type', ''),
                                exam_year=mcq_data.get('exam_year', ''),
                                ai_generated=mcq_data.get('ai_generated', False),
                                explanation_sections=explanation_sections,
                                image_url=mcq_data.get('image_url', ''),
                                difficulty_level=mcq_data.get('difficulty_level', ''),
                                key_concept=mcq_data.get('key_concept', ''),
                                primary_category=mcq_data.get('primary_category', ''),
                                secondary_category=mcq_data.get('secondary_category', ''),
                                verification_confidence=mcq_data.get('verification_confidence', '')
                            )
                            
                            # Set unified explanation
                            unified = mcq_data.get('unified_explanation', '')
                            if unified:
                                mcq.unified_explanation = unified
                                mcq.explanation = unified
                            
                            mcq.save()
                            file_imported += 1
                            total_imported += 1
                            
                        except Exception as e:
                            self.stdout.write(f"      ❌ Error importing MCQ {mcq_data.get('question_number', '?')}: {str(e)[:100]}")
                            continue
                
                file_stats[json_file.name] = {
                    'specialty': specialty,
                    'total': len(mcqs),
                    'imported': file_imported
                }
                
                self.stdout.write(f"   ✅ Imported {file_imported}/{len(mcqs)} MCQs")
                
            except Exception as e:
                self.stdout.write(f"   ❌ Error processing file: {str(e)}")
                continue
        
        # Final report
        self.stdout.write(f"\n{'='*60}")
        self.stdout.write(self.style.SUCCESS(f"🎉 IMPORT COMPLETE!"))
        self.stdout.write(f"{'='*60}")
        self.stdout.write(f"✅ Total MCQs imported: {total_imported}")
        self.stdout.write(f"✅ Total MCQs in database: {MCQ.objects.count()}")
        
        # Show subspecialty breakdown
        from django.db.models import Count
        subspecialties = MCQ.objects.values('subspecialty').annotate(
            count=Count('id')
        ).order_by('-count')
        
        self.stdout.write(f"\n📊 Subspecialty breakdown:")
        for spec in subspecialties:
            self.stdout.write(f"   {spec['subspecialty']:<35} {spec['count']:>4} MCQs")
        
        # Show file import summary
        self.stdout.write(f"\n📋 File import summary:")
        for filename, stats in file_stats.items():
            status = "✅" if stats['imported'] == stats['total'] else "⚠️"
            self.stdout.write(f"   {status} {filename:<40} {stats['imported']}/{stats['total']} MCQs")
        
        self.stdout.write(f"\n🌐 Import from source directory complete!")
        self.stdout.write(f"{'='*60}\n")