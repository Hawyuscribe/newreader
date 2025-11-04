"""
Clinical Detail Extractor for MCQ-to-Case Conversion
Ensures all critical clinical details from MCQs are preserved in case presentations

This module implements a comprehensive solution to identify and preserve
specific clinical signs, lateralization, and medical terminology from MCQs.
"""

import re
import logging
from typing import Dict, List, Set, Tuple, Optional

logger = logging.getLogger(__name__)


class ClinicalDetailExtractor:
    """
    Extracts and preserves critical clinical details from MCQ text
    """
    
    def __init__(self):
        # Initialize pattern databases
        self.lateralization_patterns = self._build_lateralization_patterns()
        self.specific_signs_patterns = self._build_specific_signs_patterns()
        self.clinical_context_patterns = self._build_clinical_context_patterns()
        self.temporal_patterns = self._build_temporal_patterns()
        self.anatomical_patterns = self._build_anatomical_patterns()
        
    def extract_critical_details(self, mcq_text: str, correct_answer: str = "") -> Dict[str, any]:
        """
        Extract all critical clinical details that must be preserved
        
        Args:
            mcq_text: Original MCQ question text
            correct_answer: Correct answer text
            
        Returns:
            Dictionary of critical details to preserve
        """
        details = {
            'lateralization': self._extract_lateralization(mcq_text),
            'specific_signs': self._extract_specific_signs(mcq_text),
            'clinical_context': self._extract_clinical_context(mcq_text),
            'temporal_context': self._extract_temporal_context(mcq_text),
            'anatomical_specifics': self._extract_anatomical_specifics(mcq_text),
            'critical_phrases': self._extract_critical_phrases(mcq_text),
            'investigation_findings': self._extract_investigation_findings(mcq_text),
            'preservation_requirements': self._generate_preservation_requirements(mcq_text)
        }
        
        return details
    
    def _build_lateralization_patterns(self) -> List[Dict[str, str]]:
        """Build patterns for detecting lateralization"""
        return [
            {'pattern': r'\bright\s+(side|sided|hand|arm|leg|eye|facial|temporal|frontal|parietal|occipital)', 'type': 'right_sided'},
            {'pattern': r'\bleft\s+(side|sided|hand|arm|leg|eye|facial|temporal|frontal|parietal|occipital)', 'type': 'left_sided'},
            {'pattern': r'\bright\s+(weakness|numbness|tremor|rigidity|dystonia|seizure)', 'type': 'right_symptom'},
            {'pattern': r'\bleft\s+(weakness|numbness|tremor|rigidity|dystonia|seizure)', 'type': 'left_symptom'},
            {'pattern': r'\bunilateral\s+right', 'type': 'unilateral_right'},
            {'pattern': r'\bunilateral\s+left', 'type': 'unilateral_left'},
            {'pattern': r'\bipsilateral', 'type': 'ipsilateral'},
            {'pattern': r'\bcontralateral', 'type': 'contralateral'},
            {'pattern': r'\bbilateral', 'type': 'bilateral'},
        ]
    
    def _build_specific_signs_patterns(self) -> List[Dict[str, str]]:
        """Build patterns for specific clinical signs"""
        return [
            # Neurological signs
            {'pattern': r'\bfigure\s+of\s+4\b', 'type': 'dystonic_sign', 'term': 'figure of 4'},
            {'pattern': r'\bfencing\s+posture\b', 'type': 'seizure_sign', 'term': 'fencing posture'},
            {'pattern': r'\bhorner\'?s\s+syndrome\b', 'type': 'autonomic_sign', 'term': "Horner's syndrome"},
            {'pattern': r'\bptosis\b', 'type': 'cranial_nerve_sign', 'term': 'ptosis'},
            {'pattern': r'\bmiosis\b', 'type': 'pupil_sign', 'term': 'miosis'},
            {'pattern': r'\bmydriasis\b', 'type': 'pupil_sign', 'term': 'mydriasis'},
            {'pattern': r'\banisocoria\b', 'type': 'pupil_sign', 'term': 'anisocoria'},
            {'pattern': r'\bnystagmus\b', 'type': 'ocular_sign', 'term': 'nystagmus'},
            {'pattern': r'\boscillopsia\b', 'type': 'visual_sign', 'term': 'oscillopsia'},
            {'pattern': r'\bdiplopia\b', 'type': 'visual_sign', 'term': 'diplopia'},
            {'pattern': r'\bhemianopia\b', 'type': 'visual_field_sign', 'term': 'hemianopia'},
            {'pattern': r'\bquadrantanopia\b', 'type': 'visual_field_sign', 'term': 'quadrantanopia'},
            {'pattern': r'\baphasia\b', 'type': 'language_sign', 'term': 'aphasia'},
            {'pattern': r'\bdysarthria\b', 'type': 'speech_sign', 'term': 'dysarthria'},
            {'pattern': r'\bdysphagia\b', 'type': 'swallowing_sign', 'term': 'dysphagia'},
            {'pattern': r'\bataxia\b', 'type': 'coordination_sign', 'term': 'ataxia'},
            {'pattern': r'\bdysmetria\b', 'type': 'coordination_sign', 'term': 'dysmetria'},
            {'pattern': r'\bhemiparesis\b', 'type': 'motor_sign', 'term': 'hemiparesis'},
            {'pattern': r'\bhemiplegia\b', 'type': 'motor_sign', 'term': 'hemiplegia'},
            {'pattern': r'\bquadriparesis\b', 'type': 'motor_sign', 'term': 'quadriparesis'},
            {'pattern': r'\bquadriplegia\b', 'type': 'motor_sign', 'term': 'quadriplegia'},
            {'pattern': r'\bparaparesis\b', 'type': 'motor_sign', 'term': 'paraparesis'},
            {'pattern': r'\bparaplegia\b', 'type': 'motor_sign', 'term': 'paraplegia'},
            {'pattern': r'\bhypesthesia\b', 'type': 'sensory_sign', 'term': 'hypesthesia'},
            {'pattern': r'\banesthesia\b', 'type': 'sensory_sign', 'term': 'anesthesia'},
            {'pattern': r'\bhyperreflexia\b', 'type': 'reflex_sign', 'term': 'hyperreflexia'},
            {'pattern': r'\bhyporeflexia\b', 'type': 'reflex_sign', 'term': 'hyporeflexia'},
            {'pattern': r'\bareflexia\b', 'type': 'reflex_sign', 'term': 'areflexia'},
            {'pattern': r'\bbabinski\s+sign\b', 'type': 'pathological_reflex', 'term': 'Babinski sign'},
            {'pattern': r'\bclonus\b', 'type': 'pathological_reflex', 'term': 'clonus'},
            
            # Movement disorder signs
            {'pattern': r'\bbradykinesia\b', 'type': 'movement_sign', 'term': 'bradykinesia'},
            {'pattern': r'\brigidity\b', 'type': 'movement_sign', 'term': 'rigidity'},
            {'pattern': r'\btremor\b', 'type': 'movement_sign', 'term': 'tremor'},
            {'pattern': r'\bchorea\b', 'type': 'movement_sign', 'term': 'chorea'},
            {'pattern': r'\ballism\b', 'type': 'movement_sign', 'term': 'ballism'},
            {'pattern': r'\bdystonia\b', 'type': 'movement_sign', 'term': 'dystonia'},
            {'pattern': r'\bmyoclonus\b', 'type': 'movement_sign', 'term': 'myoclonus'},
            
            # Seizure-specific signs
            {'pattern': r'\bnose\s+rubbing\b', 'type': 'automatism', 'term': 'nose rubbing'},
            {'pattern': r'\blip\s+smacking\b', 'type': 'automatism', 'term': 'lip smacking'},
            {'pattern': r'\bchewing\s+movements\b', 'type': 'automatism', 'term': 'chewing movements'},
            {'pattern': r'\bfidgeting\b', 'type': 'automatism', 'term': 'fidgeting'},
            {'pattern': r'\bpicking\s+movements\b', 'type': 'automatism', 'term': 'picking movements'},
            {'pattern': r'\btonic\s+posturing\b', 'type': 'seizure_sign', 'term': 'tonic posturing'},
            {'pattern': r'\bclonic\s+jerking\b', 'type': 'seizure_sign', 'term': 'clonic jerking'},
            {'pattern': r'\btonic[-\\s]clonic\b', 'type': 'seizure_sign', 'term': 'tonic-clonic'},
        ]
    
    def _build_clinical_context_patterns(self) -> List[Dict[str, str]]:
        """Build patterns for clinical context"""
        return [
            # Trauma context
            {'pattern': r'\btraumatic\s+brain\s+injury\b', 'type': 'trauma', 'context': 'TBI'},
            {'pattern': r'\bhead\s+trauma\b', 'type': 'trauma', 'context': 'head trauma'},
            {'pattern': r'\bmotorcycle\s+accident\b', 'type': 'trauma', 'context': 'motorcycle accident'},
            {'pattern': r'\bcar\s+accident\b', 'type': 'trauma', 'context': 'motor vehicle accident'},
            {'pattern': r'\bfall\s+from\s+height\b', 'type': 'trauma', 'context': 'fall from height'},
            {'pattern': r'\bsports\s+injury\b', 'type': 'trauma', 'context': 'sports injury'},
            
            # Infectious context
            {'pattern': r'\bmeningitis\b', 'type': 'infectious', 'context': 'meningitis'},
            {'pattern': r'\bencephalitis\b', 'type': 'infectious', 'context': 'encephalitis'},
            {'pattern': r'\babscess\b', 'type': 'infectious', 'context': 'abscess'},
            
            # Vascular context
            {'pattern': r'\bstroke\b', 'type': 'vascular', 'context': 'stroke'},
            {'pattern': r'\binfarct\b', 'type': 'vascular', 'context': 'infarct'},
            {'pattern': r'\bhemorrhage\b', 'type': 'vascular', 'context': 'hemorrhage'},
            {'pattern': r'\baneurysm\b', 'type': 'vascular', 'context': 'aneurysm'},
            {'pattern': r'\bav\s+malformation\b', 'type': 'vascular', 'context': 'AV malformation'},
            
            # Degenerative context
            {'pattern': r'\bparkinson\b', 'type': 'degenerative', 'context': 'Parkinson disease'},
            {'pattern': r'\balzheimer\b', 'type': 'degenerative', 'context': 'Alzheimer disease'},
            {'pattern': r'\bmultiple\s+sclerosis\b', 'type': 'demyelinating', 'context': 'multiple sclerosis'},
        ]
    
    def _build_temporal_patterns(self) -> List[Dict[str, str]]:
        """Build patterns for temporal context"""
        return [
            {'pattern': r'\bacute\b', 'type': 'acute'},
            {'pattern': r'\bchronic\b', 'type': 'chronic'},
            {'pattern': r'\bsubacute\b', 'type': 'subacute'},
            {'pattern': r'\bsudden\s+onset\b', 'type': 'sudden'},
            {'pattern': r'\bgradual\s+onset\b', 'type': 'gradual'},
            {'pattern': r'\bprogressive\b', 'type': 'progressive'},
            {'pattern': r'\bintermittent\b', 'type': 'intermittent'},
            {'pattern': r'\bepisodic\b', 'type': 'episodic'},
            {'pattern': r'\b(\d+)\s+years?\s+ago\b', 'type': 'years_ago'},
            {'pattern': r'\b(\d+)\s+months?\s+ago\b', 'type': 'months_ago'},
            {'pattern': r'\b(\d+)\s+weeks?\s+ago\b', 'type': 'weeks_ago'},
            {'pattern': r'\b(\d+)\s+days?\s+ago\b', 'type': 'days_ago'},
            {'pattern': r'\b(\d+)\s+hours?\s+ago\b', 'type': 'hours_ago'},
        ]
    
    def _build_anatomical_patterns(self) -> List[Dict[str, str]]:
        """Build patterns for specific anatomical locations"""
        return [
            # Brain regions
            {'pattern': r'\bfrontal\s+lobe\b', 'type': 'brain_region', 'location': 'frontal lobe'},
            {'pattern': r'\btemporal\s+lobe\b', 'type': 'brain_region', 'location': 'temporal lobe'},
            {'pattern': r'\bparietal\s+lobe\b', 'type': 'brain_region', 'location': 'parietal lobe'},
            {'pattern': r'\boccipital\s+lobe\b', 'type': 'brain_region', 'location': 'occipital lobe'},
            {'pattern': r'\bcerebellum\b', 'type': 'brain_region', 'location': 'cerebellum'},
            {'pattern': r'\bbrainstem\b', 'type': 'brain_region', 'location': 'brainstem'},
            {'pattern': r'\bmidbrain\b', 'type': 'brain_region', 'location': 'midbrain'},
            {'pattern': r'\bpons\b', 'type': 'brain_region', 'location': 'pons'},
            {'pattern': r'\bmedulla\b', 'type': 'brain_region', 'location': 'medulla'},
            {'pattern': r'\bthalamus\b', 'type': 'brain_region', 'location': 'thalamus'},
            {'pattern': r'\bhypothalamus\b', 'type': 'brain_region', 'location': 'hypothalamus'},
            {'pattern': r'\bbasal\s+ganglia\b', 'type': 'brain_region', 'location': 'basal ganglia'},
            {'pattern': r'\bcaudate\b', 'type': 'brain_region', 'location': 'caudate'},
            {'pattern': r'\bputamen\b', 'type': 'brain_region', 'location': 'putamen'},
            {'pattern': r'\bglobus\s+pallidus\b', 'type': 'brain_region', 'location': 'globus pallidus'},
            {'pattern': r'\bsubstantia\s+nigra\b', 'type': 'brain_region', 'location': 'substantia nigra'},
            
            # Specific nuclei
            {'pattern': r'\binferior\s+olive\b', 'type': 'nucleus', 'location': 'inferior olive'},
            {'pattern': r'\binterstitial\s+nucleus\s+of\s+cajal\b', 'type': 'nucleus', 'location': 'interstitial nucleus of Cajal'},
            {'pattern': r'\bdentate\s+nucleus\b', 'type': 'nucleus', 'location': 'dentate nucleus'},
            {'pattern': r'\bred\s+nucleus\b', 'type': 'nucleus', 'location': 'red nucleus'},
            
            # Spinal regions
            {'pattern': r'\bcervical\s+spine\b', 'type': 'spinal_region', 'location': 'cervical spine'},
            {'pattern': r'\bthoracic\s+spine\b', 'type': 'spinal_region', 'location': 'thoracic spine'},
            {'pattern': r'\blumbar\s+spine\b', 'type': 'spinal_region', 'location': 'lumbar spine'},
            {'pattern': r'\bsacral\s+spine\b', 'type': 'spinal_region', 'location': 'sacral spine'},
        ]
    
    def _extract_lateralization(self, text: str) -> List[Dict[str, str]]:
        """Extract lateralization information"""
        lateralization = []
        text_lower = text.lower()
        
        for pattern_info in self.lateralization_patterns:
            matches = re.finditer(pattern_info['pattern'], text_lower, re.IGNORECASE)
            for match in matches:
                lateralization.append({
                    'type': pattern_info['type'],
                    'text': match.group(),
                    'position': (match.start(), match.end()),
                    'full_context': text[max(0, match.start()-20):match.end()+20]
                })
        
        return lateralization
    
    def _extract_specific_signs(self, text: str) -> List[Dict[str, str]]:
        """Extract specific clinical signs"""
        signs = []
        text_lower = text.lower()
        
        for pattern_info in self.specific_signs_patterns:
            matches = re.finditer(pattern_info['pattern'], text_lower, re.IGNORECASE)
            for match in matches:
                signs.append({
                    'type': pattern_info['type'],
                    'term': pattern_info['term'],
                    'text': match.group(),
                    'position': (match.start(), match.end()),
                    'full_context': text[max(0, match.start()-20):match.end()+20]
                })
        
        return signs
    
    def _extract_clinical_context(self, text: str) -> List[Dict[str, str]]:
        """Extract clinical context"""
        context = []
        text_lower = text.lower()
        
        for pattern_info in self.clinical_context_patterns:
            matches = re.finditer(pattern_info['pattern'], text_lower, re.IGNORECASE)
            for match in matches:
                context.append({
                    'type': pattern_info['type'],
                    'context': pattern_info['context'],
                    'text': match.group(),
                    'position': (match.start(), match.end())
                })
        
        return context
    
    def _extract_temporal_context(self, text: str) -> List[Dict[str, str]]:
        """Extract temporal context"""
        temporal = []
        text_lower = text.lower()
        
        for pattern_info in self.temporal_patterns:
            matches = re.finditer(pattern_info['pattern'], text_lower, re.IGNORECASE)
            for match in matches:
                temporal.append({
                    'type': pattern_info['type'],
                    'text': match.group(),
                    'position': (match.start(), match.end())
                })
        
        return temporal
    
    def _extract_anatomical_specifics(self, text: str) -> List[Dict[str, str]]:
        """Extract specific anatomical references"""
        anatomical = []
        text_lower = text.lower()
        
        for pattern_info in self.anatomical_patterns:
            matches = re.finditer(pattern_info['pattern'], text_lower, re.IGNORECASE)
            for match in matches:
                anatomical.append({
                    'type': pattern_info['type'],
                    'location': pattern_info['location'],
                    'text': match.group(),
                    'position': (match.start(), match.end())
                })
        
        return anatomical
    
    def _extract_critical_phrases(self, text: str) -> List[str]:
        """Extract phrases that must be preserved exactly"""
        critical_phrases = []
        
        # Look for quoted phrases (often critical)
        quoted_patterns = re.findall(r'"([^"]*)"', text)
        critical_phrases.extend(quoted_patterns)
        
        # Look for specific medical terminology patterns
        medical_phrase_patterns = [
            r'\b[A-Z][a-z]+\'?s\s+(?:syndrome|disease|sign|test|maneuver)\b',  # Eponymous terms
            r'\bfigure\s+of\s+\d+\b',  # Figure patterns
            r'\b\d+[-/]\d+\s+(?:rule|criteria|scale)\b',  # Medical scales
        ]
        
        for pattern in medical_phrase_patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            critical_phrases.extend(matches)
        
        return list(set(critical_phrases))  # Remove duplicates
    
    def _extract_investigation_findings(self, text: str) -> List[Dict[str, str]]:
        """Extract specific investigation findings"""
        findings = []
        
        # Common investigation patterns
        investigation_patterns = [
            {'pattern': r'\bMRI\s+shows?\s+([^.]+)', 'type': 'MRI'},
            {'pattern': r'\bCT\s+shows?\s+([^.]+)', 'type': 'CT'},
            {'pattern': r'\bEEG\s+shows?\s+([^.]+)', 'type': 'EEG'},
            {'pattern': r'\bCSF\s+shows?\s+([^.]+)', 'type': 'CSF'},
            {'pattern': r'\bLumbar\s+puncture\s+shows?\s+([^.]+)', 'type': 'LP'},
        ]
        
        for pattern_info in investigation_patterns:
            matches = re.finditer(pattern_info['pattern'], text, re.IGNORECASE)
            for match in matches:
                findings.append({
                    'type': pattern_info['type'],
                    'finding': match.group(1).strip(),
                    'full_text': match.group()
                })
        
        return findings
    
    def _generate_preservation_requirements(self, text: str) -> List[str]:
        """Generate specific preservation requirements based on extracted details"""
        requirements = []
        
        # Extract all details
        details = {
            'lateralization': self._extract_lateralization(text),
            'specific_signs': self._extract_specific_signs(text),
            'clinical_context': self._extract_clinical_context(text),
            'temporal_context': self._extract_temporal_context(text),
            'anatomical_specifics': self._extract_anatomical_specifics(text),
            'critical_phrases': self._extract_critical_phrases(text),
            'investigation_findings': self._extract_investigation_findings(text)
        }
        
        # Generate specific requirements
        if details['lateralization']:
            laterality_terms = [item['text'] for item in details['lateralization']]
            requirements.append(f"PRESERVE EXACT LATERALIZATION: Must include specific terms: {', '.join(set(laterality_terms))}")
        
        if details['specific_signs']:
            sign_terms = [item['term'] for item in details['specific_signs']]
            requirements.append(f"PRESERVE SPECIFIC CLINICAL SIGNS: Must include exact terms: {', '.join(set(sign_terms))}")
        
        if details['clinical_context']:
            context_terms = [item['context'] for item in details['clinical_context']]
            requirements.append(f"PRESERVE CLINICAL CONTEXT: Must maintain context: {', '.join(set(context_terms))}")
        
        if details['temporal_context']:
            temporal_terms = [item['text'] for item in details['temporal_context']]
            requirements.append(f"PRESERVE TEMPORAL CONTEXT: Must include timing: {', '.join(set(temporal_terms))}")
        
        if details['anatomical_specifics']:
            anatomical_terms = [item['location'] for item in details['anatomical_specifics']]
            requirements.append(f"PRESERVE ANATOMICAL SPECIFICS: Must include: {', '.join(set(anatomical_terms))}")
        
        if details['critical_phrases']:
            requirements.append(f"PRESERVE CRITICAL PHRASES: Must include exactly: {', '.join(details['critical_phrases'])}")
        
        if details['investigation_findings']:
            finding_terms = [item['type'] for item in details['investigation_findings']]
            requirements.append(f"PRESERVE INVESTIGATION FINDINGS: Must include: {', '.join(set(finding_terms))}")
        
        return requirements


