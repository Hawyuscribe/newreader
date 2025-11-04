"""Service layer for MCQ application domain logic.

The service modules encapsulate business rules used by views, API endpoints,
Celery tasks, and future integrations. Centralizing these operations makes the
application easier to maintain and enables cross-channel reuse (web, API, AI
agents, etc.).
"""

from importlib import import_module

__all__ = [
    "MCQService",
    "BookmarkService",
    "NoteService",
    "FlashcardService",
    "ReasoningService",
    "CaseLearningService",
    "CasePreparationResult",
    "CaseFeedbackResult",
    "CaseTurnResult",
    "CaseStartResult",
    "case_learning_service",
]


def __getattr__(name):  # pragma: no cover - thin import shim
    if name == "MCQService":
        from .mcq_service import MCQService
        return MCQService
    if name == "BookmarkService":
        from .bookmark_service import BookmarkService
        return BookmarkService
    if name == "NoteService":
        from .note_service import NoteService
        return NoteService
    if name == "FlashcardService":
        from .flashcard_service import FlashcardService
        return FlashcardService
    if name == "ReasoningService":
        from .reasoning_service import ReasoningService
        return ReasoningService
    if name == "CaseLearningService":
        from .case_learning_service import CaseLearningService
        return CaseLearningService
    if name == "CasePreparationResult":
        from .case_learning_service import CasePreparationResult
        return CasePreparationResult
    if name == "CaseFeedbackResult":
        from .case_learning_service import CaseFeedbackResult
        return CaseFeedbackResult
    if name == "CaseTurnResult":
        from .case_learning_service import CaseTurnResult
        return CaseTurnResult
    if name == "CaseStartResult":
        from .case_learning_service import CaseStartResult
        return CaseStartResult
    if name == "case_learning_service":
        module = import_module('django_neurology_mcq.mcq.services.case_learning_service')
        return module.case_learning_service
    raise AttributeError(f"module 'mcq.services' has no attribute {name!r}")
