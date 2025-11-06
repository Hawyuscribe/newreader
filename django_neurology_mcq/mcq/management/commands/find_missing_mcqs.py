from django.core.management.base import BaseCommand
from django.db import transaction
from django.db.models import Count
from mcq.models import MCQ
import json
import os
from collections import defaultdict
import difflib

class Command(BaseCommand):
    help = 'Find MCQs that are in source files but not in database'

    def normalize_text(self, text):
        """Normalize text for comparison"""
        if not text:
            return ""
        # Remove extra whitespace, normalize quotes
        text = ' '.join(text.split())
        text = text.replace('"', '"').replace('"', '"')
        text = text.replace(''', "'").replace(''', "'")
        return text.strip()

    def handle(self, *args, **options):
        self.stdout.write("=== Finding Missing MCQs ===\n")
        
        # Load all MCQs from source files
        consolidated_dir = '/Users/tariqalmatrudi/NEWreader/consolidated_mcqs'
        source_mcqs = []
        source_by_file = defaultdict(list)
        
        self.stdout.write("Loading MCQs from source files...")
        for filename in sorted(os.listdir(consolidated_dir)):
            if filename.endswith('.json') and not filename.startswith('.'):
                filepath = os.path.join(consolidated_dir, filename)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        mcqs = data.get('mcqs', [])
                        for mcq in mcqs:
                            mcq['_source_file'] = filename
                            source_mcqs.append(mcq)
                            source_by_file[filename].append(mcq)
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Error loading {filename}: {str(e)}"))
        
        total_source = len(source_mcqs)
        self.stdout.write(f"\nTotal MCQs in source files: {total_source}")
        
        # Get all MCQs from database
        db_mcqs = list(MCQ.objects.all())
        db_count = len(db_mcqs)
        self.stdout.write(f"Total MCQs in database: {db_count}")
        
        # Create normalized question text sets for comparison
        db_questions_normalized = {}
        for mcq in db_mcqs:
            normalized = self.normalize_text(mcq.question_text)
            db_questions_normalized[normalized] = mcq
        
        # Find missing MCQs
        missing_mcqs = []
        found_count = 0
        
        self.stdout.write("\nAnalyzing MCQs...")
        for source_mcq in source_mcqs:
            source_text = self.normalize_text(source_mcq.get('question_text', ''))
            
            if source_text in db_questions_normalized:
                found_count += 1
            else:
                # Try fuzzy matching for very similar questions
                similar_found = False
                for db_text in db_questions_normalized:
                    similarity = difflib.SequenceMatcher(None, source_text[:200], db_text[:200]).ratio()
                    if similarity > 0.95:  # 95% similar
                        similar_found = True
                        break
                
                if not similar_found:
                    missing_mcqs.append(source_mcq)
        
        self.stdout.write(f"\nFound {found_count} MCQs that exist in database")
        self.stdout.write(f"Found {len(missing_mcqs)} MCQs that are missing")
        
        # Analyze missing MCQs by file
        missing_by_file = defaultdict(list)
        for mcq in missing_mcqs:
            missing_by_file[mcq['_source_file']].append(mcq)
        
        self.stdout.write("\n=== Missing MCQs by File ===")
        for filename, mcqs in sorted(missing_by_file.items()):
            total_in_file = len(source_by_file[filename])
            missing_in_file = len(mcqs)
            self.stdout.write(f"{filename}: {missing_in_file}/{total_in_file} missing")
        
        # Show examples of missing MCQs
        if missing_mcqs:
            self.stdout.write("\n=== Examples of Missing MCQs ===")
            for i, mcq in enumerate(missing_mcqs[:5]):
                self.stdout.write(f"\nMissing MCQ {i+1}:")
                self.stdout.write(f"  File: {mcq['_source_file']}")
                self.stdout.write(f"  Question: {mcq.get('question_text', '')[:150]}...")
                self.stdout.write(f"  Exam: {mcq.get('exam_type', '')} {mcq.get('exam_year', '')}")
                self.stdout.write(f"  Subspecialty: {mcq.get('subspecialty', '')}")
                self.stdout.write(f"  Correct Answer: {mcq.get('correct_answer', '')}")
                
                # Check specific issues
                correct_answer = str(mcq.get('correct_answer', ''))
                if len(correct_answer) > 5:
                    self.stdout.write(self.style.WARNING(f"  Issue: Correct answer too long ({len(correct_answer)} chars)"))
        
        # Export missing MCQs for manual review
        if missing_mcqs:
            export_file = 'missing_mcqs_export.json'
            with open(export_file, 'w', encoding='utf-8') as f:
                json.dump({
                    'total_missing': len(missing_mcqs),
                    'missing_by_file': {k: len(v) for k, v in missing_by_file.items()},
                    'missing_mcqs': missing_mcqs
                }, f, indent=2, ensure_ascii=False)
            self.stdout.write(f"\nExported {len(missing_mcqs)} missing MCQs to {export_file}")
        
        # Show subspecialty distribution
        self.stdout.write("\n=== Current Database Subspecialty Distribution ===")
        subspecialty_counts = MCQ.objects.values('subspecialty').annotate(
            count=Count('subspecialty')
        ).order_by('-count')
        
        for item in subspecialty_counts:
            self.stdout.write(f"  {item['subspecialty']}: {item['count']} MCQs")