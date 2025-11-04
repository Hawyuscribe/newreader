"""Bookmark orchestration helpers."""

from __future__ import annotations

from dataclasses import dataclass

from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from ..models import Bookmark, MCQ


@dataclass
class ToggleResult:
    created: bool
    message: str


class BookmarkService:
    """Encapsulate bookmark create/delete flows."""

    @staticmethod
    def toggle(user, mcq: MCQ) -> ToggleResult:
        bookmark, created = Bookmark.objects.get_or_create(user=user, mcq=mcq)
        if created:
            message = _(f"Bookmark added for MCQ #{mcq.id}")
        else:
            bookmark.delete()
            message = _(f"Bookmark removed for MCQ #{mcq.id}")
        return ToggleResult(created=created, message=str(message))

    @classmethod
    def toggle_with_feedback(cls, request, mcq: MCQ) -> ToggleResult:
        result = cls.toggle(request.user, mcq)
        messages.success(request, result.message)
        return result

    @staticmethod
    def queryset_for_user(user, hidden_mcq_ids=None):
        qs = Bookmark.objects.filter(user=user).select_related("mcq")
        if hidden_mcq_ids:
            qs = qs.exclude(mcq_id__in=list(hidden_mcq_ids))
        return qs.order_by("id")
