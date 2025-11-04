
from mcq.models import MCQ
from django.db.models import Count

# Get total MCQ count
total_mcqs = MCQ.objects.count()
print(f"Total MCQs in database: {total_mcqs}")

# Get subspecialty counts
print("MCQs by subspecialty:")
for item in MCQ.objects.values("subspecialty").annotate(count=Count("id")).order_by("-count"):
    print(f"  {item['subspecialty']}: {item['count']}")
