#!/bin/bash

# Run migrations and import script on Heroku
echo "Running migrations..."
python manage.py migrate

echo "Running MCQ import..."
python import_missing_mcqs_simple.py

echo "Checking final count..."
python -c "
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_neurology_mcq.settings')
import django
django.setup()
from mcq.models import MCQ
print(f'Final MCQ count: {MCQ.objects.count()}')
"