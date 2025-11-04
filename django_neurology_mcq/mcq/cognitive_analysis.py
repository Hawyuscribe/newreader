"""
Cognitive Analysis Engine for ReasoningPal
Analyzes user reasoning patterns and identifies cognitive errors and misconceptions.
"""

import json
import logging
import re
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from enum import Enum

logger = logging.getLogger(__name__)

class CognitiveErrorType(Enum):
    """Types of cognitive errors in medical reasoning"""
    ANCHORING_BIAS = "anchoring_bias"
    CONFIRMATION_BIAS = "confirmation_bias"
    AVAILABILITY_HEURISTIC = "availability_heuristic"
    REPRESENTATIVENESS_HEURISTIC = "representativeness_heuristic"
    PREMATURE_CLOSURE = "premature_closure"
    COMMISSION_BIAS = "commission_bias"
    OMISSION_BIAS = "omission_bias"
    OVERCONFIDENCE_BIAS = "overconfidence_bias"
    SEARCH_SATISFICING = "search_satisficing"
    DIAGNOSTIC_MOMENTUM = "diagnostic_momentum"
    FUNDAMENTAL_ATTRIBUTION_ERROR = "fundamental_attribution_error"
    SUNK_COST_FALLACY = "sunk_cost_fallacy"
    
    # Knowledge-based errors
    KNOWLEDGE_GAP = "knowledge_gap"
    MISCONCEPTION = "misconception"
    INCOMPLETE_UNDERSTANDING = "incomplete_understanding"
    WRONG_ASSOCIATION = "wrong_association"

@dataclass
class CognitiveAnalysis:
    """Results of cognitive analysis"""
    primary_error: Optional[CognitiveErrorType]
    secondary_errors: List[CognitiveErrorType]
    knowledge_gaps: List[str]
    misconceptions: List[str]
    reasoning_quality: str  # 'poor', 'fair', 'good', 'excellent'
    confidence_level: float  # 0.0 to 1.0
    analysis_summary: str

@dataclass
class GuideStep:
    """Individual step in the reasoning guidance"""
    title: str
    content: str
    question: Optional[str] = None
    evidence: Optional[str] = None
    action: Optional[str] = None

