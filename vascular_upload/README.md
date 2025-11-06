# Vascular MCQ Upload to Heroku

This package contains scripts and data for uploading vascular neurology MCQs to the Heroku app.

## Files

- `chunks/`: Directory containing MCQ chunks in JSON format
- `import_mcqs.py`: Python script for importing MCQs into Django
- `fix_heroku_app.sh`: Script to fix and configure the Heroku app
- `upload_to_heroku.sh`: Script to upload MCQs to Heroku
- `preparation_20250520_184259.log`: Log file from the preparation process

## Instructions

1. First, run the fix script to ensure the Heroku app is properly configured:

```bash
./fix_heroku_app.sh
```

2. Then, run the upload script to import the MCQs:

```bash
./upload_to_heroku.sh
```

3. Monitor the progress in the terminal or check the log files:

```bash
tail -f upload.log
```

## Details

- Total MCQs: 406
- Chunk size: 20 MCQs per chunk
- Heroku app: mcq-reader

## Notes

- The upload script processes one chunk at a time
- There's a 5-second pause between chunks to avoid overloading the server
- If the upload is interrupted, you can restart it, and duplicate MCQs will be skipped

Created on: 2025-05-20 18:42:59
