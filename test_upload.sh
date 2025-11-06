#!/bin/bash
# Test script to upload a single MCQ fixture to verify process

HEROKU_APP="radiant-gorge-35079"

# Create a test fixture with just the first MCQ
head -n 97 mcq_fixtures.json | tail -n +2 > test_mcq.json
echo ']' >> test_mcq.json

echo "Created test fixture with 1 MCQ"

# Upload to Heroku
echo "Uploading test fixture..."
cat test_mcq.json | heroku run --app $HEROKU_APP "cd /app && cat > /tmp/test.json && python manage.py loaddata /tmp/test.json"

# Check the count
echo "Checking MCQ count..."
heroku run --app $HEROKU_APP "cd /app && python manage.py shell -c 'from mcq.models import MCQ; print(f\"Total MCQs: {MCQ.objects.count()}\")'"

echo "Test complete!"