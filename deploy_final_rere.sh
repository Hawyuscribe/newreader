#!/bin/bash
# Deploy RERE MCQs with correct answers from option_analysis

APP_NAME="radiant-gorge-35079"
FIXTURE_FILE="final_rere_fixtures.json"

echo "=== Deploying RERE MCQs to Heroku ==="
echo "App: $APP_NAME (https://radiant-gorge-35079-2b52ba172c1e.herokuapp.com/dashboard/)"
echo "Expected MCQs: 3,046"
echo "Correct answers extracted from option_analysis sections"
echo ""

# 1. Check current status
echo "1. Checking current database status..."
heroku run python django_neurology_mcq/manage.py shell -c "from mcq.models import MCQ; print(f'Current MCQs: {MCQ.objects.count()}')" --app $APP_NAME

# 2. Upload fixture file
echo "2. Uploading fixture file to Heroku..."
# Use git to temporarily add the file
cp $FIXTURE_FILE django_neurology_mcq/fixtures/
git add django_neurology_mcq/fixtures/$FIXTURE_FILE
git commit -m "Add RERE fixtures for deployment"
git push heroku stable_version:main

# 3. Load fixtures
echo "3. Loading fixtures into database..."
heroku run python django_neurology_mcq/manage.py loaddata fixtures/$FIXTURE_FILE --verbosity=2 --app $APP_NAME

# 4. Verify deployment
echo "4. Verifying deployment..."
heroku run python django_neurology_mcq/manage.py shell --app $APP_NAME << 'EOF'
from mcq.models import MCQ
from django.db.models import Count

total = MCQ.objects.count()
print(f'Total MCQs after import: {total}')

# Breakdown by subspecialty
by_subspecialty = MCQ.objects.values('subspecialty').annotate(count=Count('id')).order_by('-count')
print('\nBreakdown by subspecialty:')
for sub in by_subspecialty:
    print(f'  {sub["subspecialty"]}: {sub["count"]}')

# Check explanation sections
with_option_analysis = MCQ.objects.filter(
    explanation_sections__has_key='option_analysis'
).exclude(
    explanation_sections__option_analysis=''
).count()
print(f'\nMCQs with option_analysis: {with_option_analysis}')

# Sample check of correct answers
sample_mcqs = MCQ.objects.all()[:5]
print('\nSample MCQs with correct answers:')
for mcq in sample_mcqs:
    print(f'  Q{mcq.question_number}: Correct answer = {mcq.correct_answer}')

if total == 3046:
    print('\n✓ SUCCESS: All 3,046 MCQs deployed successfully!')
    print('✓ Correct answers extracted from option_analysis sections')
else:
    print(f'\n⚠ WARNING: Expected 3,046 MCQs but found {total}')
EOF

# Clean up
git reset HEAD^ --soft
rm django_neurology_mcq/fixtures/$FIXTURE_FILE

echo ""
echo "=== Deployment Complete ==="
echo "Visit: https://radiant-gorge-35079-2b52ba172c1e.herokuapp.com/dashboard/"
