# Neurology MCQ Reader (Django)

Neurology MCQ Reader is a Django 5 application for neurology exam preparation. It combines a curated MCQ library with flashcards, high-yield summaries, AI-generated explanations, cognitive reasoning analysis, and an interactive case-based learning bot. The production deployment targets Heroku with PostgreSQL, Redis, Gunicorn, and WhiteNoise. The canonical production instance lives at https://enigmatic-hamlet-38937-db49bd5e9821.herokuapp.com/ (git remote `https://git.heroku.com/enigmatic-hamlet-38937-db49bd5e9821.git`).

## Highlights

- MCQ library with subspecialty filters, full-text search, bookmarks, notes, flashcards, hide/unhide, mock exams, and weakness drills.
- AI tooling for explanation generation, answer option improvement, Reasoning Pal feedback, test-my-understanding flows, and MCQ-to-case conversion.
- Case-based learning workspace with persistent sessions, audio transcription, and OpenAI-powered clinical reasoning coach.
- Admin and staff utilities for inline editing, import/export, session integrity tracking, diagnostics, and OpenAI self-tests.
- Account controls that enforce login, case-insensitive usernames, and optional expiration windows.

## Refactor Progress & Next Steps

The application is midway through a service-layer refactor that unifies AI orchestration and conversational logic:

- ✅ `mcq.services.CaseLearningService` now owns session creation, skip handling, intro prompt generation (general + MCQ), and screening exam generation, so the Django view is a thin adapter across web/API/background flows.
- ✅ All OpenAI usage defaults to `gpt-5-mini` through the shared integration helpers; service-level tests cover prompt building, skip retries, and screening-fallback behaviour.
- 🔄 Upcoming milestones (also tracked in `docs/REFRACTOR_MASTER_PLAN.md` & `docs/REFRACTOR_ROADMAP.md`):
  1. Finish moving consultant feedback/phase transitions (localization, investigations, differential, management) into the service state machine.
  2. Expose the service layer through DRF endpoints and shared presenters for web/API parity.
  3. Harden Celery workflows (case conversion, reasoning) with idempotent commands and richer observability.
  4. Expand automated tests for MCQ/flashcard/reasoning services and introduce OpenAI fakes for CI once end-to-end smoke tests are captured.

Refer to the refactor docs for day-by-day notes and the long-term roadmap; update them whenever new milestones ship.

## Recent Production Updates

- Imported the full `final_rere_fixtures.json` dataset into Heroku using `scripts/import_final_rere_fixture.py --truncate`, restoring 3,046 MCQs with their structured explanations.
- Added `scripts/generate_final_rere_fixture.py` to regenerate sanitized RERE exports before each import so the production data stays in sync.
- Updated MCQ rendering (`django_neurology_mcq/mcq/views.py` and `templates/mcq/mcq_detail.html`) to support both dict- and list-based answer options, ensuring all choices display correctly after the new data load.
- Disabled `AUTO_LOAD_FIXTURES` in production to prevent legacy dev fixtures from overwriting the curated Heroku dataset during deploys.

## Tech Stack

- Python 3.11, Django 5.x
- SQLite for local development, PostgreSQL in production (`DATABASE_URL`)
- Celery with Redis (`REDIS_URL`) for background processing (Reasoning Pal, case conversion, etc.)
- Gunicorn + WhiteNoise + Bootstrap 5 + custom JS/CSS
- `django-ckeditor` (CKEditor 4) for rich text editing
- OpenAI API (`OPENAI_API_KEY` or `OPENAI_KEY`) for AI features

## Repository Layout

- `django_neurology_mcq/neurology_mcq/` – project settings, urls, wsgi/asgi, Celery app, health checks.
- `django_neurology_mcq/mcq/` – primary app: models, views, AI clients, middleware, Celery tasks, management commands, and templates.
- `django_neurology_mcq/templates/` – project-level templates (`mcq/`, `admin/`).
- `django_neurology_mcq/static/` – authored static assets; run `collectstatic` to populate `django_neurology_mcq/staticfiles/`.
- `mcq/management/commands/` (inside the app) – comprehensive import/export, quality assurance, and maintenance commands.
- `Procfile`, `requirements.txt`, `runtime.txt` – Heroku process types and dependency pins.
- `docs/` and numerous `README_*.md` files – deep dives into imports, AI behaviour, smoke tests, and background processing workflows.

## Getting Started (Local)

