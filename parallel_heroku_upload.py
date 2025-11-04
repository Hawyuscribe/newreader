#\!/usr/bin/env python3
"""
Upload MCQ chunks to Heroku in parallel using the Heroku Platform API
"""
import json
import os
import subprocess
import requests
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import base64

APP_NAME = "radiant-gorge-35079-2b52ba172c1e"

def get_heroku_api_token():
    """Get Heroku API token from CLI"""
    try:
        result = subprocess.run(['heroku', 'auth:token'], 
                              capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except:
        print("Error: Could not get Heroku auth token. Please run 'heroku login' first.")
        return None

def upload_config_var(api_token, var_name, var_value):
    """Upload a single config var to Heroku"""
    url = f"https://api.heroku.com/apps/{APP_NAME}/config-vars"
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Accept": "application/vnd.heroku+json; version=3",
        "Content-Type": "application/json"
    }
    
    data = {var_name: var_value}
    
    try:
        response = requests.patch(url, headers=headers, json=data)
        if response.status_code == 200:
            return True, var_name
        else:
            return False, f"{var_name}: {response.status_code} - {response.text}"
    except Exception as e:
        return False, f"{var_name}: {str(e)}"

def upload_chunks_in_parallel():
    """Upload all chunks to Heroku in parallel"""
    api_token = get_heroku_api_token()
    if not api_token:
        return False
    
    # Read tiny chunks
    chunks_dir = Path('/Users/tariqalmatrudi/NEWreader/tiny_mcq_chunks')
    chunk_files = sorted(chunks_dir.glob('tiny_chunk_*.json'))
    
    print(f"Found {len(chunk_files)} chunks to upload")
    print(f"Target app: {APP_NAME}")
    
    # Prepare upload tasks
    upload_tasks = []
    for i, chunk_file in enumerate(chunk_files):
        with open(chunk_file, 'r') as f:
            chunk_data = f.read()
        
        # Base64 encode to handle special characters
        encoded_data = base64.b64encode(chunk_data.encode()).decode()
        var_name = f"MCQ_CHUNK_{i:03d}"
        
        upload_tasks.append((var_name, encoded_data))
    
    print(f"\nUploading {len(upload_tasks)} chunks in parallel...")
    print("This may take a few minutes...")
    
    # Upload in parallel with thread pool
    successful = 0
    failed = 0
    
    with ThreadPoolExecutor(max_workers=10) as executor:
        # Submit all tasks
        future_to_var = {
            executor.submit(upload_config_var, api_token, var_name, var_value): var_name 
            for var_name, var_value in upload_tasks
        }
        
        # Process completed tasks
        for future in as_completed(future_to_var):
            var_name = future_to_var[future]
            try:
                success, result = future.result()
                if success:
                    successful += 1
                    if successful % 50 == 0:
                        print(f"Progress: {successful}/{len(upload_tasks)} uploaded...")
                else:
                    failed += 1
                    print(f"Failed: {result}")
            except Exception as e:
                failed += 1
                print(f"Exception for {var_name}: {str(e)}")
    
    print(f"\n=== Upload Summary ===")
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"Total: {len(upload_tasks)}")
    
    return successful == len(upload_tasks)

def main():
    """Main function"""
    print("MCQ Parallel Upload to Heroku")
    print("=" * 50)
    
    # Check if chunks exist
    chunks_dir = Path('/Users/tariqalmatrudi/NEWreader/tiny_mcq_chunks')
    if not chunks_dir.exists() or not list(chunks_dir.glob('tiny_chunk_*.json')):
        print("Error: No tiny chunks found. Please create them first.")
        return False
    
    # Upload chunks
    if upload_chunks_in_parallel():
        print("\n✅ All chunks uploaded successfully\!")
        print("\nNext step: Run the import script on Heroku")
        print(f"Command: heroku run python import_mcqs_from_config.py --app {APP_NAME}")
        return True
    else:
        print("\n❌ Some chunks failed to upload")
        return False

if __name__ == "__main__":
    main()
