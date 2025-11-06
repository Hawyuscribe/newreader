# MCQ Upload Tools

## Overview

These tools facilitate the uploading of MCQ data to the Heroku application. They handle all specific requirements, including:

- Setting verified answers as the correct answers
- Including verification reasons in the explanation sections
- Categorizing MCQs based on subspecialty
- Assigning proper examination type and year (from filenames)
- Preserving all structured explanation sections

## Available Tools

### 1. `verify_setup.py`

This script verifies that your environment is properly set up for uploading MCQs:

- Checks if GitHub CLI is installed and authenticated
- Verifies that Heroku CLI is installed and authenticated
- Confirms the chunks directory exists and contains the expected files

```bash
./verify_setup.py
```

### 2. `test_sample_upload.py`

Tests the upload process by uploading a small sample chunk and verifying that all requirements are met:

- Selects the smallest chunk file for testing
- Creates a GitHub Gist for the file
- Uploads it to Heroku
- Validates that all required fields are properly processed

```bash
./test_sample_upload.py
```

### 3. `upload_single_chunk.py`

Uploads a single specified chunk file:

- Creates a GitHub Gist for the specified chunk
- Uploads it to Heroku
- Validates the upload

```bash
./upload_single_chunk.py Promotion_2022_chunk_1_of_3.json
```

### 4. `create_progress_tracker.py`

Creates a progress tracking file to help organize the upload process:

- Generates a markdown file with all chunks listed
- Groups chunks by exam type and year
- Provides a recommended upload order (smallest to largest)

```bash
./create_progress_tracker.py
```

### 5. `automate_upload.py`

Automates the upload of all chunk files:

- Processes chunks in the recommended order (smallest to largest)
- Creates GitHub Gists for each chunk
- Uploads each chunk to Heroku
- Validates each upload
- Tracks progress in a log file and progress tracker

```bash
./automate_upload.py
```

## Usage Workflow

The recommended workflow for uploading MCQs is:

1. **Setup Verification:**
   ```bash
   ./verify_setup.py
   ```

2. **Create Progress Tracker:**
   ```bash
   ./create_progress_tracker.py
   ```

3. **Test Sample Upload:**
   ```bash
   ./test_sample_upload.py
   ```

4. **Begin Manual or Automated Uploading:**
   - For manual uploads of specific chunks:
     ```bash
     ./upload_single_chunk.py Promotion_2022_chunk_1_of_3.json
     ```
   - For automated uploading of all chunks:
     ```bash
     ./automate_upload.py
     ```

5. **Monitor Progress:**
   - Check the generated log files
   - Review `upload_progress.md` for a summary of upload status

## Requirements

- GitHub CLI (`gh`) installed and authenticated
- Heroku CLI installed and authenticated
- Access to the Heroku app `radiant-gorge-35079`
- Python 3.6+

## Validation Process

Each upload includes validation to ensure that:

1. MCQs are properly imported with verified answers as correct
2. Explanation sections are preserved
3. Subspecialty categorization is applied
4. Exam types and years are correctly assigned

For detailed information about how the import process handles these requirements, see `MCQ_IMPORT_REQUIREMENTS.md`.