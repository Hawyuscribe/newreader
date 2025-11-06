# Importing New MCQ Format with Structured Explanations

This guide explains how to import MCQs with the new structured explanation format into your Neurology MCQ application, both locally and on Heroku.

## New MCQ Format Overview

The new MCQ format includes structured explanation sections instead of a single explanation field. The primary enhancements are:

1. **Structured Explanation Sections**: Explanation is divided into meaningful sections like:
   - `conceptual_foundation`
   - `pathophysiological_mechanisms`
   - `clinical_correlation` 
   - `differential_diagnosis`
   - `option_analysis`
   - `management_principles`
   
2. **Enhanced Metadata Fields**:
   - `verification_confidence`: Confidence level in the verified answer
   - `primary_category` and `secondary_category`: More specific categorization
   - `key_concept`: The core concept tested in the question
   - `difficulty_level`: The difficulty rating of the question
   
## JSON Format Example

```json
{
  "mcqs": [
    {
      "question_number": "Q1",
      "question_text": "A 25-year-old woman presents with optic neuritis...",
      "options": [
        {"letter": "A", "text": "Multiple Sclerosis"},
        {"letter": "B", "text": "Neuromyelitis Optica"},
        {"letter": "C", "text": "Acute Disseminated Encephalomyelitis"},
        {"letter": "D", "text": "Vitamin B12 Deficiency"}
      ],
      "correct_answer": "A",
      "verified_answer": "A",
      "verification_confidence": "high",
      "primary_category": "Demyelinating/Multiple Sclerosis",
      "secondary_category": "Neuroimmunology",
      "key_concept": "Clinical presentation and MRI findings of multiple sclerosis",
      "difficulty_level": "Basic",
      "subspecialty": "Neuroimmunology",
      "explanation_sections": {
        "conceptual_foundation": "Demyelinating disorders are characterized by...",
        "pathophysiological_mechanisms": "MS is an immune-mediated disorder...",
        "clinical_correlation": "Optic neuritis is one of the most common...",
        "option_analysis": "Option A (Multiple Sclerosis): Correct..."
      }
    }
  ]
}
```

## Local Import Instructions

To import MCQs locally with the new format:

1. Ensure your JSON file follows the format shown above
2. Run the import script:

```bash
python import_new_mcq_format.py /path/to/your/mcqs_file.json --force
```

The `--force` flag skips the confirmation prompt and directly proceeds with deletion of existing MCQs.

## Heroku Import Instructions

### Method 1: Using Sample Data (for testing)

If you want to test with sample data before importing your actual MCQs:

```bash
heroku run python update_heroku_directly.py sample -a your-heroku-app-name
```

This will import 3 sample MCQs with the new format structure.

### Method 2: Using URL Import (recommended for production)

The most reliable way to import MCQs on Heroku is using the URL-based import:

1. Host your JSON file in a publicly accessible location (GitHub, S3, etc.)
2. Run the import command:

```bash
heroku run python update_heroku_directly.py url https://url-to-your-mcqs-file.json -a your-heroku-app-name
```

For example:
```bash
heroku run python update_heroku_directly.py url https://raw.githubusercontent.com/username/repo/main/mcqs_data.json -a radiant-gorge-35079
```

### Method 3: Validation Only

To validate the existing MCQs on Heroku without importing new ones:

```bash
heroku run python update_heroku_directly.py validate -a your-heroku-app-name
```

## Important Notes

1. **Backup Your Data**: The import process replaces all existing MCQs. Always backup your data before importing.

2. **File Size Limits**: For large MCQ datasets, consider breaking your JSON file into smaller chunks and importing each separately to avoid timeouts on Heroku.

3. **Filename Detection**: The script attempts to detect exam type and year from the filename:
   - `Part I`, `part i`, or `part 1` in the filename → `Part I` exam type
   - `Part II`, `part ii`, or `part 2` in the filename → `Part II` exam type
   - `Promotion` in the filename → `Promotion` exam type
   - `ABPN` in the filename → `ABPN Board` exam type
   - Four-digit year (like `2023`) → sets the exam year

4. **Subspecialty Handling**: The script uses:
   - The `subspecialty` field if available
   - Falls back to the `primary_category` field if `subspecialty` is not provided
   - Replaces underscores with spaces for better display

5. **Correct Answer Priority**: The script uses:
   - `verified_answer` if available
   - Falls back to `correct_answer` if `verified_answer` is not provided

## Troubleshooting

1. **View Logs**: If you encounter issues, check the logs:
   ```bash
   heroku logs -a your-heroku-app-name
   ```

2. **Validation Report**: The script runs a validation after import to check for issues:
   ```bash
   heroku run python update_heroku_directly.py validate -a your-heroku-app-name
   ```

3. **Common Issues**:
   - **Timeout**: Heroku has a 30-second timeout for dyno operations. For large imports, consider using smaller batches.
   - **JSON Format**: Ensure your JSON is valid and follows the expected structure.
   - **URL Access**: Ensure the URL with your JSON data is publicly accessible.

## Support

For additional help, contact the development team or refer to the Django MCQ Reader documentation.