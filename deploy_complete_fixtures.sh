#!/bin/bash
# Deploy complete MCQ fixtures to Heroku

echo "=== Deploying Complete MCQ Database to Heroku ==="
echo "Heroku app: radiant-gorge-35079"
echo ""

# 1. First, backup existing data (optional)
echo "1. Backing up existing data (optional)..."
heroku run python django_neurology_mcq/manage.py dumpdata mcq.mcq --indent 2 > backup_before_deployment.json --app radiant-gorge-35079

# 2. Clear existing MCQs (optional - uncomment if needed)
# echo "2. Clearing existing MCQs..."
# heroku run python django_neurology_mcq/manage.py shell -c "from mcq.models import MCQ; MCQ.objects.all().delete()" --app radiant-gorge-35079

# 3. Copy fixtures to Heroku
echo "2. Transferring fixtures to Heroku..."
heroku run mkdir -p /app/fixtures --app radiant-gorge-35079

# Use heroku command to transfer the file
heroku ps:copy complete_mcq_fixtures.json /app/fixtures/complete_mcq_fixtures.json --app radiant-gorge-35079

# 4. Load fixtures into database
echo "3. Loading fixtures into database..."
heroku run python django_neurology_mcq/manage.py loaddata /app/fixtures/complete_mcq_fixtures.json --app radiant-gorge-35079

# 5. Verify the deployment
echo "4. Verifying deployment..."
heroku run python django_neurology_mcq/manage.py shell -c "
from mcq.models import MCQ
from django.db.models import Count

total = MCQ.objects.count()
by_subspecialty = MCQ.objects.values('subspecialty').annotate(count=Count('id')).order_by('-count')

print(f'Total MCQs imported: {total}')
print('\nBreakdown by subspecialty:')
for sub in by_subspecialty[:10]:
    print(f'  {sub["subspecialty"]}: {sub["count"]}')
    
with_explanations = MCQ.objects.filter(explanation_sections__isnull=False).count()
print(f'\nMCQs with explanation sections: {with_explanations}')
" --app radiant-gorge-35079

echo ""
echo "=== Deployment Complete ==="
echo "Visit your site: https://radiant-gorge-35079-2b52ba172c1e.herokuapp.com/dashboard/"
