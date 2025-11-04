# MCQ Explanation Management

This document outlines how to manage MCQ explanations in the Neurology MCQ database.

## Importing MCQs with Explanations

To import MCQs with explanations, use the `import_complete_mcqs.py` script which handles both MCQs and their explanations in a single process.

### Usage

```bash
python import_complete_mcqs.py [options]
```

#### Options:

- `--subspecialty SUBSPECIALTY`: Process only a specific subspecialty (e.g., "Pediatric Neurology")
- `--file FILENAME`: Process only a specific file (e.g., "Pediatric_Neurology.json")

#### Examples:

Import all MCQs and explanations from all JSON files:
```bash
python import_complete_mcqs.py
```

Import MCQs from a specific subspecialty:
```bash
python import_complete_mcqs.py --subspecialty "Headache"
```

Import from a specific file:
```bash
python import_complete_mcqs.py --file "Neuroanatomy.json"
```

### JSON File Structure

The expected structure of the JSON files is:

```json
{
  "source_file": "Subspecialty.txt",
  "created": "2025-05-08T01:59:21",
  "last_updated": "2025-05-08T02:21:51",
  "question_count": 310,
  "questions": [
    {
      "original_question": "Original question text...",
      "processed_question": "Processed question text...",
      "options": [
        "A. Option A [CORRECT]",
        "B. Option B",
        "C. Option C",
        "D. Option D"
      ],
      "correct_answer": "A. Option A",
      "explanation": {
        "Conceptual Framework & Clinical Context": "Content...",
        "Evidence-Based Analysis": "Content...",
        "Incorrect Options Analysis": "Content...",
        "Comparison Table": "Content...",
        "Clinical Pearls": "Content..."
        // Other sections...
      },
      "exam_type": "Part I",
      "year": "2022",
      "source": "Source text...",
      "question_number": "42"
    },
    // More questions...
  ]
}
```

## Updating Explanations Only

If you need to update explanations for existing MCQs, use the `update_mcq_explanations.py` script.

### Usage

```bash
python update_mcq_explanations.py [options]
```

#### Options:

- `--test`: Run in test mode with a limited set of files
- `--subspecialty SUBSPECIALTY`: Process only a specific subspecialty (e.g., "Pediatric Neurology")

#### Examples:

Update all explanations:
```bash
python update_mcq_explanations.py
```

Test with a small subset:
```bash
python update_mcq_explanations.py --test
```

Update a specific subspecialty:
```bash
python update_mcq_explanations.py --subspecialty "Headache"
```

## Fixing Unmatched MCQs

If some MCQs weren't matched correctly during the update process, use the `fix_unmatched_mcqs.py` script which employs more aggressive text matching.

### Usage

```bash
python fix_unmatched_mcqs.py
```

This script focuses on the subspecialties with the most matching issues.

## Explanation Format

The explanations are formatted in Markdown with specific sections ordered in a consistent way:

1. Conceptual Framework & Clinical Context
2. Evidence-Based Analysis
3. Incorrect Options Analysis
4. Comparison Table
5. Clinical Pearls
6. Common Pitfalls and Misconceptions
7. Latest Guidelines and Trials
8. Neuroanatomical Correlations
9. Pathophysiology Breakdown
10. Board Examination Focus

Additional sections are included after these priority sections.

## Fixing MCQ Option Formatting

Some MCQs have improperly formatted options where all options are merged into a single string. The `fix_question_format.py` script addresses this issue.

### Usage

```bash
python fix_question_format.py [options]
```

#### Options:

- `--test`: Run in test mode (no changes saved to database)
- `--limit NUMBER`: Limit processing to a specified number of MCQs (for testing)

#### Examples:

Run in test mode to see what changes would be made:
```bash
python fix_question_format.py --test
```

Fix a limited number of MCQs for testing:
```bash
python fix_question_format.py --test --limit 50
```

Fix all MCQs with merged options:
```bash
python fix_question_format.py
```

### Example of Fixed Options

Before:
```json
{
  "A": "Abnormal pulmonary function test \nB. Neurogenic change in EMG \nC. Elevated serum creatine kinase \nD. Demyelinating sensory neuropathy"
}
```

After:
```json
{
  "A": "Abnormal pulmonary function test", 
  "B": "Neurogenic change in EMG", 
  "C": "Elevated serum creatine kinase", 
  "D": "Demyelinating sensory neuropathy"
}
```

## Logs and Statistics

All scripts generate detailed logs and statistics in the `logs/` directory. These include:

- Number of MCQs processed
- Number of MCQs updated or created
- Matching methods used
- Errors encountered
- Processing time

Check these logs for detailed information about each import or update process.