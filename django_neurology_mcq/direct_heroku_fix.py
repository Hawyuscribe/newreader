#!/usr/bin/env python
"""
Direct fix for Heroku MCQ database
"""
import subprocess
import sys

def run_command(cmd):
    """Run a heroku command and return output"""
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(f"Error: {result.stderr}")
    return result.returncode == 0

def main():
    app_name = "radiant-gorge-35079"
    
    print("=== Direct Heroku MCQ Fix ===\n")
    
    # Step 1: Check current count
    print("Step 1: Checking current MCQ count...")
    cmd = f'''heroku run "python -c \\"from mcq.models import MCQ; print(f'Total MCQs: {{MCQ.objects.count()}}'); from django.db.models import Count; counts = MCQ.objects.values('subspecialty').annotate(count=Count('id')).order_by('-count'); [print(f'{{c[\\'subspecialty\\']}}: {{c[\\'count\\']}}') for c in counts[:5]]\\"" --app {app_name}'''
    run_command(cmd)
    
    # Step 2: Clear all MCQs using Django ORM
    print("\nStep 2: Clearing all MCQs...")
    clear_cmd = f'''heroku run "python -c \\"from mcq.models import MCQ, Flashcard, IncorrectAnswer, Bookmark; Flashcard.objects.all().delete(); IncorrectAnswer.objects.all().delete(); Bookmark.objects.all().delete(); deleted = MCQ.objects.all().delete(); print(f'Deleted {{deleted[0]}} MCQs')\\"" --app {app_name}'''
    if not run_command(clear_cmd):
        print("Failed to clear MCQs. Trying alternative method...")
        # Alternative: Use management command
        alt_cmd = f'heroku run "python manage.py reset_to_new_mcqs" --app {app_name}'
        run_command(alt_cmd)
    
    # Step 3: Load MCQs using management command
    print("\nStep 3: Loading new MCQs...")
    load_cmd = f'heroku run "python manage.py load_sync_chunks" --app {app_name}'
    if not run_command(load_cmd):
        print("Failed to load MCQs using chunks. Check if files exist on Heroku.")
        
    # Step 4: Verify final count
    print("\nStep 4: Verifying final count...")
    run_command(cmd)  # Run the same count command again
    
    print("\n=== Process Complete ===")
    print("If counts are still wrong, you may need to:")
    print("1. Use Django admin to manually delete MCQs")
    print("2. Run the import script locally and push to Heroku")

if __name__ == "__main__":
    main()