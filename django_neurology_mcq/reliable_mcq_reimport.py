#!/usr/bin/env python
"""
Reliable MCQ re-import script with verification
"""
import os
import sys
import json
import django
from datetime import datetime
from collections import defaultdict

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mcq.settings')
django.setup()

from django.db import transaction, connection
from mcq.models import MCQ, Subspecialty

class MCQReimporter:
    def __init__(self):
        self.expected_counts = {
            "Movement Disorders": 269,
            "Vascular Neurology/Stroke": 439,
            "Neuromuscular": 483,
            "Total": 2853
        }
        self.log_file = f"reimport_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        
    def log(self, message):
        """Log message to console and file"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"[{timestamp}] {message}"
        print(log_entry)
        with open(self.log_file, 'a') as f:
            f.write(log_entry + '\n')
    
    def verify_current_state(self):
        """Verify current database state"""
        self.log("=" * 80)
        self.log("VERIFYING CURRENT DATABASE STATE")
        self.log("=" * 80)
        
        total_mcqs = MCQ.objects.count()
        self.log(f"Total MCQs currently in database: {total_mcqs}")
        
        # Count by subspecialty
        subspecialty_counts = defaultdict(int)
        for mcq in MCQ.objects.all():
            if mcq.subspecialty:
                subspecialty_counts[mcq.subspecialty.name] += 1
        
        self.log("\nCurrent subspecialty counts:")
        for sub_name, count in sorted(subspecialty_counts.items()):
            self.log(f"  {sub_name}: {count}")
        
        return total_mcqs, subspecialty_counts
    
    def clear_all_mcqs(self):
        """Clear all MCQs from database"""
        self.log("\n" + "=" * 80)
        self.log("CLEARING ALL MCQs")
        self.log("=" * 80)
        
        try:
            with transaction.atomic():
                # Get count before deletion
                count_before = MCQ.objects.count()
                self.log(f"MCQs before deletion: {count_before}")
                
                # Delete all MCQs
                deleted_count = MCQ.objects.all().delete()[0]
                self.log(f"Deleted {deleted_count} MCQs")
                
                # Verify deletion
                count_after = MCQ.objects.count()
                self.log(f"MCQs after deletion: {count_after}")
                
                if count_after != 0:
                    raise Exception(f"Failed to delete all MCQs! {count_after} remaining")
                
                # Reset database sequences if using PostgreSQL
                if 'postgresql' in connection.settings_dict['ENGINE']:
                    with connection.cursor() as cursor:
                        cursor.execute("SELECT setval(pg_get_serial_sequence('mcq_mcq', 'id'), 1, false);")
                        self.log("Reset PostgreSQL sequence for MCQ IDs")
                
                self.log("Successfully cleared all MCQs")
                return True
                
        except Exception as e:
            self.log(f"ERROR clearing MCQs: {str(e)}")
            return False
    
    def load_fixture_files(self):
        """Load all fixture files"""
        self.log("\n" + "=" * 80)
        self.log("LOADING FIXTURE FILES")
        self.log("=" * 80)
        
        all_mcqs = []
        
        # Check for rere_fixtures.json first
        rere_path = '/Users/tariqalmatrudi/NEWreader/django_neurology_mcq/rere_fixtures.json'
        if os.path.exists(rere_path):
            self.log(f"Loading {rere_path}")
            try:
                with open(rere_path, 'r') as f:
                    data = json.load(f)
                    mcqs = [item for item in data if item['model'] == 'mcq.mcq']
                    self.log(f"  Found {len(mcqs)} MCQs in rere_fixtures.json")
                    all_mcqs.extend(mcqs)
            except Exception as e:
                self.log(f"  ERROR loading {rere_path}: {str(e)}")
        
        # Check for fixture chunks
        fixtures_dir = '/Users/tariqalmatrudi/NEWreader/django_neurology_mcq/fixtures'
        if os.path.exists(fixtures_dir):
            fixture_files = sorted([f for f in os.listdir(fixtures_dir) if f.endswith('.json')])
            self.log(f"Found {len(fixture_files)} fixture files in {fixtures_dir}")
            
            for fixture_file in fixture_files:
                fixture_path = os.path.join(fixtures_dir, fixture_file)
                try:
                    with open(fixture_path, 'r') as f:
                        data = json.load(f)
                        mcqs = [item for item in data if item['model'] == 'mcq.mcq']
                        self.log(f"  {fixture_file}: {len(mcqs)} MCQs")
                        all_mcqs.extend(mcqs)
                except Exception as e:
                    self.log(f"  ERROR loading {fixture_file}: {str(e)}")
        
        # Check for rere_chunks
        rere_chunks_dir = '/Users/tariqalmatrudi/NEWreader/django_neurology_mcq/rere_chunks'
        if os.path.exists(rere_chunks_dir):
            chunk_files = sorted([f for f in os.listdir(rere_chunks_dir) if f.endswith('.json')])
            self.log(f"Found {len(chunk_files)} chunk files in {rere_chunks_dir}")
            
            for chunk_file in chunk_files:
                chunk_path = os.path.join(rere_chunks_dir, chunk_file)
                try:
                    with open(chunk_path, 'r') as f:
                        data = json.load(f)
                        mcqs = [item for item in data if item['model'] == 'mcq.mcq']
                        self.log(f"  {chunk_file}: {len(mcqs)} MCQs")
                        all_mcqs.extend(mcqs)
                except Exception as e:
                    self.log(f"  ERROR loading {chunk_file}: {str(e)}")
        
        self.log(f"\nTotal MCQs loaded from all files: {len(all_mcqs)}")
        
        # Remove duplicates based on question text
        unique_mcqs = {}
        for mcq in all_mcqs:
            question = mcq['fields']['question']
            if question not in unique_mcqs:
                unique_mcqs[question] = mcq
        
        self.log(f"Unique MCQs after deduplication: {len(unique_mcqs)}")
        
        return list(unique_mcqs.values())
    
    def import_mcqs(self, mcq_fixtures):
        """Import MCQs into database"""
        self.log("\n" + "=" * 80)
        self.log("IMPORTING MCQs")
        self.log("=" * 80)
        
        # Create subspecialty mapping
        subspecialties = {}
        for sub in Subspecialty.objects.all():
            subspecialties[sub.name] = sub
        
        imported_count = 0
        error_count = 0
        subspecialty_counts = defaultdict(int)
        
        with transaction.atomic():
            for i, mcq_data in enumerate(mcq_fixtures):
                try:
                    fields = mcq_data['fields']
                    
                    # Get subspecialty
                    subspecialty = None
                    if 'subspecialty' in fields and fields['subspecialty']:
                        sub_name = fields['subspecialty']
                        if isinstance(sub_name, list) and sub_name:
                            sub_name = sub_name[0]
                        
                        if sub_name in subspecialties:
                            subspecialty = subspecialties[sub_name]
                            subspecialty_counts[sub_name] += 1
                    
                    # Create MCQ
                    mcq = MCQ(
                        question=fields['question'],
                        option_a=fields.get('option_a', ''),
                        option_b=fields.get('option_b', ''),
                        option_c=fields.get('option_c', ''),
                        option_d=fields.get('option_d', ''),
                        option_e=fields.get('option_e', ''),
                        correct_answer=fields.get('correct_answer', 'A'),
                        explanation=fields.get('explanation', ''),
                        exam_type=fields.get('exam_type', ''),
                        year=fields.get('year'),
                        subspecialty=subspecialty,
                        difficulty=fields.get('difficulty', 'medium'),
                        topic=fields.get('topic', ''),
                        subtopic=fields.get('subtopic', ''),
                        clinical_vignette=fields.get('clinical_vignette', False),
                        image_question=fields.get('image_question', False),
                        requires_calculator=fields.get('requires_calculator', False)
                    )
                    
                    mcq.save()
                    imported_count += 1
                    
                    if (i + 1) % 100 == 0:
                        self.log(f"  Imported {i + 1}/{len(mcq_fixtures)} MCQs...")
                        
                except Exception as e:
                    error_count += 1
                    self.log(f"  ERROR importing MCQ {i + 1}: {str(e)}")
                    if error_count > 10:
                        self.log("  Too many errors, stopping import")
                        raise
        
        self.log(f"\nImport completed:")
        self.log(f"  Successfully imported: {imported_count}")
        self.log(f"  Errors: {error_count}")
        
        self.log("\nImported subspecialty counts:")
        for sub_name, count in sorted(subspecialty_counts.items()):
            expected = self.expected_counts.get(sub_name, 'N/A')
            status = "✓" if count == expected else "✗"
            self.log(f"  {sub_name}: {count} (expected: {expected}) {status}")
        
        return imported_count, subspecialty_counts
    
    def verify_import(self):
        """Verify the import was successful"""
        self.log("\n" + "=" * 80)
        self.log("VERIFYING IMPORT")
        self.log("=" * 80)
        
        total_mcqs = MCQ.objects.count()
        expected_total = self.expected_counts['Total']
        
        self.log(f"Total MCQs in database: {total_mcqs}")
        self.log(f"Expected total: {expected_total}")
        
        if total_mcqs == expected_total:
            self.log("✓ Total count matches expected!")
        else:
            self.log(f"✗ Total count mismatch! Difference: {total_mcqs - expected_total}")
        
        # Check specific subspecialties
        subspecialty_counts = defaultdict(int)
        for mcq in MCQ.objects.all():
            if mcq.subspecialty:
                subspecialty_counts[mcq.subspecialty.name] += 1
        
        all_correct = True
        for sub_name, expected_count in self.expected_counts.items():
            if sub_name == 'Total':
                continue
                
            actual_count = subspecialty_counts.get(sub_name, 0)
            if actual_count == expected_count:
                self.log(f"✓ {sub_name}: {actual_count} (correct)")
            else:
                self.log(f"✗ {sub_name}: {actual_count} (expected {expected_count}, diff: {actual_count - expected_count})")
                all_correct = False
        
        return all_correct
    
    def run_reimport(self):
        """Run the complete reimport process"""
        self.log("Starting reliable MCQ reimport process...")
        self.log(f"Log file: {self.log_file}")
        
        # Step 1: Verify current state
        self.verify_current_state()
        
        # Step 2: Clear all MCQs
        if not self.clear_all_mcqs():
            self.log("Failed to clear MCQs. Aborting.")
            return False
        
        # Step 3: Load fixture files
        mcq_fixtures = self.load_fixture_files()
        if not mcq_fixtures:
            self.log("No MCQ fixtures found. Aborting.")
            return False
        
        # Step 4: Import MCQs
        imported_count, subspecialty_counts = self.import_mcqs(mcq_fixtures)
        
        # Step 5: Verify import
        success = self.verify_import()
        
        self.log("\n" + "=" * 80)
        if success:
            self.log("REIMPORT COMPLETED SUCCESSFULLY!")
        else:
            self.log("REIMPORT COMPLETED WITH ISSUES - CHECK COUNTS!")
        self.log("=" * 80)
        
        return success

if __name__ == "__main__":
    reimporter = MCQReimporter()
    reimporter.run_reimport()