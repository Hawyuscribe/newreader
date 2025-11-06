"""Domain utilities for MCQ-centric workflows."""

from __future__ import annotations

import json
from datetime import timedelta
from dataclasses import dataclass
from typing import Iterable, List, Optional, Sequence, Tuple

from django.utils import timezone

from ..models import MCQ
from ..explanation_sections import EXPLANATION_SECTIONS
from ..explanation_utils import merge_sections_to_text, render_explanation_as_html


EXPLANATION_PLACEHOLDER = """
<div class=\"explanation-wrapper\">
    <div class=\"alert alert-info\">
        <h4><i class=\"bi bi-lightbulb\"></i> Explanation Needed</h4>
        <p>This MCQ doesn't have a detailed explanation yet. Click the "Generate Explanation" button below to create one using AI.</p>
    </div>
</div>
"""


@dataclass(frozen=True)
class ExplanationContext:
    """Computed explanation metadata used by detail views and APIs."""

    clean_html: str
    has_structured: bool
    has_full_explanation: bool


class MCQService:
    """High level operations for MCQ entities.

    Centralizing these helpers keeps view functions light-weight while enabling
    future reuse from API endpoints or background jobs.
    """

    @staticmethod
    def get_hidden_mcq_ids(user) -> List[int]:
        """Return the MCQ ids hidden by a user.

        The HiddenMCQ model was introduced late in the project; safely handle the
        case where migrations have not run yet.
        """

        try:
            from ..models import HiddenMCQ  # type: ignore
        except Exception:
            return []

        return list(
            HiddenMCQ.objects.filter(user=user).values_list("mcq_id", flat=True)
        )

    @staticmethod
    def decode_options(options_field):
        """Parse an options JSON string into a Python object if needed."""
        if not options_field:
            return options_field

        if isinstance(options_field, dict):
            return options_field

        if isinstance(options_field, list):
            return options_field

        try:
            return json.loads(options_field)
        except (TypeError, json.JSONDecodeError):
            return options_field

    @staticmethod
    def _ordered_option_items(options_dict):
        """Return option items preserving insertion order and capturing letters."""
        ordered_items = list(options_dict.items())
        return [(str(key).strip(), value) for key, value in ordered_items]

    @staticmethod
    def _letter_for_index(index: int) -> str:
        """Map an index to an option letter (A, B, ...)."""
        if index < 26:
            return chr(ord('A') + index)
        return f"Option {index + 1}"

    @classmethod
    def ensure_options_decoded(cls, mcq: MCQ) -> MCQ:
        """Return MCQ with options coerced to Python structures."""
        decoded = cls.decode_options(mcq.options)

        if isinstance(decoded, dict):
            ordered_items = cls._ordered_option_items(decoded)
            letters = [letter for letter, _ in ordered_items]
            texts = [text for _, text in ordered_items]
            mcq.option_letters = letters
            mcq.option_map = {letter: text for letter, text in ordered_items}
            mcq.options = texts
        elif isinstance(decoded, list):
            letters = [cls._letter_for_index(idx) for idx, _ in enumerate(decoded)]
            mcq.option_letters = letters
            mcq.option_map = {letter: text for letter, text in zip(letters, decoded)}
            if decoded is not mcq.options:
                mcq.options = decoded
        else:
            mcq.option_letters = []
            mcq.option_map = {}
            if decoded is not mcq.options:
                mcq.options = decoded

        return mcq

    @staticmethod
    def _is_classification_only(mcq: MCQ) -> bool:
        explanation = getattr(mcq, "explanation", "") or ""
        return (
            bool(explanation)
            and "Classification Reason:" in explanation
            and len(explanation) < 300
        )

    @classmethod
    def build_explanation_context(cls, mcq: MCQ) -> ExplanationContext:
        """Compute the preferred explanation markup and flags."""
        is_classification_only = cls._is_classification_only(mcq)
        sections = getattr(mcq, "explanation_sections", None) or {}

        unified_text = ""
        try:
            unified_text = mcq.get_unified_explanation_text()
        except AttributeError:
            unified_text = getattr(mcq, "unified_explanation", "") or ""
            if not unified_text and isinstance(sections, dict) and sections:
                unified_text = merge_sections_to_text(sections)
            if not unified_text:
                unified_text = getattr(mcq, "explanation", "") or ""

        # Keep legacy field in sync to avoid downstream surprises
        if unified_text and not getattr(mcq, "explanation", ""):
            mcq.explanation = unified_text

        has_full = bool(unified_text) and not is_classification_only
        clean_html = (
            render_explanation_as_html(unified_text)
            if has_full and unified_text
            else EXPLANATION_PLACEHOLDER
        )

        return ExplanationContext(
            clean_html=clean_html,
            has_structured=False,
            has_full_explanation=has_full,
        )

    @staticmethod
    def next_review_date(interval_days: int):
        return timezone.now() + timedelta(days=interval_days)

    @classmethod
    def wrap_navigation(cls, sequence: Sequence[int], position: int) -> Tuple[Optional[MCQ], Optional[MCQ]]:
        """Return previous and next MCQs with wrap-around semantics."""
        if not sequence:
            return None, None

        try:
            current_id = sequence[position]
        except IndexError:
            return None, None

        prev_mcq = None
        next_mcq = None

        if len(sequence) == 1:
            return None, None

        if position + 1 < len(sequence):
            next_mcq = MCQ.objects.filter(id=sequence[position + 1]).first()
        else:
            next_mcq = MCQ.objects.filter(id=sequence[0]).first()

        if position > 0:
            prev_mcq = MCQ.objects.filter(id=sequence[position - 1]).first()
        else:
            prev_mcq = MCQ.objects.filter(id=sequence[-1]).first()

        return prev_mcq, next_mcq

    @staticmethod
    def search_queryset(query: str = "", subspecialty: Optional[str] = None):
        qs = MCQ.objects.all()
        if subspecialty:
            qs = qs.filter(subspecialty=subspecialty)
        if query:
            qs = qs.filter(question_text__icontains=query)
        return qs

    @staticmethod
    def get_user_notes(user, mcq_ids: Iterable[int]):
        from ..models import Note

        return {
            note.mcq_id: note
            for note in Note.objects.filter(user=user, mcq_id__in=mcq_ids)
        }
