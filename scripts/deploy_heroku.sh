#!/usr/bin/env bash
set -euo pipefail

# Heroku app name can be overridden with HEROKU_APP env var
APP="${HEROKU_APP:-radiant-gorge-35079}"

echo "Deploying to Heroku app: $APP"

branch=$(git rev-parse --abbrev-ref HEAD)
echo "Current branch: $branch"

echo "Ensuring heroku remote points to $APP..."
if git remote get-url heroku >/dev/null 2>&1; then
  :
else
  heroku git:remote -a "$APP"
fi

echo "Pushing to Heroku (main preferred, fallback to master)..."
set +e
git push heroku HEAD:main
status=$?
if [ $status -ne 0 ]; then
  echo "main push failed, attempting master..."
  git push heroku HEAD:master
  status=$?
fi
set -e

if [ $status -ne 0 ]; then
  echo "Push failed. Are you logged in with 'heroku login' and have access to $APP?" >&2
  exit $status
fi

echo "Restarting dynos..."
heroku ps:restart -a "$APP"

echo "Deployment complete."