def generate_clinical_detail_preservation_prompt(mcq_text: str, correct_answer: str = "") -> str:
    """
    Generate preservation prompt based on extracted clinical details
    
    Args:
        mcq_text: Original MCQ question text
        correct_answer: Correct answer text
        
    Returns:
        Detailed preservation prompt
    """
    extractor = ClinicalDetailExtractor()
    details = extractor.extract_critical_details(mcq_text, correct_answer)
    
    preservation_prompt = """
CRITICAL CLINICAL DETAIL PRESERVATION REQUIREMENTS:

"""
    
    # Add specific preservation requirements
    if details['preservation_requirements']:
        preservation_prompt += "MANDATORY PRESERVATION REQUIREMENTS:\n"
        for req in details['preservation_requirements']:
            preservation_prompt += f"- {req}\n"
        preservation_prompt += "\n"
    
    # Add specific instructions based on extracted details
    if details['lateralization']:
        preservation_prompt += "LATERALIZATION REQUIREMENTS:\n"
        for lat in details['lateralization']:
            preservation_prompt += f"- Must preserve exact lateralization: '{lat['text']}' in context: '{lat['full_context']}'\n"
        preservation_prompt += "\n"
    
    if details['specific_signs']:
        preservation_prompt += "SPECIFIC CLINICAL SIGNS REQUIREMENTS:\n"
        for sign in details['specific_signs']:
            preservation_prompt += f"- Must include exact term: '{sign['term']}' (original: '{sign['text']}')\n"
        preservation_prompt += "\n"
    
    if details['clinical_context']:
        preservation_prompt += "CLINICAL CONTEXT REQUIREMENTS:\n"
        for context in details['clinical_context']:
            preservation_prompt += f"- Must maintain {context['type']} context: {context['context']}\n"
        preservation_prompt += "\n"
    
    if details['temporal_context']:
        preservation_prompt += "TEMPORAL CONTEXT REQUIREMENTS:\n"
        for temporal in details['temporal_context']:
            preservation_prompt += f"- Must preserve timing: '{temporal['text']}'\n"
        preservation_prompt += "\n"
    
    if details['anatomical_specifics']:
        preservation_prompt += "ANATOMICAL SPECIFICITY REQUIREMENTS:\n"
        for anat in details['anatomical_specifics']:
            preservation_prompt += f"- Must include specific location: '{anat['location']}'\n"
        preservation_prompt += "\n"
    
    if details['critical_phrases']:
        preservation_prompt += "CRITICAL PHRASES REQUIREMENTS:\n"
        for phrase in details['critical_phrases']:
            preservation_prompt += f"- Must include exact phrase: '{phrase}'\n"
        preservation_prompt += "\n"
    
    preservation_prompt += """
VALIDATION REQUIREMENTS:
- The generated case MUST be validated against these preservation requirements
- Any missing critical details will result in case rejection
- All specific medical terminology must be preserved exactly
- Lateralization information is critical and cannot be generalized
- Clinical context (trauma vs non-trauma, acute vs chronic) must be maintained

FAILURE TO PRESERVE THESE DETAILS WILL COMPROMISE EDUCATIONAL INTEGRITY.
"""
    
    return preservation_prompt


if __name__ == "__main__":
    # Example usage
    extractor = ClinicalDetailExtractor()
    
    # Test with the problematic MCQ
    test_mcq = "A patient presents with a figure of 4, fencing posture, and right side nose rubbing. Which localization is most likely?"
    
    details = extractor.extract_critical_details(test_mcq)
    preservation_prompt = generate_clinical_detail_preservation_prompt(test_mcq)
    
    print("Clinical Detail Extractor - Test Results")
    print("=" * 50)
    print(f"Test MCQ: {test_mcq}")
    print("\nExtracted Details:")
    for key, value in details.items():
        if value:
            print(f"{key}: {value}")
    
    print("\nGenerated Preservation Prompt:")
    print(preservation_prompt)