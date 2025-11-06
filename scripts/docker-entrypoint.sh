#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="/app/django_neurology_mcq"

if [ -f "/app/.venv/bin/activate" ]; then
  # shellcheck disable=SC1091
  source /app/.venv/bin/activate
fi

cd /app || exit 1

: "${RUN_MIGRATIONS:=1}"
: "${RUN_COLLECTSTATIC:=1}"

if [ "${RUN_MIGRATIONS}" = "1" ]; then
  python "${PROJECT_ROOT}/manage.py" migrate --noinput
fi

if [ "${RUN_COLLECTSTATIC}" = "1" ]; then
  python "${PROJECT_ROOT}/manage.py" collectstatic --noinput
fi

exec "$@"
