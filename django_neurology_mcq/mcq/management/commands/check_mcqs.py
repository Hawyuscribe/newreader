from django.core.management.base import BaseCommand
from mcq.models import MCQ

class Command(BaseCommand):
    help = 'Check the current MCQ status in the database'

    def handle(self, *args, **kwargs):
        # Count all MCQs
        total_mcqs = MCQ.objects.count()
        self.stdout.write(f"Total MCQs in database: {total_mcqs}")
        
        # Count subspecialties
        subspecialties = MCQ.objects.values_list('subspecialty', flat=True).distinct()
        self.stdout.write("\nMCQs by subspecialty:")
        for subspec in sorted(subspecialties):
            count = MCQ.objects.filter(subspecialty=subspec).count()
            self.stdout.write(f"- {subspec}: {count}")
        
        # Count vascular MCQs specifically
        vascular_mcqs = MCQ.objects.filter(subspecialty='vascular_neurology').count()
        self.stdout.write(f"\nVascular neurology MCQs: {vascular_mcqs}")
        
        # Show sample of vascular MCQs if any exist
        if vascular_mcqs > 0:
            self.stdout.write("\nSample of recent vascular MCQs:")
            sample = MCQ.objects.filter(subspecialty='vascular_neurology').order_by('-id')[:3]
            for i, mcq in enumerate(sample):
                self.stdout.write(f"{i+1}. {mcq.question_text[:50]}...")
                self.stdout.write(f"   Answer: {mcq.correct_answer}")
        else:
            self.stdout.write("\nNo vascular MCQs found in the database.")