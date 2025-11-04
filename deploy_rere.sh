#!/bin/bash
set -e

echo "Starting RERE MCQ deployment..."

# Clear existing MCQs
echo "Clearing all existing MCQs..."
heroku run python django_neurology_mcq/manage.py shell -a radiant-gorge-35079 << 'EOF'
from mcq.models import MCQ
MCQ.objects.all().delete()
print("All MCQs cleared")
exit()
EOF

# Import each chunk
echo "Importing fixture chunks..."
for i in {01..21}; do
    echo "Importing chunk $i..."
    heroku run python django_neurology_mcq/manage.py loaddata rere_chunks/rere_chunk_$i.json -a radiant-gorge-35079
done

# Verify the import
echo "Verifying import..."
heroku run python django_neurology_mcq/manage.py shell -a radiant-gorge-35079 << 'EOF'
from mcq.models import MCQ
from django.db.models import Count

# Total count
total = MCQ.objects.count()
print(f"\nTotal MCQs: {total}")

# Count by subspecialty
subspecialty_counts = MCQ.objects.values('subspecialty').annotate(count=Count('id')).order_by('subspecialty')
print("\nMCQs by subspecialty:")
for sub in subspecialty_counts:
    print(f"  {sub['subspecialty']}: {sub['count']}")

# Check explanation sections
mcqs_with_explanations = MCQ.objects.exclude(explanation_sections=None).exclude(explanation_sections={}).count()
print(f"\nMCQs with explanation sections: {mcqs_with_explanations}")

# Sample MCQ to verify data
sample = MCQ.objects.first()
if sample:
    print(f"\nSample MCQ {sample.id}:")
    print(f"  Question: {sample.question_text[:100]}...")
    print(f"  Subspecialty: {sample.subspecialty}")
    print(f"  Correct answer: {sample.correct_answer}")
    exp_sections = sample.explanation_sections
    if exp_sections and 'option_analysis' in exp_sections:
        analysis = exp_sections['option_analysis']
        if isinstance(analysis, str):
            print(f"  Option analysis: {analysis[:100]}...")
        else:
            print(f"  Option analysis type: {type(analysis)}")
exit()
EOF

echo "Deployment complete!"