#!/usr/bin/env bash
set -euo pipefail

HEROKU_APP="${1:-enigmatic-hamlet-38937-db49bd5e9821}"
OUTPUT_FILE="${2:-.env.heroku}"

if ! command -v heroku >/dev/null 2>&1; then
  echo "Heroku CLI not found. Install it from https://devcenter.heroku.com/articles/heroku-cli" >&2
  exit 1
fi

echo "Fetching config vars for Heroku app: ${HEROKU_APP}"
tmp_file="$(mktemp)"
trap 'rm -f "${tmp_file}"' EXIT

heroku config --app "${HEROKU_APP}" --json >"${tmp_file}"

python - "$tmp_file" "$OUTPUT_FILE" <<'PY'
import json
import sys
from pathlib import Path

source, destination = sys.argv[1], sys.argv[2]
with open(source, "r", encoding="utf-8") as fh:
    data = json.load(fh)

lines = []
for key, value in sorted(data.items()):
    value = "" if value is None else str(value)
    if "\n" in value:
        value = value.replace("\n", "\\n")
    lines.append(f"{key}={value}")

content = "\n".join(lines) + "\n"
Path(destination).write_text(content, encoding="utf-8")
PY

echo "Wrote $(wc -l < "${OUTPUT_FILE}") variables to ${OUTPUT_FILE}"
echo "Review the file and copy the required entries into .env.local (do not commit secrets to git)."
