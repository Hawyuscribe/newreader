#!/bin/bash
# Heroku MCQ sync script - Generated automatically
echo "Starting MCQ sync to Heroku..."

# First, commit and push the fixture files to Heroku
echo "Adding fixture files to git..."
git add heroku_sync_chunk_001_of_028.json
git add heroku_sync_chunk_002_of_028.json
git add heroku_sync_chunk_003_of_028.json
git add heroku_sync_chunk_004_of_028.json
git add heroku_sync_chunk_005_of_028.json
git add heroku_sync_chunk_006_of_028.json
git add heroku_sync_chunk_007_of_028.json
git add heroku_sync_chunk_008_of_028.json
git add heroku_sync_chunk_009_of_028.json
git add heroku_sync_chunk_010_of_028.json
git add heroku_sync_chunk_011_of_028.json
git add heroku_sync_chunk_012_of_028.json
git add heroku_sync_chunk_013_of_028.json
git add heroku_sync_chunk_014_of_028.json
git add heroku_sync_chunk_015_of_028.json
git add heroku_sync_chunk_016_of_028.json
git add heroku_sync_chunk_017_of_028.json
git add heroku_sync_chunk_018_of_028.json
git add heroku_sync_chunk_019_of_028.json
git add heroku_sync_chunk_020_of_028.json
git add heroku_sync_chunk_021_of_028.json
git add heroku_sync_chunk_022_of_028.json
git add heroku_sync_chunk_023_of_028.json
git add heroku_sync_chunk_024_of_028.json
git add heroku_sync_chunk_025_of_028.json
git add heroku_sync_chunk_026_of_028.json
git add heroku_sync_chunk_027_of_028.json
git add heroku_sync_chunk_028_of_028.json

git commit -m "Add MCQ fixture chunks for sync"
git push heroku stable_version:main

# Wait for deployment
echo "Waiting for deployment to complete..."
sleep 30

# Clear existing MCQs first
echo "Clearing existing MCQs..."
heroku run "cd django_neurology_mcq && python manage.py shell -c 'from mcq.models import MCQ; count = MCQ.objects.count(); MCQ.objects.all().delete(); print(f"Cleared {count} MCQs")'" --app radiant-gorge-35079

# Load each chunk

echo "Loading chunk 1/28..."
heroku run "cd django_neurology_mcq && python manage.py loaddata heroku_sync_chunk_001_of_028.json" --app radiant-gorge-35079

echo "Loading chunk 2/28..."
heroku run "cd django_neurology_mcq && python manage.py loaddata heroku_sync_chunk_002_of_028.json" --app radiant-gorge-35079

echo "Loading chunk 3/28..."
heroku run "cd django_neurology_mcq && python manage.py loaddata heroku_sync_chunk_003_of_028.json" --app radiant-gorge-35079

echo "Loading chunk 4/28..."
heroku run "cd django_neurology_mcq && python manage.py loaddata heroku_sync_chunk_004_of_028.json" --app radiant-gorge-35079

echo "Loading chunk 5/28..."
heroku run "cd django_neurology_mcq && python manage.py loaddata heroku_sync_chunk_005_of_028.json" --app radiant-gorge-35079

echo "Loading chunk 6/28..."
heroku run "cd django_neurology_mcq && python manage.py loaddata heroku_sync_chunk_006_of_028.json" --app radiant-gorge-35079

echo "Loading chunk 7/28..."
heroku run "cd django_neurology_mcq && python manage.py loaddata heroku_sync_chunk_007_of_028.json" --app radiant-gorge-35079

echo "Loading chunk 8/28..."
heroku run "cd django_neurology_mcq && python manage.py loaddata heroku_sync_chunk_008_of_028.json" --app radiant-gorge-35079

echo "Loading chunk 9/28..."
heroku run "cd django_neurology_mcq && python manage.py loaddata heroku_sync_chunk_009_of_028.json" --app radiant-gorge-35079

echo "Loading chunk 10/28..."
heroku run "cd django_neurology_mcq && python manage.py loaddata heroku_sync_chunk_010_of_028.json" --app radiant-gorge-35079

