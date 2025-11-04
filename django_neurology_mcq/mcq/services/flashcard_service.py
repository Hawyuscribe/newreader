"""Flashcard orchestration for MCQ study flows."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import timedelta
from typing import Iterable, Optional

from django.contrib import messages
from django.utils import timezone

from ..models import Flashcard, MCQ


@dataclass
class FlashcardScheduleResult:
    flashcard: Flashcard
    created: bool


class FlashcardService:
    @staticmethod
    def schedule(user, mcq: MCQ, interval_days: int) -> FlashcardScheduleResult:
        next_review = timezone.now() + timedelta(days=interval_days)
        flashcard, created = Flashcard.objects.update_or_create(
            user=user,
            mcq=mcq,
            defaults={
                "interval": interval_days,
                "next_review": next_review,
            },
        )
        return FlashcardScheduleResult(flashcard=flashcard, created=created)

    @classmethod
    def schedule_with_feedback(cls, request, mcq: MCQ, interval_days: int) -> FlashcardScheduleResult:
        result = cls.schedule(request.user, mcq, interval_days)
        verb = "created" if result.created else "updated"
        messages.success(
            request,
            f"Flashcard {verb} for MCQ #{mcq.id} with interval {interval_days} days",
        )
        return result

    @staticmethod
    def _apply_review_window(queryset, review_type: str):
        now = timezone.now()
        if review_type == "week":
            return (
                queryset.filter(next_review__lte=now + timedelta(days=7)),
                "No flashcards due for review this week!",
            )
        if review_type == "today":
            return (
                queryset.filter(next_review__lte=now),
                "No flashcards due for review today!",
            )
        return queryset.filter(next_review__lte=now), "No flashcards due for review!"

    @classmethod
    def due_flashcards(cls, user, review_type: str = "today", hidden_mcq_ids: Optional[Iterable[int]] = None):
        qs = Flashcard.objects.filter(user=user).select_related("mcq")
        if hidden_mcq_ids:
            qs = qs.exclude(mcq_id__in=list(hidden_mcq_ids))

        filtered_qs, empty_message = cls._apply_review_window(qs, review_type)
        return filtered_qs.order_by("next_review"), empty_message

    @classmethod
    def due_flashcards_or_redirect(cls, request, review_type: str, hidden_mcq_ids: Iterable[int]):
        flashcards_qs, empty_message = cls.due_flashcards(
            request.user, review_type=review_type, hidden_mcq_ids=hidden_mcq_ids
        )
        if not flashcards_qs.exists():
            messages.info(request, empty_message)
            return None
        return flashcards_qs
