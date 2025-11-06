#!/usr/bin/env python3
"""
Generate commands for manually importing MCQs on Heroku console.
This script creates a set of Python commands that can be run directly in the Heroku console.
"""
import os
import json
import argparse
from pathlib import Path

# Configuration
FIXTURES_DIR = "/Users/tariqalmatrudi/NEWreader/fixtures"
OUTPUT_DIR = "/Users/tariqalmatrudi/NEWreader/import_commands"

def generate_clear_command():
    """Generate command to clear all MCQs."""
    return """
from mcq.models import MCQ, Bookmark, Flashcard, Note, ReasoningSession

# Delete related models first
bookmark_count = Bookmark.objects.count()
print(f"Deleting {bookmark_count} bookmarks...")
Bookmark.objects.all().delete()

flashcard_count = Flashcard.objects.count()
print(f"Deleting {flashcard_count} flashcards...")
Flashcard.objects.all().delete()

note_count = Note.objects.count()
print(f"Deleting {note_count} notes...")
Note.objects.all().delete()

reasoning_count = ReasoningSession.objects.count()
print(f"Deleting {reasoning_count} reasoning sessions...")
ReasoningSession.objects.all().delete()

# Finally delete MCQs
count = MCQ.objects.count()
print(f"Deleting {count} MCQs...")
MCQ.objects.all().delete()
print("Done clearing all MCQs")
"""

def generate_clear_subspecialty_command(subspecialty):
    """Generate command to clear MCQs for a specific subspecialty."""
    return f"""
from mcq.models import MCQ

# Delete MCQs for {subspecialty}
count = MCQ.objects.filter(subspecialty="{subspecialty}").count()
print(f"Deleting {{count}} MCQs for {subspecialty}...")
MCQ.objects.filter(subspecialty="{subspecialty}").delete()
print(f"Done clearing {subspecialty} MCQs")
"""

def generate_import_command(fixture_file, batch_size=25):
    """Generate command to import MCQs from a fixture file."""
    # Load fixture data
    with open(fixture_file, "r") as f:
        fixture_data = json.load(f)
    
    # Split into batches
    batches = []
    for i in range(0, len(fixture_data), batch_size):
        batches.append(fixture_data[i:i+batch_size])
    
    commands = []
    
    for i, batch in enumerate(batches):
        command = f"""
# Import batch {i+1} of {len(batches)} from {os.path.basename(fixture_file)}
from django.db import transaction
from mcq.models import MCQ

# MCQ data for this batch
fixture_data = {json.dumps(batch, indent=2)}

# Import MCQs
with transaction.atomic():
    imported = 0
    for mcq_data in fixture_data:
        try:
            # Create MCQ from fixture data
            model_name = mcq_data['model']
            if model_name != 'mcq.mcq':
                continue
                
            # Get fields
            fields = mcq_data['fields']
            mcq_id = mcq_data['pk']
            
            # Create or update the MCQ
            mcq, created = MCQ.objects.update_or_create(
                id=mcq_id,
                defaults=fields
            )
            
            imported += 1
        except Exception as e:
            print(f"Error importing MCQ: {{e}}")
    
    print(f"Successfully imported {{imported}} MCQs")
"""
        commands.append(command)
    
    return commands

def generate_verify_command():
    """Generate command to verify the import."""
    return """
from mcq.models import MCQ
from django.db.models import Count

# Get total MCQ count
total_mcqs = MCQ.objects.count()
print(f"Total MCQs in database: {total_mcqs}")

# Get subspecialty counts
print("MCQs by subspecialty:")
for item in MCQ.objects.values("subspecialty").annotate(count=Count("id")).order_by("-count"):
    print(f"  {item['subspecialty']}: {item['count']}")
"""

