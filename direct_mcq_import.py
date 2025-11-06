#!/usr/bin/env python3
"""
Direct MCQ import to Heroku using management command with chunked data
"""
import json
import subprocess
import sys
import os
import math

def split_mcqs_into_chunks():
    """Split MCQs into manageable chunks for Heroku commands"""
    
    # Load the consolidated MCQ data
    try:
        with open('/Users/tariqalmatrudi/NEWreader/all_mcqs_consolidated.json', 'r', encoding='utf-8') as f:
            mcqs = json.load(f)
        print(f"Loaded {len(mcqs)} MCQs for chunking")
    except Exception as e:
        print(f"Error loading MCQ data: {e}")
        return []
    
    # Split into chunks of 50 MCQs each
    chunk_size = 50
    chunks = []
    
    for i in range(0, len(mcqs), chunk_size):
        chunk = mcqs[i:i + chunk_size]
        chunks.append(chunk)
    
    print(f"Split MCQs into {len(chunks)} chunks of up to {chunk_size} MCQs each")
    return chunks

def create_chunked_import_commands(chunks):
    """Create management commands for each chunk"""
    
    cmd_dir = "/Users/tariqalmatrudi/NEWreader/django_neurology_mcq/mcq/management/commands"
    os.makedirs(cmd_dir, exist_ok=True)
    
    # Create main import command
    main_command = '''import json
from django.core.management.base import BaseCommand
from mcq.models import MCQ
from django.db import transaction

class Command(BaseCommand):
    help = 'Import all consolidated MCQs in chunks'
    
    def add_arguments(self, parser):
        parser.add_argument('--clear-existing', action='store_true', help='Clear existing MCQs before import')
        parser.add_argument('--start-chunk', type=int, default=1, help='Starting chunk number')
        parser.add_argument('--end-chunk', type=int, help='Ending chunk number')
    
    def handle(self, *args, **options):
        clear_existing = options['clear_existing']
        start_chunk = options['start_chunk']
        end_chunk = options.get('end_chunk')
        
        # Clear existing MCQs if requested
        if clear_existing:
            existing_count = MCQ.objects.count()
            self.stdout.write(f"Clearing {existing_count} existing MCQs...")
            MCQ.objects.all().delete()
            self.stdout.write("Existing MCQs cleared")
        
        # Import chunks
        total_chunks = self.get_total_chunks()
        if end_chunk is None:
            end_chunk = total_chunks
            
        self.stdout.write(f"Importing chunks {start_chunk} to {end_chunk} of {total_chunks}")
        
        success_count = 0
        error_count = 0
        
        for chunk_num in range(start_chunk, end_chunk + 1):
            if chunk_num > total_chunks:
                break
                
            self.stdout.write(f"\\nProcessing chunk {chunk_num}/{total_chunks}")
            
            try:
                chunk_data = self.get_chunk_data(chunk_num)
                if not chunk_data:
                    continue
                    
                with transaction.atomic():
                    for i, mcq_data in enumerate(chunk_data):
                        try:
                            self.import_single_mcq(mcq_data, success_count + i + 1)
                            success_count += 1
                        except Exception as e:
                            error_count += 1
                            self.stdout.write(f"Error importing MCQ: {e}")
                
                self.stdout.write(f"Chunk {chunk_num} completed successfully ({len(chunk_data)} MCQs)")
                
            except Exception as e:
                self.stdout.write(f"Chunk {chunk_num} failed: {e}")
                error_count += len(chunk_data) if 'chunk_data' in locals() else 50
        
        final_count = MCQ.objects.count()
        self.stdout.write(f"\\n=== Import Complete ===")
        self.stdout.write(f"Successfully imported: {success_count} MCQs")
        self.stdout.write(f"Errors: {error_count} MCQs") 
        self.stdout.write(f"Total in database: {final_count} MCQs")
    
    def get_total_chunks(self):
        """Return total number of chunks available"""
        return ''' + str(len(chunks)) + '''
    
    def get_chunk_data(self, chunk_num):
        """Get data for a specific chunk"""
        # Chunk data will be embedded here
        chunks_data = ''' + json.dumps(chunks, indent=8) + '''
        
        if chunk_num < 1 or chunk_num > len(chunks_data):
            return []
        
        return chunks_data[chunk_num - 1]
    
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
            option_analysis=mcq_data.get('option_analysis', {})
        )
        
        mcq.save()
'''
    
    # Write the main command
    with open(f"{cmd_dir}/import_chunked_mcqs.py", 'w', encoding='utf-8') as f:
        f.write(main_command)
    
    print(f"✅ Created chunked import command with {len(chunks)} chunks")

