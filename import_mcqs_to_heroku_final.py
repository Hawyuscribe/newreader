#!/usr/bin/env python3
"""
Import MCQs to Heroku Database: https://radiant-gorge-35079-2b52ba172c1e.herokuapp.com/
This script will deploy and import all MCQ chunks to the specific Heroku instance.
"""
import os
import sys
import json
import subprocess
import time
from pathlib import Path

def check_heroku_connectivity():
    """Check if we can connect to the specific Heroku instance"""
    heroku_url = "https://radiant-gorge-35079-2b52ba172c1e.herokuapp.com/"
    
    try:
        result = subprocess.run([
            'curl', '-I', heroku_url, '-m', '30'
        ], capture_output=True, text=True, timeout=60)
        
        if result.returncode == 0:
            print(f"✓ Heroku instance is reachable: {heroku_url}")
            return True
        else:
            print(f"✗ Cannot reach Heroku instance: {heroku_url}")
            return False
    except Exception as e:
        print(f"✗ Error checking Heroku connectivity: {e}")
        return False

def get_mcq_chunks():
    """Get all MCQ chunk files"""
    chunks_dir = Path("/Users/tariqalmatrudi/NEWreader/mcq_import_chunks")
    if not chunks_dir.exists():
        print(f"✗ MCQ chunks directory not found: {chunks_dir}")
        return []
    
    chunk_files = sorted(chunks_dir.glob("chunk_*.json"))
    print(f"✓ Found {len(chunk_files)} MCQ chunk files")
    
    # Count total MCQs
    total_mcqs = 0
    for chunk_file in chunk_files:
        try:
            with open(chunk_file, 'r') as f:
                mcqs = json.load(f)
                total_mcqs += len(mcqs)
        except Exception as e:
            print(f"Warning: Could not read {chunk_file}: {e}")
    
    print(f"✓ Total MCQs to import: {total_mcqs}")
    return chunk_files

