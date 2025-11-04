#!/usr/bin/env python3
"""
Direct import approach using Heroku console
"""
import json
import glob
import os
import subprocess

def create_consolidated_data():
    """Create consolidated MCQ data file"""
    print("Creating consolidated MCQ data...")
    
    directory_path = '/Users/tariqalmatrudi/Documents/FFF/output_by_specialty'
    json_files = glob.glob(os.path.join(directory_path, '*.json'))
    
    all_mcqs = []
    
    for json_file in json_files:
        filename = os.path.basename(json_file)
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            if 'mcqs' in data:
                specialty = data.get('specialty', 'Unknown')
                for mcq in data['mcqs']:
                    mcq['import_specialty'] = specialty
                    mcq['import_source'] = filename
                    all_mcqs.append(mcq)
        except Exception as e:
            print(f"Error reading {filename}: {e}")
    
    print(f"Total MCQs to import: {len(all_mcqs)}")
    
    # Split into smaller chunks
    chunk_size = 500
    chunks = []
    
    for i in range(0, len(all_mcqs), chunk_size):
        chunk = all_mcqs[i:i + chunk_size]
        chunks.append(chunk)
    
    print(f"Created {len(chunks)} chunks")
    
    # Save chunks
    for i, chunk in enumerate(chunks):
        with open(f'/tmp/mcq_chunk_{i}.json', 'w') as f:
            json.dump(chunk, f)
    
    return len(chunks)

def run_import():
    """Run the import process"""
    
    # Create consolidated data
    num_chunks = create_consolidated_data()
    
    # First delete existing MCQs
    print("\nDeleting existing MCQs...")
    delete_cmd = '''
heroku run bash -a radiant-gorge-35079 <<'EOF'
cd django_neurology_mcq
python -c "
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
import django
django.setup()
from mcq.models import MCQ
count = MCQ.objects.count()
MCQ.objects.all().delete()
print(f'Deleted {count} MCQs')
"
EOF
'''
    subprocess.run(delete_cmd, shell=True)
    
    # Import each chunk
    for i in range(num_chunks):
        print(f"\nImporting chunk {i+1}/{num_chunks}...")
        
        # Read chunk data
        with open(f'/tmp/mcq_chunk_{i}.json', 'r') as f:
            chunk_data = json.load(f)
        
        # Create import script for this chunk
        import_script = f'''
import os
import sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
sys.path.insert(0, '/app/django_neurology_mcq')
import django
django.setup()
from mcq.models import MCQ

chunk_data = {json.dumps(chunk_data)}

imported = 0
for mcq_data in chunk_data:
    try:
        # Process explanation
        explanation = ""
        explanation_sections = {{}}
        
        if 'unified_explanation' in mcq_data and mcq_data['unified_explanation']:
            explanation = mcq_data['unified_explanation']
        elif 'explanation' in mcq_data:
            if isinstance(mcq_data['explanation'], dict):
                exp_dict = mcq_data['explanation']
                parts = []
                
                for key, value in exp_dict.items():
                    if value and not value.startswith("This section information"):
                        parts.append(f"**{{key.replace('_', ' ').title()}}:**\\n{{value}}")
                
                explanation = '\\n\\n'.join(parts)
                explanation_sections = exp_dict
            else:
                explanation = mcq_data.get('explanation', '')
        
        mcq_obj = MCQ(
            question_number=mcq_data.get('question_number', ''),
            question_text=mcq_data.get('question', ''),
            options=mcq_data.get('options', {{}}),
            correct_answer=mcq_data.get('correct_answer', ''),
            subspecialty=mcq_data.get('subspecialty', mcq_data.get('import_specialty', '')),
            source_file=mcq_data.get('source_file', mcq_data.get('import_source', '')),
            exam_type=mcq_data.get('exam_type', ''),
            exam_year=mcq_data.get('exam_year'),
            explanation=explanation,
            explanation_sections=explanation_sections if explanation_sections else None,
            image_url=mcq_data.get('image_url', '')
        )
        
        mcq_obj.save()
        imported += 1
        
    except Exception as e:
        pass

print(f"Chunk {i+1}: Imported {{imported}} MCQs")
'''
        
        # Save script
        script_path = f'/tmp/import_chunk_{i}.py'
        with open(script_path, 'w') as f:
            f.write(import_script)
        
        # Copy to project and run on Heroku
        subprocess.run(f'cp {script_path} /Users/tariqalmatrudi/NEWreader/django_neurology_mcq/', shell=True)
        
        os.chdir('/Users/tariqalmatrudi/NEWreader/django_neurology_mcq')
        subprocess.run(f'git add import_chunk_{i}.py', shell=True)
        subprocess.run(f'git commit -m "Add chunk {i}"', shell=True, capture_output=True)
        subprocess.run('git push heroku stable_version:main', shell=True, capture_output=True)
        
        # Run the chunk
        subprocess.run(f'heroku run python import_chunk_{i}.py -a radiant-gorge-35079', shell=True, timeout=60)
        
        # Clean up
        subprocess.run(f'rm import_chunk_{i}.py', shell=True)
        subprocess.run(f'git rm import_chunk_{i}.py', shell=True, capture_output=True)
        subprocess.run(f'git commit -m "Remove chunk {i}"', shell=True, capture_output=True)
    
    # Final verification
    print("\nVerifying import...")
    verify_cmd = '''
heroku run bash -a radiant-gorge-35079 <<'EOF'
cd django_neurology_mcq
python -c "
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
import django
django.setup()
from mcq.models import MCQ
print(f'Total MCQs: {MCQ.objects.count()}')
subspecialties = MCQ.objects.values_list('subspecialty', flat=True).distinct()
print(f'Subspecialties: {len(subspecialties)}')
for s in sorted(subspecialties):
    count = MCQ.objects.filter(subspecialty=s).count()
    print(f'  - {s}: {count}')
"
EOF
'''
    subprocess.run(verify_cmd, shell=True)

if __name__ == "__main__":
    run_import()