class CognitiveAnalyzer:
    """Analyzes user reasoning and identifies cognitive patterns"""
    
    def __init__(self):
        self.error_patterns = self._load_error_patterns()
        self.knowledge_keywords = self._load_knowledge_keywords()
    
    def analyze_reasoning(self, mcq, user_answer: str, user_reasoning: str, is_correct: bool) -> CognitiveAnalysis:
        """
        Comprehensive analysis of user's clinical reasoning against MCQ context
        
        Args:
            mcq: MCQ object with question, options, correct answer, explanation
            user_answer: User's selected answer (A, B, C, D)
            user_reasoning: User's explanation of their reasoning
            is_correct: Whether the answer was correct
            
        Returns:
            CognitiveAnalysis object with detailed medical education analysis
        """
        try:
            logger.info(f"Deep analysis for MCQ {mcq.id}: {user_answer} ({'correct' if is_correct else 'incorrect'})")
            
            # Comprehensive contextual analysis
            try:
                detailed_analysis = self._generate_comprehensive_analysis(mcq, user_answer, user_reasoning, is_correct)
            except Exception as e:
                logger.error(f"Error in _generate_comprehensive_analysis: {e}", exc_info=True)
                # Create a basic analysis even if the comprehensive one fails
                detailed_analysis = self._create_basic_analysis(mcq, user_answer, user_reasoning, is_correct)
            
            # Analyze reasoning patterns with error handling
            try:
                detected_errors = self._detect_cognitive_errors(user_reasoning, mcq, user_answer, is_correct)
            except Exception as e:
                logger.error(f"Error in _detect_cognitive_errors: {e}")
                detected_errors = []
                
            try:
                knowledge_gaps = self._identify_comprehensive_knowledge_gaps(user_reasoning, mcq, is_correct)
            except Exception as e:
                logger.error(f"Error in _identify_comprehensive_knowledge_gaps: {e}")
                knowledge_gaps = []
                
            try:
                misconceptions = self._identify_detailed_misconceptions(user_reasoning, mcq, user_answer, is_correct)
            except Exception as e:
                logger.error(f"Error in _identify_detailed_misconceptions: {e}")
                misconceptions = []
                
            try:
                reasoning_quality = self._assess_detailed_reasoning_quality(user_reasoning, mcq, is_correct)
            except Exception as e:
                logger.error(f"Error in _assess_detailed_reasoning_quality: {e}")
                reasoning_quality = "fair"
                
            try:
                confidence = self._calculate_confidence(user_reasoning, detected_errors)
            except Exception as e:
                logger.error(f"Error in _calculate_confidence: {e}")
                confidence = 0.5
            
            return CognitiveAnalysis(
                primary_error=detected_errors[0] if detected_errors else None,
                secondary_errors=detected_errors[1:],
                knowledge_gaps=knowledge_gaps,
                misconceptions=misconceptions,
                reasoning_quality=reasoning_quality,
                confidence_level=confidence,
                analysis_summary=detailed_analysis
            )
            
        except Exception as e:
            logger.error(f"Critical error in analyze_reasoning: {e}", exc_info=True)
            # Try to generate a meaningful analysis even with errors
            try:
                basic_analysis = f"""<div class="clinical-reasoning-analysis">
<h3>Clinical Reasoning Analysis</h3>
<p>You selected <strong>{user_answer}</strong> for this question about {mcq.question[:100]}...</p>
<p>{"Your answer was correct." if is_correct else f"The correct answer was {mcq.correct_answer}."} Clinical reasoning analysis helps identify patterns in decision-making to improve diagnostic accuracy.</p>
<p>Continue practicing with similar questions to strengthen your clinical pattern recognition and decision-making skills.</p>
</div>"""
            except:
                basic_analysis = "<p>Analysis completed. Your reasoning has been noted for review.</p>"
                
            return CognitiveAnalysis(
                primary_error=None,
                secondary_errors=[],
                knowledge_gaps=[],
                misconceptions=[],
                reasoning_quality="fair",
                confidence_level=0.7 if is_correct else 0.4,
                analysis_summary=basic_analysis
            )
    
    def _detect_cognitive_errors(self, reasoning: str, mcq, user_answer: str, is_correct: bool) -> List[CognitiveErrorType]:
        """Detect cognitive biases and errors in reasoning"""
        errors = []
        reasoning_lower = reasoning.lower()
        
        # Anchoring bias - fixation on initial information
        anchoring_keywords = ['first', 'initially', 'immediately thought', 'obvious', 'clearly']
        if any(keyword in reasoning_lower for keyword in anchoring_keywords) and not is_correct:
            errors.append(CognitiveErrorType.ANCHORING_BIAS)
        
        # Confirmation bias - seeking confirming evidence
        confirmation_keywords = ['confirms', 'supports my', 'proves', 'obviously']
        if any(keyword in reasoning_lower for keyword in confirmation_keywords):
            errors.append(CognitiveErrorType.CONFIRMATION_BIAS)
        
        # Availability heuristic - recent/memorable cases
        availability_keywords = ['remember', 'seen before', 'common', 'usually', 'most cases']
        if any(keyword in reasoning_lower for keyword in availability_keywords):
            errors.append(CognitiveErrorType.AVAILABILITY_HEURISTIC)
        
        # Premature closure - stopping search too early
        closure_keywords = ['enough', 'sufficient', 'done', 'complete picture']
        if any(keyword in reasoning_lower for keyword in closure_keywords) and not is_correct:
            errors.append(CognitiveErrorType.PREMATURE_CLOSURE)
        
        # Overconfidence - excessive certainty
        confidence_keywords = ['definitely', 'certainly', 'no doubt', 'absolutely', 'sure']
        if any(keyword in reasoning_lower for keyword in confidence_keywords) and not is_correct:
            errors.append(CognitiveErrorType.OVERCONFIDENCE_BIAS)
        
        return errors
    
    def _identify_knowledge_gaps(self, reasoning: str, mcq) -> List[str]:
        """Identify specific knowledge gaps"""
        gaps = []
        reasoning_lower = reasoning.lower()
        
        # Identify uncertainty markers
        uncertainty_keywords = ["don't know", "not sure", "unclear", "confused", "don't understand"]
        if any(keyword in reasoning_lower for keyword in uncertainty_keywords):
            gaps.append("Expressed uncertainty about core concepts")
        
        # Check for missing subspecialty knowledge
        subspecialty = getattr(mcq, 'subspecialty', '')
        if subspecialty and len(reasoning) < 100:
            gaps.append(f"Limited reasoning depth for {subspecialty} topic")
        
        # Check for missing pathophysiology understanding
        if 'mechanism' not in reasoning_lower and 'pathway' not in reasoning_lower:
            gaps.append("Missing pathophysiological understanding")
        
        return gaps
    
    def _identify_misconceptions(self, reasoning: str, mcq, user_answer: str) -> List[str]:
        """Identify specific misconceptions in reasoning"""
        misconceptions = []
        
        # Analyze reasoning for common medical misconceptions
        reasoning_lower = reasoning.lower()
        
        # Common neurology misconceptions
        if 'stroke' in reasoning_lower and 'hemorrhagic' in reasoning_lower and 'anticoagulation' in reasoning_lower:
            misconceptions.append("Misconception about anticoagulation in hemorrhagic stroke")
        
        if 'seizure' in reasoning_lower and 'tongue' in reasoning_lower:
            misconceptions.append("Misconception about tongue biting as diagnostic for seizures")
        
        return misconceptions
    
    def _assess_reasoning_quality(self, reasoning: str, is_correct: bool) -> str:
        """Assess overall quality of reasoning"""
        length = len(reasoning)
        word_count = len(reasoning.split())
        
        # Basic length assessment
        if length < 50:
            return 'poor'
        elif length < 150:
            quality = 'fair'
        elif length < 300:
            quality = 'good'
        else:
            quality = 'excellent'
        
        # Adjust based on correctness
        if not is_correct and quality in ['good', 'excellent']:
            quality = 'fair'
        
        return quality
    
    def _calculate_confidence(self, reasoning: str, errors: List[CognitiveErrorType]) -> float:
        """Calculate confidence in the analysis"""
        base_confidence = 0.7
        
        # Increase confidence with longer reasoning
        length_bonus = min(0.2, len(reasoning) / 1000)
        
        # Decrease confidence with more errors
        error_penalty = len(errors) * 0.1
        
        return max(0.1, min(1.0, base_confidence + length_bonus - error_penalty))
    
    def _generate_analysis_summary(self, errors: List[CognitiveErrorType], gaps: List[str], 
                                 misconceptions: List[str], is_correct: bool) -> str:
        """Generate a summary of the cognitive analysis"""
        if is_correct and not errors:
            return "Excellent reasoning with sound clinical logic and appropriate evidence-based thinking."
        
        summary_parts = []
        
        if errors:
            error_names = [error.value.replace('_', ' ').title() for error in errors[:2]]
            summary_parts.append(f"Identified cognitive patterns: {', '.join(error_names)}")
        
        if gaps:
            summary_parts.append(f"Knowledge gaps in {len(gaps)} areas")
        
        if misconceptions:
            summary_parts.append(f"Found {len(misconceptions)} potential misconceptions")
        
        if not summary_parts:
            return "No significant cognitive errors detected, but answer was incorrect. May indicate knowledge gap or misapplication."
        
        return ". ".join(summary_parts) + "."
    
    def _load_error_patterns(self) -> Dict:
        """Load cognitive error detection patterns"""
        return {
            "anchoring": ["first thought", "initial impression", "obvious", "immediately"],
            "confirmation": ["supports", "confirms", "proves", "shows that"],
            "availability": ["remember", "seen", "common", "usual", "typical"]
        }
    
    def _load_knowledge_keywords(self) -> Dict:
        """Load subspecialty-specific knowledge keywords"""
        return {
            "epilepsy": ["seizure", "anticonvulsant", "eeg", "ictal", "postictal"],
            "stroke": ["ischemic", "hemorrhagic", "tpa", "thrombectomy", "nihss"],
            "movement_disorders": ["parkinson", "dystonia", "tremor", "bradykinesia"]
        }
    
    def _create_basic_analysis(self, mcq, user_answer: str, user_reasoning: str, is_correct: bool) -> str:
        """Create a basic analysis when comprehensive analysis fails"""
        try:
            correct_answer = mcq.correct_answer
            question_snippet = mcq.question[:100] + "..." if len(mcq.question) > 100 else mcq.question
            
            if is_correct:
                return f"""<div class="clinical-reasoning-analysis">
<h3>Clinical Reasoning Analysis</h3>
<p><strong>Well done!</strong> You correctly identified <strong>{user_answer}</strong> as the answer.</p>
<p>Your reasoning: "{user_reasoning[:200]}..." shows clinical thinking.</p>
<p>Continue practicing to strengthen your pattern recognition and clinical decision-making skills.</p>
</div>"""
            else:
                return f"""<div class="clinical-reasoning-analysis">
<h3>Clinical Reasoning Analysis</h3>
<p>You selected <strong>{user_answer}</strong>, but the correct answer was <strong>{correct_answer}</strong>.</p>
<p>Question context: {question_snippet}</p>
<p>Your reasoning shows thoughtful consideration. Review the explanation to understand the key distinguishing features that point to the correct answer.</p>
<p>Clinical reasoning improves with practice. Focus on identifying the specific clinical features that differentiate similar conditions.</p>
</div>"""
        except Exception as e:
            logger.error(f"Error in _create_basic_analysis: {e}")
            return "<p>Analysis completed. Your reasoning has been noted for review.</p>"
    
    def _convert_markdown_to_html(self, text: str) -> str:
        """Convert markdown-style formatting to clean HTML"""
        import re
        
        # Convert bold markdown to HTML
        text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
        text = re.sub(r'__([^_]+)__', r'<strong>\1</strong>', text)
        
        # Convert italic markdown to HTML
        text = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', text)
        text = re.sub(r'_([^_]+)_', r'<em>\1</em>', text)
        
        # Convert bullet points
        text = re.sub(r'^\* ', r'• ', text, flags=re.MULTILINE)
        text = re.sub(r'^\- ', r'• ', text, flags=re.MULTILINE)
        
        # Clean up any remaining markdown artifacts
        text = re.sub(r'#{1,6}\s*', '', text)  # Remove headers
        
        return text
    
    def _generate_comprehensive_analysis(self, mcq, user_answer: str, user_reasoning: str, is_correct: bool) -> str:
        """
        Generate professional clinical reasoning analysis in paragraph format
        """
        try:
            # Get option texts
            correct_option = self._get_option_text(mcq, mcq.correct_answer)
            user_option = self._get_option_text(mcq, user_answer)
            
            analysis = []
            
            # Professional header
            analysis.append('<div class="clinical-reasoning-analysis">')
            analysis.append('<h3>Clinical Reasoning Analysis</h3>')
            
            if is_correct:
                correct_analysis = self._generate_correct_analysis(mcq, user_answer, user_reasoning, correct_option)
                analysis.append(correct_analysis)
            else:
                incorrect_analysis = self._generate_incorrect_analysis(mcq, user_answer, user_reasoning, correct_option, user_option)
                analysis.append(incorrect_analysis)
            
            analysis.append('</div>')
            
            return "\n".join(analysis)
        except Exception as e:
            logger.error(f"Error in _generate_comprehensive_analysis: {e}", exc_info=True)
            # Return basic analysis if comprehensive fails
            return self._create_basic_analysis(mcq, user_answer, user_reasoning, is_correct)
    
    def _generate_correct_analysis(self, mcq, user_answer: str, user_reasoning: str, correct_option: str) -> str:
        """Generate professional analysis for correct answers"""
        try:
            analysis = []
            
            analysis.append(f'<p><strong>Excellent clinical reasoning!</strong> You correctly identified <strong>{user_answer}: {correct_option}</strong> as the answer.</p>')
            
            # Analyze their reasoning quality
            try:
                reasoning_quality = self._assess_reasoning_depth(user_reasoning)
            except:
                reasoning_quality = "moderate"
            
            if reasoning_quality == "detailed":
                analysis.append('<p>Your reasoning demonstrates strong clinical thinking with clear connections between clinical features and underlying pathophysiology. You systematically considered the key diagnostic criteria and properly weighted the clinical evidence.</p>')
            elif reasoning_quality == "moderate":
                analysis.append('<p>Your reasoning shows good clinical intuition, though it could benefit from more systematic analysis of the distinguishing features. Consider exploring the pathophysiological mechanisms that support your diagnosis.</p>')
            else:
                analysis.append('<p>While you arrived at the correct answer, developing more detailed reasoning will strengthen your clinical decision-making. Focus on identifying specific clinical features that distinguish this condition from similar presentations.</p>')
            
            # Add clinical pearls based on the question topic
            try:
                clinical_pearl = self._get_focused_clinical_pearl(mcq, correct_option)
                if clinical_pearl:
                    analysis.append(f'<p><strong>Clinical Pearl:</strong> {clinical_pearl}</p>')
            except Exception as e:
                logger.debug(f"Could not generate clinical pearl: {e}")
            
            return "\n".join(analysis)
        except Exception as e:
            logger.error(f"Error in _generate_correct_analysis: {e}")
            return f'<p>You correctly identified <strong>{user_answer}</strong> as the answer. Well done!</p>'
    
    def _generate_incorrect_analysis(self, mcq, user_answer: str, user_reasoning: str, correct_option: str, user_option: str) -> str:
        """Generate professional analysis for incorrect answers"""
        try:
            analysis = []
            
            analysis.append(f'<p>You selected <strong>{user_answer}: {user_option}</strong>, but the correct answer is <strong>{mcq.correct_answer}: {correct_option}</strong>. Let\'s explore the clinical reasoning behind this distinction.</p>')
            
            # Analyze why their choice seemed reasonable based on their reasoning
            if user_reasoning:
                analysis.append(f'<p>Your reasoning ("{user_reasoning}") shows clinical thinking. Let me help clarify the neuroanatomical and pathophysiological distinctions.</p>')
            else:
                analysis.append(f'<p>Let\'s examine the neurological basis for distinguishing between these options.</p>')
            
            # Explain the key distinguishing features
            try:
                distinguishing_features = self._get_key_distinguishing_features(mcq, correct_option, user_option)
                if distinguishing_features:
                    analysis.append(f'<p><strong>Key Distinction:</strong> {distinguishing_features}.</p>')
            except Exception as e:
                logger.debug(f"Could not generate distinguishing features: {e}")
            
            # Evidence-based reasoning
            try:
                if hasattr(mcq, 'explanation') and mcq.explanation:
                    # Extract the most important clinical evidence
                    key_evidence = self._extract_key_evidence(mcq.explanation)
                    if key_evidence:
                        analysis.append(f'<p><strong>Clinical Evidence:</strong> {key_evidence}</p>')
            except Exception as e:
                logger.debug(f"Could not extract key evidence: {e}")
            
            # Practical learning point based on the specific error
            try:
                learning_point = self._generate_specific_learning_point(mcq, correct_option, user_option, user_reasoning)
                analysis.append(f'<p><strong>Learning Point:</strong> {learning_point}</p>')
            except:
                analysis.append(f'<p><strong>Remember:</strong> Always consider the anatomical distribution and temporal evolution when evaluating neurological presentations.</p>')
            
            return "\n".join(analysis)
        except Exception as e:
            logger.error(f"Error in _generate_incorrect_analysis: {e}")
            return f'<p>You selected <strong>{user_answer}</strong>, but the correct answer was <strong>{mcq.correct_answer}</strong>. Review the explanation to understand the key distinguishing features.</p>'
        
    def _assess_reasoning_depth(self, reasoning: str) -> str:
        """Assess the depth of user's reasoning"""
        reasoning_lower = reasoning.lower()
        
        # Count indicators of detailed reasoning
        detailed_indicators = sum(1 for indicator in [
            'because', 'due to', 'pathophysiology', 'mechanism', 'differential',
            'distinguish', 'characteristic', 'specific', 'evidence', 'study'
        ] if indicator in reasoning_lower)
        
        if detailed_indicators >= 3 and len(reasoning.split()) > 20:
            return "detailed"
        elif detailed_indicators >= 1 and len(reasoning.split()) > 10:
            return "moderate"
        else:
            return "basic"
    
    def _get_focused_clinical_pearl(self, mcq, correct_option: str) -> str:
        """Get a focused clinical pearl based on the question content"""
        # Extract key medical terms from the question and answer
        question_lower = mcq.question_text.lower()
        option_lower = correct_option.lower()
        
        # Neurology-specific pearls
        if 'huntington' in option_lower:
            return "Huntington's disease shows autosomal dominant inheritance with anticipation - earlier onset and more severe symptoms in successive generations, particularly with paternal transmission."
        elif 'parkinson' in option_lower:
            return "The cardinal features of Parkinson's disease include bradykinesia (required), plus at least one of: rest tremor, rigidity, or postural instability."
        elif 'multiple sclerosis' in option_lower or 'demyelinating' in option_lower:
            return "McDonald criteria require dissemination in space and time, which can be demonstrated through clinical episodes or MRI findings."
        elif 'stroke' in question_lower or 'cerebral' in option_lower:
            return "Time is brain - each minute of untreated stroke results in loss of 1.9 million neurons and 14 billion synapses."
        elif 'seizure' in question_lower or 'epilepsy' in option_lower:
            return "A single unprovoked seizure has a 40-50% recurrence risk, while two unprovoked seizures have an 80-90% risk of further seizures."
        
        return ""
    
    def _get_key_distinguishing_features(self, mcq, correct_option: str, user_option: str) -> str:
        """Extract key distinguishing features between correct and user's choice"""
        try:
            # Extract the actual question to understand the clinical context
            question = getattr(mcq, 'question', '')
            question_lower = question.lower()
            
            # Try to extract features from the MCQ explanation if available
            if hasattr(mcq, 'explanation') and mcq.explanation:
                explanation_text = str(mcq.explanation).lower()
                
                # Look for distinguishing features in the explanation
                feature_keywords = ['because', 'due to', 'characterized by', 'presents with', 
                                  'typical', 'pathognomonic', 'specific for', 'diagnostic of',
                                  'differentiates', 'distinguishes', 'unlike', 'whereas']
                
                for sentence in str(mcq.explanation).split('.'):
                    if any(keyword in sentence.lower() for keyword in feature_keywords):
                        # Clean up the sentence and return it
                        sentence = sentence.strip()
                        if len(sentence) > 20 and len(sentence) < 200:
                            return sentence
            
            # If no explanation or features found, provide specific neurological analysis based on options
            if 'upper trunk' in correct_option.lower() and 'lower trunk' in user_option.lower():
                return "Upper trunk lesions (C5-C6) cause weakness in shoulder abduction, elbow flexion, and forearm supination with preserved hand intrinsic muscles, while lower trunk lesions (C8-T1) primarily affect hand intrinsics with preserved proximal strength"
            elif 'stroke' in question_lower or 'infarct' in question_lower:
                return "vascular territory distribution, sudden onset, and presence of cortical signs (aphasia, neglect, or visual field defects)"
            elif 'seizure' in question_lower or 'epilepsy' in question_lower:
                return "semiology progression, post-ictal features, and EEG findings specific to the seizure type"
            elif 'parkinson' in question_lower or 'movement' in question_lower:
                return "asymmetric onset, response to levodopa, and presence of non-motor symptoms"
            elif 'dementia' in question_lower or 'cognitive' in question_lower:
                return "pattern of cognitive domain involvement, progression rate, and associated neurological signs"
            elif 'neuropathy' in question_lower or 'peripheral' in question_lower:
                return "distribution pattern (length-dependent vs non-length-dependent), sensory vs motor predominance, and presence of autonomic features"
            elif 'headache' in question_lower or 'migraine' in question_lower:
                return "temporal pattern, associated features, and red flag symptoms"
            else:
                # Generic but still more specific than before
                return "anatomical localization, temporal evolution, and associated neurological findings specific to this condition"
                
        except Exception as e:
            logger.debug(f"Could not extract distinguishing features: {e}")
            return "specific neurological findings and clinical progression pattern"
    
    def _generate_specific_learning_point(self, mcq, correct_option: str, user_option: str, user_reasoning: str) -> str:
        """Generate a specific learning point based on the error made"""
        try:
            question = getattr(mcq, 'question', '').lower()
            
            # Brachial plexus specific
            if 'upper trunk' in correct_option.lower() and 'lower trunk' in user_option.lower():
                return "When evaluating brachial plexus injuries, remember that upper trunk lesions affect C5-C6 (shoulder/elbow), while lower trunk lesions affect C8-T1 (hand). The presence of both proximal and distal weakness suggests upper trunk involvement"
            
            # Stroke/vascular specific
            elif 'stroke' in question or 'infarct' in question:
                return "In vascular neurology, localization depends on arterial territories. Cortical signs (aphasia, neglect) indicate anterior circulation, while crossed findings suggest brainstem involvement"
            
            # Movement disorders
            elif 'parkinson' in question or 'tremor' in question:
                return "For movement disorders, pay attention to tremor characteristics: rest tremor suggests Parkinsonism, action tremor points to essential tremor, and intention tremor indicates cerebellar pathology"
            
            # Seizure/epilepsy
            elif 'seizure' in question or 'epilepsy' in question:
                return "Seizure semiology provides localization: focal motor suggests frontal lobe, déjà vu/fear suggests temporal lobe, and visual phenomena suggest occipital lobe origin"
            
            # Neuropathy
            elif 'neuropathy' in question or 'weakness' in question:
                return "For peripheral neuropathies, distribution is key: length-dependent pattern suggests metabolic/toxic causes, while non-length-dependent patterns suggest inflammatory or infiltrative etiologies"
            
            # Default neurological principle
            else:
                return "In neurology, accurate localization is essential. Consider: Where is the lesion? (central vs peripheral), What is the lesion? (vascular, inflammatory, neoplastic), and timing (acute, subacute, chronic)"
                
        except Exception as e:
            logger.debug(f"Could not generate specific learning point: {e}")
            return "Focus on anatomical localization and temporal evolution to narrow your differential diagnosis"
    
    def _extract_key_evidence(self, explanation: str) -> str:
        """Extract the most important clinical evidence from explanation"""
        # Remove excessive formatting and extract key clinical points
        explanation = re.sub(r'[#*]+', '', explanation)  # Remove markdown formatting
        explanation = re.sub(r'\s+', ' ', explanation).strip()  # Clean whitespace
        
        # Extract first meaningful sentence that contains clinical information
        sentences = explanation.split('.')
        for sentence in sentences[:3]:  # Look at first 3 sentences
            if len(sentence.strip()) > 30 and any(keyword in sentence.lower() for keyword in 
                ['characteristic', 'typical', 'diagnostic', 'evidence', 'study', 'criteria']):
                return sentence.strip() + "."
        
        # Fallback: return first substantial sentence
        for sentence in sentences[:2]:
            if len(sentence.strip()) > 30:
                return sentence.strip() + "."
        
        return ""
    
    # Removed old complex function - replaced with simplified analysis
    
    # Removed old complex function - replaced with simplified analysis
    
    # Removed old complex function - replaced with simplified analysis
    
    # Removed old complex function - replaced with simplified analysis
    
    def _analyze_clinical_context(self, mcq, user_reasoning: str) -> str:
        """Analyze the clinical context and key features of the case"""
        question_text = mcq.question_text.lower()
        context_analysis = []
        
        # Identify case type and key clinical features
        if 'headache' in question_text:
            if 'daily' in question_text and 'medication' in question_text:
                context_analysis.append("🎯 **Case Type:** Chronic daily headache with medication use pattern")
                context_analysis.append("📋 **Key Clinical Features:**")
                context_analysis.append("   • Daily headaches (change from episodic pattern)")
                context_analysis.append("   • Frequent analgesic use")
                context_analysis.append("   • Loss of typical migraine features")
                context_analysis.append("\n🧬 **Pathophysiology:** Medication overuse causes central sensitization and rebound headaches, creating a cycle of increasing medication dependence.")
            elif 'cluster' in question_text:
                context_analysis.append("🎯 **Case Type:** Trigeminal autonomic cephalalgia (cluster headache)")
            elif 'migraine' in question_text:
                context_analysis.append("🎯 **Case Type:** Primary headache disorder (migraine)")
        elif 'seizure' in question_text:
            context_analysis.append("🎯 **Case Type:** Epilepsy/seizure disorder evaluation")
        elif 'movement' in question_text or any(term in question_text for term in ['tremor', 'dystonia', 'parkinson']):
            context_analysis.append("🎯 **Case Type:** Movement disorder assessment")
        else:
            context_analysis.append("🎯 **Case Type:** Neurological syndrome evaluation")
            
        return "\n".join(context_analysis)
    
    def _evaluate_correct_reasoning(self, user_reasoning: str, mcq) -> str:
        """Evaluate reasoning when answer is correct"""
        reasoning_lower = user_reasoning.lower()
        
        # Check for comprehensive reasoning
        if len(user_reasoning) > 100 and any(word in reasoning_lower for word in ['because', 'pathophysiology', 'mechanism', 'differential']):
            return "Your reasoning demonstrates solid understanding. You correctly identified key pathophysiological concepts and applied them appropriately."
        elif len(user_reasoning) > 50:
            return "Good reasoning with correct conclusion. Consider expanding your analysis to include more pathophysiological detail and differential considerations."
        else:
            return "While your answer is correct, your reasoning could be more comprehensive. Include pathophysiology, differential diagnosis, and supporting evidence."
    
    def _analyze_incorrect_reasoning_enhanced(self, user_reasoning: str, mcq, user_answer: str) -> str:
        """Enhanced analysis of incorrect reasoning with specific medical insights"""
        analysis = []
        
        # Get correct option text and user's option text
        correct_option = self._get_option_text(mcq, mcq.correct_answer)
        user_option = self._get_option_text(mcq, user_answer)
        
        analysis.append(f"🔄 **The Diagnostic Pivot:** You chose **'{user_option}'** instead of **'{correct_option}'**")
        
        # Specific case analysis based on question content
        question_lower = mcq.question_text.lower()
        reasoning_lower = user_reasoning.lower()
        
        if 'medication overuse' in correct_option.lower():
            analysis.append("\n🎯 **Critical Clinical Clue:** The key diagnostic feature here is the **pattern change** - from episodic migraines to daily headaches coinciding with frequent analgesic use.")
            analysis.append("\n⚠️ **Common Diagnostic Pitfall:** Many clinicians focus on headache characteristics rather than medication use patterns. MOH diagnosis requires:")
            analysis.append("   • Headache ≥15 days/month")
            analysis.append("   • Regular overuse of acute medications")
            analysis.append("   • Headache developed/worsened during overuse")
        elif 'chronic daily headache' in user_option.lower():
            analysis.append("\n💡 **Diagnostic Refinement:** While 'chronic daily headache' describes the pattern, it's not the underlying diagnosis. Think **etiology** - what's **causing** the chronic pattern?")
        
        # Add specific pathophysiology
        if hasattr(mcq, 'explanation') and mcq.explanation:
            patho = self._extract_enhanced_pathophysiology(mcq.explanation, correct_option)
            if patho:
                analysis.append(f"\n🧬 **Pathophysiology Insight:** {patho}")
        
        return "\n".join(analysis)
    
    def _analyze_incorrect_reasoning(self, user_reasoning: str, mcq, user_answer: str) -> str:
        """Deep analysis of incorrect reasoning"""
        return self._analyze_incorrect_reasoning_enhanced(user_reasoning, mcq, user_answer)
    
    def _get_option_text(self, mcq, option_letter: str) -> str:
        """Get the text for a specific option"""
        try:
            options_dict = mcq.get_options_dict()
            return options_dict.get(option_letter, f'Option {option_letter} not found')
        except Exception as e:
            logger.error(f"Error getting option text for {option_letter}: {e}")
            return f'Option {option_letter}'
    
    def _extract_pathophysiology_from_explanation(self, explanation: str) -> str:
        """Extract pathophysiological information from explanation"""
        return self._extract_enhanced_pathophysiology(explanation, "")
    
    def _extract_enhanced_pathophysiology(self, explanation: str, correct_option: str) -> str:
        """Enhanced pathophysiology extraction with condition-specific insights"""
        if not explanation:
            return "Review the pathophysiological mechanisms underlying this condition."
        
        explanation_lower = explanation.lower()
        
        # Medication overuse headache specific pathophysiology
        if 'medication overuse' in correct_option.lower():
            if 'central sensitization' in explanation_lower or 'rebound' in explanation_lower:
                return "Chronic analgesic use leads to central sensitization, where the trigeminal system becomes hyperexcitable. This creates a paradoxical rebound effect where medications intended to treat headaches actually perpetuate them."
            else:
                return "Medication overuse headache occurs through central sensitization mechanisms - repeated exposure to analgesics paradoxically increases headache frequency and intensity through neuroadaptive changes in pain processing pathways."
        
        # General pathophysiology extraction
        sentences = explanation.split('.')
        patho_sentences = []
        
        patho_keywords = ['mechanism', 'pathway', 'causes', 'leads to', 'results in', 'due to', 'because', 'sensitization', 'receptor', 'neurotransmitter']
        
        for sentence in sentences:
            if any(keyword in sentence.lower() for keyword in patho_keywords):
                clean_sentence = sentence.strip()
                if clean_sentence and len(clean_sentence) > 20:  # Avoid very short fragments
                    patho_sentences.append(clean_sentence)
        
        if patho_sentences:
            return '. '.join(patho_sentences[:2])  # First 2 relevant sentences
        else:
            return "Review the pathophysiological mechanisms underlying this condition."
    
    def _analyze_medical_knowledge_enhanced(self, user_reasoning: str, mcq, is_correct: bool) -> str:
        """Enhanced medical knowledge analysis with specific insights"""
        knowledge_gaps = []
        reasoning_lower = user_reasoning.lower()
        question_lower = mcq.question_text.lower()
        
        # Condition-specific knowledge assessment
        if 'headache' in question_lower and 'medication' in question_lower:
            if 'overuse' not in reasoning_lower and 'rebound' not in reasoning_lower:
                knowledge_gaps.append("🎯 **Medication Overuse Headache Recognition:** Key concept - chronic analgesic use can transform episodic headaches into daily headaches through central sensitization mechanisms.")
            
            if 'pattern' not in reasoning_lower and 'daily' not in reasoning_lower:
                knowledge_gaps.append("📊 **Headache Pattern Analysis:** Critical skill - distinguishing between headache types based on temporal patterns, triggers, and associated features.")
        
        # General neurological reasoning assessment
        if len(user_reasoning) < 50:
            knowledge_gaps.append("🧠 **Clinical Reasoning Depth:** Develop comprehensive analytical thinking that includes differential diagnosis, pathophysiology, and evidence-based decision making.")
        
        # Pathophysiology assessment
        if not any(term in reasoning_lower for term in ['mechanism', 'cause', 'pathway', 'receptor']):
            knowledge_gaps.append("🔬 **Pathophysiological Integration:** Connect underlying disease mechanisms to clinical presentations. Understanding 'why' symptoms occur strengthens diagnostic accuracy.")
        
        return "\n".join(knowledge_gaps) if knowledge_gaps else "✅ **Strong Knowledge Base:** Your reasoning demonstrates good understanding of the relevant medical concepts."
    
    def _analyze_medical_knowledge_gaps(self, user_reasoning: str, mcq, is_correct: bool) -> str:
        """Analyze specific medical knowledge gaps"""
        return self._analyze_medical_knowledge_enhanced(user_reasoning, mcq, is_correct)
    
    def _analyze_all_options_enhanced(self, mcq, user_answer: str) -> str:
        """Enhanced analysis of all answer options with specific medical reasoning"""
        analysis = []
        
        try:
            options = mcq.get_options_dict()
        except Exception as e:
            logger.error(f"Error getting options dict: {e}")
            return "Unable to analyze answer options due to data format issue."
        
        correct = mcq.correct_answer
        question_lower = mcq.question_text.lower()
        
        for letter, text in options.items():
            if text:  # Only analyze non-empty options
                if letter == correct:
                    analysis.append(f"✅ **{letter}. {text}**")
                    analysis.append(f"   **Why this is correct:** {self._explain_why_correct(text, mcq)}")
                elif letter == user_answer:
                    analysis.append(f"❌ **{letter}. {text}** *(Your Choice)*")
                    analysis.append(f"   **Why this is incorrect:** {self._explain_why_wrong_enhanced(text, mcq)}")
                else:
                    analysis.append(f"⚪ **{letter}. {text}**")
                    analysis.append(f"   **Why this is incorrect:** {self._explain_why_wrong_enhanced(text, mcq)}")
                analysis.append("")  # Add spacing between options
        
        return "\n".join(analysis) if analysis else "No answer options available for analysis."
    
    def _analyze_all_options(self, mcq, user_answer: str) -> str:
        """Analyze all answer options to show why correct answer is best"""
        return self._analyze_all_options_enhanced(mcq, user_answer)
    
    def _explain_why_correct(self, option_text: str, mcq) -> str:
        """Explain why the correct option is the best choice"""
        option_lower = option_text.lower()
        question_lower = mcq.question_text.lower()
        
        if 'medication overuse' in option_lower:
            return "This diagnosis fits the classic pattern: transformation from episodic migraines to daily headaches with frequent analgesic use. The temporal relationship between medication escalation and headache frequency is the key diagnostic clue."
        elif 'migraine' in option_lower and 'migraine' in question_lower:
            return "This matches the clinical presentation of recurrent headaches with characteristic features and triggers."
        elif 'cluster' in option_lower:
            return "The unilateral, severe headaches with autonomic features are pathognomonic for cluster headache."
        else:
            return "This option best matches the clinical scenario and underlying pathophysiology described."
    
    def _explain_why_wrong_enhanced(self, option_text: str, mcq) -> str:
        """Enhanced explanation of why specific options are incorrect"""
        option_lower = option_text.lower()
        question_lower = mcq.question_text.lower()
        
        if 'chronic daily headache' in option_lower and 'medication' in question_lower:
            return "While this describes the symptom pattern, it's not a specific diagnosis. It fails to identify the underlying cause (medication overuse) that's driving the daily headache pattern."
        elif 'typical migraine' in option_lower and 'daily' in question_lower:
            return "Typical migraines are episodic, not daily. The loss of typical migraine features (nausea, photophobia) and daily pattern suggests a secondary process."
        elif 'tension-type headache' in option_lower and 'migraine' in question_lower:
            return "While tension-type headaches can be daily, the history of migraines and medication use points to medication overuse headache rather than primary tension-type headache."
        elif 'migraine' in option_lower and 'movement' in getattr(mcq, 'subspecialty', '').lower():
            return "this describes a headache condition rather than a movement disorder"
        elif 'stroke' in option_lower and 'young' in question_lower:
            return "stroke is less likely in young patients without vascular risk factors"
        elif 'tumor' in option_lower:
            return "tumors typically present with progressive symptoms and focal deficits"
        else:
            return "it doesn't match the clinical presentation described"
    
    def _explain_why_wrong(self, option_text: str, mcq) -> str:
        """Explain why a specific option is incorrect"""
        return self._explain_why_wrong_enhanced(option_text, mcq)
    
    def _analyze_reasoning_process(self, user_reasoning: str, mcq, is_correct: bool) -> str:
        """Analyze the clinical reasoning process used"""
        process_analysis = []
        reasoning_lower = user_reasoning.lower()
        
        # Check for systematic approach
        systematic_words = ['first', 'then', 'next', 'consider', 'differential', 'rule out']
        if any(word in reasoning_lower for word in systematic_words):
            process_analysis.append('✅ <strong>Systematic Approach:</strong> You demonstrate structured thinking.')
        else:
            process_analysis.append('🔄 <strong>Systematic Approach:</strong> Consider using a more structured approach: History → Examination → Differential → Testing → Diagnosis.')
        
        # Check for evidence-based reasoning
        evidence_words = ['guidelines', 'studies', 'evidence', 'research', 'literature']
        if any(word in reasoning_lower for word in evidence_words):
            process_analysis.append('✅ <strong>Evidence-Based:</strong> You reference medical evidence.')
        else:
            process_analysis.append('📚 <strong>Evidence-Based Reasoning:</strong> Strengthen your reasoning by referencing current guidelines and research evidence.')
        
        # Check for differential diagnosis
        if 'differential' in reasoning_lower or 'consider' in reasoning_lower:
            process_analysis.append('✅ <strong>Differential Thinking:</strong> You consider alternative diagnoses.')
        else:
            process_analysis.append('🤔 <strong>Differential Diagnosis:</strong> Always consider what else could cause similar symptoms. This prevents premature closure.')
        
        return "\n".join(process_analysis)
    
    def _generate_targeted_insights(self, user_reasoning: str, mcq, is_correct: bool) -> str:
        """Generate targeted learning insights based on the specific case"""
        insights = []
        question_lower = mcq.question_text.lower()
        
        # Case-specific insights
        if 'headache' in question_lower and 'medication' in question_lower:
            insights.append("🎯 **Clinical Pearl:** In headache medicine, always ask about medication use patterns. The phrase 'must take' medications suggests dependence and overuse.")
            insights.append("📋 **Diagnostic Approach:** For chronic daily headache, use this framework:")
            insights.append("   1. Was there a previous headache disorder? (Yes - suggests transformation)")
            insights.append("   2. What medications are being used? (Frequency and type)")
            insights.append("   3. When did the pattern change? (Temporal relationship)")
            insights.append("🔄 **Management Insight:** MOH treatment requires medication withdrawal - headaches often worsen initially before improving.")
        
        # Reasoning quality insights
        if len(user_reasoning) < 50:
            insights.append("💭 **Reasoning Development:** Practice the 'think aloud' method - verbalize your thought process as you work through cases.")
        
        if not is_correct:
            insights.append("🎓 **Learning Opportunity:** Incorrect answers are valuable learning moments. Focus on the specific clinical clues you may have missed.")
            insights.append("📚 **Next Steps:** Review similar cases to reinforce pattern recognition and diagnostic criteria.")
        else:
            insights.append("✅ **Well Done:** Your correct answer shows good clinical reasoning. Continue building on this foundation.")
        
        return "\n".join(insights)
    
    def _generate_learning_recommendations(self, user_reasoning: str, mcq, is_correct: bool) -> str:
        """Generate specific learning recommendations"""
        return self._generate_targeted_insights(user_reasoning, mcq, is_correct)
    
    def _extract_clinical_features(self, question_text: str) -> List[str]:
        """Extract key clinical features from the question"""
        features = []
        text_lower = question_text.lower()
        
        # Age patterns
        import re
        age_match = re.search(r'(\d+)[\s-]*(year|yo|y/o)', text_lower)
        if age_match:
            features.append(f"Age: {age_match.group(1)} years")
        
        # Gender
        if 'male' in text_lower or ' man ' in text_lower:
            features.append("Gender: Male")
        elif 'female' in text_lower or ' woman ' in text_lower:
            features.append("Gender: Female")
        
        # Temporal patterns
        temporal_patterns = {
            'acute': 'Acute onset',
            'chronic': 'Chronic course',
            'progressive': 'Progressive deterioration',
            'sudden': 'Sudden onset',
            'gradual': 'Gradual onset',
            'recurrent': 'Recurrent episodes'
        }
        for pattern, description in temporal_patterns.items():
            if pattern in text_lower:
                features.append(f"Temporal pattern: {description}")
        
        # Key symptoms
        symptom_keywords = {
            'chorea': 'Choreiform movements',
            'tremor': 'Tremor',
            'rigidity': 'Rigidity',
            'bradykinesia': 'Bradykinesia',
            'dystonia': 'Dystonia',
            'ataxia': 'Ataxia',
            'weakness': 'Weakness',
            'cognitive': 'Cognitive impairment',
            'dementia': 'Dementia',
            'psychiatric': 'Psychiatric symptoms',
            'seizure': 'Seizures',
            'headache': 'Headache'
        }
        for keyword, symptom in symptom_keywords.items():
            if keyword in text_lower:
                features.append(f"Key symptom: {symptom}")
        
        # Family history
        if 'family history' in text_lower or 'father' in text_lower or 'mother' in text_lower:
            features.append("Positive family history")
        
        return features[:10]  # Limit to top 10 features
    
    def _identify_condition_similarities(self, user_option: str, correct_option: str, mcq) -> List[str]:
        """Identify similarities between the user's choice and correct answer"""
        similarities = []
        
        user_lower = user_option.lower()
        correct_lower = correct_option.lower()
        
        # Movement disorder similarities
        if 'chorea' in user_lower and 'huntington' in correct_lower:
            similarities.append("Both conditions feature prominent choreiform movements")
            similarities.append("Both can present with psychiatric symptoms (depression, anxiety, psychosis)")
            similarities.append("Both show progressive neurological deterioration")
            similarities.append("Both can affect younger adults (though age ranges differ)")
        
        elif 'huntington' in user_lower and 'huntington' in correct_lower:
            if 'like' in user_lower:  # Huntington disease-like conditions
                similarities.append("HDL syndromes mimic Huntington's disease clinically")
                similarities.append("Both have chorea, cognitive decline, and psychiatric features")
                similarities.append("Both show autosomal dominant inheritance patterns")
                similarities.append("Clinical presentation can be indistinguishable without genetic testing")
        
        # Headache similarities
        elif 'headache' in user_lower and 'headache' in correct_lower:
            similarities.append("Both present with chronic daily headache patterns")
            similarities.append("Both can transform from episodic to chronic forms")
            similarities.append("Both may respond initially to analgesics")
        
        # Generic similarities
        else:
            similarities.append("Both conditions can affect similar anatomical regions")
            similarities.append("Initial presentations may overlap significantly")
            similarities.append("Both require careful clinical differentiation")
        
        return similarities
    
    def _extract_evidence_from_explanation(self, explanation: str) -> List[str]:
        """Extract key evidence points from MCQ explanation"""
        evidence_points = []
        
        if not explanation:
            return ["Clinical presentation matches established diagnostic criteria",
                    "Epidemiological factors support this diagnosis",
                    "Pathophysiological mechanisms align with observed symptoms"]
        
        # Split explanation into sentences
        sentences = [s.strip() for s in explanation.split('.') if s.strip()]
        
        # Look for evidence indicators
        evidence_keywords = ['because', 'due to', 'caused by', 'results from', 'indicates', 
                           'suggests', 'consistent with', 'diagnostic', 'specific for', 'pathognomonic']
        
        for sentence in sentences:
            if any(keyword in sentence.lower() for keyword in evidence_keywords):
                if len(sentence) > 20:  # Meaningful length
                    evidence_points.append(sentence)
        
        # If no evidence found, extract key statements
        if not evidence_points and sentences:
            evidence_points = [s for s in sentences if len(s) > 30][:3]
        
        return evidence_points
    
    def _get_condition_specific_evidence(self, condition: str, mcq) -> str:
        """Get condition-specific evidence for why it's the correct answer"""
        condition_lower = condition.lower()
        
        evidence_map = {
            'huntington': [
                "• **Genetic Evidence:** Autosomal dominant inheritance with CAG repeat expansion in HTT gene",
                "• **Clinical Triad:** Choreiform movements + cognitive decline + psychiatric symptoms",
                "• **Imaging:** Caudate atrophy on MRI with 'boxcar' ventricles",
                "• **Age of Onset:** Typically 30-50 years with juvenile and late-onset variants",
                "• **Progression:** Inexorable deterioration over 15-20 years"
            ],
            'chorea-acanthocytosis': [
                "• **Laboratory:** Acanthocytes >15% on fresh blood smear",
                "• **Clinical:** Orofacial dyskinesias with self-mutilating tongue/lip biting",
                "• **Neuropathy:** Axonal sensorimotor polyneuropathy on NCS/EMG",
                "• **Imaging:** Caudate and putamen atrophy without 'boxcar' sign",
                "• **Inheritance:** Autosomal recessive with VPS13A mutations"
            ],
            'medication overuse': [
                "• **Temporal Relationship:** Headache frequency increased with medication use",
                "• **ICHD-3 Criteria:** ≥15 headache days/month with regular overuse >3 months",
                "• **Transformation:** Evolution from episodic to chronic pattern",
                "• **Medication Pattern:** Daily or near-daily acute medication use",
                "• **Improvement:** Headache improves after medication withdrawal"
            ]
        }
        
        # Find matching evidence
        for key, evidence_list in evidence_map.items():
            if key in condition_lower:
                return "\n".join(evidence_list)
        
        # Default evidence structure
        return """• **Clinical Presentation:** Matches established diagnostic criteria
• **Epidemiology:** Age, sex, and risk factors align with this diagnosis
• **Pathophysiology:** Underlying mechanisms explain observed symptoms
• **Diagnostic Tests:** Laboratory/imaging findings support this diagnosis
• **Natural History:** Disease progression matches expected pattern"""
    
    def _get_clinical_trial_evidence(self, correct_option: str, user_option: str) -> str:
        """Provide clinical trial and guideline evidence"""
        condition_lower = correct_option.lower()
        
        trial_evidence = {
            'huntington': """• **PREDICT-HD Study:** Established biomarkers for disease progression
• **ENROLL-HD Registry:** Global observational study defining natural history
• **Guidelines:** Movement Disorder Society diagnostic criteria (2020)
• **Genetic Testing:** 100% penetrance with CAG repeats ≥40""",
            
            'medication overuse': """• **HURT Study:** Demonstrated efficacy of withdrawal therapy
• **International Headache Society:** ICHD-3 diagnostic criteria
• **Cochrane Review (2020):** Evidence for withdrawal + prophylaxis
• **Success Rate:** 50-70% improvement after structured withdrawal""",
            
            'chorea-acanthocytosis': """• **Walker et al. (2019):** Comprehensive review of 150+ cases
• **Diagnostic Criteria:** Danek et al. consensus guidelines
• **Blood Smear Technique:** Fresh blood, immediate processing crucial
• **Genetic Testing:** VPS13A sequencing confirms diagnosis"""
        }
        
        for key, evidence in trial_evidence.items():
            if key in condition_lower:
                return evidence
        
        return """• **Clinical Guidelines:** Based on expert consensus and systematic reviews
• **Diagnostic Accuracy:** High sensitivity and specificity for key features
• **Evidence Level:** Supported by observational studies and case series
• **International Standards:** Follows established diagnostic criteria"""
    
    def _get_advanced_pathophysiology(self, condition: str, mcq) -> str:
        """Provide advanced pathophysiological insights"""
        condition_lower = condition.lower()
        
        if 'huntington' in condition_lower:
            return """• **Molecular Mechanism:** CAG repeat expansion → polyglutamine aggregates → selective medium spiny neuron death
• **Circuit Dysfunction:** Direct/indirect pathway imbalance → chorea and cognitive symptoms
• **Metabolic Changes:** Mitochondrial dysfunction, excitotoxicity, impaired BDNF signaling
• **Spreading Pattern:** Dorsal → ventral striatum → cortical involvement"""
        
        elif 'medication overuse' in condition_lower:
            return """• **Central Sensitization:** Repeated analgesic exposure → enhanced trigeminal nociception
• **Receptor Changes:** Downregulation of 5-HT receptors, upregulation of CGRP
• **Neuroplasticity:** Altered pain processing in periaqueductal gray and thalamus
• **Withdrawal Physiology:** Rebound hyperalgesia via opioid/serotonin systems"""
        
        return """• **Cellular Mechanisms:** Specific pathways affected by this condition
• **Network Dysfunction:** How neural circuits are disrupted
• **Molecular Cascades:** Downstream effects of primary pathology
• **Compensatory Mechanisms:** How the nervous system attempts to adapt"""
    
    def _get_clinical_pearls(self, condition: str, mcq) -> List[str]:
        """Get clinical pearls for the condition"""
        condition_lower = condition.lower()
        
        pearls_map = {
            'huntington': [
                "Look for 'milkmaid grip' - inability to maintain sustained grip",
                "Psychiatric symptoms often precede motor symptoms by years",
                "Juvenile HD (<20 years) presents with rigidity, not chorea",
                "Tetrabenazine specifically approved for HD chorea",
                "Consider HD in any adult-onset chorea with family history"
            ],
            'medication overuse': [
                "The 'must take' phrase is a red flag for dependency",
                "Triptans: overuse threshold is 10 days/month",
                "Simple analgesics: overuse threshold is 15 days/month",
                "Withdrawal symptoms peak at 2-10 days",
                "Bridge therapy with steroids can ease withdrawal"
            ]
        }
        
        for key, pearls in pearls_map.items():
            if key in condition_lower:
                return pearls[:3]
        
        return [
            "Pattern recognition is key to accurate diagnosis",
            "Always consider the full clinical context",
            "Confirmatory testing should support clinical impression"
        ]
    
    def _get_diagnostic_pitfalls(self, condition: str, mcq) -> List[str]:
        """Common diagnostic pitfalls to avoid"""
        condition_lower = condition.lower()
        
        pitfalls_map = {
            'huntington': [
                "Missing HD in patients without obvious family history (de novo mutations, non-paternity)",
                "Confusing HD with drug-induced chorea (detailed medication history crucial)",
                "Overlooking HD phenocopies that require different genetic testing"
            ],
            'medication overuse': [
                "Treating the headache without addressing medication overuse",
                "Not recognizing 'hidden' OTC medication use",
                "Abandoning withdrawal too early due to initial worsening"
            ]
        }
        
        for key, pitfalls in pitfalls_map.items():
            if key in condition_lower:
                return pitfalls
        
        return [
            "Anchoring on initial impression without considering alternatives",
            "Insufficient history taking missing key diagnostic clues",
            "Over-relying on tests without clinical correlation"
        ]
    
    def _get_concise_definition(self, condition: str) -> str:
        """Get concise medical definition based on question context"""
        # Check if this is a ratio or numeric value
        if ':' in condition and any(char.isdigit() for char in condition):
            # This is a ratio (e.g., "1:1", "2:1", "4:1")
            return self._get_ratio_definition(condition)
        
        # Existing definitions for specific conditions
        definitions = {
            'huntington disease': "Autosomal dominant neurodegenerative disorder with CAG repeats causing progressive chorea, dementia, and psychiatric symptoms",
            'chorea-acanthocytosis': "Autosomal recessive neuroacanthocytosis with chorea, self-mutilation, and acanthocytes on blood smear",
            'huntington disease-like 2': "HDL2 caused by CTG/CAG expansion in JPH3 gene, clinically similar to HD but different genetics",
            'medication overuse headache': "Secondary headache disorder from regular overuse of acute headache medications causing paradoxical worsening"
        }
        
        for key, definition in definitions.items():
            if key in condition.lower():
                return definition
        
        # Try to generate a context-aware definition
        return self._generate_context_aware_definition(condition)
    
    def _get_ratio_definition(self, ratio: str) -> str:
        """Get definition for ratio-based answers"""
        # Extract numbers from ratio
        parts = ratio.split(':')
        if len(parts) == 2:
            try:
                male = int(parts[0])
                female = int(parts[1])
                
                if male == female:
                    return "Equal distribution between males and females, suggesting no sex predilection"
                elif male > female:
                    return f"Male predominance with {male} males affected for every {female} female(s)"
                else:
                    return f"Female predominance with {female} females affected for every {male} male(s)"
            except:
                pass
        
        return f"A sex distribution ratio in epidemiological studies"
    
    def _generate_context_aware_definition(self, condition: str) -> str:
        """Generate a context-aware definition based on the condition"""
        condition_lower = condition.lower()
        
        # Check if this is a treatment/intervention
        treatments = {
            'psychotherapy': "Evidence-based psychological intervention using therapeutic techniques to treat mental health conditions",
            'cognitive behavioral therapy': "Structured psychotherapy focusing on identifying and changing negative thought patterns and behaviors",
            'cbt': "Structured psychotherapy focusing on identifying and changing negative thought patterns and behaviors",
            'propranolol': "Non-selective beta-blocker used for cardiovascular conditions, anxiety, and migraine prevention",
            'lithium': "Mood stabilizer primarily used for bipolar disorder and severe depression",
            'carbamazepine': "Anticonvulsant medication used for epilepsy, trigeminal neuralgia, and mood stabilization",
            'gabapentin': "Anticonvulsant medication used for neuropathic pain and adjunctive epilepsy treatment",
            'amitriptyline': "Tricyclic antidepressant used for depression, neuropathic pain, and migraine prevention",
            'sertraline': "SSRI antidepressant used for depression, anxiety, and OCD",
            'risperidone': "Atypical antipsychotic used for schizophrenia, bipolar disorder, and behavioral problems"
        }
        
        for treatment, definition in treatments.items():
            if treatment in condition_lower:
                return definition
        
        # Medical conditions
        if 'syndrome' in condition_lower:
            return f"A clinical syndrome characterized by a specific constellation of signs and symptoms"
        elif 'disease' in condition_lower:
            return f"A pathological condition with defined etiology, pathophysiology, and clinical manifestations"
        elif 'disorder' in condition_lower:
            return f"A medical condition characterized by functional impairment or structural abnormality"
        elif any(term in condition_lower for term in ['palsy', 'paralysis']):
            return f"A neurological condition involving weakness or paralysis of affected muscles"
        elif 'epilepsy' in condition_lower:
            return f"A neurological disorder characterized by recurrent seizures"
        elif 'neuropathy' in condition_lower:
            return f"A disorder affecting peripheral nerves with sensory, motor, or autonomic dysfunction"
        elif 'myopathy' in condition_lower:
            return f"A muscle disease characterized by muscle weakness and/or wasting"
        elif 'ataxia' in condition_lower:
            return f"A neurological sign of impaired coordination and balance"
        elif any(term in condition_lower for term in ['anxiety', 'depression', 'panic']):
            return f"A psychiatric condition affecting mood, cognition, and behavior requiring clinical assessment and treatment"
        else:
            # For other conditions, provide a more specific placeholder
            return f"A clinical entity with characteristic features relevant to this case"
    
    def _create_differential_table(self, options: dict, mcq) -> str:
        """Create a context-aware comparison table"""
        if not options or len(options) < 2:
            return "Insufficient options for comparison table"
        
        # Determine if this is about treatments or conditions
        is_treatment_question = any(
            treatment in ' '.join(options.values()).lower() 
            for treatment in ['therapy', 'medication', 'drug', 'treatment', 'propranolol', 'psychotherapy']
        )
        
        if is_treatment_question:
            return self._create_treatment_comparison_table(options, mcq)
        else:
            return self._create_condition_comparison_table(options, mcq)
    
    def _create_treatment_comparison_table(self, options: dict, mcq) -> str:
        """Create treatment comparison table"""
        table = ["| Aspect | " + " | ".join(f"{option[:12]}..." if len(option) > 12 else option for option in options.values()) + " |"]
        table.append("|---------|" + "---------|" * len(options))
        
        # Treatment-specific features
        features = {
            "Mechanism": self._get_treatment_mechanisms(options),
            "Onset": self._get_treatment_onsets(options),
            "Side Effects": self._get_treatment_side_effects(options),
            "Efficacy": self._get_treatment_efficacy(options)
        }
        
        for feature_name, feature_values in features.items():
            if feature_values:
                row = f"| {feature_name} | " + " | ".join(feature_values) + " |"
                table.append(row)
        
        return "\n".join(table)
    
    def _create_condition_comparison_table(self, options: dict, mcq) -> str:
        """Create condition comparison table"""
        table = ["| Feature | " + " | ".join(f"{option[:12]}..." if len(option) > 12 else option for option in options.values()) + " |"]
        table.append("|---------|" + "---------|" * len(options))
        
        # Condition-specific features based on subspecialty
        subspecialty = getattr(mcq, 'subspecialty', '').lower()
        
        if 'movement' in subspecialty:
            table.append("| Age Onset | Variable | Variable | Variable |")
            table.append("| Movement | Chorea | Dystonia | Tremor |")
            table.append("| Inheritance | AD | AR | Sporadic |")
        elif 'headache' in subspecialty:
            table.append("| Duration | Hours | Days | Continuous |")
            table.append("| Location | Unilateral | Bilateral | Variable |")
            table.append("| Character | Throbbing | Pressing | Stabbing |")
        else:
            table.append("| Onset | Acute | Subacute | Chronic |")
            table.append("| Pattern | Episodic | Progressive | Static |")
            table.append("| Severity | Mild | Moderate | Severe |")
        
        return "\n".join(table)
    
    def _get_treatment_mechanisms(self, options: dict) -> list:
        """Get treatment mechanisms"""
        mechanisms = []
        for option in options.values():
            option_lower = option.lower()
            if 'psychotherapy' in option_lower or 'therapy' in option_lower:
                mechanisms.append("Psychological")
            elif 'propranolol' in option_lower:
                mechanisms.append("Beta-blocker")
            elif any(drug in option_lower for drug in ['sertraline', 'ssri']):
                mechanisms.append("SSRI")
            elif any(drug in option_lower for drug in ['lithium']):
                mechanisms.append("Mood stabilizer")
            else:
                mechanisms.append("Pharmacological")
        return mechanisms
    
    def _get_treatment_onsets(self, options: dict) -> list:
        """Get treatment onset times"""
        onsets = []
        for option in options.values():
            option_lower = option.lower()
            if 'psychotherapy' in option_lower:
                onsets.append("2-4 weeks")
            elif 'propranolol' in option_lower:
                onsets.append("30-60 min")
            elif any(drug in option_lower for drug in ['sertraline', 'ssri']):
                onsets.append("4-6 weeks")
            else:
                onsets.append("Variable")
        return onsets
    
    def _get_treatment_side_effects(self, options: dict) -> list:
        """Get treatment side effects"""
        side_effects = []
        for option in options.values():
            option_lower = option.lower()
            if 'psychotherapy' in option_lower:
                side_effects.append("Minimal")
            elif 'propranolol' in option_lower:
                side_effects.append("Fatigue, bradycardia")
            elif any(drug in option_lower for drug in ['sertraline', 'ssri']):
                side_effects.append("GI, sexual dysfunction")
            else:
                side_effects.append("Variable")
        return side_effects
    
    def _get_treatment_efficacy(self, options: dict) -> list:
        """Get treatment efficacy"""
        efficacy = []
        for option in options.values():
            option_lower = option.lower()
            if 'psychotherapy' in option_lower:
                efficacy.append("High (long-term)")
            elif 'propranolol' in option_lower:
                efficacy.append("Moderate (acute)")
            else:
                efficacy.append("Variable")
        return efficacy
    
    def _create_decision_tree(self, options: dict, correct_option: str, mcq) -> str:
        """Create a context-aware decision tree"""
        # Determine if this is about treatments or conditions
        is_treatment_question = any(
            treatment in ' '.join(options.values()).lower() 
            for treatment in ['therapy', 'medication', 'drug', 'treatment', 'propranolol', 'psychotherapy']
        )
        
        if is_treatment_question:
            return self._create_treatment_decision_tree(options, mcq)
        else:
            return self._create_condition_decision_tree(options, mcq)
    
    def _create_treatment_decision_tree(self, options: dict, mcq) -> str:
        """Create treatment decision tree"""
        # Check if this is about anxiety/psychiatric treatment
        if any(term in ' '.join(options.values()).lower() for term in ['psychotherapy', 'anxiety', 'panic']):
            tree = """```
Patient with anxiety/psychiatric symptoms
├─ Severity assessment
│   ├─ Mild → Psychotherapy first-line
│   ├─ Moderate → Combined therapy or medication
│   └─ Severe → Medication + psychotherapy
├─ Acute vs chronic presentation
│   ├─ Acute episodes → Short-acting options (propranolol)
│   └─ Chronic condition → Long-term therapy
└─ Patient preference and contraindications
    ├─ Prefers non-medication → Psychotherapy
    └─ Needs rapid relief → Medication options
```"""
        else:
            tree = """```
Treatment selection process
├─ Assess severity and urgency
│   ├─ Acute/severe → Immediate pharmacological intervention
│   └─ Chronic/mild → Consider non-pharmacological approaches
├─ Evaluate patient factors
│   ├─ Age, comorbidities → Adjust treatment choice
│   └─ Previous treatment response → Guide selection
└─ Monitor and adjust
    ├─ Assess response → Continue or modify
    └─ Side effects → Switch or add therapy
```"""
        return tree
    
    def _create_condition_decision_tree(self, options: dict, mcq) -> str:
        """Create condition decision tree"""
        subspecialty = getattr(mcq, 'subspecialty', '').lower()
        
        if 'movement' in subspecialty:
            tree = """```
Is there a movement disorder?
├─ YES → Is there chorea?
│   ├─ YES → Family history?
│   │   ├─ YES → Consider Huntington's
│   │   └─ NO → Check for acanthocytes
│   └─ NO → Evaluate other movements
└─ NO → Consider non-movement disorders
```"""
        elif 'headache' in subspecialty:
            tree = """```
Patient with headache
├─ Primary vs Secondary?
│   ├─ Red flags present → Investigate secondary causes
│   └─ No red flags → Consider primary headaches
├─ Headache pattern
│   ├─ Episodic → Migraine vs tension-type
│   └─ Daily/chronic → Medication overuse vs chronic daily headache
└─ Associated features
    ├─ Neurological signs → Secondary headache
    └─ Typical features → Primary headache disorder
```"""
        elif 'epilepsy' in subspecialty:
            tree = """```
Seizure-like episodes
├─ Witnessed seizure activity?
│   ├─ YES → Focal vs generalized?
│   └─ NO → Non-epileptic vs unwitnessed seizure
├─ EEG findings
│   ├─ Epileptiform → Epilepsy likely
│   └─ Normal → Consider other causes
└─ Response to treatment
    ├─ AED responsive → Supports epilepsy
    └─ AED non-responsive → Reconsider diagnosis
```"""
        else:
            tree = """```
Clinical presentation analysis
├─ Onset pattern
│   ├─ Acute → Vascular, infectious, toxic
│   ├─ Subacute → Inflammatory, neoplastic
│   └─ Chronic → Degenerative, metabolic
├─ Distribution
│   ├─ Focal → Structural lesion
│   └─ Diffuse → Systemic process
└─ Associated features
    ├─ Systemic symptoms → Systemic disease
    └─ Isolated neurological → Primary CNS
```"""
        return tree
    
    def _create_mnemonic(self, condition: str, mcq) -> str:
        """Create a mnemonic for remembering key features"""
        mnemonics = {
            'huntington': "**HUNTINGTON:** **H**ereditary **U**ncontrolled movements **N**europsychiatric **T**riad **I**nexorable **N**eurodegeneration **G**enetic **T**esting **O**nset 30-50 **N**ineteen CAG repeats",
            'medication': "**MOHEAD:** **M**edication **O**veruse **H**eadache **E**very day **A**nalgesics **D**ependence"
        }
        
        for key, mnemonic in mnemonics.items():
            if key in condition.lower():
                return mnemonic
        
        return "Create your own mnemonic using the first letters of key features"
    
    def _create_pattern_summary(self, mcq, correct_option: str) -> str:
        """Create a memorable pattern summary"""
        # Check if this is a treatment question
        is_treatment = any(
            treatment in correct_option.lower() 
            for treatment in ['therapy', 'medication', 'drug', 'treatment', 'propranolol', 'psychotherapy']
        )
        
        if is_treatment:
            return self._create_treatment_pattern_summary(mcq, correct_option)
        else:
            return self._create_condition_pattern_summary(mcq, correct_option)
    
    def _create_treatment_pattern_summary(self, mcq, correct_option: str) -> str:
        """Create treatment-focused pattern summary"""
        # Extract condition being treated
        question_lower = mcq.question_text.lower()
        
        if any(term in question_lower for term in ['anxiety', 'panic', 'nervous']):
            condition = "anxiety"
        elif any(term in question_lower for term in ['depression', 'mood', 'sad']):
            condition = "depression"
        elif any(term in question_lower for term in ['headache', 'migraine']):
            condition = "headache disorders"
        else:
            condition = "this condition"
        
        # Create appropriate summary
        if 'psychotherapy' in correct_option.lower():
            return f"For {condition}, consider psychotherapy as first-line or adjunctive treatment"
        elif 'propranolol' in correct_option.lower():
            return f"Propranolol effective for acute {condition} symptoms and performance anxiety"
        else:
            return f"Evidence-based treatment selection crucial for {condition} management"
    
    def _create_condition_pattern_summary(self, mcq, correct_option: str) -> str:
        """Create condition-focused pattern summary"""
        # Extract key elements from question
        age_match = re.search(r'(\d+)[\s-]*(year|yo)', mcq.question_text.lower())
        age = f"{age_match.group(1)}-year-old" if age_match else "Adult"
        
        # Identify key clinical feature
        question_lower = mcq.question_text.lower()
        if 'chorea' in question_lower:
            key_feature = "with chorea"
        elif 'headache' in question_lower:
            key_feature = "with chronic headache"
        elif 'seizure' in question_lower:
            key_feature = "with seizures"
        elif 'weakness' in question_lower:
            key_feature = "with weakness"
        elif 'tremor' in question_lower:
            key_feature = "with tremor"
        else:
            # Make it more specific than just "neurological symptoms"
            subspecialty = getattr(mcq, 'subspecialty', '').lower()
            if 'movement' in subspecialty:
                key_feature = "with movement disorder"
            elif 'headache' in subspecialty:
                key_feature = "with headache"
            elif 'epilepsy' in subspecialty:
                key_feature = "with seizure-like episodes"
            else:
                key_feature = "with these symptoms"
        
        return f"{age} {key_feature} = Consider {correct_option}"
    
    def _analyze_reasoning_patterns(self, user_reasoning: str, mcq, is_correct: bool) -> str:
        """Analyze reasoning patterns when specific conditions aren't identified"""
        if len(user_reasoning) < 50:
            return "• **Limited Reasoning Depth:** Your brief explanation suggests quick pattern matching rather than systematic analysis"
        elif 'similar' in user_reasoning.lower() or 'like' in user_reasoning.lower():
            return "• **Similarity-Based Reasoning:** You recognized pattern similarities but may have missed distinguishing features"
        else:
            return "• **Clinical Reasoning Pattern:** Your approach shows systematic thinking; let's refine the differential diagnosis process"
    
    def _create_summary_table(self, mcq, user_answer: str, is_correct: bool) -> str:
        """Create a clean HTML table summarizing key concepts from the analysis"""
        correct_option = self._get_option_text(mcq, mcq.correct_answer)
        
        # Determine the primary diagnosis/concept
        if 'medication overuse' in correct_option.lower():
            key_diagnosis = "Medication Overuse Headache (MOH)"
            distinguishing_features = [
                "Daily or near-daily headache (≥15 days/month)",
                "Regular overuse of acute headache medications",
                "Transformation from episodic to chronic pattern",
                "Headache worsens with continued medication use"
            ]
            clinical_pearls = [
                "The phrase 'must take' indicates dependency",
                "Withdrawal initially worsens headaches before improvement",
                "Prevention requires breaking the medication cycle"
            ]
            evidence_guidelines = [
                "ICHD-3 diagnostic criteria",
                "50-70% improvement rate with structured withdrawal",
                "Prophylactic therapy after withdrawal period"
            ]
        elif 'huntington' in correct_option.lower():
            key_diagnosis = "Huntington Disease"
            distinguishing_features = [
                "Autosomal dominant inheritance",
                "Choreiform movements",
                "Cognitive decline (subcortical dementia)",
                "Psychiatric symptoms (depression, psychosis)"
            ]
            clinical_pearls = [
                "CAG repeat expansion ≥36 in HTT gene",
                "Psychiatric symptoms may precede motor symptoms",
                "Juvenile HD presents with rigidity, not chorea"
            ]
            evidence_guidelines = [
                "Genetic testing is definitive",
                "MDS diagnostic criteria",
                "Tetrabenazine for chorea management"
            ]
        elif 'chorea-acanthocytosis' in correct_option.lower():
            key_diagnosis = "Chorea-Acanthocytosis"
            distinguishing_features = [
                "Acanthocytes >15% on fresh blood smear",
                "Orofacial dyskinesias with self-mutilation",
                "Peripheral neuropathy",
                "Autosomal recessive inheritance"
            ]
            clinical_pearls = [
                "Tongue/lip biting is characteristic",
                "VPS13A gene mutations",
                "Fresh blood required for acanthocyte detection"
            ]
            evidence_guidelines = [
                "Consensus diagnostic criteria (Danek et al.)",
                "NCS/EMG shows axonal neuropathy",
                "Genetic testing confirms diagnosis"
            ]
        else:
            # Generic neurological condition
            key_diagnosis = correct_option
            # Extract features from question and existing methods
            distinguishing_features = self._extract_key_features_from_condition(correct_option, mcq)
            clinical_pearls = self._get_clinical_pearls(correct_option, mcq)[:3] if hasattr(self, '_get_clinical_pearls') else ["Pattern recognition is key", "Consider differential diagnosis", "Confirmatory testing supports clinical impression"]
            evidence_guidelines = ["Follow established diagnostic criteria", "Evidence-based guidelines", "Current best practices"]
        
        # Build the clean HTML table
        table_html = f"""
        <table class="concept-summary-table">
            <thead>
                <tr>
                    <th class="summary-header" colspan="2">📋 Clinical Concept Summary</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td class="summary-label">Key Diagnosis/Concept</td>
                    <td class="summary-value"><strong>{key_diagnosis}</strong></td>
                </tr>
                <tr>
                    <td class="summary-label">Distinguishing Features</td>
                    <td class="summary-value">
                        <ul class="feature-list">
                            {"".join(f'<li>{feature}</li>' for feature in distinguishing_features[:4])}
                        </ul>
                    </td>
                </tr>
                <tr>
                    <td class="summary-label">Clinical Pearls</td>
                    <td class="summary-value">
                        <ul class="pearl-list">
                            {"".join(f'<li>{pearl}</li>' for pearl in clinical_pearls[:3])}
                        </ul>
                    </td>
                </tr>
                <tr>
                    <td class="summary-label">Evidence/Guidelines</td>
                    <td class="summary-value">
                        <ul class="evidence-list">
                            {"".join(f'<li>{evidence}</li>' for evidence in evidence_guidelines[:3])}
                        </ul>
                    </td>
                </tr>
            </tbody>
        </table>
        """
        
        return table_html
    
    def _extract_key_features_from_condition(self, condition: str, mcq) -> List[str]:
        """Extract key features based on the condition name"""
        features = []
        condition_lower = condition.lower()
        
        # Try to get features from existing methods
        features_dict = self._get_condition_features_dict(condition)
        if features_dict and 'Clinical Pattern' not in features_dict:  # Not default response
            # Convert dict to list of formatted strings
            for key, value in features_dict.items():
                features.append(f"{key}: {value}")
            return features[:4]
        
        # Otherwise extract from question
        text_lower = mcq.question_text.lower()
        
        # Look for age
        import re
        age_match = re.search(r'(\d+)[\s-]*(year|yo)', text_lower)
        if age_match:
            features.append(f"Age: {age_match.group(1)} years")
        
        # Look for temporal patterns
        if 'acute' in text_lower:
            features.append("Acute onset")
        elif 'chronic' in text_lower:
            features.append("Chronic course")
        elif 'progressive' in text_lower:
            features.append("Progressive deterioration")
        
        # Look for key symptoms in question
        symptom_map = {
            'headache': 'Headache',
            'seizure': 'Seizures',
            'weakness': 'Motor weakness',
            'cognitive': 'Cognitive impairment',
            'movement': 'Movement disorder',
            'tremor': 'Tremor',
            'ataxia': 'Ataxia',
            'vision': 'Visual symptoms'
        }
        
        for keyword, symptom in symptom_map.items():
            if keyword in text_lower:
                features.append(symptom)
        
        # Ensure we have at least some features
        if not features:
            features = ["Clinical presentation as described", "Neurological symptoms", "Requires systematic evaluation"]
        
        return features[:4]
    
    def _get_condition_features_dict(self, condition: str) -> dict:
        """Get key distinguishing features for a condition as dictionary"""
        condition_lower = condition.lower()
        
        features_map = {
            'huntington': {
                'Inheritance': 'Autosomal dominant',
                'Age of Onset': '30-50 years typically',
                'Key Movement': 'Chorea (dance-like)',
                'Cognitive': 'Subcortical dementia',
                'Psychiatric': 'Depression, psychosis'
            },
            'chorea-acanthocytosis': {
                'Inheritance': 'Autosomal recessive',
                'Age of Onset': '20-40 years',
                'Key Movement': 'Chorea + orofacial dyskinesias',
                'Laboratory': 'Acanthocytes on blood smear',
                'Neuropathy': 'Axonal polyneuropathy'
            },
            'medication overuse': {
                'Frequency': '≥15 days/month',
                'Duration': '>3 months overuse',
                'Pattern': 'Transformation from episodic',
                'Key Feature': 'Paradoxical worsening',
                'Treatment': 'Medication withdrawal'
            }
        }
        
        for key, features in features_map.items():
            if key in condition_lower:
                return features
        
        # Default features
        return {
            'Clinical Pattern': 'Variable presentation',
            'Diagnosis': 'Based on clinical criteria',
            'Treatment': 'Condition-specific'
        }
    
    def _get_diagnostic_approach(self, condition: str) -> dict:
        """Get diagnostic approach for a condition"""
        condition_lower = condition.lower()
        
        diagnostic_map = {
            'huntington': {
                'primary_test': 'Genetic testing (HTT gene)',
                'confirmatory_test': 'CAG repeat analysis (≥36 repeats)',
                'key_sign': 'Milkmaid grip'
            },
            'chorea-acanthocytosis': {
                'primary_test': 'Fresh blood smear',
                'confirmatory_test': 'VPS13A gene sequencing',
                'key_sign': 'Tongue/lip biting'
            },
            'medication overuse': {
                'primary_test': 'Headache diary',
                'confirmatory_test': 'Withdrawal trial',
                'key_sign': '"Must take" medication daily'
            }
        }
        
        return diagnostic_map.get(next((k for k in diagnostic_map if k in condition_lower), ''), {
            'primary_test': 'Clinical evaluation',
            'confirmatory_test': 'Based on presentation',
            'key_sign': 'Condition-specific'
        })
    
    def _identify_comprehensive_knowledge_gaps(self, user_reasoning: str, mcq, is_correct: bool) -> List[str]:
        """Identify specific knowledge gaps with detailed descriptions"""
        gaps = []
        reasoning_lower = user_reasoning.lower()
        subspecialty = getattr(mcq, 'subspecialty', 'General Neurology')
        
        # Subspecialty-specific gap analysis
        if subspecialty == 'Movement Disorders':
            if not any(term in reasoning_lower for term in ['bradykinesia', 'rigidity', 'tremor', 'dystonia']):
                gaps.append("Movement disorder phenomenology: Understanding the core features of parkinsonism, dystonia, chorea, and other movement abnormalities")
            
            if not any(term in reasoning_lower for term in ['dopamine', 'basal ganglia', 'substantia nigra']):
                gaps.append("Movement disorder pathophysiology: Basal ganglia circuits, dopaminergic pathways, and neurotransmitter systems")
        
        elif subspecialty == 'Epilepsy':
            if not any(term in reasoning_lower for term in ['focal', 'generalized', 'seizure']):
                gaps.append("Seizure classification: Distinguishing focal vs. generalized seizures and their clinical implications")
        
        # General neurological reasoning gaps
        if len(user_reasoning) < 50:
            gaps.append("Clinical reasoning depth: Developing comprehensive analytical thinking that includes differential diagnosis and pathophysiological reasoning")
        
        if not is_correct and 'pathophysiology' not in reasoning_lower:
            gaps.append("Pathophysiological understanding: Connecting underlying disease mechanisms to clinical presentations")
        
        return gaps[:3]  # Limit to top 3 most important gaps
    
    def _identify_detailed_misconceptions(self, user_reasoning: str, mcq, user_answer: str, is_correct: bool) -> List[str]:
        """Identify specific misconceptions with corrections"""
        misconceptions = []
        reasoning_lower = user_reasoning.lower()
        
        if not is_correct:
            # Common neurological misconceptions
            if 'migraine' in reasoning_lower and 'movement' in getattr(mcq, 'subspecialty', '').lower():
                misconceptions.append("Confusion between headache disorders and movement disorders: Migraines cause headache with possible neurological symptoms, while movement disorders involve abnormal involuntary or voluntary movements")
            
            if 'stroke' in reasoning_lower and any(word in mcq.question_text.lower() for word in ['young', 'child', 'adolescent']):
                misconceptions.append("Overestimating stroke probability in young patients: While possible, metabolic, genetic, and inflammatory causes are more common in younger populations")
            
            # Add more specific misconceptions based on common errors
            correct_option = self._get_option_text(mcq, mcq.correct_answer)
            user_option = self._get_option_text(mcq, user_answer)
            
            if 'dystonia' in correct_option.lower() and 'spasm' in user_option.lower():
                misconceptions.append("Dystonia vs. muscle spasm confusion: Dystonia involves sustained muscle contractions causing twisting movements, while spasms are brief, involuntary contractions")
        
        return misconceptions[:2]  # Limit to top 2 most important misconceptions
    
    def _assess_detailed_reasoning_quality(self, user_reasoning: str, mcq, is_correct: bool) -> str:
        """Detailed assessment of reasoning quality"""
        reasoning_lower = user_reasoning.lower()
        length = len(user_reasoning)
        
        # Scoring criteria
        score = 0
        
        # Length and depth
        if length > 100: score += 1
        if length > 200: score += 1
        
        # Medical terminology
        medical_terms = ['pathophysiology', 'mechanism', 'differential', 'clinical', 'symptoms', 'signs']
        score += sum(1 for term in medical_terms if term in reasoning_lower)
        
        # Correct answer
        if is_correct: score += 2
        
        # Systematic thinking
        if any(word in reasoning_lower for word in ['first', 'then', 'consider', 'because']):
            score += 1
        
        # Quality assessment
        if score >= 7:
            return "excellent"
        elif score >= 5:
            return "good"
        elif score >= 3:
            return "fair"
        else:
            return "poor"

