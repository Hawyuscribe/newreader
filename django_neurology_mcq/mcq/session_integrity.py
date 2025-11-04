"""
Session Integrity Checker
Prevents serving wrong case data to users through comprehensive validation
"""

import json
import logging
from django.core.cache import cache
from django.utils import timezone
from .case_session_validator import case_validator
from .models import MCQ, MCQCaseConversionSession

logger = logging.getLogger(__name__)


class SessionIntegrityChecker:
    """
    Ensures case sessions maintain integrity and prevent data corruption
    """
    
    def __init__(self):
        self.integrity_cache_timeout = 1800  # 30 minutes
    
    def validate_session_integrity(self, session, mcq, user=None):
        """
        Comprehensive session integrity validation
        
        Args:
            session: MCQCaseConversionSession object
            mcq: Source MCQ object
            user: Optional user for additional checks
            
        Returns:
            dict: Integrity validation result
        """
        
        integrity_issues = []
        integrity_score = 100
        
        # 1. Basic session validation
        if not session or not session.is_ready():
            return {
                'valid': False,
                'reason': 'Session not ready or invalid',
                'score': 0,
                'issues': ['session_not_ready']
            }
        
        # 2. MCQ reference validation
        if session.mcq_id != mcq.id:
            integrity_issues.append('mcq_id_mismatch')
            integrity_score -= 50
            logger.error(f"Session MCQ mismatch: session.mcq_id={session.mcq_id}, mcq.id={mcq.id}")
        
        # 3. Case data validation
        if not session.case_data or not isinstance(session.case_data, dict):
            integrity_issues.append('invalid_case_data')
            integrity_score -= 40
        else:
            # Validate case data references correct MCQ
            case_mcq_id = session.case_data.get('source_mcq_id')
            if case_mcq_id != mcq.id:
                integrity_issues.append('case_data_mcq_mismatch')
                integrity_score -= 50
                logger.error(f"Case data MCQ mismatch: case_mcq_id={case_mcq_id}, mcq.id={mcq.id}")
        
        # 4. User validation (if provided)
        if user and session.user_id != user.id:
            integrity_issues.append('user_mismatch')
            integrity_score -= 30
        
        # 5. Professional case validation using API
        if session.case_data and integrity_score > 50:
            try:
                case_validation = case_validator.validate_case_session(
                    mcq, 
                    session.case_data, 
                    session_id=session.id
                )
                
                if not case_validation['valid']:
                    integrity_issues.append('case_content_invalid')
                    integrity_score -= 40
                    logger.warning(f"Case content validation failed for session {session.id}: {case_validation['reason']}")
                elif case_validation.get('risk_level') in ['high', 'critical']:
                    integrity_issues.append('high_risk_content')
                    integrity_score -= 20
                    
            except Exception as e:
                logger.error(f"Case validation error for session {session.id}: {e}")
                integrity_issues.append('validation_error')
                integrity_score -= 10
        
        # 6. Session age validation
        if session.created_at:
            hours_old = (timezone.now() - session.created_at).total_seconds() / 3600
            if hours_old > 24:  # Sessions older than 24 hours are suspicious
                integrity_issues.append('session_too_old')
                integrity_score -= 15
        
        # 7. Data corruption indicators
        corruption_indicators = self._check_corruption_indicators(session, mcq)
        if corruption_indicators:
            integrity_issues.extend(corruption_indicators)
            integrity_score -= 10 * len(corruption_indicators)
        
        # Determine overall validity
        is_valid = integrity_score >= 70 and 'mcq_id_mismatch' not in integrity_issues and 'case_data_mcq_mismatch' not in integrity_issues
        
        # Generate reason
        if is_valid:
            reason = f"Session integrity validated (score: {integrity_score})"
        else:
            critical_issues = [issue for issue in integrity_issues if 'mismatch' in issue or 'invalid' in issue]
            reason = f"Integrity compromised: {', '.join(critical_issues[:3])}"
        
        result = {
            'valid': is_valid,
            'reason': reason,
            'score': max(0, integrity_score),
            'issues': integrity_issues,
            'timestamp': timezone.now().isoformat()
        }
        
        # Log integrity check result
        status = "VALID" if is_valid else "COMPROMISED"
        logger.info(f"Session {session.id} integrity: {status} - Score: {integrity_score}")
        
        return result
    
    def _check_corruption_indicators(self, session, mcq):
        """
        Check for data corruption indicators
        """
        indicators = []
        
        if not session.case_data:
            return indicators
        
        # Check for placeholder or template content
        case_text = str(session.case_data.get('clinical_presentation', '')).lower()
        
        corruption_patterns = [
            'lorem ipsum',
            'placeholder text',
            'sample case',
            'template case',
            'xxx',
            '[insert',
            'todo:',
            'fixme:'
        ]
        
        for pattern in corruption_patterns:
            if pattern in case_text:
                indicators.append('template_content_detected')
                break
        
        # Check for extremely short content
        if len(case_text.strip()) < 50:
            indicators.append('insufficient_content')
        
        # Check for missing critical fields
        required_fields = ['clinical_presentation', 'patient_demographics', 'question_prompt']
        missing_fields = [field for field in required_fields if not session.case_data.get(field)]
        if missing_fields:
            indicators.append('missing_critical_fields')
        
        # Check for validation metadata
        if not session.case_data.get('professional_validation', {}).get('passed'):
            indicators.append('no_validation_metadata')
        
        return indicators
    
    def ensure_session_integrity(self, session_id, mcq_id, user_id=None):
        """
        High-level function to ensure session integrity before serving to user
        
        Args:
            session_id: Session ID to validate
            mcq_id: Expected MCQ ID
            user_id: Expected user ID
            
        Returns:
            tuple: (is_valid, session_object, error_message)
        """
        
        try:
            # Get session and MCQ objects
            session = MCQCaseConversionSession.objects.select_related('mcq', 'user').get(id=session_id)
            mcq = MCQ.objects.get(id=mcq_id)
            
        except MCQCaseConversionSession.DoesNotExist:
            return False, None, "Session not found"
        except MCQ.DoesNotExist:
            return False, None, "MCQ not found"
        except Exception as e:
            logger.error(f"Error retrieving session/MCQ: {e}")
            return False, None, "Database error"
        
        # Validate user if provided
        if user_id and session.user_id != user_id:
            logger.warning(f"User mismatch for session {session_id}: expected {user_id}, got {session.user_id}")
            return False, None, "Session belongs to different user"
        
        # Perform comprehensive integrity validation
        integrity_result = self.validate_session_integrity(session, mcq)
        
        if not integrity_result['valid']:
            # Log the integrity failure
            logger.error(f"Session integrity failed for session {session_id}: {integrity_result['reason']}")
            
            # For critical failures, invalidate the session
            if any(issue in integrity_result['issues'] for issue in ['mcq_id_mismatch', 'case_data_mcq_mismatch']):
                self._invalidate_session(session)
                return False, None, f"Critical integrity failure: {integrity_result['reason']}"
            
            return False, session, f"Integrity validation failed: {integrity_result['reason']}"
        
        # Session is valid
        logger.info(f"Session {session_id} integrity validated successfully")
        return True, session, None
    
    def _invalidate_session(self, session):
        """
        Invalidate a compromised session
        """
        try:
            session.status = 'failed'
            session.error_message = f"Session invalidated due to integrity failure at {timezone.now()}"
            session.save()
            
            # Clear related caches
            cache_keys = [
                f"mcq_case_conversion_{session.mcq_id}_v427_validated",
                f"case_session_{session.id}",
                f"user_case_session_{session.user_id}_{session.mcq_id}"
            ]
            
            for key in cache_keys:
                cache.delete(key)
            
            logger.info(f"Session {session.id} invalidated and caches cleared")
            
        except Exception as e:
            logger.error(f"Error invalidating session {session.id}: {e}")
    
    def clear_integrity_cache(self, session_id=None):
        """
        Clear integrity validation cache
        """
        if session_id:
            # Clear specific session cache
            cache.delete(f"integrity_check_{session_id}")
        else:
            # This would clear all integrity caches in a production system
            logger.info("Integrity cache clear requested")
    
    def get_integrity_statistics(self):
        """
        Get integrity validation statistics for monitoring
        """
        # In a production system, this would return real metrics
        return {
            'total_checks': 'metrics_pending',
            'integrity_rate': 'metrics_pending',
            'common_issues': 'metrics_pending'
        }


# Global integrity checker instance
session_integrity = SessionIntegrityChecker()