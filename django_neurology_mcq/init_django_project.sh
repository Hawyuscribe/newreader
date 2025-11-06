#!/bin/bash
# Initialize Django project

set -e

# Activate virtual environment
source ../venv/bin/activate

echo "Creating database migrations..."
python manage.py makemigrations mcq

echo "Applying migrations..."
python manage.py migrate

echo "Setting up static files..."
python manage.py collectstatic --noinput

echo "Migrating data from old database..."
python migrate_data.py

echo "Creating superuser..."
echo "Username: admin"
echo "Email: admin@example.com"
echo "Password: admin"
echo "Note: This is just a placeholder. In a production environment, use a secure password!"

echo "Django project initialization complete!"
echo "You can now run the development server with:"
echo "python manage.py runserver"