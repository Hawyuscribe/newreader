
from mcq.models import MCQ, UserProfile, Bookmark
from django.contrib.auth.models import User
from django.db.models import Q, Count

# 1. Check total MCQs
total_mcqs = MCQ.objects.count()
print(f"Total MCQs in database: {total_mcqs}")

# 2. Check vascular MCQs specifically
vascular_mcqs = MCQ.objects.filter(Q(subspecialty__icontains='vascular') | Q(subspecialty__icontains='stroke')).count()
print(f"Vascular MCQs: {vascular_mcqs}")

# 3. Check all subspecialties
subspecialties = MCQ.objects.values('subspecialty').annotate(count=Count('id')).order_by('-count')
print("\nMCQs by subspecialty:")
for sub in subspecialties:
    print(f"  {sub['subspecialty']}: {sub['count']}")

# 4. Check for empty fields that might cause issues
empty_questions = MCQ.objects.filter(question='').count()
empty_subspecialties = MCQ.objects.filter(subspecialty='').count()
print(f"\nMCQs with empty questions: {empty_questions}")
print(f"MCQs with empty subspecialties: {empty_subspecialties}")

# 5. Check the dashboard view for issues
try:
    from mcq.views import dashboard
    print("\nDashboard view loaded successfully")
except Exception as e:
    print(f"\nError loading dashboard view: {str(e)}")

# 6. Try to create a test MCQ
try:
    test_mcq = MCQ(
        question="Test question for dashboard",
        option_a="A",
        option_b="B",
        option_c="C",
        option_d="D",
        option_e="E",
        correct_answer="A",
        subspecialty="vascular_neurology",
        explanation="Test explanation",
        exam_year="2025",
        exam_type="Test"
    )
    test_mcq.save()
    print(f"\nTest MCQ created with ID: {test_mcq.id}")
    
    # Retrieve to verify
    retrieved = MCQ.objects.get(id=test_mcq.id)
    print(f"Retrieved MCQ: {retrieved.question}")
except Exception as e:
    print(f"\nError creating test MCQ: {str(e)}")
