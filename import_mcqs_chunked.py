#!/usr/bin/env python3
"""
Create and upload MCQ import scripts in chunks
"""

import json
import glob
import os
import subprocess
import time

def create_import_script_template():
    """Create the base import script template"""
    return '''#!/usr/bin/env python3
import os
import sys
import json
from datetime import datetime

# Add Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
sys.path.insert(0, '/app/django_neurology_mcq')

import django
django.setup()

from mcq.models import MCQ

# MCQ data
MCQ_DATA = ###DATA###

def process_explanation(mcq_data):
    """Process explanation data from either unified or subsection format"""
    explanation_sections = {}
    
    if 'unified_explanation' in mcq_data and mcq_data['unified_explanation']:
        unified_text = mcq_data['unified_explanation']
        explanation = unified_text
        
        if 'explanation' in mcq_data and isinstance(mcq_data['explanation'], dict):
            exp_dict = mcq_data['explanation']
            section_mapping = {
                'option_analysis': 'option_analysis',
                'conceptual_foundation': 'conceptual_foundation',
                'pathophysiology': 'pathophysiology',
                'clinical_manifestation': 'clinical_manifestation',
                'diagnostic_approach': 'diagnostic_approach',
                'management_principles': 'management_principles',
                'follow_up_guidelines': 'follow_up_guidelines',
                'clinical_pearls': 'clinical_pearls',
                'references': 'references'
            }
            
            for old_key, new_key in section_mapping.items():
                if old_key in exp_dict and exp_dict[old_key] and \\
                   not exp_dict[old_key].startswith("This section information is included"):
                    explanation_sections[new_key] = exp_dict[old_key]
        
    elif 'explanation' in mcq_data and isinstance(mcq_data['explanation'], dict):
        exp_dict = mcq_data['explanation']
        explanation_parts = []
        
        if exp_dict.get('option_analysis'):
            explanation_parts.append(f"**Option Analysis:**\\n{exp_dict['option_analysis']}")
        if exp_dict.get('conceptual_foundation'):
            explanation_parts.append(f"**Conceptual Foundation:**\\n{exp_dict['conceptual_foundation']}")
        if exp_dict.get('pathophysiology'):
            explanation_parts.append(f"**Pathophysiology:**\\n{exp_dict['pathophysiology']}")
        if exp_dict.get('clinical_manifestation'):
            explanation_parts.append(f"**Clinical Manifestation:**\\n{exp_dict['clinical_manifestation']}")
        if exp_dict.get('diagnostic_approach'):
            explanation_parts.append(f"**Diagnostic Approach:**\\n{exp_dict['diagnostic_approach']}")
        if exp_dict.get('management_principles'):
            explanation_parts.append(f"**Management Principles:**\\n{exp_dict['management_principles']}")
        if exp_dict.get('follow_up_guidelines'):
            explanation_parts.append(f"**Follow-up Guidelines:**\\n{exp_dict['follow_up_guidelines']}")
        
        if exp_dict.get('clinical_pearls'):
            if isinstance(exp_dict['clinical_pearls'], list):
                pearls_text = '\\n'.join(f"• {pearl}" for pearl in exp_dict['clinical_pearls'])
            else:
                pearls_text = exp_dict['clinical_pearls']
            explanation_parts.append(f"**Clinical Pearls:**\\n{pearls_text}")
            
        if exp_dict.get('references'):
            explanation_parts.append(f"**References:**\\n{exp_dict['references']}")
        
        explanation = '\\n\\n'.join(explanation_parts) if explanation_parts else ""
        
        explanation_sections = {
            'option_analysis': exp_dict.get('option_analysis', ''),
            'conceptual_foundation': exp_dict.get('conceptual_foundation', ''),
            'pathophysiology': exp_dict.get('pathophysiology', ''),
            'clinical_manifestation': exp_dict.get('clinical_manifestation', ''),
            'diagnostic_approach': exp_dict.get('diagnostic_approach', ''),
            'management_principles': exp_dict.get('management_principles', ''),
            'follow_up_guidelines': exp_dict.get('follow_up_guidelines', ''),
            'clinical_pearls': exp_dict.get('clinical_pearls', []),
            'references': exp_dict.get('references', '')
        }
    else:
        explanation = mcq_data.get('explanation', '') or ''
        
    return explanation, explanation_sections

def main():
    print(f"Importing MCQs - Chunk {MCQ_DATA.get('chunk_number', 'Unknown')}/{MCQ_DATA.get('total_chunks', 'Unknown')}")
    print(f"Specialty: {MCQ_DATA.get('specialty', 'Unknown')}")
    
    total_imported = 0
    errors = []
    
    mcqs = MCQ_DATA.get('mcqs', [])
    
    for idx, mcq_data in enumerate(mcqs):
        try:
            explanation, explanation_sections = process_explanation(mcq_data)
            
            mcq_obj = MCQ(
                question_number=mcq_data.get('question_number', ''),
                question_text=mcq_data.get('question', ''),
                options=mcq_data.get('options', {}),
                correct_answer=mcq_data.get('correct_answer', ''),
                subspecialty=mcq_data.get('subspecialty', MCQ_DATA.get('specialty', '')),
                source_file=mcq_data.get('source_file', ''),
                exam_type=mcq_data.get('exam_type', ''),
                exam_year=mcq_data.get('exam_year'),
                explanation=explanation,
                explanation_sections=explanation_sections if explanation_sections else None,
                image_url=mcq_data.get('image_url', '')
            )
            
            mcq_obj.save()
            total_imported += 1
            
            if (idx + 1) % 50 == 0:
                print(f"  Imported {idx + 1}/{len(mcqs)}...")
                
        except Exception as e:
            errors.append(f"Error in MCQ {idx}: {str(e)}")
    
    print(f"\\nChunk complete: imported {total_imported} MCQs with {len(errors)} errors")
    
    if errors:
        print("\\nFirst 5 errors:")
        for error in errors[:5]:
            print(f"  - {error}")

if __name__ == "__main__":
    main()
'''

