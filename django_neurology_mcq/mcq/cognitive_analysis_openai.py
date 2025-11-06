"""
OpenAI-powered Cognitive Analysis Engine for Clinical Reasoning
Replaces rule-based system with GPT-4.1 mini for sophisticated medical education feedback
"""

import json
import logging
import re
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum

from .openai_integration import client as openai_client, chat_completion, FALLBACK_MODEL
from .clinical_reasoning_prompt import (
    create_clinical_reasoning_prompt,
    FEW_SHOT_EXAMPLES,
    OPENAI_CONFIG
)
from .guideline_context import build_guideline_context

logger = logging.getLogger(__name__)


class CognitiveErrorType(Enum):
    """Types of cognitive errors in medical reasoning"""
    ANCHORING_BIAS = "anchoring_bias"
    CONFIRMATION_BIAS = "confirmation_bias"
    AVAILABILITY_HEURISTIC = "availability_heuristic"
    PREMATURE_CLOSURE = "premature_closure"
    KNOWLEDGE_GAP = "knowledge_gap"
    MISCONCEPTION = "misconception"


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


class CognitiveAnalyzerOpenAI:
    """
    OpenAI-powered analyzer for medical reasoning using GPT-4.1 mini
    Provides sophisticated, context-aware clinical reasoning feedback
    """
    
    def __init__(self):
        """Initialize with OpenAI client"""
        self.client = openai_client
        if not self.client:
            logger.error("Failed to initialize OpenAI client for cognitive analysis")
            raise ValueError("OpenAI client not available")
    
    def analyze_reasoning(self, mcq, user_answer: str, user_reasoning: str, is_correct: bool) -> CognitiveAnalysis:
        """
        Analyze user's clinical reasoning using OpenAI GPT-4.1 mini
        
        Args:
            mcq: MCQ object with question and options
            user_answer: User's selected answer
            user_reasoning: User's reasoning explanation
            is_correct: Whether the answer was correct
            
        Returns:
            CognitiveAnalysis object with AI-generated feedback
        """
        try:
            # Prepare MCQ data for the prompt
            mcq_data = self._prepare_mcq_data(mcq, user_answer)
            user_data = {
                'selected_answer': user_answer,
                'reasoning': user_reasoning,
                'is_correct': is_correct
            }
            
            # Create the prompt
            system_prompt, user_prompt = create_clinical_reasoning_prompt(mcq_data, user_data)
            
            # Build messages (lean; no few-shot for efficiency)
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
            
            # Make API call to OpenAI
            logger.info(f"Calling OpenAI for clinical reasoning analysis (MCQ {mcq.id})")
            
            response = chat_completion(
                self.client,
                OPENAI_CONFIG["model"],
                messages,
                temperature=OPENAI_CONFIG["temperature"],
                max_tokens=OPENAI_CONFIG["max_tokens"],
                top_p=OPENAI_CONFIG["top_p"],
                frequency_penalty=OPENAI_CONFIG["frequency_penalty"],
                presence_penalty=OPENAI_CONFIG["presence_penalty"],
                timeout=90  # allow longer generations for full structured output
            )
            
            # Extract the analysis
            ai_analysis = ''
            try:
                ai_analysis = response.choices[0].message.content or ''
            except Exception:
                ai_analysis = ''
            if not ai_analysis or not str(ai_analysis).strip():
                # One concise retry; prefer a different model if GPT‑5 returned empty
                try:
                    logger.info("Empty analysis; retrying with minimal teaching prompt")
                    minimal_system = (
                        "You are a neurologist educator. Return HTML only (no preamble). "
                        "Give a one-paragraph verdict, then 4–6 bullets with key distinguishers and teaching points. "
                        "Aim for 180–250 words."
                    )
                    minimal_user = user_prompt
                    # Use fallback mini model if the primary is a GPT‑5 variant
                    retry_model = FALLBACK_MODEL if str(OPENAI_CONFIG["model"]).startswith("gpt-5") else OPENAI_CONFIG["model"]
                    resp2 = chat_completion(
                        self.client,
                        retry_model,
                        [
                            {"role": "system", "content": minimal_system},
                            {"role": "user", "content": minimal_user},
                        ],
                        max_tokens=min(OPENAI_CONFIG["max_tokens"], 900),
                        temperature=OPENAI_CONFIG["temperature"] if not str(retry_model).startswith("gpt-5") else None,
                        top_p=OPENAI_CONFIG["top_p"] if not str(retry_model).startswith("gpt-5") else None,
                        timeout=45,
                    )
                    alt = ''
                    try:
                        alt = resp2.choices[0].message.content or ''
                    except Exception:
                        alt = ''
                    if alt.strip():
                        ai_analysis = alt
                except Exception:
                    pass
            if not ai_analysis or not str(ai_analysis).strip():
                logger.warning(f"OpenAI returned empty analysis for MCQ {mcq.id}; using fallback analysis")
                return self._create_fallback_analysis(mcq, user_answer, user_reasoning, is_correct)
            logger.info(f"Received AI analysis for MCQ {mcq.id}, length: {len(ai_analysis)}")
            
            # Parse cognitive errors from the response
            cognitive_errors = self._extract_cognitive_errors(ai_analysis, is_correct)
            
            # Determine reasoning quality based on AI feedback
            reasoning_quality = self._assess_reasoning_quality(ai_analysis, is_correct)
            
            # Calculate confidence level
            confidence_level = self._calculate_confidence_level(is_correct, reasoning_quality)
            
            return CognitiveAnalysis(
                primary_error=cognitive_errors[0] if cognitive_errors else None,
                secondary_errors=cognitive_errors[1:],
                knowledge_gaps=self._extract_knowledge_gaps(ai_analysis),
                misconceptions=self._extract_misconceptions(ai_analysis),
                reasoning_quality=reasoning_quality,
                confidence_level=confidence_level,
                analysis_summary=self._format_analysis_html(ai_analysis)
            )
            
        except Exception as e:
            logger.error(f"Error in OpenAI cognitive analysis: {e}", exc_info=True)
            # Fallback to basic analysis
            return self._create_fallback_analysis(mcq, user_answer, user_reasoning, is_correct)
    
    def _prepare_mcq_data(self, mcq, user_answer: str) -> Dict:
        """Prepare MCQ data for the prompt"""
        options = mcq.get_options_dict()
        # Build guideline context generically from existing MCQ content only
        try:
            guideline_ctx = build_guideline_context(
                mcq.question_text,
                list(options.values()),
                getattr(mcq, 'explanation_sections', None),
                getattr(mcq, 'explanation', None)
            )
        except Exception:
            guideline_ctx = ""

        return {
            'question': mcq.question_text,
            'options': options,
            'correct_answer': mcq.correct_answer,
            'correct_answer_text': options.get(mcq.correct_answer, ''),
            'selected_answer_text': options.get(user_answer, ''),
            'explanation': getattr(mcq, 'explanation', ''),
            'guideline_context': guideline_ctx
        }
    
    def _extract_cognitive_errors(self, ai_analysis: str, is_correct: bool) -> List[CognitiveErrorType]:
        """Extract cognitive errors mentioned in AI analysis"""
        errors = []
        analysis_lower = ai_analysis.lower()
        
        error_patterns = {
            CognitiveErrorType.ANCHORING_BIAS: ['anchoring', 'fixated', 'premature conclusion'],
            CognitiveErrorType.CONFIRMATION_BIAS: ['confirmation bias', 'selective attention'],
            CognitiveErrorType.AVAILABILITY_HEURISTIC: ['availability', 'recent case', 'common presentation'],
            CognitiveErrorType.PREMATURE_CLOSURE: ['premature closure', 'stopped thinking', 'didn\'t consider'],
            CognitiveErrorType.KNOWLEDGE_GAP: ['knowledge gap', 'didn\'t know', 'unfamiliar with'],
            CognitiveErrorType.MISCONCEPTION: ['misconception', 'incorrect understanding', 'misunderstood']
        }
        
        for error_type, patterns in error_patterns.items():
            if any(pattern in analysis_lower for pattern in patterns):
                errors.append(error_type)
        
        # If incorrect but no specific errors identified, assume knowledge gap
        if not is_correct and not errors:
            errors.append(CognitiveErrorType.KNOWLEDGE_GAP)
        
        return errors
    
    def _extract_knowledge_gaps(self, ai_analysis: str) -> List[str]:
        """Extract specific knowledge gaps from AI analysis"""
        gaps = []
        
        # Look for specific mentions of gaps or areas to review
        gap_patterns = [
            r'should review (.+?)(?:\.|,)',
            r'gap in understanding of (.+?)(?:\.|,)',
            r'need to strengthen knowledge of (.+?)(?:\.|,)',
            r'important to understand (.+?)(?:\.|,)'
        ]
        
        for pattern in gap_patterns:
            matches = re.findall(pattern, ai_analysis, re.IGNORECASE)
            gaps.extend(matches)
        
        # Clean and deduplicate
        gaps = list(set(gap.strip() for gap in gaps if len(gap.strip()) > 10))[:3]
        
        return gaps
    
    def _extract_misconceptions(self, ai_analysis: str) -> List[str]:
        """Extract misconceptions from AI analysis"""
        misconceptions = []
        
        patterns = [
            r'misconception that (.+?)(?:\.|,)',
            r'incorrectly assumed (.+?)(?:\.|,)',
            r'mistaken belief that (.+?)(?:\.|,)'
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, ai_analysis, re.IGNORECASE)
            misconceptions.extend(matches)
        
        return list(set(m.strip() for m in misconceptions if len(m.strip()) > 10))[:3]
    
    def _assess_reasoning_quality(self, ai_analysis: str, is_correct: bool) -> str:
        """Assess overall reasoning quality from AI feedback"""
        analysis_lower = ai_analysis.lower()
        
        if is_correct:
            if any(term in analysis_lower for term in ['excellent', 'comprehensive', 'thorough', 'strong']):
                return 'excellent'
            elif any(term in analysis_lower for term in ['good', 'sound', 'appropriate']):
                return 'good'
            else:
                return 'fair'
        else:
            if any(term in analysis_lower for term in ['significant gap', 'major error', 'fundamental']):
                return 'poor'
            else:
                return 'fair'
    
    def _calculate_confidence_level(self, is_correct: bool, reasoning_quality: str) -> float:
        """Calculate confidence level based on correctness and quality"""
        quality_scores = {
            'excellent': 0.9,
            'good': 0.75,
            'fair': 0.5,
            'poor': 0.25
        }
        
        base_score = quality_scores.get(reasoning_quality, 0.5)
        
        # Adjust based on correctness
        if is_correct:
            return min(base_score + 0.1, 1.0)
        else:
            return max(base_score - 0.1, 0.0)
    
    def _format_analysis_html(self, ai_analysis: str) -> str:
        """Format the AI analysis with proper HTML structure"""
        # The AI response should already include HTML formatting
        # Just wrap it in a container div
        formatted = f'<div class="clinical-reasoning-analysis ai-generated">\n{ai_analysis}\n</div>'
        
        # Ensure proper HTML structure
        formatted = self._clean_html_formatting(formatted)
        
        return formatted
    
    def _clean_html_formatting(self, html: str) -> str:
        """Clean and validate HTML formatting"""
        # Remove any markdown that might have slipped through
        html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
        html = re.sub(r'\*(.+?)\*', r'<em>\1</em>', html)
        
        # Ensure all paragraphs are properly closed
        html = re.sub(r'<p>([^<]+)(?!</p>)', r'<p>\1</p>', html)
        
        return html
    
    def _create_fallback_analysis(self, mcq, user_answer: str, user_reasoning: str, is_correct: bool) -> CognitiveAnalysis:
        """Create fallback analysis when OpenAI fails"""
        logger.warning("Using fallback analysis due to OpenAI error")
        
        if is_correct:
            summary = f"""<div class="clinical-reasoning-analysis">
<h3>Clinical Reasoning Analysis</h3>
<p><strong>Well done!</strong> You correctly identified {user_answer} as the answer.</p>
<p>Your reasoning shows clinical thinking. Continue to deepen your understanding of the neurological principles involved.</p>
<p><strong>Key Learning:</strong> Focus on the pathophysiological mechanisms and clinical correlations that support your correct diagnosis.</p>
</div>"""
        else:
            summary = f"""<div class="clinical-reasoning-analysis">
<h3>Clinical Reasoning Analysis</h3>
<p>You selected <strong>{user_answer}</strong>, but the correct answer was <strong>{mcq.correct_answer}</strong>.</p>
<p>Review the neuroanatomical and clinical features that distinguish these conditions.</p>
<p><strong>Learning Point:</strong> Systematic analysis of clinical presentations helps identify key distinguishing features between similar conditions.</p>
</div>"""
        
        return CognitiveAnalysis(
            primary_error=CognitiveErrorType.KNOWLEDGE_GAP if not is_correct else None,
            secondary_errors=[],
            knowledge_gaps=["Review the key distinguishing features for this topic"],
            misconceptions=[],
            reasoning_quality="fair",
            confidence_level=0.7 if is_correct else 0.4,
            analysis_summary=summary
        )


