#\!/usr/bin/env python3
"""
Create smaller MCQ chunks that fit within Heroku's config var limits
Heroku config vars have a 32KB limit per value
"""
import json
import os
from pathlib import Path

def create_small_chunks():
    """Split MCQs into smaller chunks for Heroku config vars"""
    
    # Read all MCQs from existing chunks
    chunks_dir = Path("/Users/tariqalmatrudi/NEWreader/mcq_import_chunks")
    all_mcqs = []
    
    print("Reading existing chunks...")
    for chunk_file in sorted(chunks_dir.glob("chunk_*.json")):
        with open(chunk_file, 'r') as f:
            mcqs = json.load(f)
            all_mcqs.extend(mcqs)
    
    print(f"Total MCQs: {len(all_mcqs)}")
    
    # Create smaller chunks (50 MCQs per chunk to stay under 32KB limit)
    small_chunks_dir = Path("/Users/tariqalmatrudi/NEWreader/small_mcq_chunks")
    small_chunks_dir.mkdir(exist_ok=True)
    
    chunk_size = 50  # Smaller size to ensure we stay under limit
    num_chunks = (len(all_mcqs) + chunk_size - 1) // chunk_size
    
    print(f"Creating {num_chunks} small chunks...")
    
    for i in range(num_chunks):
        start_idx = i * chunk_size
        end_idx = min((i + 1) * chunk_size, len(all_mcqs))
        chunk_mcqs = all_mcqs[start_idx:end_idx]
        
        # Write chunk
        chunk_filename = small_chunks_dir / f"small_chunk_{i:03d}.json"
        with open(chunk_filename, 'w') as f:
            json.dump(chunk_mcqs, f, separators=(',', ':'))  # Compact JSON
        
        # Check file size
        file_size = os.path.getsize(chunk_filename)
        print(f"Created {chunk_filename.name}: {len(chunk_mcqs)} MCQs, {file_size/1024:.1f}KB")
        
        if file_size > 30000:  # Leave some margin under 32KB
            print(f"WARNING: {chunk_filename.name} might be too large\!")
    
    print(f"\n✓ Created {num_chunks} small chunks in {small_chunks_dir}")
    return num_chunks

if __name__ == "__main__":
    create_small_chunks()
EOF < /dev/null