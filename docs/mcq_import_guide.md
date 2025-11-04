# MCQ Import Guide

This guide explains how to use the JSON fixtures approach to preload MCQs into your Neurology MCQ application.

## Overview

The application is now designed to automatically load MCQs from JSON fixtures. This approach has several advantages:

1. **Preloaded Data**: MCQs are bundled with the application code, making deployment simpler
2. **Version Control**: MCQs can be tracked in version control
3. **Consistent Data**: Everyone using the application gets the same set of MCQs
4. **Faster Deployment**: No need to upload MCQs separately after deployment

## Directory Structure

The fixtures are organized as follows:

```
django_neurology_mcq/
  fixtures/
    mcqs/
      all_mcqs.json               # All MCQs combined in one file
      Critical_Care_Neurology.json # MCQs for specific subspecialty
      Dementia.json
      ... (other subspecialties) ...
      mcq_stats.json              # Statistics about the MCQs
```

## Importing MCQs Locally

To convert MCQs from text files and load them into your local database:

1. Make sure your text files are in the correct format in the configured directory
2. Run the provided script:

```bash
./load_mcqs_locally.sh
```

This script will:
- Convert your MCQ text files to JSON fixtures
- Clear existing MCQs from the database
- Load the new fixtures
- Verify the import

## Deploying to Heroku with Preloaded MCQs

To deploy your application to Heroku with preloaded MCQs:

```bash
./deploy_with_fixtures.sh
```

This script will:
- Convert your MCQ text files to JSON fixtures
- Commit the fixtures to the repository
- Deploy the application to Heroku
- Set up necessary environment variables
- Run migrations
- Verify the deployment

## Using the Management Command Directly

You can also use the management command directly:

```bash
cd django_neurology_mcq
python manage.py load_mcq_fixtures --clear --all
```

Options:
- `--directory`: Specify a custom directory for fixtures (default: fixtures/mcqs)
- `--all`: Load all MCQs from a single file (all_mcqs.json)
- `--clear`: Clear existing MCQs before importing

## How It Works

1. **Auto-loading**: The application is configured to automatically load fixtures when it starts up if the MCQ table is empty.
2. **Conversion**: The converter script parses MCQ text files and converts them to Django fixtures format.
3. **Management Command**: The `load_mcq_fixtures` management command provides a way to manually load fixtures.

## Customizing the Process

If you need to customize the fixture loading process:

1. Edit the `mcq_to_json_converter.py` script to change how MCQs are parsed from text files
2. Set `AUTO_LOAD_FIXTURES=False` in your environment variables to disable auto-loading
3. Use the management command with custom options for finer control

## Handling Primary Key Conflicts

If you load the fixtures and notice that not all MCQs are imported (e.g., expected 3153 but only 2379 were loaded), this is likely due to duplicate primary keys in the fixture files.

### Using the PK Conflict Resolution Tool

The system includes a utility script to fix primary key conflicts:

```bash
# From the project root directory
python fix_pk_conflicts.py
```

This script:
1. Identifies duplicate primary keys in the fixture file
2. Assigns new unique primary keys to resolve conflicts
3. Creates a fixed fixture file (`all_mcqs_fixed.json`)

After running this script, replace the original fixture file with the fixed one:

```bash
# From the project root directory
cd django_neurology_mcq/fixtures/mcqs
cp all_mcqs.json all_mcqs.json.backup  # Create a backup first
cp all_mcqs_fixed.json all_mcqs.json
```

Then reload the fixtures:

```bash
cd ../..  # Back to django_neurology_mcq directory
python manage.py load_mcq_fixtures --all --clear
```

## Troubleshooting

If you encounter issues with the fixture loading:

1. Check the logs for error messages
2. Verify that the text files are in the expected format
3. Run the management command with higher verbosity for more details:
   ```bash
   python manage.py load_mcq_fixtures --clear --all -v 2
   ```
4. Check the MCQ table in the database to verify the import:
   ```bash
   python manage.py shell -c "from mcq.models import MCQ; print(MCQ.objects.count())"
   ```
5. If not all MCQs were loaded (comparing the count in the fixture file vs. the database):
   ```bash
   # Count MCQs in fixture file
   python -c "import json; f=open('fixtures/mcqs/all_mcqs.json'); data=json.load(f); print(len(data)); f.close()"
   
   # Count MCQs in database
   python manage.py shell -c "from mcq.models import MCQ; print(MCQ.objects.count())"
   ```
   If these numbers don't match, use the fix_pk_conflicts.py script as described above.