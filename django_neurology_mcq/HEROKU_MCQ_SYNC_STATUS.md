# Heroku MCQ Sync Status

## Summary

The Heroku database currently contains more MCQs than expected because old MCQs were not properly cleared before importing the new ones. 

### Expected vs Actual MCQ Counts

**Expected (from local database):**
- Total: 2,853 MCQs
- Neuromuscular: 483
- Vascular Neurology/Stroke: 439
- Neuroimmunology: 299
- Epilepsy: 284
- Movement Disorders: 269

**Actual on Heroku (showing excess):**
- Movement Disorders: 594 (should be 269)
- Vascular Neurology/Stroke: 760 (should be 439)
- Neuromuscular: 659 (should be 483)
- Total: ~5,436 MCQs (should be 2,853)

## Completed Actions

1. **Updated MCQ template** - The explanation sections now match the new MCQ format with proper field names
2. **Created sync files** - Generated 29 JSON chunks containing all 2,853 MCQs
3. **Deployed sync tools** - Added `load_sync_chunks` management command to Heroku

## Next Steps

To properly sync the MCQs:

1. **Clear the database** - Run on Heroku:
   ```bash
   heroku run "python manage.py reset_to_new_mcqs" --app radiant-gorge-35079
   ```

2. **Load the new MCQs** - Run on Heroku:
   ```bash
   heroku run "python manage.py load_sync_chunks" --app radiant-gorge-35079
   ```

3. **Verify the counts** - Check that totals match expected values

## Alternative Approach

If the above commands timeout, you can use the Django admin interface:
1. Login to https://radiant-gorge-35079-2b52ba172c1e.herokuapp.com/admin/
2. Go to MCQs section
3. Select all and delete
4. Then run the import command

## Notes

- The dashboard shows "0 / X MCQs completed" because it tracks progress using Flashcard records, not MCQ counts
- All 2,853 MCQs have the proper explanation structure including the new `follow_up_guidelines` field
- The template has been updated to display all explanation sections correctly