#!/usr/bin/env python3
"""
Final version of MCQ upload script using the correct import_mcqs_json command.
"""
import os
import subprocess
import time
import json
from datetime import datetime

SOURCE_DIR = "/Users/tariqalmatrudi/Documents/MCQs for the board/Previous MCQs/json explained/reclass"
APP_NAME = "radiant-gorge-35079"
LOG_FILE = f"upload_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

# Files already imported
IMPORTED_FILES = [
    "Part I 2023_mcqs_20250515_072926.json",
]

def log_message(message):
    """Log message to console and file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] {message}"
    print(log_line)
    with open(LOG_FILE, 'a') as f:
        f.write(log_line + '\n')

def get_mcq_count():
    """Get current MCQ count from Heroku."""
    cmd = 'heroku run --app radiant-gorge-35079 --no-tty "cd /app/django_neurology_mcq && python manage.py shell -c \'from mcq.models import MCQ; print(MCQ.objects.count())\'"'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    for line in result.stdout.split('\n'):
        if line.strip().isdigit():
            return int(line.strip())
    return None

def upload_json_file(json_file):
    """Upload a JSON file using import_mcqs_json command in chunks."""
    filename = os.path.basename(json_file)
    log_message(f"Processing {filename}")
    
    # Read the original file
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    # Get MCQs (handle both direct list and dict with 'mcqs' key)
    if isinstance(data, dict) and 'mcqs' in data:
        mcqs = data['mcqs']
    else:
        mcqs = data if isinstance(data, list) else []
    
    log_message(f"Found {len(mcqs)} MCQs in {filename}")
    
    # Split into 50-MCQ chunks
    chunk_size = 50
    num_chunks = (len(mcqs) + chunk_size - 1) // chunk_size
    
    successful_chunks = 0
    for i in range(num_chunks):
        chunk_start = i * chunk_size
        chunk_end = min(chunk_start + chunk_size, len(mcqs))
        chunk = mcqs[chunk_start:chunk_end]
        
        # Create chunk file
        chunk_data = {'mcqs': chunk} if isinstance(data, dict) else chunk
        chunk_filename = f"chunk_{i+1}_of_{num_chunks}.json"
        
        with open(chunk_filename, 'w') as f:
            json.dump(chunk_data, f, indent=2)
        
        log_message(f"Uploading chunk {i+1}/{num_chunks} ({len(chunk)} MCQs)")
        
        # Copy chunk to Heroku
        copy_cmd = f'cat {chunk_filename} | heroku run --app {APP_NAME} --no-tty "cat > /tmp/chunk.json"'
        result = subprocess.run(copy_cmd, shell=True, capture_output=True, text=True)
        
        if result.returncode != 0:
            log_message(f"Failed to copy chunk {i+1}: {result.stderr}")
            continue
        
        # Import chunk using import_mcqs_json
        import_cmd = f'heroku run --app {APP_NAME} --no-tty "cd /app/django_neurology_mcq && python manage.py import_mcqs_json /tmp/chunk.json"'
        result = subprocess.run(import_cmd, shell=True, capture_output=True, text=True)
        
        if result.returncode == 0:
            log_message(f"✓ Chunk {i+1} imported successfully")
            successful_chunks += 1
        else:
            log_message(f"✗ Failed to import chunk {i+1}")
            log_message(f"Error: {result.stderr[:200]}")
        
        # Clean up chunk file
        os.remove(chunk_filename)
        
        # Brief pause between chunks
        time.sleep(2)
    
    log_message(f"File summary: {successful_chunks}/{num_chunks} chunks imported")
    return successful_chunks == num_chunks

def main():
    log_message("MCQ Upload Script - Final Version")
    log_message("="*50)
    
    # Get all files to import
    all_files = sorted([f for f in os.listdir(SOURCE_DIR) if f.endswith('.json')])
    remaining_files = [f for f in all_files if f not in IMPORTED_FILES]
    
    log_message(f"Total files: {len(all_files)}")
    log_message(f"Already imported: {len(IMPORTED_FILES)}")
    log_message(f"Remaining to import: {len(remaining_files)}")
    
    if not remaining_files:
        log_message("No files to import!")
        return
    
    # Get initial count
    initial_count = get_mcq_count()
    log_message(f"Initial MCQ count: {initial_count}")
    
    # Process each file
    results = []
    for idx, filename in enumerate(remaining_files, 1):
        log_message(f"\n{'='*50}")
        log_message(f"File {idx}/{len(remaining_files)}: {filename}")
        
        # Get count before
        before_count = get_mcq_count()
        
        # Upload file
        source_path = os.path.join(SOURCE_DIR, filename)
        success = upload_json_file(source_path)
        
        # Get count after
        time.sleep(3)
        after_count = get_mcq_count()
        
        # Record result
        result = {
            'file': filename,
            'success': success,
            'before': before_count,
            'after': after_count,
            'added': after_count - before_count if before_count and after_count else 0
        }
        results.append(result)
        
        log_message(f"Result: {'SUCCESS' if success else 'FAILED'}")
        if before_count and after_count:
            log_message(f"MCQs added: {after_count - before_count}")
            log_message(f"Total MCQs: {after_count}")
        
        # Longer pause between files
        if idx < len(remaining_files):
            log_message("Waiting 5 seconds before next file...")
            time.sleep(5)
    
    # Final summary
    log_message(f"\n{'='*50}")
    log_message("FINAL SUMMARY")
    log_message(f"{'='*50}")
    
    successful = sum(1 for r in results if r['success'])
    failed = len(results) - successful
    
    log_message(f"Total files processed: {len(results)}")
    log_message(f"Successful: {successful}")
    log_message(f"Failed: {failed}")
    
    # Final count
    final_count = get_mcq_count()
    log_message(f"\nFinal MCQ count: {final_count}")
    if initial_count and final_count:
        log_message(f"Total MCQs added: {final_count - initial_count}")
    
    # Save detailed results
    results_file = f"upload_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(results_file, 'w') as f:
        json.dump({
            'timestamp': datetime.now().isoformat(),
            'initial_count': initial_count,
            'final_count': final_count,
            'results': results
        }, f, indent=2)
    
    log_message(f"\nResults saved to: {results_file}")
    log_message(f"Log saved to: {LOG_FILE}")

if __name__ == "__main__":
    main()