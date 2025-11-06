# MCQ Import Commands

This directory contains Python commands for importing MCQs into Heroku.

## How to use these commands

1. Open the Heroku dashboard: https://dashboard.heroku.com/apps/radiant-gorge-35079
2. Go to the 'More' dropdown and select 'Run Console'
3. Start a Python console: `python manage.py shell`
4. Copy and paste the contents of each file into the console in order:
   - First, run the clear command: `00_clear_all_mcqs.py`
   - Then run each import command in numerical order
   - Finally, run the verify command: `99_verify_import.py`

## Tips

- Copy the entire file content at once, the shell can handle multiple line inputs
- Wait for each command to complete before running the next one
- If you encounter errors, check the console output for details
