#!/usr/bin/env python3
"""
Comprehensive MCQ-to-Case conversion testing and improvement system
Tests MCQs from all specialties, analyzes results, and provides fix recommendations
"""

import os
import sys
import django
import random
import json
from datetime import datetime
from collections import defaultdict

# Setup Django
sys.path.append('/Users/tariqalmatrudi/NEWreader/django_neurology_mcq')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
django.setup()

from mcq.models import MCQ
from mcq.mcq_case_converter import convert_mcq_to_case

class MCQTestingSystem:
    def __init__(self):
        self.test_results = []
        self.specialty_results = defaultdict(list)
        self.current_cycle = 1
        
    def get_all_specialties(self):
        """Get all subspecialties from the database"""
        specialties = MCQ.objects.values_list('subspecialty', flat=True).distinct()
        specialties = [s for s in specialties if s and s.strip()]
        return sorted(specialties)
    
    def get_random_mcqs_by_specialty(self, specialty, count):
        """Get random MCQs from a specific specialty"""
        mcqs = list(MCQ.objects.filter(subspecialty=specialty))
        if len(mcqs) < count:
            return mcqs  # Return all if less than requested
        return random.sample(mcqs, count)
    
    def extract_key_terms_from_mcq(self, question_text):
        """Extract important medical terms from MCQ for validation"""
        text = question_text.lower()
        
        # Medical conditions and key terms
        medical_terms = [
            'stroke', 'seizure', 'epilepsy', 'parkinson', 'huntington', 'alzheimer',
            'multiple sclerosis', 'ms', 'migraine', 'headache', 'neuropathy', 'myopathy',
            'weakness', 'paralysis', 'tremor', 'rigidity', 'chorea', 'dystonia',
            'ataxia', 'aphasia', 'dysarthria', 'dysphagia', 'diplopia',
            'dementia', 'cognitive', 'memory', 'confusion', 'horner',
            'bilateral', 'left', 'right', 'frontal', 'temporal', 'parietal',
            'brainstem', 'cerebellum', 'spinal', 'caudate', 'putamen',
            'ct', 'mri', 'eeg', 'emg', 'csf', 'lumbar puncture',
            'surgery', 'surgical', 'cabg', 'bypass', 'cardiac',
            'hypertension', 'diabetes', 'atrial fibrillation',
            'thalamotomy', 'dbs', 'vns', 'refractory', 'intractable',
            'cocaine', 'amphetamine', 'ptosis', 'miosis', 'anhidrosis'
        ]
        
        found_terms = []
        for term in medical_terms:
            if term in text:
                found_terms.append(term)
        
        return found_terms
    
    def detect_advanced_management(self, question_text):
        """Detect if this is an advanced management question"""
        text = question_text.lower()
        advanced_keywords = [
            'thalamotomy', 'dbs', 'deep brain stimulation', 'vns', 'vagal nerve stimulation',
            'epilepsy surgery', 'hemispherectomy', 'corpus callosotomy',
            'refractory', 'intractable', 'resistant', 'failed medical therapy',
            'surgical', 'surgery'
        ]
        return any(keyword in text for keyword in advanced_keywords)
    
    def analyze_case_quality(self, mcq, case_data):
        """Analyze the quality of generated case"""
        analysis = {
            'mcq_id': mcq.id,
            'specialty': mcq.subspecialty,
            'question': mcq.question_text,
            'correct_answer': mcq.correct_answer,
            'issues': [],
            'quality_score': 0,
            'preservation_score': 0,
            'clinical_realism_score': 0,
            'detail_score': 0
        }
        
        # Extract case details
        clinical_presentation = case_data.get('clinical_presentation', '')
        patient_demographics = case_data.get('patient_demographics', '')
        question_type = case_data.get('question_type', '')
        fallback_used = case_data.get('fallback_used', False)
        
        analysis['case_data'] = {
            'clinical_presentation': clinical_presentation,
            'patient_demographics': patient_demographics,
            'question_type': question_type,
            'fallback_used': fallback_used
        }
        
        # Check for major issues
        if fallback_used:
            analysis['issues'].append('FALLBACK_USED')
        
        if not clinical_presentation or len(clinical_presentation.strip()) < 20:
            analysis['issues'].append('INSUFFICIENT_CONTENT')
            return analysis
        
        # Check term preservation
        expected_terms = self.extract_key_terms_from_mcq(mcq.question_text)
        presentation_lower = clinical_presentation.lower()
        
        if expected_terms:
            preserved_terms = [term for term in expected_terms if term in presentation_lower]
            missing_terms = [term for term in expected_terms if term not in presentation_lower]
            
            analysis['expected_terms'] = expected_terms
            analysis['preserved_terms'] = preserved_terms
            analysis['missing_terms'] = missing_terms
            
            if expected_terms:
                preservation_rate = len(preserved_terms) / len(expected_terms)
                analysis['preservation_score'] = preservation_rate * 100
            
            # Critical term missing
            critical_terms = ['horner', 'parkinson', 'huntington', 'caudate', 'stroke', 'seizure', 'epilepsy']
            for term in critical_terms:
                if term in mcq.question_text.lower() and term not in presentation_lower:
                    analysis['issues'].append(f'CRITICAL_TERM_MISSING: {term}')
        
        # Check for topic mismatch
        if self.detect_topic_mismatch(mcq.question_text, clinical_presentation):
            analysis['issues'].append('TOPIC_MISMATCH')
        
        # Check clinical realism
        clinical_score = self.assess_clinical_realism(clinical_presentation, patient_demographics)
        analysis['clinical_realism_score'] = clinical_score
        
        # Check detail level for advanced management
        if self.detect_advanced_management(mcq.question_text):
            detail_score = self.assess_detail_level(clinical_presentation)
            analysis['detail_score'] = detail_score
            if detail_score < 60:
                analysis['issues'].append('INSUFFICIENT_DETAIL_FOR_ADVANCED')
        
        # Overall quality score
        base_score = 100
        for issue in analysis['issues']:
            if 'CRITICAL' in issue or 'TOPIC_MISMATCH' in issue:
                base_score = 0  # Critical failure
                break
            elif 'FALLBACK' in issue:
                base_score -= 30
            elif 'INSUFFICIENT' in issue:
                base_score -= 20
            else:
                base_score -= 10
        
        analysis['quality_score'] = max(0, base_score)
        
        return analysis
    
    def detect_topic_mismatch(self, original_question, generated_case):
        """Detect if the generated case is about a different topic than the MCQ"""
        original_lower = original_question.lower()
        case_lower = generated_case.lower()
        
        # Define topic keywords
        topics = {
            'movement_disorders': ['parkinson', 'huntington', 'chorea', 'tremor', 'rigidity', 'bradykinesia'],
            'stroke': ['stroke', 'hemiparesis', 'aphasia', 'infarct', 'hemorrhage'],
            'epilepsy': ['seizure', 'epilepsy', 'ictal', 'convulsion'],
            'horner': ['horner', 'ptosis', 'miosis', 'anhidrosis'],
            'dementia': ['alzheimer', 'dementia', 'cognitive', 'memory'],
            'headache': ['migraine', 'headache', 'cluster'],
            'neuropathy': ['neuropathy', 'weakness', 'guillain']
        }
        
        original_topics = []
        case_topics = []
        
        for topic, keywords in topics.items():
            if any(kw in original_lower for kw in keywords):
                original_topics.append(topic)
            if any(kw in case_lower for kw in keywords):
                case_topics.append(topic)
        
        # If original has clear topic but case has different topic
        if original_topics and case_topics:
            return not any(topic in case_topics for topic in original_topics)
        
        return False
    
    def assess_clinical_realism(self, clinical_presentation, patient_demographics):
        """Assess clinical realism of the generated case"""
        score = 100
        
        if not patient_demographics or len(patient_demographics.strip()) < 10:
            score -= 20
        
        # Check for clinical language
        clinical_words = ['presents', 'history', 'examination', 'symptoms', 'complains', 'reports']
        if not any(word in clinical_presentation.lower() for word in clinical_words):
            score -= 15
        
        # Check for specific details
        if not any(char.isdigit() for char in clinical_presentation):
            score -= 10
        
        # Check length
        if len(clinical_presentation) < 50:
            score -= 20
        
        return max(0, score)
    
    def assess_detail_level(self, clinical_presentation):
        """Assess detail level for advanced management cases"""
        score = 100
        text = clinical_presentation.lower()
        
        # Check for medication details
        med_indicators = ['mg', 'dose', 'daily', 'twice', 'three times', 'q8h', 'q12h']
        if not any(indicator in text for indicator in med_indicators):
            score -= 30
        
        # Check for treatment failure descriptions
        failure_indicators = ['failed', 'inadequate', 'side effects', 'intolerant', 'refractory']
        if not any(indicator in text for indicator in failure_indicators):
            score -= 25
        
        # Check for functional impact
        impact_indicators = ['unable to work', 'disability', 'adl', 'quality of life', 'function']
        if not any(indicator in text for indicator in impact_indicators):
            score -= 20
        
        # Check for specific medication names
        common_meds = ['levodopa', 'carbidopa', 'ropinirole', 'pramipexole', 'levetiracetam', 'valproate']
        if not any(med in text for med in common_meds):
            score -= 15
        
        return max(0, score)
    
    def test_mcqs(self, mcqs_per_specialty=20):
        """Test MCQs from all specialties"""
        print(f"🧪 Testing {mcqs_per_specialty} MCQs per specialty (Cycle {self.current_cycle})")
        print("=" * 100)
        
        specialties = self.get_all_specialties()
        print(f"Found {len(specialties)} specialties: {', '.join(specialties[:5])}{'...' if len(specialties) > 5 else ''}")
        
        all_results = []
        specialty_summaries = {}
        
        for specialty in specialties:
            print(f"\n🔬 Testing {specialty}...")
            
            # Get random MCQs from this specialty
            mcqs = self.get_random_mcqs_by_specialty(specialty, mcqs_per_specialty)
            
            if not mcqs:
                print(f"  ⚠️ No MCQs found for {specialty}")
                continue
            
            print(f"  Testing {len(mcqs)} MCQs...")
            
            specialty_results = []
            for i, mcq in enumerate(mcqs, 1):
                try:
                    # Convert MCQ to case
                    case_data = convert_mcq_to_case(mcq)
                    
                    # Analyze quality
                    analysis = self.analyze_case_quality(mcq, case_data)
                    specialty_results.append(analysis)
                    all_results.append(analysis)
                    
                    if i % 5 == 0:
                        print(f"    Progress: {i}/{len(mcqs)}")
                        
                except Exception as e:
                    print(f"    ❌ Error with MCQ {mcq.id}: {e}")
                    analysis = {
                        'mcq_id': mcq.id,
                        'specialty': specialty,
                        'issues': ['CONVERSION_ERROR'],
                        'quality_score': 0,
                        'error': str(e)
                    }
                    specialty_results.append(analysis)
                    all_results.append(analysis)
            
            # Summarize specialty results
            specialty_summaries[specialty] = self.summarize_specialty_results(specialty_results)
        
        # Overall analysis
        overall_summary = self.analyze_overall_results(all_results)
        
        # Generate report
        self.generate_comprehensive_report(overall_summary, specialty_summaries, all_results)
        
        return overall_summary, specialty_summaries, all_results
    
    def summarize_specialty_results(self, results):
        """Summarize results for a single specialty"""
        if not results:
            return {}
        
        total = len(results)
        quality_scores = [r['quality_score'] for r in results]
        avg_quality = sum(quality_scores) / total if quality_scores else 0
        
        # Count issues
        issue_counts = defaultdict(int)
        for result in results:
            for issue in result.get('issues', []):
                issue_counts[issue] += 1
        
        # Count perfect cases
        perfect_cases = len([r for r in results if r['quality_score'] >= 90])
        good_cases = len([r for r in results if 70 <= r['quality_score'] < 90])
        poor_cases = len([r for r in results if r['quality_score'] < 50])
        
        return {
            'total_tested': total,
            'avg_quality_score': avg_quality,
            'perfect_cases': perfect_cases,
            'good_cases': good_cases,
            'poor_cases': poor_cases,
            'common_issues': dict(issue_counts),
            'success_rate': (perfect_cases + good_cases) / total * 100 if total > 0 else 0
        }
    
    def analyze_overall_results(self, all_results):
        """Analyze overall results across all specialties"""
        if not all_results:
            return {}
        
        total = len(all_results)
        quality_scores = [r['quality_score'] for r in all_results]
        avg_quality = sum(quality_scores) / total
        
        # Issue analysis
        all_issues = []
        for result in all_results:
            all_issues.extend(result.get('issues', []))
        
        issue_counts = defaultdict(int)
        for issue in all_issues:
            issue_counts[issue] += 1
        
        # Performance categories
        excellent = len([r for r in all_results if r['quality_score'] >= 90])
        good = len([r for r in all_results if 70 <= r['quality_score'] < 90])
        acceptable = len([r for r in all_results if 50 <= r['quality_score'] < 70])
        poor = len([r for r in all_results if r['quality_score'] < 50])
        
        return {
            'total_tested': total,
            'avg_quality_score': avg_quality,
            'excellent_cases': excellent,
            'good_cases': good,
            'acceptable_cases': acceptable,
            'poor_cases': poor,
            'success_rate': (excellent + good) / total * 100,
            'top_issues': sorted(issue_counts.items(), key=lambda x: x[1], reverse=True)[:10]
        }
    
    def generate_comprehensive_report(self, overall_summary, specialty_summaries, detailed_results):
        """Generate comprehensive test report with fix recommendations"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_file = f"/Users/tariqalmatrudi/NEWreader/mcq_test_report_cycle_{self.current_cycle}_{timestamp}.json"
        
        report = {
            'cycle': self.current_cycle,
            'timestamp': timestamp,
            'overall_summary': overall_summary,
            'specialty_summaries': specialty_summaries,
            'detailed_results': detailed_results,
            'fix_recommendations': self.generate_fix_recommendations(overall_summary)
        }
        
        # Save detailed report
        with open(report_file, 'w') as f:
            json.dump(report, f, indent=2)
        
        # Print summary
        self.print_test_summary(overall_summary, specialty_summaries)
        
        print(f"\n📄 Detailed report saved to: {report_file}")
        
        return report
    
    def generate_fix_recommendations(self, overall_summary):
        """Generate specific fix recommendations based on test results"""
        recommendations = []
        
        top_issues = overall_summary.get('top_issues', [])
        
        for issue, count in top_issues:
            if issue == 'TOPIC_MISMATCH':
                recommendations.append({
                    'priority': 'CRITICAL',
                    'issue': issue,
                    'count': count,
                    'fix': 'Strengthen validation to reject cases that change medical topics. Add more specific critical term checking.',
                    'code_location': 'validate_case_preservation_fallback function'
                })
            elif issue == 'CRITICAL_TERM_MISSING':
                recommendations.append({
                    'priority': 'CRITICAL', 
                    'issue': issue,
                    'count': count,
                    'fix': 'Enhance critical term detection and make validation fail immediately for missing critical terms.',
                    'code_location': 'extract_key_medical_terms and validation functions'
                })
            elif issue == 'INSUFFICIENT_DETAIL_FOR_ADVANCED':
                recommendations.append({
                    'priority': 'HIGH',
                    'issue': issue,
                    'count': count,
                    'fix': 'Improve prompts for advanced management cases to require specific medication details and treatment failures.',
                    'code_location': 'create_domain_specific_prompt function'
                })
            elif issue == 'FALLBACK_USED':
                recommendations.append({
                    'priority': 'MEDIUM',
                    'issue': issue,
                    'count': count,
                    'fix': 'Investigate why AI generation is failing and improve prompts or reduce validation strictness.',
                    'code_location': 'generate_validated_case function'
                })
        
        return recommendations
    
    def print_test_summary(self, overall_summary, specialty_summaries):
        """Print formatted test summary"""
        print(f"\n{'='*100}")
        print(f"📊 COMPREHENSIVE TEST RESULTS - CYCLE {self.current_cycle}")
        print(f"{'='*100}")
        
        # Overall results
        total = overall_summary['total_tested']
        avg_score = overall_summary['avg_quality_score']
        success_rate = overall_summary['success_rate']
        
        print(f"\n🎯 OVERALL PERFORMANCE:")
        print(f"  Total MCQs Tested: {total}")
        print(f"  Average Quality Score: {avg_score:.1f}/100")
        print(f"  Success Rate: {success_rate:.1f}% (Excellent + Good)")
        
        print(f"\n📈 PERFORMANCE BREAKDOWN:")
        print(f"  🎉 Excellent (≥90): {overall_summary['excellent_cases']}/{total} ({overall_summary['excellent_cases']/total*100:.1f}%)")
        print(f"  ✅ Good (70-89): {overall_summary['good_cases']}/{total} ({overall_summary['good_cases']/total*100:.1f}%)")
        print(f"  ⚠️ Acceptable (50-69): {overall_summary['acceptable_cases']}/{total} ({overall_summary['acceptable_cases']/total*100:.1f}%)")
        print(f"  ❌ Poor (<50): {overall_summary['poor_cases']}/{total} ({overall_summary['poor_cases']/total*100:.1f}%)")
        
        print(f"\n🔍 TOP ISSUES:")
        for issue, count in overall_summary['top_issues'][:5]:
            percentage = count / total * 100
            print(f"  {issue}: {count} cases ({percentage:.1f}%)")
        
        # Specialty breakdown
        print(f"\n🏥 SPECIALTY PERFORMANCE:")
        sorted_specialties = sorted(specialty_summaries.items(), 
                                  key=lambda x: x[1].get('success_rate', 0), reverse=True)
        
        for specialty, summary in sorted_specialties[:10]:  # Show top 10
            success_rate = summary.get('success_rate', 0)
            avg_score = summary.get('avg_quality_score', 0)
            total_tested = summary.get('total_tested', 0)
            
            if success_rate >= 80:
                emoji = "🎉"
            elif success_rate >= 60:
                emoji = "✅"
            elif success_rate >= 40:
                emoji = "⚠️"
            else:
                emoji = "❌"
            
            print(f"  {emoji} {specialty}: {success_rate:.1f}% success ({avg_score:.1f}/100 avg) [{total_tested} MCQs]")
        
        # Assessment
        print(f"\n🎯 OVERALL ASSESSMENT:")
        if success_rate >= 80:
            print("🎉 EXCELLENT: System is performing very well!")
        elif success_rate >= 60:
            print("✅ GOOD: System is working well with some improvement opportunities")
        elif success_rate >= 40:
            print("⚠️ NEEDS IMPROVEMENT: Several issues need to be addressed")
        else:
            print("❌ POOR: Major improvements needed")

def run_initial_comprehensive_test():
    """Run the initial comprehensive test with 20 MCQs per specialty"""
    testing_system = MCQTestingSystem()
    overall, specialty, detailed = testing_system.test_mcqs(mcqs_per_specialty=20)
    return testing_system, overall, specialty, detailed

def run_improvement_cycle(testing_system):
    """Run a 5 MCQ improvement cycle"""
    testing_system.current_cycle += 1
    overall, specialty, detailed = testing_system.test_mcqs(mcqs_per_specialty=5)
    return overall, specialty, detailed

if __name__ == "__main__":
    print("🚀 Starting Comprehensive MCQ-to-Case Conversion Testing")
    print("This will test the system across all specialties and provide improvement recommendations")
    print()
    
    # Run initial comprehensive test
    system, overall_results, specialty_results, detailed_results = run_initial_comprehensive_test()
    
    print(f"\n🔧 Fix recommendations have been generated.")
    print(f"Please review the detailed report and implement fixes.")
    print(f"Then run improvement cycles with 5 MCQs per specialty until perfect performance is achieved.")