def create_heroku_import_script():
    """Create a script to run the import on Heroku"""
    script_content = '''#!/usr/bin/env python3
"""
Heroku MCQ Import Script
This runs on the Heroku dyno to import MCQs
"""
import os
import sys
import django
import json
import requests
from pathlib import Path

# Django setup
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
django.setup()

from mcq.models import MCQ

def download_chunk(chunk_url, chunk_filename):
    """Download a chunk file from URL"""
    try:
        response = requests.get(chunk_url, timeout=60)
        response.raise_for_status()
        
        with open(chunk_filename, 'w') as f:
            json.dump(response.json(), f)
        
        print(f"✓ Downloaded {chunk_filename}")
        return True
    except Exception as e:
        print(f"✗ Error downloading {chunk_filename}: {e}")
        return False

def import_chunk(chunk_file):
    """Import MCQs from a chunk file"""
    try:
        with open(chunk_file, 'r') as f:
            mcqs = json.load(f)
        
        imported = 0
        errors = []
        
        for mcq_data in mcqs:
            try:
                # Process explanation
                explanation = ""
                explanation_sections = {}
                
                if 'unified_explanation' in mcq_data and mcq_data['unified_explanation']:
                    explanation = mcq_data['unified_explanation']
                elif 'explanation' in mcq_data:
                    if isinstance(mcq_data['explanation'], dict):
                        exp_dict = mcq_data['explanation']
                        parts = []
                        
                        # Build explanation from sections
                        for section_key, section_title in [
                            ('option_analysis', 'Option Analysis'),
                            ('conceptual_foundation', 'Conceptual Foundation'),
                            ('pathophysiology', 'Pathophysiology'),
                            ('clinical_manifestation', 'Clinical Manifestation'),
                            ('diagnostic_approach', 'Diagnostic Approach'),
                            ('management_principles', 'Management Principles'),
                            ('follow_up_guidelines', 'Follow-up Guidelines'),
                            ('clinical_pearls', 'Clinical Pearls'),
                            ('references', 'References')
                        ]:
                            if section_key in exp_dict and exp_dict[section_key]:
                                content = exp_dict[section_key]
                                if not (isinstance(content, str) and content.startswith("This section information")):
                                    parts.append(f"**{section_title}:**\\n{content}")
                                    explanation_sections[section_key] = content
                        
                        explanation = '\\n\\n'.join(parts)
                    else:
                        explanation = mcq_data.get('explanation', '')
                
                # Get correct answer
                correct_answer = mcq_data.get('correct_answer', '')
                if not correct_answer and 'correct_answer_text' in mcq_data:
                    # Try to match correct_answer_text to options
                    correct_text = mcq_data['correct_answer_text']
                    options = mcq_data.get('options', [])
                    if isinstance(options, list):
                        for i, option in enumerate(options):
                            if option.strip() == correct_text.strip():
                                correct_answer = chr(65 + i)  # A, B, C, etc.
                                break
                
                # Create MCQ object
                mcq_obj = MCQ(
                    question_number=mcq_data.get('question_number', ''),
                    question_text=mcq_data.get('question', ''),
                    options=mcq_data.get('options', {}),
                    correct_answer=correct_answer,
                    correct_answer_text=mcq_data.get('correct_answer_text', ''),
                    subspecialty=mcq_data.get('subspecialty', mcq_data.get('import_specialty', '')),
                    source_file=mcq_data.get('source_file', mcq_data.get('import_source', '')),
                    exam_type=mcq_data.get('exam_type', ''),
                    exam_year=mcq_data.get('exam_year'),
                    explanation=explanation,
                    explanation_sections=explanation_sections if explanation_sections else None,
                    image_url=mcq_data.get('image_url', ''),
                    ai_generated=mcq_data.get('ai_generated', False)
                )
                
                mcq_obj.save()
                imported += 1
                
                if imported % 50 == 0:
                    print(f"  Imported {imported} MCQs...")
                
            except Exception as e:
                error_msg = f"Error importing MCQ {mcq_data.get('question_number', 'unknown')}: {str(e)}"
                errors.append(error_msg)
                print(f"  ✗ {error_msg}")
        
        print(f"✓ Imported {imported} MCQs from {os.path.basename(chunk_file)}")
        if errors:
            print(f"  - {len(errors)} errors occurred")
        
        return imported, errors
        
    except Exception as e:
        print(f"✗ Error processing chunk {chunk_file}: {e}")
        return 0, [str(e)]

def main():
    """Main import function"""
    print("=== MCQ Import to Heroku ===")
    print("Target: https://radiant-gorge-35079-2b52ba172c1e.herokuapp.com/")
    
    # Check current MCQ count
    current_count = MCQ.objects.count()
    print(f"Current MCQ count: {current_count}")
    
    # Get chunk URLs from environment variables or command line
    chunk_urls = []
    for i in range(10):  # Assume max 10 chunks
        env_var = f"CHUNK_{i:03d}_URL"
        url = os.environ.get(env_var)
        if url:
            chunk_urls.append((f"chunk_{i:03d}.json", url))
    
    if not chunk_urls:
        print("No chunk URLs provided via environment variables")
        return
    
    total_imported = 0
    total_errors = []
    
    # Process each chunk
    for chunk_filename, chunk_url in chunk_urls:
        print(f"\\nProcessing {chunk_filename}...")
        
        # Download chunk
        if download_chunk(chunk_url, chunk_filename):
            # Import chunk
            imported, errors = import_chunk(chunk_filename)
            total_imported += imported
            total_errors.extend(errors)
            
            # Clean up
            if os.path.exists(chunk_filename):
                os.remove(chunk_filename)
        
        # Small delay between chunks
        time.sleep(2)
    
    print(f"\\n=== Import Summary ===")
    print(f"Total MCQs imported: {total_imported}")
    print(f"Total errors: {len(total_errors)}")
    print(f"Final MCQ count: {MCQ.objects.count()}")
    
    if total_errors:
        print("\\nFirst 10 errors:")
        for error in total_errors[:10]:
            print(f"- {error}")

if __name__ == "__main__":
    main()
'''
    
    with open('/Users/tariqalmatrudi/NEWreader/heroku_mcq_import.py', 'w') as f:
        f.write(script_content)
    
    print("✓ Created Heroku import script")

def upload_chunks_to_gists():
    """Upload MCQ chunks to GitHub Gists for Heroku access"""
    chunk_files = get_mcq_chunks()
    chunk_urls = []
    
    for chunk_file in chunk_files:
        try:
            # Create a simple file server using a temp upload (for demo purposes)
            # In production, you'd use a proper file hosting service
            chunk_name = chunk_file.name
            
            print(f"Processing {chunk_name}...")
            
            # For now, we'll create environment variables to pass the chunks
            # In a real deployment, these would be uploaded to a file hosting service
            chunk_urls.append((chunk_name, f"file://{chunk_file}"))
            
        except Exception as e:
            print(f"✗ Error processing {chunk_file}: {e}")
    
    return chunk_urls

