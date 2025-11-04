# API Key Setup Instructions

This application requires an OpenAI API key to enable AI features like MCQ explanations and answer verification.

## Current Setup

Your OpenAI API key should be configured in a `.env` file at the root of the project. This file should contain a line like:

```
OPENAI_API_KEY=sk-your-openai-key
```

The application will now automatically load this API key whenever it starts.

## How It Works

1. A `.env` file in the project root stores your API key
2. The `load_env.py` script loads this environment variable
3. The Django settings have been modified to load this file at startup
4. The startup scripts (`keep_django_running.sh` and `run_django_dev.sh`) have been updated to run `load_env.py`

## If You Need to Change the API Key

1. Edit the `.env` file in the project root
2. Replace the existing API key with your new one
3. Restart the Django server

## Troubleshooting

If you encounter API key issues:

1. Verify the `.env` file exists and contains the correct API key
2. Run `python3 load_env.py` to test environment variable loading
3. Check the Django logs for any API-related errors
4. Ensure python-dotenv is installed: `pip install python-dotenv`

The `.env` file is excluded from Git in the `.gitignore` file to prevent accidentally committing your API key to the repository.
