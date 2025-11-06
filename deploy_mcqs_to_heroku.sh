#!/bin/bash
# MCQ Deployment Script for Heroku

APP_NAME="radiant-gorge-35079"
RERE_DIR="/Users/tariqalmatrudi/Documents/MCQs for the board/Previous MCQs/json explained/reclass/RERE"
LOG_FILE="deployment_log_$(date +%Y%m%d_%H%M%S).txt"

echo "MCQ Deployment to Heroku" | tee -a $LOG_FILE
echo "========================" | tee -a $LOG_FILE
echo "Started at: $(date)" | tee -a $LOG_FILE

# Step 1: Delete existing MCQs
echo -e "\n[Step 1] Deleting existing MCQs..." | tee -a $LOG_FILE
heroku run "cd /app/django_neurology_mcq && python manage.py shell -c 'from mcq.models import MCQ; count = MCQ.objects.count(); print(f\"Deleting {count} MCQs...\"); MCQ.objects.all().delete(); print(\"Done\")'" -a $APP_NAME | tee -a $LOG_FILE

# Step 2: Upload management command
echo -e "\n[Step 2] Uploading management command..." | tee -a $LOG_FILE
# This needs to be done manually or through git push
echo "Please ensure import_rere_mcqs.py is deployed to Heroku" | tee -a $LOG_FILE

# Step 3: Process each JSON file
echo -e "\n[Step 3] Importing MCQs from RERE files..." | tee -a $LOG_FILE

# Get list of files
files=($(ls "$RERE_DIR"/*.json | sort))
total_files=${#files[@]}

echo "Found $total_files files to process" | tee -a $LOG_FILE

# Upload each file to a temporary GitHub Gist and import
for i in "${!files[@]}"; do
    file="${files[$i]}"
    filename=$(basename "$file")
    echo -e "\n[$((i+1))/$total_files] Processing $filename..." | tee -a $LOG_FILE
    
    # Create temporary file for upload
    echo "Please upload $filename to a GitHub Gist and get the raw URL" | tee -a $LOG_FILE
    echo "Then run:" | tee -a $LOG_FILE
    echo "heroku run 'cd /app/django_neurology_mcq && python manage.py import_rere_mcqs [GIST_URL]' -a $APP_NAME" | tee -a $LOG_FILE
    
    # Alternative: Direct file upload approach
    # You can also scp or use other methods to upload the file directly
done

# Step 4: Final verification
echo -e "\n[Step 4] Verification script..." | tee -a $LOG_FILE
cat > verify_mcqs.py << 'EOF'
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
import django
django.setup()

from mcq.models import MCQ
from django.db.models import Count

# Total count
total = MCQ.objects.count()
print(f"Total MCQs: {total}")
print(f"Expected: 3,046")

# By subspecialty
print("\nMCQs by Subspecialty:")
subspecialties = MCQ.objects.values('subspecialty').annotate(count=Count('id')).order_by('-count')
for item in subspecialties[:10]:
    print(f"  {item['subspecialty']}: {item['count']}")

# Check correct answers
with_correct = MCQ.objects.exclude(correct_answer__isnull=True).exclude(correct_answer='').count()
print(f"\nMCQs with correct answers: {with_correct} ({with_correct/total*100:.1f}%)")

# Check explanation sections
with_sections = MCQ.objects.exclude(explanation_sections__isnull=True).count()
print(f"MCQs with explanation sections: {with_sections} ({with_sections/total*100:.1f}%)")
EOF

echo "Run verification with:" | tee -a $LOG_FILE
echo "heroku run 'cd /app/django_neurology_mcq && python verify_mcqs.py' -a $APP_NAME" | tee -a $LOG_FILE

echo -e "\nDeployment instructions completed at: $(date)" | tee -a $LOG_FILE
echo "Log file: $LOG_FILE" | tee -a $LOG_FILE