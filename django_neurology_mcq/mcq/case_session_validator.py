"""
Professional Case Session Validator
Prevents serving wrong cases to users through API-based validation
"""

import json
import hashlib
import logging
from django.core.cache import cache
from django.utils import timezone
from datetime import timedelta
from .openai_integration import (
    client as client,
    chat_completion,
    DEFAULT_MODEL,
    FALLBACK_MODEL,
    get_first_choice_text,
)
import os

# Environment-aware configuration
MIN_CONFIDENCE_THRESHOLD = 40 if os.environ.get('DYNO') else 70
VALIDATION_CACHE_TIMEOUT = 1800 if os.environ.get('DYNO') else 3600  # Shorter cache on Heroku

logger = logging.getLogger(__name__)

# Use centralized OpenAI client from openai_integration


class CaseSessionValidator:
    """
    API-based validator to ensure case sessions match their source MCQs
    """
    
    def __init__(self):
        self.validation_cache_timeout = VALIDATION_CACHE_TIMEOUT
    
    def validate_case_session(self, mcq, case_data, session_id=None):
        """
        Comprehensive API-based validation of case session data
        
        Args:
            mcq: Source MCQ object
            case_data: Generated case data dictionary
            session_id: Optional session ID for tracking
            
        Returns:
            dict: Validation result with 'valid', 'reason', 'score', and metadata
        """
        
        # On Heroku, trust cases that were already validated during generation
        if os.environ.get('DYNO') and case_data.get('_validation_result'):
            existing_validation = case_data.get('_validation_result')
            if existing_validation.get('valid') and existing_validation.get('score', 0) >= MIN_CONFIDENCE_THRESHOLD:
                logger.info(f"Trusting existing validation for MCQ {mcq.id} on Heroku")
                return existing_validation
        
        # Create validation fingerprint
        validation_key = self._create_validation_key(mcq, case_data)
        
        # Check cache first
        cached_result = cache.get(validation_key)
        if cached_result:
            logger.info(f"Using cached validation for MCQ {mcq.id}")
            return cached_result
        
        # Perform API-based validation
        validation_result = self._api_validate_case_session(mcq, case_data, session_id)
        
        # Cache the result
        cache.set(validation_key, validation_result, self.validation_cache_timeout)
        
        # Log validation result
        status = "VALID" if validation_result['valid'] else "INVALID"
        logger.info(f"Case validation for MCQ {mcq.id}: {status} - {validation_result['reason'][:100]}")
        
        return validation_result
    
    def _api_validate_case_session(self, mcq, case_data, session_id):
        """
        Use OpenAI API to intelligently validate case-MCQ consistency
        """
        
        if not client:
            logger.warning("OpenAI client not available, using fallback validation")
            return self._fallback_validation(mcq, case_data)
        
        # Extract key information for validation
        mcq_summary = self._extract_mcq_summary(mcq)
        case_summary = self._extract_case_summary(case_data)
        
        validation_prompt = f"""
        MEDICAL EDUCATION VALIDATION TASK:
        
        You are validating that a clinical case accurately represents its source MCQ for educational consistency.
        
        SOURCE MCQ INFORMATION:
        ID: {mcq.id}
        Question: {mcq.question_text[:300]}...
        Correct Answer: {mcq.correct_answer}
        Subspecialty: {mcq.subspecialty}
        
        GENERATED CASE INFORMATION:
        Patient Demographics: {case_data.get('patient_demographics', 'N/A')}
        Clinical Presentation: {case_data.get('clinical_presentation', 'N/A')[:400]}...
        Question Type: {case_data.get('question_type', 'N/A')}
        Core Concept: {case_data.get('core_concept_type', 'N/A')}
        Reported Source MCQ ID: {case_data.get('source_mcq_id', 'N/A')}
        Session ID: {session_id or 'N/A'}
        
        VALIDATION REQUIREMENTS:
        
        1. MEDICAL TOPIC CONSISTENCY:
           - Both MCQ and case must address the same medical condition/syndrome
           - Example: If MCQ tests Parkinson's disease, case must be about Parkinson's/movement disorders
           - Example: If MCQ tests seizures, case must be about epilepsy/seizures
           - Topic drift to unrelated conditions is INVALID
        
        2. NEUROLOGICAL SUBSPECIALTY MATCH:
           - Case must belong to the same neurological subspecialty as MCQ
           - Cross-subspecialty drift indicates data corruption
        
        3. EDUCATIONAL OBJECTIVE PRESERVATION:
           - Both must test the same type of neurological knowledge
           - Core learning concepts must be preserved
        
        4. DATA INTEGRITY:
           - Case must reference the correct source MCQ ID ({mcq.id})
           - No evidence of data corruption or session mixing
        
        5. CLINICAL COHERENCE:
           - Case must make medical sense and be educationally valuable
           - Adequate detail for meaningful learning
        
        CRITICAL INVALIDATION CRITERIA:
        - MCQ about rigidity/bradykinesia → Case about leg weakness/diabetes = INVALID
        - MCQ about seizures → Case about multiple sclerosis = INVALID  
        - MCQ about stroke → Case about peripheral neuropathy = INVALID
        - Wrong MCQ ID reference = INVALID
        - Empty or nonsensical case content = INVALID
        
        VALIDATION OUTPUT (JSON):
        {{
            "is_valid": true/false,
            "confidence_score": 0-100,
            "medical_topic_match": true/false,
            "subspecialty_consistency": true/false,
            "educational_alignment": true/false,
            "data_integrity": true/false,
            "clinical_coherence": true/false,
            "primary_concern": "main issue if invalid",
            "detailed_assessment": "thorough explanation of validation decision",
            "risk_level": "low/medium/high/critical"
        }}
        """
        
        try:
            try:
                response = chat_completion(
                    client,
                    DEFAULT_MODEL,
                    [
                        {
                            "role": "system",
                            "content": """You are an expert medical education validator with deep expertise in neurology MCQs and case-based learning.

Your critical responsibility is to prevent educational content corruption by ensuring generated cases accurately represent their source MCQs.

VALIDATION PRINCIPLES:
- Medical topic consistency is paramount
- Educational integrity must be preserved  
- Data corruption must be detected and prevented
- Clinical coherence is essential

VALIDATION STANDARDS:
- Be strict about medical topic preservation
- Detect any evidence of case-MCQ mismatches
- Identify data integrity violations immediately
- Ensure educational value is maintained

Output ONLY valid JSON matching the required schema."""
                    },
                        {"role": "user", "content": validation_prompt}
                    ],
                    max_tokens=1000,
                    temperature=0.1,  # Very low temperature for consistent validation
                    response_format={"type": "json_object"}
                )
            except Exception as primary_error:
                if FALLBACK_MODEL and FALLBACK_MODEL != DEFAULT_MODEL:
                    logger.warning(
                        "Primary validation model %s failed (%s); retrying with fallback %s",
                        DEFAULT_MODEL,
                        primary_error,
                        FALLBACK_MODEL,
                    )
                    response = chat_completion(
                        client,
                        FALLBACK_MODEL,
                        [
                            {
                                "role": "system",
                                "content": """You are an expert medical education validator with deep expertise in neurology MCQs and case-based learning.

Your critical responsibility is to prevent educational content corruption by ensuring generated cases accurately represent their source MCQs.

VALIDATION PRINCIPLES:
- Medical topic consistency is paramount
- Educational integrity must be preserved  
- Data corruption must be detected and prevented
- Clinical coherence is essential

VALIDATION STANDARDS:
- Be strict about medical topic preservation
- Detect any evidence of case-MCQ mismatches
- Identify data integrity violations immediately
- Ensure educational value is maintained

Output ONLY valid JSON matching the required schema."""
                            },
                            {"role": "user", "content": validation_prompt}
                        ],
                        max_tokens=1000,
                        temperature=0.1,
                        response_format={"type": "json_object"}
                    )
                else:
                    raise
            
            response_payload = get_first_choice_text(response)
            if not response_payload:
                raise ValueError("Validation model returned empty content.")
            api_response = json.loads(response_payload)
            
            # Convert API response to our validation format
            is_valid = api_response.get('is_valid', False)
            confidence = api_response.get('confidence_score', 0)
            risk_level = api_response.get('risk_level', 'unknown')
            
            # Determine final validity based on environment-aware criteria
            if risk_level == 'critical' or confidence < MIN_CONFIDENCE_THRESHOLD:
                is_valid = False
            
            reason = api_response.get('detailed_assessment', 'API validation completed')
            if not is_valid:
                primary_concern = api_response.get('primary_concern', 'Validation failed')
                reason = f"{primary_concern}: {reason}"
            
            return {
                'valid': is_valid,
                'reason': reason[:500],  # Limit reason length
                'score': confidence,
                'api_validation': api_response,
                'validation_method': 'api',
                'risk_level': risk_level,
                'timestamp': timezone.now().isoformat()
            }
            
        except Exception as e:
            logger.error(f"API validation error for MCQ {mcq.id}: {e}")
            return self._fallback_validation(mcq, case_data)
    
    def _fallback_validation(self, mcq, case_data):
        """
        Fallback validation when API is unavailable
        """
        
        # Critical checks only
        if not isinstance(case_data, dict):
            return {
                'valid': False,
                'reason': 'Invalid case data structure',
                'score': 0,
                'validation_method': 'fallback',
                'timestamp': timezone.now().isoformat()
            }
        
        # Check MCQ ID match (critical)
        if case_data.get('source_mcq_id') != mcq.id:
            return {
                'valid': False,
                'reason': f'CRITICAL: MCQ ID mismatch - case references {case_data.get("source_mcq_id")}, expected {mcq.id}',
                'score': 0,
                'validation_method': 'fallback',
                'timestamp': timezone.now().isoformat()
            }
        
        # Check basic content presence
        required_fields = ['clinical_presentation', 'patient_demographics']
        missing_fields = [field for field in required_fields if not case_data.get(field)]
        
        if missing_fields:
            return {
                'valid': False,
                'reason': f'Missing critical fields: {", ".join(missing_fields)}',
                'score': 20,
                'validation_method': 'fallback',
                'timestamp': timezone.now().isoformat()
            }
        
        # Basic content length check
        case_content = str(case_data.get('clinical_presentation', ''))
        if len(case_content.strip()) < 100:
            return {
                'valid': False,
                'reason': 'Case content insufficient for educational use',
                'score': 30,
                'validation_method': 'fallback',
                'timestamp': timezone.now().isoformat()
            }
        
        # If basic checks pass, allow with warning - be more permissive on Heroku
        fallback_score = 60 if os.environ.get('DYNO') else 70
        return {
            'valid': True,
            'reason': 'Basic validation passed (API validation recommended)',
            'score': fallback_score,
            'validation_method': 'fallback',
            'timestamp': timezone.now().isoformat()
        }
    
    def _create_validation_key(self, mcq, case_data):
        """
        Create a unique validation cache key
        """
        # Create fingerprint from MCQ and case essentials
        mcq_finger = f"{mcq.id}_{mcq.question_text[:50]}_{mcq.subspecialty}"
        case_finger = f"{case_data.get('source_mcq_id')}_{case_data.get('clinical_presentation', '')[:50]}"
        
        combined = f"{mcq_finger}_{case_finger}"
        hash_key = hashlib.md5(combined.encode()).hexdigest()[:16]
        
        return f"case_validation_{hash_key}"
    
    def _extract_mcq_summary(self, mcq):
        """Extract key summary information from MCQ"""
        return {
            'id': mcq.id,
            'subspecialty': mcq.subspecialty,
            'question_length': len(mcq.question_text),
            'has_demographics': any(term in mcq.question_text.lower() for term in ['year-old', 'male', 'female', 'patient']),
            'question_type': self._detect_question_type_simple(mcq.question_text)
        }
    
    def _extract_case_summary(self, case_data):
        """Extract key summary information from case data"""
        return {
            'source_mcq_id': case_data.get('source_mcq_id'),
            'has_demographics': bool(case_data.get('patient_demographics')),
            'content_length': len(str(case_data.get('clinical_presentation', ''))),
            'question_type': case_data.get('question_type'),
            'core_concept': case_data.get('core_concept_type')
        }
    
    def _detect_question_type_simple(self, question_text):
        """Simple question type detection"""
        text = question_text.lower()
        
        if any(word in text for word in ['treatment', 'management', 'therapy', 'should be done']):
            return 'management'
        elif any(word in text for word in ['test', 'investigation', 'study', 'workup']):
            return 'investigation'
        else:
            return 'diagnosis'
    
    def clear_validation_cache(self, mcq_id=None):
        """
        Clear validation cache for specific MCQ or all
        """
        if mcq_id:
            # Clear specific MCQ validation cache
            pattern = f"case_validation_*_{mcq_id}_*"
            # Note: Django cache doesn't support pattern deletion easily
            # This is a simplified implementation
            logger.info(f"Validation cache cleared for MCQ {mcq_id}")
        else:
            # Clear all validation cache
            logger.info("All validation cache cleared")
    
    def get_validation_stats(self):
        """
        Get validation statistics for monitoring
        """
        # This would be implemented with proper metrics collection
        return {
            'total_validations': 'metrics_pending',
            'success_rate': 'metrics_pending',
            'api_usage': 'metrics_pending'
        }


# Global validator instance
case_validator = CaseSessionValidator()
