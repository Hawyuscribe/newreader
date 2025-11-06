"""Service helpers for MCQ notes."""

from __future__ import annotations

from dataclasses import dataclass

from django.contrib import messages

from ..models import MCQ, Note


@dataclass
class NoteResult:
    note: Note
    created: bool


class NoteService:
    @staticmethod
    def save_note(user, mcq: MCQ, text: str) -> NoteResult:
        note, created = Note.objects.update_or_create(
            user=user,
            mcq=mcq,
            defaults={"note_text": text},
        )
        return NoteResult(note=note, created=created)

    @classmethod
    def save_with_feedback(cls, request, mcq: MCQ, text: str) -> NoteResult:
        result = cls.save_note(request.user, mcq, text)
        messages.success(request, f"Note saved for MCQ #{mcq.id}")
        return result