1. **Create a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install --upgrade pip
   pip install -r requirements.txt
   ```
2. **Create `.env` at the repository root** (used by `dotenv` in settings):
   ```env
   SECRET_KEY=dev-secret
   DEBUG=true
   REASONING_INLINE=true          # fall back to inline execution if no worker
   OPENAI_API_KEY=sk-...
   OPENAI_MODEL=gpt-5-mini
   # DATABASE_URL=postgres://...   # optional: override SQLite
   # REDIS_URL=redis://localhost:6379/0
   ```
   AI features degrade to mocked responses if no API key is provided.
3. **Run database setup**
   ```bash
   python django_neurology_mcq/manage.py migrate
   python django_neurology_mcq/manage.py collectstatic --noinput
   python django_neurology_mcq/manage.py createsuperuser
   ```
4. **Start the development server**
   ```bash
   python django_neurology_mcq/manage.py runserver
   ```

### Background Tasks

- Preferred: run Redis locally (or point `REDIS_URL` to a managed instance) and start Celery:
  ```bash
  PYTHONPATH=django_neurology_mcq \
  celery -A neurology_mcq.celery_app worker -l info
  ```
- If you do not have a worker or Redis, set `REASONING_INLINE=true` or `CELERY_EAGER=true` so cognitive analysis and case conversion run synchronously.

## Heroku-Parity Local Stack (Docker)

The repository ships with a Docker Compose stack that mirrors the production layout (Heroku-22 base image, Gunicorn, Celery worker, Postgres, Redis). Use it whenever you want a 1:1 reproduction of production issues.

1. **Sync Heroku config (optional but recommended)**
   ```bash
   ./scripts/sync_heroku_env.sh <heroku-app-name>        # defaults to enigmatic-hamlet-38937-db49bd5e9821
   cp .env.example .env.local
   # Copy the secrets you need from .env.heroku into .env.local (do NOT commit either file)
   ```

2. **Pull the production database (optional)**
   ```bash
   ./scripts/sync_heroku_db.sh <heroku-app-name>         # writes into postgres://postgres:postgres@localhost:5432/neurology_mcq
   ```
   You need the Heroku CLI and local PostgreSQL client tools (`pg_dump`, `pg_restore`). The script will drop/recreate the destination database automatically before running `heroku pg:pull`.

3. **Start the stack**
   ```bash
   docker compose up --build
   ```
   - Web UI: http://localhost:8000  
   - Celery worker runs in its own service using the same container image.  
   - The entrypoint runs `migrate` automatically; set `RUN_MIGRATIONS=0` in `.env.local` to disable.  
   - Static collection is skipped by default. Set `RUN_COLLECTSTATIC=1` if you want the full Heroku behaviour.

4. **Iterate**
   The repository is bind-mounted into the containers, so code edits on your host apply immediately. Restart the affected service (`docker compose restart web`) after changing dependencies.

5. **Tear down**
   ```bash
   docker compose down
   docker compose down -v    # also removes Postgres/Redis volumes
   ```

The Docker image is built from the official `heroku/heroku:22` stack and installs Python 3.11 with the same system libraries used by Heroku’s Python buildpack, so anything that works in this environment should behave the same in production.

### Useful Management Commands

- List available commands: `python django_neurology_mcq/manage.py help`.
- Import/export tooling lives under `django_neurology_mcq/mcq/management/commands/` (examples include `import_consolidated_mcqs`, `sync_to_heroku`, `fix_explanation_sections`). Review the related `README_*.md` files before running production scripts.
- Example local import of a consolidated JSON file:
  ```bash
  python django_neurology_mcq/manage.py import_consolidated_mcqs path/to/file.json
  ```

## Environment Variables

| Variable | Default | Purpose |
| --- | --- | --- |
| `SECRET_KEY` | auto-generated fallback (unsafe) | Django secret key; always override in production. |
| `DEBUG` | `false` | Enables Django debug mode; must be `false` in prod. |
| `ALLOWED_HOSTS` | `radiant-gorge-35079.herokuapp.com,...` | Comma-separated hosts served by Django. |
| `DATABASE_URL` | *(unset)* | PostgreSQL connection string for production deployments. |
| `REDIS_URL` | `redis://localhost:6379/0` | Celery broker/result backend; supports `rediss://` with SSL. |
| `OPENAI_API_KEY` / `OPENAI_KEY` | *(unset)* | OpenAI API key used by all AI features. |
| `OPENAI_MODEL` | `gpt-5-mini` | Primary OpenAI model id for completions and reasoning. |
| `OPENAI_TRANSCRIBE_MODEL` | `whisper-1` | Model used for audio transcription in case-based learning. |
| `REASONING_INLINE` | `false` | Force cognitive reasoning tasks to run inline on the web worker. |
| `CELERY_EAGER` | `false` | When `true`, Celery executes tasks synchronously (useful for local dev). |
| `DEBUG_API_TOKEN` | *(unset)* | Optional token for staff-only debug endpoints (send via `X-Debug-Token`). |
| `DYNO` / `RAILWAY_ENVIRONMENT` | set by platforms | Used for environment-specific tuning in code. |