class ReasoningGuideGeneratorOpenAI:
    """Generates step-by-step reasoning guidance using OpenAI analysis"""
    
    def __init__(self):
        self.cognitive_analyzer = CognitiveAnalyzerOpenAI()
    
    def generate_guidance(self, mcq, user_answer: str, user_reasoning: str, is_correct: bool) -> List[GuideStep]:
        """Generate guidance steps based on AI analysis"""
        analysis = self.cognitive_analyzer.analyze_reasoning(mcq, user_answer, user_reasoning, is_correct)
        return self.generate_guidance_from_analysis(analysis)
    
    def generate_guidance_from_analysis(self, analysis: CognitiveAnalysis) -> List[GuideStep]:
        """Generate guidance steps from existing analysis (avoids duplicate API calls)"""
        steps = []
        
        # Step 1: Present the analysis
        steps.append(GuideStep(
            title="🎯 Clinical Reasoning Analysis",
            content=analysis.analysis_summary,
            question=None,
            evidence=None,
            action=None
        ))
        
        # Additional steps can be added based on the analysis
        if analysis.knowledge_gaps:
            steps.append(GuideStep(
                title="📚 Areas for Review",
                content=self._format_knowledge_gaps(analysis.knowledge_gaps),
                action="Review these topics to strengthen your clinical reasoning"
            ))
        
        if analysis.primary_error:
            steps.append(GuideStep(
                title="🔍 Reasoning Pattern Analysis",
                content=self._format_cognitive_errors(analysis.primary_error, analysis.secondary_errors),
                action="Reflect on these patterns to improve diagnostic accuracy"
            ))
        
        return steps
    
    def _format_knowledge_gaps(self, gaps: List[str]) -> str:
        """Format knowledge gaps as HTML"""
        if not gaps:
            return "<p>Continue building on your current knowledge base.</p>"
        
        html = "<p>Consider reviewing these areas:</p><ul>"
        for gap in gaps:
            html += f"<li>{gap}</li>"
        html += "</ul>"
        
        return html
    
    def _format_cognitive_errors(self, primary: CognitiveErrorType, secondary: List[CognitiveErrorType]) -> str:
        """Format cognitive errors as educational feedback"""
        error_descriptions = {
            CognitiveErrorType.ANCHORING_BIAS: "Focusing too early on one diagnosis without considering alternatives",
            CognitiveErrorType.CONFIRMATION_BIAS: "Selectively interpreting information to support initial impression",
            CognitiveErrorType.AVAILABILITY_HEURISTIC: "Overweighting recent or memorable cases",
            CognitiveErrorType.PREMATURE_CLOSURE: "Accepting a diagnosis before verification",
            CognitiveErrorType.KNOWLEDGE_GAP: "Missing key medical knowledge for this topic",
            CognitiveErrorType.MISCONCEPTION: "Incorrect understanding of medical concepts"
        }
        
        html = f"<p><strong>Primary pattern identified:</strong> {error_descriptions.get(primary, 'Learning opportunity identified')}</p>"
        
        if secondary:
            html += "<p>Also consider:</p><ul>"
            for error in secondary:
                html += f"<li>{error_descriptions.get(error, error.value)}</li>"
            html += "</ul>"
        
        return html


# Alias for backward compatibility
CognitiveAnalyzer = CognitiveAnalyzerOpenAI
ReasoningGuideGenerator = ReasoningGuideGeneratorOpenAI
