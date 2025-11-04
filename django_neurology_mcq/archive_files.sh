#!/bin/bash
# Script to archive and remove temporary files

# Create archive subdirectories
mkdir -p archive/analysis
mkdir -p archive/fixes
mkdir -p archive/checks
mkdir -p archive/imports
mkdir -p archive/tests
mkdir -p archive/exports
mkdir -p archive/misc

# 1. Temporary Analysis Scripts
echo "Moving analysis scripts..."
mv analyze_explanations.py archive/analysis/ 2>/dev/null
mv analyze_inconclusive_examples.py archive/analysis/ 2>/dev/null
mv analyze_inconclusive_mcqs.py archive/analysis/ 2>/dev/null
mv analyze_mcq_metadata.py archive/analysis/ 2>/dev/null
mv analyze_mcqs.py archive/analysis/ 2>/dev/null
mv analyze_missing_exam_year.py archive/analysis/ 2>/dev/null
mv analyze_placeholders.py archive/analysis/ 2>/dev/null
mv sample_comparison.py archive/analysis/ 2>/dev/null
mv simple_comparison.py archive/analysis/ 2>/dev/null
mv extract_and_compare_mcqs.py archive/analysis/ 2>/dev/null
mv combine_results.py archive/analysis/ 2>/dev/null
mv identify_missing_mcqs.py archive/analysis/ 2>/dev/null
mv improved_extraction.py archive/analysis/ 2>/dev/null
mv process_all_questions.py archive/analysis/ 2>/dev/null

# 2. One-time Fix Scripts
echo "Moving fix scripts..."
mv fix_all_explanations.py archive/fixes/ 2>/dev/null
mv fix_all_subspecialty_explanations.py archive/fixes/ 2>/dev/null
mv fix_correct_answers.py archive/fixes/ 2>/dev/null
mv fix_explanation_json.py archive/fixes/ 2>/dev/null
mv fix_explanation_placeholders.py archive/fixes/ 2>/dev/null
mv fix_explanations_by_subspecialty.py archive/fixes/ 2>/dev/null
mv fix_heroku_explanations.py archive/fixes/ 2>/dev/null
mv fix_placeholder_direct.py archive/fixes/ 2>/dev/null
mv fix_placeholder_questions.py archive/fixes/ 2>/dev/null
mv fix_placeholder_questions_improved.py archive/fixes/ 2>/dev/null
mv fix_question_format.py archive/fixes/ 2>/dev/null
mv fix_remaining_placeholders.py archive/fixes/ 2>/dev/null
mv fix_specific_mismatches.py archive/fixes/ 2>/dev/null
mv fix_subspecialty_explanations.py archive/fixes/ 2>/dev/null
mv fix_unmatched_mcqs.py archive/fixes/ 2>/dev/null
mv mcq/fixed_views.py archive/fixes/ 2>/dev/null
mv mcq/views.py.broken archive/fixes/ 2>/dev/null
mv force_explanation_styling.py archive/fixes/ 2>/dev/null
mv format_all_explanations.py archive/fixes/ 2>/dev/null
mv format_missing_mcqs.py archive/fixes/ 2>/dev/null
mv fix_mcq_metadata.py archive/fixes/ 2>/dev/null
mv fix_neuroimmunology_metadata_properly.py archive/fixes/ 2>/dev/null
mv fix_neuroimmunology_years.py archive/fixes/ 2>/dev/null
mv assign_neuroimmunology_metadata.py archive/fixes/ 2>/dev/null

