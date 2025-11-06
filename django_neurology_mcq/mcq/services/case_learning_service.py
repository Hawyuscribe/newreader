"""AI-first case-learning service.

This module replaces the legacy state-machine implementation with a leaner
conversational service that relies on the OpenAI chat API to craft cases and
respond to learner input. All prompts, responses, and session persistence live
here so the web view remains a thin adapter.
"""

from __future__ import annotations

import logging
import uuid
from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from django.core.exceptions import PermissionDenied
from django.db import transaction
from django.utils import timezone

from ..models import PersistentCaseLearningSession
from ..openai_integration import (
    DEFAULT_MODEL,
    FALLBACK_MODEL,
    chat_completion,
    client,
    get_first_choice_text,
)

logger = logging.getLogger(__name__)


@dataclass
class ConversationResult:
    session: PersistentCaseLearningSession
    assistant_message: str
    notice: Optional[str] = None


class CaseSessionRepository:
    """CRUD helpers for conversation persistence."""

    def create_session(
        self,
        *,
        user_id: int,
        session_id: str,
        specialty: str,
        difficulty: str,
        case_data: Dict[str, Any],
        messages: List[Dict[str, str]],
    ) -> PersistentCaseLearningSession:
        session = PersistentCaseLearningSession.objects.create(
            session_id=session_id,
            user_id=user_id,
            specialty=specialty,
            difficulty=difficulty,
            state=0,
            case_data=case_data,
            messages=messages,
            history_gathered=[],
            examination_findings=[],
            created_at=timezone.now(),
            last_activity=timezone.now(),
        )
        return session

    def get_session_for_user(
        self, session_id: str, user_id: int
    ) -> PersistentCaseLearningSession:
        try:
            session = PersistentCaseLearningSession.objects.get(session_id=session_id)
        except PersistentCaseLearningSession.DoesNotExist as exc:  # pragma: no cover
            raise PermissionDenied("Session not found") from exc
        if session.user_id != user_id:
            raise PermissionDenied("Session not found")
        return session

    def save_conversation(
        self,
        session: PersistentCaseLearningSession,
        *,
        messages: List[Dict[str, str]],
        case_data: Optional[Dict[str, Any]] = None,
    ) -> None:
        session.messages = messages[-50:]  # keep the recent history bounded
        session.last_activity = timezone.now()
        if case_data is not None:
            session.case_data = case_data
        session.save(update_fields=["messages", "case_data", "last_activity"])

    def replace_conversation(
        self,
        session: PersistentCaseLearningSession,
        *,
        messages: List[Dict[str, str]],
        case_data: Dict[str, Any],
        specialty: Optional[str] = None,
        difficulty: Optional[str] = None,
    ) -> None:
        session.messages = messages
        session.case_data = case_data
        session.last_activity = timezone.now()
        session.created_at = timezone.now()
        session.completed = False
        session.completed_at = None
        session.auto_delete_after = None
        if specialty:
            session.specialty = specialty
        if difficulty:
            session.difficulty = difficulty
        session.save(
            update_fields=[
                "messages",
                "case_data",
                "last_activity",
                "created_at",
                "completed",
                "completed_at",
                "auto_delete_after",
                "specialty",
                "difficulty",
            ]
        )


