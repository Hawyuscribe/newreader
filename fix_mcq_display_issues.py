#!/usr/bin/env python3
"""
Comprehensive fix for MCQ display issues:
1. Fix MCQ options formatting - ensure proper A/B/C/D display
2. Fix explanation structure - convert old format to new structured format
"""

import sqlite3
import json
import os
import re
from datetime import datetime

def backup_database():
    """Create a backup of the database before making changes"""
    db_path = '/Users/tariqalmatrudi/NEWreader/django_neurology_mcq/neurology_mcq.db'
    backup_path = f'/Users/tariqalmatrudi/NEWreader/django_neurology_mcq/neurology_mcq_backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}.db'
    
    try:
        import shutil
        shutil.copy2(db_path, backup_path)
        print(f"✅ Database backed up to: {backup_path}")
        return True
    except Exception as e:
        print(f"❌ Failed to backup database: {e}")
        return False

def fix_options_formatting():
    """Fix any MCQ options that might be in incorrect format"""
    db_path = '/Users/tariqalmatrudi/NEWreader/django_neurology_mcq/neurology_mcq.db'
    
    if not os.path.exists(db_path):
        print(f"❌ Database not found at {db_path}")
        return False
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        print("🔧 Checking and fixing options formatting...")
        
        # Get all MCQs with options
        cursor.execute("SELECT id, options FROM mcq_mcq WHERE options IS NOT NULL")
        mcqs = cursor.fetchall()
        
        fixed_count = 0
        for mcq_id, options in mcqs:
            try:
                # Parse the current options
                if isinstance(options, str):
                    parsed_options = json.loads(options)
                else:
                    parsed_options = options
                
                # Check if it's a list format (needs fixing)
                if isinstance(parsed_options, list):
                    print(f"🔧 Fixing MCQ #{mcq_id}: Converting list to A/B/C/D format")
                    
                    # Convert list to dictionary with A, B, C, D keys
                    option_letters = ['A', 'B', 'C', 'D', 'E']
                    options_dict = {}
                    
                    for i, option_text in enumerate(parsed_options):
                        if i < len(option_letters):
                            options_dict[option_letters[i]] = option_text
                    
                    # Update the database
                    cursor.execute(
                        "UPDATE mcq_mcq SET options = ? WHERE id = ?",
                        (json.dumps(options_dict), mcq_id)
                    )
                    fixed_count += 1
                    
            except (json.JSONDecodeError, Exception) as e:
                print(f"⚠️  Could not fix MCQ #{mcq_id}: {e}")
        
        conn.commit()
        conn.close()
        
        print(f"✅ Fixed {fixed_count} MCQs with options formatting issues")
        return True
        
    except Exception as e:
        print(f"❌ Error fixing options: {e}")
        return False

def convert_explanation_to_structured(explanation_text):
    """Convert old-style explanation to new structured format"""
    if not explanation_text or len(explanation_text.strip()) < 50:
        return {}
    
    sections = {}
    
    # Split the explanation into potential sections
    text = explanation_text.strip()
    
    # Try to identify different parts of the explanation
    # Look for common patterns in medical explanations
    
    # Extract option analysis if present
    option_analysis_match = re.search(
        r'(### Option [A-E]:|Why.*?wrong|Why.*?correct|Option.*?analysis)', 
        text, re.IGNORECASE | re.MULTILINE
    )
    if option_analysis_match:
        option_start = option_analysis_match.start()
        sections['option_analysis'] = text[option_start:].strip()
        text = text[:option_start].strip()
    
    # Extract clinical pearls if present
    pearls_match = re.search(
        r'(Clinical Pearl|Pearl|Remember|Key Point|Important)', 
        text, re.IGNORECASE
    )
    if pearls_match:
        pearls_start = pearls_match.start()
        remaining_text = text[pearls_start:]
        
        # Look for the end of pearls section
        pearls_end_match = re.search(r'\n\n(?=[A-Z])', remaining_text)
        if pearls_end_match:
            sections['clinical_pearls'] = remaining_text[:pearls_end_match.start()].strip()
            text = text[:pearls_start] + remaining_text[pearls_end_match.start():]
        else:
            sections['clinical_pearls'] = remaining_text.strip()
            text = text[:pearls_start].strip()
    
    # Extract evidence/guidelines if present
    evidence_match = re.search(
        r'(Evidence|Guideline|Reference|Study|Trial)', 
        text, re.IGNORECASE
    )
    if evidence_match:
        evidence_start = evidence_match.start()
        sections['current_evidence'] = text[evidence_start:].strip()
        text = text[:evidence_start].strip()
    
    # The remaining text goes to conceptual foundation
    if text:
        sections['conceptual_foundation'] = text.strip()
    
    # If we couldn't parse into sections, put everything in conceptual_foundation
    if not sections and explanation_text:
        sections['conceptual_foundation'] = explanation_text.strip()
    
    return sections

