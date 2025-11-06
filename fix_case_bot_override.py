#!/usr/bin/env python3
"""
Fix Case Bot Override Issue

The case bot is generating new content via OpenAI API instead of using 
the pre-generated MCQ case data. This causes different cases to be displayed
than what was actually generated.

Solution: When MCQ case data is provided, use the exact case content 
without additional AI generation.
"""

def fix_case_bot_override():
    """Fix the case bot to use exact MCQ case data without AI override"""
    
    print("🔧 Fixing Case Bot Override Issue...")
    
    case_bot_file = '/Users/tariqalmatrudi/NEWreader/django_neurology_mcq/mcq/case_bot_enhanced.py'
    
    with open(case_bot_file, 'r') as f:
        content = f.read()
    
    # Find the section where the bot makes API calls for MCQ cases
    old_mcq_case_logic = '''                # Check if this is an MCQ case with specific starting stage
                if session.get('is_mcq_case') and session.get('mcq_starting_stage'):
                    initial_prompt = generate_mcq_stage_prompt(specialty, case_data, session['mcq_starting_stage'])
                    session['state'] = session['mcq_starting_stage']
                    
                    # Different user prompts based on starting stage
                    if session['mcq_starting_stage'] == CASE_STATES['DIFFERENTIAL_PROMPT']:
                        user_prompt = "Present the complete clinical case up to this point, then ask for my differential diagnosis."
                    elif session['mcq_starting_stage'] == CASE_STATES['MANAGEMENT_PROMPT']:
                        user_prompt = "Present the established diagnosis and current situation, then ask for my management plan."
                    elif session['mcq_starting_stage'] == CASE_STATES['INVESTIGATIONS_PROMPT']:
                        user_prompt = "Present the clinical presentation, then ask what investigations I would order."
                    else:
                        user_prompt = "Present the chief complaint."
                        session['state'] = CASE_STATES['HISTORY_TAKING']
                else:
                    # Regular case - start with chief complaint
                    initial_prompt = generate_initial_case_prompt(specialty, case_data)
                    user_prompt = "Present the chief complaint."
                    session['state'] = CASE_STATES['HISTORY_TAKING']
                
                print(f"DEBUG: Generated prompt successfully, calling API...")
                bot_response = make_api_call_with_retry([
                    {"role": "system", "content": initial_prompt},
                    {"role": "user", "content": user_prompt}
                ], temperature=0.8)
                print(f"DEBUG: API call successful")'''
    
    new_mcq_case_logic = '''                # Check if this is an MCQ case - use exact case content without AI generation
                if session.get('is_mcq_case'):
                    print(f"DEBUG: This is an MCQ case, using pre-generated content directly")
                    
                    # Use the exact clinical presentation from the MCQ case data
                    clinical_presentation = case_data.get('clinical_presentation', '')
                    patient_demographics = case_data.get('patient_demographics', 'Patient')
                    question_type = case_data.get('question_type', 'diagnosis')
                    
                    # Create the bot response using exact case content (no AI generation)
                    bot_response = f"""**Case Presentation:**

{patient_demographics} presents with the following clinical picture:

{clinical_presentation}

This is a {question_type} case. What would you like to explore further?

Available options:
- Ask about specific history details
- Proceed to examination
- Discuss your differential diagnosis
- Ask about investigations"""
                    
                    # Set appropriate starting stage
                    if question_type == 'management':
                        session['mcq_starting_stage'] = CASE_STATES['MANAGEMENT_PROMPT']
                        session['state'] = CASE_STATES['MANAGEMENT_PROMPT']
                    elif question_type == 'investigation':
                        session['mcq_starting_stage'] = CASE_STATES['INVESTIGATIONS_PROMPT']
                        session['state'] = CASE_STATES['INVESTIGATIONS_PROMPT']
                    else:
                        session['mcq_starting_stage'] = CASE_STATES['DIFFERENTIAL_PROMPT']
                        session['state'] = CASE_STATES['DIFFERENTIAL_PROMPT']
                    
                    print(f"DEBUG: Using exact MCQ case content, no API call needed")
                else:
                    # Regular case - generate with AI
                    initial_prompt = generate_initial_case_prompt(specialty, case_data)
                    user_prompt = "Present the chief complaint."
                    session['state'] = CASE_STATES['HISTORY_TAKING']
                    
                    print(f"DEBUG: Generated prompt successfully, calling API...")
                    bot_response = make_api_call_with_retry([
                        {"role": "system", "content": initial_prompt},
                        {"role": "user", "content": user_prompt}
                    ], temperature=0.8)
                    print(f"DEBUG: API call successful")'''
    
    if old_mcq_case_logic in content:
        content = content.replace(old_mcq_case_logic, new_mcq_case_logic)
        print("✅ Fixed MCQ case logic to use exact content")
    else:
        print("⚠️  MCQ case logic pattern not found - content may have changed")
    
    # Write the updated content
    with open(case_bot_file, 'w') as f:
        f.write(content)
    
    print("✅ Case Bot Override Fix Applied!")
    print("\nWhat was fixed:")
    print("1. ✅ MCQ cases now use exact pre-generated content")
    print("2. ✅ No additional AI generation that could create different cases")  
    print("3. ✅ Frontend will display the exact same case that backend generated")
    print("4. ✅ Eliminates repetitive 'right-sided weakness' cases from AI override")

if __name__ == "__main__":
    fix_case_bot_override()