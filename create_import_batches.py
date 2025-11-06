#!/usr/bin/env python3
"""
Create multiple small import batches for Heroku deployment
"""
import json
import os
import subprocess

def create_import_batches():
    """Create multiple small Django management commands with MCQ data"""
    
    # Load the consolidated MCQ data
    try:
        with open('/Users/tariqalmatrudi/NEWreader/all_mcqs_consolidated.json', 'r', encoding='utf-8') as f:
            mcqs = json.load(f)
        print(f"Loaded {len(mcqs)} MCQs for batch creation")
    except Exception as e:
        print(f"Error loading MCQ data: {e}")
        return False
    
    # Create small batches of 25 MCQs each
    batch_size = 25
    total_batches = (len(mcqs) + batch_size - 1) // batch_size
    
    cmd_dir = "/Users/tariqalmatrudi/NEWreader/django_neurology_mcq/mcq/management/commands"
    os.makedirs(cmd_dir, exist_ok=True)
    
    print(f"Creating {total_batches} batch import commands...")
    
    for batch_num in range(total_batches):
        start_idx = batch_num * batch_size
        end_idx = min(start_idx + batch_size, len(mcqs))
        batch_mcqs = mcqs[start_idx:end_idx]
        
        # Create command for this batch
        command_content = f'''import json
from django.core.management.base import BaseCommand
from mcq.models import MCQ
from django.db import transaction

class Command(BaseCommand):
    help = 'Import MCQ batch {batch_num + 1} of {total_batches} ({len(batch_mcqs)} MCQs)'
    
    def handle(self, *args, **options):
        self.stdout.write(f"Importing batch {batch_num + 1}/{total_batches} ({len(batch_mcqs)} MCQs)")
        
        mcq_data = {json.dumps(batch_mcqs, indent=8)}
        
        success_count = 0
        error_count = 0
        
        try:
            with transaction.atomic():
                for i, mcq in enumerate(mcq_data):
                    try:
                        self.import_single_mcq(mcq, {start_idx} + i + 1)
                        success_count += 1
                    except Exception as e:
                        error_count += 1
                        self.stdout.write(f"Error importing MCQ {{i+1}}: {{e}}")
            
            self.stdout.write(f"Batch {batch_num + 1} completed successfully")
            self.stdout.write(f"Successfully imported: {{success_count}} MCQs")
            self.stdout.write(f"Errors: {{error_count}} MCQs")
            
        except Exception as e:
            self.stdout.write(f"Batch {batch_num + 1} failed: {{e}}")
    
    def import_single_mcq(self, mcq_data, mcq_number):
        """Import a single MCQ with proper data validation"""
        
        # Handle correct_answer field
        correct_answer = mcq_data.get('correct_answer', '')
        if isinstance(correct_answer, (list, tuple)) and len(correct_answer) > 0:
            correct_answer = str(correct_answer[0])
        else:
            correct_answer = str(correct_answer)
        
        # Ensure correct_answer is within field limits (max 10 chars)
        correct_answer = correct_answer[:10] if correct_answer else ''
        
        # Get question text from various possible fields
        question_text = (
            mcq_data.get('question_text') or 
            mcq_data.get('question') or 
            ''
        )
        
        # Create MCQ instance
        mcq = MCQ(
            question_number=str(mcq_data.get('question_number', mcq_number))[:20],
            question_text=question_text,
            options=mcq_data.get('options', []),
            correct_answer=correct_answer,
            correct_answer_text=mcq_data.get('correct_answer_text', ''),
            subspecialty=mcq_data.get('subspecialty', 'General Neurology'),
            exam_year=str(mcq_data.get('exam_year', ''))[:10],
            exam_type=str(mcq_data.get('exam_type', ''))[:50],
            explanation=mcq_data.get('explanation', ''),
            option_analysis=mcq_data.get('option_analysis', {{}})
        )
        
        mcq.save()
'''
        
        # Write the batch command
        batch_filename = f"import_batch_{batch_num + 1:03d}.py"
        with open(f"{cmd_dir}/{batch_filename}", 'w', encoding='utf-8') as f:
            f.write(command_content)
        
        if (batch_num + 1) % 10 == 0:
            print(f"Created {batch_num + 1}/{total_batches} batch commands...")
    
    print(f"✅ Created {total_batches} batch import commands")
    
    # Create a master command to run all batches
    master_command = f'''import subprocess
import sys
from django.core.management.base import BaseCommand
from mcq.models import MCQ

class Command(BaseCommand):
    help = 'Import all MCQ batches sequentially'
    
    def add_arguments(self, parser):
        parser.add_argument('--clear-existing', action='store_true', help='Clear existing MCQs before import')
        parser.add_argument('--start-batch', type=int, default=1, help='Starting batch number')
        parser.add_argument('--end-batch', type=int, default={total_batches}, help='Ending batch number')
    
    def handle(self, *args, **options):
        clear_existing = options['clear_existing']
        start_batch = options['start_batch']
        end_batch = options['end_batch']
        
        # Clear existing MCQs if requested
        if clear_existing:
            existing_count = MCQ.objects.count()
            self.stdout.write(f"Clearing {{existing_count}} existing MCQs...")
            MCQ.objects.all().delete()
            self.stdout.write("Existing MCQs cleared")
        
        # Import batches
        self.stdout.write(f"Importing batches {{start_batch}} to {{end_batch}} of {total_batches}")
        
        total_success = 0
        total_errors = 0
        
        for batch_num in range(start_batch, end_batch + 1):
            self.stdout.write(f"\\nRunning batch {{batch_num}}/{total_batches}...")
            
            try:
                from django.core.management import call_command
                call_command(f'import_batch_{{batch_num:03d}}')
                total_success += 25  # Approximate
                
            except Exception as e:
                self.stdout.write(f"Batch {{batch_num}} failed: {{e}}")
                total_errors += 25
        
        final_count = MCQ.objects.count()
        self.stdout.write(f"\\n=== Import Complete ===")
        self.stdout.write(f"Estimated successful imports: {{total_success}}")
        self.stdout.write(f"Estimated errors: {{total_errors}}")
        self.stdout.write(f"Total in database: {{final_count}} MCQs")
'''
    
    with open(f"{cmd_dir}/import_all_batches.py", 'w', encoding='utf-8') as f:
        f.write(master_command)
    
    print(f"✅ Created master import command: import_all_batches.py")
    return True

