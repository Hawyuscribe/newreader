#!/bin/bash
# Script to deploy the MCQ import management command to Heroku
# Usage: ./deploy_heroku_command.sh

set -e

# Heroku app name
HEROKU_APP="radiant-gorge-35079"

# Management command path
COMMAND_PATH="/Users/tariqalmatrudi/NEWreader/mcq/management/commands/import_mcqs_heroku.py"

# Check if management command exists
if [[ ! -f "$COMMAND_PATH" ]]; then
    echo "Error: Management command not found at $COMMAND_PATH"
    exit 1
fi

# Check if we're logged in to Heroku
if ! heroku auth:whoami &>/dev/null; then
    echo "Not logged in to Heroku. Please run 'heroku login' first."
    exit 1
fi

echo "=== Deploying MCQ Import Management Command to Heroku ==="
echo "App: $HEROKU_APP"

# Create management directories if they don't exist
echo "Creating management directories..."
heroku run "mkdir -p mcq/management/commands" --app "$HEROKU_APP"

# Upload the command file
echo "Uploading management command..."
cat "$COMMAND_PATH" | heroku run "cat > mcq/management/commands/import_mcqs_heroku.py" --app "$HEROKU_APP"

# Create __init__.py files
echo "Creating __init__.py files..."
heroku run "touch mcq/management/__init__.py mcq/management/commands/__init__.py" --app "$HEROKU_APP"

echo "=== Deployment Completed Successfully ==="
echo "You can now use the import_mcqs_heroku.sh script to import MCQs to Heroku."