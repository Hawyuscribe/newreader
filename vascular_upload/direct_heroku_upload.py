import os
import json
import requests
import sys
from dotenv import load_dotenv

# Load environment variables for API key
load_dotenv()
HEROKU_API_KEY = os.getenv('HEROKU_API_KEY')

if not HEROKU_API_KEY:
    print("Error: HEROKU_API_KEY environment variable not set.")
    print("Please set this in a .env file or directly in your environment.")
    sys.exit(1)

def upload_mcq_chunk(chunk_file_path, app_name="radiant-gorge-35079"):
    """
    Uploads a chunk of MCQs directly to the Heroku app via API
    """
    # Read the chunk file
    try:
        with open(chunk_file_path, 'r') as f:
            mcqs = json.load(f)
    except Exception as e:
        print(f"Error reading chunk file: {e}")
        return False

    # Prepare headers for the API request
    headers = {
        "Accept": "application/vnd.heroku+json; version=3",
        "Authorization": f"Bearer {HEROKU_API_KEY}",
        "Content-Type": "application/json"
    }

    # Endpoint to add MCQs (replace with your actual API endpoint)
    api_url = f"https://{app_name}.herokuapp.com/api/mcqs/bulk-import/"

    # Make the API request
    try:
        print(f"Uploading {len(mcqs)} MCQs to {app_name}...")
        response = requests.post(api_url, headers=headers, json=mcqs)
        
        if response.status_code == 200 or response.status_code == 201:
            print("Upload successful!")
            try:
                result = response.json()
                print(f"Created: {result.get('created', 0)}")
                print(f"Updated: {result.get('updated', 0)}")
                print(f"Failed: {result.get('failed', 0)}")
            except:
                print("Response received but couldn't parse JSON result.")
            return True
        else:
            print(f"Upload failed with status code: {response.status_code}")
            print(f"Response: {response.text}")
            return False
    except Exception as e:
        print(f"Error during API request: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python direct_heroku_upload.py <path_to_chunk_file>")
        sys.exit(1)
    
    chunk_file = sys.argv[1]
    upload_mcq_chunk(chunk_file)