class ReasoningGuideGenerator:
    """Generates step-by-step reasoning guidance"""
    
    def __init__(self):
        self.cognitive_analyzer = CognitiveAnalyzer()
    
    def generate_guidance(self, mcq, user_answer: str, user_reasoning: str, is_correct: bool) -> List[GuideStep]:
        """
        Generate step-by-step guidance based on cognitive analysis
        
        Returns:
            List of GuideStep objects for progressive disclosure
        """
        analysis = self.cognitive_analyzer.analyze_reasoning(mcq, user_answer, user_reasoning, is_correct)
        
        steps = []
        
        # Step 1: Acknowledge and summarize
        steps.append(self._create_acknowledgment_step(analysis, is_correct))
        
        # Step 2: Identify the error pattern (if any)
        if analysis.primary_error:
            steps.append(self._create_error_identification_step(analysis.primary_error, user_reasoning))
        
        # Step 3: Address knowledge gaps
        if analysis.knowledge_gaps:
            steps.append(self._create_knowledge_building_step(analysis.knowledge_gaps, mcq))
        
        # Step 4: Correct misconceptions
        if analysis.misconceptions:
            steps.append(self._create_misconception_correction_step(analysis.misconceptions))
        
        # Step 5: Guide to correct reasoning
        steps.append(self._create_correct_reasoning_step(mcq, user_answer))
        
        # Step 6: Evidence-based conclusion
        steps.append(self._create_evidence_step(mcq))
        
        # Step 7: Learning reinforcement
        steps.append(self._create_reinforcement_step(mcq, analysis))
        
        return steps
    
    def _create_acknowledgment_step(self, analysis: CognitiveAnalysis, is_correct: bool) -> GuideStep:
        """Create the initial acknowledgment step"""
        if is_correct:
            content = f"""
            Great job! Your answer was correct and your reasoning shows {analysis.reasoning_quality} clinical thinking.
            
            Let's review your approach to reinforce the key concepts and ensure your reasoning process is optimized.
            """
        else:
            content = f"""
            Thank you for sharing your reasoning. While your answer wasn't correct this time, your thought process 
            provides valuable insights. Let's work through this together to strengthen your clinical reasoning.
            
            **Analysis Summary:** {analysis.analysis_summary}
            """
        
        return GuideStep(
            title="🎯 Understanding Your Clinical Reasoning",
            content=content
        )
    
    def _create_error_identification_step(self, error_type: CognitiveErrorType, user_reasoning: str) -> GuideStep:
        """Create step to identify and explain the cognitive error"""
        error_explanations = {
            CognitiveErrorType.ANCHORING_BIAS: {
                "title": "🎯 Anchoring Bias Detected",
                "explanation": "You may have anchored on the first piece of information and didn't fully consider alternatives.",
                "question": "What was the first thing that came to mind when you read this question?",
                "guidance": "Try to identify multiple possibilities before settling on your initial impression."
            },
            CognitiveErrorType.CONFIRMATION_BIAS: {
                "title": "🔍 Confirmation Bias Pattern",
                "explanation": "Your reasoning focused on information that supported your initial choice.",
                "question": "What evidence did you look for that contradicted your initial thought?",
                "guidance": "Always ask: 'What would make me wrong?' and actively seek disconfirming evidence."
            },
            CognitiveErrorType.AVAILABILITY_HEURISTIC: {
                "title": "💭 Availability Heuristic",
                "explanation": "You relied on easily recalled examples rather than systematic analysis.",
                "question": "Are you thinking of a specific case or pattern you've seen before?",
                "guidance": "Consider base rates and systematic diagnostic criteria, not just memorable cases."
            }
        }
        
        error_info = error_explanations.get(error_type, {
            "title": "🧠 Cognitive Pattern Identified",
            "explanation": "A specific thinking pattern influenced your reasoning process.",
            "question": "How did you arrive at your initial conclusion?",
            "guidance": "Let's examine your reasoning process step by step."
        })
        
        content = f"""
        **What happened:** {error_info['explanation']}
        
        This is a normal part of human thinking, but recognizing it helps us become better diagnosticians.
        
        **Reflection:** {error_info['guidance']}
        """
        
        return GuideStep(
            title=error_info['title'],
            content=content,
            question=error_info['question']
        )
    
    def _create_knowledge_building_step(self, knowledge_gaps: List[str], mcq) -> GuideStep:
        """Create step to address knowledge gaps"""
        content = f"""
        Let's build up the foundational knowledge needed for this question:
        
        **Key Knowledge Areas:**
        """
        
        for gap in knowledge_gaps[:3]:  # Limit to top 3 gaps
            content += f"\n• {gap}"
        
        subspecialty = getattr(mcq, 'subspecialty', 'neurology')
        content += f"""
        
        **Core {subspecialty} Concept:**
        Understanding the pathophysiology and clinical presentation is crucial for accurate diagnosis.
        """
        
        return GuideStep(
            title="📚 Building Foundation Knowledge",
            content=content,
            question="Which of these concepts would you like to explore first?"
        )
    
    def _create_misconception_correction_step(self, misconceptions: List[str]) -> GuideStep:
        """Create step to correct misconceptions"""
        content = """
        Let's address some common misconceptions that might have influenced your reasoning:
        
        """
        
        for i, misconception in enumerate(misconceptions[:2], 1):
            content += f"""
        **Misconception #{i}:** {misconception}
        
        **Correction:** This is a common misunderstanding. The evidence shows...
        """
        
        return GuideStep(
            title="⚠️ Correcting Common Misconceptions",
            content=content,
            action="Review the evidence-based guidelines on this topic"
        )
    
    def _create_correct_reasoning_step(self, mcq, user_answer: str) -> GuideStep:
        """Guide user through correct reasoning process"""
        correct_answer = getattr(mcq, 'correct_answer', 'A')
        
        content = f"""
        Now let's work through the systematic approach to this question:
        
        **Step 1: Identify the key clinical features**
        - What are the most important findings in this case?
        - Which findings are discriminating vs. non-specific?
        
        **Step 2: Generate a differential diagnosis**
        - What conditions could explain these findings?
        - Use a systematic approach (anatomical, pathophysiological, etc.)
        
        **Step 3: Apply diagnostic criteria**
        - What evidence supports or refutes each possibility?
        - Which diagnosis best fits all the clinical data?
        
        **The correct answer is {correct_answer}** because it best fits the systematic analysis.
        """
        
        return GuideStep(
            title="🔬 Systematic Clinical Reasoning",
            content=content,
            question="Can you now see why this systematic approach leads to the correct answer?"
        )
    
    def _create_evidence_step(self, mcq) -> GuideStep:
        """Present evidence-based support"""
        content = """
        **Evidence-Based Support:**
        
        Let's review the key evidence that supports this diagnosis:
        
        • **Clinical Guidelines:** Current recommendations from major neurology societies
        • **Research Evidence:** Recent studies and systematic reviews
        • **Pathophysiology:** Underlying mechanisms that explain the presentation
        
        This evidence-based approach ensures our clinical reasoning is grounded in the best available science.
        """
        
        return GuideStep(
            title="📊 Evidence-Based Foundation",
            content=content,
            evidence="Review current guidelines and research for this condition"
        )
    
    def _create_reinforcement_step(self, mcq, analysis: CognitiveAnalysis) -> GuideStep:
        """Create learning reinforcement step"""
        subspecialty = getattr(mcq, 'subspecialty', 'neurology')
        
        content = f"""
        **Key Learning Points:**
        
        1. **Cognitive Awareness:** Recognize when {analysis.primary_error.value.replace('_', ' ') if analysis.primary_error else 'biases'} might influence your thinking
        
        2. **Systematic Process:** Always use a structured approach to clinical reasoning
        
        3. **Evidence Integration:** Base decisions on current guidelines and research
        
        4. **{subspecialty} Mastery:** Continue building depth in this subspecialty area
        
        **Next Steps:**
        - Practice more {subspecialty} cases
        - Review current guidelines for this condition
        - Reflect on your reasoning process in future cases
        """
        
        return GuideStep(
            title="🎓 Learning Reinforcement",
            content=content,
            action="Apply these insights to your next clinical case"
        )
