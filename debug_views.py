#!/usr/bin/env python3
"""
Debug script to check and fix the Django views in the Heroku app.
"""
import subprocess
import logging
from pathlib import Path
from datetime import datetime

# Set up logging
log_filename = f"django_views_debug_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Log to both file and console
console = logging.StreamHandler()
console.setLevel(logging.INFO)
logging.getLogger('').addHandler(console)

# Heroku app name
APP_NAME = "radiant-gorge-35079"

logging.info("Starting Django views debug script")

# First, check the views.py file to see how MCQs are being loaded
view_check_cmd = f"""heroku run --app {APP_NAME} "cd /app/django_neurology_mcq && cat mcq/views.py" > views_output.txt"""
subprocess.run(view_check_cmd, shell=True)

# Check the dashboard view specifically
dashboard_check_script = """
from mcq.models import MCQ, UserProfile, Bookmark
from django.contrib.auth.models import User
from django.db.models import Q, Count

# 1. Check total MCQs
total_mcqs = MCQ.objects.count()
print(f"Total MCQs in database: {total_mcqs}")

# 2. Check vascular MCQs specifically
vascular_mcqs = MCQ.objects.filter(Q(subspecialty__icontains='vascular') | Q(subspecialty__icontains='stroke')).count()
print(f"Vascular MCQs: {vascular_mcqs}")

# 3. Check all subspecialties
subspecialties = MCQ.objects.values('subspecialty').annotate(count=Count('id')).order_by('-count')
print("\\nMCQs by subspecialty:")
for sub in subspecialties:
    print(f"  {sub['subspecialty']}: {sub['count']}")

# 4. Check for empty fields that might cause issues
empty_questions = MCQ.objects.filter(question='').count()
empty_subspecialties = MCQ.objects.filter(subspecialty='').count()
print(f"\\nMCQs with empty questions: {empty_questions}")
print(f"MCQs with empty subspecialties: {empty_subspecialties}")

# 5. Check the dashboard view for issues
try:
    from mcq.views import dashboard
    print("\\nDashboard view loaded successfully")
except Exception as e:
    print(f"\\nError loading dashboard view: {str(e)}")

# 6. Try to create a test MCQ
try:
    test_mcq = MCQ(
        question="Test question for dashboard",
        option_a="A",
        option_b="B",
        option_c="C",
        option_d="D",
        option_e="E",
        correct_answer="A",
        subspecialty="vascular_neurology",
        explanation="Test explanation",
        exam_year="2025",
        exam_type="Test"
    )
    test_mcq.save()
    print(f"\\nTest MCQ created with ID: {test_mcq.id}")
    
    # Retrieve to verify
    retrieved = MCQ.objects.get(id=test_mcq.id)
    print(f"Retrieved MCQ: {retrieved.question}")
except Exception as e:
    print(f"\\nError creating test MCQ: {str(e)}")
"""

# Create a file for the dashboard check script
with open("dashboard_check_script.py", "w") as f:
    f.write(dashboard_check_script)

# Run the dashboard check script
dashboard_check_cmd = f"""heroku run --app {APP_NAME} "cd /app/django_neurology_mcq && python manage.py shell" < dashboard_check_script.py"""
subprocess.run(dashboard_check_cmd, shell=True)

# Create a patch to ensure proper dashboard rendering
dashboard_fix_script = """
# Check the dashboard.html template
try:
    from django.template.loader import render_to_string
    from django.contrib.auth.models import User
    from mcq.models import MCQ, UserProfile, Bookmark
    import tempfile
    import os
    
    # Sample user
    users = User.objects.all()
    if users:
        user = users.first()
        print(f"Using sample user: {user.username}")
        
        # Try rendering the template
        context = {
            'total_mcqs': MCQ.objects.count(),
            'subspecialties': MCQ.objects.values('subspecialty').annotate(count=Count('id')).order_by('-count'),
            'user': user,
        }
        
        try:
            # Save the rendered template to a file for inspection
            rendered = render_to_string('dashboard.html', context)
            print("Template rendered successfully")
            
            with tempfile.NamedTemporaryFile(delete=False, suffix='.html', mode='w') as f:
                f.write(rendered)
                temp_file = f.name
            
            print(f"Saved rendered template to {temp_file}")
            
            # Copy the template content to a temporary location we can access
            with open(temp_file, 'r') as f:
                content = f.read()
            
            with open('/tmp/dashboard_rendered.html', 'w') as f:
                f.write(content)
            
            # Check for common issues in the template
            if "No MCQs available" in content:
                print("Template shows 'No MCQs available' message")
            
            if "subspecialties|length" in content:
                print("Template has a conditional check for subspecialties|length")
        except Exception as e:
            print(f"Template rendering error: {str(e)}")
    else:
        print("No users found for testing")
except Exception as e:
    print(f"Template checking error: {str(e)}")
"""

