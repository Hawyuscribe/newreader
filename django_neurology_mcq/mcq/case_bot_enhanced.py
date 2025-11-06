import json
import logging
import os
import tempfile
from typing import Any, Dict

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .openai_integration import client
from .services.case_learning_service import case_conversation_service

logger = logging.getLogger(__name__)


def case_based_learning_enhanced(request):
    """Render the enhanced case-based learning interface."""

    return render(request, "mcq/case_based_learning_enhanced.html")


def _json_request(request) -> Dict[str, Any]:
    try:
        return json.loads(request.body.decode("utf-8"))
    except (ValueError, UnicodeDecodeError) as exc:  # pragma: no cover
        logger.debug("Failed to parse JSON payload: %s", exc)
        raise ValueError("Invalid JSON body") from exc


@csrf_exempt
@login_required
def neurology_bot_enhanced(request):
    """Single endpoint that powers the enhanced case-based learning UI."""

    if request.method != "POST":
        return JsonResponse({"error": "Method not allowed"}, status=405)

    try:
        payload = _json_request(request)
    except ValueError as exc:
        return JsonResponse({"error": str(exc)}, status=400)

    action = payload.get("action")
    session_id = payload.get("session_id")
    message = (payload.get("message") or "").strip()
    custom_request = (payload.get("custom_request") or "").strip() or None

    try:
        if action == "skip_case" and session_id:
            result = case_conversation_service.skip_case(
                user=request.user,
                session_id=session_id,
            )
        elif session_id and message:
            result = case_conversation_service.process_user_message(
                user=request.user,
                session_id=session_id,
                message=message,
            )
        else:
            specialty = payload.get("specialty")
            difficulty = payload.get("difficulty", "random")
            mcq_context = (
                payload.get("mcq_case_data")
                if isinstance(payload.get("mcq_case_data"), dict)
                else None
            )
            result = case_conversation_service.start_new_case(
                user=request.user,
                specialty=specialty,
                difficulty=difficulty,
                custom_request=custom_request,
                mcq_context=mcq_context,
                reuse_session_id=session_id,
            )
    except PermissionDenied:
        return JsonResponse({"error": "Session not found"}, status=404)
    except ValueError as exc:
        return JsonResponse({"error": str(exc)}, status=400)
    except RuntimeError as exc:
        logger.exception("Case bot runtime error")
        return JsonResponse({"error": str(exc)}, status=500)
    except Exception as exc:  # pragma: no cover
        logger.exception("Unexpected case bot failure")
        return JsonResponse({"error": "Unexpected error"}, status=500)

    return JsonResponse(result)


@csrf_exempt
@login_required
def transcribe_audio_enhanced(request):
    """Handle audio transcription for case-based learning."""

    if client is None:
        return JsonResponse(
            {"error": "OpenAI transcription is not configured."}, status=500
        )

    if request.method != "POST":
        return JsonResponse({"error": "Method not allowed"}, status=405)

    audio_file = request.FILES.get("audio")
    if not audio_file:
        return JsonResponse({"error": "No audio file provided"}, status=400)

    if audio_file.size > 25 * 1024 * 1024:
        return JsonResponse({"error": "Audio file too large (max 25MB)"}, status=400)

    mime_type = request.POST.get("mimeType", audio_file.content_type or "audio/webm")
    extension = ".webm"
    if "ogg" in mime_type:
        extension = ".ogg"
    elif "mp4" in mime_type or "m4a" in mime_type:
        extension = ".m4a"
    elif "wav" in mime_type:
        extension = ".wav"
    elif "mp3" in mime_type:
        extension = ".mp3"

    with tempfile.NamedTemporaryFile(mode="wb", suffix=extension, delete=False) as temp:
        for chunk in audio_file.chunks():
            temp.write(chunk)
        temp_path = temp.name

    try:
        result_text = ""
        with open(temp_path, "rb") as handle:
            transcription = client.audio.transcriptions.create(
                model="whisper-1",
                file=handle,
                response_format="text",
                language="en",
            )
        if isinstance(transcription, str):
            result_text = transcription.strip()
        elif transcription:
            result_text = getattr(transcription, "text", "") or ""
            result_text = result_text.strip()
        text = result_text
        return JsonResponse({"text": text})
    except Exception as exc:  # pragma: no cover
        logger.exception("Transcription failed")
        return JsonResponse({"error": str(exc)}, status=500)
    finally:
        try:
            os.unlink(temp_path)
        except OSError:
            pass
