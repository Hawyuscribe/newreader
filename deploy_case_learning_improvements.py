#!/usr/bin/env python3
"""
Deploy Case-Based Learning Improvements to Heroku
"""

import os
import subprocess
import shutil
from datetime import datetime

def backup_current_files():
    """Backup current files before deployment"""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_dir = f'backup_case_learning_{timestamp}'
    
    files_to_backup = [
        'django_neurology_mcq/mcq/case_bot.py',
        'django_neurology_mcq/templates/mcq/case_based_learning.html'
    ]
    
    os.makedirs(backup_dir, exist_ok=True)
    
    for file_path in files_to_backup:
        if os.path.exists(file_path):
            dest_path = os.path.join(backup_dir, os.path.basename(file_path))
            shutil.copy2(file_path, dest_path)
            print(f"Backed up {file_path} to {dest_path}")
    
    return backup_dir

def apply_improvements():
    """Apply the improved files"""
    # Replace case_bot.py
    if os.path.exists('django_neurology_mcq/mcq/case_bot_improved.py'):
        shutil.copy2('django_neurology_mcq/mcq/case_bot_improved.py', 
                     'django_neurology_mcq/mcq/case_bot.py')
        print("✓ Updated case_bot.py with improvements")
    
    # Replace template
    if os.path.exists('django_neurology_mcq/templates/mcq/case_based_learning_improved.html'):
        shutil.copy2('django_neurology_mcq/templates/mcq/case_based_learning_improved.html',
                     'django_neurology_mcq/templates/mcq/case_based_learning.html')
        print("✓ Updated case_based_learning.html with improvements")
    
    # Add model additions to models.py
    models_addition = """
# Case-Based Learning Models
from django.contrib.auth.models import User

class CaseLearningSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session_id = models.CharField(max_length=50, unique=True)
    specialty = models.CharField(max_length=100)
    case_hash = models.CharField(max_length=20)
    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    final_state = models.CharField(max_length=50, default='INITIAL')
    patient_outcome = models.CharField(max_length=20, choices=[
        ('stable', 'Stable'),
        ('improving', 'Improving'),
        ('deteriorating', 'Deteriorating')
    ], default='stable')
    score = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-started_at']
        indexes = [
            models.Index(fields=['user', 'specialty']),
            models.Index(fields=['case_hash']),
        ]

class CaseLearningHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=100)
    case_hash = models.CharField(max_length=20)
    condition = models.CharField(max_length=200)
    seen_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['user', 'case_hash']
        ordering = ['-seen_at']
        indexes = [
            models.Index(fields=['user', 'specialty', '-seen_at']),
        ]
"""
    
    # Check if models need updating
    models_path = 'django_neurology_mcq/mcq/models.py'
    if os.path.exists(models_path):
        with open(models_path, 'r') as f:
            content = f.read()
        
        if 'CaseLearningSession' not in content:
            with open(models_path, 'a') as f:
                f.write('\n\n' + models_addition)
            print("✓ Added Case Learning models")

def create_deployment_script():
    """Create a script to run on Heroku"""
    script_content = """#!/bin/bash
# Deploy Case Learning Improvements

echo "Deploying Case-Based Learning improvements..."

# Create migrations if needed
python manage.py makemigrations mcq --noinput || true

# Apply migrations
python manage.py migrate --noinput

# Clear any stale cache
python -c "from django.core.cache import cache; cache.clear()"

echo "Deployment complete!"
"""
    
    with open('deploy_case_improvements.sh', 'w') as f:
        f.write(script_content)
    
    os.chmod('deploy_case_improvements.sh', 0o755)
    print("✓ Created deployment script")

def main():
    print("Case-Based Learning Improvement Deployment")
    print("=" * 50)
    
    # Step 1: Backup
    print("\n1. Backing up current files...")
    backup_dir = backup_current_files()
    
    # Step 2: Apply improvements
    print("\n2. Applying improvements...")
    apply_improvements()
    
    # Step 3: Create deployment script
    print("\n3. Creating deployment script...")
    create_deployment_script()
    
    # Step 4: Commit changes
    print("\n4. Committing changes...")
    subprocess.run(['git', 'add', '.'], check=True)
    subprocess.run(['git', 'commit', '-m', 'Improve Case-Based Learning module with session management, case variety, and better UX'], check=True)
    
    print("\n✅ All improvements applied successfully!")
    print(f"Backup saved in: {backup_dir}")
    print("\nNext steps:")
    print("1. Review the changes")
    print("2. Push to Heroku: git push heroku stable_version:main")
    print("3. Run on Heroku: heroku run bash deploy_case_improvements.sh")
    print("4. Test at: https://radiant-gorge-35079-2b52ba172c1e.herokuapp.com/case-based-learning/")

if __name__ == '__main__':
    main()