echo "Loading chunk 11/28..."
heroku run "cd django_neurology_mcq && python manage.py loaddata heroku_sync_chunk_011_of_028.json" --app radiant-gorge-35079

echo "Loading chunk 12/28..."
heroku run "cd django_neurology_mcq && python manage.py loaddata heroku_sync_chunk_012_of_028.json" --app radiant-gorge-35079

echo "Loading chunk 13/28..."
heroku run "cd django_neurology_mcq && python manage.py loaddata heroku_sync_chunk_013_of_028.json" --app radiant-gorge-35079

echo "Loading chunk 14/28..."
heroku run "cd django_neurology_mcq && python manage.py loaddata heroku_sync_chunk_014_of_028.json" --app radiant-gorge-35079

echo "Loading chunk 15/28..."
heroku run "cd django_neurology_mcq && python manage.py loaddata heroku_sync_chunk_015_of_028.json" --app radiant-gorge-35079

echo "Loading chunk 16/28..."
heroku run "cd django_neurology_mcq && python manage.py loaddata heroku_sync_chunk_016_of_028.json" --app radiant-gorge-35079

echo "Loading chunk 17/28..."
heroku run "cd django_neurology_mcq && python manage.py loaddata heroku_sync_chunk_017_of_028.json" --app radiant-gorge-35079

echo "Loading chunk 18/28..."
heroku run "cd django_neurology_mcq && python manage.py loaddata heroku_sync_chunk_018_of_028.json" --app radiant-gorge-35079

echo "Loading chunk 19/28..."
heroku run "cd django_neurology_mcq && python manage.py loaddata heroku_sync_chunk_019_of_028.json" --app radiant-gorge-35079

echo "Loading chunk 20/28..."
heroku run "cd django_neurology_mcq && python manage.py loaddata heroku_sync_chunk_020_of_028.json" --app radiant-gorge-35079

echo "Loading chunk 21/28..."
heroku run "cd django_neurology_mcq && python manage.py loaddata heroku_sync_chunk_021_of_028.json" --app radiant-gorge-35079

echo "Loading chunk 22/28..."
heroku run "cd django_neurology_mcq && python manage.py loaddata heroku_sync_chunk_022_of_028.json" --app radiant-gorge-35079

echo "Loading chunk 23/28..."
heroku run "cd django_neurology_mcq && python manage.py loaddata heroku_sync_chunk_023_of_028.json" --app radiant-gorge-35079

echo "Loading chunk 24/28..."
heroku run "cd django_neurology_mcq && python manage.py loaddata heroku_sync_chunk_024_of_028.json" --app radiant-gorge-35079

echo "Loading chunk 25/28..."
heroku run "cd django_neurology_mcq && python manage.py loaddata heroku_sync_chunk_025_of_028.json" --app radiant-gorge-35079

echo "Loading chunk 26/28..."
heroku run "cd django_neurology_mcq && python manage.py loaddata heroku_sync_chunk_026_of_028.json" --app radiant-gorge-35079

echo "Loading chunk 27/28..."
heroku run "cd django_neurology_mcq && python manage.py loaddata heroku_sync_chunk_027_of_028.json" --app radiant-gorge-35079

echo "Loading chunk 28/28..."
heroku run "cd django_neurology_mcq && python manage.py loaddata heroku_sync_chunk_028_of_028.json" --app radiant-gorge-35079

echo "Verifying final count..."
heroku run "cd django_neurology_mcq && python manage.py shell -c 'from mcq.models import MCQ; from django.db.models import Count; total = MCQ.objects.count(); print(f"Final count: {total} MCQs"); subspecialties = MCQ.objects.values("subspecialty").annotate(count=Count("id")).order_by("-count"); print("\nTop subspecialties:"); [print(f"  {s[\"subspecialty\"]}: {s[\"count\"]}") for s in subspecialties[:5]]'" --app radiant-gorge-35079

echo "MCQ sync complete!"