def main():
    """Main function to generate import commands."""
    parser = argparse.ArgumentParser(description="Generate commands for manually importing MCQs on Heroku console")
    parser.add_argument("--subspecialty", help="Only generate commands for this subspecialty")
    parser.add_argument("--fixtures-dir", default=FIXTURES_DIR, help="Directory containing fixture files")
    parser.add_argument("--output-dir", default=OUTPUT_DIR, help="Directory to save command files")
    parser.add_argument("--batch-size", type=int, default=25, help="Number of MCQs per batch")
    parser.add_argument("--file", help="Generate commands for a specific fixture file")
    
    args = parser.parse_args()
    
    # Create output directory
    os.makedirs(args.output_dir, exist_ok=True)
    
    # Generate clear command
    clear_file = os.path.join(args.output_dir, "00_clear_all_mcqs.py")
    with open(clear_file, "w") as f:
        f.write(generate_clear_command())
    
    print(f"Generated clear command: {clear_file}")
    
    # Generate import commands
    if args.file:
        # Generate commands for a specific file
        file_path = args.file
        if not os.path.isfile(file_path):
            print(f"File not found: {file_path}")
            return
        
        print(f"Generating commands for {file_path}")
        commands = generate_import_command(file_path, args.batch_size)
        
        for i, command in enumerate(commands):
            command_file = os.path.join(args.output_dir, f"import_{os.path.basename(file_path)}_{i+1}_of_{len(commands)}.py")
            with open(command_file, "w") as f:
                f.write(command)
            
            print(f"Generated import command: {command_file}")
    elif args.subspecialty:
        # Generate commands for a specific subspecialty
        subspecialty_dir = os.path.join(args.fixtures_dir, args.subspecialty.replace(" ", "_").replace("/", "_"))
        if not os.path.isdir(subspecialty_dir):
            # Try to find a matching directory
            for dirname in os.listdir(args.fixtures_dir):
                if args.subspecialty.lower() in dirname.lower() and os.path.isdir(os.path.join(args.fixtures_dir, dirname)):
                    subspecialty_dir = os.path.join(args.fixtures_dir, dirname)
                    break
        
        if not os.path.isdir(subspecialty_dir):
            print(f"No fixtures directory found for subspecialty: {args.subspecialty}")
            return
        
        print(f"Generating commands for {args.subspecialty} from {subspecialty_dir}")
        
        # Generate clear subspecialty command
        clear_subspec_file = os.path.join(args.output_dir, f"01_clear_{args.subspecialty.replace(' ', '_').replace('/', '_')}.py")
        with open(clear_subspec_file, "w") as f:
            f.write(generate_clear_subspecialty_command(args.subspecialty))
        
        print(f"Generated clear subspecialty command: {clear_subspec_file}")
        
        # Find all fixture files
        fixture_files = sorted([f for f in os.listdir(subspecialty_dir) if f.endswith(".json")])
        if not fixture_files:
            print(f"No fixture files found in {subspecialty_dir}")
            return
        
        print(f"Found {len(fixture_files)} fixture files")
        
        # Generate import commands for each fixture
        file_count = 0
        for i, fixture_file in enumerate(fixture_files):
            file_path = os.path.join(subspecialty_dir, fixture_file)
            print(f"Generating commands for {fixture_file}")
            
            commands = generate_import_command(file_path, args.batch_size)
            
            for j, command in enumerate(commands):
                file_count += 1
                command_file = os.path.join(args.output_dir, f"02_{i+1:02d}_{j+1:02d}_import_{fixture_file}.py")
                with open(command_file, "w") as f:
                    f.write(command)
                
                print(f"Generated import command: {command_file}")
    else:
        # Generate commands for all fixtures
        print("Generating commands for all fixtures")
        
        # Find all subspecialty directories
        subspecialty_dirs = [d for d in os.listdir(args.fixtures_dir) if os.path.isdir(os.path.join(args.fixtures_dir, d))]
        if not subspecialty_dirs:
            print(f"No subspecialty directories found in {args.fixtures_dir}")
            return
        
        print(f"Found {len(subspecialty_dirs)} subspecialties")
        
        file_count = 0
        
        # Generate import commands for each subspecialty
        for i, subdir in enumerate(subspecialty_dirs):
            subspecialty = subdir.replace("_", " ")
            print(f"Generating commands for {subspecialty}")
            
            # Generate clear subspecialty command
            clear_subspec_file = os.path.join(args.output_dir, f"01_{i+1:02d}_clear_{subdir}.py")
            with open(clear_subspec_file, "w") as f:
                f.write(generate_clear_subspecialty_command(subspecialty))
            
            print(f"Generated clear subspecialty command: {clear_subspec_file}")
            
            # Find all fixture files
            subdir_path = os.path.join(args.fixtures_dir, subdir)
            fixture_files = sorted([f for f in os.listdir(subdir_path) if f.endswith(".json")])
            if not fixture_files:
                print(f"No fixture files found in {subdir_path}")
                continue
            
            print(f"Found {len(fixture_files)} fixture files")
            
            # Generate import commands for each fixture
            for j, fixture_file in enumerate(fixture_files):
                file_path = os.path.join(subdir_path, fixture_file)
                print(f"Generating commands for {fixture_file}")
                
                commands = generate_import_command(file_path, args.batch_size)
                
                for k, command in enumerate(commands):
                    file_count += 1
                    command_file = os.path.join(args.output_dir, f"02_{i+1:02d}_{j+1:02d}_{k+1:02d}_import_{fixture_file}.py")
                    with open(command_file, "w") as f:
                        f.write(command)
                    
                    print(f"Generated import command: {command_file}")
    
    # Generate verify command
    verify_file = os.path.join(args.output_dir, "99_verify_import.py")
    with open(verify_file, "w") as f:
        f.write(generate_verify_command())
    
    print(f"Generated verify command: {verify_file}")
    
    # Create README
    readme_file = os.path.join(args.output_dir, "README.md")
    with open(readme_file, "w") as f:
        f.write("""# MCQ Import Commands

This directory contains Python commands for importing MCQs into Heroku.

## How to use these commands

1. Open the Heroku dashboard: https://dashboard.heroku.com/apps/radiant-gorge-35079
2. Go to the 'More' dropdown and select 'Run Console'
3. Start a Python console: `python manage.py shell`
4. Copy and paste the contents of each file into the console in order:
   - First, run the clear command: `00_clear_all_mcqs.py`
   - Then run each import command in numerical order
   - Finally, run the verify command: `99_verify_import.py`

## Tips

- Copy the entire file content at once, the shell can handle multiple line inputs
- Wait for each command to complete before running the next one
- If you encounter errors, check the console output for details
""")
    
    print(f"Generated README: {readme_file}")
    
    print(f"\nCommands are ready for use. Follow the instructions in {readme_file}")

if __name__ == "__main__":
    main()