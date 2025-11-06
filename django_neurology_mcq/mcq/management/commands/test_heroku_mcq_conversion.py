#!/usr/bin/env python
"""
Django management command to test MCQ conversion on Heroku
"""

from django.core.management.base import BaseCommand
from mcq.models import MCQ
from mcq.mcq_case_converter import convert_mcq_to_case
from datetime import datetime
import os
import json

class Command(BaseCommand):
    help = 'Test MCQ conversion on Heroku'

    def handle(self, *args, **options):
        self.stdout.write("🧪 Testing MCQ Conversion on Heroku")
        self.stdout.write("=" * 50)
        
        # Environment info
        dyno = os.environ.get('DYNO', 'local')
        self.stdout.write(f"Environment: {dyno}")
        
        # Test Redis
        try:
            from django.core.cache import cache
            cache.set('test_key', 'test_value', 10)
            redis_status = cache.get('test_key') == 'test_value'
            self.stdout.write(f"Redis: {'✅' if redis_status else '❌'}")
        except Exception as e:
            self.stdout.write(f"Redis: ❌ {e}")
            redis_status = False
        
        # Test OpenAI
        try:
            api_key = os.environ.get('OPENAI_API_KEY')
            openai_status = api_key is not None and len(api_key) > 10
            self.stdout.write(f"OpenAI API Key: {'✅' if openai_status else '❌'}")
        except Exception as e:
            self.stdout.write(f"OpenAI: ❌ {e}")
            openai_status = False
        
        # Get a random MCQ
        try:
            mcq = MCQ.objects.filter(subspecialty__isnull=False).order_by('?').first()
            if not mcq:
                self.stdout.write("❌ No MCQs found in database")
                return
                
            self.stdout.write(f"\n📝 Testing MCQ: {mcq.id}")
            self.stdout.write(f"Subspecialty: {mcq.subspecialty}")
            self.stdout.write(f"Question: {mcq.question_text[:100]}...")
            self.stdout.write(f"Correct Answer: {mcq.correct_answer}")
            
        except Exception as e:
            self.stdout.write(f"❌ Error getting MCQ: {e}")
            return
        
        # Test conversion
        try:
            self.stdout.write(f"\n🔄 Starting conversion at {datetime.now().strftime('%H:%M:%S')}")
            start_time = datetime.now()
            
            case_data = convert_mcq_to_case(mcq, include_debug=True)
            
            end_time = datetime.now()
            duration = (end_time - start_time).total_seconds()
            
            self.stdout.write(f"✅ Conversion completed in {duration:.2f} seconds")
            
            # Analyze results
            self.stdout.write("\n📊 RESULTS ANALYSIS:")
            self.stdout.write(f"Source MCQ ID: {case_data.get('source_mcq_id')} (Expected: {mcq.id})")
            self.stdout.write(f"MCQ ID Match: {'✅' if case_data.get('source_mcq_id') == mcq.id else '❌'}")
            self.stdout.write(f"Patient Demographics: {case_data.get('patient_demographics', 'N/A')}")
            self.stdout.write(f"Specialty: {case_data.get('specialty', 'N/A')}")
            self.stdout.write(f"Core Concept: {case_data.get('core_concept_type', 'N/A')}")
            
            # Validation info
            validation = case_data.get('professional_validation', {})
            self.stdout.write(f"\n🔍 VALIDATION:")
            self.stdout.write(f"Passed: {'✅' if validation.get('passed') else '❌'}")
            self.stdout.write(f"Score: {validation.get('score', 0)}/100")
            self.stdout.write(f"Reason: {validation.get('reason', 'N/A')}")
            
            if validation.get('issues'):
                self.stdout.write(f"Issues: {', '.join(validation['issues'])}")
            
            # Check for issues
            issues_found = []
            
            if case_data.get('source_mcq_id') != mcq.id:
                issues_found.append(f"MCQ ID mismatch: {case_data.get('source_mcq_id')} != {mcq.id}")
            
            if case_data.get('specialty') != mcq.subspecialty:
                issues_found.append(f"Specialty mismatch: {case_data.get('specialty')} != {mcq.subspecialty}")
            
            if validation.get('score', 0) < 70:
                issues_found.append(f"Low validation score: {validation.get('score')}")
            
            if not validation.get('passed'):
                issues_found.append("Validation failed")
            
            self.stdout.write(f"\n⚠️ ISSUES DETECTED: {len(issues_found)}")
            for issue in issues_found:
                self.stdout.write(f"  - {issue}")
            
            # Overall result
            success = len(issues_found) == 0 and validation.get('passed', False)
            self.stdout.write(f"\n🎯 OVERALL RESULT: {'✅ SUCCESS' if success else '❌ ISSUES FOUND'}")
            
            # Test consistency
            self.stdout.write(f"\n🔄 Testing conversion consistency...")
            consistent = True
            for i in range(3):
                try:
                    case_data_2 = convert_mcq_to_case(mcq, include_debug=False)
                    if case_data_2.get('source_mcq_id') != mcq.id:
                        self.stdout.write(f"  Attempt {i+1}: ❌ MCQ ID mismatch: {case_data_2.get('source_mcq_id')}")
                        consistent = False
                    else:
                        self.stdout.write(f"  Attempt {i+1}: ✅ MCQ ID correct: {case_data_2.get('source_mcq_id')}")
                except Exception as e:
                    self.stdout.write(f"  Attempt {i+1}: ❌ Error: {e}")
                    consistent = False
            
            self.stdout.write(f"Consistency: {'✅ CONSISTENT' if consistent else '❌ INCONSISTENT'}")
            
            # Output final result
            final_success = success and consistent
            self.stdout.write(f"\n{'='*50}")
            self.stdout.write(f"FINAL RESULT: {'✅ ALL TESTS PASSED' if final_success else '❌ ISSUES DETECTED'}")
            self.stdout.write(f"{'='*50}")
            
        except Exception as e:
            self.stdout.write(f"❌ Conversion failed: {e}")
            import traceback
            self.stdout.write(traceback.format_exc())