class CaseConversationService:
    """Coordinates AI prompts and session persistence."""

    SYSTEM_PROMPT_TEMPLATE = (
        "You are an expert neurology attending running a live teaching case. "
        "Craft immersive, medically accurate cases and respond as a supportive "
        "mentor. Follow these rules:\n"
        "- Keep the tone collegial and succinct.\n"
        "- Start every case with only the chief complaint in one to two sentences; do not provide history, exam findings, "
        "investigations, or diagnosis until the learner asks.\n"
        "- Prompt the learner to begin history-taking and wait for their questions before revealing additional details.\n"
        "- Never reveal the final diagnosis until the learner explicitly asks to conclude.\n"
        "- When the learner issues short commands such as 'proceed to investigations', treat them as stage transitions and "
        "supply only the information relevant to that phase.\n"
        "- If the learner explicitly requests specific information or a stage summary (history, localization, investigations, "
        "differential, diagnosis, management, teaching points, etc.), provide that content immediately without redirecting "
        "the question back to them.\n"
        "- When you provide targeted information, generate plausible, internally consistent clinical details even if they have not been mentioned yet.\n"
        "- Avoid ending targeted replies with questions like 'What would you like to do next?'.\n"
        "- Include reasoning, red flags, and evidence-based guidance when you reach those phases.\n"
        "- Use Markdown for structure (lists, bold headings).\n"
        "- Highlight learning points and encourage reflection.\n"
        "Context: specialty={specialty}; difficulty={difficulty}.\n"
    )

    MAX_HISTORY_MESSAGES = 12

    STAGE_KEYWORDS = {
        "HISTORY": [
            "history",
            "onset",
            "tempo",
            "provocative",
            "associated symptom",
            "progression",
        ],
        "MOTOR_SENSORY": [
            "distribution",
            "weakness",
            "motor",
            "sensory",
            "cranial nerve",
            "facial",
            "dysarthria",
        ],
        "LOCALIZATION": [
            "localize",
            "localise",
            "localization",
            "vascular territory",
            "territory",
            "topography",
            "neuroanatomical",
        ],
        "INVESTIGATIONS": [
            "investigation",
            "imaging",
            "ct",
            "mri",
            "cta",
            "angiogram",
            "angiography",
            "laboratory",
            "lab",
            "blood work",
            "results",
        ],
        "DIFFERENTIAL": [
            "differential",
            "red flag",
            "red-flag",
            "considerations",
            "prioritised",
            "prioritized",
            "evidence",
            "reasoning",
        ],
        "DIAGNOSIS": [
            "diagnosis",
            "acute management",
            "management",
            "treatment",
            "therapy",
            "plan",
        ],
        "TEACHING": [
            "teaching",
            "teaching pearls",
            "learning",
            "follow-up",
            "follow up",
            "reflection",
            "resident",
            "next steps",
        ],
    }

    STAGE_INSTRUCTIONS = {
        "INTRO": (
            "Provide a concise chief complaint only, then invite the learner to begin their history-taking."
        ),
        "HISTORY": (
            "Provide the focused history that the learner requested. Summarize onset, tempo, provoking or alleviating "
            "factors, and associated neurological symptoms in a concise narrative, inventing plausible patient answers "
            "that fit the case. Answer directly without redirecting the question back to the learner, and do not end with a question."
        ),
        "MOTOR_SENSORY": (
            "Detail the distribution of weakness, associated sensory findings, and any cranial nerve involvement. Provide specific examples such as strength grades, regions of sensory loss, and named cranial nerve deficits. "
            "Respond definitively without prompting the learner for additional instructions or ending with a question."
        ),
        "LOCALIZATION": (
            "Analyse the collected findings to localize the lesion. Explicitly name the most likely neuroanatomical structures "
            "and vascular territory involved, explaining how the symptoms support this localisation. Do not ask the learner "
            "what they would like to do next or finish with a question."
        ),
        "INVESTIGATIONS": (
            "Summarize investigations that have already been completed, including imaging and key laboratory results, "
            "and explain their findings with concrete data. Assume the studies are available and avoid asking which tests to order or how the learner would like to proceed."
        ),
        "DIFFERENTIAL": (
            "Present a prioritised differential diagnosis with brief justification for each option and highlight relevant "
            "red flags, referencing evidence or reasoning that supports your ranking. List the items explicitly and conclude with a concise statement rather than a question."
        ),
        "DIAGNOSIS": (
            "State the leading diagnosis explicitly and outline the immediate management steps, including acute therapy "
            "and supportive care, offering clear attending-level guidance with specific interventions. Do not ask the learner what they would like to do next."
        ),
        "TEACHING": (
            "Provide teaching pearls, follow-up recommendations, and reflective points for a neurology resident. "
            "Encourage clinical reasoning insights without deferring the conversation or ending with a question, and end with a confident statement."
        ),
    }

    def __init__(self, repository: Optional[CaseSessionRepository] = None):
        if client is None:
            logger.warning(
                "OpenAI client is not initialised; case-based learning responses will fail."
            )
        self.repository = repository or CaseSessionRepository()

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------
    def start_new_case(
        self,
        *,
        user,
        specialty: str,
        difficulty: str,
        custom_request: Optional[str] = None,
        mcq_context: Optional[Dict[str, Any]] = None,
        reuse_session_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Start a fresh case, optionally overwriting an existing session."""

        specialty = (specialty or "general neurology").strip() or "general neurology"
        difficulty = (difficulty or "random").strip().lower()
        if difficulty not in {"easy", "moderate", "hard", "random"}:
            difficulty = "random"

        system_prompt = self._build_system_prompt(
            specialty, difficulty, custom_request, mcq_context
        )
        user_instruction = self._build_case_launch_instruction(
            specialty, difficulty, custom_request, mcq_context
        )

        assistant_message, conversation_messages = self._call_model(
            system_prompt,
            initial_user_instruction=user_instruction,
            force_prompt=self._build_force_prompt(user_instruction, stage="INTRO"),
        )

        case_data = {
            "specialty": specialty,
            "difficulty": difficulty,
            "custom_request": custom_request,
            "origin": "mcq" if mcq_context else "freeform",
            "system_prompt": system_prompt,
            "phase": "CONVERSATION",
        }

        if reuse_session_id:
            session = self.repository.get_session_for_user(reuse_session_id, user.id)
            self.repository.replace_conversation(
                session,
                messages=conversation_messages,
                case_data=case_data,
                specialty=specialty,
                difficulty=difficulty,
            )
        else:
            session_id = uuid.uuid4().hex
            session = self.repository.create_session(
                user_id=user.id,
                session_id=session_id,
                specialty=specialty,
                difficulty=difficulty,
                case_data=case_data,
                messages=conversation_messages,
            )

        result = ConversationResult(session=session, assistant_message=assistant_message)
        return self._serialize_result(result, initial=True)

    def process_user_message(
        self, *, user, session_id: str, message: str
    ) -> Dict[str, Any]:
        session = self.repository.get_session_for_user(session_id, user.id)
        case_data = session.case_data or {}
        system_prompt = case_data.get("system_prompt")
        if not system_prompt:
            raise ValueError("Session is missing system prompt metadata")

        message = message.strip()
        if not message:
            raise ValueError("Message cannot be empty")

        stage = self._detect_stage_command(message)
        effective_system_prompt = (
            self._augment_system_prompt(system_prompt, stage, message)
            if stage
            else system_prompt
        )

        if stage:
            conversation = [{"role": "system", "content": effective_system_prompt}]
        else:
            conversation = self._conversation_for_session(session, effective_system_prompt)
        conversation.append({"role": "user", "content": message})

        force_prompt = None if stage else self._build_force_prompt(message, stage=None)

        try:
            assistant_message, _ = self._call_model(
                effective_system_prompt,
                conversation_override=conversation,
                force_prompt=force_prompt,
            )
        except RuntimeError as exc:
            if "empty content" in str(exc).lower():
                logger.warning(
                    "Primary stage-aware response returned empty content; retrying with full history."
                )
                fallback_system_prompt = (
                    effective_system_prompt if stage else system_prompt
                )
                fallback_conversation = self._conversation_for_session(
                    session, fallback_system_prompt
                )
                fallback_conversation.append({"role": "user", "content": message})
                fallback_force_prompt = self._build_force_prompt(message, stage=stage)
                assistant_message, _ = self._call_model(
                    fallback_system_prompt,
                    conversation_override=fallback_conversation,
                    force_prompt=fallback_force_prompt,
                )
            else:
                raise

        session_messages = session.messages or []
        session_messages.append({"role": "user", "content": message})
        session_messages.append({"role": "assistant", "content": assistant_message})
        case_data["phase"] = stage or "CONVERSATION"
        self.repository.save_conversation(
            session, messages=session_messages, case_data=case_data
        )

        result = ConversationResult(session=session, assistant_message=assistant_message)
        return self._serialize_result(result)

    def skip_case(self, *, user, session_id: str) -> Dict[str, Any]:
        session = self.repository.get_session_for_user(session_id, user.id)
        case_data = session.case_data or {}
        specialty = case_data.get("specialty", session.specialty)
        difficulty = case_data.get("difficulty", session.difficulty)
        custom_request = case_data.get("custom_request")
        return self.start_new_case(
            user=user,
            specialty=specialty,
            difficulty=difficulty,
            custom_request=custom_request,
            reuse_session_id=session.session_id,
        )

    def resume_session(self, *, user, session_id: str) -> Dict[str, Any]:
        session = self.repository.get_session_for_user(session_id, user.id)
        messages = session.messages or []
        last_assistant = next(
            (msg["content"] for msg in reversed(messages) if msg.get("role") == "assistant"),
            "I have the case ready. How would you like to proceed?",
        )
        case_data = session.case_data or {}
        case_data["phase"] = "CONVERSATION"
        self.repository.save_conversation(session, messages=messages, case_data=case_data)
        result = ConversationResult(
            session=session,
            assistant_message=last_assistant,
            notice="Resumed your saved case."
        )
        return self._serialize_result(result)

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------
    def _build_system_prompt(
        self,
        specialty: str,
        difficulty: str,
        custom_request: Optional[str],
        mcq_context: Optional[Dict[str, Any]],
    ) -> str:
        prompt = self.SYSTEM_PROMPT_TEMPLATE.format(
            specialty=specialty,
            difficulty=difficulty,
        )
        if custom_request:
            prompt += f"\nLearner request: {custom_request.strip()}\n"
        if mcq_context:
            prompt += (
                "\nThis case must align with the following MCQ context. "
                "Use it verbatim for consistency with the learner's prior question.\n"
                f"MCQ prompt: {mcq_context.get('question_text', '')}\n"
                f"Correct answer: {mcq_context.get('correct_answer_text', '')}\n"
            )
        return prompt

    def _build_case_launch_instruction(
        self,
        specialty: str,
        difficulty: str,
        custom_request: Optional[str],
        mcq_context: Optional[Dict[str, Any]],
    ) -> str:
        base = (
            "Start a new neurology teaching case. Present only the chief complaint in one to two sentences, "
            "avoid giving history, examination, investigations, red flags, or diagnoses. After the chief complaint, "
            "invite the learner to begin history-taking (for example, ask what they would like to know next)."
        )
        if mcq_context:
            base += " Ensure the eventual history and findings remain consistent with the supplied MCQ context." 
        return base

    def _build_force_prompt(self, context: Optional[str], stage: Optional[str] = None) -> str:
        instruction_body = self.STAGE_INSTRUCTIONS.get(
            stage or "",
            "Provide the information the learner requested directly. Avoid returning questions to the learner; instead deliver the most relevant clinical details, and do not end with a question."
        )
        trimmed_context = (context or "").strip()
        directive = (
            "IMPORTANT: Respond to the learner's request now. "
            f"{instruction_body} Do not redirect, stall, or conclude with a question."
        )
        if trimmed_context:
            snippet = trimmed_context[:400]
            directive += f" Learner request to honour:\n{snippet}"
        return directive

    def _conversation_for_session(
        self, session: PersistentCaseLearningSession, system_prompt: str
    ) -> List[Dict[str, str]]:
        conversation: List[Dict[str, str]] = [
            {"role": "system", "content": system_prompt}
        ]
        history = session.messages or []
        conversation.extend(history[-self.MAX_HISTORY_MESSAGES :])
        return conversation

    def _detect_stage_command(self, message: str) -> Optional[str]:
        lowered = message.lower()
        for stage, keywords in self.STAGE_KEYWORDS.items():
            if any(keyword in lowered for keyword in keywords):
                return stage
        return None

    def _augment_system_prompt(
        self, base_prompt: str, stage: Optional[str], learner_message: str
    ) -> str:
        if not stage:
            return base_prompt
        directive = self._build_force_prompt(learner_message, stage=stage)
        return f"{base_prompt}\n\nCURRENT REQUEST:\n{directive}"

    def _call_model(
        self,
        system_prompt: str,
        initial_user_instruction: Optional[str] = None,
        conversation_override: Optional[List[Dict[str, str]]] = None,
        force_prompt: Optional[str] = None,
    ) -> (str, List[Dict[str, str]]):
        if client is None:
            raise RuntimeError("OpenAI client is not configured. Set OPENAI_API_KEY.")
        base_conversation = conversation_override or [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": initial_user_instruction or "Start the case."},
        ]

        models_to_try: List[str] = [DEFAULT_MODEL]
        if FALLBACK_MODEL and FALLBACK_MODEL not in models_to_try:
            models_to_try.append(FALLBACK_MODEL)

        last_error: Optional[Exception] = None

        for model_name in models_to_try:
            conversation = [msg.copy() for msg in base_conversation]
            attempt_conversations = [conversation]
            if force_prompt:
                forced = [msg.copy() for msg in base_conversation]
                forced.append({"role": "system", "content": force_prompt})
                attempt_conversations.insert(0, forced)

            for attempt_idx, convo in enumerate(attempt_conversations):
                try:
                    response = chat_completion(
                        client,
                        model_name,
                        convo,
                        max_tokens=700,
                        temperature=0.7,
                        timeout=45,
                    )
                    assistant_message = get_first_choice_text(response)
                except Exception as exc:  # pragma: no cover
                    logger.warning(
                        "Case bot model %s attempt %d failed: %s",
                        model_name,
                        attempt_idx + 1,
                        exc,
                        exc_info=True,
                    )
                    last_error = exc
                    continue

                if not assistant_message:
                    logger.warning(
                        "Case bot model %s attempt %d returned empty content.",
                        model_name,
                        attempt_idx + 1,
                    )
                    continue

                if conversation_override is None:
                    convo.append({"role": "assistant", "content": assistant_message})
                    # drop system message before persisting
                    return assistant_message, convo[1:]
                return assistant_message, convo

        if last_error:
            raise RuntimeError(f"Failed to generate case content: {last_error}")
        raise RuntimeError("AI returned empty content after multiple attempts.")

    def _serialize_result(self, result: ConversationResult, initial: bool = False) -> Dict[str, Any]:
        payload: Dict[str, Any] = {
            "success": True,
            "session_id": result.session.session_id,
            "message": result.assistant_message,
            "state": "CONVERSATION",
            "specialty": result.session.specialty,
            "difficulty": result.session.difficulty,
        }
        if result.notice:
            payload["notice_message"] = result.notice
            payload["notice_variant"] = "info"
        if initial:
            payload["notice_message"] = "New AI-generated case ready."
            payload["notice_variant"] = "info"
        return payload


case_conversation_service = CaseConversationService()