## Deployment (Heroku)

The repository is pre-configured for Heroku (Procfile, Gunicorn, WhiteNoise, Celery). To deploy a fresh instance:

1. **Create the Heroku app & add add-ons**
   ```bash
   heroku create <app-name>
   heroku addons:create heroku-postgresql:standard-0 -a <app-name>
   heroku addons:create heroku-redis:standard-0 -a <app-name>
   ```
2. **Configure required environment variables**
   ```bash
   heroku config:set \
     SECRET_KEY=$(python -c 'import secrets; print(secrets.token_urlsafe(50))') \
     OPENAI_API_KEY=sk-... \
     OPENAI_MODEL=gpt-5-mini \
     ALLOWED_HOSTS=<app-name>.herokuapp.com,your-custom-domain.com \
     DJANGO_SETTINGS_MODULE=neurology_mcq.settings \
     -a <app-name>
   # Optional safety toggles
   heroku config:set REASONING_INLINE=false CELERY_EAGER=false -a <app-name>
   ```
   The app reads database and Redis credentials from `DATABASE_URL` and `REDIS_URL`, which Heroku injects automatically.
3. **Deploy**
   ```bash
   git push heroku stable_version:main
   # or, if using the default main branch
   git push heroku main
   ```
   The `release` process in `Procfile` runs migrations and `collectstatic`. When inspecting production errors, capture a focused stream from the web dyno to avoid noisy router/worker chatter:
   ```bash
   heroku logs --app <app-name> --source app --dyno web.1 --num 200
   ```
   (Add `--tail` while debugging live.)
   We previously tailed logs by default, which made initial debugging slow because Heroku had to stream the entire backlog. Grabbing a bounded snapshot first (`--num 200`) surfaces failures immediately, and you can follow up with `--tail` only after confirming the issue.
4. **Scale the worker (optional but recommended)**
   ```bash
   heroku ps:scale worker=1 -a <app-name>
   ```
   Without a worker you can temporarily set `REASONING_INLINE=true`, but long-running tasks (case conversion, reasoning analysis) will then execute on the web dyno.
5. **Verify**
   - Run smoke checks listed in `scripts/heroku_smoke_test_checklist.md`.
   - Hit `/health/` for a quick status probe.
   - Confirm static assets by loading the main dashboard after deployment.

**Procfile summary**

```
web: python -m gunicorn neurology_mcq.wsgi:application --chdir django_neurology_mcq --log-file - --workers 3 --timeout 120
release: python django_neurology_mcq/manage.py migrate --noinput && python django_neurology_mcq/manage.py collectstatic --noinput
worker: PYTHONPATH=django_neurology_mcq celery -A django_neurology_mcq.neurology_mcq.celery_app worker -l info
```

WhiteNoise serves static files directly from the `web` dyno; no extra CDN configuration is required for baseline deployments.

## Data Import & Maintenance

- Production import pipelines are documented in `README_MCQ_IMPORT.md`, `README_MCQ_UPLOAD_TOOLS.md`, `README_EXPLANATIONS.md`, and related files.
- Automation scripts for Heroku live at the repository root (`deploy_and_import_mcqs.sh`, `upload_mcqs_to_heroku.py`, etc.). Many of them assume authenticated Heroku CLI access.
- When modifying MCQ data, prefer management commands over ad-hoc scripts to keep integrity systems (case conversion caching, explanation validation, etc.) in sync.

## Testing & QA

- Run the Django test suite: `python django_neurology_mcq/manage.py test`.
- Execute the Playwright end-to-end suite once the web app is running locally (or against a staging URL):  
  1. Install browsers if you have not already: `npm run playwright:install`.  
  2. Provide an authenticated staff session by setting `PLAYWRIGHT_ADMIN_USERNAME` / `PLAYWRIGHT_ADMIN_PASSWORD`; optionally pin an MCQ ID with `PLAYWRIGHT_MCQ_ID`.  
  3. Start the target server (e.g. `python django_neurology_mcq/manage.py runserver`).  
  4. Run the tests: `npm run playwright:test`. View HTML reports with `npm run playwright:report`.
- Additional smoke tests and manual QA checklists are provided under `docs/` and files such as `MANUAL_TEST_GUIDE.md`, `BACKGROUND_TASKS_IMPLEMENTATION_COMPLETE.md`, and `scripts/heroku_smoke_test_checklist.md`.

## Further Reading

- `docs/ARCHITECTURE_OVERVIEW.md` – end-to-end system overview.
- `MODALS_AND_AI_README.md` – AI prompt flows, fallbacks, and UI behaviour.
- `BACKGROUND_PROCESSING_GUIDE.md` – Celery/Redis configuration and worker expectations.
- Numerous dated analysis reports capture recent fixes and should be consulted before large data migrations.
