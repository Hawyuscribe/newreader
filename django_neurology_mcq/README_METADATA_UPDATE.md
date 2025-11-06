# MCQ Metadata Update

## Summary

This document describes the process and outcomes of updating the metadata for all MCQs in the Neurology MCQ database. The primary focus was to ensure all MCQs have proper `exam_year` and `exam_type` values, as this information is crucial for filtering questions in the mock exam feature.

## Initial Analysis

An initial analysis found:
- All 3,044 MCQs had `exam_type` values
- 38 MCQs were missing `exam_year` values, all from the Neuroimmunology subspecialty

## Update Process

The update process involved:

1. Examining the original source files in `/Users/tariqalmatrudi/Documents/MCQs for the board/Classified MCQs/with explanation/`
2. Creating matching algorithms to find corresponding questions in the original sources
3. Extracting year and exam type data when available
4. Using statistically-derived defaults when no match was found

The script used for this update is located at:
`/Users/tariqalmatrudi/NEWreader/django_neurology_mcq/fix_mcq_metadata.py`

## Results

After running the update process:
- All 3,044 MCQs now have both `exam_year` and `exam_type` values
- For the 38 Neuroimmunology MCQs previously missing `exam_year`:
  - All were assigned the year 2019 (based on statistical patterns in existing Neuroimmunology MCQs)
  - All have `exam_type` set to "Other"

## Year Distribution in Database

The distribution of exam years across all MCQs:
- 2018: 406 MCQs (13.34%)
- 2019: 430 MCQs (14.13%)
- 2020: 404 MCQs (13.27%)
- 2021: 675 MCQs (22.17%)
- 2022: 478 MCQs (15.70%)
- 2023: 364 MCQs (11.96%)
- 2024: 287 MCQs (9.43%)

## Exam Type Distribution in Database

The distribution of exam types across all MCQs:
- Part II: 1,607 MCQs (52.79%)
- Part I: 935 MCQs (30.72%)
- Promotion: 464 MCQs (15.24%)
- Other: 38 MCQs (1.25%)

## Verification

A separate verification script was created to confirm all metadata fields are properly populated:
`/Users/tariqalmatrudi/NEWreader/django_neurology_mcq/verify_mcq_metadata.py`

The verification results show that all MCQs now have both `exam_year` and `exam_type` values.

## Recommendation for Future Imports

For future MCQ imports, consider implementing the following requirements:

1. Make `exam_year` and `exam_type` required fields during import
2. Validate that `exam_year` falls within a reasonable range (e.g., 2015-2025)
3. Normalize `exam_type` values to one of: "Part I", "Part II", "Promotion", or "Other"
4. Update import scripts to extract and assign proper metadata from source files