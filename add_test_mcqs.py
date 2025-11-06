#!/usr/bin/env python3
"""
Script to add test MCQs with proper field names.
"""
import subprocess
import logging
from pathlib import Path
from datetime import datetime

# Set up logging
log_filename = f"add_test_mcqs_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
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

# Heroku app name
APP_NAME = "radiant-gorge-35079"

logging.info("Starting test MCQ addition script")

# Create a simple script to add test MCQs
test_mcq_script = """
from mcq.models import MCQ
from django.db.models import Q

# Check existing MCQs
total_mcqs = MCQ.objects.count()
print(f"Current MCQ count: {total_mcqs}")

# Get the field names from the MCQ model
field_names = [field.name for field in MCQ._meta.fields]
print(f"Available fields: {field_names}")

# Add 10 test vascular MCQs
for i in range(1, 11):
    try:
        # Create the MCQ with proper field names
        mcq = MCQ(
            question_text=f"Test Vascular MCQ #{i}",
            options={{"option_a": f"Option A for question {i}", 
                    "option_b": f"Option B for question {i}",
                    "option_c": f"Option C for question {i}", 
                    "option_d": f"Option D for question {i}",
                    "option_e": f"Option E for question {i}"}},
            correct_answer="A",
            subspecialty="vascular_neurology",
            explanation=f"This is a test explanation for question {i}",
            exam_year="2025",
            exam_type="Test"
        )
        mcq.save()
        print(f"Created test MCQ with ID: {mcq.id}")
    except Exception as e:
        print(f"Error creating MCQ #{i}: {str(e)}")

# Verify the MCQs were added
vascular_count = MCQ.objects.filter(
    Q(subspecialty__icontains='vascular') | 
    Q(subspecialty__icontains='stroke')
).count()
print(f"Vascular MCQ count after adding test MCQs: {vascular_count}")
"""

# Create a file for the script
with open("test_mcq_script.py", "w") as f:
    f.write(test_mcq_script)

# Upload and run the script on Heroku
logging.info("Running script on Heroku")
cmd = f"""heroku run:detached --app {APP_NAME} "cd /app/django_neurology_mcq && python manage.py shell < /dev/stdin" < test_mcq_script.py"""
subprocess.run(cmd, shell=True)

logging.info("Script started in the background")

# Restart the app to refresh the dashboard
logging.info("Restarting the Heroku app")
restart_cmd = f"heroku restart --app {APP_NAME}"
subprocess.run(restart_cmd, shell=True)

logging.info("Script execution completed")