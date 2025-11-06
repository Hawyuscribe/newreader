#!/bin/bash
# Load RERE MCQ fixtures

echo "Starting RERE MCQ deployment..."

# First, clear all existing MCQs
echo "Clearing existing MCQs..."
heroku run python django_neurology_mcq/manage.py shell --command="from mcq.models import MCQ; MCQ.objects.all().delete(); print('MCQs cleared')" -a radiant-gorge-35079

# Wait a moment
sleep 2

# Load each chunk individually
echo "Loading RERE fixtures..."
for i in {01..21}
do
    echo "Loading chunk $i..."
    heroku run python django_neurology_mcq/manage.py loaddata rere_chunks/rere_chunk_$i.json -a radiant-gorge-35079
    sleep 1
done

# Verify the result
echo "Verifying deployment..."
heroku run python django_neurology_mcq/manage.py shell --command="from mcq.models import MCQ; print(f'Total MCQs: {MCQ.objects.count()}')" -a radiant-gorge-35079

echo "Deployment complete!"