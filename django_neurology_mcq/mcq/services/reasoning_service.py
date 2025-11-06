"""Service utilities for cognitive reasoning workflows."""

from __future__ import annotations

import ast
import json
import logging
import os
from dataclasses import dataclass
from datetime import timedelta
from typing import Any, Dict, Iterable, List, Optional, Tuple

from django.utils import timezone

from ..models import CognitiveReasoningSession, MCQ

logger = logging.getLogger(__name__)


@dataclass
class ServiceResult:
    payload: Dict[str, Any]
    status: int = 200


class ReasoningService:
    """Encapsulates ReasoningPal orchestration across inline and background flows."""

    MIN_REASON_LENGTH = 10
    _VALID_FEEDBACK = {'helpful', 'somewhat_helpful', 'not_helpful'}

    # ------------------------------------------------------------------
    # Session lifecycle
    # ------------------------------------------------------------------
    @classmethod
    def start_analysis(
        cls,
        user,
        mcq: MCQ,
        selected_answer: str,
        user_reasoning: str,
        is_correct: bool,
    ) -> ServiceResult:
        session = CognitiveReasoningSession.objects.create(
            user=user,
            mcq=mcq,
            selected_answer=selected_answer,
            is_correct=is_correct,
            user_reasoning=user_reasoning,
            status=CognitiveReasoningSession.ANALYZING,
        )

        try:
            if cls._should_run_inline():
                logger.info("Running cognitive reasoning inline for session %s", session.id)
                payload = cls._run_inline(session)
                return ServiceResult(payload=payload)

            logger.info("Queueing background reasoning task for session %s", session.id)
            payload = cls._queue_background_task(session)
            return ServiceResult(payload=payload)

        except Exception as exc:  # pragma: no cover - defensive path
            logger.error("Reasoning analysis failed for session %s: %s", session.id, exc, exc_info=True)
            error_payload = cls._handle_session_error(session, exc)
            return ServiceResult(payload=error_payload, status=500)

    # ------------------------------------------------------------------
    # Inline analysis
    # ------------------------------------------------------------------
    @classmethod
    def _run_inline(cls, session: CognitiveReasoningSession) -> Dict[str, Any]:
        generator = cls._resolve_generator()
        steps = cls._serialize_steps(
            generator.generate_guidance(
                session.mcq,
                session.selected_answer,
                session.user_reasoning,
                session.is_correct,
            )
        )

        cls._store_guidance(session, steps, status=CognitiveReasoningSession.READY)

        first_step = steps[0] if steps else {
            'title': 'Clinical Reasoning Analysis',
            'content': '<p>Analysis complete.</p>'
        }

        return {
            'success': True,
            'status': 'ready',
            'session_id': session.id,
            'analysis': cls._analysis_metadata(session, steps, 0, first_step.get('content', '')),
            'current_step': 0,
            'step': first_step,
            'has_next_step': len(steps) > 1,
        }

    @classmethod
    def _resolve_generator(cls):  # pragma: no cover - import side effects
        try:
            from ..cognitive_analysis_openai import ReasoningGuideGenerator as OpenAIGenerator

            try:
                return OpenAIGenerator()
            except Exception as exc:
                logger.warning("OpenAI reasoning generator unavailable: %s", exc)
        except Exception as exc:
            logger.debug("OpenAI reasoning generator import failed: %s", exc)

        from ..cognitive_analysis import ReasoningGuideGenerator as RuleBasedGenerator

        return RuleBasedGenerator()

    # ------------------------------------------------------------------
    # Background execution
    # ------------------------------------------------------------------
    @classmethod
    def _queue_background_task(cls, session: CognitiveReasoningSession) -> Dict[str, Any]:
        from ..tasks import process_clinical_reasoning_analysis

        task = process_clinical_reasoning_analysis.delay(
            session.id,
            session.mcq.id,
            session.selected_answer,
            session.user_reasoning,
            session.is_correct,
        )

        session.task_id = task.id
        session.save(update_fields=['task_id'])

        return {
            'success': True,
            'session_id': session.id,
            'task_id': task.id,
            'status': 'processing',
            'analysis': {
                'primary_error': None,
                'secondary_errors': [],
                'knowledge_gaps': [],
                'misconceptions': [],
                'reasoning_quality': 'analyzing',
                'confidence_score': 0,
                'analysis_summary': 'Analysis in progress...',
                'total_steps': 1,
            },
            'current_step': 0,
            'step': cls._analysis_in_progress_step(),
            'has_next_step': False,
        }

    @staticmethod
    def _analysis_in_progress_step() -> Dict[str, Any]:
        return {
            'title': '🔄 Analysis in Progress',
            'content': '''
                <div class="text-center">
                    <div class="spinner-border text-primary mb-3" role="status">
                        <span class="visually-hidden">Loading...</span>
                    </div>
                    <h5>AI-Powered Clinical Reasoning Analysis</h5>
                    <p class="text-muted">Our advanced model is analyzing your reasoning...</p>
                    <p><small>This typically takes 1-2 minutes for comprehensive analysis.</small></p>
                </div>
            ''',
            'question': None,
            'evidence': None,
            'action': 'Please wait while we analyze your clinical reasoning...'
        }

    # ------------------------------------------------------------------
    # Session utilities
    # ------------------------------------------------------------------
    @classmethod
    def _store_guidance(
        cls,
        session: CognitiveReasoningSession,
        steps: List[Dict[str, Any]],
        *,
        status: str,
    ) -> None:
        session.guidance_steps = steps
        session.current_step = 0
        session.status = status
        if not session.reasoning_quality:
            session.reasoning_quality = 'fair'
        if not session.confidence_score:
            session.confidence_score = 50
        session.save()

    @classmethod
    def _analysis_metadata(
        cls,
        session: CognitiveReasoningSession,
        steps: List[Dict[str, Any]],
        current_index: int,
        analysis_summary: str,
    ) -> Dict[str, Any]:
        return {
            'primary_error': session.primary_error,
            'secondary_errors': session.secondary_errors,
            'knowledge_gaps': session.knowledge_gaps,
            'misconceptions': session.misconceptions,
            'reasoning_quality': session.reasoning_quality,
            'confidence_score': session.confidence_score,
            'total_steps': len(steps),
            'analysis_summary': analysis_summary,
        }

    @classmethod
    def _serialize_steps(cls, steps: Iterable[Any]) -> List[Dict[str, Any]]:
        serialized: List[Dict[str, Any]] = []
        for step in steps or []:
            serialized.append({
                'title': getattr(step, 'title', None),
                'content': getattr(step, 'content', ''),
                'question': getattr(step, 'question', None),
                'evidence': getattr(step, 'evidence', None),
                'action': getattr(step, 'action', None),
            })
        return serialized

    @staticmethod
    def _should_run_inline() -> bool:
        env = os.environ
        return (
            env.get('CELERY_EAGER', 'false').lower() == 'true'
            or env.get('REASONING_INLINE', 'false').lower() == 'true'
        )

    @classmethod
    def _handle_session_error(cls, session: CognitiveReasoningSession, exc: Exception) -> Dict[str, Any]:
        session.status = CognitiveReasoningSession.ERROR
        session.error_message = str(exc)
        session.save(update_fields=['status', 'error_message'])

        return {
            'success': False,
            'error': 'Analysis failed. Please try again.',
            'session_id': session.id,
            'step': {
                'title': '⚠️ Analysis Error',
                'content': '''
                We encountered an error while analyzing your reasoning. This doesn't reflect on your clinical thinking!

                **What you can do:**
                - Try submitting your reasoning again
                - Contact support if the problem persists
                - Your reasoning has been saved for review
                ''',
                'question': None,
                'evidence': None,
                'action': 'Try again or contact support',
            },
        }

    # ------------------------------------------------------------------
    # Step navigation
    # ------------------------------------------------------------------
    @classmethod
    def advance_step(cls, session: CognitiveReasoningSession) -> ServiceResult:
        guidance = cls._normalize_guidance(session.guidance_steps)
        if not guidance:
            return ServiceResult(
                payload={'success': False, 'error': 'Guidance not available yet'},
                status=400,
            )

        if session.current_step >= len(guidance) - 1:
            return ServiceResult(
                payload={
                    'success': False,
                    'error': 'Already at the last step',
                    'is_completed': True,
                }
            )

        session.current_step += 1
        session.save(update_fields=['current_step'])

        current_step_data = guidance[session.current_step]
        return ServiceResult(
            payload={
                'success': True,
                'current_step': session.current_step,
                'step': current_step_data,
                'has_next_step': session.current_step < len(guidance) - 1,
                'is_completed': session.current_step >= len(guidance) - 1,
            }
        )

    # ------------------------------------------------------------------
    # Feedback capture
    # ------------------------------------------------------------------
    @classmethod
    def submit_feedback(
        cls,
        session: CognitiveReasoningSession,
        feedback: str,
        comments: str,
    ) -> ServiceResult:
        feedback = (feedback or '').strip()
        if feedback not in cls._VALID_FEEDBACK:
            return ServiceResult(
                payload={'error': 'Invalid feedback value'},
                status=400,
            )

        session.user_feedback = feedback
        session.feedback_comments = comments.strip()
        session.completed_at = timezone.now()
        session.save(update_fields=['user_feedback', 'feedback_comments', 'completed_at'])

        logger.info("Captured reasoning feedback for session %s: %s", session.id, feedback)
        return ServiceResult(payload={'success': True, 'message': 'Thank you for your feedback!'})

    # ------------------------------------------------------------------
    # Background status checks
    # ------------------------------------------------------------------
    @classmethod
    def check_task_status(cls, session: CognitiveReasoningSession) -> ServiceResult:
        if session.status == CognitiveReasoningSession.READY:
            return ServiceResult(payload=cls._build_ready_payload(session))

        if session.status == CognitiveReasoningSession.FAILED:
            try:
                payload = cls._inline_fallback(session)
                return ServiceResult(payload=payload)
            except Exception as exc:  # pragma: no cover - defensive
                logger.error("Inline fallback after failure failed: %s", exc, exc_info=True)
                return ServiceResult(
                    payload={
                        'success': False,
                        'status': 'failed',
                        'error': session.error_message or 'Analysis failed',
                    }
                )

        if session.status in (CognitiveReasoningSession.ANALYZING, CognitiveReasoningSession.PROCESSING):
            return ServiceResult(
                payload={
                    'success': True,
                    'status': 'processing',
                    'message': 'Analysis still in progress...',
                }
            )

        return ServiceResult(
            payload={
                'success': False,
                'status': 'error',
                'error': f'Unexpected session status: {session.status}',
            }
        )

    @classmethod
    def _inline_fallback(cls, session: CognitiveReasoningSession) -> Dict[str, Any]:
        generator = cls._resolve_generator()
        steps = cls._serialize_steps(
            generator.generate_guidance(
                session.mcq,
                session.selected_answer,
                session.user_reasoning,
                session.is_correct,
            )
        )
        cls._store_guidance(session, steps, status=CognitiveReasoningSession.READY)
        first_step = steps[0] if steps else {'title': 'Clinical Reasoning Analysis', 'content': '<p>Analysis complete.</p>'}
        return {
            'success': True,
            'status': 'ready',
            'session_id': session.id,
            'analysis': cls._analysis_metadata(session, steps, 0, first_step.get('content', '')),
            'current_step': 0,
            'step': first_step,
            'has_next_step': len(steps) > 1,
        }

    @classmethod
    def _build_ready_payload(cls, session: CognitiveReasoningSession) -> Dict[str, Any]:
        guidance = cls._normalize_guidance(session.guidance_steps)
        total_steps = len(guidance)
        current_idx = session.current_step or 0
        if current_idx < 0 or current_idx >= total_steps:
            current_idx = 0

        current_step = guidance[current_idx] if total_steps else None
        summary = ''
        if total_steps:
            summary = cls._step_content(current_step)
            if not summary:
                for step in guidance:
                    summary = cls._step_content(step)
                    if summary:
                        current_step = step
                        break

        return {
            'success': True,
            'status': 'ready',
            'session_id': session.id,
            'analysis': cls._analysis_metadata(session, guidance, current_idx, summary),
            'current_step': current_idx,
            'step': current_step,
            'has_next_step': current_idx < total_steps - 1 if total_steps else False,
        }

    @staticmethod
    def _step_content(step: Optional[Dict[str, Any]]) -> str:
        if isinstance(step, dict):
            return (step.get('content') or '').strip()
        return ''

    @classmethod
    def _normalize_guidance(cls, guidance) -> List[Dict[str, Any]]:
        if isinstance(guidance, list):
            return guidance
        if isinstance(guidance, dict):
            return [guidance]
        if isinstance(guidance, str):
            try:
                parsed = json.loads(guidance)
            except Exception:
                try:
                    parsed = ast.literal_eval(guidance)
                except Exception:
                    parsed = []
            return cls._normalize_guidance(parsed)
        return []

    # ------------------------------------------------------------------
    # Diagnostics (admin)
    # ------------------------------------------------------------------
    @classmethod
    def failed_session_summary(cls, hours: int = 24, limit: int = 10) -> ServiceResult:
        cutoff = timezone.now() - timedelta(hours=hours)

        failed = CognitiveReasoningSession.objects.filter(
            status=CognitiveReasoningSession.FAILED,
            created_at__gte=cutoff,
        ).select_related('user', 'mcq').order_by('-created_at')[:limit]

        processing = CognitiveReasoningSession.objects.filter(
            status__in=[CognitiveReasoningSession.PROCESSING, CognitiveReasoningSession.ANALYZING],
            created_at__gte=cutoff,
        ).select_related('user', 'mcq').order_by('-created_at')[:5]

        stats = {
            'failed_last_24h': failed.count(),
            'processing_stuck': processing.count(),
            'total_sessions_24h': CognitiveReasoningSession.objects.filter(created_at__gte=cutoff).count(),
        }

        now = timezone.now()
        failed_data = [
            {
                'id': session.id,
                'user': session.user.username,
                'mcq_id': session.mcq.id,
                'task_id': session.task_id,
                'error_message': session.error_message,
                'created_at': session.created_at.isoformat(),
                'time_ago': (now - session.created_at).total_seconds() / 60,
            }
            for session in failed
        ]

        processing_data = [
            {
                'id': session.id,
                'user': session.user.username,
                'mcq_id': session.mcq.id,
                'task_id': session.task_id,
                'status': session.status,
                'created_at': session.created_at.isoformat(),
                'time_ago': (now - session.created_at).total_seconds() / 60,
            }
            for session in processing
        ]

        return ServiceResult(
            payload={
                'success': True,
                'stats': stats,
                'failed_sessions': failed_data,
                'stuck_processing': processing_data,
            }
        )
