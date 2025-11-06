#!/usr/bin/env python3
"""
Test 10 random MCQs from each different category/subspecialty
Comprehensive validation across all medical domains
"""

import os
import sys
import django
import random

# Setup Django
sys.path.append('/Users/tariqalmatrudi/NEWreader/django_neurology_mcq')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
django.setup()

from mcq.models import MCQ
from mcq.mcq_case_converter import convert_mcq_to_case

def test_10_per_category():
    """Test 10 random MCQs from each subspecialty"""
    
    print("🧪 COMPREHENSIVE CATEGORY TESTING")
    print("=" * 100)
    print("Testing 10 random MCQs from each subspecialty to validate system performance")
    print()
    
    # Get all subspecialties with their counts
    specialties = MCQ.objects.values_list('subspecialty', flat=True).distinct()
    specialties = [s for s in specialties if s and s.strip()]
    
    # Filter specialties with enough MCQs and get counts
    valid_specialties = []
    for specialty in specialties:
        count = MCQ.objects.filter(subspecialty=specialty).count()
        if count >= 10:  # Only test specialties with at least 10 MCQs
            valid_specialties.append((specialty, count))
    
    # Sort by count for better representation
    valid_specialties.sort(key=lambda x: x[1], reverse=True)
    
    print(f"📊 Found {len(valid_specialties)} subspecialties with ≥10 MCQs")
    print(f"Total MCQs in database: {MCQ.objects.count()}")
    print()
    
    overall_results = []
    category_summaries = {}
    
    for i, (specialty, mcq_count) in enumerate(valid_specialties, 1):
        print(f"\n🏥 {i}/{len(valid_specialties)}: {specialty}")
        print(f"📊 Available MCQs: {mcq_count}")
        print("-" * 80)
        
        # Get 10 random MCQs from this specialty
        all_mcqs = list(MCQ.objects.filter(subspecialty=specialty))
        test_mcqs = random.sample(all_mcqs, min(10, len(all_mcqs)))
        
        category_results = []
        successful_conversions = 0
        ai_successes = 0
        excellent_cases = 0
        good_cases = 0
        
        for j, mcq in enumerate(test_mcqs, 1):
            print(f"  {j:2d}/10: MCQ {mcq.id} - ", end="")
            
            try:
                # Test conversion
                case_data = convert_mcq_to_case(mcq)
                
                # Extract case details
                clinical_presentation = case_data.get('clinical_presentation', '')
                fallback_used = case_data.get('fallback_used', False)
                question_type = case_data.get('question_type', '')
                
                # Quick quality assessment
                has_content = len(clinical_presentation.strip()) > 20
                
                if has_content:
                    successful_conversions += 1
                    
                    if not fallback_used:
                        ai_successes += 1
                    
                    # Assess content preservation
                    original_lower = mcq.question_text.lower()
                    case_lower = clinical_presentation.lower()
                    
                    # Extract critical terms
                    critical_terms = extract_critical_terms_simple(original_lower)
                    preserved_terms = [term for term in critical_terms if term in case_lower]
                    
                    preservation_rate = len(preserved_terms) / len(critical_terms) if critical_terms else 1.0
                    
                    # Quality scoring
                    quality_indicators = 0
                    if len(clinical_presentation) > 50:
                        quality_indicators += 1
                    if any(word in case_lower for word in ['presents', 'history', 'examination']):
                        quality_indicators += 1
                    if any(char.isdigit() for char in clinical_presentation):
                        quality_indicators += 1
                    if preservation_rate >= 0.8:
                        quality_indicators += 1
                    
                    if quality_indicators >= 3 and preservation_rate >= 0.8:
                        excellent_cases += 1
                        print("🎉 EXCELLENT")
                    elif quality_indicators >= 2 and preservation_rate >= 0.6:
                        good_cases += 1
                        print("✅ GOOD")
                    elif fallback_used:
                        print("⚠️ FALLBACK")
                    else:
                        print("🟡 FAIR")
                    
                    result = {
                        'mcq_id': mcq.id,
                        'success': True,
                        'ai_generated': not fallback_used,
                        'preservation_rate': preservation_rate,
                        'quality_indicators': quality_indicators,
                        'question_type': question_type
                    }
                else:
                    print("❌ NO CONTENT")
                    result = {
                        'mcq_id': mcq.id,
                        'success': False,
                        'error': 'No content generated'
                    }
                
                category_results.append(result)
                overall_results.append(result)
                
            except Exception as e:
                print(f"❌ ERROR: {str(e)[:50]}...")
                result = {
                    'mcq_id': mcq.id,
                    'success': False,
                    'error': str(e)
                }
                category_results.append(result)
                overall_results.append(result)
        
        # Category summary
        total_tested = len(category_results)
        success_rate = (successful_conversions / total_tested) * 100 if total_tested > 0 else 0
        ai_success_rate = (ai_successes / total_tested) * 100 if total_tested > 0 else 0
        excellence_rate = (excellent_cases / total_tested) * 100 if total_tested > 0 else 0
        
        category_summaries[specialty] = {
            'total_tested': total_tested,
            'successful_conversions': successful_conversions,
            'ai_successes': ai_successes,
            'excellent_cases': excellent_cases,
            'good_cases': good_cases,
            'success_rate': success_rate,
            'ai_success_rate': ai_success_rate,
            'excellence_rate': excellence_rate
        }
        
        print(f"  📊 Summary: {successful_conversions}/10 success ({success_rate:.0f}%) | {ai_successes}/10 AI ({ai_success_rate:.0f}%) | {excellent_cases}/10 excellent ({excellence_rate:.0f}%)")
    
    # Generate comprehensive report
    generate_comprehensive_report(overall_results, category_summaries)
    
    return overall_results, category_summaries

