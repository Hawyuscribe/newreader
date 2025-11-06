#!/usr/bin/env python3
"""
Continue converting remaining explanations to structured format
Process the remaining 3000+ MCQs in batches
"""

import sqlite3
import json
import os
import re

def convert_explanation_to_structured(explanation_text):
    """Enhanced conversion of old-style explanation to new structured format"""
    if not explanation_text or len(explanation_text.strip()) < 50:
        return {}
    
    sections = {}
    text = explanation_text.strip()
    
    # Enhanced parsing patterns for medical explanations
    
    # 1. Extract option analysis section
    option_patterns = [
        r'(### Option [A-E]:|Option [A-E][\s\S]*?(?=Option [A-E]|$))',
        r'(Why.*?wrong|Why.*?correct|Option.*?analysis)[\s\S]*?(?=\n\n[A-Z]|\n##|\n###|$)',
        r'([A-E]\.\s+.*?(?=[A-E]\.\s+|$))',  # A. option B. option format
    ]
    
    for pattern in option_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE | re.MULTILINE)
        if matches:
            # Combine all option analysis
            option_analysis = '\n\n'.join(matches)
            if len(option_analysis) > 100:  # Substantial content
                sections['option_analysis'] = option_analysis.strip()
                # Remove from main text
                for match in matches:
                    text = text.replace(match, '').strip()
            break
    
    # 2. Extract clinical pearls
    pearls_patterns = [
        r'(Clinical Pearl|Pearl|Remember|Key Point|Important|Memorize)[\s\S]*?(?=\n\n[A-Z]|\n##|\n###|Evidence|Reference|$)',
        r'(\d+\.\s+.*?:.*?)(?=\d+\.|Evidence|Reference|$)',  # Numbered pearls
    ]
    
    for pattern in pearls_patterns:
        match = re.search(pattern, text, re.IGNORECASE | re.MULTILINE)
        if match:
            pearls_content = match.group(1)
            if len(pearls_content) > 50:
                sections['clinical_pearls'] = pearls_content.strip()
                text = text.replace(match.group(0), '').strip()
            break
    
    # 3. Extract evidence/guidelines section
    evidence_patterns = [
        r'(Evidence|Guideline|Reference|Study|Trial|Literature)[\s\S]*?$',
        r'(Summary of.*?Guidelines?)[\s\S]*?$',
        r'(Current.*?Evidence)[\s\S]*?$',
    ]
    
    for pattern in evidence_patterns:
        match = re.search(pattern, text, re.IGNORECASE | re.MULTILINE)
        if match:
            evidence_content = match.group(0)
            if len(evidence_content) > 50:
                sections['current_evidence'] = evidence_content.strip()
                text = text.replace(match.group(0), '').strip()
            break
    
    # 4. Extract pathophysiology section
    patho_patterns = [
        r'(Pathophysiology|Mechanism|Pathogenesis)[\s\S]*?(?=\n\n[A-Z]|\n##|\n###|Clinical|Management|Option|$)',
        r'(The.*?mechanism|Mechanism.*?involves)[\s\S]*?(?=\n\n[A-Z]|Clinical|Management|Option|$)',
    ]
    
    for pattern in patho_patterns:
        match = re.search(pattern, text, re.IGNORECASE | re.MULTILINE)
        if match:
            patho_content = match.group(0)
            if len(patho_content) > 100:
                sections['pathophysiological_mechanisms'] = patho_content.strip()
                text = text.replace(match.group(0), '').strip()
            break
    
    # 5. Extract clinical correlation
    clinical_patterns = [
        r'(Clinical.*?correlation|Clinical.*?significance|Clinical.*?presentation)[\s\S]*?(?=\n\n[A-Z]|\n##|\n###|Management|Option|Evidence|$)',
        r'(Clinically|In clinical practice)[\s\S]*?(?=\n\n[A-Z]|Management|Option|Evidence|$)',
    ]
    
    for pattern in clinical_patterns:
        match = re.search(pattern, text, re.IGNORECASE | re.MULTILINE)
        if match:
            clinical_content = match.group(0)
            if len(clinical_content) > 100:
                sections['clinical_correlation'] = clinical_content.strip()
                text = text.replace(match.group(0), '').strip()
            break
    
    # 6. Extract management/treatment section
    management_patterns = [
        r'(Management|Treatment|Therapy|Intervention)[\s\S]*?(?=\n\n[A-Z]|\n##|\n###|Option|Evidence|$)',
        r'(The.*?treatment|Treatment.*?involves)[\s\S]*?(?=\n\n[A-Z]|Option|Evidence|$)',
    ]
    
    for pattern in management_patterns:
        match = re.search(pattern, text, re.IGNORECASE | re.MULTILINE)
        if match:
            mgmt_content = match.group(0)
            if len(mgmt_content) > 100:
                sections['management_principles'] = mgmt_content.strip()
                text = text.replace(match.group(0), '').strip()
            break
    
    # 7. Extract diagnostic approach
    diagnostic_patterns = [
        r'(Diagnostic|Diagnosis|Investigation)[\s\S]*?(?=\n\n[A-Z]|\n##|\n###|Management|Option|Evidence|$)',
        r'(The.*?diagnosis|Diagnosis.*?made)[\s\S]*?(?=\n\n[A-Z]|Management|Option|Evidence|$)',
    ]
    
    for pattern in diagnostic_patterns:
        match = re.search(pattern, text, re.IGNORECASE | re.MULTILINE)
        if match:
            diag_content = match.group(0)
            if len(diag_content) > 100:
                sections['diagnostic_approach'] = diag_content.strip()
                text = text.replace(match.group(0), '').strip()
            break
    
    # 8. Everything else goes to conceptual foundation
    if text and len(text.strip()) > 50:
        sections['conceptual_foundation'] = text.strip()
    
    # If we couldn't parse into multiple sections, put everything in conceptual_foundation
    if len(sections) <= 1 and explanation_text:
        sections = {'conceptual_foundation': explanation_text.strip()}
    
    return sections

