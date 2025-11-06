# Neurology MCQ Platform Refactor Roadmap

This roadmap captures the target architecture for the ongoing refactor so every feature remains consistent across the web UI, API integrations, and background jobs.

## Architectural Principles

- **Domain-first modules**: group code by domain (MCQs, flashcards, reasoning, case learning, AI orchestration) rather than by framework layer.
- **Service layer**: expose reusable services that form the contract between views, REST/GraphQL APIs, Celery tasks, and future mobile clients.
- **Task orchestration**: treat async jobs (case conversion, reasoning analysis) as first-class workflows with idempotent commands and progress tracking.
- **API consistency**: consolidate HTTP endpoints behind DRF viewsets (or equivalent) while keeping server-rendered views thin.
- **Observability**: centralize logging, metrics, and tracing hooks to follow a request from user action through AI calls and database writes.

## Target Module Layout (incremental)

```
django_neurology_mcq/
  mcq/
    domain/
      mcq.py            # entities, value objects, validation helpers
      flashcard.py
      reasoning.py
      case_learning.py
    services/
      mcq_service.py    # implemented
      flashcard_service.py  # implemented
      bookmark_service.py   # implemented
      note_service.py       # implemented
      reasoning_service.py  # TODO
      case_service.py       # TODO
      ai_service.py         # TODO (wraps openai_integration)
    api/
      mcq.py             # DRF viewsets / serializers (planned)
      flashcards.py
      reasoning.py
    workflows/
      case_conversion.py # high-level orchestrators used by Celery/HTTP
      reasoning.py
    presenters/
      dashboard.py       # view-model builders for server-rendered templates
```

## Refactor Phases

1. **Service Layer Extraction (in progress)**
   - ✅ Consolidate bookmark, note, flashcard, and explanation helpers under `mcq.services`.
   - 🔄 Continue migrating view logic (remaining MCQ utilities, incorrect-answer tracking) into dedicated services.

2. **Reasoning & Case Learning Core**
   - ✅ Introduce `services/reasoning_service.py` for Reasoning Pal lifecycle (inline execution and Celery orchestration).
   - 🔄 Extract case conversion flows into `services/case_service.py` with shared lifecycle helpers.
   - 🔄 Move session lifecycle logic (creation, cancellation, progress checks) to workflows reusable by Celery and HTTP endpoints.

3. **API Harmonization**
   - Introduce Django REST Framework (or lightweight JSON responders) that call the new services; keep API/PWA behavior in sync with server-rendered pages.
   - Document canonical request/response schemas for MCQ detail, flashcard queue, reasoning sessions, and case bot interactions.

4. **Background Task Hardening**
   - Wrap Celery tasks with workflow helpers, ensure idempotency, and surface worker status via service APIs (`get_task_status`, `retry`, etc.).
   - Centralize Redis/Heroku feature flags (e.g., `REASONING_INLINE`, `CELERY_EAGER`) inside service factories.

5. **Front-End Integration**
   - Replace template-specific data assembly with presenter classes that consume service DTOs.
   - Align JavaScript/HTMX endpoints with the standardized API contract.

6. **Quality Gate**
   - ✅ Added the first service-level tests for `CaseLearningService.process_user_turn`, `initialize_case_conversation`, and `skip_case`, validating exam-to-localization gating, screening exam injection, MCQ intro handling, skip retries, and localization feedback transitions.
   - Continue adding test suites around each domain service, including fixtures for MCQ operations, flashcard scheduling, reasoning flows, and case conversions.
   - Layer property-based tests for AI fallbacks (mocked OpenAI responses) to ensure deterministic behavior.

## Immediate Next Steps

- ✅ Route session creation, specialty resolution, skip-case resets, history/exam feedback, phase navigation, and bot response synthesis through `CaseLearningService` so views only marshal AI responses.
- Migrate MCQ listing/search/dialer logic into `MCQService` (includes pagination, hidden filtering, and navigation caches).
- Harden ReasoningService by adding presenter-friendly serializers and background retry policies.
- Extract the remaining conversational state machine into `CaseLearningService` with dependency injection hooks for AI adapters and caching (intro prompt builders now centralized; next up: consultant prompt sequences).
- Prepare serializer layer (even without full DRF adoption) to guarantee consistent JSON across endpoints.

## Tracking Progress

- Use this roadmap as a checklist; mark each bullet when completed and link relevant PRs/commits.
- Update README and docs as new service modules ship so contributors know the canonical entry points.
- Keep existing views functional during migration by delegating to the service layer (as done for bookmarks/notes/flashcards).

---

This document evolves as the refactor proceeds. Please add observations, pain points, or follow-up tasks as you migrate additional features.
