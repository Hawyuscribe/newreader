"""
Script to upload MCQs via Heroku Django shell
"""

import json
import sys
import os
import tempfile
import subprocess

def create_upload_script(mcqs):
    """Creates a Django shell script for uploading MCQs"""
    script = """
import json
from django.db import transaction
from mcq.models import MCQ

# MCQs data as JSON string - will be replaced
mcqs_data = json.loads('''
{0}
''')

print(f"Processing {{len(mcqs_data)}} MCQs")

# Track imports
created = 0
updated = 0
skipped = 0"""
    
    return script.format(json.dumps(mcqs))

# Process each MCQ
with transaction.atomic():
    for mcq_data in mcqs_data:
        question = mcq_data.get('question_text', '')
        if not question:
            print("Skipping MCQ with no question text")
            skipped += 1
            continue
        
        # Check if MCQ already exists
        existing = MCQ.objects.filter(question_text=question).first()
        
        if existing:
            # Only update if subspecialty is not already vascular_neurology
            if existing.subspecialty != 'vascular_neurology' and mcq_data.get('subspecialty') == 'vascular_neurology':
                existing.subspecialty = 'vascular_neurology'
                existing.options = mcq_data.get('options', {})
                existing.correct_answer = mcq_data.get('correct_answer', '')
                existing.explanation = mcq_data.get('explanation', '')
                existing.exam_year = mcq_data.get('exam_year', '')
                existing.exam_type = mcq_data.get('exam_type', '')
                existing.save()
                updated += 1
                print(f"Updated: {question[:30]}...")
            else:
                skipped += 1
                print(f"Skipped (already exists): {question[:30]}...")
        else:
            # Create new MCQ
            try:
                new_mcq = MCQ(
                    question_text=question,
                    options=mcq_data.get('options', {}),
                    correct_answer=mcq_data.get('correct_answer', ''),
                    explanation=mcq_data.get('explanation', ''),
                    subspecialty=mcq_data.get('subspecialty', 'vascular_neurology'),
                    exam_year=mcq_data.get('exam_year', ''),
                    exam_type=mcq_data.get('exam_type', '')
                )
                new_mcq.save()
                created += 1
                print(f"Created: {question[:30]}...")
            except Exception as e:
                print(f"Error creating MCQ: {str(e)}")
                skipped += 1

print(f"Results: Created {created}, Updated {updated}, Skipped {skipped}")

# Count vascular MCQs
vascular_count = MCQ.objects.filter(subspecialty="vascular_neurology").count()
print(f"Total vascular MCQs: {vascular_count}")
""".format(mcqs_json=json.dumps(mcqs))

def upload_mcqs(mcqs, app_name="radiant-gorge-35079"):
    """Uploads MCQs to Heroku via Django shell"""
    # Create a temporary script file
    temp_dir = tempfile.mkdtemp()
    script_file = os.path.join(temp_dir, "upload_mcqs.py")
    
    # Write the upload script
    with open(script_file, 'w') as f:
        f.write(create_upload_script(mcqs))
    
    try:
        # Upload the script to Heroku
        print("Uploading script to Heroku...")
        with open(script_file, 'r') as f:
            upload_cmd = ["heroku", "run", "cat > /tmp/upload_mcqs.py", "--app", app_name]
            result = subprocess.run(upload_cmd, stdin=f, capture_output=True, text=True)
        
        if result.returncode != 0:
            print(f"Error uploading script: {result.stderr}")
            return False
        
        # Run the script
        print("Running upload script on Heroku...")
        run_cmd = ["heroku", "run", "cd django_neurology_mcq && python -c 'exec(open(\"/tmp/upload_mcqs.py\").read())'", "--app", app_name]
        result = subprocess.run(run_cmd, capture_output=True, text=True)
        
        # Print output
        if result.stdout:
            print("Output:")
            for line in result.stdout.splitlines():
                print(f"  {line}")
        
        if result.stderr:
            print("Errors:")
            for line in result.stderr.splitlines():
                print(f"  {line}")
        
        return result.returncode == 0
        
    finally:
        # Clean up
        if os.path.exists(script_file):
            os.unlink(script_file)
        os.rmdir(temp_dir)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python upload_script.py <json_file>")
        sys.exit(1)
    
    # Read MCQs from file
    json_file = sys.argv[1]
    with open(json_file, 'r') as f:
        mcqs = json.load(f)
    
    print(f"Uploading {len(mcqs)} MCQs from {json_file}...")
    success = upload_mcqs(mcqs)
    
    if success:
        print("Upload completed successfully!")
    else:
        print("Upload failed")