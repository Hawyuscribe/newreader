#!/usr/bin/env bash
set -euo pipefail

# Configure Heroku app for ReasoningPal reliability and audio transcription.
# Usage: OPENAI_API_KEY=sk-... ./scripts/heroku_reasoningpal_setup.sh <HEROKU_APP_NAME>

APP="${1:-}"
if [[ -z "$APP" ]]; then
  echo "Usage: OPENAI_API_KEY=sk-... $0 <HEROKU_APP_NAME>" >&2
  exit 1
fi

if ! command -v heroku >/dev/null 2>&1; then
  echo "Heroku CLI not found. Install from https://devcenter.heroku.com/articles/heroku-cli" >&2
  exit 1
fi

if [[ -z "${OPENAI_API_KEY:-}" ]]; then
  echo "OPENAI_API_KEY env var is required. Example: OPENAI_API_KEY=sk-... $0 $APP" >&2
  exit 1
fi

echo "🔎 Verifying app: $APP"
heroku apps:info -a "$APP" >/dev/null

echo "⚙️  Setting core config vars"
heroku config:set \
  OPENAI_API_KEY="${OPENAI_API_KEY}" \
  OPENAI_MODEL="gpt-5-mini" \
  OPENAI_TRANSCRIBE_MODEL="whisper-1" \
  REASONING_INLINE="true" \
  PYTHONUNBUFFERED="1" \
  -a "$APP"

echo "✅ Config set. Current relevant vars:"
heroku config:get OPENAI_MODEL OPENAI_TRANSCRIBE_MODEL REASONING_INLINE -a "$APP"

cat <<'NOTE'

Next steps:
- Deploy code: git push heroku HEAD:main (or your branch), or via CI.
- Smoke test:
  1) Log in as staff and visit /debug/openai-selftest/ (should return chat_ok: true).
  2) Open an MCQ, submit ReasoningPal; Step 2 should finish and show results (inline mode).
  3) Record a short audio clip in the modal; transcription should return 200 (no 500).

Optional (enable background workers later):
- Provision Redis and a worker dyno, then disable inline mode for tasks:
    heroku addons:create heroku-redis:hobby-dev -a $APP
    heroku ps:scale worker=1 -a $APP
    heroku config:unset REASONING_INLINE CELERY_EAGER -a $APP

NOTE

echo "🚀 Done."

