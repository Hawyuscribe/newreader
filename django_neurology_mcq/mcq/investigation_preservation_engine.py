"""
Investigation Preservation Engine
Ensures all diagnostic test results, imaging findings, and laboratory values from MCQs are preserved in generated cases

This module extracts and preserves critical investigation findings that are essential
for clinical decision-making and educational objectives.
"""

import re
import logging
from typing import Dict, List, Tuple, Optional, Set
from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass
class InvestigationFinding:
    """Structure for an investigation finding"""
    test_type: str
    finding: str
    full_text: str
    importance: str  # 'critical', 'supporting', 'contextual'
    category: str


class InvestigationPreservationEngine:
    """
    Extracts and preserves all investigation findings from MCQ text
    """
    
    def __init__(self):
        self.investigation_patterns = self._build_investigation_patterns()
        self.result_patterns = self._build_result_patterns()
        
    def extract_investigations(self, mcq_text: str) -> Dict[str, any]:
        """
        Extract all investigation findings from MCQ text
        
        Args:
            mcq_text: Original MCQ question text
            
        Returns:
            Dictionary of investigation findings to preserve
        """
        findings = {
            'neurophysiology': [],  # EEG, EMG, NCS, EP
            'imaging': [],  # CT, MRI, angiography
            'laboratory': [],  # Blood tests, CSF, genetics
            'pathology': [],  # Biopsy results
            'clinical_tests': [],  # Specific clinical tests
            'all_findings': []  # Complete list for validation
        }
        
        # Extract each type of investigation
        findings['neurophysiology'] = self._extract_neurophysiology_findings(mcq_text)
        findings['imaging'] = self._extract_imaging_findings(mcq_text)
        findings['laboratory'] = self._extract_laboratory_findings(mcq_text)
        findings['pathology'] = self._extract_pathology_findings(mcq_text)
        findings['clinical_tests'] = self._extract_clinical_test_findings(mcq_text)
        
        # Compile all findings
        findings['all_findings'] = (
            findings['neurophysiology'] + 
            findings['imaging'] + 
            findings['laboratory'] + 
            findings['pathology'] + 
            findings['clinical_tests']
        )
        
        return findings
    
    def _build_investigation_patterns(self) -> Dict[str, List[Dict[str, str]]]:
        """Build patterns for different investigation types"""
        return {
            'neurophysiology': [
                # EEG patterns - enhanced to handle various formats
                {'pattern': r'(EEG|electroencephalogram)\s+shows?\s+([^.]+)', 'type': 'EEG'},
                {'pattern': r'(EEG|electroencephalogram)\s+demonstrates?\s+([^.]+)', 'type': 'EEG'},
                {'pattern': r'(EEG|electroencephalogram)\s+reveals?\s+([^.]+)', 'type': 'EEG'},
                {'pattern': r'(EEG|electroencephalogram)[:]\s*([^.]+)', 'type': 'EEG'},
                # Handle "electroencephalogram (EEG) shows" format
                {'pattern': r'electroencephalogram\s*\(EEG\)\s+shows?\s+([^.]+)', 'type': 'EEG'},
                {'pattern': r'electroencephalogram\s*\(EEG\)\s+demonstrates?\s+([^.]+)', 'type': 'EEG'},
                {'pattern': r'electroencephalogram\s*\(EEG\)\s+reveals?\s+([^.]+)', 'type': 'EEG'},
                # Handle "An EEG shows" format
                {'pattern': r'An?\s+(EEG|electroencephalogram)\s+shows?\s+([^.]+)', 'type': 'EEG'},
                
                # EMG/NCS patterns
                {'pattern': r'(EMG|electromyography)\s+shows?\s+([^.]+)', 'type': 'EMG'},
                {'pattern': r'(NCS|nerve conduction study)\s+shows?\s+([^.]+)', 'type': 'NCS'},
                {'pattern': r'nerve conduction\s+shows?\s+([^.]+)', 'type': 'NCS'},
                
                # Evoked potentials
                {'pattern': r'(VEP|visual evoked potential)\s+shows?\s+([^.]+)', 'type': 'VEP'},
                {'pattern': r'(BAEP|brainstem auditory evoked potential)\s+shows?\s+([^.]+)', 'type': 'BAEP'},
                {'pattern': r'(SSEP|somatosensory evoked potential)\s+shows?\s+([^.]+)', 'type': 'SSEP'},
            ],
            
            'imaging': [
                # MRI patterns
                {'pattern': r'(MRI|magnetic resonance imaging)\s+shows?\s+([^.]+)', 'type': 'MRI'},
                {'pattern': r'(MRI|magnetic resonance imaging)\s+demonstrates?\s+([^.]+)', 'type': 'MRI'},
                {'pattern': r'(MRI|magnetic resonance imaging)\s+reveals?\s+([^.]+)', 'type': 'MRI'},
                {'pattern': r'brain\s+MRI\s+shows?\s+([^.]+)', 'type': 'MRI'},
                {'pattern': r'spine\s+MRI\s+shows?\s+([^.]+)', 'type': 'MRI'},
                
                # CT patterns
                {'pattern': r'(CT|computed tomography)\s+shows?\s+([^.]+)', 'type': 'CT'},
                {'pattern': r'(CT scan)\s+shows?\s+([^.]+)', 'type': 'CT'},
                {'pattern': r'head\s+CT\s+shows?\s+([^.]+)', 'type': 'CT'},
                
                # Other imaging
                {'pattern': r'(angiography|angiogram)\s+shows?\s+([^.]+)', 'type': 'Angiography'},
                {'pattern': r'(PET|positron emission tomography)\s+shows?\s+([^.]+)', 'type': 'PET'},
                {'pattern': r'(SPECT)\s+shows?\s+([^.]+)', 'type': 'SPECT'},
                {'pattern': r'(ultrasound|sonography)\s+shows?\s+([^.]+)', 'type': 'Ultrasound'},
            ],
            
            'laboratory': [
                # Blood tests
                {'pattern': r'(CBC|complete blood count)\s+shows?\s+([^.]+)', 'type': 'CBC'},
                {'pattern': r'(hemoglobin|Hgb|Hb)\s*[:=]\s*([0-9.]+)', 'type': 'Hemoglobin'},
                {'pattern': r'(glucose|blood sugar)\s*[:=]\s*([0-9.]+)', 'type': 'Glucose'},
                {'pattern': r'(creatinine)\s*[:=]\s*([0-9.]+)', 'type': 'Creatinine'},
                
                # CSF analysis
                {'pattern': r'(CSF|cerebrospinal fluid)\s+shows?\s+([^.]+)', 'type': 'CSF'},
                {'pattern': r'(CSF|cerebrospinal fluid)\s+analysis\s+reveals?\s+([^.]+)', 'type': 'CSF'},
                {'pattern': r'lumbar puncture\s+shows?\s+([^.]+)', 'type': 'CSF'},
                
                # Antibodies/markers
                {'pattern': r'(antibody|antibodies)\s+to\s+([^.]+)', 'type': 'Antibody'},
                {'pattern': r'(anti-[A-Za-z0-9]+)\s+antibodies?\s+([^.]+)', 'type': 'Antibody'},
                
                # Genetics
                {'pattern': r'genetic\s+testing\s+shows?\s+([^.]+)', 'type': 'Genetic'},
                {'pattern': r'(mutation|deletion)\s+in\s+([^.]+)', 'type': 'Genetic'},
            ],
            
            'pathology': [
                {'pattern': r'(biopsy)\s+shows?\s+([^.]+)', 'type': 'Biopsy'},
                {'pattern': r'(histopathology)\s+shows?\s+([^.]+)', 'type': 'Histopathology'},
                {'pattern': r'(pathology)\s+shows?\s+([^.]+)', 'type': 'Pathology'},
            ],
            
            'clinical_tests': [
                {'pattern': r'(Tensilon test)\s+([^.]+)', 'type': 'Tensilon'},
                {'pattern': r'(ice pack test)\s+([^.]+)', 'type': 'Ice pack'},
                {'pattern': r'(Romberg test)\s+([^.]+)', 'type': 'Romberg'},
            ]
        }
    
    def _build_result_patterns(self) -> List[str]:
        """Build patterns for result descriptions"""
        return [
            'positive', 'negative', 'normal', 'abnormal', 'elevated', 'decreased',
            'shows', 'demonstrates', 'reveals', 'consistent with', 'suggestive of',
            'compatible with', 'diagnostic of', 'typical for', 'characteristic of'
        ]
    
    def _extract_neurophysiology_findings(self, text: str) -> List[InvestigationFinding]:
        """Extract neurophysiology test findings"""
        findings = []
        
        for pattern_info in self.investigation_patterns['neurophysiology']:
            matches = re.finditer(pattern_info['pattern'], text, re.IGNORECASE)
            for match in matches:
                test_type = pattern_info['type']
                
                # Extract the finding text
                if len(match.groups()) >= 2:
                    finding_text = match.group(2).strip()
                else:
                    finding_text = match.group(1).strip()
                
                finding = InvestigationFinding(
                    test_type=test_type,
                    finding=finding_text,
                    full_text=match.group(0),
                    importance='critical' if test_type == 'EEG' else 'supporting',
                    category='neurophysiology'
                )
                findings.append(finding)
        
        return findings
    
    def _extract_imaging_findings(self, text: str) -> List[InvestigationFinding]:
        """Extract imaging findings"""
        findings = []
        
        for pattern_info in self.investigation_patterns['imaging']:
            matches = re.finditer(pattern_info['pattern'], text, re.IGNORECASE)
            for match in matches:
                test_type = pattern_info['type']
                
                if len(match.groups()) >= 2:
                    finding_text = match.group(2).strip()
                else:
                    finding_text = match.group(1).strip()
                
                finding = InvestigationFinding(
                    test_type=test_type,
                    finding=finding_text,
                    full_text=match.group(0),
                    importance='critical',
                    category='imaging'
                )
                findings.append(finding)
        
        return findings
    
    def _extract_laboratory_findings(self, text: str) -> List[InvestigationFinding]:
        """Extract laboratory findings"""
        findings = []
        
        for pattern_info in self.investigation_patterns['laboratory']:
            matches = re.finditer(pattern_info['pattern'], text, re.IGNORECASE)
            for match in matches:
                test_type = pattern_info['type']
                
                if len(match.groups()) >= 2:
                    finding_text = match.group(2).strip()
                else:
                    finding_text = match.group(1).strip()
                
                finding = InvestigationFinding(
                    test_type=test_type,
                    finding=finding_text,
                    full_text=match.group(0),
                    importance='supporting',
                    category='laboratory'
                )
                findings.append(finding)
        
        return findings
    
    def _extract_pathology_findings(self, text: str) -> List[InvestigationFinding]:
        """Extract pathology findings"""
        findings = []
        
        for pattern_info in self.investigation_patterns['pathology']:
            matches = re.finditer(pattern_info['pattern'], text, re.IGNORECASE)
            for match in matches:
                test_type = pattern_info['type']
                
                if len(match.groups()) >= 2:
                    finding_text = match.group(2).strip()
                else:
                    finding_text = match.group(1).strip()
                
                finding = InvestigationFinding(
                    test_type=test_type,
                    finding=finding_text,
                    full_text=match.group(0),
                    importance='critical',
                    category='pathology'
                )
                findings.append(finding)
        
        return findings
    
    def _extract_clinical_test_findings(self, text: str) -> List[InvestigationFinding]:
        """Extract clinical test findings"""
        findings = []
        
        for pattern_info in self.investigation_patterns['clinical_tests']:
            matches = re.finditer(pattern_info['pattern'], text, re.IGNORECASE)
            for match in matches:
                test_type = pattern_info['type']
                
                if len(match.groups()) >= 1:
                    finding_text = match.group(1).strip()
                else:
                    finding_text = match.group(0).strip()
                
                finding = InvestigationFinding(
                    test_type=test_type,
                    finding=finding_text,
                    full_text=match.group(0),
                    importance='supporting',
                    category='clinical_tests'
                )
                findings.append(finding)
        
        return findings
    
    def generate_investigation_preservation_prompt(self, mcq_text: str) -> str:
        """Generate preservation prompt for investigations"""
        findings = self.extract_investigations(mcq_text)
        
        if not findings['all_findings']:
            return ""
        
        prompt = """
CRITICAL INVESTIGATION PRESERVATION REQUIREMENTS:

ALL DIAGNOSTIC TEST RESULTS FROM THE MCQ MUST BE PRESERVED EXACTLY:
"""
        
        # Group by category
        for category in ['neurophysiology', 'imaging', 'laboratory', 'pathology', 'clinical_tests']:
            category_findings = findings.get(category, [])
            if category_findings:
                prompt += f"\n{category.upper()} FINDINGS:\n"
                for finding in category_findings:
                    prompt += f"- MUST INCLUDE: {finding.full_text}\n"
        
        prompt += """
VALIDATION REQUIREMENTS:
- The case MUST include ALL investigation findings mentioned in the original MCQ
- Test results must be presented in the EXACT same format and with the SAME values
- Critical findings (EEG, MRI, CT, biopsy) are MANDATORY for case validity
- These findings directly determine the diagnosis and management approach

FAILURE TO PRESERVE INVESTIGATION FINDINGS WILL COMPROMISE THE EDUCATIONAL OBJECTIVE.
"""
        
        return prompt
    
    def validate_investigation_preservation(self, mcq_text: str, case_text: str) -> Dict[str, any]:
        """Validate that all investigations are preserved in the case"""
        original_findings = self.extract_investigations(mcq_text)
        
        validation_result = {
            'valid': True,
            'missing_investigations': [],
            'preserved_investigations': [],
            'preservation_rate': 0.0
        }
        
        if not original_findings['all_findings']:
            validation_result['preservation_rate'] = 100.0
            return validation_result
        
        case_text_lower = case_text.lower()
        
        for finding in original_findings['all_findings']:
            # Check if the finding is preserved in the case
            finding_keywords = self._extract_keywords(finding.finding)
            
            preserved = False
            for keyword in finding_keywords:
                if keyword.lower() in case_text_lower:
                    preserved = True
                    break
            
            if preserved:
                validation_result['preserved_investigations'].append(finding.full_text)
            else:
                validation_result['missing_investigations'].append(finding.full_text)
                validation_result['valid'] = False
        
        total_findings = len(original_findings['all_findings'])
        preserved_count = len(validation_result['preserved_investigations'])
        validation_result['preservation_rate'] = (preserved_count / total_findings * 100) if total_findings > 0 else 100.0
        
        return validation_result
    
    def _extract_keywords(self, finding_text: str) -> List[str]:
        """Extract key words from investigation finding"""
        # Remove common words
        stop_words = {'the', 'a', 'an', 'and', 'or', 'with', 'shows', 'demonstrates', 'reveals'}
        
        # Extract significant words
        words = re.findall(r'\b\w+\b', finding_text.lower())
        keywords = [w for w in words if w not in stop_words and len(w) > 2]
        
        return keywords


