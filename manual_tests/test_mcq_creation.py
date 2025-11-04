#!/usr/bin/env python3
import json
import subprocess
import tempfile
import os

def run_heroku_command(script):
    """Execute a Python script on Heroku."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.py') as file:
        file.write(script)
        file_path = file.name
    
    try:
        cmd = f"cat {file_path} | heroku run --app mcq-reader python manage.py shell"
        process = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("STDOUT:")
        print(process.stdout)
        if process.stderr:
            print("\nSTDERR:")
            print(process.stderr)
    finally:
        if os.path.exists(file_path):
            os.unlink(file_path)

# Create a single test MCQ
test_script = """
from mcq.models import MCQ

# Create a test MCQ
try:
    mcq = MCQ(
        question_text="This is a test vascular MCQ",
        options={
            "option_a": "Option A",
            "option_b": "Option B",
            "option_c": "Option C",
            "option_d": "Option D",
            "option_e": "Option E"
        },
        correct_answer="A",
        explanation="This is a test explanation",
        subspecialty="vascular_neurology",
        exam_year="2025",
        exam_type="Test"
    )
    mcq.save()
    print("Test MCQ created successfully!")
    
    # Verify it was saved
    test_mcq = MCQ.objects.get(question_text="This is a test vascular MCQ")
    print(f"Retrieved MCQ ID: {test_mcq.id}")
    print(f"Question: {test_mcq.question_text}")
    print(f"Answer: {test_mcq.correct_answer}")
    
except Exception as e:
    print(f"Error creating MCQ: {str(e)}")
"""

print("Running test MCQ creation on Heroku...")
run_heroku_command(test_script)