def continue_explanation_conversion(batch_size=200):
    """Continue converting explanations in batches"""
    
    db_path = '/Users/tariqalmatrudi/NEWreader/django_neurology_mcq/neurology_mcq.db'
    
    if not os.path.exists(db_path):
        print(f"❌ Database not found at {db_path}")
        return False
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        print(f"📝 Converting explanations to structured format (batch size: {batch_size})...")
        
        # Get MCQs with old-style explanations but no structured explanations
        cursor.execute(f"""
            SELECT id, explanation, question_text 
            FROM mcq_mcq 
            WHERE explanation IS NOT NULL 
            AND explanation != '' 
            AND (explanation_sections IS NULL OR explanation_sections = '{{}}' OR explanation_sections = '')
            LIMIT {batch_size}
        """)
        mcqs = cursor.fetchall()
        
        if not mcqs:
            print("✅ No more MCQs need conversion!")
            return True
        
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
                    section_count = len([k for k, v in structured_sections.items() if v and len(str(v).strip()) > 50])
                    print(f"✅ Converted MCQ #{mcq_id} ({section_count} sections): {question_text[:50]}...")
                    
            except Exception as e:
                print(f"⚠️  Could not convert MCQ #{mcq_id}: {e}")
        
        conn.commit()
        conn.close()
        
        print(f"\n✅ Successfully converted {converted_count}/{len(mcqs)} explanations")
        
        # Check remaining count
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT COUNT(*) FROM mcq_mcq 
            WHERE explanation IS NOT NULL 
            AND explanation != '' 
            AND (explanation_sections IS NULL OR explanation_sections = '{}' OR explanation_sections = '')
        """)
        remaining = cursor.fetchone()[0]
        conn.close()
        
        print(f"📊 Remaining MCQs to convert: {remaining}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error converting explanations: {e}")
        return False

def main():
    """Main function to continue explanation conversion"""
    
    print("🚀 Continuing explanation conversion...")
    print("=" * 60)
    
    # Convert in batches
    batch_count = 0
    max_batches = 15  # Convert up to 3000 MCQs (15 * 200)
    
    while batch_count < max_batches:
        print(f"\n📦 Processing batch {batch_count + 1}/{max_batches}...")
        
        if continue_explanation_conversion(batch_size=200):
            batch_count += 1
            
            # Check if there are more to convert
            db_path = '/Users/tariqalmatrudi/NEWreader/django_neurology_mcq/neurology_mcq.db'
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute("""
                SELECT COUNT(*) FROM mcq_mcq 
                WHERE explanation IS NOT NULL 
                AND explanation != '' 
                AND (explanation_sections IS NULL OR explanation_sections = '{}' OR explanation_sections = '')
            """)
            remaining = cursor.fetchone()[0]
            conn.close()
            
            if remaining == 0:
                print("🎉 All explanations have been converted!")
                break
        else:
            print("❌ Batch conversion failed")
            break
    
    print("\n" + "=" * 60)
    print("🏁 Explanation conversion session completed!")

if __name__ == "__main__":
    main()