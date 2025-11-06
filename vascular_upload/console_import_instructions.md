# Heroku Console Import Instructions

## Step 1: Log into Heroku Dashboard
- Go to https://dashboard.heroku.com
- Sign in with your credentials
- Select the "radiant-gorge-35079" app
- Click "More" → "Run Console" → select "bash"

## Step 2: Create a temporary directory
```bash
mkdir -p /tmp/mcq_upload
```

## Step 3: Create the MCQ file
```bash
cat > /tmp/mcq_upload/single_mcq.json
```

Then paste this content:
```json
[
  {
    "question_text": "Patient with acute stroke brain MRI found dorsal cerebellar infarction (superior cerebellar artery) what will you find in exam:",
    "options": {
      "option_a": "Ipsilateral truncal Hyperalgesia",
      "option_b": "Ipsilateral Horner",
      "option_c": "Hearing loss",
      "option_d": "",
      "option_e": ""
    },
    "correct_answer": "B",
    "explanation": "",
    "subspecialty": "vascular_neurology",
    "exam_year": "2018",
    "exam_type": "Part I"
  }
]
```
Press Ctrl+D when done pasting

## Step 4: Create the import script
```bash
cat > /tmp/mcq_upload/import.py
```

Then paste this content:
```python
import json
from django.db import transaction
from mcq.models import MCQ

# Load MCQs
with open('/tmp/mcq_upload/single_mcq.json', 'r') as f:
    mcqs = json.load(f)

print(f"Processing {len(mcqs)} MCQs")

# Import counters
created = 0
updated = 0
skipped = 0

# Process in transaction
with transaction.atomic():
    for mcq_data in mcqs:
        question = mcq_data.get('question_text', '')
        if not question:
            print("Skipping MCQ with no question text")
            skipped += 1
            continue
        
        # Check if MCQ exists
        existing = MCQ.objects.filter(question_text=question).first()
        
        if existing:
            # Only update if needed
            if existing.subspecialty != 'vascular_neurology':
                existing.subspecialty = 'vascular_neurology'
                existing.save()
                updated += 1
                print(f"Updated: {question[:30]}...")
            else:
                skipped += 1
                print(f"Skipped (already exists): {question[:30]}...")
        else:
            # Create new
            MCQ.objects.create(
                question_text=question,
                options=mcq_data.get('options', {}),
                correct_answer=mcq_data.get('correct_answer', ''),
                explanation=mcq_data.get('explanation', ''),
                subspecialty=mcq_data.get('subspecialty', 'vascular_neurology'),
                exam_year=mcq_data.get('exam_year', ''),
                exam_type=mcq_data.get('exam_type', '')
            )
            created += 1
            print(f"Created: {question[:30]}...")

print(f"Results: Created {created}, Updated {updated}, Skipped {skipped}")
```
Press Ctrl+D when done pasting

## Step 5: Run the import script
```bash
cd django_neurology_mcq
python manage.py shell < /tmp/mcq_upload/import.py
```

## Step 6: Verify the import
```bash
python manage.py shell -c "from mcq.models import MCQ; print(f'Vascular MCQs: {MCQ.objects.filter(subspecialty=\"vascular_neurology\").count()}')"
```

## Step 7: If successful, move on to the full chunks
After confirming the single MCQ import works, follow the same process but with each chunk file.