"""
Clinical Inference Engine
Adds medically accurate implied clinical details based on neurological anatomy and physiology

This module enhances clinical presentations by inferring logical medical details
that would be present but not explicitly stated in the original MCQ.
"""

import re
import logging
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass
class ClinicalInference:
    """Structure for a clinical inference"""
    trigger_pattern: str
    inferred_detail: str
    anatomical_basis: str
    confidence: float  # 0.0 to 1.0
    category: str


class ClinicalInferenceEngine:
    """
    Adds clinically accurate implied details to case presentations
    """
    
    def __init__(self):
        self.seizure_inferences = self._build_seizure_inferences()
        self.neurological_inferences = self._build_neurological_inferences()
        self.vascular_inferences = self._build_vascular_inferences()
        self.movement_inferences = self._build_movement_disorder_inferences()
        
    def enhance_clinical_presentation(self, clinical_text: str, mcq_text: str = "") -> str:
        """
        Enhance clinical presentation with medically accurate inferred details
        
        Args:
            clinical_text: Generated case clinical presentation
            mcq_text: Original MCQ text for context
            
        Returns:
            Enhanced clinical presentation with inferred details
        """
        enhanced_text = clinical_text
        added_inferences = []
        
        # Apply seizure-specific inferences
        enhanced_text, seizure_inferences = self._apply_seizure_inferences(enhanced_text, mcq_text)
        added_inferences.extend(seizure_inferences)
        
        # Apply neurological inferences
        enhanced_text, neuro_inferences = self._apply_neurological_inferences(enhanced_text, mcq_text)
        added_inferences.extend(neuro_inferences)
        
        # Apply vascular inferences
        enhanced_text, vascular_inferences = self._apply_vascular_inferences(enhanced_text, mcq_text)
        added_inferences.extend(vascular_inferences)
        
        # Apply movement disorder inferences
        enhanced_text, movement_inferences = self._apply_movement_inferences(enhanced_text, mcq_text)
        added_inferences.extend(movement_inferences)
        
        # Log inferences for debugging
        if added_inferences:
            logger.info(f"Added {len(added_inferences)} clinical inferences: {[inf.inferred_detail for inf in added_inferences]}")
        
        return enhanced_text
    
    def _build_seizure_inferences(self) -> List[ClinicalInference]:
        """Build seizure-specific clinical inferences"""
        return [
            # Fencing posture with lateralization
            ClinicalInference(
                trigger_pattern=r"(right.{0,20}nose.{0,20}rubbing|nose.{0,20}rubbing.{0,20}right)",
                inferred_detail="The left arm was noted to be extended in a fencing posture during the tonic phase",
                anatomical_basis="Right temporal lobe seizures cause contralateral (left) arm extension due to crossed motor pathways",
                confidence=0.9,
                category="seizure_semiology"
            ),
            ClinicalInference(
                trigger_pattern=r"(left.{0,20}nose.{0,20}rubbing|nose.{0,20}rubbing.{0,20}left)",
                inferred_detail="The right arm was noted to be extended in a fencing posture during the tonic phase",
                anatomical_basis="Left temporal lobe seizures cause contralateral (right) arm extension due to crossed motor pathways",
                confidence=0.9,
                category="seizure_semiology"
            ),
            
            # Figure of 4 with lateralization
            ClinicalInference(
                trigger_pattern=r"figure.{0,10}of.{0,10}4.{0,50}(right|left)",
                inferred_detail="The dystonic posturing was asymmetric, more prominent on the contralateral side",
                anatomical_basis="Figure of 4 sign indicates supplementary motor area involvement with contralateral predominance",
                confidence=0.85,
                category="seizure_semiology"
            ),
            
            # Automatisms with consciousness
            ClinicalInference(
                trigger_pattern=r"(automatisms|lip.{0,10}smacking|chewing.{0,10}movements|picking.{0,10}movements)",
                inferred_detail="During these episodes, the patient appeared confused and was unresponsive to verbal commands",
                anatomical_basis="Complex automatisms indicate impaired consciousness due to bilateral temporal involvement",
                confidence=0.8,
                category="seizure_consciousness"
            ),
            
            # Ictal speech arrest
            ClinicalInference(
                trigger_pattern=r"(speech.{0,10}arrest|unable.{0,10}to.{0,10}speak)",
                inferred_detail="The patient was unable to follow commands during the episode but could grunt or make sounds",
                anatomical_basis="Ictal speech arrest involves dominant hemisphere language areas while preserving vocalization centers",
                confidence=0.85,
                category="seizure_language"
            ),
            
            # Post-ictal state
            ClinicalInference(
                trigger_pattern=r"(seizure|episode|convulsion).{0,50}(brief|seconds|minutes)",
                inferred_detail="Following the episode, there was a brief period of confusion lasting 1-2 minutes before full recovery",
                anatomical_basis="Post-ictal confusion is expected after complex partial seizures due to temporary hippocampal dysfunction",
                confidence=0.75,
                category="seizure_recovery"
            ),
            
            # Examination findings for seizure management cases
            ClinicalInference(
                trigger_pattern=r"(seizure|epilep).{0,100}(management|medication|treatment)",
                inferred_detail="On examination, the patient is alert and oriented with normal vital signs. Neurological examination is unremarkable with normal mental status, cranial nerves, motor strength, reflexes, and coordination",
                anatomical_basis="Normal interictal neurological examination is typical after generalized seizures in patients without underlying structural abnormalities",
                confidence=0.9,
                category="examination_findings"
            ),
            
            # Specific examination for visual seizures/auras
            ClinicalInference(
                trigger_pattern=r"(visual.{0,20}hallucination|colorful|circular.{0,20}objects)",
                inferred_detail="On examination during interictal periods, the child is alert and cooperative with normal vital signs. Visual fields are intact, and neurological examination including fundoscopy is normal",
                anatomical_basis="Benign childhood epilepsy with occipital paroxysms typically has normal interictal examination",
                confidence=0.85,
                category="examination_findings"
            ),
            
            # Remove inappropriate post-ictal confusion for visual auras
            ClinicalInference(
                trigger_pattern=r"(visual.{0,20}hallucination|visual.{0,20}phenomena).{0,50}(no.{0,10}loss.{0,10}consciousness|alert|awake)",
                inferred_detail="",  # Empty inference to prevent post-ictal confusion
                anatomical_basis="Visual auras without loss of consciousness do not cause post-ictal confusion",
                confidence=0.95,
                category="seizure_exclusion"
            )
        ]
    
    def _build_neurological_inferences(self) -> List[ClinicalInference]:
        """Build general neurological inferences"""
        return [
            # Horner's syndrome
            ClinicalInference(
                trigger_pattern=r"(ptosis|miosis|anhidrosis)",
                inferred_detail="The pupillary asymmetry was more noticeable in dim lighting conditions",
                anatomical_basis="Horner's syndrome is more apparent in low light when normal pupil dilation is impaired",
                confidence=0.8,
                category="autonomic"
            ),
            
            # Hemiparesis patterns
            ClinicalInference(
                trigger_pattern=r"(right.{0,20}hemiparesis|left.{0,20}hemiparesis)",
                inferred_detail="The weakness followed an upper motor neuron pattern with increased tone and hyperreflexia",
                anatomical_basis="Central hemiparesis involves pyramidal tract damage causing spastic weakness pattern",
                confidence=0.9,
                category="motor"
            ),
            
            # Visual field defects
            ClinicalInference(
                trigger_pattern=r"(hemianopia|visual.{0,10}field.{0,10}defect)",
                inferred_detail="The patient was unaware of the visual deficit initially (anosognosia for hemianopia)",
                anatomical_basis="Posterior cerebral artery strokes often cause hemianopia with initial lack of awareness",
                confidence=0.7,
                category="visual"
            ),
            
            # Ataxia patterns
            ClinicalInference(
                trigger_pattern=r"(ataxia|coordination.{0,10}problems|dysmetria)",
                inferred_detail="Gait was wide-based with tendency to fall toward the side of the lesion",
                anatomical_basis="Cerebellar lesions cause ipsilateral ataxia with characteristic gait abnormalities",
                confidence=0.85,
                category="cerebellar"
            ),
            
            # General examination for management cases
            ClinicalInference(
                trigger_pattern=r"(management|treatment).{0,50}(approach|medication|therapy)",
                inferred_detail="Physical examination reveals stable vital signs and findings consistent with the presenting condition",
                anatomical_basis="Management decisions require complete clinical assessment including examination findings",
                confidence=0.8,
                category="examination_context"
            ),
            
            # Examination for localization cases
            ClinicalInference(
                trigger_pattern=r"localization.{0,50}(likely|most)",
                inferred_detail="Neurological examination demonstrates focal findings consistent with the suspected anatomical location",
                anatomical_basis="Localization questions require specific examination findings that correlate with neuroanatomy",
                confidence=0.85,
                category="localization_exam"
            )
        ]
    
    def _build_vascular_inferences(self) -> List[ClinicalInference]:
        """Build stroke and vascular inferences"""
        return [
            # Acute stroke timing
            ClinicalInference(
                trigger_pattern=r"(sudden.{0,10}onset|acute.{0,10}stroke)",
                inferred_detail="The symptoms reached maximum severity within minutes of onset",
                anatomical_basis="Vascular events typically have rapid onset due to immediate loss of blood supply",
                confidence=0.9,
                category="temporal"
            ),
            
            # Watershed infarcts
            ClinicalInference(
                trigger_pattern=r"(bilateral.{0,20}weakness|hypotension)",
                inferred_detail="Weakness was most prominent in the shoulders and hips (man-in-the-barrel syndrome)",
                anatomical_basis="Watershed infarcts affect border zones between vascular territories, sparing face and distal extremities",
                confidence=0.8,
                category="vascular_pattern"
            ),
            
            # Lacunar strokes
            ClinicalInference(
                trigger_pattern=r"(pure.{0,10}motor|pure.{0,10}sensory)",
                inferred_detail="No cortical signs such as aphasia, neglect, or visual field defects were present",
                anatomical_basis="Lacunar strokes affect subcortical structures, sparing cortical functions",
                confidence=0.85,
                category="stroke_pattern"
            )
        ]
    
    def _build_movement_disorder_inferences(self) -> List[ClinicalInference]:
        """Build movement disorder inferences"""
        return [
            # Parkinson's tremor
            ClinicalInference(
                trigger_pattern=r"(rest.{0,10}tremor|pill.{0,10}rolling)",
                inferred_detail="The tremor was asymmetric, more prominent on one side, and improved with voluntary movement",
                anatomical_basis="Parkinsonian tremor typically begins unilaterally due to asymmetric substantia nigra degeneration",
                confidence=0.9,
                category="movement"
            ),
            
            # Essential tremor
            ClinicalInference(
                trigger_pattern=r"(action.{0,10}tremor|postural.{0,10}tremor)",
                inferred_detail="The tremor was bilateral but asymmetric, and notably improved with alcohol consumption",
                anatomical_basis="Essential tremor involves cerebellar circuits and characteristically responds to alcohol",
                confidence=0.8,
                category="movement"
            ),
            
            # Dystonia
            ClinicalInference(
                trigger_pattern=r"(dystonia|dystonic.{0,10}posturing)",
                inferred_detail="The abnormal posturing was task-specific and could be temporarily relieved by sensory tricks",
                anatomical_basis="Dystonia involves basal ganglia circuits and shows characteristic sensory geste patterns",
                confidence=0.8,
                category="movement"
            )
        ]
    
    def _apply_seizure_inferences(self, text: str, mcq_text: str) -> Tuple[str, List[ClinicalInference]]:
        """Apply seizure-specific inferences with context awareness"""
        enhanced_text = text
        applied_inferences = []
        
        for inference in self.seizure_inferences:
            if re.search(inference.trigger_pattern, text.lower(), re.IGNORECASE):
                # Check if the inference is contextually appropriate
                if self._is_inference_contextually_appropriate(inference, text, mcq_text):
                    # Check if the inference is already present
                    if not self._inference_already_present(enhanced_text, inference.inferred_detail):
                        enhanced_text = self._add_inference_to_text(enhanced_text, inference)
                        applied_inferences.append(inference)
        
        return enhanced_text, applied_inferences
    
    def _apply_neurological_inferences(self, text: str, mcq_text: str) -> Tuple[str, List[ClinicalInference]]:
        """Apply general neurological inferences"""
        enhanced_text = text
        applied_inferences = []
        
        for inference in self.neurological_inferences:
            if re.search(inference.trigger_pattern, text.lower(), re.IGNORECASE):
                if not self._inference_already_present(enhanced_text, inference.inferred_detail):
                    enhanced_text = self._add_inference_to_text(enhanced_text, inference)
                    applied_inferences.append(inference)
        
        return enhanced_text, applied_inferences
    
    def _apply_vascular_inferences(self, text: str, mcq_text: str) -> Tuple[str, List[ClinicalInference]]:
        """Apply vascular inferences"""
        enhanced_text = text
        applied_inferences = []
        
        for inference in self.vascular_inferences:
            if re.search(inference.trigger_pattern, text.lower(), re.IGNORECASE):
                if not self._inference_already_present(enhanced_text, inference.inferred_detail):
                    enhanced_text = self._add_inference_to_text(enhanced_text, inference)
                    applied_inferences.append(inference)
        
        return enhanced_text, applied_inferences
    
    def _apply_movement_inferences(self, text: str, mcq_text: str) -> Tuple[str, List[ClinicalInference]]:
        """Apply movement disorder inferences"""
        enhanced_text = text
        applied_inferences = []
        
        for inference in self.movement_inferences:
            if re.search(inference.trigger_pattern, text.lower(), re.IGNORECASE):
                if not self._inference_already_present(enhanced_text, inference.inferred_detail):
                    enhanced_text = self._add_inference_to_text(enhanced_text, inference)
                    applied_inferences.append(inference)
        
        return enhanced_text, applied_inferences
    
    def _inference_already_present(self, text: str, inference_detail: str) -> bool:
        """Check if the inference is already present in the text"""
        # Extract key phrases from the inference
        key_phrases = self._extract_key_phrases(inference_detail)
        
        for phrase in key_phrases:
            if phrase.lower() in text.lower():
                return True
        
        return False
    
    def _extract_key_phrases(self, inference_detail: str) -> List[str]:
        """Extract key phrases from inference detail for checking"""
        # Remove common words and extract meaningful phrases
        stop_words = {'the', 'was', 'were', 'is', 'are', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'during', 'noted', 'observed'}
        
        words = inference_detail.lower().split()
        key_phrases = []
        
        # Look for medical terms (longer than 3 characters, not stop words)
        current_phrase = []
        for word in words:
            clean_word = re.sub(r'[^\w]', '', word)
            if len(clean_word) > 3 and clean_word not in stop_words:
                current_phrase.append(clean_word)
            else:
                if len(current_phrase) >= 2:
                    key_phrases.append(' '.join(current_phrase))
                current_phrase = []
        
        # Add final phrase if exists
        if len(current_phrase) >= 2:
            key_phrases.append(' '.join(current_phrase))
        
        return key_phrases
    
    def _is_inference_contextually_appropriate(self, inference: ClinicalInference, text: str, mcq_text: str) -> bool:
        """Check if an inference is contextually appropriate for the specific case"""
        
        combined_text = (text + " " + mcq_text).lower()
        
        # Enhanced context awareness for post-ictal confusion
        if "post-ictal confusion" in inference.inferred_detail.lower():
            # Don't add post-ictal confusion for:
            # 1. Visual auras/simple partial seizures (occipital seizures)
            # 2. Cases explicitly mentioning "no loss of consciousness"
            # 3. Brief visual phenomena without complex seizure activity
            # 4. Benign childhood epilepsy with occipital paroxysms
            
            # Visual aura/simple partial seizure indicators
            visual_aura_indicators = [
                'visual hallucination', 'colorful', 'circular objects', 'moving circles',
                'visual field', 'visual phenomena', 'sees colors', 'perceives',
                'occipital', 'benign childhood epilepsy', 'occipital paroxysms',
                'visual aura', 'simple partial', 'focal seizure'
            ]
            
            # No consciousness impairment indicators
            no_consciousness_indicators = [
                'no loss of consciousness', 'alert', 'awake', 'conscious',
                'no impairment of consciousness', 'remains conscious',
                'fully aware', 'alert during episode', 'responsive during'
            ]
            
            # Age-specific considerations (children with visual seizures often have benign forms)
            age_considerations = [
                '7-year-old', '8-year-old', '9-year-old', '10-year-old',
                'child', 'childhood', 'pediatric', 'boy', 'girl'
            ]
            
            # Check for visual auras without consciousness impairment
            has_visual_indicators = any(indicator in combined_text for indicator in visual_aura_indicators)
            has_no_consciousness_loss = any(indicator in combined_text for indicator in no_consciousness_indicators)
            is_child_case = any(indicator in combined_text for indicator in age_considerations)
            
            # If visual aura with no consciousness loss, skip post-ictal confusion
            if has_visual_indicators and has_no_consciousness_loss:
                return False
            
            # If child with visual phenomena (often benign), be very conservative
            if is_child_case and has_visual_indicators and 'visual hallucination' in combined_text:
                return False
            
            # If described as brief visual phenomena, likely simple partial
            if 'visual' in combined_text and ('brief' in combined_text or 'short' in combined_text):
                return False
            
            # If occipital lobe involvement mentioned, be cautious about post-ictal confusion
            if 'occipital' in combined_text and 'visual' in combined_text:
                return False
        
        # Enhanced examination findings context
        if inference.category == "examination_findings":
            # Only add seizure-specific examination if it's actually a seizure case
            if "seizure" not in combined_text and "epilep" not in combined_text:
                return False
            
            # For visual seizure examination, ensure it's appropriate
            if "visual" in inference.inferred_detail.lower():
                if not any(indicator in combined_text for indicator in ['visual', 'hallucination', 'occipital']):
                    return False
        
        # Age-specific inference validation
        if inference.category == "seizure_recovery":
            # Be more conservative with recovery inferences in children
            if any(age_term in combined_text for age_term in ['child', 'boy', 'girl', '7-year-old', '8-year-old']):
                if 'visual' in combined_text:
                    # Visual seizures in children often don't have significant post-ictal periods
                    return False
        
        # Clinical context validation
        if inference.category == "seizure_consciousness":
            # Don't add consciousness-related inferences if visual auras are mentioned
            if 'visual hallucination' in combined_text and 'consciousness' in inference.inferred_detail.lower():
                return False
        
        return True
    
    def _add_inference_to_text(self, text: str, inference: ClinicalInference) -> str:
        """Add the inference to the clinical text in a natural way"""
        # Find a good insertion point (end of a sentence)
        sentences = text.split('. ')
        
        # Insert the inference as a new sentence
        if len(sentences) > 1:
            # Insert before the last sentence
            sentences.insert(-1, inference.inferred_detail.rstrip('.'))
            return '. '.join(sentences)
        else:
            # Append to the end
            return f"{text.rstrip('.')}. {inference.inferred_detail}"
    
    def get_inference_metadata(self, clinical_text: str) -> Dict[str, any]:
        """Get metadata about applied inferences for debugging"""
        metadata = {
            'total_inferences': 0,
            'categories': {},
            'confidence_scores': [],
            'anatomical_bases': []
        }
        
        all_inferences = (self.seizure_inferences + self.neurological_inferences + 
                         self.vascular_inferences + self.movement_inferences)
        
        for inference in all_inferences:
            if re.search(inference.trigger_pattern, clinical_text.lower(), re.IGNORECASE):
                metadata['total_inferences'] += 1
                metadata['categories'][inference.category] = metadata['categories'].get(inference.category, 0) + 1
                metadata['confidence_scores'].append(inference.confidence)
                metadata['anatomical_bases'].append(inference.anatomical_basis)
        
        if metadata['confidence_scores']:
            metadata['average_confidence'] = sum(metadata['confidence_scores']) / len(metadata['confidence_scores'])
        else:
            metadata['average_confidence'] = 0.0
        
        return metadata


