from django.core.management.base import BaseCommand
from mcq.models import MCQ
from django.db import connection

class Command(BaseCommand):
    help = 'Fix MCQ IDs by resetting sequence'

    def handle(self, *args, **options):
        # First, let's check the current situation
        total = MCQ.objects.count()
        self.stdout.write(f"Total MCQs: {total}")
        
        if total == 0:
            self.stdout.write(self.style.WARNING("No MCQs found!"))
            return
            
        # Check for large IDs
        large_ids = MCQ.objects.filter(id__gte=100000000)
        if large_ids.exists():
            self.stdout.write(self.style.WARNING(f"\nFound {large_ids.count()} MCQs with extremely large IDs!"))
            samples = large_ids.order_by('-id')[:5]
            for mcq in samples:
                self.stdout.write(f"  ID: {mcq.id}, Question: {mcq.question_text[:50]}...")
            
            # Get current max ID that's reasonable
            reasonable_mcqs = MCQ.objects.filter(id__lt=100000000)
            if reasonable_mcqs.exists():
                max_reasonable_id = reasonable_mcqs.order_by('-id').first().id
                self.stdout.write(f"\nHighest reasonable ID: {max_reasonable_id}")
            else:
                max_reasonable_id = 0
                
            # Fix: Update large IDs to sequential values
            self.stdout.write("\nFixing large IDs...")
            next_id = max_reasonable_id + 1
            
            for mcq in large_ids.order_by('id'):
                old_id = mcq.id
                # Use raw SQL to avoid auto-increment issues
                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE mcq_mcq SET id = %s WHERE id = %s",
                        [next_id, old_id]
                    )
                self.stdout.write(f"  Updated ID {old_id} -> {next_id}")
                next_id += 1
                
            # Reset the sequence to the correct value
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT setval(pg_get_serial_sequence('mcq_mcq', 'id'), %s)",
                    [next_id]
                )
            
            self.stdout.write(self.style.SUCCESS(f"\nFixed {large_ids.count()} MCQs with large IDs"))
            self.stdout.write(f"Next ID will be: {next_id}")
        else:
            # Just ensure sequence is correct
            max_id = MCQ.objects.order_by('-id').first().id
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT setval(pg_get_serial_sequence('mcq_mcq', 'id'), %s)",
                    [max_id + 1]
                )
            self.stdout.write(self.style.SUCCESS(f"Sequence is correct. Next ID will be: {max_id + 1}"))
            
        # Final check
        self.stdout.write("\nFinal ID distribution:")
        from django.db.models import Min, Max
        stats = MCQ.objects.aggregate(min_id=Min('id'), max_id=Max('id'))
        self.stdout.write(f"ID range: {stats['min_id']} - {stats['max_id']}")