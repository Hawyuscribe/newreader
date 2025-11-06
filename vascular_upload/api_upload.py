#!/usr/bin/env python3
"""
Script to upload MCQs to Heroku via API endpoint
Uses direct HTTP requests with API key authentication
"""

import os
import json
import sys
import requests
import time
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()
HEROKU_API_KEY = os.getenv('HEROKU_API_KEY')

if not HEROKU_API_KEY:
    print("Error: HEROKU_API_KEY not found in environment variables or .env file")
    print("Please set this value and try again")
    sys.exit(1)

def upload_mcqs(file_path, app_name="radiant-gorge-35079", chunk_size=None):
    """
    Uploads MCQs to Heroku app via API
    
    Args:
        file_path: Path to the JSON file containing MCQs
        app_name: Heroku app name
        chunk_size: Optional number of MCQs to upload in each chunk (None = all at once)
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = f"api_upload_{timestamp}.log"
    
    # Log function
    def log(message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"[{timestamp}] {message}"
        print(log_message)
        with open(log_file, "a") as f:
            f.write(log_message + "\n")
    
    log(f"Starting MCQ upload via API for {file_path}")
    
    # Read MCQs from file
    try:
        with open(file_path, 'r') as f:
            mcqs = json.load(f)
        log(f"Loaded {len(mcqs)} MCQs from {file_path}")
    except Exception as e:
        log(f"Error reading file: {str(e)}")
        return False
    
    # API endpoint URL with the actual app URL - try a different endpoint pattern
    api_url = f"https://{app_name}-2b52ba172c1e.herokuapp.com/mcq/import/"
    log(f"Using API endpoint: {api_url}")
    
    # Request headers with API key
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {HEROKU_API_KEY}"
    }
    
    # Determine if we need to chunk the data
    if chunk_size and chunk_size > 0:
        # Split MCQs into chunks
        chunks = [mcqs[i:i + chunk_size] for i in range(0, len(mcqs), chunk_size)]
        log(f"Split data into {len(chunks)} chunks of approximately {chunk_size} MCQs each")
        
        total_created = 0
        total_updated = 0
        total_failed = 0
        
        for i, chunk in enumerate(chunks):
            log(f"Uploading chunk {i+1}/{len(chunks)} with {len(chunk)} MCQs...")
            
            try:
                response = requests.post(api_url, json=chunk, headers=headers)
                
                if response.status_code == 200 or response.status_code == 201:
                    try:
                        result = response.json()
                        created = result.get('created', 0)
                        updated = result.get('updated', 0)
                        failed = result.get('failed', 0)
                        
                        total_created += created
                        total_updated += updated
                        total_failed += failed
                        
                        log(f"Chunk {i+1} results: Created: {created}, Updated: {updated}, Failed: {failed}")
                    except Exception as e:
                        log(f"Error parsing response for chunk {i+1}: {str(e)}")
                else:
                    log(f"Chunk {i+1} upload failed with status code: {response.status_code}")
                    log(f"Response: {response.text}")
                
                # Small delay between chunks to avoid overwhelming the server
                if i < len(chunks) - 1:
                    log("Waiting 2 seconds before next chunk...")
                    time.sleep(2)
                    
            except Exception as e:
                log(f"Error uploading chunk {i+1}: {str(e)}")
        
        log("\nUPLOAD SUMMARY:")
        log(f"Total MCQs Created: {total_created}")
        log(f"Total MCQs Updated: {total_updated}")
        log(f"Total MCQs Failed: {total_failed}")
        
    else:
        # Upload all MCQs at once
        log(f"Uploading all {len(mcqs)} MCQs in a single request...")
        
        try:
            response = requests.post(api_url, json=mcqs, headers=headers)
            
            # Show the raw response regardless of status code
            log(f"Response status code: {response.status_code}")
            log(f"Response headers: {response.headers}")
            log(f"Raw response content: {response.text[:1000]}")  # Show first 1000 chars only
            
            if response.status_code == 200 or response.status_code == 201:
                try:
                    result = response.json()
                    created = result.get('created', 0)
                    updated = result.get('updated', 0)
                    failed = result.get('failed', 0)
                    
                    log("\nUPLOAD SUMMARY:")
                    log(f"MCQs Created: {created}")
                    log(f"MCQs Updated: {updated}")
                    log(f"MCQs Failed: {failed}")
                except Exception as e:
                    log(f"Error parsing response as JSON: {str(e)}")
            else:
                log(f"Upload failed with status code: {response.status_code}")
                return False
        except Exception as e:
            log(f"Error during API request: {str(e)}")
            return False
    
    log("Upload process completed")
    log(f"Log file saved to: {log_file}")
    return True

def upload_combined_file(directory, output_file=None, app_name="radiant-gorge-35079"):
    """
    Combines all vascular chunks into a single file and uploads
    
    Args:
        directory: Directory containing the chunk files
        output_file: Optional output file path for the combined file
        app_name: Heroku app name
    """
    if output_file is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"vascular_combined_{timestamp}.json"
    
    # Get all chunk files
    chunk_files = []
    for filename in os.listdir(directory):
        if filename.startswith("vascular_chunk_") and filename.endswith(".json") and "manifest" not in filename:
            chunk_files.append(os.path.join(directory, filename))
    
    # Sort chunk files numerically
    chunk_files.sort()
    
    # Combine chunks
    all_mcqs = []
    for chunk_file in chunk_files:
        with open(chunk_file, 'r') as f:
            mcqs = json.load(f)
            all_mcqs.extend(mcqs)
    
    # Write combined file
    with open(output_file, 'w') as f:
        json.dump(all_mcqs, f, indent=2)
    
    print(f"Combined {len(chunk_files)} chunk files into {output_file} with {len(all_mcqs)} total MCQs")
    
    # Upload the combined file
    return upload_mcqs(output_file, app_name, chunk_size=50)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  Single file: python api_upload.py <file_path> [chunk_size]")
        print("  Combine chunks: python api_upload.py --combine <directory>")
        sys.exit(1)
    
    if sys.argv[1] == "--combine":
        if len(sys.argv) < 3:
            print("Usage for combine mode: python api_upload.py --combine <directory>")
            sys.exit(1)
        directory = sys.argv[2]
        upload_combined_file(directory)
    else:
        file_path = sys.argv[1]
        chunk_size = None
        if len(sys.argv) >= 3:
            try:
                chunk_size = int(sys.argv[2])
            except ValueError:
                print(f"Invalid chunk size: {sys.argv[2]}")
                sys.exit(1)
        
        upload_mcqs(file_path, chunk_size=chunk_size)