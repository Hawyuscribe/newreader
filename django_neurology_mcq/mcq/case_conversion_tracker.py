"""
MCQ-to-Case Conversion Comprehensive Tracking System
Tracks every step from button click to case display to diagnose session mismatches
"""

import json
import logging
import time
from datetime import datetime
from django.core.cache import cache
from django.utils import timezone

logger = logging.getLogger(__name__)

class CaseConversionTracker:
    """
    Comprehensive tracking system for MCQ to case conversion
    Logs every step to help diagnose why wrong cases are displayed
    """
    
    def __init__(self):
        self.tracking_version = "v1.0_comprehensive_tracking"
    
    def start_conversion_tracking(self, mcq_id, user_id, request_source="button_click"):
        """
        Start tracking a new MCQ-to-case conversion
        
        Args:
            mcq_id: MCQ ID being converted
            user_id: User initiating conversion
            request_source: Source of the request (button_click, existing_session, etc.)
        
        Returns:
            str: Tracking ID for this conversion
        """
        tracking_id = f"track_{mcq_id}_{user_id}_{int(time.time())}"
        
        track_data = {
            'tracking_id': tracking_id,
            'mcq_id': mcq_id,
            'user_id': user_id,
            'request_source': request_source,
            'start_time': timezone.now().isoformat(),
            'steps': []
        }
        
        self._log_step(track_data, "TRACKING_START", {
            'message': f'Started tracking MCQ {mcq_id} conversion for user {user_id}',
            'source': request_source,
            'timestamp': timezone.now().isoformat()
        })
        
        # Store in cache for 2 hours
        cache.set(f"conversion_tracking_{tracking_id}", track_data, 7200)
        
        logger.info(f"🔍 TRACKING START: {tracking_id} - MCQ {mcq_id} for user {user_id}")
        
        return tracking_id
    
    def log_conversion_session_creation(self, tracking_id, session_id, session_fingerprint, mcq_content_hash):
        """
        Log creation of MCQCaseConversionSession
        """
        track_data = self._get_tracking_data(tracking_id)
        if not track_data:
            return
            
        self._log_step(track_data, "SESSION_CREATION", {
            'conversion_session_id': session_id,
            'session_fingerprint': session_fingerprint,
            'mcq_content_hash': mcq_content_hash,
            'message': f'Created conversion session {session_id}',
            'timestamp': timezone.now().isoformat()
        })
        
        self._save_tracking_data(tracking_id, track_data)
        logger.info(f"🔍 SESSION_CREATION: {tracking_id} - Session {session_id} created")
    
    def log_background_task_start(self, tracking_id, task_id, mcq_id, user_id):
        """
        Log background task initiation
        """
        track_data = self._get_tracking_data(tracking_id)
        if not track_data:
            return
            
        self._log_step(track_data, "BACKGROUND_TASK_START", {
            'task_id': task_id,
            'mcq_id': mcq_id,
            'user_id': user_id,
            'message': f'Background task {task_id} started for MCQ {mcq_id}',
            'timestamp': timezone.now().isoformat()
        })
        
        self._save_tracking_data(tracking_id, track_data)
        logger.info(f"🔍 BACKGROUND_TASK_START: {tracking_id} - Task {task_id}")
    
    def log_case_generation(self, tracking_id, case_data, api_call_details=None):
        """
        Log case generation with API details
        """
        track_data = self._get_tracking_data(tracking_id)
        if not track_data:
            return
            
        # Extract key case data for logging (avoid storing full case to save space)
        case_summary = {
            'source_mcq_id': case_data.get('source_mcq_id'),
            'patient_demographics': case_data.get('patient_demographics', '')[:100] + '...',
            'clinical_presentation_length': len(str(case_data.get('clinical_presentation', ''))),
            'question_type': case_data.get('question_type'),
            'has_integrity_metadata': '_integrity_metadata' in case_data
        }
        
        self._log_step(track_data, "CASE_GENERATION", {
            'case_summary': case_summary,
            'api_call_details': api_call_details,
            'message': f'Case generated for MCQ {case_data.get("source_mcq_id")}',
            'timestamp': timezone.now().isoformat()
        })
        
        self._save_tracking_data(tracking_id, track_data)
        logger.info(f"🔍 CASE_GENERATION: {tracking_id} - Generated for MCQ {case_data.get('source_mcq_id')}")
    
    def log_validation_result(self, tracking_id, validation_result, validator_type="case_validator"):
        """
        Log case validation results
        """
        track_data = self._get_tracking_data(tracking_id)
        if not track_data:
            return
            
        self._log_step(track_data, "CASE_VALIDATION", {
            'validator_type': validator_type,
            'validation_result': validation_result,
            'message': f'Case validation: {validation_result.get("valid", False)} - {validation_result.get("reason", "No reason")}',
            'timestamp': timezone.now().isoformat()
        })
        
        self._save_tracking_data(tracking_id, track_data)
        logger.info(f"🔍 CASE_VALIDATION: {tracking_id} - Valid: {validation_result.get('valid')}")
    
    def log_database_storage(self, tracking_id, session_id, storage_checksum):
        """
        Log database storage of case data
        """
        track_data = self._get_tracking_data(tracking_id)
        if not track_data:
            return
            
        self._log_step(track_data, "DATABASE_STORAGE", {
            'conversion_session_id': session_id,
            'storage_checksum': storage_checksum,
            'message': f'Case data stored in session {session_id}',
            'timestamp': timezone.now().isoformat()
        })
        
        self._save_tracking_data(tracking_id, track_data)
        logger.info(f"🔍 DATABASE_STORAGE: {tracking_id} - Stored in session {session_id}")
    
    def log_django_session_transfer(self, tracking_id, django_session_key, transfer_checksum, case_data_summary):
        """
        Log transfer to Django session
        """
        track_data = self._get_tracking_data(tracking_id)
        if not track_data:
            return
            
        self._log_step(track_data, "DJANGO_SESSION_TRANSFER", {
            'django_session_key': django_session_key,
            'transfer_checksum': transfer_checksum,
            'case_data_summary': case_data_summary,
            'message': f'Case data transferred to Django session: {django_session_key}',
            'timestamp': timezone.now().isoformat()
        })
        
        self._save_tracking_data(tracking_id, track_data)
        logger.info(f"🔍 DJANGO_SESSION_TRANSFER: {tracking_id} - Key: {django_session_key}")
    
    def log_frontend_response(self, tracking_id, response_data):
        """
        Log response sent to frontend
        """
        track_data = self._get_tracking_data(tracking_id)
        if not track_data:
            return
            
        # Clean response data for logging
        clean_response = {
            'success': response_data.get('success'),
            'status': response_data.get('status'),
            'session_id': response_data.get('session_id'),
            'session_key': response_data.get('session_key'),
            'message': response_data.get('message'),
            'has_case_data': 'case_data' in response_data
        }
        
        self._log_step(track_data, "FRONTEND_RESPONSE", {
            'response_data': clean_response,
            'message': f'Response sent to frontend: {clean_response["status"]}',
            'timestamp': timezone.now().isoformat()
        })
        
        self._save_tracking_data(tracking_id, track_data)
        logger.info(f"🔍 FRONTEND_RESPONSE: {tracking_id} - Status: {clean_response['status']}")
    
    def log_case_bot_request(self, tracking_id, session_id, mcq_case_data_received, user_id):
        """
        Log when case bot receives request with MCQ case data
        """
        track_data = self._get_tracking_data(tracking_id)
        if not track_data:
            # Create new tracking if not found (case bot might be called independently)
            track_data = {
                'tracking_id': tracking_id,
                'mcq_id': 'unknown',
                'user_id': user_id,
                'request_source': 'case_bot_direct',
                'start_time': timezone.now().isoformat(),
                'steps': []
            }
            
        case_data_summary = None
        if mcq_case_data_received and isinstance(mcq_case_data_received, dict):
            case_data_summary = {
                'source_mcq_id': mcq_case_data_received.get('source_mcq_id'),
                'question_type': mcq_case_data_received.get('question_type'),
                'has_clinical_presentation': bool(mcq_case_data_received.get('clinical_presentation')),
                'clinical_presentation_length': len(str(mcq_case_data_received.get('clinical_presentation', ''))),
                'has_patient_demographics': bool(mcq_case_data_received.get('patient_demographics'))
            }
            
        self._log_step(track_data, "CASE_BOT_REQUEST", {
            'session_id': session_id,
            'mcq_case_data_received': bool(mcq_case_data_received),
            'case_data_summary': case_data_summary,
            'user_id': user_id,
            'message': f'Case bot received request with session_id: {session_id}',
            'timestamp': timezone.now().isoformat()
        })
        
        self._save_tracking_data(tracking_id, track_data)
        logger.info(f"🔍 CASE_BOT_REQUEST: {tracking_id} - Session: {session_id}, MCQ data: {bool(mcq_case_data_received)}")
    
    def log_django_session_retrieval(self, tracking_id, session_id, session_found, session_data_summary):
        """
        Log Django session retrieval in case bot
        """
        track_data = self._get_tracking_data(tracking_id)
        if not track_data:
            return
            
        self._log_step(track_data, "DJANGO_SESSION_RETRIEVAL", {
            'session_id': session_id,
            'session_found': session_found,
            'session_data_summary': session_data_summary,
            'message': f'Django session retrieval: {session_id} - Found: {session_found}',
            'timestamp': timezone.now().isoformat()
        })
        
        self._save_tracking_data(tracking_id, track_data)
        logger.info(f"🔍 DJANGO_SESSION_RETRIEVAL: {tracking_id} - Found: {session_found}")
    
    def log_case_bot_response(self, tracking_id, bot_response_preview, is_mcq_case, actual_mcq_id):
        """
        Log case bot response generation
        """
        track_data = self._get_tracking_data(tracking_id)
        if not track_data:
            return
            
        self._log_step(track_data, "CASE_BOT_RESPONSE", {
            'bot_response_preview': bot_response_preview[:200] + '...' if len(bot_response_preview) > 200 else bot_response_preview,
            'is_mcq_case': is_mcq_case,
            'actual_mcq_id': actual_mcq_id,
            'message': f'Case bot generated response for MCQ case: {is_mcq_case}',
            'timestamp': timezone.now().isoformat()
        })
        
        self._save_tracking_data(tracking_id, track_data)
        logger.info(f"🔍 CASE_BOT_RESPONSE: {tracking_id} - MCQ case: {is_mcq_case}, MCQ ID: {actual_mcq_id}")
    
    def log_error(self, tracking_id, error_step, error_message, error_details=None):
        """
        Log any errors during conversion
        """
        track_data = self._get_tracking_data(tracking_id)
        if not track_data:
            return
            
        self._log_step(track_data, f"ERROR_{error_step}", {
            'error_message': error_message,
            'error_details': error_details,
            'message': f'Error in {error_step}: {error_message}',
            'timestamp': timezone.now().isoformat()
        })
        
        self._save_tracking_data(tracking_id, track_data)
        logger.error(f"🔍 ERROR_{error_step}: {tracking_id} - {error_message}")
    
    def get_tracking_report(self, tracking_id):
        """
        Get comprehensive tracking report
        """
        track_data = self._get_tracking_data(tracking_id)
        if not track_data:
            return None
            
        # Calculate timing between steps
        steps = track_data.get('steps', [])
        for i, step in enumerate(steps):
            if i > 0:
                prev_time = datetime.fromisoformat(steps[i-1]['timestamp'].replace('Z', '+00:00'))
                curr_time = datetime.fromisoformat(step['timestamp'].replace('Z', '+00:00'))
                step['time_since_previous_ms'] = int((curr_time - prev_time).total_seconds() * 1000)
        
        return {
            'tracking_summary': {
                'tracking_id': track_data['tracking_id'],
                'mcq_id': track_data['mcq_id'],
                'user_id': track_data['user_id'],
                'total_steps': len(steps),
                'start_time': track_data['start_time'],
                'last_step_time': steps[-1]['timestamp'] if steps else None
            },
            'detailed_steps': steps,
            'potential_issues': self._analyze_potential_issues(track_data)
        }
    
    def _analyze_potential_issues(self, track_data):
        """
        Analyze tracking data for potential issues
        """
        issues = []
        steps = track_data.get('steps', [])
        
        # Check for missing critical steps
        step_types = [step['step_type'] for step in steps]
        
        if 'CASE_GENERATION' not in step_types:
            issues.append("Missing case generation step")
            
        if 'DJANGO_SESSION_TRANSFER' not in step_types:
            issues.append("Missing Django session transfer step")
            
        if 'CASE_BOT_REQUEST' not in step_types:
            issues.append("Case bot never received request")
        
        # Check for MCQ ID mismatches
        mcq_ids = []
        for step in steps:
            data = step.get('data', {})
            if 'source_mcq_id' in data.get('case_summary', {}):
                mcq_ids.append(data['case_summary']['source_mcq_id'])
            if 'actual_mcq_id' in data:
                mcq_ids.append(data['actual_mcq_id'])
        
        unique_mcq_ids = list(set(mcq_ids))
        if len(unique_mcq_ids) > 1:
            issues.append(f"MCQ ID mismatch detected: {unique_mcq_ids}")
        
        # Check for session key mismatches
        session_keys = []
        for step in steps:
            data = step.get('data', {})
            if 'django_session_key' in data:
                session_keys.append(data['django_session_key'])
            if 'session_id' in data and step['step_type'] == 'CASE_BOT_REQUEST':
                session_keys.append(data['session_id'])
        
        unique_session_keys = list(set(session_keys))
        if len(unique_session_keys) > 1:
            issues.append(f"Session key mismatch detected: {unique_session_keys}")
        
        return issues
    
    def _log_step(self, track_data, step_type, step_data):
        """
        Add a step to the tracking data
        """
        step = {
            'step_type': step_type,
            'timestamp': timezone.now().isoformat(),
            'data': step_data
        }
        track_data['steps'].append(step)
    
    def _get_tracking_data(self, tracking_id):
        """
        Get tracking data from cache
        """
        return cache.get(f"conversion_tracking_{tracking_id}")
    
    def _save_tracking_data(self, tracking_id, track_data):
        """
        Save tracking data to cache
        """
        cache.set(f"conversion_tracking_{tracking_id}", track_data, 7200)


# Global tracker instance
conversion_tracker = CaseConversionTracker()