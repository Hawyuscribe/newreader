#!/usr/bin/env python3
"""
Direct import of MCQs to Heroku by splitting into smaller fixture files.
"""
import os
import json
import subprocess
from pathlib import Path
import django
import tempfile

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
django.setup()

from mcq.models import MCQ
from django.core import serializers
from django.db.models import Count

# Get all MCQs
mcqs = MCQ.objects.all()
total_mcqs = mcqs.count()
print(f"Found {total_mcqs} MCQs to export")

# Heroku app name
APP_NAME = "radiant-gorge-35079"

# Create a directory for fixtures
fixtures_dir = Path("fixtures")
fixtures_dir.mkdir(exist_ok=True)

# Export MCQs in chunks of 500
chunk_size = 500
total_chunks = (total_mcqs + chunk_size - 1) // chunk_size

# Clear all existing MCQs on Heroku
print("Clearing existing MCQs on Heroku...")
clear_cmd = f"heroku run --app {APP_NAME} \"cd /app/django_neurology_mcq && python manage.py shell -c 'from mcq.models import MCQ; count = MCQ.objects.count(); print(f\\\"Deleting {count} MCQs...\\\"); MCQ.objects.all().delete(); print(\\\"Done\\\")'\" "
subprocess.run(clear_cmd, shell=True)

# Export and import by subspecialty
subspecialties = MCQ.objects.values('subspecialty').annotate(count=Count('id')).order_by('-count')

for subspec_data in subspecialties:
    subspecialty = subspec_data['subspecialty']
    count = subspec_data['count']
    
    print(f"\nProcessing {subspecialty} ({count} MCQs)...")
    
    # Export MCQs for this subspecialty
    mcqs_subset = MCQ.objects.filter(subspecialty=subspecialty)
    fixture_data = serializers.serialize('json', mcqs_subset)
    
    # Create temp file
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as f:
        f.write(fixture_data)
        temp_path = f.name
    
    # Create loaddata script
    loaddata_script = f"""
    import json
    import tempfile
    from django.core import serializers
    from mcq.models import MCQ
    
    # Count MCQs before import
    before_count = MCQ.objects.filter(subspecialty="{subspecialty}").count()
    print(f"Before import: {before_count} MCQs for {subspecialty}")
    
    # Delete existing MCQs for this subspecialty
    MCQ.objects.filter(subspecialty="{subspecialty}").delete()
    
    # Load from file
    with open('/tmp/import_data.json', 'r') as f:
        data = f.read()
    
    # Import
    from django.db import transaction
    with transaction.atomic():
        objects = serializers.deserialize('json', data)
        for obj in objects:
            obj.save()
    
    # Count MCQs after import
    after_count = MCQ.objects.filter(subspecialty="{subspecialty}").count()
    print(f"After import: {after_count} MCQs for {subspecialty}")
    """
    
    # Create temp script file
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.py') as f:
        f.write(loaddata_script)
        script_path = f.name
    
    # Upload to Heroku and import
    try:
        print(f"Uploading and importing {subspecialty} MCQs...")
        
        # Upload fixture file
        upload_cmd = f"cat {temp_path} | heroku run --app {APP_NAME} \"cat > /tmp/import_data.json\""
        subprocess.run(upload_cmd, shell=True)
        
        # Upload script
        upload_script_cmd = f"cat {script_path} | heroku run --app {APP_NAME} \"cat > /tmp/import_script.py\""
        subprocess.run(upload_script_cmd, shell=True)
        
        # Run script
        run_cmd = f"heroku run --app {APP_NAME} \"cd /app/django_neurology_mcq && python manage.py shell -c 'exec(open(\\\"/tmp/import_script.py\\\").read())'\""
        subprocess.run(run_cmd, shell=True)
        
        print(f"Successfully imported {subspecialty} MCQs to Heroku")
    except Exception as e:
        print(f"Error importing {subspecialty}: {str(e)}")
    finally:
        # Clean up
        os.unlink(temp_path)
        os.unlink(script_path)

# Verify import
print("\nVerifying import...")
verify_cmd = f"heroku run --app {APP_NAME} \"cd /app/django_neurology_mcq && python manage.py shell -c 'from mcq.models import MCQ; from django.db.models import Count; total=MCQ.objects.count(); print(f\\\"Total MCQs: {total}\\\"); subspecialties=MCQ.objects.values(\\\"subspecialty\\\").annotate(count=Count(\\\"id\\\")); print(\\\"MCQs by subspecialty:\\\"); [print(f\\\"  {item[\\\"subspecialty\\\"]}: {item[\\\"count\\\"]}\\\") for item in subspecialties]'\""
subprocess.run(verify_cmd, shell=True)

print("Import completed!")