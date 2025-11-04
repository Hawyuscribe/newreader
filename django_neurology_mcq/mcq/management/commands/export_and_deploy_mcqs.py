"""
Management command to export MCQs from local database and deploy to Heroku
"""
import os
import json
import subprocess
import tempfile
from pathlib import Path
from django.core.management.base import BaseCommand
from django.core import serializers
from mcq.models import MCQ

class Command(BaseCommand):
    help = 'Export MCQs from local database and deploy to Heroku'
    
    def add_arguments(self, parser):
        parser.add_argument('--app', default='radiant-gorge-35079', help='Heroku app name')
        parser.add_argument('--batch-size', type=int, default=500, help='Batch size for import')
        parser.add_argument('--clear', action='store_true', help='Clear all MCQs on Heroku before importing')
        parser.add_argument('--subspecialty', help='Only export/import specific subspecialty')
    
    def handle(self, *args, **options):
        app_name = options['app']
        batch_size = options['batch_size']
        clear_existing = options['clear']
        subspecialty = options.get('subspecialty')
        
        # Export MCQs from local database
        self.stdout.write('Exporting MCQs from local database...')
        
        # Filter by subspecialty if specified
        queryset = MCQ.objects.all()
        if subspecialty:
            queryset = queryset.filter(subspecialty=subspecialty)
            self.stdout.write(f'Filtering by subspecialty: {subspecialty}')
        
        # Get count
        total_mcqs = queryset.count()
        self.stdout.write(f'Found {total_mcqs} MCQs to export')
        
        if total_mcqs == 0:
            self.stdout.write(self.style.ERROR('No MCQs to export. Aborting.'))
            return
        
        # Delete existing MCQs on Heroku if requested
        if clear_existing:
            self.stdout.write('Clearing existing MCQs on Heroku...')
            clear_cmd = f"""
            cd /app/django_neurology_mcq && python manage.py shell -c "
            from mcq.models import MCQ
            initial_count = MCQ.objects.count()
            print(f'Deleting {initial_count} MCQs...')
            MCQ.objects.all().delete()
            final_count = MCQ.objects.count()
            print(f'Final MCQ count: {final_count}')
            "
            """
            self.run_heroku_command(clear_cmd, app_name)
        
        # Process in batches
        batches = []
        
        for i in range(0, total_mcqs, batch_size):
            self.stdout.write(f'Preparing batch {i+1}-{min(i+batch_size, total_mcqs)}...')
            
            # Serialize the batch
            batch_queryset = queryset[i:i+batch_size]
            batch_data = serializers.serialize('json', batch_queryset)
            batches.append(batch_data)
        
        # Now import each batch to Heroku
        for i, batch_data in enumerate(batches):
            batch_start = i * batch_size + 1
            batch_end = min((i + 1) * batch_size, total_mcqs)
            self.stdout.write(f'Importing batch {batch_start}-{batch_end} to Heroku...')
            
            # Create temp file for the batch
            with tempfile.NamedTemporaryFile(delete=False, suffix='.json') as temp:
                temp.write(batch_data.encode('utf-8'))
                temp_path = temp.name
            
            # Upload to Heroku using Git and import
            import_cmd = f"""
            cd /app/django_neurology_mcq && python manage.py shell -c '
            import json
            from django.core import serializers
            from mcq.models import MCQ
            
            # Load data from JSON
            with open("/tmp/batch_import.json", "r") as f:
                data = f.read()
            
            # Parse JSON
            objects = serializers.deserialize("json", data)
            
            # Import MCQs
            from django.db import transaction
            with transaction.atomic():
                count = 0
                for obj in objects:
                    try:
                        # Check if MCQ with this ID already exists
                        existing = MCQ.objects.filter(id=obj.object.id).exists()
                        if existing:
                            # Update existing
                            obj.save()
                            count += 1
                        else:
                            # Save new
                            obj.save()
                            count += 1
                    except Exception as e:
                        print(f"Error importing MCQ {obj.object.id}: {str(e)[:100]}")
                
                print(f"Successfully imported {count} MCQs")
            '
            """
            
            try:
                # Upload the file to Heroku
                upload_cmd = f"cat {temp_path} | heroku run 'cat > /tmp/batch_import.json' --app {app_name}"
                subprocess.check_call(upload_cmd, shell=True)
                
                # Run the import command
                self.run_heroku_command(import_cmd, app_name)
                
                # Clean up
                os.unlink(temp_path)
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error importing batch: {str(e)}'))
                # Don't delete the file so we can retry
                self.stdout.write(self.style.ERROR(f'Batch file saved at: {temp_path}'))
        
        # Verify the import
        self.stdout.write('Verifying import...')
        verify_cmd = f"""
        cd /app/django_neurology_mcq && python manage.py shell -c "
        from mcq.models import MCQ
        from django.db.models import Count
        
        total = MCQ.objects.count()
        print(f'Total MCQs in database: {total}')
        
        # By subspecialty
        print('\\nMCQs by Subspecialty:')
        subspecialties = MCQ.objects.values('subspecialty').annotate(count=Count('id')).order_by('-count')
        for item in subspecialties[:10]:
            print(f\"  {item['subspecialty']}: {item['count']}\")
        
        # Check correct answers
        with_correct = MCQ.objects.exclude(correct_answer__isnull=True).exclude(correct_answer='').count()
        print(f'\\nMCQs with correct answers: {with_correct} ({with_correct/total*100:.1f}%)')
        "
        """
        self.run_heroku_command(verify_cmd, app_name)
        
        self.stdout.write(self.style.SUCCESS('MCQ export and import completed!'))
    
    def run_heroku_command(self, command, app_name):
        """Run a command on Heroku."""
        heroku_cmd = ['heroku', 'run', '--app', app_name, command]
        subprocess.run(heroku_cmd, check=True)