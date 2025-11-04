#!/bin/bash
# Script to check the directory structure on Heroku
echo "Checking Heroku directory structure..."
heroku run "ls -la" --app mcq-reader
echo "Checking for django_neurology_mcq directory..."
heroku run "find . -name django_neurology_mcq -type d" --app mcq-reader
echo "Looking for manage.py file..."
heroku run "find . -name manage.py" --app mcq-reader
echo "Checking python path..."
heroku run "echo \$PYTHONPATH" --app mcq-reader