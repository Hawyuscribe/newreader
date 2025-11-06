#!/bin/bash
# Deploy RERE MCQs to Heroku (radiant-gorge-35079)

echo "=== Deploying RERE MCQs to Heroku ==="
echo "Source: RERE directory (3,046 MCQs)"
echo "Target: radiant-gorge-35079-2b52ba172c1e.herokuapp.com"
echo ""

# 1. Show current status
echo "1. Checking current database status..."
heroku run python django_neurology_mcq/manage.py shell -c "from mcq.models import MCQ; print(f'Current MCQs in database: {MCQ.objects.count()}')" --app radiant-gorge-35079

# 2. Transfer fixture file using git and heroku
echo "2. Transferring fixture file to Heroku..."
# First, try to copy the file directly
cat rere_complete_fixtures.json | heroku run "cat > /tmp/rere_complete_fixtures.json" --app radiant-gorge-35079

# 3. Load fixtures
echo "3. Loading fixtures into database..."
heroku run python django_neurology_mcq/manage.py loaddata /tmp/rere_complete_fixtures.json --app radiant-gorge-35079

# 4. Verify the deployment
echo "4. Verifying deployment..."
heroku run python django_neurology_mcq/manage.py shell -c "
from mcq.models import MCQ
from django.db.models import Count

total = MCQ.objects.count()
by_subspecialty = MCQ.objects.values('subspecialty').annotate(count=Count('id')).order_by('-count')

print(f'Total MCQs after import: {total}')
print('\nBreakdown by subspecialty:')
for sub in by_subspecialty:
    print(f'  {sub["subspecialty"]}: {sub["count"]}')
    
# Check for explanation sections
with_explanations = MCQ.objects.filter(explanation_sections__isnull=False).count()
empty_explanations = MCQ.objects.filter(explanation_sections={}).count()
print(f'\nMCQs with explanation sections: {with_explanations}')
print(f'MCQs with empty explanation sections: {empty_explanations}')

# Check metadata preservation
with_metadata = MCQ.objects.filter(metadata__isnull=False).count()
print(f'MCQs with metadata: {with_metadata}')
" --app radiant-gorge-35079

echo ""
echo "=== Deployment Complete ==="
echo "Visit your site: https://radiant-gorge-35079-2b52ba172c1e.herokuapp.com/dashboard/"