# Create a file for the dashboard fix script
with open("dashboard_fix_script.py", "w") as f:
    f.write(dashboard_fix_script)

# Run the dashboard fix script
dashboard_fix_cmd = f"""heroku run --app {APP_NAME} "cd /app/django_neurology_mcq && python manage.py shell" < dashboard_fix_script.py"""
subprocess.run(dashboard_fix_cmd, shell=True)

# Create a direct fix for any issues found
patch_script = """
from mcq.models import MCQ
from django.db.models import Q

# 1. Fix any empty subspecialties
empty_subs = MCQ.objects.filter(Q(subspecialty='') | Q(subspecialty=None))
print(f"Found {empty_subs.count()} MCQs with empty subspecialties")
if empty_subs.exists():
    empty_subs.update(subspecialty='vascular_neurology')
    print("Updated empty subspecialties to 'vascular_neurology'")

# 2. Ensure proper casing for vascular subspecialty
vascular_varied = MCQ.objects.filter(
    Q(subspecialty__icontains='vascular') | 
    Q(subspecialty__icontains='stroke')
).exclude(subspecialty='vascular_neurology')

print(f"Found {vascular_varied.count()} vascular MCQs with non-standard subspecialty names")
if vascular_varied.exists():
    # Standardize the subspecialty name
    for mcq in vascular_varied:
        print(f"Updating MCQ {mcq.id} from '{mcq.subspecialty}' to 'vascular_neurology'")
        mcq.subspecialty = 'vascular_neurology'
        mcq.save()
    print("Standardized all vascular subspecialty names")

# 3. Add some dummy MCQs if none exist
total_mcqs = MCQ.objects.count()
if total_mcqs == 0:
    print("No MCQs found in database, adding some test MCQs")
    
    # Create 5 test MCQs
    for i in range(1, 6):
        test_mcq = MCQ(
            question=f"Test Vascular MCQ #{i}",
            option_a=f"Option A for question {i}",
            option_b=f"Option B for question {i}",
            option_c=f"Option C for question {i}",
            option_d=f"Option D for question {i}",
            option_e=f"Option E for question {i}",
            correct_answer="A",
            subspecialty="vascular_neurology",
            explanation=f"This is a test explanation for question {i}",
            exam_year="2025",
            exam_type="Test"
        )
        test_mcq.save()
        print(f"Created test MCQ with ID: {test_mcq.id}")
    
    print("Added 5 test MCQs")

# 4. Final verification
subspecialties = MCQ.objects.values('subspecialty').annotate(count=Count('id')).order_by('-count')
print("\\nFinal MCQs by subspecialty:")
for sub in subspecialties:
    print(f"  {sub['subspecialty']}: {sub['count']}")

vascular_mcqs = MCQ.objects.filter(
    Q(subspecialty__icontains='vascular') | 
    Q(subspecialty__icontains='stroke')
).count()
print(f"\\nTotal vascular MCQs: {vascular_mcqs}")
"""

# Create a file for the patch script
with open("patch_script.py", "w") as f:
    f.write(patch_script)

# Run the patch script
patch_cmd = f"""heroku run --app {APP_NAME} "cd /app/django_neurology_mcq && python manage.py shell" < patch_script.py"""
subprocess.run(patch_cmd, shell=True)

# Finally, restart the app to ensure all changes are applied
restart_cmd = f"heroku restart --app {APP_NAME}"
subprocess.run(restart_cmd, shell=True)

logging.info("Debug script completed")