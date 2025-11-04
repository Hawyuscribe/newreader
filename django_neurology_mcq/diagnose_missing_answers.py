import os
import django

# This script is meant to be run on Heroku to diagnose missing answers
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
django.setup()

from mcq.models import MCQ

print("=== MCQ Correct Answer Diagnosis ===\n")

# Check specific MCQ if provided via command line
import sys
if len(sys.argv) > 1:
    try:
        mcq_id = int(sys.argv[1])
        mcq = MCQ.objects.get(pk=mcq_id)
        print(f"Specific MCQ {mcq_id}:")
        print(f"  Question Number: {mcq.question_number}")
        print(f"  Question: {mcq.question_text[:100]}...")
        print(f"  Correct Answer: '{mcq.correct_answer}'")
        print(f"  Correct Answer repr: {repr(mcq.correct_answer)}")
        print(f"  Correct Answer length: {len(mcq.correct_answer)}")
        print(f"  Options: {mcq.options}")
        print(f"  Is empty: {mcq.correct_answer == ''}")
        print(f"  Is whitespace: {mcq.correct_answer.strip() == ''}")
        print()
    except MCQ.DoesNotExist:
        print(f"MCQ {mcq_id} not found")
    except ValueError:
        print(f"Invalid MCQ ID: {sys.argv[1]}")

# General statistics
total = MCQ.objects.count()
print(f"Total MCQs in database: {total}")

# Check for various empty/invalid values
empty_count = MCQ.objects.filter(correct_answer='').count()
whitespace_count = MCQ.objects.filter(correct_answer__regex=r'^\s*$').count()
none_str_count = MCQ.objects.filter(correct_answer='None').count()
null_str_count = MCQ.objects.filter(correct_answer='null').count()

print(f"\nProblematic correct_answer values:")
print(f"  Empty string: {empty_count}")
print(f"  Whitespace only: {whitespace_count}")
print(f"  'None' string: {none_str_count}")
print(f"  'null' string: {null_str_count}")

# Check for unusual answers
valid_answers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
unusual = MCQ.objects.exclude(correct_answer__in=valid_answers).values_list('correct_answer', flat=True).distinct()
print(f"\nUnusual answers (not A-H): {list(unusual)}")

# Get samples of problematic MCQs
problematic = MCQ.objects.exclude(correct_answer__in=valid_answers)[:10]
if problematic:
    print(f"\nSample problematic MCQs:")
    for mcq in problematic:
        print(f"  ID: {mcq.id}, Q#{mcq.question_number}")
        print(f"    Answer: '{mcq.correct_answer}' (repr: {repr(mcq.correct_answer)})")
        print(f"    Question: {mcq.question_text[:80]}...")
        print(f"    Options: {list(mcq.options.keys()) if mcq.options else 'None'}")

# Check for MCQs where correct_answer is not in options
print("\nMCQs where correct_answer not in options:")
mismatch_count = 0
for mcq in MCQ.objects.all()[:100]:  # Check first 100 to avoid timeout
    if mcq.options and mcq.correct_answer and mcq.correct_answer not in mcq.options:
        mismatch_count += 1
        if mismatch_count <= 5:  # Show first 5
            print(f"  ID: {mcq.id}, Answer: '{mcq.correct_answer}', Options: {list(mcq.options.keys())}")

print(f"Total mismatches in first 100: {mismatch_count}")

# Check for long answers
long_answers = MCQ.objects.filter(correct_answer__regex=r'^.{6,}$')[:5]
if long_answers:
    print(f"\nMCQs with long answers (>5 chars):")
    for mcq in long_answers:
        print(f"  ID: {mcq.id}, Answer: '{mcq.correct_answer}' (length: {len(mcq.correct_answer)})")