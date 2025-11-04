#!/usr/bin/env python3
"""
Comprehensive MCQ-to-Case Analysis
Evaluates if generated cases truly serve their educational purpose and maintain clinical accuracy
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

class ComprehensiveMCQAnalyzer:
    def __init__(self):
        self.analysis_results = []
        self.patterns = defaultdict(list)
        
    def extract_critical_content(self, question_text):
        """Extract critical medical content that must be preserved"""
        text = question_text.lower()
        
        critical_content = {
            'specific_conditions': [],
            'anatomical_locations': [],
            'clinical_signs': [],
            'medications': [],
            'procedures': [],
            'investigations': [],
            'patient_demographics': [],
            'clinical_context': []
        }
        
        # Specific neurological conditions
        conditions = [
            'horner syndrome', 'parkinson', 'huntington', 'alzheimer', 'multiple sclerosis', 'ms',
            'guillain barre', 'gbs', 'myasthenia gravis', 'epilepsy', 'seizure',
            'stroke', 'tia', 'migraine', 'cluster headache', 'tension headache',
            'dementia', 'delirium', 'depression', 'anxiety'
        ]
        
        for condition in conditions:
            if condition in text:
                critical_content['specific_conditions'].append(condition)
        
        # Anatomical locations
        locations = [
            'bilateral caudate', 'caudate', 'putamen', 'globus pallidus', 'thalamus',
            'brainstem', 'midbrain', 'pons', 'medulla', 'cerebellum',
            'frontal lobe', 'temporal lobe', 'parietal lobe', 'occipital lobe',
            'left hemisphere', 'right hemisphere', 'bilateral'
        ]
        
        for location in locations:
            if location in text:
                critical_content['anatomical_locations'].append(location)
        
        # Clinical signs
        signs = [
            'ptosis', 'miosis', 'anhidrosis', 'diplopia', 'nystagmus',
            'tremor', 'rigidity', 'bradykinesia', 'chorea', 'dystonia', 'ataxia',
            'hemiparesis', 'paraparesis', 'quadriparesis', 'weakness',
            'aphasia', 'dysarthria', 'dysphagia'
        ]
        
        for sign in signs:
            if sign in text:
                critical_content['clinical_signs'].append(sign)
        
        # Advanced procedures
        procedures = [
            'thalamotomy', 'pallidotomy', 'dbs', 'deep brain stimulation',
            'vns', 'vagal nerve stimulation', 'hemispherectomy', 'corpus callosotomy',
            'cabg', 'bypass surgery', 'cardiac surgery'
        ]
        
        for procedure in procedures:
            if procedure in text:
                critical_content['procedures'].append(procedure)
        
        # Medications
        medications = [
            'levodopa', 'carbidopa', 'ropinirole', 'pramipexole', 'rasagiline',
            'topiramate', 'topamax', 'lamotrigine', 'lamictal', 'levetiracetam', 'keppra',
            'phenytoin', 'carbamazepine', 'valproate', 'depakote'
        ]
        
        for med in medications:
            if med in text:
                critical_content['medications'].append(med)
        
        return critical_content
    
    def detect_question_purpose(self, mcq):
        """Determine the educational purpose of the MCQ"""
        text = mcq.question_text.lower()
        
        # Diagnosis questions
        if any(phrase in text for phrase in ['diagnosis', 'most likely', 'what is the', 'which condition']):
            return 'diagnosis'
        
        # Management questions
        if any(phrase in text for phrase in ['treatment', 'management', 'next step', 'best management', 'therapy']):
            return 'management'
        
        # Advanced management
        if any(phrase in text for phrase in ['refractory', 'failed', 'surgery', 'surgical', 'thalamotomy', 'dbs']):
            return 'advanced_management'
        
        # Investigation questions
        if any(phrase in text for phrase in ['investigation', 'test', 'imaging', 'mri', 'ct', 'eeg', 'emg']):
            return 'investigation'
        
        # Anatomy/localization
        if any(phrase in text for phrase in ['lesion', 'where', 'location', 'localize']):
            return 'localization'
        
        return 'general'
    
    def evaluate_case_quality(self, mcq, case_data):
        """Comprehensive evaluation of case quality and purpose alignment"""
        
        analysis = {
            'mcq_id': mcq.id,
            'specialty': getattr(mcq, 'subspecialty', 'Unknown'),
            'original_question': mcq.question_text,
            'correct_answer': mcq.correct_answer,
            'educational_purpose': self.detect_question_purpose(mcq),
            'critical_content': self.extract_critical_content(mcq.question_text),
            'case_quality_score': 0,
            'purpose_alignment_score': 0,
            'content_preservation_score': 0,
            'clinical_realism_score': 0,
            'educational_value_score': 0,
            'issues': [],
            'strengths': [],
            'recommendations': []
        }
        
        # Extract case data
        clinical_presentation = case_data.get('clinical_presentation', '')
        patient_demographics = case_data.get('patient_demographics', '')
        question_type = case_data.get('question_type', '')
        fallback_used = case_data.get('fallback_used', False)
        
        analysis['generated_case'] = {
            'patient_demographics': patient_demographics,
            'clinical_presentation': clinical_presentation,
            'question_type': question_type,
            'fallback_used': fallback_used
        }
        
        # 1. Content Preservation Analysis
        preservation_score = self.analyze_content_preservation(mcq, case_data, analysis)
        analysis['content_preservation_score'] = preservation_score
        
        # 2. Purpose Alignment Analysis
        purpose_score = self.analyze_purpose_alignment(mcq, case_data, analysis)
        analysis['purpose_alignment_score'] = purpose_score
        
        # 3. Clinical Realism Analysis
        realism_score = self.analyze_clinical_realism(case_data, analysis)
        analysis['clinical_realism_score'] = realism_score
        
        # 4. Educational Value Analysis
        educational_score = self.analyze_educational_value(mcq, case_data, analysis)
        analysis['educational_value_score'] = educational_score
        
        # 5. Overall Quality Score
        if fallback_used:
            analysis['case_quality_score'] = 30  # Fallback gets low score
            analysis['issues'].append('FALLBACK_USED')
        else:
            analysis['case_quality_score'] = (preservation_score + purpose_score + realism_score + educational_score) / 4
        
        # 6. Generate specific recommendations
        self.generate_recommendations(analysis)
        
        return analysis
    
    def analyze_content_preservation(self, mcq, case_data, analysis):
        """Analyze how well critical content is preserved"""
        clinical_presentation = case_data.get('clinical_presentation', '').lower()
        critical_content = analysis['critical_content']
        
        score = 100
        
        # Check specific conditions
        for condition in critical_content['specific_conditions']:
            if condition not in clinical_presentation:
                analysis['issues'].append(f'MISSING_CONDITION: {condition}')
                score -= 25  # Heavy penalty for missing conditions
        
        # Check anatomical locations
        for location in critical_content['anatomical_locations']:
            if location not in clinical_presentation:
                analysis['issues'].append(f'MISSING_LOCATION: {location}')
                score -= 15
        
        # Check clinical signs
        for sign in critical_content['clinical_signs']:
            if sign not in clinical_presentation:
                analysis['issues'].append(f'MISSING_SIGN: {sign}')
                score -= 10
        
        # Check procedures
        for procedure in critical_content['procedures']:
            if procedure not in clinical_presentation:
                analysis['issues'].append(f'MISSING_PROCEDURE: {procedure}')
                score -= 20
        
        return max(0, score)
    
    def analyze_purpose_alignment(self, mcq, case_data, analysis):
        """Analyze if the case serves the same educational purpose as the MCQ"""
        original_purpose = analysis['educational_purpose']
        case_type = case_data.get('question_type', '')
        
        score = 100
        
        # Check purpose alignment
        purpose_mapping = {
            'diagnosis': ['diagnosis'],
            'management': ['management'],
            'advanced_management': ['advanced_management', 'management'],
            'investigation': ['investigation'],
            'localization': ['diagnosis', 'localization']
        }
        
        expected_types = purpose_mapping.get(original_purpose, [original_purpose])
        if case_type not in expected_types:
            analysis['issues'].append(f'PURPOSE_MISMATCH: {original_purpose} → {case_type}')
            score -= 30
        
        # Advanced management specific checks
        if original_purpose == 'advanced_management':
            clinical_presentation = case_data.get('clinical_presentation', '').lower()
            if not any(indicator in clinical_presentation for indicator in ['failed', 'refractory', 'side effects']):
                analysis['issues'].append('MISSING_TREATMENT_FAILURE_CONTEXT')
                score -= 20
            
            if not any(indicator in clinical_presentation for indicator in ['mg', 'dose', 'daily']):
                analysis['issues'].append('MISSING_MEDICATION_DETAILS')
                score -= 15
        
        return max(0, score)
    
    def analyze_clinical_realism(self, case_data, analysis):
        """Analyze clinical realism of the generated case"""
        clinical_presentation = case_data.get('clinical_presentation', '')
        patient_demographics = case_data.get('patient_demographics', '')
        
        score = 100
        
        # Check basic requirements
        if len(clinical_presentation) < 50:
            analysis['issues'].append('INSUFFICIENT_LENGTH')
            score -= 20
        
        # Check for clinical language
        clinical_words = ['presents', 'history', 'examination', 'symptoms', 'complains', 'reports']
        if not any(word in clinical_presentation.lower() for word in clinical_words):
            analysis['issues'].append('NON_CLINICAL_LANGUAGE')
            score -= 15
        
        # Check for specific details
        if not any(char.isdigit() for char in clinical_presentation):
            analysis['issues'].append('LACKS_SPECIFIC_DETAILS')
            score -= 10
        
        # Check demographics
        if not patient_demographics or 'year-old' not in patient_demographics:
            analysis['issues'].append('POOR_DEMOGRAPHICS')
            score -= 15
        
        return max(0, score)
    
    def analyze_educational_value(self, mcq, case_data, analysis):
        """Analyze educational value and teaching effectiveness"""
        score = 100
        
        # Check if case teaches the same concept
        original_lower = mcq.question_text.lower()
        presentation_lower = case_data.get('clinical_presentation', '').lower()
        
        # Topic consistency check
        medical_topics = {
            'movement': ['parkinson', 'huntington', 'chorea', 'tremor', 'rigidity'],
            'seizure': ['seizure', 'epilepsy', 'ictal', 'convulsion'],
            'stroke': ['stroke', 'hemiparesis', 'infarct', 'aphasia'],
            'eye': ['horner', 'ptosis', 'diplopia', 'miosis'],
            'cardiac': ['cabg', 'bypass', 'cardiac', 'coronary']
        }
        
        original_topics = set()
        case_topics = set()
        
        for topic, keywords in medical_topics.items():
            if any(kw in original_lower for kw in keywords):
                original_topics.add(topic)
            if any(kw in presentation_lower for kw in keywords):
                case_topics.add(topic)
        
        if original_topics and case_topics and not original_topics.intersection(case_topics):
            analysis['issues'].append(f'TOPIC_DRIFT: {original_topics} → {case_topics}')
            score -= 40
        
        # Check for appropriate complexity
        if analysis['educational_purpose'] == 'advanced_management':
            if 'complex' not in presentation_lower and 'advanced' not in presentation_lower:
                analysis['issues'].append('INSUFFICIENT_COMPLEXITY_FOR_ADVANCED')
                score -= 15
        
        return max(0, score)
    
    def generate_recommendations(self, analysis):
        """Generate specific recommendations for improvement"""
        issues = analysis['issues']
        recommendations = []
        
        # Content preservation recommendations
        if any('MISSING_CONDITION' in issue for issue in issues):
            recommendations.append('CRITICAL: Strengthen critical condition preservation in validation')
        
        if any('MISSING_LOCATION' in issue for issue in issues):
            recommendations.append('HIGH: Improve anatomical location preservation')
        
        # Purpose alignment recommendations
        if any('PURPOSE_MISMATCH' in issue for issue in issues):
            recommendations.append('CRITICAL: Fix question type detection and prompting')
        
        if any('MISSING_TREATMENT_FAILURE' in issue for issue in issues):
            recommendations.append('HIGH: Enhance advanced management case prompts')
        
        # Clinical realism recommendations
        if any('NON_CLINICAL_LANGUAGE' in issue for issue in issues):
            recommendations.append('MEDIUM: Improve clinical language in prompts')
        
        if any('TOPIC_DRIFT' in issue for issue in issues):
            recommendations.append('CRITICAL: Fix topic preservation in AI prompts')
        
        analysis['recommendations'] = recommendations
    
    def test_comprehensive_sample(self, mcqs_per_specialty=3):
        """Test comprehensive sample across specialties"""
        print("🔬 COMPREHENSIVE MCQ-TO-CASE ANALYSIS")
        print("=" * 100)
        print("Testing educational purpose alignment, content preservation, and clinical realism")
        print()
        
        # Get all specialties
        specialties = MCQ.objects.values_list('subspecialty', flat=True).distinct()
        specialties = [s for s in specialties if s and s.strip()]
        
        print(f"📊 Found {len(specialties)} specialties")
        
        all_results = []
        specialty_summaries = {}
        
        for specialty in sorted(specialties):
            print(f"\n🏥 TESTING {specialty}")
            print("-" * 60)
            
            # Get random MCQs from this specialty
            mcqs = list(MCQ.objects.filter(subspecialty=specialty))
            if len(mcqs) < mcqs_per_specialty:
                test_mcqs = mcqs
            else:
                test_mcqs = random.sample(mcqs, mcqs_per_specialty)
            
            specialty_results = []
            
            for i, mcq in enumerate(test_mcqs, 1):
                print(f"  {i}/{len(test_mcqs)}: MCQ {mcq.id} - ", end="")
                
                try:
                    # Convert MCQ to case
                    case_data = convert_mcq_to_case(mcq)
                    
                    # Comprehensive analysis
                    analysis = self.evaluate_case_quality(mcq, case_data)
                    specialty_results.append(analysis)
                    all_results.append(analysis)
                    
                    # Quick status
                    overall_score = analysis['case_quality_score']
                    if overall_score >= 80:
                        print(f"✅ EXCELLENT ({overall_score:.0f}%)")
                    elif overall_score >= 60:
                        print(f"🟡 GOOD ({overall_score:.0f}%)")
                    elif overall_score >= 40:
                        print(f"⚠️ FAIR ({overall_score:.0f}%)")
                    else:
                        print(f"❌ POOR ({overall_score:.0f}%)")
                    
                    # Show top issues
                    if analysis['issues']:
                        top_issues = analysis['issues'][:2]
                        print(f"      Issues: {', '.join(top_issues)}")
                    
                except Exception as e:
                    print(f"❌ ERROR: {e}")
                    analysis = {
                        'mcq_id': mcq.id,
                        'specialty': specialty,
                        'case_quality_score': 0,
                        'issues': ['CONVERSION_ERROR'],
                        'error': str(e)
                    }
                    specialty_results.append(analysis)
                    all_results.append(analysis)
            
            # Specialty summary
            if specialty_results:
                avg_score = sum(r['case_quality_score'] for r in specialty_results) / len(specialty_results)
                excellent_count = len([r for r in specialty_results if r['case_quality_score'] >= 80])
                
                specialty_summaries[specialty] = {
                    'avg_score': avg_score,
                    'excellent_count': excellent_count,
                    'total_tested': len(specialty_results),
                    'common_issues': self.get_common_issues(specialty_results)
                }
                
                print(f"    📊 Specialty Average: {avg_score:.1f}% ({excellent_count}/{len(specialty_results)} excellent)")
        
        # Generate comprehensive report
        self.generate_comprehensive_report(all_results, specialty_summaries)
        
        return all_results, specialty_summaries
    
    def get_common_issues(self, results):
        """Get common issues from results"""
        issue_counts = defaultdict(int)
        for result in results:
            for issue in result.get('issues', []):
                issue_counts[issue] += 1
        return dict(issue_counts)
    
    def generate_comprehensive_report(self, all_results, specialty_summaries):
        """Generate comprehensive analysis report"""
        print(f"\n{'='*100}")
        print(f"📊 COMPREHENSIVE ANALYSIS REPORT")
        print(f"{'='*100}")
        
        total_tested = len(all_results)
        
        # Overall quality distribution
        excellent = len([r for r in all_results if r['case_quality_score'] >= 80])
        good = len([r for r in all_results if 60 <= r['case_quality_score'] < 80])
        fair = len([r for r in all_results if 40 <= r['case_quality_score'] < 60])
        poor = len([r for r in all_results if r['case_quality_score'] < 40])
        
        print(f"\n🎯 OVERALL QUALITY DISTRIBUTION:")
        print(f"🎉 Excellent (≥80%): {excellent}/{total_tested} ({excellent/total_tested*100:.1f}%)")
        print(f"✅ Good (60-79%): {good}/{total_tested} ({good/total_tested*100:.1f}%)")
        print(f"⚠️ Fair (40-59%): {fair}/{total_tested} ({fair/total_tested*100:.1f}%)")
        print(f"❌ Poor (<40%): {poor}/{total_tested} ({poor/total_tested*100:.1f}%)")
        
        # Component scores
        avg_preservation = sum(r.get('content_preservation_score', 0) for r in all_results) / total_tested
        avg_purpose = sum(r.get('purpose_alignment_score', 0) for r in all_results) / total_tested
        avg_realism = sum(r.get('clinical_realism_score', 0) for r in all_results) / total_tested
        avg_educational = sum(r.get('educational_value_score', 0) for r in all_results) / total_tested
        
        print(f"\n📈 COMPONENT ANALYSIS:")
        print(f"🔍 Content Preservation: {avg_preservation:.1f}%")
        print(f"🎯 Purpose Alignment: {avg_purpose:.1f}%")
        print(f"🏥 Clinical Realism: {avg_realism:.1f}%")
        print(f"📚 Educational Value: {avg_educational:.1f}%")
        
        # Most common issues
        all_issues = []
        for result in all_results:
            all_issues.extend(result.get('issues', []))
        
        issue_counts = defaultdict(int)
        for issue in all_issues:
            issue_counts[issue] += 1
        
        print(f"\n🚨 TOP ISSUES REQUIRING ATTENTION:")
        for issue, count in sorted(issue_counts.items(), key=lambda x: x[1], reverse=True)[:5]:
            percentage = count / total_tested * 100
            print(f"  {issue}: {count} cases ({percentage:.1f}%)")
        
        # Best and worst performing specialties
        sorted_specialties = sorted(specialty_summaries.items(), key=lambda x: x[1]['avg_score'], reverse=True)
        
        print(f"\n🏆 TOP PERFORMING SPECIALTIES:")
        for specialty, summary in sorted_specialties[:5]:
            score = summary['avg_score']
            excellent = summary['excellent_count']
            total = summary['total_tested']
            print(f"  {specialty}: {score:.1f}% avg ({excellent}/{total} excellent)")
        
        print(f"\n📉 SPECIALTIES NEEDING IMPROVEMENT:")
        for specialty, summary in sorted_specialties[-5:]:
            score = summary['avg_score']
            excellent = summary['excellent_count']
            total = summary['total_tested']
            if score < 70:
                print(f"  {specialty}: {score:.1f}% avg ({excellent}/{total} excellent)")
        
        # Critical recommendations
        print(f"\n🔧 CRITICAL FIXES NEEDED:")
        critical_issues = [issue for issue, count in issue_counts.items() if count >= total_tested * 0.1]  # >10% prevalence
        
        if any('MISSING_CONDITION' in issue for issue in critical_issues):
            print("  1. 🚨 URGENT: Fix critical condition preservation in validation")
        if any('TOPIC_DRIFT' in issue for issue in critical_issues):
            print("  2. 🚨 URGENT: Fix topic consistency in AI prompts")
        if any('PURPOSE_MISMATCH' in issue for issue in critical_issues):
            print("  3. 🚨 URGENT: Fix educational purpose alignment")
        if any('FALLBACK_USED' in issue for issue in critical_issues):
            print("  4. ⚠️ HIGH: Reduce fallback usage by improving AI generation")

def main():
    analyzer = ComprehensiveMCQAnalyzer()
    results, summaries = analyzer.test_comprehensive_sample(mcqs_per_specialty=3)
    
    print(f"\n✅ Comprehensive analysis complete!")
    print(f"Results stored for detailed review and targeted improvements.")

if __name__ == "__main__":
    main()