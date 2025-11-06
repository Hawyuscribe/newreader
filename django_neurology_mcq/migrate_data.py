#!/usr/bin/env python3
"""
Script to migrate data from the old SQLite database to the new Django database.
Run this script after running migrations but before starting the Django application.
"""

import os
import sys
import json
import sqlite3
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
django.setup()

from django.contrib.auth.models import User
from mcq.models import MCQ, Bookmark, Flashcard, Note
from django.utils import timezone
from datetime import datetime

def main():
    # Source database path
    src_db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'neurology_mcq.db')
    
    if not os.path.exists(src_db_path):
        print(f"Source database not found at {src_db_path}")
        sys.exit(1)
    
    # Connect to source database
    src_conn = sqlite3.connect(src_db_path)
    src_conn.row_factory = sqlite3.Row
    src_cursor = src_conn.cursor()
    
    # Create superuser if it doesn't exist
    if not User.objects.filter(is_superuser=True).exists():
        print("Creating superuser...")
        User.objects.create_superuser('admin', 'admin@example.com', 'admin')
    
    # Create regular user if it doesn't exist
    if not User.objects.filter(username='demo').exists():
        print("Creating demo user...")
        User.objects.create_user('demo', 'demo@example.com', 'demo')
    
    # Get the demo user
    demo_user = User.objects.get(username='demo')
    
    # Migrate MCQs
    print("Migrating MCQs...")
    src_cursor.execute('SELECT * FROM mcqs')
    mcq_map = {}  # To map old IDs to new IDs
    
    for row in src_cursor.fetchall():
        row_dict = dict(row)
        
        # Convert options to JSON if it's a string
        options = row_dict['options']
        if isinstance(options, str):
            try:
                options = json.loads(options)
            except json.JSONDecodeError:
                # If not valid JSON, keep as is
                pass
        
        mcq, created = MCQ.objects.update_or_create(
            question_number=row_dict['question_number'],
            defaults={
                'question_text': row_dict['question_text'],
                'options': options,
                'correct_answer': row_dict['correct_answer'],
                'subspecialty': row_dict['subspecialty'],
                'source_file': row_dict['source_file'],
                'exam_type': row_dict['exam_type'],
                'exam_year': row_dict['exam_year'],
                'explanation': row_dict['explanation']
            }
        )
        
        # Map old ID to new ID
        mcq_map[row_dict['id']] = mcq.id
        
        if created:
            print(f"Added MCQ: {mcq.question_number}")
        else:
            print(f"Updated MCQ: {mcq.question_number}")
    
    # Migrate Bookmarks
    print("\nMigrating Bookmarks...")
    src_cursor.execute('SELECT * FROM bookmarks')
    
    for row in src_cursor.fetchall():
        row_dict = dict(row)
        
        # Skip if the MCQ doesn't exist in our map
        if row_dict['mcq_id'] not in mcq_map:
            continue
        
        new_mcq_id = mcq_map[row_dict['mcq_id']]
        
        bookmark, created = Bookmark.objects.update_or_create(
            user=demo_user,
            mcq_id=new_mcq_id,
            defaults={
                'created_at': datetime.fromisoformat(row_dict['created_at']) if row_dict['created_at'] else timezone.now()
            }
        )
        
        if created:
            print(f"Added Bookmark for MCQ #{new_mcq_id}")
    
    # Migrate Flashcards
    print("\nMigrating Flashcards...")
    src_cursor.execute('SELECT * FROM flashcards')
    
    for row in src_cursor.fetchall():
        row_dict = dict(row)
        
        # Skip if the MCQ doesn't exist in our map
        if row_dict['mcq_id'] not in mcq_map:
            continue
        
        new_mcq_id = mcq_map[row_dict['mcq_id']]
        
        flashcard, created = Flashcard.objects.update_or_create(
            user=demo_user,
            mcq_id=new_mcq_id,
            defaults={
                'interval': row_dict['interval'],
                'next_review': datetime.fromisoformat(row_dict['next_review']) if row_dict['next_review'] else timezone.now(),
                'last_reviewed': datetime.fromisoformat(row_dict['last_reviewed']) if row_dict['last_reviewed'] else None,
                'ease_factor': row_dict['ease_factor'],
                'created_at': datetime.fromisoformat(row_dict['created_at']) if row_dict['created_at'] else timezone.now()
            }
        )
        
        if created:
            print(f"Added Flashcard for MCQ #{new_mcq_id}")
    
    # Migrate Notes
    print("\nMigrating Notes...")
    src_cursor.execute('SELECT * FROM notes')
    
    for row in src_cursor.fetchall():
        row_dict = dict(row)
        
        # Skip if the MCQ doesn't exist in our map
        if row_dict['mcq_id'] not in mcq_map:
            continue
        
        new_mcq_id = mcq_map[row_dict['mcq_id']]
        
        note, created = Note.objects.update_or_create(
            user=demo_user,
            mcq_id=new_mcq_id,
            defaults={
                'note_text': row_dict['note_text'],
                'created_at': datetime.fromisoformat(row_dict['created_at']) if row_dict['created_at'] else timezone.now(),
                'updated_at': datetime.fromisoformat(row_dict['updated_at']) if row_dict['updated_at'] else timezone.now()
            }
        )
        
        if created:
            print(f"Added Note for MCQ #{new_mcq_id}")
    
    # Close connections
    src_conn.close()
    
    print("\nData migration complete!")

if __name__ == "__main__":
    main()