# 3. One-time Check Scripts
echo "Moving check scripts..."
mv check_correct_answers.py archive/checks/ 2>/dev/null
mv check_explanation_status.py archive/checks/ 2>/dev/null
mv check_explanations_by_subspecialty.py archive/checks/ 2>/dev/null
mv check_explanations.py archive/checks/ 2>/dev/null
mv check_heroku_explanations.py archive/checks/ 2>/dev/null
mv check_heroku_explanations_direct.py archive/checks/ 2>/dev/null
mv check_incorrect_options.py archive/checks/ 2>/dev/null
mv check_mcq_counts.py archive/checks/ 2>/dev/null
mv check_mcqs.py archive/checks/ 2>/dev/null
mv check_question_options.py archive/checks/ 2>/dev/null
mv check_specific_mcqs.py archive/checks/ 2>/dev/null
mv verify_fixes.py archive/checks/ 2>/dev/null
mv verify_heroku_explanations.py archive/checks/ 2>/dev/null
mv verify_heroku_update.py archive/checks/ 2>/dev/null
mv verify_mcq_metadata.py archive/checks/ 2>/dev/null
mv verify_mcqs.py archive/checks/ 2>/dev/null
mv heroku_check_script.py archive/checks/ 2>/dev/null
mv heroku_verify.py archive/checks/ 2>/dev/null
mv count_mcqs_by_subspecialty.py archive/checks/ 2>/dev/null

# 4. Duplicate/Older Import Scripts
echo "Moving import scripts..."
mv import_all_explanations.py archive/imports/ 2>/dev/null
mv import_all_missed_explanations.py archive/imports/ 2>/dev/null
mv import_explanations_direct.py archive/imports/ 2>/dev/null
mv import_explanations_improved.py archive/imports/ 2>/dev/null
mv import_explanations_special.py archive/imports/ 2>/dev/null
mv import_explanations.py archive/imports/ 2>/dev/null
mv import_mcqs.py archive/imports/ 2>/dev/null
mv import_mcqs_enhanced.py archive/imports/ 2>/dev/null
mv import_mcqs_with_explanations.py archive/imports/ 2>/dev/null
mv import_heroku_simple.py archive/imports/ 2>/dev/null
mv import_heroku_explanations.py archive/imports/ 2>/dev/null
mv import_all_specialties.py archive/imports/ 2>/dev/null
mv import_custom_mcqs.py archive/imports/ 2>/dev/null
mv import_complete_mcqs.py archive/imports/ 2>/dev/null
mv import_explanations_from_source.py archive/imports/ 2>/dev/null
mv import_explanations_heroku.py archive/imports/ 2>/dev/null
mv import_full_explanations.py archive/imports/ 2>/dev/null
mv import_mcqs_with_structured_explanations.py archive/imports/ 2>/dev/null
mv improved_import.py archive/imports/ 2>/dev/null

# 5. Export Scripts
echo "Moving export scripts..."
mv export_explanations.py archive/exports/ 2>/dev/null
mv export_explanations_by_subspecialty.py archive/exports/ 2>/dev/null
mv export_heroku_explanations.py archive/exports/ 2>/dev/null
mv export_mcq_questions.py archive/exports/ 2>/dev/null
mv export_pdf_questions.py archive/exports/ 2>/dev/null
mv export_sample_mcqs.py archive/exports/ 2>/dev/null

# 6. Test Files and Examples
echo "Moving test files..."
mv create_test_file.py archive/tests/ 2>/dev/null
mv test_case_insensitive_login.py archive/tests/ 2>/dev/null
mv test_explanation.py archive/tests/ 2>/dev/null

# 7. Other Miscellaneous Files
echo "Moving miscellaneous files..."
mv create_detailed_explanations.py archive/misc/ 2>/dev/null
mv create_exam_year_update_script.py archive/misc/ 2>/dev/null
mv create_heroku_explanations.py archive/misc/ 2>/dev/null
mv compare_subspecialty_explanations.py archive/misc/ 2>/dev/null
mv split_explanations.py archive/misc/ 2>/dev/null

# Move subdirectories that are likely temporary
echo "Moving temporary directories..."
if [ -d "temp_heroku_transfer" ]; then
    mv temp_heroku_transfer archive/
fi

if [ -d "explanation_import" ]; then
    mv explanation_import archive/
fi

# Don't automatically move logs, chunks, samples and other data-containing directories
# These may need manual review

echo "Done! Files have been moved to the archive directory."
echo "Review the archive directory to ensure no critical files were moved."
echo "To delete the archived files permanently, run: rm -rf archive"