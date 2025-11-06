#!/usr/bin/env python
"""
Quick script to check field length on Heroku
"""
from django.db import connection

def check_field_length():
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT character_maximum_length 
            FROM information_schema.columns 
            WHERE table_name = 'mcq_mcq' 
            AND column_name = 'correct_answer'
        """)
        result = cursor.fetchone()
        if result:
            print(f"correct_answer field length: {result[0]}")
        else:
            print("Could not find field information")

if __name__ == '__main__':
    import os
    import sys
    import django
    
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
    django.setup()
    
    check_field_length()