def enhance_case_with_investigation_findings(case_text: str, mcq_text: str) -> str:
    """
    Add investigation findings to case presentation if missing
    
    Args:
        case_text: Generated case text
        mcq_text: Original MCQ text
        
    Returns:
        Enhanced case text with investigation findings
    """
    try:
        engine = InvestigationPreservationEngine()
        findings = engine.extract_investigations(mcq_text)
        
        if not findings['all_findings']:
            return case_text
        
        # Check if investigations are already included
        validation = engine.validate_investigation_preservation(mcq_text, case_text)
        
        if validation['valid']:
            return case_text
        
        # Add missing investigations
        investigation_section = "\n\nInvestigations performed:\n"
        
        for finding in findings['all_findings']:
            if finding.full_text not in validation['preserved_investigations']:
                investigation_section += f"- {finding.full_text}\n"
        
        # Insert before the question prompt
        if "Given this" in case_text:
            parts = case_text.split("Given this", 1)
            enhanced_text = parts[0].rstrip() + investigation_section + "\nGiven this" + parts[1]
        else:
            enhanced_text = case_text.rstrip() + investigation_section
        
        return enhanced_text
        
    except Exception as e:
        logger.error(f"Error enhancing case with investigations: {e}")
        return case_text


if __name__ == "__main__":
    # Test the investigation preservation engine
    test_mcq = "A 7-year-old boy presents with visual hallucinations. An electroencephalogram (EEG) shows occipital lobe spikes. MRI brain shows normal findings. What is the management?"
    
    engine = InvestigationPreservationEngine()
    findings = engine.extract_investigations(test_mcq)
    
    print("Investigation Findings Extracted:")
    for finding in findings['all_findings']:
        print(f"- {finding.test_type}: {finding.finding} (Full: {finding.full_text})")
    
    prompt = engine.generate_investigation_preservation_prompt(test_mcq)
    print("\nPreservation Prompt:")
    print(prompt)