def extract_critical_terms_simple(text):
    """Extract critical medical terms for preservation checking"""
    critical_terms = []
    
    terms = [
        'seizure', 'epilepsy', 'parkinson', 'huntington', 'alzheimer',
        'multiple sclerosis', 'ms', 'stroke', 'migraine', 'headache',
        'neuropathy', 'myopathy', 'weakness', 'tremor', 'rigidity',
        'horner', 'ptosis', 'miosis', 'diplopia', 'ataxia',
        'bilateral', 'caudate', 'thalamus', 'brainstem', 'cerebellum'
    ]
    
    for term in terms:
        if term in text:
            critical_terms.append(term)
    
    return critical_terms

def generate_comprehensive_report(overall_results, category_summaries):
    """Generate comprehensive test report"""
    
    print(f"\n{'='*100}")
    print(f"📊 COMPREHENSIVE CATEGORY TEST RESULTS")
    print(f"{'='*100}")
    
    # Overall statistics
    total_tested = len(overall_results)
    total_successful = len([r for r in overall_results if r.get('success', False)])
    total_ai_generated = len([r for r in overall_results if r.get('ai_generated', False)])
    total_excellent = len([r for r in overall_results if r.get('quality_indicators', 0) >= 3])
    
    overall_success_rate = (total_successful / total_tested) * 100 if total_tested > 0 else 0
    overall_ai_rate = (total_ai_generated / total_tested) * 100 if total_tested > 0 else 0
    overall_excellence_rate = (total_excellent / total_tested) * 100 if total_tested > 0 else 0
    
    print(f"\n🎯 OVERALL PERFORMANCE:")
    print(f"  Total MCQs Tested: {total_tested}")
    print(f"  Successful Conversions: {total_successful}/{total_tested} ({overall_success_rate:.1f}%)")
    print(f"  AI Generated Cases: {total_ai_generated}/{total_tested} ({overall_ai_rate:.1f}%)")
    print(f"  Excellent Quality Cases: {total_excellent}/{total_tested} ({overall_excellence_rate:.1f}%)")
    
    # Performance assessment
    print(f"\n🏆 SYSTEM ASSESSMENT:")
    if overall_success_rate >= 95:
        print(f"🎉 OUTSTANDING: {overall_success_rate:.1f}% success rate - System performing exceptionally!")
    elif overall_success_rate >= 85:
        print(f"🎉 EXCELLENT: {overall_success_rate:.1f}% success rate - System working very well!")
    elif overall_success_rate >= 75:
        print(f"✅ GOOD: {overall_success_rate:.1f}% success rate - System working well!")
    elif overall_success_rate >= 60:
        print(f"🟡 ACCEPTABLE: {overall_success_rate:.1f}% success rate - Room for improvement")
    else:
        print(f"⚠️ NEEDS WORK: {overall_success_rate:.1f}% success rate - Significant improvements needed")
    
    # Category performance ranking
    print(f"\n🏆 TOP PERFORMING CATEGORIES:")
    sorted_categories = sorted(category_summaries.items(), 
                              key=lambda x: (x[1]['success_rate'], x[1]['excellence_rate']), 
                              reverse=True)
    
    for i, (category, summary) in enumerate(sorted_categories[:10], 1):
        success_rate = summary['success_rate']
        excellence_rate = summary['excellence_rate']
        ai_rate = summary['ai_success_rate']
        
        emoji = "🎉" if success_rate >= 90 else "✅" if success_rate >= 80 else "🟡" if success_rate >= 70 else "⚠️"
        print(f"  {i:2d}. {emoji} {category}: {success_rate:.0f}% success | {excellence_rate:.0f}% excellent | {ai_rate:.0f}% AI")
    
    # Categories needing attention
    problem_categories = [(cat, summ) for cat, summ in sorted_categories if summ['success_rate'] < 80]
    
    if problem_categories:
        print(f"\n⚠️ CATEGORIES NEEDING ATTENTION:")
        for category, summary in problem_categories:
            success_rate = summary['success_rate']
            ai_rate = summary['ai_success_rate']
            print(f"  ❌ {category}: {success_rate:.0f}% success | {ai_rate:.0f}% AI generation")
    
    # Quality distribution
    print(f"\n📈 QUALITY DISTRIBUTION:")
    fallback_count = total_successful - total_ai_generated
    fallback_rate = (fallback_count / total_tested) * 100 if total_tested > 0 else 0
    
    print(f"  🎉 Excellent Quality: {total_excellent}/{total_tested} ({overall_excellence_rate:.1f}%)")
    print(f"  🤖 AI Generated: {total_ai_generated}/{total_tested} ({overall_ai_rate:.1f}%)")
    print(f"  🔄 Fallback Used: {fallback_count}/{total_tested} ({fallback_rate:.1f}%)")
    
    # Recommendations
    print(f"\n🔧 RECOMMENDATIONS:")
    if overall_success_rate >= 90:
        print(f"✅ System is performing excellently across all categories!")
        print(f"✅ Ready for full production deployment")
    elif overall_success_rate >= 80:
        print(f"✅ System is working well with minor opportunities for improvement")
        if fallback_rate > 30:
            print(f"💡 Consider improving AI generation to reduce fallback usage")
    else:
        print(f"⚠️ System needs improvement in underperforming categories")
        if problem_categories:
            print(f"🎯 Focus on: {', '.join([cat for cat, _ in problem_categories[:3]])}")
    
    print(f"\n✅ Comprehensive category testing complete!")
    print(f"📊 Tested {len(category_summaries)} subspecialties with {total_tested} total MCQs")

def main():
    """Run comprehensive category testing"""
    results, summaries = test_10_per_category()
    return results, summaries

if __name__ == "__main__":
    main()