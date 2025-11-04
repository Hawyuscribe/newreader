#!/usr/bin/env python3
"""
Improved script to import vascular/stroke MCQs to Heroku with better error handling
and direct database interaction.
"""
import os
import json
import subprocess
import requests
import tempfile
import logging
from pathlib import Path
from datetime import datetime

# Set up logging
log_filename = f"vascular_import_fixed_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Log to both file and console
console = logging.StreamHandler()
console.setLevel(logging.INFO)
logging.getLogger('').addHandler(console)

logging.info("Starting improved vascular/stroke MCQ import script")

# Source file containing vascular MCQs
VASCULAR_FILE = '/Users/tariqalmatrudi/Documents/MCQs for the board/test/json f/vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json'
logging.info(f"Processing vascular MCQs from: {VASCULAR_FILE}")

# Heroku app name
APP_NAME = "radiant-gorge-35079"

# Create a directory for processed chunks
chunks_dir = Path("vascular_chunks_fixed")
chunks_dir.mkdir(exist_ok=True)

try:
    # Read and parse the vascular MCQs file
    with open(VASCULAR_FILE, 'r') as f:
        data = json.load(f)
    
    # Process metadata
    if 'metadata' in data:
        logging.info(f"File metadata: {data['metadata']}")
    
    # Extract the MCQs
    if 'mcqs' in data and isinstance(data['mcqs'], list):
        mcqs = data['mcqs']
        logging.info(f"Found {len(mcqs)} vascular MCQs in file")
    else:
        raise ValueError("No MCQs found in the file")
    
    # Prepare MCQs for import
    formatted_mcqs = []
    for idx, mcq in enumerate(mcqs):
        # Get explanation fields
        explanation_parts = []
        for field in ['Conceptual Foundation', 'Pathophysiology', 'Clinical Correlation', 
                      'Diagnostic Approach', 'Management Principles', 'Option Analysis',
                      'Clinical Pearls', 'Current Evidence']:
            if field in mcq and mcq[field]:
                explanation_parts.append(f"**{field}**\n\n{mcq[field]}")
        
        explanation_text = "\n\n".join(explanation_parts) if explanation_parts else ""
        
        # Format the MCQ object
        formatted_mcq = {
            'id': idx + 1,  # Add an ID for better tracking
            'question': mcq.get('Question Text', ''),
            'option_a': mcq.get('Option A', ''),
            'option_b': mcq.get('Option B', ''),
            'option_c': mcq.get('Option C', ''),
            'option_d': mcq.get('Option D', ''),
            'option_e': mcq.get('Option E', ''),
            'correct_answer': mcq.get('Correct Answer', ''),
            'subspecialty': mcq.get('Subspecialty', 'vascular_neurology'),
            'explanation': explanation_text,
            'exam_year': mcq.get('Exam Year', ''),
            'exam_type': mcq.get('Exam Type', '')
        }
        
        # Add image URL if present
        if mcq.get('Has Image') == 'Yes' and mcq.get('Image URL'):
            formatted_mcq['image_url'] = mcq.get('Image URL')
        
        formatted_mcqs.append(formatted_mcq)
    
    logging.info(f"Prepared {len(formatted_mcqs)} formatted MCQs")
    
    # Split into smaller chunks - go even smaller for better reliability
    chunk_size = 10
    total_chunks = (len(formatted_mcqs) + chunk_size - 1) // chunk_size
    
    chunk_files = []
    for chunk_idx in range(total_chunks):
        start_idx = chunk_idx * chunk_size
        end_idx = min(start_idx + chunk_size, len(formatted_mcqs))
        
        chunk_mcqs = formatted_mcqs[start_idx:end_idx]
        chunk_filename = chunks_dir / f"vascular_mcqs_chunk_{chunk_idx + 1}_of_{total_chunks}.json"
        
        with open(chunk_filename, 'w') as f:
            json.dump(chunk_mcqs, f, indent=2)
        
        chunk_files.append(chunk_filename)
    
    logging.info(f"Created {len(chunk_files)} chunks")
    
    # Clear existing vascular MCQs on Heroku
    logging.info("Clearing existing vascular MCQs...")
    clear_script = """
from mcq.models import MCQ
from django.db.models import Q

vascular_count = MCQ.objects.filter(
    Q(subspecialty__icontains='vascular') | 
    Q(subspecialty__icontains='stroke')
).count()

print(f"Found {vascular_count} vascular MCQs to delete")

if vascular_count > 0:
    MCQ.objects.filter(
        Q(subspecialty__icontains='vascular') | 
        Q(subspecialty__icontains='stroke')
    ).delete()
    print(f"Deleted {vascular_count} vascular MCQs")
"""
    
    # Create a file for the script
    with open("clear_script.py", "w") as f:
        f.write(clear_script)
    
    # Upload and run the clear script
    clear_cmd = f"""heroku run --app {APP_NAME} "cd /app/django_neurology_mcq && python manage.py shell" < clear_script.py"""
    subprocess.run(clear_cmd, shell=True)
    
    # Process each chunk and upload to Heroku
    for chunk_idx, chunk_file in enumerate(chunk_files):
        chunk_num = chunk_idx + 1
        
        logging.info(f"Processing chunk {chunk_num}/{total_chunks}")
        
        # Create a custom script to import this chunk
        import_script = f"""
import json
import sys
from django.db import transaction
from mcq.models import MCQ

# Load MCQ data
try:
    with open(sys.stdin.buffer, 'rb') as f:
        mcqs_data = json.load(f)
    
    print(f"Loaded {{len(mcqs_data)}} MCQs")
    
    # Import MCQs
    success_count = 0
    error_count = 0
    
    with transaction.atomic():
        for mcq_data in mcqs_data:
            try:
                # Create MCQ
                mcq = MCQ(
                    question=mcq_data['question'],
                    option_a=mcq_data['option_a'],
                    option_b=mcq_data['option_b'],
                    option_c=mcq_data['option_c'],
                    option_d=mcq_data['option_d'],
                    option_e=mcq_data['option_e'],
                    correct_answer=mcq_data['correct_answer'],
                    subspecialty=mcq_data['subspecialty'],
                    explanation=mcq_data['explanation'],
                    exam_year=mcq_data['exam_year'],
                    exam_type=mcq_data['exam_type']
                )
                
                # Add image URL if present
                if 'image_url' in mcq_data:
                    mcq.image_url = mcq_data['image_url']
                
                # Save to database
                mcq.save()
                success_count += 1
            except Exception as e:
                print(f"Error importing MCQ: {{str(e)}}")
                error_count += 1
    
    print(f"Successfully imported {{success_count}} MCQs")
    if error_count > 0:
        print(f"Failed to import {{error_count}} MCQs")
    
    # Verify the import
    db_count = MCQ.objects.filter(
        subspecialty__icontains='vascular'
    ).count()
    
    print(f"Total vascular MCQs in database: {{db_count}}")
except Exception as e:
    print(f"Import error: {{str(e)}}")
"""
        
        # Create a file for the import script
        with open("import_script.py", "w") as f:
            f.write(import_script)
        
        # Upload and run the import script
        import_cmd = f"""cat {chunk_file} | heroku run --app {APP_NAME} "cd /app/django_neurology_mcq && python manage.py shell" < import_script.py"""
        result = subprocess.run(import_cmd, shell=True, capture_output=True, text=True)
        
        logging.info(f"Import result: {result.stdout}")
        if result.stderr:
            logging.error(f"Import error: {result.stderr}")
    
    # Verify the import
    logging.info("Verifying import...")
    verify_script = """
from mcq.models import MCQ
from django.db.models import Q

vascular_count = MCQ.objects.filter(
    Q(subspecialty__icontains='vascular') | 
    Q(subspecialty__icontains='stroke')
).count()

print(f"Found {vascular_count} vascular MCQs in the database")

mcq_sample = list(MCQ.objects.filter(
    Q(subspecialty__icontains='vascular') | 
    Q(subspecialty__icontains='stroke')
)[:5])

print("Sample MCQs:")
for mcq in mcq_sample:
    print(f"ID: {mcq.id}, Question: {mcq.question[:50]}..., Answer: {mcq.correct_answer}")
"""
    
    # Create a file for the verification script
    with open("verify_script.py", "w") as f:
        f.write(verify_script)
    
    # Run the verification script
    verify_cmd = f"""heroku run --app {APP_NAME} "cd /app/django_neurology_mcq && python manage.py shell" < verify_script.py"""
    result = subprocess.run(verify_cmd, shell=True, capture_output=True, text=True)
    
    logging.info(f"Verification result: {result.stdout}")
    if result.stderr:
        logging.error(f"Verification error: {result.stderr}")
    
    # Check if we have MCQs in the database
    if "Found 0 vascular MCQs in the database" in result.stdout:
        logging.error("Import failed! No vascular MCQs found in the database")
        
        # Debug database connection
        debug_script = """
from django.conf import settings
import os

# Print database settings
print("Database settings:")
print(settings.DATABASES)

# Print environment variables
print("\\nEnvironment variables:")
db_url = os.environ.get('DATABASE_URL')
if db_url:
    print(f"DATABASE_URL: {db_url[:20]}...")
else:
    print("DATABASE_URL not found")

# Try a simple database operation
from django.db import connection
cursor = connection.cursor()
cursor.execute("SELECT 1")
print("\\nDatabase connection test:", cursor.fetchone())
"""
        
        # Create a file for the debug script
        with open("debug_script.py", "w") as f:
            f.write(debug_script)
        
        # Run the debug script
        debug_cmd = f"""heroku run --app {APP_NAME} "cd /app/django_neurology_mcq && python manage.py shell" < debug_script.py"""
        debug_result = subprocess.run(debug_cmd, shell=True, capture_output=True, text=True)
        
        logging.info(f"Database debug result: {debug_result.stdout}")
    else:
        logging.info("Import completed successfully!")
    
    # Try to restart the app to refresh connections
    logging.info("Restarting the app...")
    restart_cmd = f"heroku restart --app {APP_NAME}"
    subprocess.run(restart_cmd, shell=True)
    
except Exception as e:
    logging.error(f"Script error: {str(e)}")
    raise

logging.info("Script completed")