from django.core.management.base import BaseCommand
from mcq.models import MCQ

class Command(BaseCommand):
    help = 'Fix Neuro-Oncology subspecialty name mismatch'

    def handle(self, *args, **options):
        self.stdout.write('Fixing Neuro-Oncology subspecialty name...')
        
        # Find MCQs with "Neuro-Oncology" (capital O) and change to "Neuro-oncology" (lowercase o)
        mcqs_to_fix = MCQ.objects.filter(subspecialty='Neuro-Oncology')
        count = mcqs_to_fix.count()
        
        self.stdout.write(f'Found {count} MCQs with "Neuro-Oncology"')
        
        if count > 0:
            # Update to the correct case
            updated = mcqs_to_fix.update(subspecialty='Neuro-oncology')
            self.stdout.write(f'Updated {updated} MCQs to use "Neuro-oncology"')
        
        # Check final count
        final_count = MCQ.objects.filter(subspecialty='Neuro-oncology').count()
        self.stdout.write(f'Final count for "Neuro-oncology": {final_count}')
        
        # Also check if there are any other case variations
        all_neuro_onc = MCQ.objects.filter(subspecialty__icontains='neuro').filter(subspecialty__icontains='onc')
        self.stdout.write(f'All neuro-onc related subspecialties:')
        for mcq in all_neuro_onc.values('subspecialty').distinct():
            count = MCQ.objects.filter(subspecialty=mcq['subspecialty']).count()
            self.stdout.write(f'  {mcq["subspecialty"]}: {count}')
        
        self.stdout.write(self.style.SUCCESS('Neuro-oncology name fix complete!'))