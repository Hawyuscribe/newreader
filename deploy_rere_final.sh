#!/bin/bash
# Deploy RERE MCQs to Heroku with improved error handling

APP_NAME="radiant-gorge-35079"
FIXTURE_FILE="rere_final_fixtures.json"

echo "=== Deploying RERE MCQs to Heroku ==="
echo "App: $APP_NAME"
echo "Expected MCQs: 3,046"
echo ""

# 1. Check current status
echo "1. Checking current database status..."
heroku run python django_neurology_mcq/manage.py shell -c "from mcq.models import MCQ; print(f'Current MCQs: {MCQ.objects.count()}')" --app $APP_NAME

# 2. Upload fixture file using a different method
echo "2. Uploading fixture file to Heroku..."

# First, try using heroku ps:copy if available
if command -v heroku &> /dev/null && heroku ps:copy --help &> /dev/null; then
    echo "Using heroku ps:copy..."
    heroku ps:copy $FIXTURE_FILE /tmp/$FIXTURE_FILE --app $APP_NAME
else
    echo "Using git method..."
    # Alternative: use git to add the file temporarily
    cp $FIXTURE_FILE django_neurology_mcq/fixtures/
    git add django_neurology_mcq/fixtures/$FIXTURE_FILE
    git commit -m "Add RERE fixtures temporarily"
    git push heroku stable_version:main
    heroku run cp django_neurology_mcq/fixtures/$FIXTURE_FILE /tmp/$FIXTURE_FILE --app $APP_NAME
fi

# 3. Load fixtures with proper error handling
echo "3. Loading fixtures into database..."
heroku run python django_neurology_mcq/manage.py loaddata /tmp/$FIXTURE_FILE --verbosity=2 --app $APP_NAME

# 4. Verify deployment
echo "4. Verifying deployment..."
heroku run python django_neurology_mcq/manage.py shell --app $APP_NAME << EOF
from mcq.models import MCQ
from django.db.models import Count
import sys

total = MCQ.objects.count()
print(f'Total MCQs after import: {total}')

# Breakdown by subspecialty
by_subspecialty = MCQ.objects.values('subspecialty').annotate(count=Count('id')).order_by('-count')
print('\nBreakdown by subspecialty:')
for sub in by_subspecialty:
    print(f'  {sub["subspecialty"]}: {sub["count"]}')

# Check explanation sections
with_explanations = MCQ.objects.filter(explanation_sections__isnull=False).exclude(explanation_sections={}).count()
print(f'\nMCQs with explanation sections: {with_explanations}')

# Check metadata
with_metadata = MCQ.objects.filter(metadata__isnull=False).exclude(metadata={}).count()
print(f'MCQs with metadata: {with_metadata}')

# Check if we have the expected count
if total == 3046:
    print('\n✓ SUCCESS: All 3,046 MCQs deployed successfully!')
else:
    print(f'\n⚠ WARNING: Expected 3,046 MCQs but found {total}')
    sys.exit(1)
EOF

echo ""
echo "=== Deployment Complete ==="
echo "Visit: https://radiant-gorge-35079-2b52ba172c1e.herokuapp.com/dashboard/"