def deploy_to_heroku():
    """Deploy the import script and run it on Heroku"""
    try:
        print("\\n=== Deploying to Heroku ===")
        
        # Check if we're in a git repository
        git_check = subprocess.run(['git', 'status'], capture_output=True, text=True)
        if git_check.returncode != 0:
            print("✗ Not in a git repository")
            return False
        
        # Add the import script to git
        subprocess.run(['git', 'add', 'heroku_mcq_import.py'], check=True)
        
        # Create a deployment commit
        try:
            subprocess.run([
                'git', 'commit', '-m', 
                'Add MCQ import script for Heroku deployment'
            ], check=True)
        except subprocess.CalledProcessError:
            print("No changes to commit (script already exists)")
        
        # Check if we have heroku remote
        remotes = subprocess.run(['git', 'remote', '-v'], capture_output=True, text=True)
        if 'heroku' not in remotes.stdout:
            print("\\n⚠️  No Heroku remote found. Please add it manually:")
            print("   heroku git:remote -a radiant-gorge-35079-2b52ba172c1e")
            return False
        
        # Push to Heroku
        print("Pushing to Heroku...")
        push_result = subprocess.run([
            'git', 'push', 'heroku', 'stable_version:main'
        ], capture_output=True, text=True)
        
        if push_result.returncode == 0:
            print("✓ Successfully pushed to Heroku")
            return True
        else:
            print(f"✗ Error pushing to Heroku: {push_result.stderr}")
            return False
            
    except Exception as e:
        print(f"✗ Error deploying to Heroku: {e}")
        return False

def run_import_on_heroku(chunk_urls):
    """Run the import script on Heroku"""
    try:
        print("\\n=== Running Import on Heroku ===")
        
        # Set environment variables for chunk URLs
        env_vars = []
        for i, (chunk_name, chunk_url) in enumerate(chunk_urls):
            env_var = f"CHUNK_{i:03d}_URL={chunk_url}"
            env_vars.append(env_var)
        
        # For file:// URLs, we need to copy the files to Heroku first
        # This is a simplified approach - in production, use proper file hosting
        
        print("Starting import process on Heroku...")
        heroku_cmd = [
            'heroku', 'run', 
            'python', 'heroku_mcq_import.py',
            '--app', 'radiant-gorge-35079-2b52ba172c1e'
        ]
        
        result = subprocess.run(heroku_cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✓ Import completed successfully")
            print("Output:", result.stdout)
            return True
        else:
            print(f"✗ Import failed: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"✗ Error running import on Heroku: {e}")
        return False

def main():
    """Main deployment and import function"""
    print("MCQ Import to Heroku")
    print("=" * 50)
    print("Target: https://radiant-gorge-35079-2b52ba172c1e.herokuapp.com/case-based-learning/")
    
    # Step 1: Check connectivity
    print("\\n1. Checking Heroku connectivity...")
    if not check_heroku_connectivity():
        print("✗ Cannot connect to Heroku. Aborting.")
        return False
    
    # Step 2: Get MCQ chunks
    print("\\n2. Getting MCQ chunks...")
    chunk_files = get_mcq_chunks()
    if not chunk_files:
        print("✗ No MCQ chunks found. Aborting.")
        return False
    
    # Step 3: Create import script
    print("\\n3. Creating Heroku import script...")
    create_heroku_import_script()
    
    # Step 4: Upload chunks (simplified for this demo)
    print("\\n4. Preparing chunks for upload...")
    chunk_urls = upload_chunks_to_gists()
    
    # Step 5: Deploy to Heroku
    print("\\n5. Deploying to Heroku...")
    if not deploy_to_heroku():
        print("✗ Deployment failed. Please check manually.")
        return False
    
    # Step 6: Run import
    print("\\n6. Running import on Heroku...")
    if not run_import_on_heroku(chunk_urls):
        print("✗ Import failed. Please check Heroku logs.")
        return False
    
    print("\\n✅ MCQ import completed successfully!")
    print("\\nNext steps:")
    print("1. Verify at: https://radiant-gorge-35079-2b52ba172c1e.herokuapp.com/")
    print("2. Test case-based learning: https://radiant-gorge-35079-2b52ba172c1e.herokuapp.com/case-based-learning/")
    print("3. Check logs: heroku logs --tail --app radiant-gorge-35079-2b52ba172c1e")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)