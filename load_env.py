"""
Helper script to load environment variables from .env file
Run this before starting Django or include it in your startup script
"""

import os
from pathlib import Path
try:
    from dotenv import load_dotenv
except ImportError:
    print("python-dotenv not installed. Please install it with: pip install python-dotenv")
    import sys
    sys.exit(1)

# Get the project root directory
project_root = Path(__file__).resolve().parent

# Load environment variables from .env file
load_dotenv(os.path.join(project_root, '.env'))

# Test if the API key was loaded
api_key = os.environ.get('OPENAI_API_KEY')
if api_key:
    print(f"OpenAI API key loaded successfully (first 5 chars: {api_key[:5]}...)")
else:
    print("Warning: OpenAI API key not found in environment variables")