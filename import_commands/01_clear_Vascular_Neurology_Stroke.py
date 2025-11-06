
from mcq.models import MCQ

# Delete MCQs for Vascular Neurology/Stroke
count = MCQ.objects.filter(subspecialty="Vascular Neurology/Stroke").count()
print(f"Deleting {count} MCQs for Vascular Neurology/Stroke...")
MCQ.objects.filter(subspecialty="Vascular Neurology/Stroke").delete()
print(f"Done clearing Vascular Neurology/Stroke MCQs")
