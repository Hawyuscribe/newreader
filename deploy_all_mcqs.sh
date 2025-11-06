#!/bin/bash
# Complete MCQ deployment script for Heroku

APP_NAME="radiant-gorge-35079"
RERE_DIR="/Users/tariqalmatrudi/Documents/MCQs for the board/Previous MCQs/json explained/reclass/RERE"
LOG_FILE="deployment_log_$(date +%Y%m%d_%H%M%S).txt"

echo "MCQ Deployment to Heroku" | tee $LOG_FILE
echo "========================" | tee -a $LOG_FILE
echo "Started at: $(date)" | tee -a $LOG_FILE

# Step 1: Delete existing MCQs
echo -e "\n[Step 1] Deleting existing MCQs..." | tee -a $LOG_FILE
heroku run python heroku_delete_mcqs.py -a $APP_NAME 2>&1 | tee -a $LOG_FILE

# Step 2: Prepare files for upload
echo -e "\n[Step 2] Preparing RERE files..." | tee -a $LOG_FILE

# Create a temporary directory for upload
TEMP_DIR="/tmp/rere_upload_$(date +%Y%m%d_%H%M%S)"
mkdir -p $TEMP_DIR

# Copy Python scripts
cp heroku_import_rere_mcqs.py $TEMP_DIR/
cp verify_deployment.py $TEMP_DIR/

# Copy RERE JSON files
cp -r "$RERE_DIR" $TEMP_DIR/

# Create upload script for Heroku
cat > $TEMP_DIR/run_import.py << 'EOF'
#!/usr/bin/env python3
import subprocess
import os

# Run the import script with the RERE directory
subprocess.run(['python', 'heroku_import_rere_mcqs.py', 'RERE'])

# Run verification
subprocess.run(['python', 'verify_deployment.py'])
EOF

chmod +x $TEMP_DIR/run_import.py

# Step 3: Create archive for upload
echo -e "\n[Step 3] Creating archive..." | tee -a $LOG_FILE
cd $TEMP_DIR
tar -czf mcq_deployment.tar.gz *
cd -

# Step 4: Upload files to Heroku
echo -e "\n[Step 4] Uploading files to Heroku..." | tee -a $LOG_FILE

# Using a direct approach with Heroku CLI
heroku run bash -a $APP_NAME << EOF
cd /app
mkdir -p mcq_deployment
cd mcq_deployment
# Download the files (you'll need to host them somewhere accessible)
# For now, we'll use the direct import approach
EOF

# Alternative approach: Split the import into smaller chunks
echo -e "\n[Step 5] Running import in batches..." | tee -a $LOG_FILE

# Process each file individually
for json_file in "$RERE_DIR"/*.json; do
    filename=$(basename "$json_file")
    echo "Processing $filename..." | tee -a $LOG_FILE
    
    # Create a temporary script for this file
    cat > /tmp/import_${filename%.json}.py << EOF
import os
import sys
import json

# Read the JSON data
json_data = '''$(cat "$json_file")'''
data = json.loads(json_data)

# Django setup
sys.path.append('/app/django_neurology_mcq')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
import django
django.setup()

# Run import
from heroku_import_rere_mcqs import REREImporter
importer = REREImporter('/tmp')

# Save temporary file
with open('/tmp/${filename}', 'w') as f:
    json.dump(data, f)

# Import this file
importer.import_file('/tmp/${filename}')
EOF

    # Upload and run this script
    heroku run python -a $APP_NAME < /tmp/import_${filename%.json}.py 2>&1 | tee -a $LOG_FILE
    
    # Small delay between files
    sleep 2
done

# Step 6: Final verification
echo -e "\n[Step 6] Running final verification..." | tee -a $LOG_FILE
heroku run python verify_deployment.py -a $APP_NAME 2>&1 | tee -a $LOG_FILE

echo -e "\nDeployment completed at: $(date)" | tee -a $LOG_FILE

# Cleanup
rm -rf $TEMP_DIR
rm -f /tmp/import_*.py

echo -e "\nView the log file: $LOG_FILE"