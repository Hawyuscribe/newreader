# Batch Import Instructions for Vascular Neurology MCQs

After you've tested the single MCQ import and confirmed it works, you can use this approach to import all chunks in batches.

## For Each Chunk (1-21):

### Step 1: Prepare the chunk file
Create a file with the chunk contents. For example, for chunk 1:

```bash
cat > /tmp/mcq_upload/current_chunk.json
```

Then paste the contents of the chunk file (`vascular_chunk_XX_of_21.json`) and press Ctrl+D when done.

### Step 2: Run the import script

```bash
cd django_neurology_mcq
python manage.py shell
```

In the Python shell, paste this code:

```python
import json
from django.db import transaction
from mcq.models import MCQ

# Load the chunk
with open('/tmp/mcq_upload/current_chunk.json', 'r') as f:
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
                existing.options = mcq_data.get('options', {})
                existing.correct_answer = mcq_data.get('correct_answer', '')
                existing.explanation = mcq_data.get('explanation', '')
                existing.exam_year = mcq_data.get('exam_year', '')
                existing.exam_type = mcq_data.get('exam_type', '')
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

# Check the total vascular MCQs
vascular_count = MCQ.objects.filter(subspecialty="vascular_neurology").count()
print(f"Total vascular MCQs: {vascular_count}")

# Exit the shell
exit()
```

### Step 3: Repeat for each chunk

After completing one chunk, move to the next and repeat the process.

## Alternative Approach: Combining All Chunks

If you prefer to do everything in one go, you can combine all chunks:

1. Copy all MCQs from all chunks into a single file
2. Follow the same process as above, but with the combined file

## Verifying the Import

After importing all chunks, verify the total number of vascular MCQs:

```bash
python manage.py shell -c "from mcq.models import MCQ; print(f'Total MCQs: {MCQ.objects.count()}'); print(f'Vascular MCQs: {MCQ.objects.filter(subspecialty=\"vascular_neurology\").count()}')"
```

You should have approximately 406 vascular neurology MCQs if all were imported successfully.