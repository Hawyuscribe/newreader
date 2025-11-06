#!/bin/bash
# Heroku MCQ sync script
echo "Starting MCQ sync to Heroku..."

# Clear existing MCQs first
echo "Clearing existing MCQs..."
heroku run "cd django_neurology_mcq && python manage.py shell -c 'from mcq.models import MCQ; MCQ.objects.all().delete(); print(f\"Cleared {MCQ.objects.count()} MCQs\")'" --app radiant-gorge-35079

# Load each chunk

echo "Loading chunk 1/29..."
heroku run "cd django_neurology_mcq && python manage.py loaddata heroku_sync_chunk_001_of_029.json" --app radiant-gorge-35079

echo "Loading chunk 2/29..."
heroku run "cd django_neurology_mcq && python manage.py loaddata heroku_sync_chunk_002_of_029.json" --app radiant-gorge-35079

echo "Loading chunk 3/29..."
heroku run "cd django_neurology_mcq && python manage.py loaddata heroku_sync_chunk_003_of_029.json" --app radiant-gorge-35079

echo "Loading chunk 4/29..."
heroku run "cd django_neurology_mcq && python manage.py loaddata heroku_sync_chunk_004_of_029.json" --app radiant-gorge-35079

echo "Loading chunk 5/29..."
heroku run "cd django_neurology_mcq && python manage.py loaddata heroku_sync_chunk_005_of_029.json" --app radiant-gorge-35079

echo "Loading chunk 6/29..."
heroku run "cd django_neurology_mcq && python manage.py loaddata heroku_sync_chunk_006_of_029.json" --app radiant-gorge-35079

echo "Loading chunk 7/29..."
heroku run "cd django_neurology_mcq && python manage.py loaddata heroku_sync_chunk_007_of_029.json" --app radiant-gorge-35079

echo "Loading chunk 8/29..."
heroku run "cd django_neurology_mcq && python manage.py loaddata heroku_sync_chunk_008_of_029.json" --app radiant-gorge-35079

echo "Loading chunk 9/29..."
heroku run "cd django_neurology_mcq && python manage.py loaddata heroku_sync_chunk_009_of_029.json" --app radiant-gorge-35079

echo "Loading chunk 10/29..."
heroku run "cd django_neurology_mcq && python manage.py loaddata heroku_sync_chunk_010_of_029.json" --app radiant-gorge-35079

echo "Loading chunk 11/29..."
heroku run "cd django_neurology_mcq && python manage.py loaddata heroku_sync_chunk_011_of_029.json" --app radiant-gorge-35079

echo "Loading chunk 12/29..."
heroku run "cd django_neurology_mcq && python manage.py loaddata heroku_sync_chunk_012_of_029.json" --app radiant-gorge-35079

echo "Loading chunk 13/29..."
heroku run "cd django_neurology_mcq && python manage.py loaddata heroku_sync_chunk_013_of_029.json" --app radiant-gorge-35079

echo "Loading chunk 14/29..."
heroku run "cd django_neurology_mcq && python manage.py loaddata heroku_sync_chunk_014_of_029.json" --app radiant-gorge-35079

echo "Loading chunk 15/29..."
heroku run "cd django_neurology_mcq && python manage.py loaddata heroku_sync_chunk_015_of_029.json" --app radiant-gorge-35079

echo "Loading chunk 16/29..."
heroku run "cd django_neurology_mcq && python manage.py loaddata heroku_sync_chunk_016_of_029.json" --app radiant-gorge-35079

echo "Loading chunk 17/29..."
heroku run "cd django_neurology_mcq && python manage.py loaddata heroku_sync_chunk_017_of_029.json" --app radiant-gorge-35079

echo "Loading chunk 18/29..."
heroku run "cd django_neurology_mcq && python manage.py loaddata heroku_sync_chunk_018_of_029.json" --app radiant-gorge-35079

echo "Loading chunk 19/29..."
heroku run "cd django_neurology_mcq && python manage.py loaddata heroku_sync_chunk_019_of_029.json" --app radiant-gorge-35079

echo "Loading chunk 20/29..."
heroku run "cd django_neurology_mcq && python manage.py loaddata heroku_sync_chunk_020_of_029.json" --app radiant-gorge-35079

echo "Loading chunk 21/29..."
heroku run "cd django_neurology_mcq && python manage.py loaddata heroku_sync_chunk_021_of_029.json" --app radiant-gorge-35079

echo "Loading chunk 22/29..."
heroku run "cd django_neurology_mcq && python manage.py loaddata heroku_sync_chunk_022_of_029.json" --app radiant-gorge-35079

echo "Loading chunk 23/29..."
heroku run "cd django_neurology_mcq && python manage.py loaddata heroku_sync_chunk_023_of_029.json" --app radiant-gorge-35079

echo "Loading chunk 24/29..."
heroku run "cd django_neurology_mcq && python manage.py loaddata heroku_sync_chunk_024_of_029.json" --app radiant-gorge-35079

echo "Loading chunk 25/29..."
heroku run "cd django_neurology_mcq && python manage.py loaddata heroku_sync_chunk_025_of_029.json" --app radiant-gorge-35079

echo "Loading chunk 26/29..."
heroku run "cd django_neurology_mcq && python manage.py loaddata heroku_sync_chunk_026_of_029.json" --app radiant-gorge-35079

echo "Loading chunk 27/29..."
heroku run "cd django_neurology_mcq && python manage.py loaddata heroku_sync_chunk_027_of_029.json" --app radiant-gorge-35079

echo "Loading chunk 28/29..."
heroku run "cd django_neurology_mcq && python manage.py loaddata heroku_sync_chunk_028_of_029.json" --app radiant-gorge-35079

echo "Loading chunk 29/29..."
heroku run "cd django_neurology_mcq && python manage.py loaddata heroku_sync_chunk_029_of_029.json" --app radiant-gorge-35079

echo "Verifying final count..."
heroku run "cd django_neurology_mcq && python manage.py shell -c 'from mcq.models import MCQ; print(f\"Final count: {{MCQ.objects.count()}} MCQs\")'" --app radiant-gorge-35079

echo "MCQ sync complete!"