def enhance_case_with_clinical_inferences(clinical_presentation: str, mcq_text: str = "") -> str:
    """
    Public function to enhance clinical presentation with inferred details
    
    Args:
        clinical_presentation: Original case clinical presentation
        mcq_text: Original MCQ text for context
        
    Returns:
        Enhanced clinical presentation with medically accurate inferred details
    """
    try:
        inference_engine = ClinicalInferenceEngine()
        enhanced_presentation = inference_engine.enhance_clinical_presentation(clinical_presentation, mcq_text)
        
        # Log the enhancement for debugging
        metadata = inference_engine.get_inference_metadata(enhanced_presentation)
        if metadata['total_inferences'] > 0:
            logger.info(f"Enhanced clinical presentation with {metadata['total_inferences']} inferences (avg confidence: {metadata['average_confidence']:.2f})")
        
        return enhanced_presentation
        
    except Exception as e:
        logger.error(f"Error in clinical inference enhancement: {e}")
        # Return original text if enhancement fails
        return clinical_presentation


if __name__ == "__main__":
    # Test the inference engine
    test_text = "A patient presents with a figure of 4, fencing posture, and right side nose rubbing during brief episodes."
    
    engine = ClinicalInferenceEngine()
    enhanced = engine.enhance_clinical_presentation(test_text)
    
    print("Original:", test_text)
    print("\nEnhanced:", enhanced)
    
    metadata = engine.get_inference_metadata(enhanced)
    print(f"\nInferences added: {metadata['total_inferences']}")
    print(f"Categories: {metadata['categories']}")
    print(f"Average confidence: {metadata['average_confidence']:.2f}")