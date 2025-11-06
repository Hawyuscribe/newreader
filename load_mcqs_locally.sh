#!/bin/bash

# Local MCQ Fixture Loader with enhanced logging
# This script converts MCQs to JSON fixtures and loads them into the local database

# Configuration
SOURCE_DIR="/Users/tariqalmatrudi/Documents/MCQs for the board/Classified MCQs/reclassified"
FIXTURES_DIR="./django_neurology_mcq/fixtures/mcqs"
APP_DIR="./django_neurology_mcq"
LOGS_DIR="./logs"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
LOG_FILE="${LOGS_DIR}/mcq_import_${TIMESTAMP}.log"
IMPORT_LOG_FILE="${LOGS_DIR}/import_${TIMESTAMP}.log"
VERBOSE=true

# Ensure log directories exist
mkdir -p "$LOGS_DIR"
mkdir -p "$LOGS_DIR/mcq_conversion_logs"
mkdir -p "$LOGS_DIR/errors"

# Touch log files to ensure they exist
touch "$LOG_FILE"
touch "$IMPORT_LOG_FILE"

# Echo with timestamps to both console and log file
log() {
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

# Echo with timestamps only to log file
log_silent() {
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] $1" >> "$LOG_FILE"
    if [ "$VERBOSE" = true ]; then
        echo "[$(date +'%Y-%m-%d %H:%M:%S')] $1"
    fi
}

log "Starting Local MCQ Import Process with enhanced logging..."
log "Source directory: $SOURCE_DIR"
log "Fixtures directory: $FIXTURES_DIR"
log "Log files: $LOG_FILE and $IMPORT_LOG_FILE"

# Step 1: Set up the fixtures directory
log "Step 1: Setting up fixtures directory..."
mkdir -p "$FIXTURES_DIR"

# Step 2: Run the Python converter script with enhanced logging
log "Step 2: Converting MCQs to JSON fixtures..."
python mcq_to_json_converter_enhanced.py | tee -a "$LOG_FILE"

if [ ${PIPESTATUS[0]} -ne 0 ]; then
    log "Error: Failed to convert MCQs to JSON"
    exit 1
fi

# Make sure fixtures directory exists
if [ ! -d "$FIXTURES_DIR" ]; then
    log "Error: Fixtures directory not found: $FIXTURES_DIR"
    exit 1
fi

# Count MCQs in fixtures before loading
log "Counting MCQs in fixtures before loading..."
FIXTURE_COUNT=$(python -c "import json; f=open('$FIXTURES_DIR/all_mcqs.json'); data=json.load(f); print(len(data)); f.close()" 2>/dev/null)
if [ -z "$FIXTURE_COUNT" ]; then
    log "Error: Could not count MCQs in fixtures. File may be empty or invalid."
    FIXTURE_COUNT=0
fi
log "Found $FIXTURE_COUNT MCQs in fixtures"

# Step 3: Backup existing database
log "Step 3: Backing up existing database..."
DB_FILE="$APP_DIR/neurology_mcq.db"
if [ -f "$DB_FILE" ]; then
    BACKUP_FILE="$APP_DIR/neurology_mcq_backup_${TIMESTAMP}.db"
    cp "$DB_FILE" "$BACKUP_FILE"
    log "Database backed up to $BACKUP_FILE"
else
    log "No existing database to backup."
fi

# Step 4: Load the fixtures into the local database with detailed logging
log "Step 4: Loading fixtures into local database..."
cd "$APP_DIR"

# Activate virtual environment if it exists
if [ -f "../venv/bin/activate" ]; then
    log "Activating virtual environment..."
    source "../venv/bin/activate"
fi

# Get current MCQ count before clearing
BEFORE_COUNT=$(python manage.py shell -c "from mcq.models import MCQ; print(MCQ.objects.count())" 2>/dev/null | grep -o '[0-9]\+' | tail -1)
if [ -z "$BEFORE_COUNT" ]; then
    BEFORE_COUNT=0
fi
log "Current MCQ count before clear: $BEFORE_COUNT"

# Clear existing MCQs
log "Clearing existing MCQs..."
python manage.py load_mcq_fixtures --clear --all -v 2 | tee "$IMPORT_LOG_FILE" 2>&1
IMPORT_STATUS=$?

if [ $IMPORT_STATUS -ne 0 ]; then
    log "Warning: Import process returned non-zero status: $IMPORT_STATUS"
    log "Check import log for details: $IMPORT_LOG_FILE"
    
    # Extract error messages
    grep -i error "$IMPORT_LOG_FILE" | tee -a "$LOG_FILE"
else
    log "Import process completed with status: $IMPORT_STATUS"
fi

# Analyze import results
log "Analyzing import results..."

# Get current MCQ count after import
AFTER_COUNT=$(python manage.py shell -c "from mcq.models import MCQ; print(MCQ.objects.count())" 2>/dev/null | grep -o '[0-9]\+' | tail -1)
if [ -z "$AFTER_COUNT" ]; then
    AFTER_COUNT=0
fi
log "MCQ count after import: $AFTER_COUNT"

# Deactivate virtual environment if it was activated
if [ -n "$VIRTUAL_ENV" ]; then
    log "Deactivating virtual environment..."
    deactivate
fi

