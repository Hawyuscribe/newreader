"""Check subspecialty counts in the database."""
from django.core.management.base import BaseCommand
from django.db.models import Count
from mcq.models import MCQ


class Command(BaseCommand):
    help = 'Check subspecialty counts'
    
    def handle(self, *args, **options):
        # Get all unique subspecialties with counts
        subspecialty_counts = MCQ.objects.values('subspecialty').annotate(count=Count('id')).order_by('subspecialty')
        
        self.stdout.write("=== Subspecialty counts in database ===")
        total = 0
        for sub in subspecialty_counts:
            self.stdout.write(f"{sub['subspecialty']}: {sub['count']}")
            total += sub['count']
        
        self.stdout.write(f"\nTotal MCQs: {total}")
        
        # Check specific subspecialties that appear as 0 on website
        self.stdout.write("\n=== Specific subspecialty checks ===")
        neurooph = MCQ.objects.filter(subspecialty='Neuroophthalmology').count()
        vascular = MCQ.objects.filter(subspecialty='Vascular Neurology/Stroke').count()
        unclassified = MCQ.objects.filter(subspecialty='Other/Unclassified').count()
        
        self.stdout.write(f"Neuroophthalmology: {neurooph}")
        self.stdout.write(f"Vascular Neurology/Stroke: {vascular}")
        self.stdout.write(f"Other/Unclassified: {unclassified}")
        
        # Check for variations in subspecialty names
        self.stdout.write("\n=== Subspecialty name variations ===")
        like_neurooph = MCQ.objects.filter(subspecialty__icontains='neuroop').count()
        like_vascular = MCQ.objects.filter(subspecialty__icontains='vascular').count()
        like_stroke = MCQ.objects.filter(subspecialty__icontains='stroke').count()
        
        self.stdout.write(f"Contains 'neuroop': {like_neurooph}")
        self.stdout.write(f"Contains 'vascular': {like_vascular}")
        self.stdout.write(f"Contains 'stroke': {like_stroke}")
        
        # Sample MCQs
        self.stdout.write("\n=== Sample MCQs ===")
        sample = MCQ.objects.first()
        if sample:
            self.stdout.write(f"First MCQ:")
            self.stdout.write(f"  ID: {sample.id}")
            self.stdout.write(f"  Question: {sample.question_text[:80]}...")
            self.stdout.write(f"  Subspecialty: '{sample.subspecialty}'")
            self.stdout.write(f"  Correct answer: {sample.correct_answer}")
            self.stdout.write(f"  Has explanations: {bool(sample.explanation_sections)}")