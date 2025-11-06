#!/bin/bash
# Deploy Case Learning Improvements

echo "Deploying Case-Based Learning improvements..."

# Create migrations if needed
python manage.py makemigrations mcq --noinput || true

# Apply migrations
python manage.py migrate --noinput

# Clear any stale cache
python -c "from django.core.cache import cache; cache.clear()"

echo "Deployment complete!"
