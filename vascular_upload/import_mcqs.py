
import json
import sys
from mcq.models import MCQ

# Load MCQs from JSON file
with open(sys.argv[1], 'r') as f:
    mcqs = json.load(f)

print(f"Processing {len(mcqs)} MCQs")

# Track success and errors
success_count = 0
error_count = 0
errors = []

for i, mcq_data in enumerate(mcqs):
    try:
        # Extract fields
        question_text = mcq_data.get('question_text', '')
        options = mcq_data.get('options', {})
        correct_answer = mcq_data.get('correct_answer', '')
        explanation = mcq_data.get('explanation', '')
        subspecialty = mcq_data.get('subspecialty', 'vascular_neurology')
        exam_year = mcq_data.get('exam_year', '')
        exam_type = mcq_data.get('exam_type', '')
        
        # Check if the MCQ already exists
        if MCQ.objects.filter(question_text=question_text).exists():
            print(f"MCQ already exists: {question_text[:30]}...")
            error_count += 1
            errors.append(f"Duplicate: {question_text[:30]}...")
            continue
        
        # Create and save MCQ
        mcq = MCQ(
            question_text=question_text,
            options=options,
            correct_answer=correct_answer,
            explanation=explanation,
            subspecialty=subspecialty,
            exam_year=exam_year,
            exam_type=exam_type
        )
        
        mcq.save()
        success_count += 1
        print(f"Saved MCQ {i+1}: {question_text[:30]}...")
    
    except Exception as e:
        error_count += 1
        errors.append(str(e))
        print(f"Error processing MCQ {i+1}: {str(e)}")

# Print summary
print(f"\nRESULTS:")
print(f"Successfully imported: {success_count} MCQs")
print(f"Failed to import: {error_count} MCQs")

if errors:
    print("\nErrors:")
    for error in errors[:5]:
        print(f" - {error}")
    if len(errors) > 5:
        print(f" - ...and {len(errors) - 5} more errors")
