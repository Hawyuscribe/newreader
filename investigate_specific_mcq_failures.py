#!/usr/bin/env python
import os
import sys
import django

# Setup Django
sys.path.append('/Users/tariqalmatrudi/NEWreader/django_neurology_mcq')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
django.setup()

from mcq.models import MCQ
from mcq.mcq_case_converter import convert_mcq_to_case
import json

def investigate_specific_mcqs():
    """Investigate the specific MCQs that failed in supervised testing"""
    
    # MCQ IDs from the failed test
    failed_mcqs = [
        {'id': '43416183', 'specialty': 'Neuroimmunology', 'issue': 'missing "ms" term'},
        {'id': '99986753', 'specialty': 'Epilepsy', 'issue': 'topic mismatch (stroke → neuropathy)'}
    ]
    
    print("=== INVESTIGATING SPECIFIC MCQ FAILURES ===\n")
    
    for mcq_info in failed_mcqs:
        print(f"--- MCQ {mcq_info['id']} ({mcq_info['specialty']}) ---")
        print(f"Expected issue: {mcq_info['issue']}\n")
        
        try:
            # Try to find MCQ by original_question_number first
            mcq = None
            try:
                mcq = MCQ.objects.get(original_question_number=mcq_info['id'])
            except MCQ.DoesNotExist:
                # Try by id as fallback
                try:
                    mcq = MCQ.objects.get(id=mcq_info['id'])
                except MCQ.DoesNotExist:
                    print(f"❌ MCQ {mcq_info['id']} not found in database\n")
                    continue
            
            print(f"✅ Found MCQ: {mcq.question[:100]}...")
            print(f"   Specialty: {mcq.specialty}")
            print(f"   Subspecialty: {mcq.subspecialty}")
            print(f"   Original Question Number: {mcq.original_question_number}")
            
            # Try conversion
            print("\n🔄 Attempting conversion...")
            
            try:
                case_data = converter.convert_mcq_to_case(mcq)
                print("✅ Conversion successful!")
                
                # Analyze the converted case for the specific issues
                if mcq_info['specialty'] == 'Neuroimmunology':
                    # Check for MS terms
                    case_text = case_data.get('case_description', '').lower()
                    mcq_text = (mcq.question + ' ' + mcq.option_a + ' ' + mcq.option_b + 
                               ' ' + mcq.option_c + ' ' + mcq.option_d + ' ' + mcq.explanation).lower()
                    
                    print(f"\n🔍 Checking for MS-related terms:")
                    ms_terms = ['ms', 'multiple sclerosis', 'demyelinating', 'sclerosis']
                    
                    for term in ms_terms:
                        in_original = term in mcq_text
                        in_case = term in case_text
                        print(f"   '{term}': Original={in_original}, Case={in_case}")
                        if in_original and not in_case:
                            print(f"   ⚠️  CRITICAL TERM LOSS: '{term}' missing from case!")
                
                elif mcq_info['specialty'] == 'Epilepsy':
                    # Check for topic consistency
                    case_text = case_data.get('case_description', '').lower()
                    mcq_text = (mcq.question + ' ' + mcq.option_a + ' ' + mcq.option_b + 
                               ' ' + mcq.option_c + ' ' + mcq.option_d + ' ' + mcq.explanation).lower()
                    
                    print(f"\n🔍 Checking for topic consistency:")
                    stroke_terms = ['stroke', 'infarct', 'hemorrhage', 'ischemic']
                    neuropathy_terms = ['neuropathy', 'peripheral nerve', 'nerve damage']
                    epilepsy_terms = ['seizure', 'epilepsy', 'convulsion', 'ictal']
                    
                    print("   Stroke terms in original:", any(term in mcq_text for term in stroke_terms))
                    print("   Stroke terms in case:", any(term in case_text for term in stroke_terms))
                    print("   Neuropathy terms in original:", any(term in mcq_text for term in neuropathy_terms))
                    print("   Neuropathy terms in case:", any(term in case_text for term in neuropathy_terms))
                    print("   Epilepsy terms in original:", any(term in mcq_text for term in epilepsy_terms))
                    print("   Epilepsy terms in case:", any(term in case_text for term in epilepsy_terms))
                
                # Show case description snippet
                print(f"\n📝 Case description (first 200 chars):")
                print(f"   {case_data.get('case_description', '')[:200]}...")
                
            except Exception as e:
                print(f"❌ Conversion failed: {str(e)}")
                import traceback
                traceback.print_exc()
        
        except Exception as e:
            print(f"❌ Error processing MCQ {mcq_info['id']}: {str(e)}")
        
        print("\n" + "="*80 + "\n")
    
    # Test additional MCQs from same specialties
    print("=== TESTING ADDITIONAL MCQs FROM SAME SPECIALTIES ===\n")
    
    specialties_to_test = ['Neuroimmunology', 'Epilepsy']
    
    for specialty in specialties_to_test:
        print(f"--- Testing {specialty} MCQs ---")
        
        try:
            # Get 3 MCQs from this specialty
            mcqs = MCQ.objects.filter(specialty=specialty)[:3]
            
            if not mcqs:
                mcqs = MCQ.objects.filter(subspecialty__icontains=specialty.lower())[:3]
            
            print(f"Found {len(mcqs)} MCQs to test")
            
            for i, mcq in enumerate(mcqs, 1):
                print(f"\n  MCQ {i}: {mcq.original_question_number or mcq.id}")
                print(f"    Question: {mcq.question[:80]}...")
                
                try:
                    case_data = converter.convert_mcq_to_case(mcq)
                    print(f"    ✅ Conversion successful")
                    
                    # Quick validation for specialty-specific terms
                    case_text = case_data.get('case_description', '').lower()
                    mcq_text = (mcq.question + ' ' + mcq.explanation).lower()
                    
                    if specialty == 'Neuroimmunology':
                        ms_terms = ['ms', 'multiple sclerosis', 'demyelinating']
                        critical_loss = []
                        for term in ms_terms:
                            if term in mcq_text and term not in case_text:
                                critical_loss.append(term)
                        if critical_loss:
                            print(f"    ⚠️  Critical terms lost: {critical_loss}")
                    
                except Exception as e:
                    print(f"    ❌ Conversion failed: {str(e)}")
        
        except Exception as e:
            print(f"❌ Error testing {specialty} MCQs: {str(e)}")
        
        print()

if __name__ == "__main__":
    investigate_specific_mcqs()