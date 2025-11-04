from django.core.management.base import BaseCommand
from mcq.models import MCQ
from django.db.models import Min, Max

class Command(BaseCommand):
    help = 'Check MCQ IDs in the database'

    def handle(self, *args, **options):
        # Get total count
        total = MCQ.objects.count()
        self.stdout.write(f"Total MCQs: {total}")
        
        if total == 0:
            self.stdout.write(self.style.WARNING("No MCQs found in database!"))
            return
            
        # Get ID range
        id_stats = MCQ.objects.aggregate(min_id=Min('id'), max_id=Max('id'))
        self.stdout.write(f"ID range: {id_stats['min_id']} - {id_stats['max_id']}")
        
        # Check for large IDs
        large_ids = MCQ.objects.filter(id__gte=100000000).count()
        if large_ids > 0:
            self.stdout.write(self.style.WARNING(f"Found {large_ids} MCQs with IDs >= 100000000"))
            
            # Show sample large IDs
            sample_large = MCQ.objects.filter(id__gte=100000000).order_by('-id')[:10]
            self.stdout.write("\nSample large IDs:")
            for mcq in sample_large:
                self.stdout.write(f"  ID: {mcq.id}, Question: {mcq.question_text[:50]}...")
                
        # Check specific IDs from the 404 errors
        test_ids = [100090767, 100090772]
        self.stdout.write("\nChecking specific IDs from 404 errors:")
        for test_id in test_ids:
            exists = MCQ.objects.filter(id=test_id).exists()
            self.stdout.write(f"  ID {test_id}: {'EXISTS' if exists else 'NOT FOUND'}")
            
        # Show ID distribution by subspecialty
        from django.db.models import Count
        self.stdout.write("\nTop subspecialties by count:")
        subspecialties = MCQ.objects.values('subspecialty').annotate(
            count=Count('id'),
            min_id=Min('id'),
            max_id=Max('id')
        ).order_by('-count')[:10]
        
        for sub in subspecialties:
            self.stdout.write(f"  {sub['subspecialty']}: {sub['count']} MCQs (ID range: {sub['min_id']}-{sub['max_id']})")