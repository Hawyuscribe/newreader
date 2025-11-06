#!/usr/bin/env python3
"""
Cycle 2: Comprehensive MCQ Testing with Enhanced Analysis
Building on previous improvements to achieve even higher quality
"""

import os
import sys
import django
import random
from collections import defaultdict
import json

# Setup Django
sys.path.append('/Users/tariqalmatrudi/NEWreader/django_neurology_mcq')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
django.setup()

from mcq.models import MCQ
from mcq.mcq_case_converter import convert_mcq_to_case, detect_question_type

class Cycle2Analyzer:
    def __init__(self):
        self.cycle_results = []
        self.specialty_performance = {}
        self.issue_patterns = defaultdict(list)
        
    def run_cycle_2_testing(self, mcqs_per_specialty=5):
        """Run Cycle 2 with more rigorous testing"""
        print("🚀 CYCLE 2: COMPREHENSIVE MCQ-TO-CASE TESTING")
        print("=" * 100)
        print("Building on previous improvements - Testing for remaining edge cases and quality issues")
        print()
        
        # Get all specialties with sufficient MCQs
        specialties = MCQ.objects.values_list('subspecialty', flat=True).distinct()
        specialties = [s for s in specialties if s and s.strip()]
        
        # Filter specialties with enough MCQs
        valid_specialties = []
        for specialty in specialties:
            count = MCQ.objects.filter(subspecialty=specialty).count()
            if count >= mcqs_per_specialty:
                valid_specialties.append((specialty, count))
        
        # Sort by MCQ count for better representation
        valid_specialties.sort(key=lambda x: x[1], reverse=True)
        
        print(f"📊 Testing {len(valid_specialties)} specialties with ≥{mcqs_per_specialty} MCQs each")
        print(f"Total MCQs in database: {MCQ.objects.count()}")
        print()
        
        all_results = []
        
        for i, (specialty, mcq_count) in enumerate(valid_specialties, 1):
            print(f"\n🏥 {i}/{len(valid_specialties)}: {specialty} ({mcq_count} MCQs available)")
            print("-" * 80)
            
            # Get random MCQs from this specialty
            mcqs = list(MCQ.objects.filter(subspecialty=specialty))
            test_mcqs = random.sample(mcqs, mcqs_per_specialty)
            
            specialty_results = []
            
            for j, mcq in enumerate(test_mcqs, 1):
                print(f"  {j}/{mcqs_per_specialty}: MCQ {mcq.id} - ", end="")
                
                try:
                    # Comprehensive analysis
                    result = self.analyze_single_mcq_enhanced(mcq)
                    specialty_results.append(result)
                    all_results.append(result)
                    
                    # Quick status
                    overall_score = result['overall_quality_score']
                    if result['critical_failure']:
                        print(f"❌ CRITICAL FAILURE ({overall_score:.0f}%)")
                    elif overall_score >= 90:
                        print(f"🎉 EXCELLENT ({overall_score:.0f}%)")
                    elif overall_score >= 75:
                        print(f"✅ GOOD ({overall_score:.0f}%)")
                    elif overall_score >= 60:
                        print(f"🟡 FAIR ({overall_score:.0f}%)")
                    else:
                        print(f"⚠️ POOR ({overall_score:.0f}%)")
                    
                    # Show critical issues
                    if result['critical_issues']:
                        print(f"      Critical: {', '.join(result['critical_issues'][:2])}")
                    
                except Exception as e:
                    print(f"❌ ERROR: {e}")
                    result = {
                        'mcq_id': mcq.id,
                        'specialty': specialty,
                        'overall_quality_score': 0,
                        'critical_failure': True,
                        'critical_issues': ['CONVERSION_ERROR'],
                        'error': str(e)
                    }
                    specialty_results.append(result)
                    all_results.append(result)
            
            # Specialty summary
            self.analyze_specialty_performance(specialty, specialty_results)
        
        # Overall cycle analysis
        self.analyze_cycle_2_results(all_results)
        
        return all_results
    
    def analyze_single_mcq_enhanced(self, mcq):
        """Enhanced analysis with stricter quality criteria"""
        
        result = {
            'mcq_id': mcq.id,
            'specialty': getattr(mcq, 'subspecialty', 'Unknown'),
            'original_question': mcq.question_text,
            'correct_answer': mcq.correct_answer,
            'critical_failure': False,
            'critical_issues': [],
            'quality_issues': [],
            'overall_quality_score': 0,
            'component_scores': {
                'content_preservation': 0,
                'purpose_alignment': 0,
                'clinical_realism': 0,
                'educational_value': 0
            }
        }
        
        # Detect expected question type
        expected_type = detect_question_type(mcq)
        result['expected_question_type'] = expected_type
        
        # Convert MCQ to case
        case_data = convert_mcq_to_case(mcq)
        
        # Extract case details
        clinical_presentation = case_data.get('clinical_presentation', '')
        patient_demographics = case_data.get('patient_demographics', '')
        generated_type = case_data.get('question_type', '')
        fallback_used = case_data.get('fallback_used', False)
        
        result['generated_case'] = {
            'clinical_presentation': clinical_presentation,
            'patient_demographics': patient_demographics,
            'question_type': generated_type,
            'fallback_used': fallback_used
        }
        
        # 1. CRITICAL FAILURE CHECKS
        if fallback_used:
            result['critical_issues'].append('FALLBACK_USED')
            result['critical_failure'] = True
        
        if not clinical_presentation or len(clinical_presentation.strip()) < 20:
            result['critical_issues'].append('INSUFFICIENT_CONTENT')
            result['critical_failure'] = True
        
        # Critical medical terms preservation
        critical_terms = self.extract_critical_medical_terms(mcq.question_text)
        missing_critical = []
        if critical_terms:
            presentation_lower = clinical_presentation.lower()
            for term in critical_terms:
                if term not in presentation_lower:
                    missing_critical.append(term)
            
            if missing_critical:
                result['critical_issues'].append(f'MISSING_CRITICAL_TERMS: {", ".join(missing_critical[:3])}')
                if len(missing_critical) >= 2:  # Multiple missing critical terms = critical failure
                    result['critical_failure'] = True
        
        # Topic consistency check
        topic_consistent = self.check_topic_consistency(mcq.question_text, clinical_presentation)
        if not topic_consistent:
            result['critical_issues'].append('MAJOR_TOPIC_DRIFT')
            result['critical_failure'] = True
        
        # 2. COMPONENT SCORING (only if not critical failure)
        if not result['critical_failure']:
            # Content Preservation Score
            result['component_scores']['content_preservation'] = self.score_content_preservation(mcq, case_data, critical_terms, missing_critical)
            
            # Purpose Alignment Score
            result['component_scores']['purpose_alignment'] = self.score_purpose_alignment(expected_type, generated_type, mcq, case_data)
            
            # Clinical Realism Score
            result['component_scores']['clinical_realism'] = self.score_clinical_realism(case_data)
            
            # Educational Value Score
            result['component_scores']['educational_value'] = self.score_educational_value(mcq, case_data)
            
            # Overall quality score
            scores = list(result['component_scores'].values())
            result['overall_quality_score'] = sum(scores) / len(scores)
        else:
            result['overall_quality_score'] = 20  # Critical failure gets low score
        
        return result
    
    def extract_critical_medical_terms(self, question_text):
        """Extract critical medical terms that MUST be preserved"""
        text = question_text.lower()
        
        critical_terms = []
        
        # Specific conditions
        conditions = [
            'multiple sclerosis', 'ms', 'parkinson', 'huntington', 'alzheimer',
            'horner syndrome', 'horner', 'guillain barre', 'gbs', 'myasthenia gravis',
            'stroke', 'tia', 'seizure', 'epilepsy', 'migraine', 'cluster headache'
        ]
        
        # Anatomical specifics
        anatomy = [
            'bilateral caudate', 'caudate', 'putamen', 'thalamus', 'brainstem',
            'frontal lobe', 'temporal lobe', 'parietal lobe', 'cerebellum'
        ]
        
        # Clinical signs
        signs = [
            'ptosis', 'miosis', 'anhidrosis', 'diplopia', 'nystagmus',
            'tremor', 'rigidity', 'bradykinesia', 'chorea', 'dystonia',
            'hemiparesis', 'paraparesis', 'aphasia', 'dysarthria'
        ]
        
        # Advanced procedures
        procedures = [
            'thalamotomy', 'dbs', 'deep brain stimulation', 'vns',
            'hemispherectomy', 'cabg', 'bypass surgery'
        ]
        
        all_terms = conditions + anatomy + signs + procedures
        
        for term in all_terms:
            if term in text:
                critical_terms.append(term)
        
        return critical_terms
    
    def check_topic_consistency(self, original_question, clinical_presentation):
        """Check if topics are consistent between original and generated"""
        original_lower = original_question.lower()
        case_lower = clinical_presentation.lower()
        
        # Define medical domains
        domains = {
            'movement_disorders': ['parkinson', 'huntington', 'chorea', 'tremor', 'rigidity', 'bradykinesia', 'dystonia'],
            'multiple_sclerosis': ['multiple sclerosis', 'ms', 'demyelinating', 'oligoclonal'],
            'stroke_vascular': ['stroke', 'tia', 'infarct', 'hemorrhage', 'ischemic'],
            'epilepsy': ['seizure', 'epilepsy', 'ictal', 'convulsion'],
            'dementia_cognitive': ['alzheimer', 'dementia', 'cognitive impairment', 'memory loss'],
            'headache': ['migraine', 'headache', 'cluster'],
            'neuropathy': ['neuropathy', 'guillain', 'weakness', 'peripheral nerve'],
            'horner_syndrome': ['horner', 'ptosis', 'miosis', 'anhidrosis'],
            'cardiac_surgery': ['cabg', 'bypass', 'cardiac surgery', 'coronary']
        }
        
        original_domains = set()
        case_domains = set()
        
        for domain, keywords in domains.items():
            if any(kw in original_lower for kw in keywords):
                original_domains.add(domain)
            if any(kw in case_lower for kw in keywords):
                case_domains.add(domain)
        
        # If original has clear domain but case has different domain = inconsistent
        if original_domains and case_domains:
            return bool(original_domains.intersection(case_domains))
        
        return True  # If no clear domains detected, assume consistent
    
    def score_content_preservation(self, mcq, case_data, critical_terms, missing_critical):
        """Score content preservation quality"""
        score = 100
        
        # Heavy penalty for missing critical terms
        if missing_critical:
            score -= len(missing_critical) * 20
        
        # Check for key contextual elements
        original_lower = mcq.question_text.lower()
        case_lower = case_data.get('clinical_presentation', '').lower()
        
        # Age preservation
        age_original = self.extract_age(original_lower)
        age_case = self.extract_age(case_lower)
        if age_original and age_case:
            age_diff = abs(int(age_original) - int(age_case))
            if age_diff > 15:
                score -= 10
        
        # Gender preservation
        if 'female' in original_lower and 'male' in case_lower:
            score -= 15
        elif 'male' in original_lower and 'female' in case_lower:
            score -= 15
        
        return max(0, score)
    
    def score_purpose_alignment(self, expected_type, generated_type, mcq, case_data):
        """Score purpose alignment quality"""
        score = 100
        
        # Perfect alignment
        if expected_type == generated_type:
            return score
        
        # Acceptable alignments
        acceptable_mappings = {
            'diagnosis': ['diagnosis'],
            'management': ['management', 'advanced_management'],
            'investigation': ['investigation'],
            'advanced_management': ['advanced_management', 'management']
        }
        
        if generated_type in acceptable_mappings.get(expected_type, []):
            score -= 10  # Minor penalty for close but not exact
        else:
            score -= 30  # Major penalty for mismatch
        
        return max(0, score)
    
    def score_clinical_realism(self, case_data):
        """Score clinical realism"""
        score = 100
        
        clinical_presentation = case_data.get('clinical_presentation', '')
        patient_demographics = case_data.get('patient_demographics', '')
        
        # Length check
        if len(clinical_presentation) < 50:
            score -= 20
        
        # Clinical language
        clinical_words = ['presents', 'history', 'examination', 'symptoms', 'reports', 'complains']
        if not any(word in clinical_presentation.lower() for word in clinical_words):
            score -= 15
        
        # Specific details
        if not any(char.isdigit() for char in clinical_presentation):
            score -= 10
        
        # Demographics quality
        if not patient_demographics or 'year-old' not in patient_demographics:
            score -= 15
        
        return max(0, score)
    
    def score_educational_value(self, mcq, case_data):
        """Score educational value"""
        score = 100
        
        clinical_presentation = case_data.get('clinical_presentation', '')
        
        # Teaching progression
        if len(clinical_presentation) < 100:
            score -= 15  # Too brief for good teaching case
        
        # Clinical complexity appropriate to question
        if 'advanced' in mcq.question_text.lower() or 'refractory' in mcq.question_text.lower():
            if not any(indicator in clinical_presentation.lower() for indicator in ['failed', 'mg', 'dose']):
                score -= 20
        
        return max(0, score)
    
    def extract_age(self, text):
        """Extract age from text"""
        import re
        age_match = re.search(r'(\d+)[-\s]year[-\s]old', text)
        if age_match:
            return age_match.group(1)
        return None
    
    def analyze_specialty_performance(self, specialty, results):
        """Analyze performance for a single specialty"""
        if not results:
            return
        
        total = len(results)
        critical_failures = len([r for r in results if r['critical_failure']])
        excellent = len([r for r in results if r['overall_quality_score'] >= 90])
        good = len([r for r in results if 75 <= r['overall_quality_score'] < 90])
        
        avg_score = sum(r['overall_quality_score'] for r in results) / total
        
        # Component averages
        component_avgs = {}
        for component in ['content_preservation', 'purpose_alignment', 'clinical_realism', 'educational_value']:
            component_avgs[component] = sum(r['component_scores'][component] for r in results) / total
        
        self.specialty_performance[specialty] = {
            'total_tested': total,
            'critical_failures': critical_failures,
            'excellent_count': excellent,
            'good_count': good,
            'avg_score': avg_score,
            'component_averages': component_avgs,
            'success_rate': ((total - critical_failures) / total) * 100
        }
        
        print(f"    📊 {specialty}: {avg_score:.1f}% avg | {excellent + good}/{total} good+ | {critical_failures} critical failures")
    
    def analyze_cycle_2_results(self, all_results):
        """Comprehensive analysis of Cycle 2 results"""
        print(f"\n{'='*100}")
        print(f"📊 CYCLE 2 COMPREHENSIVE ANALYSIS")
        print(f"{'='*100}")
        
        total_tested = len(all_results)
        critical_failures = len([r for r in all_results if r['critical_failure']])
        excellent = len([r for r in all_results if r['overall_quality_score'] >= 90])
        good = len([r for r in all_results if 75 <= r['overall_quality_score'] < 90])
        fair = len([r for r in all_results if 60 <= r['overall_quality_score'] < 75])
        poor = len([r for r in all_results if r['overall_quality_score'] < 60])
        
        print(f"\n🎯 OVERALL PERFORMANCE:")
        print(f"  Total MCQs Tested: {total_tested}")
        print(f"  Critical Failures: {critical_failures}/{total_tested} ({critical_failures/total_tested*100:.1f}%)")
        print(f"  Success Rate: {(total_tested-critical_failures)/total_tested*100:.1f}%")
        
        print(f"\n📈 QUALITY DISTRIBUTION:")
        print(f"  🎉 Excellent (≥90%): {excellent}/{total_tested} ({excellent/total_tested*100:.1f}%)")
        print(f"  ✅ Good (75-89%): {good}/{total_tested} ({good/total_tested*100:.1f}%)")
        print(f"  🟡 Fair (60-74%): {fair}/{total_tested} ({fair/total_tested*100:.1f}%)")
        print(f"  ⚠️ Poor (<60%): {poor}/{total_tested} ({poor/total_tested*100:.1f}%)")
        
        # Component analysis
        if total_tested > 0:
            component_averages = {}
            for component in ['content_preservation', 'purpose_alignment', 'clinical_realism', 'educational_value']:
                component_averages[component] = sum(r['component_scores'][component] for r in all_results) / total_tested
            
            print(f"\n📊 COMPONENT AVERAGES:")
            for component, avg in component_averages.items():
                print(f"  {component.replace('_', ' ').title()}: {avg:.1f}%")
        
        # Issue analysis
        all_critical_issues = []
        all_quality_issues = []
        
        for result in all_results:
            all_critical_issues.extend(result['critical_issues'])
            all_quality_issues.extend(result.get('quality_issues', []))
        
        if all_critical_issues:
            critical_counts = defaultdict(int)
            for issue in all_critical_issues:
                critical_counts[issue] += 1
            
            print(f"\n🚨 TOP CRITICAL ISSUES:")
            for issue, count in sorted(critical_counts.items(), key=lambda x: x[1], reverse=True)[:5]:
                percentage = count / total_tested * 100
                print(f"  {issue}: {count} cases ({percentage:.1f}%)")
        
        # Specialty rankings
        print(f"\n🏆 TOP PERFORMING SPECIALTIES:")
        sorted_specialties = sorted(self.specialty_performance.items(), 
                                  key=lambda x: x[1]['avg_score'], reverse=True)
        
        for specialty, perf in sorted_specialties[:5]:
            score = perf['avg_score']
            success_rate = perf['success_rate']
            print(f"  {specialty}: {score:.1f}% avg ({success_rate:.1f}% success)")
        
        print(f"\n📉 SPECIALTIES NEEDING ATTENTION:")
        for specialty, perf in sorted_specialties[-5:]:
            score = perf['avg_score']
            success_rate = perf['success_rate']
            if score < 80:
                print(f"  {specialty}: {score:.1f}% avg ({success_rate:.1f}% success)")
        
        # Generate improvement recommendations
        self.generate_cycle_2_recommendations(all_results, critical_counts if 'critical_counts' in locals() else {})
    
    def generate_cycle_2_recommendations(self, all_results, critical_issues):
        """Generate specific improvement recommendations for Cycle 2"""
        print(f"\n🔧 CYCLE 2 IMPROVEMENT RECOMMENDATIONS:")
        print("-" * 50)
        
        total_tested = len(all_results)
        critical_failures = len([r for r in all_results if r['critical_failure']])
        
        if critical_failures > 0:
            failure_rate = critical_failures / total_tested * 100
            if failure_rate > 10:
                print(f"1. 🚨 URGENT: Reduce critical failure rate ({failure_rate:.1f}%)")
                
                # Analyze most common critical issues
                for issue, count in critical_issues.items():
                    if count >= total_tested * 0.05:  # >5% prevalence
                        if 'FALLBACK_USED' in issue:
                            print(f"   → Fix AI generation failures causing fallbacks")
                        elif 'MISSING_CRITICAL_TERMS' in issue:
                            print(f"   → Strengthen validation for critical medical terms")
                        elif 'MAJOR_TOPIC_DRIFT' in issue:
                            print(f"   → Improve topic consistency in AI prompts")
        
        # Component-specific recommendations
        component_averages = {}
        for component in ['content_preservation', 'purpose_alignment', 'clinical_realism', 'educational_value']:
            component_averages[component] = sum(r['component_scores'][component] for r in all_results) / total_tested
        
        for component, avg in component_averages.items():
            if avg < 85:
                print(f"2. Improve {component.replace('_', ' ')}: {avg:.1f}% (target: ≥85%)")
        
        # Overall assessment
        overall_avg = sum(r['overall_quality_score'] for r in all_results) / total_tested
        excellent_rate = len([r for r in all_results if r['overall_quality_score'] >= 90]) / total_tested * 100
        
        print(f"\n🎯 CYCLE 2 ASSESSMENT:")
        if excellent_rate >= 70:
            print(f"🎉 EXCELLENT: {excellent_rate:.1f}% excellent cases - System performing very well!")
        elif excellent_rate >= 50:
            print(f"✅ GOOD: {excellent_rate:.1f}% excellent cases - System working well with room for improvement")
        elif excellent_rate >= 30:
            print(f"🟡 FAIR: {excellent_rate:.1f}% excellent cases - Significant improvements needed")
        else:
            print(f"⚠️ POOR: {excellent_rate:.1f}% excellent cases - Major improvements required")

def main():
    """Run Cycle 2 comprehensive testing"""
    analyzer = Cycle2Analyzer()
    results = analyzer.run_cycle_2_testing(mcqs_per_specialty=5)
    
    print(f"\n✅ Cycle 2 testing complete!")
    print(f"Results analyzed for {len(results)} total MCQ conversions.")

if __name__ == "__main__":
    main()