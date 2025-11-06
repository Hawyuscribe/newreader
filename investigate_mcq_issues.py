#!/usr/bin/env python3
"""
Quick investigation script to check MCQ options formatting and explanation structure issues
without needing Django environment
"""

import sqlite3
import json
import os

def investigate_mcq_issues():
    """Check MCQ database for options formatting and explanation structure"""
    
    # Path to the SQLite database
    db_path = '/Users/tariqalmatrudi/NEWreader/django_neurology_mcq/neurology_mcq.db'
    
    if not os.path.exists(db_path):
        print(f"❌ Database not found at {db_path}")
        return
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        print("🔍 Investigating MCQ issues...")
        print("=" * 50)
        
        # Check total MCQ count
        cursor.execute("SELECT COUNT(*) FROM mcq_mcq")
        total_mcqs = cursor.fetchone()[0]
        print(f"📊 Total MCQs in database: {total_mcqs}")
        
        # Check for options formatting issues
        print("\n🔧 Checking options formatting...")
        cursor.execute("SELECT id, question_text, options FROM mcq_mcq LIMIT 10")
        mcqs_sample = cursor.fetchall()
        
        problematic_options = 0
        for mcq_id, question_text, options in mcqs_sample:
            if options:
                try:
                    # Check if options is a proper JSON
                    parsed_options = json.loads(options)
                    if isinstance(parsed_options, list):
                        print(f"⚠️  MCQ #{mcq_id}: Options stored as list format - {parsed_options}")
                        problematic_options += 1
                    elif isinstance(parsed_options, dict):
                        # Check if keys are proper (A, B, C, D)
                        keys = list(parsed_options.keys())
                        if all(key in ['A', 'B', 'C', 'D', 'E'] for key in keys):
                            print(f"✅ MCQ #{mcq_id}: Options properly formatted - {keys}")
                        else:
                            print(f"⚠️  MCQ #{mcq_id}: Unusual option keys - {keys}")
                            problematic_options += 1
                except json.JSONDecodeError:
                    print(f"❌ MCQ #{mcq_id}: Invalid JSON in options - {options}")
                    problematic_options += 1
        
        print(f"\n📊 Options issues found: {problematic_options}/10 sample MCQs")
        
        # Check explanation structure
        print("\n📝 Checking explanation structure...")
        cursor.execute("SELECT id, question_text, explanation_sections FROM mcq_mcq WHERE explanation_sections IS NOT NULL LIMIT 5")
        explanation_mcqs = cursor.fetchall()
        
        for mcq_id, question_text, explanation_sections in explanation_mcqs:
            if explanation_sections:
                try:
                    parsed_sections = json.loads(explanation_sections)
                    print(f"\n📋 MCQ #{mcq_id} explanation sections:")
                    if isinstance(parsed_sections, dict):
                        for key, value in parsed_sections.items():
                            status = "✅ Has content" if value and len(str(value).strip()) > 50 else "⚠️  Empty/short"
                            print(f"  - {key}: {status}")
                    else:
                        print(f"  ⚠️  Unusual format: {type(parsed_sections)}")
                except json.JSONDecodeError:
                    print(f"  ❌ Invalid JSON in explanation_sections")
        
        # Check for old-style explanations
        print("\n📰 Checking old-style explanations...")
        cursor.execute("SELECT COUNT(*) FROM mcq_mcq WHERE explanation IS NOT NULL AND explanation != ''")
        old_style_count = cursor.fetchone()[0]
        print(f"📊 MCQs with old-style explanations: {old_style_count}")
        
        cursor.execute("SELECT COUNT(*) FROM mcq_mcq WHERE explanation_sections IS NOT NULL")
        new_style_count = cursor.fetchone()[0]
        print(f"📊 MCQs with new structured explanations: {new_style_count}")
        
        conn.close()
        
        print("\n" + "=" * 50)
        print("🏁 Investigation complete!")
        
    except Exception as e:
        print(f"❌ Error investigating database: {e}")

if __name__ == "__main__":
    investigate_mcq_issues()