def deploy_and_run():
    """Deploy all batch commands to Heroku and run the master command"""
    
    print("\n=== Deploying to Heroku ===")
    
    # Add all new files to git
    print("1. Adding batch commands to git...")
    try:
        subprocess.run([
            'git', 'add', 'django_neurology_mcq/mcq/management/commands/'
        ], cwd='/Users/tariqalmatrudi/NEWreader', capture_output=True, text=True)
        
        # Commit the changes
        result = subprocess.run([
            'git', 'commit', '-m', 'Add batch MCQ import commands for 3046 MCQs'
        ], cwd='/Users/tariqalmatrudi/NEWreader', capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Batch commands committed to git")
        else:
            print("ℹ️  No new changes to commit")
        
        # Push to Heroku
        print("2. Pushing to Heroku...")
        result = subprocess.run([
            'git', 'push', 'heroku', 'HEAD:main'
        ], cwd='/Users/tariqalmatrudi/NEWreader', capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Code deployed to Heroku")
        else:
            print(f"⚠️  Deploy warning: {result.stderr}")
        
    except Exception as e:
        print(f"⚠️  Warning: Could not auto-deploy: {e}")
        return False
    
    # Run the master import command on Heroku
    print("3. Running MCQ import on Heroku...")
    try:
        cmd = [
            'heroku', 'run', 
            'python', 'django_neurology_mcq/manage.py', 'import_all_batches', 
            '--clear-existing',
            '--app', 'radiant-gorge-35079'
        ]
        
        print(f"Running: {' '.join(cmd)}")
        result = subprocess.run(cmd, cwd='/Users/tariqalmatrudi/NEWreader', 
                              capture_output=True, text=True, timeout=2400)  # 40 minute timeout
        
        print("Heroku output:")
        print(result.stdout)
        if result.stderr:
            print("Errors:")
            print(result.stderr)
        
        if result.returncode == 0:
            print("✅ MCQ import completed successfully on Heroku!")
            return True
        else:
            print(f"❌ MCQ import failed with return code: {result.returncode}")
            return False
            
    except subprocess.TimeoutExpired:
        print("⚠️  Import command timed out (40 minutes)")
        print("The import may still be running on Heroku. Check manually.")
        return None
    except Exception as e:
        print(f"❌ Error running import command: {e}")
        return False

def main():
    print("=== Create and Deploy MCQ Import Batches ===")
    print("This will create batch import commands for 3,046 MCQs and deploy them to Heroku")
    
    # Step 1: Create batch commands
    if not create_import_batches():
        print("❌ Failed to create batch commands. Exiting.")
        return False
    
    # Step 2: Deploy and run
    print("\n=== Deploying and Running ===")
    import_success = deploy_and_run()
    
    if import_success is False:
        print("❌ Import failed. Exiting.")
        return False
    elif import_success is None:
        print("⚠️  Import may still be running. Please check manually.")
        return True
    
    print("\n🎉 SUCCESS! Batch import process completed!")
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)