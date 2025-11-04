#!/usr/bin/env python3
"""
Analyze Case-Based Learning Module for Technical Issues
"""

import json
import os
import re
from collections import defaultdict
from datetime import datetime

# Issues to check:
# 1. Session memory management
# 2. Case repetition patterns
# 3. Prompt efficiency
# 4. State transition logic
# 5. Error handling
# 6. Performance bottlenecks

def analyze_case_bot():
    """Analyze case_bot.py for issues"""
    issues = []
    
    # Read the case_bot.py file
    case_bot_path = '/Users/tariqalmatrudi/NEWreader/django_neurology_mcq/mcq/case_bot.py'
    with open(case_bot_path, 'r') as f:
        content = f.read()
        lines = content.split('\n')
    
    # Issue 1: Global session storage without cleanup
    if 'active_sessions = {}' in content and 'del active_sessions' not in content:
        issues.append({
            'severity': 'HIGH',
            'type': 'Memory Leak',
            'description': 'Sessions are stored globally without cleanup mechanism',
            'line': 33,
            'fix': 'Implement session timeout and cleanup'
        })
    
    # Issue 2: No case history tracking
    if 'case_history' not in content and 'previous_cases' not in content:
        issues.append({
            'severity': 'HIGH',
            'type': 'Case Repetition',
            'description': 'No mechanism to track previously shown cases',
            'fix': 'Implement case history tracking per user'
        })
    
    # Issue 3: Large prompt sizes
    prompt_sizes = []
    for i, line in enumerate(lines):
        if 'prompt' in line and '"""' in lines[i-1] if i > 0 else False:
            # Find the closing """
            j = i
            while j < len(lines) and '"""' not in lines[j]:
                j += 1
            prompt_size = j - i
            if prompt_size > 50:
                prompt_sizes.append((i, prompt_size))
    
    if prompt_sizes:
        issues.append({
            'severity': 'MEDIUM',
            'type': 'Prompt Efficiency',
            'description': f'Large prompts found ({len(prompt_sizes)} instances)',
            'lines': [p[0] for p in prompt_sizes],
            'fix': 'Optimize prompt sizes and use dynamic content injection'
        })
    
    # Issue 4: No rate limiting
    if 'rate_limit' not in content and 'throttle' not in content:
        issues.append({
            'severity': 'MEDIUM',
            'type': 'API Protection',
            'description': 'No rate limiting for API calls',
            'fix': 'Implement rate limiting to prevent abuse'
        })
    
    # Issue 5: Hardcoded temperature value
    if 'temperature=0.7' in content:
        issues.append({
            'severity': 'LOW',
            'type': 'Flexibility',
            'description': 'Hardcoded temperature value reduces case variety',
            'line': content.find('temperature=0.7'),
            'fix': 'Make temperature dynamic based on phase'
        })
    
    # Issue 6: No error recovery in state transitions
    if 'try:' not in content[content.find('CASE_STATES'):content.find('CASE_STATES') + 500]:
        issues.append({
            'severity': 'MEDIUM',
            'type': 'Error Handling',
            'description': 'State transitions lack error recovery',
            'fix': 'Add try-catch blocks around state transitions'
        })
    
    # Issue 7: Inefficient string concatenation
    concat_count = content.count('+= f"\\n')
    if concat_count > 10:
        issues.append({
            'severity': 'LOW',
            'type': 'Performance',
            'description': f'Inefficient string concatenation ({concat_count} instances)',
            'fix': 'Use list append and join for better performance'
        })
    
    # Issue 8: No session persistence
    if 'save_session' not in content and 'persist' not in content:
        issues.append({
            'severity': 'MEDIUM',
            'type': 'User Experience',
            'description': 'Sessions are lost on page reload',
            'fix': 'Implement session persistence to database'
        })
    
    return issues

def analyze_frontend():
    """Analyze frontend for issues"""
    issues = []
    
    template_path = '/Users/tariqalmatrudi/NEWreader/django_neurology_mcq/templates/mcq/case_based_learning.html'
    with open(template_path, 'r') as f:
        content = f.read()
    
    # Issue 1: No session recovery
    if 'localStorage' not in content and 'sessionStorage' not in content:
        issues.append({
            'severity': 'MEDIUM',
            'type': 'User Experience',
            'description': 'No client-side session recovery',
            'fix': 'Implement localStorage for session recovery'
        })
    
    # Issue 2: No loading states for phase transitions
    if 'transition' not in content.lower():
        issues.append({
            'severity': 'LOW',
            'type': 'UX',
            'description': 'No smooth transitions between phases',
            'fix': 'Add transition animations'
        })
    
    # Issue 3: No keyboard shortcuts
    if 'keydown' not in content or 'keyboard' not in content:
        issues.append({
            'severity': 'LOW',
            'type': 'Accessibility',
            'description': 'No keyboard shortcuts for common actions',
            'fix': 'Add keyboard shortcuts for phase navigation'
        })
    
    return issues

