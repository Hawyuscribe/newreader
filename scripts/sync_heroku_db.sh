#!/usr/bin/env bash
set -euo pipefail

HEROKU_APP="${1:-enigmatic-hamlet-38937-db49bd5e9821}"
LOCAL_DB_URL="${2:-postgres://postgres:postgres@localhost:5432/neurology_mcq}"

if ! command -v heroku >/dev/null 2>&1; then
  echo "Heroku CLI not found. Install it from https://devcenter.heroku.com/articles/heroku-cli" >&2
  exit 1
fi

if ! command -v pg_dump >/dev/null 2>&1; then
  echo "PostgreSQL client tools (pg_dump, pg_restore) are required on your machine." >&2
  exit 1
fi

parse_url() {
  python - <<'PY' "$1"
from urllib.parse import urlparse
import sys

url = urlparse(sys.argv[1])
db = url.path.lstrip('/') or 'postgres'
print(
    db,
    url.username or 'postgres',
    url.hostname or 'localhost',
    url.port or 5432,
    url.password or '',
)
PY
}

read DB_NAME DB_USER DB_HOST DB_PORT DB_PASSWORD <<<"$(parse_url "${LOCAL_DB_URL}")"

export PGPASSWORD="${DB_PASSWORD}"

echo "Recreating local database ${DB_NAME} on ${DB_HOST}:${DB_PORT}"
dropdb --if-exists --host "${DB_HOST}" --port "${DB_PORT}" --username "${DB_USER}" "${DB_NAME}" || true
createdb --host "${DB_HOST}" --port "${DB_PORT}" --username "${DB_USER}" "${DB_NAME}"

unset PGPASSWORD

echo "Pulling Heroku DATABASE_URL into ${LOCAL_DB_URL}"
heroku pg:pull --app "${HEROKU_APP}" DATABASE_URL "${LOCAL_DB_URL}"

echo "Database sync complete."
