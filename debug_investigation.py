#!/usr/bin/env python3
import sys
sys.path.append('django_neurology_mcq/mcq')

from investigation_preservation_engine import InvestigationPreservationEngine

engine = InvestigationPreservationEngine()
test_mcq = "A 7-year-old boy presents with visual hallucinations. An electroencephalogram (EEG) shows occipital lobe spikes. What is the management?"

findings = engine.extract_investigations(test_mcq)
print("Extracted findings:")
for category, category_findings in findings.items():
    if category_findings and category != 'all_findings':
        print(f"{category}: {len(category_findings)} findings")
        for finding in category_findings:
            print(f"  - {finding.test_type}: {finding.finding}")

print(f"Total findings: {len(findings['all_findings'])}")

# Also test the patterns directly
import re
for pattern_info in engine.investigation_patterns['neurophysiology']:
    matches = re.finditer(pattern_info['pattern'], test_mcq, re.IGNORECASE)
    for match in matches:
        print(f"Pattern '{pattern_info['pattern']}' matched: {match.group(0)}")