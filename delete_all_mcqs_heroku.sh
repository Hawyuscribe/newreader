#!/bin/bash
# Script to delete ALL MCQs from Heroku to ensure no duplicates

APP_NAME="radiant-gorge-35079"
LOG_FILE="deletion_log_$(date +%Y%m%d_%H%M%S).txt"

echo "MCQ DELETION FROM HEROKU" | tee $LOG_FILE
echo "=======================" | tee -a $LOG_FILE
echo "Started at: $(date)" | tee -a $LOG_FILE

# Check current count
echo -e "\nChecking current MCQ count..." | tee -a $LOG_FILE
heroku run "cd /app/django_neurology_mcq && python manage.py shell -c 'from mcq.models import MCQ; print(f\"Current MCQs: {MCQ.objects.count()}\")'" -a $APP_NAME | tee -a $LOG_FILE

# Delete all MCQs
echo -e "\nDeleting ALL MCQs..." | tee -a $LOG_FILE
heroku run "cd /app/django_neurology_mcq && python manage.py shell -c '
from mcq.models import MCQ
from django.db import transaction

# Delete in batches to avoid timeout
initial_count = MCQ.objects.count()
print(f\"Deleting {initial_count} MCQs...\")

deleted = 0
batch_size = 500

while MCQ.objects.exists():
    with transaction.atomic():
        batch_ids = list(MCQ.objects.values_list(\"id\", flat=True)[:batch_size])
        if batch_ids:
            MCQ.objects.filter(id__in=batch_ids).delete()
            deleted += len(batch_ids)
            print(f\"Deleted {deleted} so far...\")

print(f\"Deletion complete! Total deleted: {deleted}\")
final_count = MCQ.objects.count()
print(f\"Remaining MCQs: {final_count}\")
'" -a $APP_NAME | tee -a $LOG_FILE

# Verify deletion
echo -e "\nVerifying deletion..." | tee -a $LOG_FILE
heroku run "cd /app/django_neurology_mcq && python manage.py shell -c '
from mcq.models import MCQ
count = MCQ.objects.count()
if count == 0:
    print(\"✓ SUCCESS: Database is clean - no MCQs remain\")
else:
    print(f\"✗ ERROR: {count} MCQs still exist - deletion incomplete!\")
'" -a $APP_NAME | tee -a $LOG_FILE

echo -e "\nDeletion completed at: $(date)" | tee -a $LOG_FILE
echo "Log file: $LOG_FILE" | tee -a $LOG_FILE