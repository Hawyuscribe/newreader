from django.core.management.base import BaseCommand
from django.db.models import Count
from mcq.models import MCQ
import json
import os
from collections import defaultdict

class Command(BaseCommand):
    help = 'Analyze duplicate MCQs in source files and database'

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
        self.stdout.write("=== Analyzing Duplicates ===\n")
        
        # Step 1: Analyze duplicates in source files
        consolidated_dir = '/Users/tariqalmatrudi/NEWreader/consolidated_mcqs'
        source_mcqs = []
        
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
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Error loading {filename}: {str(e)}"))
        
        total_source = len(source_mcqs)
        self.stdout.write(f"Total MCQ entries in source files: {total_source}")
        
        # Find duplicates in source files
        question_occurrences = defaultdict(list)
        for mcq in source_mcqs:
            normalized = self.normalize_text(mcq.get('question_text', ''))
            if normalized:
                question_occurrences[normalized].append(mcq)
        
        # Count unique questions
        unique_questions = len(question_occurrences)
        duplicate_count = total_source - unique_questions
        
        self.stdout.write(f"\nUnique questions in source files: {unique_questions}")
        self.stdout.write(f"Duplicate entries: {duplicate_count}")
        
        # Show duplicate examples
        self.stdout.write("\n=== Examples of Duplicates in Source Files ===")
        dup_examples = 0
        for question_text, mcqs in question_occurrences.items():
            if len(mcqs) > 1 and dup_examples < 5:
                dup_examples += 1
                self.stdout.write(f"\nDuplicate {dup_examples}: Question appears {len(mcqs)} times")
                self.stdout.write(f"  Question: {question_text[:150]}...")
                self.stdout.write("  Found in:")
                for mcq in mcqs:
                    self.stdout.write(f"    - {mcq['_source_file']} ({mcq.get('exam_type', '')} {mcq.get('exam_year', '')})")
        
        # Analyze files with most duplicates
        file_duplicate_counts = defaultdict(int)
        for question_text, mcqs in question_occurrences.items():
            if len(mcqs) > 1:
                files = set(mcq['_source_file'] for mcq in mcqs)
                for file in files:
                    file_duplicate_counts[file] += 1
        
        if file_duplicate_counts:
            self.stdout.write("\n=== Files with Duplicate Questions ===")
            for file, count in sorted(file_duplicate_counts.items(), key=lambda x: x[1], reverse=True):
                self.stdout.write(f"  {file}: {count} questions appear in multiple files")
        
        # Step 2: Check database status
        db_count = MCQ.objects.count()
        self.stdout.write(f"\n=== Database Status ===")
        self.stdout.write(f"Total MCQs in database: {db_count}")
        
        # Check for duplicates in database (should be none due to unique constraint)
        duplicate_questions = MCQ.objects.values('question_text').annotate(
            count=Count('id')
        ).filter(count__gt=1)
        
        if duplicate_questions.exists():
            self.stdout.write(self.style.WARNING(f"Found {duplicate_questions.count()} duplicate questions in database!"))
        else:
            self.stdout.write("No duplicate questions in database (as expected)")
        
        # Final summary
        self.stdout.write(f"\n=== Summary ===")
        self.stdout.write(f"Source files contain: {total_source} MCQ entries")
        self.stdout.write(f"Unique questions: {unique_questions}")
        self.stdout.write(f"Duplicates in source: {duplicate_count}")
        self.stdout.write(f"Database contains: {db_count} MCQs")
        self.stdout.write(f"Difference: {unique_questions - db_count} unique questions not in database")
        
        # If there's still a difference, let's find what's missing
        if unique_questions > db_count:
            self.stdout.write("\nChecking for questions that might be missing...")
            
            # Get all normalized questions from database
            db_questions = set()
            for mcq in MCQ.objects.all():
                db_questions.add(self.normalize_text(mcq.question_text))
            
            # Find unique questions not in database
            missing_count = 0
            for question_text, mcqs in question_occurrences.items():
                if question_text not in db_questions:
                    missing_count += 1
                    if missing_count <= 5:
                        self.stdout.write(f"\nMissing question {missing_count}:")
                        self.stdout.write(f"  Question: {question_text[:150]}...")
                        self.stdout.write(f"  From: {mcqs[0]['_source_file']}")
                        self.stdout.write(f"  Correct answer: {mcqs[0].get('correct_answer', '')}")
            
            self.stdout.write(f"\nTotal missing unique questions: {missing_count}")