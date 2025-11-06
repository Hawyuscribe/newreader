#!/usr/bin/env python3
"""
Analyze AI generation bottlenecks to improve success rate to >95%
"""

import os
import sys
import django
import random
from collections import defaultdict

# Setup Django
sys.path.append('/Users/tariqalmatrudi/NEWreader/django_neurology_mcq')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
django.setup()

from mcq.models import MCQ
from mcq.mcq_case_converter import convert_mcq_to_case

class AIGenerationAnalyzer:
    def __init__(self):
        self.failure_patterns = defaultdict(list)
        self.validation_failures = defaultdict(int)
        
    def analyze_ai_failures(self, num_samples_per_specialty=10):
        """Analyze why AI generation is failing to identify improvement opportunities"""
        
        print("🔍 ANALYZING AI GENERATION BOTTLENECKS")
        print("=" * 80)
        print("Goal: Identify why AI generation fails and how to reach >95% success")
        print()
        
        # Get specialties with lower AI success rates
        problem_specialties = [
            'Vascular Neurology/Stroke',
            'Epilepsy', 
            'Neuroophthalmology',
            'Movement Disorders',
            'Critical Care Neurology'
        ]
        
        all_failures = []
        
        for specialty in problem_specialties:
            print(f"🔬 ANALYZING {specialty}")
            print("-" * 60)
            
            mcqs = list(MCQ.objects.filter(subspecialty=specialty)[:num_samples_per_specialty])
            specialty_failures = []
            
            for mcq in mcqs:
                try:
                    # Capture validation details
                    failure_info = self.analyze_single_mcq_failures(mcq)
                    if failure_info:
                        specialty_failures.append(failure_info)
                        all_failures.append(failure_info)
                        
                except Exception as e:
                    print(f"  Error analyzing MCQ {mcq.id}: {e}")
            
            # Specialty summary
            if specialty_failures:
                print(f"  📊 Found {len(specialty_failures)} AI generation failures")
                common_issues = defaultdict(int)
                for failure in specialty_failures:
                    for issue in failure['validation_errors']:
                        common_issues[issue] += 1
                
                print(f"  🚨 Top issues: {dict(list(common_issues.items())[:3])}")
            else:
                print(f"  ✅ No AI generation failures detected")
            print()
        
        # Overall analysis
        self.generate_improvement_strategy(all_failures)
        
        return all_failures
    
    def analyze_single_mcq_failures(self, mcq):
        """Analyze a single MCQ for AI generation failure patterns"""
        
        # Mock the conversion process to capture validation failures
        failure_info = None
        
        try:
            case_data = convert_mcq_to_case(mcq)
            fallback_used = case_data.get('fallback_used', False)
            
            if fallback_used:
                # This was an AI generation failure
                failure_info = {
                    'mcq_id': mcq.id,
                    'specialty': mcq.subspecialty,
                    'question_type': self.classify_question_type(mcq.question_text),
                    'question_length': len(mcq.question_text),
                    'has_specific_terms': self.has_specific_medical_terms(mcq.question_text),
                    'complexity_level': self.assess_complexity(mcq.question_text),
                    'validation_errors': self.infer_validation_errors(mcq.question_text),
                    'question_text': mcq.question_text[:100] + "..." if len(mcq.question_text) > 100 else mcq.question_text
                }
                
                print(f"  ❌ MCQ {mcq.id}: AI failed - {', '.join(failure_info['validation_errors'][:2])}")
                
        except Exception as e:
            print(f"  🚫 MCQ {mcq.id}: Conversion error - {e}")
        
        return failure_info
    
    def classify_question_type(self, question_text):
        """Classify question type"""
        text = question_text.lower()
        
        if any(word in text for word in ['treatment', 'management', 'therapy', 'next step']):
            return 'management'
        elif any(word in text for word in ['diagnosis', 'most likely', 'condition']):
            return 'diagnosis'
        elif any(word in text for word in ['test', 'investigation', 'workup']):
            return 'investigation'
        else:
            return 'other'
    
    def has_specific_medical_terms(self, question_text):
        """Check if question has specific medical terms that might cause validation issues"""
        text = question_text.lower()
        
        specific_terms = [
            'stroke', 'seizure', 'epilepsy', 'parkinson', 'huntington',
            'multiple sclerosis', 'ms', 'horner', 'lesion', 'bilateral',
            'caudate', 'thalamus', 'brainstem', 'neuropathy'
        ]
        
        found_terms = [term for term in specific_terms if term in text]
        return len(found_terms) > 0
    
    def assess_complexity(self, question_text):
        """Assess question complexity"""
        text = question_text.lower()
        
        complexity_indicators = [
            len(question_text) > 200,  # Long questions
            'post-operative' in text or 'surgery' in text,  # Surgical context
            'refractory' in text or 'failed' in text,  # Treatment failure
            text.count(',') > 3,  # Multiple clauses
            any(term in text for term in ['advanced', 'complex', 'rare'])  # Explicit complexity
        ]
        
        complexity_score = sum(complexity_indicators)
        
        if complexity_score >= 3:
            return 'high'
        elif complexity_score >= 1:
            return 'medium'
        else:
            return 'low'
    
    def infer_validation_errors(self, question_text):
        """Infer likely validation errors based on question content"""
        text = question_text.lower()
        likely_errors = []
        
        # Topic drift patterns
        if 'stroke' in text:
            likely_errors.append('STROKE_TOPIC_DRIFT')
        if 'seizure' in text or 'epilepsy' in text:
            likely_errors.append('EPILEPSY_TOPIC_DRIFT')
        if 'multiple sclerosis' in text or ' ms ' in text:
            likely_errors.append('MS_CONTEXT_LOSS')
        if 'parkinson' in text:
            likely_errors.append('MOVEMENT_DISORDER_DRIFT')
        
        # Missing context patterns
        if 'lesion' in text:
            likely_errors.append('MISSING_LESION_CONTEXT')
        if 'surgery' in text or 'surgical' in text:
            likely_errors.append('MISSING_SURGICAL_CONTEXT')
        if 'bilateral' in text:
            likely_errors.append('MISSING_BILATERAL_CONTEXT')
        
        return likely_errors if likely_errors else ['GENERAL_VALIDATION_FAILURE']
    
    def generate_improvement_strategy(self, all_failures):
        """Generate comprehensive strategy to reach >95% AI success"""
        
        print(f"🎯 STRATEGY TO REACH >95% AI GENERATION SUCCESS")
        print("=" * 80)
        
        if not all_failures:
            print("✅ No AI generation failures detected in sample!")
            print("System may already be close to 95% success rate.")
            return
        
        # Analyze failure patterns
        failure_types = defaultdict(int)
        question_types = defaultdict(int)
        complexities = defaultdict(int)
        specialties = defaultdict(int)
        
        for failure in all_failures:
            for error in failure['validation_errors']:
                failure_types[error] += 1
            question_types[failure['question_type']] += 1
            complexities[failure['complexity_level']] += 1
            specialties[failure['specialty']] += 1
        
        print(f"📊 FAILURE ANALYSIS ({len(all_failures)} total failures):")
        print(f"  Most common validation errors: {dict(list(failure_types.items())[:5])}")
        print(f"  Question types with issues: {dict(question_types)}")
        print(f"  Complexity distribution: {dict(complexities)}")
        print(f"  Problem specialties: {dict(list(specialties.items())[:3])}")
        
        print(f"\n🔧 IMPROVEMENT STRATEGIES:")
        
        # Strategy 1: Fix validation strictness
        print(f"\n1. 🎯 OPTIMIZE VALIDATION STRICTNESS")
        print(f"   Current Issue: Validation may be too strict, rejecting good cases")
        print(f"   Solution: Implement graduated validation with quality tiers")
        print(f"   Implementation:")
        print(f"   - Tier 1: Perfect preservation (current standard)")
        print(f"   - Tier 2: Good preservation (minor variations allowed)")
        print(f"   - Tier 3: Acceptable preservation (key terms preserved)")
        print(f"   - Only fallback if all tiers fail")
        
        # Strategy 2: Improve AI prompting
        print(f"\n2. 🤖 ENHANCE AI PROMPTING")
        print(f"   Current Issue: AI may need better guidance for specific scenarios")
        print(f"   Solutions:")
        print(f"   - Add few-shot examples in prompts")
        print(f"   - Use specialty-specific prompting")
        print(f"   - Implement retrieval-augmented generation (RAG)")
        print(f"   - Add negative examples (what NOT to do)")
        
        # Strategy 3: Progressive retry system
        print(f"\n3. 🔄 IMPLEMENT PROGRESSIVE RETRY SYSTEM")
        print(f"   Current Issue: Only 2 attempts before fallback")
        print(f"   Solution:")
        print(f"   - Attempt 1: Standard prompt")
        print(f"   - Attempt 2: Enhanced prompt with specific warnings")
        print(f"   - Attempt 3: Simplified case generation (reduced complexity)")
        print(f"   - Attempt 4: Template-based generation")
        print(f"   - Fallback only after 4 attempts")
        
        # Strategy 4: Adaptive prompting
        print(f"\n4. 🧠 IMPLEMENT ADAPTIVE PROMPTING")
        print(f"   Solution: Customize prompts based on:")
        print(f"   - Question complexity level")
        print(f"   - Medical specialty")
        print(f"   - Identified challenging terms")
        print(f"   - Historical failure patterns")
        
        # Strategy 5: Quality scoring refinement
        print(f"\n5. 📊 REFINE QUALITY SCORING")
        print(f"   Current Issue: Binary pass/fail validation")
        print(f"   Solution: Implement scoring system:")
        print(f"   - Content preservation: 40 points")
        print(f"   - Topic consistency: 30 points")
        print(f"   - Clinical realism: 20 points")
        print(f"   - Educational value: 10 points")
        print(f"   - Accept cases with score ≥75/100")
        
        # Strategy 6: Specific fixes for common errors
        top_errors = sorted(failure_types.items(), key=lambda x: x[1], reverse=True)[:3]
        
        print(f"\n6. 🔨 TARGET SPECIFIC ERROR PATTERNS")
        for error, count in top_errors:
            print(f"   Fix {error} ({count} occurrences):")
            if 'TOPIC_DRIFT' in error:
                print(f"   - Add stronger topic preservation constraints")
                print(f"   - Use topic-specific validation rules")
            elif 'MISSING_CONTEXT' in error:
                print(f"   - Relax context validation requirements")
                print(f"   - Allow paraphrasing of key terms")
            elif 'MS_CONTEXT' in error:
                print(f"   - Special handling for MS abbreviation")
                print(f"   - Accept 'multiple sclerosis' for 'MS'")
        
        print(f"\n🎯 IMPLEMENTATION PRIORITY:")
        print(f"1. HIGH: Implement graduated validation (Strategy 1)")
        print(f"2. HIGH: Add progressive retry system (Strategy 3)")
        print(f"3. MEDIUM: Enhance specialty-specific prompting (Strategy 2)")
        print(f"4. MEDIUM: Implement quality scoring (Strategy 5)")
        print(f"5. LOW: Add adaptive prompting (Strategy 4)")
        
        print(f"\n📈 EXPECTED OUTCOMES:")
        print(f"✅ Target: >95% AI generation success")
        print(f"✅ Improved case quality and variety")
        print(f"✅ Reduced fallback dependency")
        print(f"✅ Better user experience")

def main():
    analyzer = AIGenerationAnalyzer()
    failures = analyzer.analyze_ai_failures(num_samples_per_specialty=15)
    
    print(f"\n✅ Analysis complete!")
    print(f"📋 Ready to implement improvements for >95% AI success rate")

if __name__ == "__main__":
    main()