# Database Migration Guide

This document explains how to transfer MCQ data between environments, particularly from local development to Heroku deployment, and handle common issues like primary key conflicts.

## Overview

The Django Neurology MCQ application uses SQLite for local development and PostgreSQL on Heroku. This migration guide provides instructions for:

1. Exporting MCQs from the local SQLite database
2. Breaking exports into manageable chunks
3. Importing MCQs to the Heroku PostgreSQL database
4. Handling primary key conflicts during fixture imports
5. Verifying successful import

## Available Scripts

The following scripts are available to help with the migration process:

- **`export_mcqs_chunked.py`**: Exports all MCQs from the local database and splits them into manageable chunks
- **`import_data_to_heroku.sh`**: Handles the full import process including uploading chunks to Heroku
- **`verify_mcq_import.py`**: Django management command to verify the import status

## Export Process

The export process extracts MCQs from the local SQLite database and creates JSON files:

```bash
# Run the export script
python export_mcqs_chunked.py
```

This will:
- Connect to the local SQLite database
- Extract all MCQs
- Process and normalize the data
- Split MCQs into chunks of 500 (configurable)
- Save each chunk as a separate JSON file in the `mcq_exports` directory
- Create a manifest file with metadata about the export

## Import Process

To import the MCQs to Heroku:

```bash
# Edit the script to set your Heroku app name
nano import_data_to_heroku.sh

# Run the import script
./import_data_to_heroku.sh
```

This will:
1. Run the export script locally if not already done
2. Upload all chunk files to Heroku
3. Run the import command on Heroku to process all chunks
4. Verify the import results

## Manual Import

If you need more control over the import process, you can run the commands manually:

```bash
# On your local machine
python export_mcqs_chunked.py

# Upload files to Heroku (replace YOUR_APP_NAME)
heroku run "mkdir -p /app/mcq_exports" --app YOUR_APP_NAME
heroku run "cat > /app/mcq_exports/mcqs_chunk_1_of_X.json" --app YOUR_APP_NAME < mcq_exports/mcqs_chunk_1_of_X.json

# Import on Heroku (replace YOUR_APP_NAME)
heroku run "cd django_neurology_mcq && python manage.py import_mcqs_chunked /app/mcq_exports" --app YOUR_APP_NAME
```

## Verification

To verify the import was successful:

```bash
# On Heroku (replace YOUR_APP_NAME)
heroku run "cd django_neurology_mcq && python manage.py verify_mcq_import --detailed" --app YOUR_APP_NAME
```

This will show:
- Total number of MCQs in the database
- Percentage of MCQs with subspecialties and explanations
- Detailed breakdown by subspecialty, exam type, and year (with --detailed flag)
- Any issues or warnings about the data

## Handling Primary Key Conflicts

When loading MCQ fixtures, you may encounter an issue where not all MCQs are loaded (e.g., expected 3153 but only 2379 were loaded). This is likely due to duplicate primary keys in the fixture file.

### Detecting PK Conflicts

The system will now automatically detect when not all MCQs are loaded and log a warning:

```
Not all MCQs were loaded. Expected: 3153, Loaded: 2379. 
This is likely due to primary key conflicts in the fixture file.
```

### Fixing PK Conflicts

A utility script is provided to fix primary key conflicts:

```bash
# From the project root directory
python fix_pk_conflicts.py
```

This script will:
1. Identify duplicate primary keys in the fixture file
2. Assign new unique primary keys to resolve conflicts
3. Create a fixed fixture file (`all_mcqs_fixed.json`)

After running this script, replace the original fixture file with the fixed one:

```bash
# From the project root directory
cd django_neurology_mcq/fixtures/mcqs
cp all_mcqs.json all_mcqs.json.backup  # Create a backup first
cp all_mcqs_fixed.json all_mcqs.json
```

Then load the fixed fixture:

```bash
# From the django_neurology_mcq directory
python manage.py load_mcq_fixtures --all --clear
```

## Troubleshooting

### Missing MCQs

If some MCQs are missing after import:
1. Check the export and import logs for errors
2. Verify the total count matches between environments
3. Try importing individual chunks that may have failed
4. **Check for primary key conflicts** (see "Handling Primary Key Conflicts" section)

### Database Performance

If the database becomes slow after importing many MCQs:
1. Ensure proper indexes are in place
2. Consider optimizing queries in views
3. Implement caching for frequently accessed questions

### Import Failures

If the import process fails:
1. Check Heroku logs for errors
2. Verify database connection and permissions
3. Try reducing the batch size in the import command
4. Import individual chunk files instead of the entire dataset at once

## Additional Notes

- The chunked approach helps avoid Heroku timeouts and memory limits
- Consider using Heroku Scheduler for large imports that might exceed the 30-minute request limit
- Always backup your data before attempting large migrations
- For extremely large datasets, consider using Heroku's pgbackups to directly clone the database