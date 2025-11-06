# Neurology MCQ Platform – Grand Refactor Plan

This living document captures the end-to-end modernization strategy for the Neurology MCQ platform. It records what has already been delivered, what is underway, and what remains so the roadmap survives resets, context loss, or team turnover.

---

## Guiding Principles

- **Domain-first architecture**: isolate core domains (MCQs, flashcards, reasoning, case-based learning, AI adapters) behind service modules and workflows.
- **Single sources of truth**: views, CLI scripts, web APIs, and background tasks should all delegate to the same service layer.
- **Deterministic AI orchestration**: AI prompts, fallbacks, and inline/async execution must be centralized so behaviour is predictable and testable.
- **User-focused flows**: every feature should feel like a realistic neurology training experience (consultant-guided, no spoilers, progressive disclosure).
- **Observability & safety nets**: instrument long-running flows, keep retry logic inside services, and protect against repeated or stale content.

---

## Milestones Completed (chronological)

1. **Repository Orientation & Core README refresh**
   - Updated root `README.md` with accurate stack, env vars, deployment, and doc references.

2. **Service Layer Kick-off**
   - Introduced `mcq.services` package with `MCQService`, `BookmarkService`, `NoteService`, `FlashcardService`.
   - Refactored MCQ/flashcard/bookmark/note views to use the service layer.
   - Created a new documentation hub `docs/REFRACTOR_ROADMAP.md` (checklist format).

3. **Reasoning Pal Modernization**
   - Added `ReasoningService` encapsulating session lifecycle, inline/background execution, feedback capture, and diagnostics.
   - Slimmed the reasoning views to input validation + JSON marshalling.
   - Documented status updates in the roadmap and ensured `manage.py check/test` pass (zero tests collected, but harness OK).

4. **Case-Based Learning Enhancements (current)**
   - Enforced unique case delivery keyed by specialty, difficulty, and optional custom learner requests.
   - Crafted variant generation with nuanced twists once the curated pool is exhausted.
   - Persisted learner requests and surfaced them across prompts/responses.
   - Structured the conversational flow (chief complaint → HPI → exam → localization → investigations → differential → management → follow-up → conclusion) with a supervising consultant persona.
   - Added a follow-up phase before the final reveal and reinforced “diagnosis revealed only in conclusion” across prompts.
   - Logged custom-request support and consultant-guided flow in this master plan per process agreement.

5. **Case Learning Service Extraction (partial)**
   - Introduced `services/case_learning_service.py` housing the session manager, case-history tracker, and unique-case generation helpers.
   - Wrapped the enhanced bot around the service singleton (no more in-file class copies).
   - Centralized session resets, specialty resolution, and initial case assignment (including skip-case regeneration) so the view calls the service for all entry points.
   - Moved history/examination feedback checks and their AI handoffs into the service so user prompts are screened before the view branches into the broader state machine.
   - Relocated phase-navigation logic ("proceed to…", prompt→feedback hand-offs, screening-exam injection) and bot-response assembly so the view now delegates entire turn processing to the service.
   - Standardized every OpenAI call on `gpt-5-mini` via the shared integration helpers; legacy direct model strings were removed from converters and maintenance scripts.
   - Centralized session start/skip behaviour through `initialize_case_conversation` and `skip_case`, trimming the view to a thin orchestration shell while keeping MCQ-alignment hooks injectable.
   - Moved general/MCQ intro prompt builders into the service so future API clients, Celery tasks, and the web view share identical entry prompts (legacy wrappers remain temporarily for backwards compatibility).
   - Brought screening neurological exam generation into the service, guaranteeing consistent orchestrated prompts and fallback messaging across channels.
   - Remaining work: migrate the conversational state machine + Celery workflows into the service.

6. **Service Test Coverage Kick-off**
   - Added focused unit tests for `CaseLearningService.process_user_turn`, covering exam-to-localization gating, auto-injected screening exams, and localization feedback scaffolding.
   - Extended coverage to the new `initialize_case_conversation` entry point (general vs MCQ cases with enhancer hooks) and established the test harness under `mcq/tests/` to bootstrap broader service-level regression coverage.
   - Validated `skip_case` retry behaviour so MCQ payloads fall back to fresh unique cases and skip history updates consistently.
   - Added regression tests for the service-managed screening exam generator (success + fallback) to lock in the shared orchestration behaviour.

---

## Workstreams In Progress / Next Up

1. **Case Learning Service Extraction (highest priority)**
   - ✅ Introduce `services/case_learning_service.py` to centralize session management, case history, and unique case generation.
   - 🔄 Expand the service to drive phase transitions and persistence (session/skip initialization now delegated; conversational transitions still handled in `case_bot_enhanced.py`).
   - [ ] Port Celery task logic (MCQ-to-case conversion) into reusable workflows with idempotency guards and tracking hooks.
   - [ ] Wrap `PersistentCaseLearningSession` access behind repository/helper classes.

2. **AI Adapter & Presenter Layer**
   - [ ] Introduce adapter classes for all OpenAI interactions (`CaseNarrativeGenerator`, `ReasoningNarrativeGenerator`) with deterministic interfaces.
   - [ ] Add presenter/serializer helpers so views and future REST/GraphQL endpoints share response schemas.

3. **API Harmonization**
   - [ ] Stand up DRF viewsets (or equivalent) for MCQs, flashcards, reasoning sessions, and case learning using the service layer.
   - [ ] Define canonical JSON contracts (request/response) and document them.

4. **Background Task Hardening**
   - [ ] Centralize retry policies, error handling, and task status reporting for Celery jobs (reasoning + case conversion).
   - [ ] Respect feature flags (`REASONING_INLINE`, `CELERY_EAGER`) inside service factories.

5. **Front-End / Client Integration**
   - [ ] Replace template-specific data assembly with presenters tied to service DTOs.
   - [ ] Align JavaScript/HTMX/API consumers with the standardized service responses.

6. **Testing Strategy**
   - [ ] Seed Django test cases for the existing services (MCQ, flashcards, bookmarks, reasoning, case learning once extracted).
   - [ ] Add fixture factories / property-based tests to validate AI fallbacks and prevent regression.

---

## Decision Log / Notes

- **AI Credentials**: Tests currently hit the live OpenAI API (API key supplied via env). Long term need to add mocks/fakes for repeatable CI runs.
- **Legacy Scripts**: The root-level manual scripts were moved into `manual_tests/` to stop them breaking test discovery. They double as historical references for future automated tests.
- **CKEditor 4 Warning**: `manage.py check` still surfaces the upstream CKEditor deprecation warning—tracked but not yet addressed.
- **Custom Learner Requests**: Stored with session metadata and hashed into case history to guarantee uniqueness. Future API design should surface this field explicitly.

---

## How to Contribute Safely

1. **Stay within the service layer**: add new behaviours to `mcq.services.*` (or the future `case_learning_service`) instead of expanding views.
2. **Record changes here**: whenever a milestone ships or priorities shift, update this master plan and `docs/REFRACTOR_ROADMAP.md`.
3. **Validate locally**: run `python django_neurology_mcq/manage.py check` and `python django_neurology_mcq/manage.py test` (adds to our safety net even if no tests exist yet).
4. **Plan before coding**: large changes should start with a mini-plan referencing the roadmap milestones to keep the vision intact.

This document is the authoritative guide—keep it in sync with reality.
