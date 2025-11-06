#!/usr/bin/env python3
"""
Test importing a single MCQ to Heroku.
"""
import subprocess

# Heroku app name
APP_NAME = "radiant-gorge-35079"

# Create a direct import command with quotes properly escaped
cmd = '''heroku run --app {} "cd /app/django_neurology_mcq && python manage.py shell -c 'from mcq.models import MCQ; test_mcq = MCQ(question=\"Test Vascular MCQ\", option_a=\"Option A\", option_b=\"Option B\", option_c=\"Option C\", option_d=\"Option D\", option_e=\"Option E\", correct_answer=\"A\", subspecialty=\"vascular_neurology\", explanation=\"This is a test MCQ\", exam_year=\"2023\", exam_type=\"Test\"); test_mcq.save(); print(\"MCQ created with ID:\", test_mcq.id); print(\"Total MCQs:\", MCQ.objects.count())'"'''.format(APP_NAME)

# Run on Heroku
print("Creating test MCQ on Heroku...")
result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

print("STDOUT:", result.stdout)
print("STDERR:", result.stderr)