# Calculate difference and success rate
EXPECTED_COUNT=$FIXTURE_COUNT
IMPORTED_COUNT=$AFTER_COUNT
DIFFERENCE=$((EXPECTED_COUNT - IMPORTED_COUNT))

if [ $EXPECTED_COUNT -gt 0 ]; then
    SUCCESS_RATE=$(echo "scale=2; ($IMPORTED_COUNT * 100) / $EXPECTED_COUNT" | bc)
else
    SUCCESS_RATE=0
fi

log "Import statistics:"
log "  - MCQs in fixtures: $EXPECTED_COUNT"
log "  - MCQs successfully imported: $IMPORTED_COUNT"
log "  - Difference: $DIFFERENCE"
log "  - Success rate: ${SUCCESS_RATE}%"

# Get subspecialty breakdown
log "Subspecialty breakdown:"
python manage.py shell -c "from django.db.models import Count; from mcq.models import MCQ; for item in MCQ.objects.values('subspecialty').annotate(count=Count('id')).order_by('subspecialty'): print(f\"{item['subspecialty']}: {item['count']}\")" 2>/dev/null | while read line; do
    log_silent "  - $line"
done

# Check for discrepancies in subspecialty counts
log "Checking for subspecialty count discrepancies..."
python -c "
import json, os, datetime
try:
    # Load fixture stats
    with open('$FIXTURES_DIR/mcq_stats.json', 'r') as f:
        fixture_stats = json.load(f)
    
    fixture_counts = fixture_stats.get('by_subspecialty', {})
    
    # Get DB counts via Django shell
    import subprocess
    result = subprocess.run(
        ['python', 'manage.py', 'shell', '-c', 
         'from django.db.models import Count; from mcq.models import MCQ; import json; print(json.dumps(dict(MCQ.objects.values_list(\"subspecialty\", flat=True).annotate(count=Count(\"id\")).order_by(\"subspecialty\"))))'],
        capture_output=True, text=True
    )
    
    db_counts = json.loads(result.stdout.strip())
    
    # Compare counts
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f'\\n[{current_time}] Subspecialty comparison:')
    
    all_subspecialties = set(list(fixture_counts.keys()) + list(db_counts.keys()))
    discrepancies = []
    
    for subspec in sorted(all_subspecialties):
        fixture_count = fixture_counts.get(subspec, 0)
        db_count = db_counts.get(subspec, 0)
        diff = fixture_count - db_count
        
        if diff != 0:
            discrepancies.append((subspec, fixture_count, db_count, diff))
            current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f'[{current_time}] DISCREPANCY: {subspec}: Expected {fixture_count}, got {db_count}, diff: {diff}')
    
    if not discrepancies:
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f'[{current_time}] No subspecialty count discrepancies found')
    else:
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f'[{current_time}] Found {len(discrepancies)} subspecialties with count discrepancies')
        
except Exception as e:
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f'[{current_time}] Error checking subspecialty counts: {str(e)}')
" | tee -a "$LOG_FILE"

# Return to original directory
cd ..

# Check import log for specific errors
log "Analyzing import log for specific errors..."
if [ -f "$IMPORT_LOG_FILE" ]; then
    VALIDATION_ERRORS=$(grep -i "validation\|invalid\|error" "$IMPORT_LOG_FILE" | wc -l)
    INTEGRITY_ERRORS=$(grep -i "integrity\|duplicate\|unique" "$IMPORT_LOG_FILE" | wc -l)
    
    log "Import log analysis:"
    log "  - Validation errors: $VALIDATION_ERRORS"
    log "  - Integrity errors: $INTEGRITY_ERRORS"
    
    if [ $VALIDATION_ERRORS -gt 0 ] || [ $INTEGRITY_ERRORS -gt 0 ]; then
        log "Sample errors from import log:"
        grep -i "validation\|invalid\|error\|integrity\|duplicate\|unique" "$IMPORT_LOG_FILE" | head -10 | tee -a "$LOG_FILE"
    fi
else
    log "Import log file not found: $IMPORT_LOG_FILE"
fi

# Final status report
if [ $DIFFERENCE -eq 0 ]; then
    log "SUCCESS: All $IMPORTED_COUNT MCQs were successfully imported!"
    IMPORT_STATUS="SUCCESS"
elif [ $IMPORTED_COUNT -eq 0 ]; then
    log "FAILURE: No MCQs were imported!"
    IMPORT_STATUS="FAILURE"
elif [ $SUCCESS_RATE -ge 95 ]; then
    log "PARTIAL SUCCESS: $IMPORTED_COUNT of $EXPECTED_COUNT MCQs imported ($SUCCESS_RATE% success rate)."
    IMPORT_STATUS="PARTIAL"
else
    log "WARNING: Only $IMPORTED_COUNT of $EXPECTED_COUNT MCQs imported ($SUCCESS_RATE% success rate)."
    IMPORT_STATUS="WARNING"
fi

echo ""
echo "=================== IMPORT COMPLETED: $IMPORT_STATUS ==================="
echo "Your local database now contains $IMPORTED_COUNT MCQs!"
echo "Run the application with: cd $APP_DIR && python manage.py runserver"
echo "Detailed logs:"
echo "  - Main log: $LOG_FILE"
echo "  - Import log: $IMPORT_LOG_FILE"
echo "======================================================================"