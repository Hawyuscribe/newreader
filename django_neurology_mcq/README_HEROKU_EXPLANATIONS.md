# MCQ Explanation Transfer to Heroku

This document explains how to transfer MCQ explanations from your local SQLite database to the Heroku PostgreSQL database.

## Overview

The process involves:
1. Exporting explanations from the local database
2. Splitting them by subspecialty 
3. Uploading them to Heroku in batches
4. Verifying the updates

## Prerequisites

- Heroku CLI installed and logged in
- Python 3.x
- Required Python packages: psycopg2-binary, requests
- Access to both local and Heroku databases

## Step 1: Export Explanations

```bash
# Export all explanations from local database by subspecialty
python export_explanations_by_subspecialty.py
```

This creates JSON files in the `explanation_exports` directory, one for each subspecialty.

## Step 2: Update Heroku Database

### Option 1: Update a Single Subspecialty

```bash
# Update a single subspecialty
python update_fast.py --file explanation_exports/Epilepsy_explanations_TIMESTAMP.json --subspecialty "Epilepsy" --batch-size 20 --pause 2
```

Parameters:
- `--file`: Path to the exported JSON file
- `--subspecialty`: Name of the subspecialty (for reporting)
- `--batch-size`: Number of MCQs to update in each batch (default: 20)
- `--pause`: Seconds to pause between batches (default: 2)
- `--log-file`: Optional path to save execution log

### Option 2: Update All Subspecialties

```bash
# Update all subspecialties in sequence
./update_remaining.sh
```

This script:
- Processes all subspecialties in a predefined order
- Adjusts batch size and pause times based on subspecialty size
- Logs results for each subspecialty
- Creates a summary of all updates

## Step 3: Verify Updates

```bash
# Check the status of explanations on Heroku
python verify_heroku_update.py
```

This script:
- Connects to the Heroku database
- Checks how many MCQs have proper explanations vs placeholders
- Shows progress by subspecialty
- Saves verification results to a JSON file

## Troubleshooting

If you encounter issues:

1. **Database Connection Errors**:
   - Ensure Heroku CLI is logged in (`heroku login`)
   - Check your DATABASE_URL (`heroku config:get DATABASE_URL`)

2. **Timeout Errors**:
   - Decrease batch size (e.g., `--batch-size 10`)
   - Increase pause time (e.g., `--pause 5`)

3. **Script Execution Errors**:
   - Check the logs directory for detailed error information
   - Verify Python environment has required packages

## Performance Considerations

- Larger subspecialties (400+ MCQs) may need smaller batch sizes
- If Heroku dynos are sleeping, the first batch may take longer
- The entire process for all subspecialties can take 30-60 minutes

## Completion Verification

After running all updates, run the verification script again to ensure all explanations have been properly transferred.