def split_and_upload_mcqs():
    """Split MCQs into chunks and upload them"""
    
    # Read all MCQ files
    directory_path = '/Users/tariqalmatrudi/Documents/FFF/output_by_specialty'
    json_files = glob.glob(os.path.join(directory_path, '*.json'))
    
    chunks = []
    chunk_size = 100  # MCQs per chunk
    
    # Process each file
    for json_file in json_files:
        filename = os.path.basename(json_file)
        if filename == 'reorganization_summary.txt':
            continue
        
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            specialty = data.get('specialty', 'Unknown')
            mcqs = data.get('mcqs', [])
            
            # Split into chunks
            for i in range(0, len(mcqs), chunk_size):
                chunk_mcqs = mcqs[i:i + chunk_size]
                chunks.append({
                    'specialty': specialty,
                    'mcqs': chunk_mcqs,
                    'source_file': filename
                })
                
        except Exception as e:
            print(f"Error reading {filename}: {e}")
    
    print(f"Created {len(chunks)} chunks")
    
    # First, delete existing MCQs
    print("Deleting existing MCQs on Heroku...")
    delete_cmd = '''
cd django_neurology_mcq && python -c "
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
import django
django.setup()
from mcq.models import MCQ
count = MCQ.objects.count()
MCQ.objects.all().delete()
print(f'Deleted {count} MCQs')"
'''
    
    subprocess.run(['heroku', 'run', delete_cmd, '-a', 'radiant-gorge-35079'], capture_output=True)
    
    # Process each chunk
    template = create_import_script_template()
    
    for i, chunk_data in enumerate(chunks):
        print(f"\nProcessing chunk {i+1}/{len(chunks)} - {chunk_data['specialty']} ({len(chunk_data['mcqs'])} MCQs)")
        
        # Add chunk info
        chunk_data['chunk_number'] = i + 1
        chunk_data['total_chunks'] = len(chunks)
        
        # Create script with data
        script_content = template.replace('###DATA###', json.dumps(chunk_data, indent=2))
        
        # Save to file
        script_path = f'/tmp/import_chunk_{i+1}.py'
        with open(script_path, 'w') as f:
            f.write(script_content)
        
        # Upload and run on Heroku
        try:
            # Copy to Django directory
            subprocess.run(['cp', script_path, f'/Users/tariqalmatrudi/NEWreader/django_neurology_mcq/import_chunk_{i+1}.py'])
            
            # Add to git
            os.chdir('/Users/tariqalmatrudi/NEWreader/django_neurology_mcq')
            subprocess.run(['git', 'add', f'import_chunk_{i+1}.py'])
            subprocess.run(['git', 'commit', '-m', f'Add import chunk {i+1}'], capture_output=True)
            subprocess.run(['git', 'push', 'heroku', 'stable_version:main'], capture_output=True)
            
            # Run the import
            result = subprocess.run(
                ['heroku', 'run', f'python import_chunk_{i+1}.py', '-a', 'radiant-gorge-35079'],
                capture_output=True,
                text=True,
                timeout=120
            )
            
            if result.stdout:
                print(result.stdout)
            
            # Clean up
            os.remove(f'import_chunk_{i+1}.py')
            subprocess.run(['git', 'rm', f'import_chunk_{i+1}.py'], capture_output=True)
            subprocess.run(['git', 'commit', '-m', f'Remove import chunk {i+1}'], capture_output=True)
            
            # Small delay between chunks
            time.sleep(2)
            
        except Exception as e:
            print(f"Error processing chunk {i+1}: {e}")
    
    # Final verification
    print("\nVerifying final import...")
    verify_cmd = '''
cd django_neurology_mcq && python -c "
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
    print(f'  - {s}: {count}')"
'''
    
    result = subprocess.run(['heroku', 'run', verify_cmd, '-a', 'radiant-gorge-35079'], capture_output=True, text=True)
    print(result.stdout)

if __name__ == "__main__":
    split_and_upload_mcqs()