def analyze_case_variety():
    """Check for case repetition patterns"""
    case_bot_path = '/Users/tariqalmatrudi/NEWreader/django_neurology_mcq/mcq/case_bot.py'
    with open(case_bot_path, 'r') as f:
        content = f.read()
    
    # Extract specialty conditions
    specialty_match = re.search(r'specialty_conditions = \{(.*?)\}', content, re.DOTALL)
    if specialty_match:
        conditions_text = specialty_match.group(1)
        # Count conditions per specialty
        specialty_counts = {}
        current_specialty = None
        
        for line in conditions_text.split('\n'):
            if "'" in line and ':' in line and '[' in line:
                current_specialty = line.split("'")[1]
                specialty_counts[current_specialty] = 0
            elif current_specialty and "'" in line and ',' in line:
                specialty_counts[current_specialty] += 1
        
        # Find specialties with few cases
        low_variety = [(s, c) for s, c in specialty_counts.items() if c < 20]
        
        return {
            'total_specialties': len(specialty_counts),
            'total_conditions': sum(specialty_counts.values()),
            'average_per_specialty': sum(specialty_counts.values()) / len(specialty_counts) if specialty_counts else 0,
            'low_variety_specialties': low_variety
        }
    
    return None

def generate_report():
    """Generate comprehensive analysis report"""
    print("Analyzing Case-Based Learning Module...")
    print("=" * 60)
    
    # Analyze backend
    backend_issues = analyze_case_bot()
    print(f"\nBackend Issues Found: {len(backend_issues)}")
    for issue in backend_issues:
        print(f"\n[{issue['severity']}] {issue['type']}: {issue['description']}")
        if 'line' in issue:
            print(f"  Line: {issue['line']}")
        print(f"  Fix: {issue['fix']}")
    
    # Analyze frontend
    frontend_issues = analyze_frontend()
    print(f"\n\nFrontend Issues Found: {len(frontend_issues)}")
    for issue in frontend_issues:
        print(f"\n[{issue['severity']}] {issue['type']}: {issue['description']}")
        print(f"  Fix: {issue['fix']}")
    
    # Analyze case variety
    variety_analysis = analyze_case_variety()
    if variety_analysis:
        print(f"\n\nCase Variety Analysis:")
        print(f"  Total Specialties: {variety_analysis['total_specialties']}")
        print(f"  Total Conditions: {variety_analysis['total_conditions']}")
        print(f"  Average per Specialty: {variety_analysis['average_per_specialty']:.1f}")
        if variety_analysis['low_variety_specialties']:
            print(f"  Low Variety Specialties:")
            for spec, count in variety_analysis['low_variety_specialties']:
                print(f"    - {spec}: {count} cases")
    
    # Summary
    all_issues = backend_issues + frontend_issues
    high_priority = len([i for i in all_issues if i['severity'] == 'HIGH'])
    medium_priority = len([i for i in all_issues if i['severity'] == 'MEDIUM'])
    low_priority = len([i for i in all_issues if i['severity'] == 'LOW'])
    
    print(f"\n\nSummary:")
    print(f"  High Priority Issues: {high_priority}")
    print(f"  Medium Priority Issues: {medium_priority}")
    print(f"  Low Priority Issues: {low_priority}")
    print(f"  Total Issues: {len(all_issues)}")
    
    # Save report
    report = {
        'timestamp': datetime.now().isoformat(),
        'backend_issues': backend_issues,
        'frontend_issues': frontend_issues,
        'case_variety': variety_analysis,
        'summary': {
            'high': high_priority,
            'medium': medium_priority,
            'low': low_priority,
            'total': len(all_issues)
        }
    }
    
    with open('/Users/tariqalmatrudi/NEWreader/case_learning_analysis.json', 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"\nDetailed report saved to: case_learning_analysis.json")

if __name__ == '__main__':
    generate_report()