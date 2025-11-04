#!/bin/bash
# Complete MCQ Deployment Script - Clean import with no duplicates

APP_NAME="radiant-gorge-35079"
RERE_DIR="/Users/tariqalmatrudi/Documents/MCQs for the board/Previous MCQs/json explained/reclass/RERE"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
LOG_FILE="deployment_log_${TIMESTAMP}.txt"

echo "COMPLETE MCQ DEPLOYMENT" | tee $LOG_FILE
echo "======================" | tee -a $LOG_FILE
echo "Started at: $(date)" | tee -a $LOG_FILE
echo "" | tee -a $LOG_FILE

# STEP 1: DELETE ALL EXISTING MCQs
echo "[STEP 1] DELETING ALL EXISTING MCQs" | tee -a $LOG_FILE
echo "===================================" | tee -a $LOG_FILE

# Check current count first
heroku run "cd /app/django_neurology_mcq && python manage.py shell -c '
from mcq.models import MCQ
count = MCQ.objects.count()
print(f\"Current MCQs in database: {count}\")
if count > 0:
    print(\"Proceeding with deletion...\")
else:
    print(\"Database is already empty\")
'" -a $APP_NAME | tee -a $LOG_FILE

# Delete all MCQs in batches
heroku run "cd /app/django_neurology_mcq && python manage.py shell -c '
from mcq.models import MCQ
from django.db import transaction

initial_count = MCQ.objects.count()
if initial_count > 0:
    print(f\"Deleting {initial_count} MCQs...\")
    
    # Method 1: Try bulk delete first
    try:
        MCQ.objects.all().delete()
        print(\"Bulk deletion successful\")
    except Exception as e:
        print(f\"Bulk deletion failed: {e}\")
        print(\"Trying batch deletion...\")
        
        # Method 2: Batch deletion
        deleted = 0
        batch_size = 100
        
        while MCQ.objects.exists():
            with transaction.atomic():
                batch_ids = list(MCQ.objects.values_list(\"id\", flat=True)[:batch_size])
                if batch_ids:
                    MCQ.objects.filter(id__in=batch_ids).delete()
                    deleted += len(batch_ids)
                    if deleted % 500 == 0:
                        print(f\"Deleted {deleted} MCQs...\")
        
        print(f\"Batch deletion complete. Total deleted: {deleted}\")

final_count = MCQ.objects.count()
print(f\"\\nFinal MCQ count: {final_count}\")
if final_count == 0:
    print(\"✓ SUCCESS: All MCQs deleted\")
else:
    print(\"✗ ERROR: Some MCQs remain\")
'" -a $APP_NAME | tee -a $LOG_FILE

# STEP 2: PREPARE FILES FOR UPLOAD
echo -e "\n[STEP 2] PREPARING FILES FOR UPLOAD" | tee -a $LOG_FILE
echo "====================================" | tee -a $LOG_FILE

# Create list of files to upload
echo "Creating file list..." | tee -a $LOG_FILE
ls -la "$RERE_DIR"/*.json | tee -a $LOG_FILE

# STEP 3: MANUAL UPLOAD INSTRUCTIONS
echo -e "\n[STEP 3] MANUAL UPLOAD REQUIRED" | tee -a $LOG_FILE
echo "===============================" | tee -a $LOG_FILE
echo "" | tee -a $LOG_FILE
echo "To complete the deployment, you need to:" | tee -a $LOG_FILE
echo "" | tee -a $LOG_FILE
echo "1. Upload each JSON file from RERE directory to GitHub Gists" | tee -a $LOG_FILE
echo "2. For each file, create a public Gist and get the raw URL" | tee -a $LOG_FILE
echo "3. Run the import command for each file:" | tee -a $LOG_FILE
echo "" | tee -a $LOG_FILE

# Generate commands for each file
cd "$RERE_DIR"
for file in *.json; do
    echo "For $file:" | tee -a $LOG_FILE
    echo "  heroku run 'cd /app/django_neurology_mcq && python manage.py import_rere_mcqs [GIST_RAW_URL_FOR_$file]' -a $APP_NAME" | tee -a $LOG_FILE
    echo "" | tee -a $LOG_FILE
done
cd -

# STEP 4: VERIFICATION SCRIPT
echo -e "\n[STEP 4] VERIFICATION" | tee -a $LOG_FILE
echo "=====================" | tee -a $LOG_FILE
echo "" | tee -a $LOG_FILE
echo "After importing all files, run this verification:" | tee -a $LOG_FILE
echo "" | tee -a $LOG_FILE

cat > verify_deployment.sh << 'EOF'
heroku run "cd /app/django_neurology_mcq && python manage.py shell -c '
from mcq.models import MCQ
from django.db.models import Count

print(\"=\"*60)
print(\"MCQ DEPLOYMENT VERIFICATION\")
print(\"=\"*60)

# Total count
total = MCQ.objects.count()
print(f\"\\nTotal MCQs: {total}\")
print(f\"Expected: 3,046\")
if total >= 3000:
    print(\"✓ PASS: MCQ count is acceptable\")
else:
    print(\"✗ FAIL: MCQ count is too low\")

# Check for duplicates
from django.db.models import Count
duplicates = MCQ.objects.values(\"question_text\").annotate(count=Count(\"id\")).filter(count__gt=1)
dup_count = duplicates.count()
print(f\"\\nDuplicate questions: {dup_count}\")
if dup_count == 0:
    print(\"✓ PASS: No duplicates found\")
else:
    print(\"✗ WARNING: Duplicates detected\")
    print(\"First 5 duplicates:\")
    for dup in duplicates[:5]:
        print(f\"  - {dup[\\\"question_text\\\"][:100]}... (count: {dup[\\\"count\\\"]})\")

# By subspecialty
print(\"\\nMCQs by Subspecialty:\")
subspecialties = MCQ.objects.values(\"subspecialty\").annotate(count=Count(\"id\")).order_by(\"-count\")
for item in subspecialties:
    print(f\"  {item[\\\"subspecialty\\\"]}: {item[\\\"count\\\"]}\")

# Check correct answers
with_correct = MCQ.objects.exclude(correct_answer__isnull=True).exclude(correct_answer=\"\").count()
print(f\"\\nMCQs with correct answers: {with_correct} ({with_correct/total*100:.1f}%)\")

# Check explanation sections
with_sections = MCQ.objects.exclude(explanation_sections__isnull=True).count()
print(f\"MCQs with explanation sections: {with_sections} ({with_sections/total*100:.1f}%)\")

# Sample MCQ check
sample = MCQ.objects.first()
if sample:
    print(\"\\nSample MCQ:\")
    print(f\"  Question: {sample.question_text[:100]}...\")
    print(f\"  Subspecialty: {sample.subspecialty}\")
    print(f\"  Correct Answer: {sample.correct_answer}\")
    print(f\"  Has explanation sections: {bool(sample.explanation_sections)}\")
    if sample.explanation_sections:
        print(f\"  Sections: {list(sample.explanation_sections.keys())[:5]}...\")

print(\"\\n\" + \"=\"*60)
'" -a radiant-gorge-35079
EOF

chmod +x verify_deployment.sh
echo "Run verification with: ./verify_deployment.sh" | tee -a $LOG_FILE

echo -e "\nDeployment instructions completed at: $(date)" | tee -a $LOG_FILE
echo "Log file: $LOG_FILE" | tee -a $LOG_FILE

# Create summary
echo -e "\n=== SUMMARY ===" | tee -a $LOG_FILE
echo "1. All existing MCQs have been deleted" | tee -a $LOG_FILE
echo "2. Upload each JSON file to GitHub Gist" | tee -a $LOG_FILE
echo "3. Run import command for each Gist URL" | tee -a $LOG_FILE
echo "4. Run verification script to confirm deployment" | tee -a $LOG_FILE
echo "" | tee -a $LOG_FILE
echo "Total files to upload: $(ls "$RERE_DIR"/*.json | wc -l)" | tee -a $LOG_FILE