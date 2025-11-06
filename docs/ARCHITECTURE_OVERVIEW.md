# Neurology MCQ Reader – Architecture Overview

This document summarizes the structure and design of the Neurology MCQ Reader Django application, based on the current repository snapshot.

## High-Level

- Framework: Django (project: `neurology_mcq`, main app: `mcq`)
- Deployment: Heroku (web via Gunicorn + WhiteNoise, Postgres, Redis)
- AI Features: OpenAI API (configurable model via `OPENAI_MODEL`)
- Background: Celery configured to use `REDIS_URL`

## Repos & Paths

- `django_neurology_mcq/neurology_mcq/`
  - `settings.py`: env-driven configuration (SQLite dev, Postgres prod via `DATABASE_URL`), WhiteNoise, CKEditor
  - `urls.py`: project-level URLs; delegates to `mcq.urls`
  - `wsgi.py` / `asgi.py`: server entrypoints
  - `celery_app.py`: Celery configuration using Redis (SSL if `rediss://`)

- `django_neurology_mcq/mcq/` (primary app)
  - `models/`: MCQ model, user interactions (bookmarks, notes, flashcards, incorrect answers), case and reasoning session models, high-yield content
  - `views.py`: dashboard, search, MCQ detail, answer checks, flashcards, bookmarks, notes, admin tools, AI endpoints
  - `urls.py`: public endpoints (MCQs, flashcards, case learning, admin/debug tools)
  - `middleware/`: 
    - `login_required`: redirects anonymous users to `/login/`
    - `account_expiration`: enforces account expiry policies
    - `temp_mcq_cleanup`: cleans temporary MCQ data
  - `tasks/`: Celery tasks for background processing
  - `openai_integration.py`: central OpenAI client, fallback mocks, explanation generation, verification, option generation; model is configurable via `OPENAI_MODEL`
  - `case_bot_enhanced.py`: interactive case-based learning bot; uses OpenAI client; model selection via `OPENAI_MODEL`
  - `clinical_reasoning_prompt.py`: reasoning flow and prompt config (now model driven by `OPENAI_MODEL`)
  - `management/commands/`: extensive import/export and maintenance commands for MCQs and explanations
  - `templates/mcq/`: login, dashboard, MCQ views, high-yield pages, admin debug console, etc.

- `django_neurology_mcq/templates/`
  - `mcq/`: app templates (login, dashboard, mcq detail, high-yield, admin/debug)
  - `admin/`: admin template overrides

- Static
  - `django_neurology_mcq/static/`: author CSS/JS (source)
  - `django_neurology_mcq/staticfiles/`: collected static; WhiteNoise serves in prod

## Settings and Env

- `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`
- `DATABASE_URL` (prod) / SQLite fallback (dev)
- `REDIS_URL`: Celery broker/result with SSL handling for Heroku
- `OPENAI_API_KEY`, `OPENAI_MODEL` (defaults to `gpt-5-mini`; override as needed)
- `STATIC_ROOT`/`STATIC_URL` configured; `CompressedManifestStaticFilesStorage` via WhiteNoise

## URLs (selected)

- Core
  - `/` → Dashboard
  - `/login/`, `/logout/`
  - `/search/`, `/subspecialty/<name>/`
  - `/mcq/<id>/` + actions: check answer, bookmarks, notes, flashcards
  - `/mcq/<id>/create_explanation/`, `/mcq/<id>/new_options/`, `/mcq/<id>/improve/`, `/mcq/<id>/ask_gpt/`

- Learning
  - `/case-based-learning/` (enhanced case bot)
  - `/api/neurology-bot/` (case bot API)
  - `/api/transcribe-audio/`
  - `/mcq/<id>/reasoning_pal/` + cognitive reasoning session endpoints

- Admin/Debug
  - `/admin/` (Django admin)
  - `/admin-export/`, import/export endpoints
  - `/admin/debug/*` (debug console, tracking, Heroku tests)

## AI Integration

- OpenAI client initialized in `mcq/openai_integration.py` with retries and a health check (`client.models.list()`)
- Model selection via `OPENAI_MODEL` env; default `gpt-5-mini` with optional `OPENAI_FALLBACK_MODEL`
- If API is unavailable or unauthorized, module returns high-quality mock responses to keep UX responsive

## Background Processing

- Celery configured in `neurology_mcq/celery_app.py` with Redis broker/backend
- Worker dyno recommended on Heroku (Procfile worker entry not currently present in repo; add if needed):
  - `worker: celery -A neurology_mcq.celery_app worker -l info`

## Authentication & Access

- Custom case-insensitive auth backend
- Login required middleware protects app routes; login at `/login/`
- Registration removed; accounts are admin-provisioned

## Deployment Notes (Heroku)

- `Procfile`:
  - `web: python -m gunicorn neurology_mcq.wsgi:application --chdir django_neurology_mcq`
  - `release: python django_neurology_mcq/manage.py migrate --noinput && python django_neurology_mcq/manage.py collectstatic --noinput`
- Set `OPENAI_API_KEY`, `OPENAI_MODEL`, `SECRET_KEY`, attach Postgres/Redis
- Static served via WhiteNoise; collectstatic runs in release phase

## Known Caveats

- `django-ckeditor` bundles CKEditor 4.x (deprecated upstream) → consider migration to CKEditor 5
- Some components perform DB access during app init (warnings appear in logs); consider moving to `AppConfig.ready()` or lazy paths if needed

## Getting Started (Dev)

1. `pip install -r requirements.txt`
2. Create `.env` with `SECRET_KEY`, `DEBUG=true`, optional `OPENAI_API_KEY`, `OPENAI_MODEL`
3. `python django_neurology_mcq/manage.py migrate`
4. `python django_neurology_mcq/manage.py runserver`
5. Optional: start Celery worker

## Maintenance Scripts

The repo contains many importer/exporter utilities and one-off analysis scripts (root and `django_neurology_mcq/`). Use management commands where possible for consistency. See `mcq/management/commands/` for supported operations (e.g., importing consolidated JSON exports, reclassifying, syncing to Heroku).
