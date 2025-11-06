# MCQ Data Import Guide

This guide explains how to import MCQs into the Neurology MCQ application, whether running locally or on Heroku.

## Overview

There are several ways to import data into the application:

1. **Web Interface**: Upload JSON data through the web UI (easiest)
2. **Django Management Command**: Import from the command line
3. **Export/Import Scripts**: For transferring data between environments
4. **Database Transfer**: For direct PostgreSQL database transfers

## 1. Web Interface Import

The web interface provides the simplest way to import MCQs, especially for smaller batches.

### Preparing Your Data

1. Create a JSON file with your MCQs in the following format:
   ```json
   [
     {
       "question_number": "Sample-1",
       "question_text": "A 65-year-old man presents with unilateral resting tremor...",
       "options": "{\"A\": \"Option A\", \"B\": \"Option B\", \"C\": \"Option C\", \"D\": \"Option D\"}",
       "correct_answer": "B",
       "subspecialty": "Movement Disorders",
       "source_file": null,
       "exam_type": "Sample",
       "exam_year": 2023,
       "explanation": null
     },
     // more MCQs here...
   ]
   ```

2. Make sure the options field is a properly formatted JSON string

### Import Steps

1. Log in to the application
2. Navigate to the Import page:
   - Click on the "Import" link in the navigation menu, or
   - Go directly to `/import/` 
3. Click "Choose File" and select your JSON file
4. Click "Upload" to start the import process
5. Wait for the import to complete
6. You'll be redirected to the dashboard with a success message showing how many MCQs were imported

### Notes and Limitations

- The importer will check for duplicates based on question_number and question_text
- Duplicate questions will be skipped (not overwritten)
- For large imports (1000+ MCQs), consider splitting your JSON file into smaller chunks
- Maximum upload size is typically limited to 10MB by default

## 2. Django Management Command

For larger imports, you can use the Django management command which can handle chunked files and has better error handling.

### Import Using Management Command

1. Ensure your MCQ data is formatted as JSON (same format as above)
2. Transfer the JSON file to the server (for Heroku, you'll need to create a directory on the dyno)
3. Run the import command:

```bash
# Local Development
python manage.py import_mcqs_chunked /path/to/your/data --batch-size 50

# On Heroku
heroku run "cd django_neurology_mcq && python manage.py import_mcqs_chunked /app/data --chunk-file your_data.json --batch-size 50" --app your-app-name
```

### Options

- `--batch-size`: Number of MCQs to process in a single transaction (default: 100)
- `--chunk-file`: Specific JSON file to import (otherwise imports all files in directory)

## 3. Export/Import Scripts

For transferring data between environments (e.g., from development to production), you can use the provided export and import scripts.

### Exporting MCQs from Local Database

```bash
# Run the export script
python export_mcqs_chunked.py

# This will create a directory 'mcq_exports' with:
# - mcqs_chunk_1_of_X.json, mcqs_chunk_2_of_X.json, etc.
# - export_manifest.json
```

### Importing MCQs to Heroku

```bash
# Upload test file with 100 MCQs
heroku run "mkdir -p /app/mcq_exports" --app your-app-name
heroku run "cat > /app/mcq_exports/test_mcqs.json" --app your-app-name < test_100_mcqs.json

# Import the MCQs
heroku run "cd django_neurology_mcq && python manage.py import_mcqs_chunked /app/mcq_exports --chunk-file test_mcqs.json" --app your-app-name
```

### Using the Automated Scripts

For full automation, you can use:

1. `export_mcqs_chunked.py`: Exports all MCQs to chunked JSON files
2. `upload_chunk_to_heroku.py`: Uploads a specific chunk to Heroku
3. `upload_all_chunks.sh`: Orchestrates the upload of all chunks

## 4. Verifying Your Import

After importing, verify that your data was imported correctly:

```bash
# On local development
python manage.py verify_mcq_import --detailed

# On Heroku
heroku run "cd django_neurology_mcq && python manage.py verify_mcq_import --detailed" --app your-app-name
```

This will display:
- Total number of MCQs
- Breakdown by subspecialty
- Breakdown by exam type
- Breakdown by exam year

## Troubleshooting

### Common Issues

1. **JSON Format Issues**: Ensure your JSON is valid and properly formatted
   - Validate using a tool like [JSONLint](https://jsonlint.com/)

2. **Duplicate MCQs**: Duplicate MCQs are skipped, not updated
   - Check import messages for "already existing" counts

3. **Import Timing Out**: For very large imports
   - Use chunked imports with smaller batch sizes
   - Increase your Heroku dyno size temporarily

4. **Missing Fields**: Required fields include:
   - question_text
   - options
   - correct_answer