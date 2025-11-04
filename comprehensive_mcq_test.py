#!/usr/bin/env python3
"""
Comprehensive MCQ Testing Script for Heroku
This script provides multiple ways to test MCQ conversion
"""

import os
import sys

# Add this script to your project and deploy it
SCRIPT_CONTENT = '''
# File: django_neurology_mcq/mcq/management/commands/test_random_mcq.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from mcq.models import MCQ, MCQCaseConversionSession
from mcq.mcq_case_converter import convert_mcq_to_case, clear_mcq_cache
import json
import random
import traceback
from datetime import datetime

class Command(BaseCommand):
    help = 'Test a random MCQ conversion with comprehensive output'

    def add_arguments(self, parser):
        parser.add_argument(
            '--mcq-id',
            type=int,
            help='Specific MCQ ID to test (optional)'
        )
        parser.add_argument(
            '--exclude-id',
            type=int,
            default=100420848,
            help='MCQ ID to exclude from random selection'
        )

    def handle(self, *args, **options):
        self.stdout.write("=" * 80)
        self.stdout.write("MCQ CASE CONVERSION TEST")
        self.stdout.write("=" * 80)
        
        # Select MCQ
        mcq_id = options.get('mcq_id')
        if mcq_id:
            try:
                mcq = MCQ.objects.get(id=mcq_id)
                self.stdout.write(f"\\nTesting specific MCQ: {mcq_id}")
            except MCQ.DoesNotExist:
                self.stdout.write(self.style.ERROR(f"MCQ {mcq_id} not found!"))
                return
        else:
            # Get random MCQ
            exclude_id = options.get('exclude_id')
            mcqs = MCQ.objects.exclude(id=exclude_id).order_by('?')[:5]
            if not mcqs:
                self.stdout.write(self.style.ERROR("No MCQs found!"))
                return
            mcq = mcqs[0]
            self.stdout.write(f"\\nSelected random MCQ: {mcq.id}")
        
        # Display MCQ details
        self.stdout.write(f"\\nMCQ Details:")
        self.stdout.write(f"- ID: {mcq.id}")
        self.stdout.write(f"- Subspecialty: {mcq.subspecialty}")
        self.stdout.write(f"- Exam Type: {mcq.exam_type}")
        self.stdout.write(f"- Year: {mcq.year}")
        self.stdout.write(f"- Question: {mcq.question_text[:200]}...")
        self.stdout.write(f"- Options:")
        for i, opt in enumerate(['A', 'B', 'C', 'D', 'E']):
            option_text = getattr(mcq, f'option_{opt.lower()}', '')
            if option_text:
                self.stdout.write(f"  {opt}: {option_text[:100]}...")
        self.stdout.write(f"- Correct Answer: {mcq.correct_answer}")
        
        # Clear cache
        self.stdout.write(f"\\nClearing cache for MCQ {mcq.id}...")
        clear_mcq_cache(mcq.id)
        
        # Test conversion
        self.stdout.write("\\nStarting conversion...")
        start_time = datetime.now()
        
        try:
            case_data = convert_mcq_to_case(mcq)
            end_time = datetime.now()
            duration = (end_time - start_time).total_seconds()
            
            self.stdout.write(self.style.SUCCESS(f"\\n✅ CONVERSION SUCCESSFUL! (Duration: {duration:.2f}s)"))
            
            # Display case summary
            self.stdout.write("\\nCase Summary:")
            self.stdout.write(f"- Patient Demographics: {case_data.get('patient_demographics', 'N/A')}")
            self.stdout.write(f"- Specialty: {case_data.get('specialty', 'N/A')}")
            self.stdout.write(f"- Question Type: {case_data.get('question_type', 'N/A')}")
            self.stdout.write(f"- Difficulty: {case_data.get('difficulty', 'N/A')}")
            self.stdout.write(f"- Core Concept: {case_data.get('core_concept_type', 'N/A')}")
            
            # Display clinical presentation
            clinical = case_data.get('clinical_presentation', 'N/A')
            self.stdout.write(f"\\nClinical Presentation:")
            if len(clinical) > 500:
                self.stdout.write(f"{clinical[:500]}...")
                self.stdout.write(f"[Total length: {len(clinical)} characters]")
            else:
                self.stdout.write(clinical)
            
            # Display question prompt
            self.stdout.write(f"\\nQuestion Prompt:")
            self.stdout.write(case_data.get('question_prompt', 'N/A'))
            
            # Check validation
            if 'professional_validation' in case_data:
                val = case_data['professional_validation']
                self.stdout.write(f"\\nValidation Results:")
                self.stdout.write(f"- Passed: {val.get('passed', 'N/A')}")
                self.stdout.write(f"- Score: {val.get('score', 'N/A')}/100")
                self.stdout.write(f"- Method: {val.get('method', 'N/A')}")
                self.stdout.write(f"- Reason: {val.get('reason', 'N/A')}")
                if val.get('issues'):
                    self.stdout.write(f"- Issues: {', '.join(val['issues'])}")
            
            # Test JSON serialization
            self.stdout.write("\\nTesting JSON serialization...")
            json_str = json.dumps(case_data, indent=2)
            self.stdout.write(self.style.SUCCESS(f"✅ JSON serialization successful ({len(json_str)} characters)"))
            
            # Content alignment check
            case_text = json.dumps(case_data).lower()
            mcq_text = mcq.question_text.lower()
            
            # Extract key medical terms from MCQ
            medical_terms = [
                'parkinson', 'alzheimer', 'seizure', 'stroke', 'migraine',
                'neuropathy', 'dementia', 'epilepsy', 'tremor', 'weakness',
                'headache', 'memory', 'cognitive', 'motor', 'sensory',
                'ataxia', 'dystonia', 'myasthenia', 'multiple sclerosis', 'ms'
            ]
            
            mcq_terms = [term for term in medical_terms if term in mcq_text]
            case_terms = [term for term in medical_terms if term in case_text]
            
            self.stdout.write(f"\\nContent Alignment Check:")
            self.stdout.write(f"- Key terms in MCQ: {mcq_terms if mcq_terms else 'No specific terms found'}")
            self.stdout.write(f"- Key terms in Case: {case_terms if case_terms else 'No specific terms found'}")
            
            matching_terms = [term for term in mcq_terms if term in case_terms]
            if matching_terms:
                self.stdout.write(self.style.SUCCESS(f"✅ Case aligns with MCQ! Matching terms: {matching_terms}"))
            elif mcq_terms:
                self.stdout.write(self.style.WARNING("⚠️  Case may not perfectly align with MCQ topic"))
            
            # Check for specific issues
            if mcq.id == 100420848:  # The problematic Parkinson's MCQ
                has_parkinsons = 'parkinson' in case_text
                has_peripheral = 'peripheral neuropathy' in case_text
                self.stdout.write(f"\\nSpecial Check for MCQ 100420848:")
                self.stdout.write(f"- Contains 'Parkinson': {has_parkinsons}")
                self.stdout.write(f"- Contains 'Peripheral Neuropathy': {has_peripheral}")
                if has_parkinsons and not has_peripheral:
                    self.stdout.write(self.style.SUCCESS("✅ Correctly shows Parkinson's case!"))
                else:
                    self.stdout.write(self.style.ERROR("❌ Still showing wrong case!"))
            
            # Extended data check
            if '_extended_data' in case_data:
                self.stdout.write("\\n✅ Extended data available for future features")
            
            # System metadata
            self.stdout.write(f"\\nSystem Metadata:")
            self.stdout.write(f"- Source MCQ ID: {case_data.get('source_mcq_id', 'N/A')}")
            self.stdout.write(f"- Generator Version: {case_data.get('generator_version', 'N/A')}")
            self.stdout.write(f"- MCQ Validated: {case_data.get('mcq_source_validated', 'N/A')}")
            
        except Exception as e:
            end_time = datetime.now()
            duration = (end_time - start_time).total_seconds()
            
            self.stdout.write(self.style.ERROR(f"\\n❌ CONVERSION FAILED! (Duration: {duration:.2f}s)"))
            self.stdout.write(self.style.ERROR(f"Error: {str(e)}"))
            self.stdout.write("\\nFull traceback:")
            self.stdout.write(traceback.format_exc())
            
            # Check for specific error types
            error_str = str(e).lower()
            if 'json' in error_str and 'serializable' in error_str:
                self.stdout.write(self.style.ERROR("\\n⚠️  JSON serialization error detected!"))
            elif 'openai' in error_str or 'api' in error_str:
                self.stdout.write(self.style.ERROR("\\n⚠️  OpenAI API error detected!"))
            elif 'timeout' in error_str:
                self.stdout.write(self.style.ERROR("\\n⚠️  Timeout error detected!"))
        
        self.stdout.write("\\n" + "=" * 80)
        self.stdout.write("TEST COMPLETE")
        self.stdout.write("=" * 80)
'''

print("COMPREHENSIVE MCQ TESTING SOLUTION")
print("=" * 80)
print("\nTo enable comprehensive testing on Heroku:")
print("\n1. Create the management command file:")
print("   mkdir -p django_neurology_mcq/mcq/management/commands")
print("   touch django_neurology_mcq/mcq/management/commands/__init__.py")
print("\n2. Add the test_random_mcq.py file with the content above")
print("\n3. Deploy to Heroku")
print("\n4. Run tests with:")
print("   # Test a random MCQ:")
print("   heroku run python django_neurology_mcq/manage.py test_random_mcq --app radiant-gorge-35079")
print("\n   # Test a specific MCQ:")
print("   heroku run python django_neurology_mcq/manage.py test_random_mcq --mcq-id 100420848 --app radiant-gorge-35079")
print("\n5. Monitor logs in another terminal:")
print("   heroku logs --tail --app radiant-gorge-35079")
print("\nThis provides:")
print("- Complete MCQ details")
print("- Full case output")
print("- Validation results")
print("- Performance metrics")
print("- Error analysis")
print("- Content alignment checking")
print("- JSON serialization testing")