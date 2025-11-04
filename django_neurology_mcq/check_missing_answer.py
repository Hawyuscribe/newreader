import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
django.setup()

from mcq.models import MCQ

# Check all MCQs for similar issues
count_empty = MCQ.objects.filter(correct_answer='').count()
count_whitespace = MCQ.objects.filter(correct_answer__regex=r'^\s*$').count()
count_none_as_str = MCQ.objects.filter(correct_answer='None').count()
count_null_as_str = MCQ.objects.filter(correct_answer='null').count()

print(f"Total MCQs: {MCQ.objects.count()}")
print(f"MCQs with empty correct_answer: {count_empty}")
print(f"MCQs with whitespace correct_answer: {count_whitespace}")
print(f"MCQs with 'None' as correct_answer: {count_none_as_str}")
print(f"MCQs with 'null' as correct_answer: {count_null_as_str}")

# Check for unusual values
unusual_answers = MCQ.objects.exclude(correct_answer__in=['A', 'B', 'C', 'D', 'E', 'F']).values_list('correct_answer', flat=True).distinct()
print(f"\nUnusual correct answers: {list(unusual_answers)}")

# Get samples of MCQs with unusual answers
if unusual_answers:
    print("\nSamples of MCQs with unusual answers:")
    for ans in unusual_answers[:5]:
        mcq = MCQ.objects.filter(correct_answer=ans).first()
        print(f"  Answer '{ans}' (repr: {repr(ans)}): MCQ ID {mcq.id}, Q#{mcq.question_number}")
        print(f"    Question: {mcq.question_text[:80]}...")
        print(f"    Options: {list(mcq.options.keys()) if mcq.options else 'None'}")