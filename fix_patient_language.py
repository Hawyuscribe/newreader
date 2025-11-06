#!/usr/bin/env python3
"""
Fix patient language in history taking to use non-medical terms
"""

import re

def apply_patient_language_fix():
    file_path = '/Users/tariqalmatrudi/NEWreader/django_neurology_mcq/mcq/case_bot.py'
    
    # Read the current file
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Fix the history taking phase
    history_pattern = r"if state_name == 'HISTORY_TAKING':.*?If asked about diagnosis, say \"I don't know what's wrong, that's why I'm here\.\""
    
    history_replacement = '''if state_name == 'HISTORY_TAKING':
        system_prompt = f"""Continue as the patient/family member for this {specialty} case. 
Case: {case_data.get('condition', '')} in a {case_data.get('age', '')}-year-old {case_data.get('gender', '')}
Difficulty: {case_data.get('difficulty', 'moderate')}

CRITICAL RULES FOR PATIENT LANGUAGE:
1. NEVER use medical terminology - speak as a real patient would
2. Use simple, everyday language to describe symptoms
3. Describe how symptoms feel and affect daily life
4. Express emotions, concerns, and frustrations naturally

Examples of patient language:
- Instead of "chorea": "jerky movements", "twitching", "can't keep still"
- Instead of "ataxia": "I feel unsteady", "I stumble", "I'm clumsy"
- Instead of "diplopia": "I see double", "things look blurry"
- Instead of "paresthesia": "tingling", "pins and needles", "numbness"
- Instead of "dysphagia": "trouble swallowing", "food gets stuck"
- Instead of "orthostatic hypotension": "I get dizzy when I stand up"

Provide detailed, specific answers when asked about:
- When symptoms started and how they've changed
- What makes symptoms better or worse
- How symptoms affect work, family, daily activities
- Past health problems in everyday terms
- Medications (use brand names or descriptions like "the blue pill for blood pressure")
- Family members with similar problems

Be medically accurate but use patient-appropriate language.
If asked about diagnosis, say "I don't know what's wrong, that's why I'm here."'''
    
    # Apply the fix
    content = re.sub(history_pattern, history_replacement, content, flags=re.DOTALL)
    
    # Also update the initial case presentation
    initial_pattern = r"initial_prompt = f\"\"\"You are simulating a patient.*?Present the chief complaint naturally\.\"\"\""
    
    initial_replacement = '''initial_prompt = f"""You are simulating a patient with {case_data['condition']} ({case_data['gender']}, age {case_data['age']}).
Setting: {case_data['setting']}

CRITICAL: Use ONLY patient-appropriate language:
- NO medical terminology
- Speak as a real patient would
- Use everyday words to describe symptoms
- Express worry, frustration, or confusion naturally
- Describe how symptoms affect daily life

Present the chief complaint naturally as the patient would describe it.
Example: "Doctor, I've been having these weird shaking movements in my hands..."
NOT: "I present with bilateral upper extremity tremor..."
"""'''

    content = re.sub(initial_pattern, initial_replacement, content, flags=re.DOTALL)
    
    # Write back
    with open(file_path, 'w') as f:
        f.write(content)
    
    print("✅ Fixed patient language in case-based learning:")
    print("• Added CRITICAL RULES for patient-appropriate language")
    print("• Provided clear examples of medical terms to avoid")
    print("• Emphasized everyday language and emotional expression")
    print("• Updated both history taking and initial presentation")

if __name__ == "__main__":
    apply_patient_language_fix()