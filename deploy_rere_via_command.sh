#!/bin/bash
# Deploy RERE MCQs using the new management command

RERE_DIR="/Users/tariqalmatrudi/Documents/MCQs for the board/Previous MCQs/json explained/reclass/RERE"
APP_NAME="radiant-gorge-35079"

echo "=== Deploying RERE MCQs to Heroku ==="
echo "App: $APP_NAME"
echo "RERE Directory: $RERE_DIR"
echo ""

# 1. Check current status
echo "1. Checking current database status..."
heroku run python django_neurology_mcq/manage.py shell -c "from mcq.models import MCQ; print(f'Current MCQs: {MCQ.objects.count()}')" --app $APP_NAME

# 2. Clear and import all MCQs
echo "2. Importing all RERE MCQs (with --clear flag)..."
heroku run python django_neurology_mcq/manage.py import_rere_mcqs --dir "/app/RERE" --clear --app $APP_NAME

# 3. Verify deployment
echo "3. Verifying deployment..."
heroku run python django_neurology_mcq/manage.py shell -c "
from mcq.models import MCQ
from django.db.models import Count

total = MCQ.objects.count()
print(f'Total MCQs: {total}')

# Breakdown by subspecialty
by_sub = MCQ.objects.values('subspecialty').annotate(count=Count('id')).order_by('-count')
print('\\nBreakdown by subspecialty:')
for sub in by_sub[:10]:
    print(f'  {sub[\"subspecialty\"]}: {sub[\"count\"]}')
" --app $APP_NAME

echo ""
echo "=== Deployment Complete ==="
echo "Visit: https://radiant-gorge-35079-2b52ba172c1e.herokuapp.com/dashboard/"