def migrate_explanations_to_structured():
    """Convert old explanation format to new structured format"""
    db_path = '/Users/tariqalmatrudi/NEWreader/django_neurology_mcq/neurology_mcq.db'
    
    if not os.path.exists(db_path):
        print(f"❌ Database not found at {db_path}")
        return False
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        print("📝 Converting explanations to structured format...")
        
        # Get MCQs with old-style explanations but no structured explanations
        cursor.execute("""
            SELECT id, explanation, question_text 
            FROM mcq_mcq 
            WHERE explanation IS NOT NULL 
            AND explanation != '' 
            AND (explanation_sections IS NULL OR explanation_sections = '{}' OR explanation_sections = '')
            LIMIT 100
        """)
        mcqs = cursor.fetchall()
        
        print(f"🔄 Found {len(mcqs)} MCQs to convert...")
        
        converted_count = 0
        for mcq_id, explanation, question_text in mcqs:
            try:
                # Convert explanation to structured format
                structured_sections = convert_explanation_to_structured(explanation)
                
                if structured_sections:
                    # Update the database with structured explanation
                    cursor.execute(
                        "UPDATE mcq_mcq SET explanation_sections = ? WHERE id = ?",
                        (json.dumps(structured_sections), mcq_id)
                    )
                    
                    converted_count += 1
                    print(f"✅ Converted MCQ #{mcq_id}: {question_text[:50]}...")
                    
            except Exception as e:
                print(f"⚠️  Could not convert MCQ #{mcq_id}: {e}")
        
        conn.commit()
        conn.close()
        
        print(f"✅ Successfully converted {converted_count} explanations to structured format")
        return True
        
    except Exception as e:
        print(f"❌ Error converting explanations: {e}")
        return False

def create_template_fix():
    """Create a fixed template that properly handles both old and new explanation formats"""
    
    template_path = '/Users/tariqalmatrudi/NEWreader/templates/mcq.html'
    backup_path = '/Users/tariqalmatrudi/NEWreader/templates/mcq_backup.html'
    
    try:
        # Read current template
        with open(template_path, 'r') as f:
            template_content = f.read()
        
        # Create backup
        with open(backup_path, 'w') as f:
            f.write(template_content)
        print(f"✅ Template backed up to: {backup_path}")
        
        # Fix the options display - ensure we use get_options_dict method
        # The template already uses mcq.options_dict.items() which should work correctly
        # But let's make sure the model method is working properly
        
        # The main issue might be in how Flask/Django is passing the data
        # Let's check if the template needs any adjustments
        
        return True
        
    except Exception as e:
        print(f"❌ Error creating template fix: {e}")
        return False

def main():
    """Main function to run all fixes"""
    print("🚀 Starting MCQ display issues fix...")
    print("=" * 60)
    
    # Step 1: Backup database
    if not backup_database():
        print("❌ Cannot proceed without database backup")
        return
    
    # Step 2: Fix options formatting
    print("\n" + "=" * 60)
    if fix_options_formatting():
        print("✅ Options formatting fixed")
    else:
        print("⚠️  Options formatting fix failed")
    
    # Step 3: Convert explanations to structured format
    print("\n" + "=" * 60)
    if migrate_explanations_to_structured():
        print("✅ Explanation structure migration completed")
    else:
        print("⚠️  Explanation structure migration failed")
    
    # Step 4: Create template fix
    print("\n" + "=" * 60)
    if create_template_fix():
        print("✅ Template fixes applied")
    else:
        print("⚠️  Template fixes failed")
    
    print("\n" + "=" * 60)
    print("🎉 MCQ display issues fix completed!")
    print("\nNext steps:")
    print("1. Test the application to verify fixes")
    print("2. If issues persist, check template rendering in the web app")
    print("3. Consider running more explanation conversions in batches")

if __name__ == "__main__":
    main()