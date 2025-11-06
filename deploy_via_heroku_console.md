# Deploying MCQs to Heroku

After multiple attempts, we've identified that there are connection timeout issues when trying to import large MCQ data files to Heroku via the CLI. 

Here are alternative approaches to import your MCQs:

## Option 1: Using Heroku Console

One reliable method is to use the Heroku console directly to perform the import. Follow these steps:

1. Log into the Heroku Dashboard: https://dashboard.heroku.com/
2. Select your app: radiant-gorge-35079
3. Click on "More" in the top right and select "Run console"
4. Open a bash shell by typing `bash` and hitting enter
5. You'll now have direct access to the Heroku environment

In the console, you can run Python commands to import data. Here's a suggested workflow:

```bash
# Navigate to your Django project directory
cd /app/django_neurology_mcq

# Open a Python shell with Django configured
python manage.py shell
```

Once in the Python shell, you can run import commands:

```python
# Import libraries
from mcq.models import MCQ
import json
import requests
from django.db import transaction

# Example: Import from a URL
# Replace with a URL where you've hosted your JSON file
url = "YOUR_HOSTED_JSON_URL"
response = requests.get(url)
data = json.loads(response.text)

# Check data structure
if "mcqs" in data:
    mcqs_data = data["mcqs"]
    print(f"Found {len(mcqs_data)} MCQs to import")
    
    # Import MCQs
    success_count = 0
    error_count = 0
    
    with transaction.atomic():
        for mcq_data in mcqs_data:
            try:
                # Process MCQ (simplified example)
                subspecialty = "Headache"  # Replace with actual subspecialty
                question_text = mcq_data.get("Question Text", "").strip()
                
                # Check if MCQ exists
                existing = MCQ.objects.filter(
                    question_text=question_text,
                    subspecialty=subspecialty
                ).first()
                
                # Build options dict
                options = {}
                for letter in ['A', 'B', 'C', 'D', 'E', 'F']:
                    key = f"Option {letter}"
                    if key in mcq_data and mcq_data[key]:
                        options[letter] = mcq_data[key].strip()
                
                if existing:
                    # Update existing
                    existing.options = options
                    existing.correct_answer = mcq_data.get("Correct Answer", "")
                    existing.save()
                else:
                    # Create new
                    mcq = MCQ(
                        question_text=question_text,
                        options=options,
                        correct_answer=mcq_data.get("Correct Answer", ""),
                        subspecialty=subspecialty,
                        explanation=mcq_data.get("Option Analysis", ""),
                        # Add other fields as needed
                    )
                    mcq.save()
                
                success_count += 1
            except Exception as e:
                print(f"Error importing MCQ: {str(e)}")
                error_count += 1
    
    print(f"Import results: {success_count} successful, {error_count} failed")
```

## Option 2: Create a Django Management Command

You could create a custom Django management command that downloads and imports MCQs from a URL:

1. Create a new management command file at `/app/django_neurology_mcq/mcq/management/commands/import_mcqs_from_url.py`

```python
from django.core.management.base import BaseCommand
import requests
import json
from mcq.models import MCQ
from django.db import transaction

class Command(BaseCommand):
    help = 'Import MCQs from a URL'

    def add_arguments(self, parser):
        parser.add_argument('url', type=str, help='URL to JSON file with MCQs')
        parser.add_argument('--subspecialty', type=str, help='Override subspecialty for all MCQs')

    def handle(self, *args, **options):
        url = options['url']
        subspecialty_override = options.get('subspecialty')
        
        self.stdout.write(f"Downloading MCQs from {url}...")
        response = requests.get(url)
        data = json.loads(response.text)
        
        if "mcqs" in data:
            mcqs_data = data["mcqs"]
            self.stdout.write(f"Found {len(mcqs_data)} MCQs to import")
            
            success_count = 0
            error_count = 0
            
            with transaction.atomic():
                for mcq_data in mcqs_data:
                    try:
                        # Use override or extract from data
                        subspecialty = subspecialty_override or mcq_data.get("Subspecialty", "Other")
                        
                        # Process MCQ data
                        # ... similar to the code in Option 1
                        
                        success_count += 1
                    except Exception as e:
                        self.stdout.write(self.style.ERROR(f"Error importing MCQ: {str(e)}"))
                        error_count += 1
            
            self.stdout.write(self.style.SUCCESS(f"Import results: {success_count} successful, {error_count} failed"))
```

Then you could run this command from the Heroku console:

```bash
cd /app/django_neurology_mcq
python manage.py import_mcqs_from_url https://your-hosted-json-url.com/mcqs.json --subspecialty="Headache"
```

## Option 3: Host Your JSON Files

To make the above options work, you'll need to host your JSON files somewhere accessible via a URL. Options include:

1. GitHub Gists or repositories (public or private)
2. A file sharing service like Dropbox, Google Drive, or AWS S3
3. A temporary file hosting service

## Next Steps

1. Upload your JSON files to a hosting service that provides direct download URLs
2. Use either Option 1 or Option 2 to import the data directly on Heroku

This approach should work better than trying to transfer large files through the Heroku CLI, which is causing the timeouts we've been experiencing.