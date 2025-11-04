#!/usr/bin/env python3
"""
Iterative MCQ-to-Case conversion testing and improvement system
Tests 5 MCQs from each specialty, analyzes results, provides fixes, and continues until perfect
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

class IterativeMCQTester:
    def __init__(self):
        self.cycle_number = 1
        self.test_history = []
        
    def get_all_specialties(self):
        """Get all subspecialties from the database"""
        specialties = MCQ.objects.values_list('subspecialty', flat=True).distinct()
        specialties = [s for s in specialties if s and s.strip()]
        return sorted(specialties)
    
    def get_random_mcqs_from_specialty(self, specialty, count=5):
        """Get random MCQs from a specific specialty"""
        mcqs = list(MCQ.objects.filter(subspecialty=specialty))
        if len(mcqs) < count:
            return mcqs
        return random.sample(mcqs, count)
    
    def extract_critical_terms(self, question_text):
        """Extract critical medical terms that MUST be preserved"""
        text = question_text.lower()
        critical_terms = []
        
        # Specific conditions that must not be changed
        conditions = [
            'horner', 'parkinson', 'huntington', 'alzheimer', 'stroke', 'seizure', 'epilepsy',
            'migraine', 'headache', 'multiple sclerosis', 'ms', 'dementia', 'neuropathy',
            'myopathy', 'chorea', 'dystonia', 'tremor', 'rigidity', 'ataxia',
            'caudate', 'putamen', 'thalamus', 'brainstem', 'cerebellum'
        ]
        
        # Advanced treatments
        advanced_treatments = [
            'thalamotomy', 'dbs', 'deep brain stimulation', 'vns', 'vagal nerve stimulation',
            'hemispherectomy', 'corpus callosotomy', 'epilepsy surgery'
        ]
        
        # Clinical signs
        signs = [
            'ptosis', 'miosis', 'anhidrosis', 'diplopia', 'aphasia', 'dysarthria',
            'hemiparesis', 'paraparesis', 'quadriparesis'
        ]
        
        all_terms = conditions + advanced_treatments + signs
        
        for term in all_terms:
            if term in text:
                critical_terms.append(term)
        
        return critical_terms
    
    def analyze_single_mcq(self, mcq):
        """Analyze conversion of a single MCQ"""
        analysis = {
            'mcq_id': mcq.id,
            'specialty': mcq.subspecialty,
            'question': mcq.question_text[:100] + "..." if len(mcq.question_text) > 100 else mcq.question_text,
            'critical_terms': self.extract_critical_terms(mcq.question_text),
            'success': False,
            'issues': [],
            'quality_score': 0,
            'case_summary': ''
        }
        
        try:
            # Convert MCQ to case
            case_data = convert_mcq_to_case(mcq)
            
            clinical_presentation = case_data.get('clinical_presentation', '')
            fallback_used = case_data.get('fallback_used', False)
            
            analysis['case_summary'] = clinical_presentation[:150] + "..." if len(clinical_presentation) > 150 else clinical_presentation
            analysis['fallback_used'] = fallback_used
            
            # Check for major issues
            if fallback_used:
                analysis['issues'].append('FALLBACK_USED')
                analysis['quality_score'] = 30  # Fallback gets partial credit if it preserves terms
            
            if not clinical_presentation or len(clinical_presentation.strip()) < 20:
                analysis['issues'].append('NO_CONTENT')
                analysis['quality_score'] = 0
                return analysis
            
            # Check critical term preservation
            presentation_lower = clinical_presentation.lower()
            missing_critical = []
            preserved_critical = []
            
            for term in analysis['critical_terms']:
                if term in presentation_lower:
                    preserved_critical.append(term)
                else:
                    missing_critical.append(term)
            
            analysis['preserved_critical'] = preserved_critical
            analysis['missing_critical'] = missing_critical
            
            if missing_critical:
                analysis['issues'].append(f'MISSING_CRITICAL: {", ".join(missing_critical)}')
                analysis['quality_score'] = 0  # Any missing critical term = failure
                return analysis
            
            # Check for topic mismatch
            if self.detect_topic_mismatch(mcq.question_text, clinical_presentation):
                analysis['issues'].append('TOPIC_MISMATCH')
                analysis['quality_score'] = 0
                return analysis
            
            # Check for advanced management detail
            if self.is_advanced_management(mcq.question_text):
                detail_score = self.check_advanced_detail(clinical_presentation)
                if detail_score < 70:
                    analysis['issues'].append('INSUFFICIENT_ADVANCED_DETAIL')
                    analysis['quality_score'] = max(50, detail_score)
                else:
                    analysis['quality_score'] = 100
                    analysis['success'] = True
            else:
                # Regular case - if we get here, it's good
                analysis['quality_score'] = 100
                analysis['success'] = True
            
        except Exception as e:
            analysis['issues'].append(f'CONVERSION_ERROR: {str(e)}')
            analysis['quality_score'] = 0
        
        return analysis
    
    def detect_topic_mismatch(self, original_question, generated_case):
        """Detect if the case is about a completely different topic"""
        original = original_question.lower()
        case = generated_case.lower()
        
        # Define clear topic categories
        topic_keywords = {
            'movement': ['parkinson', 'huntington', 'chorea', 'tremor', 'rigidity', 'bradykinesia', 'dystonia'],
            'stroke': ['stroke', 'hemiparesis', 'aphasia', 'infarct', 'hemorrhage', 'ischemic'],
            'epilepsy': ['seizure', 'epilepsy', 'ictal', 'convulsion', 'epileptic'],
            'eye': ['horner', 'ptosis', 'miosis', 'diplopia', 'visual', 'eye'],
            'dementia': ['alzheimer', 'dementia', 'cognitive', 'memory'],
            'headache': ['migraine', 'headache', 'cluster'],
            'neuropathy': ['neuropathy', 'guillain', 'weakness', 'polyneuropathy']
        }
        
        original_topics = set()
        case_topics = set()
        
        for topic, keywords in topic_keywords.items():
            if any(kw in original for kw in keywords):
                original_topics.add(topic)
            if any(kw in case for kw in keywords):
                case_topics.add(topic)
        
        # If original has a clear topic but case has a different topic
        if original_topics and case_topics and not original_topics.intersection(case_topics):
            return True
        
        return False
    
    def is_advanced_management(self, question_text):
        """Check if this is an advanced management question"""
        text = question_text.lower()
        advanced_keywords = [
            'thalamotomy', 'dbs', 'deep brain stimulation', 'vns', 'surgery',
            'refractory', 'intractable', 'resistant', 'failed'
        ]
        return any(kw in text for kw in advanced_keywords)
    
    def check_advanced_detail(self, clinical_presentation):
        """Check if advanced management case has sufficient detail"""
        text = clinical_presentation.lower()
        score = 0
        
        # Medication details (30 points)
        if any(indicator in text for indicator in ['mg', 'dose', 'daily', 'q8h', 'q12h']):
            score += 30
        
        # Treatment failure (25 points)
        if any(indicator in text for indicator in ['failed', 'inadequate', 'side effects', 'refractory']):
            score += 25
        
        # Functional impact (25 points)
        if any(indicator in text for indicator in ['unable to work', 'disability', 'adl', 'quality of life']):
            score += 25
        
        # Specific medications (20 points)
        if any(med in text for med in ['levodopa', 'carbidopa', 'ropinirole', 'levetiracetam', 'valproate']):
            score += 20
        
        return score
    
    def run_test_cycle(self):
        """Run one test cycle with 5 MCQs from each specialty"""
        print(f"\n🔬 CYCLE {self.cycle_number}: Testing 5 MCQs from each specialty")
        print("=" * 80)
        
        specialties = self.get_all_specialties()
        print(f"Testing {len(specialties)} specialties...")
        
        all_results = []
        specialty_summaries = {}
        
        for specialty in specialties:
            print(f"\n📋 {specialty}:")
            
            mcqs = self.get_random_mcqs_from_specialty(specialty, 5)
            if not mcqs:
                print("  ⚠️ No MCQs found")
                continue
            
            specialty_results = []
            for i, mcq in enumerate(mcqs, 1):
                print(f"  {i}/5: Testing MCQ {mcq.id}...", end=" ")
                
                analysis = self.analyze_single_mcq(mcq)
                specialty_results.append(analysis)
                all_results.append(analysis)
                
                if analysis['success']:
                    print("✅ SUCCESS")
                else:
                    print(f"❌ FAILED: {', '.join(analysis['issues'])}")
            
            # Specialty summary
            success_count = len([r for r in specialty_results if r['success']])
            specialty_summaries[specialty] = {
                'tested': len(specialty_results),
                'success': success_count,
                'success_rate': success_count / len(specialty_results) * 100 if specialty_results else 0,
                'common_issues': self.get_common_issues(specialty_results)
            }
            
            print(f"  📊 Success: {success_count}/{len(specialty_results)} ({specialty_summaries[specialty]['success_rate']:.1f}%)")
        
        # Overall analysis
        total_tested = len(all_results)
        total_success = len([r for r in all_results if r['success']])
        overall_success_rate = total_success / total_tested * 100 if total_tested > 0 else 0
        
        cycle_results = {
            'cycle': self.cycle_number,
            'total_tested': total_tested,
            'total_success': total_success,
            'success_rate': overall_success_rate,
            'specialty_summaries': specialty_summaries,
            'detailed_results': all_results,
            'is_perfect': overall_success_rate == 100.0
        }
        
        self.test_history.append(cycle_results)
        
        # Print summary
        self.print_cycle_summary(cycle_results)
        
        # Generate fixes if not perfect
        if not cycle_results['is_perfect']:
            self.analyze_and_suggest_fixes(all_results)
        
        return cycle_results
    
    def get_common_issues(self, results):
        """Get common issues from a set of results"""
        issue_counts = defaultdict(int)
        for result in results:
            for issue in result['issues']:
                issue_counts[issue] += 1
        return dict(issue_counts)
    
    def print_cycle_summary(self, cycle_results):
        """Print summary for current cycle"""
        print(f"\n{'='*80}")
        print(f"📊 CYCLE {cycle_results['cycle']} SUMMARY")
        print(f"{'='*80}")
        
        success_rate = cycle_results['success_rate']
        total = cycle_results['total_tested']
        success = cycle_results['total_success']
        
        print(f"🎯 Overall Performance: {success}/{total} ({success_rate:.1f}%)")
        
        if cycle_results['is_perfect']:
            print("🎉 PERFECT CYCLE ACHIEVED! All MCQs converted successfully!")
            return
        
        # Show top performing specialties
        sorted_specialties = sorted(
            cycle_results['specialty_summaries'].items(),
            key=lambda x: x[1]['success_rate'],
            reverse=True
        )
        
        print(f"\n🏆 Top Performing Specialties:")
        for specialty, summary in sorted_specialties[:5]:
            rate = summary['success_rate']
            tested = summary['tested']
            success = summary['success']
            emoji = "🎉" if rate == 100 else "✅" if rate >= 80 else "⚠️" if rate >= 60 else "❌"
            print(f"  {emoji} {specialty}: {success}/{tested} ({rate:.1f}%)")
        
        print(f"\n❌ Worst Performing Specialties:")
        for specialty, summary in sorted_specialties[-5:]:
            if summary['success_rate'] < 100:
                rate = summary['success_rate']
                tested = summary['tested']
                success = summary['success']
                print(f"  ❌ {specialty}: {success}/{tested} ({rate:.1f}%)")
    
    def analyze_and_suggest_fixes(self, all_results):
        """Analyze results and suggest specific fixes"""
        print(f"\n🔧 ANALYSIS & FIX RECOMMENDATIONS:")
        print("-" * 50)
        
        # Collect all issues
        issue_counts = defaultdict(int)
        issue_examples = defaultdict(list)
        
        for result in all_results:
            if not result['success']:
                for issue in result['issues']:
                    issue_counts[issue] += 1
                    if len(issue_examples[issue]) < 3:  # Keep max 3 examples
                        issue_examples[issue].append({
                            'mcq_id': result['mcq_id'],
                            'specialty': result['specialty'],
                            'question': result['question']
                        })
        
        # Prioritize fixes
        sorted_issues = sorted(issue_counts.items(), key=lambda x: x[1], reverse=True)
        
        for i, (issue, count) in enumerate(sorted_issues[:5], 1):
            print(f"\n{i}. {issue} ({count} cases)")
            
            if 'MISSING_CRITICAL' in issue:
                print("   🔧 FIX: Strengthen critical term validation")
                print("   📍 LOCATION: validate_case_preservation_fallback function")
                print("   💡 ACTION: Add more critical terms and make validation fail immediately")
                
            elif issue == 'TOPIC_MISMATCH':
                print("   🔧 FIX: Improve topic preservation in prompts")
                print("   📍 LOCATION: create_domain_specific_prompt function")
                print("   💡 ACTION: Add stronger topic preservation instructions")
                
            elif issue == 'INSUFFICIENT_ADVANCED_DETAIL':
                print("   🔧 FIX: Enhance advanced management prompts")
                print("   📍 LOCATION: ADVANCED MANAGEMENT CASES section in prompts")
                print("   💡 ACTION: Require specific medication details and failure descriptions")
                
            elif issue == 'FALLBACK_USED':
                print("   🔧 FIX: Investigate AI generation failures")
                print("   📍 LOCATION: generate_validated_case function")
                print("   💡 ACTION: Review why validation is too strict")
            
            # Show examples
            if issue_examples[issue]:
                print("   📝 Examples:")
                for example in issue_examples[issue]:
                    print(f"      - MCQ {example['mcq_id']} ({example['specialty']}): {example['question']}")
        
        print(f"\n⚡ PRIORITY ACTIONS NEEDED:")
        if 'MISSING_CRITICAL' in [issue for issue, _ in sorted_issues[:3]]:
            print("1. 🚨 CRITICAL: Fix missing critical terms immediately")
        if 'TOPIC_MISMATCH' in [issue for issue, _ in sorted_issues[:3]]:
            print("2. 🚨 CRITICAL: Fix topic drift issues immediately")
        if any('INSUFFICIENT' in issue for issue, _ in sorted_issues[:3]):
            print("3. ⚠️ HIGH: Improve detail level for advanced cases")
    
    def run_until_perfect(self):
        """Run cycles until perfect performance is achieved"""
        print("🚀 Starting Iterative MCQ Testing Until Perfect Performance")
        print("Testing 5 MCQs from each specialty per cycle")
        
        max_cycles = 10  # Prevent infinite loops
        
        while self.cycle_number <= max_cycles:
            cycle_results = self.run_test_cycle()
            
            if cycle_results['is_perfect']:
                print(f"\n🎉🎉🎉 PERFECT PERFORMANCE ACHIEVED IN CYCLE {self.cycle_number}! 🎉🎉🎉")
                print("All MCQs across all specialties converted successfully!")
                break
            
            print(f"\n⏭️ Moving to next cycle... (Current success rate: {cycle_results['success_rate']:.1f}%)")
            print("💡 Please implement the suggested fixes before running the next cycle.")
            
            # Ask user if they want to continue or implement fixes
            response = input("\n🤔 Continue to next cycle (c) or stop to implement fixes (s)? [c/s]: ").strip().lower()
            if response == 's':
                print("⏸️ Stopping for fix implementation. Run again after implementing fixes.")
                break
            
            self.cycle_number += 1
        
        if self.cycle_number > max_cycles:
            print(f"\n⚠️ Reached maximum cycles ({max_cycles}). Consider implementing major fixes.")
        
        self.print_final_summary()
    
    def print_final_summary(self):
        """Print final summary of all cycles"""
        if not self.test_history:
            return
        
        print(f"\n{'='*80}")
        print(f"📈 FINAL SUMMARY - {len(self.test_history)} CYCLES COMPLETED")
        print(f"{'='*80}")
        
        for cycle in self.test_history:
            cycle_num = cycle['cycle']
            success_rate = cycle['success_rate']
            total = cycle['total_tested']
            success = cycle['total_success']
            
            emoji = "🎉" if success_rate == 100 else "✅" if success_rate >= 80 else "⚠️" if success_rate >= 60 else "❌"
            print(f"Cycle {cycle_num}: {emoji} {success}/{total} ({success_rate:.1f}%)")
        
        # Show improvement trend
        if len(self.test_history) > 1:
            first_rate = self.test_history[0]['success_rate']
            last_rate = self.test_history[-1]['success_rate']
            improvement = last_rate - first_rate
            
            print(f"\n📊 Improvement: {improvement:+.1f}% ({first_rate:.1f}% → {last_rate:.1f}%)")

def main():
    """Main function to run iterative testing"""
    tester = IterativeMCQTester()
    tester.run_until_perfect()

if __name__ == "__main__":
    main()