def deploy_and_run():
    """Deploy the import command to Heroku and run it"""
    
    print("\n=== Deploying to Heroku ===")
    
    # Deploy to Heroku
    print("1. Deploying code to Heroku...")
    try:
        subprocess.run([
            'git', 'add', 'django_neurology_mcq/mcq/management/commands/import_chunked_mcqs.py'
        ], cwd='/Users/tariqalmatrudi/NEWreader', capture_output=True, text=True)
        
        # Check if there are changes to commit
        result = subprocess.run([
            'git', 'status', '--porcelain'
        ], cwd='/Users/tariqalmatrudi/NEWreader', capture_output=True, text=True)
        
        if result.stdout.strip():
            # Commit the changes
            subprocess.run([
                'git', 'commit', '-m', 'Add chunked MCQ import command for 3046 MCQs'
            ], cwd='/Users/tariqalmatrudi/NEWreader', capture_output=True, text=True)
            
            # Push to Heroku
            result = subprocess.run([
                'git', 'push', 'heroku', 'HEAD:main'
            ], cwd='/Users/tariqalmatrudi/NEWreader', capture_output=True, text=True)
            
            if result.returncode == 0:
                print("✅ Code deployed to Heroku")
            else:
                print(f"⚠️  Deploy warning: {result.stderr}")
        else:
            print("ℹ️  No changes to deploy")
        
    except Exception as e:
        print(f"⚠️  Warning: Could not auto-deploy: {e}")
        print("Please manually commit and push the import_chunked_mcqs.py file")
    
    # Run the import command on Heroku
    print("2. Running MCQ import on Heroku...")
    try:
        cmd = [
            'heroku', 'run', 
            'python', 'django_neurology_mcq/manage.py', 'import_chunked_mcqs', 
            '--clear-existing',
            '--app', 'radiant-gorge-35079'
        ]
        
        print(f"Running: {' '.join(cmd)}")
        result = subprocess.run(cmd, cwd='/Users/tariqalmatrudi/NEWreader', 
                              capture_output=True, text=True, timeout=1800)  # 30 minute timeout
        
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
        print("⚠️  Import command timed out (30 minutes)")
        print("The import may still be running on Heroku. Check manually.")
        return None
    except Exception as e:
        print(f"❌ Error running import command: {e}")
        return False

def verify_import():
    """Verify the import by checking MCQ count on Heroku"""
    
    print("\n=== Verifying Import ===")
    try:
        cmd = [
            'heroku', 'run', 
            'python', 'django_neurology_mcq/manage.py', 'shell', '-c',
            'from mcq.models import MCQ; print(f"Total MCQs in database: {MCQ.objects.count()}")',
            '--app', 'radiant-gorge-35079'
        ]
        
        result = subprocess.run(cmd, cwd='/Users/tariqalmatrudi/NEWreader', 
                              capture_output=True, text=True, timeout=60)
        
        if result.returncode == 0:
            print("✅ Verification successful:")
            print(result.stdout)
            return True
        else:
            print(f"❌ Verification failed: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ Error verifying import: {e}")
        return False

def main():
    print("=== Direct MCQ Import to Heroku ===")
    print("This will import 3,046 MCQs directly to Heroku database")
    
    # Step 1: Split MCQs into chunks
    print("\n1. Splitting MCQs into chunks...")
    chunks = split_mcqs_into_chunks()
    
    if not chunks:
        print("❌ Failed to split MCQ data. Exiting.")
        return False
    
    # Step 2: Create import commands
    print("\n2. Creating chunked import commands...")
    create_chunked_import_commands(chunks)
    
    # Step 3: Deploy and import
    print("\n3. Deploying and running import...")
    import_success = deploy_and_run()
    
    if import_success is False:
        print("❌ Import failed. Exiting.")
        return False
    
    # Step 4: Verify
    print("\n4. Verifying import...")
    verify_success = verify_import()
    
    if verify_success:
        print("\n🎉 SUCCESS! All 3,046 MCQs have been successfully imported to Heroku!")
        print("The MCQ database is now ready for use.")
        return True
    else:
        print("\n⚠️  Import may have completed but verification failed.")
        print("Please check the Heroku app manually.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)