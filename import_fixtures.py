#!/usr/bin/env python3
"""
Script to import Django fixtures from uploaded JSON files.
This script is meant to be run on Heroku.
"""
import os
import json
import sys
import django
import glob
from django.db import transaction
from django.core.management import call_command

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
django.setup()

from mcq.models import MCQ, Bookmark, Flashcard, Note, ReasoningSession

def clear_subspecialty(subspecialty):
    """Clear MCQs for a specific subspecialty."""
    count = MCQ.objects.filter(subspecialty=subspecialty).count()
    print(f"Deleting {count} MCQs for {subspecialty}...")
    MCQ.objects.filter(subspecialty=subspecialty).delete()
    print(f"Done clearing {subspecialty} MCQs")
    return count

def clear_all_mcqs():
    """Clear all existing MCQs."""
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
    return count

def import_fixture(fixture_path):
    """Import a Django fixture file."""
    print(f"Importing fixture: {fixture_path}")
    
    try:
        # Count expected MCQs
        with open(fixture_path, 'r') as f:
            data = json.load(f)
            expected_count = len(data)
        
        # Import the fixture
        call_command('loaddata', fixture_path, verbosity=1)
        
        # Verify import count
        return expected_count
    except Exception as e:
        print(f"Error importing fixture: {e}")
        return 0

def import_subspecialty(subspecialty_dir, clear=True):
    """Import all fixtures for a subspecialty."""
    # Get subspecialty name from directory name
    subspecialty = os.path.basename(subspecialty_dir).replace('_', ' ')
    print(f"\nImporting fixtures for {subspecialty}")
    
    # Clear existing MCQs for this subspecialty if requested
    if clear:
        clear_subspecialty(subspecialty)
    
    # Find all fixture files
    fixture_files = sorted(glob.glob(os.path.join(subspecialty_dir, "*.json")))
    
    if not fixture_files:
        print(f"No fixture files found in {subspecialty_dir}")
        return 0
    
    print(f"Found {len(fixture_files)} fixture files")
    
    # Import each fixture
    total_imported = 0
    
    for fixture_file in fixture_files:
        imported = import_fixture(fixture_file)
        total_imported += imported
        print(f"Imported {imported} MCQs from {os.path.basename(fixture_file)}")
    
    print(f"Successfully imported {total_imported} MCQs for {subspecialty}")
    return total_imported

def main():
    """Main function to import fixtures."""
    # Check if a specific subspecialty is requested
    if len(sys.argv) > 1:
        subspecialty_name = sys.argv[1]
        clear_all = "--clear-all" in sys.argv
        
        # Check if it's a directory or a specific file
        if os.path.isdir(subspecialty_name):
            # Import all fixtures in the directory
            import_subspecialty(subspecialty_name, clear=True)
        elif os.path.isfile(subspecialty_name) and subspecialty_name.endswith('.json'):
            # Import a specific fixture file
            print(f"Importing single fixture file: {subspecialty_name}")
            if clear_all:
                clear_all_mcqs()
            import_fixture(subspecialty_name)
        else:
            # Try to find a directory matching the subspecialty name
            normalized_name = subspecialty_name.replace(' ', '_')
            directories = glob.glob(f"fixtures/*{normalized_name}*")
            
            if directories:
                if clear_all:
                    clear_all_mcqs()
                for directory in directories:
                    import_subspecialty(directory, clear=True)
            else:
                print(f"No fixtures found for subspecialty: {subspecialty_name}")
                print("Available subspecialties:")
                subspecialty_dirs = glob.glob("fixtures/*")
                for subdir in subspecialty_dirs:
                    if os.path.isdir(subdir):
                        print(f"- {os.path.basename(subdir).replace('_', ' ')}")
    else:
        # No arguments, import all fixtures
        fixtures_dir = "fixtures"
        if not os.path.isdir(fixtures_dir):
            print(f"Fixtures directory not found: {fixtures_dir}")
            return
        
        print("Importing all fixtures")
        
        # Clear all MCQs first
        clear_all_mcqs()
        
        # Get all subspecialty directories
        subspecialty_dirs = [d for d in glob.glob(os.path.join(fixtures_dir, "*")) if os.path.isdir(d)]
        
        if not subspecialty_dirs:
            print(f"No subspecialty directories found in {fixtures_dir}")
            return
        
        print(f"Found {len(subspecialty_dirs)} subspecialties")
        
        # Import each subspecialty
        total_imported = 0
        
        for subdir in subspecialty_dirs:
            imported = import_subspecialty(subdir, clear=False)
            total_imported += imported
        
        print(f"\nTotal MCQs imported: {total_imported}")
    
    # Verify import
    print("\nVerifying import...")
    total_mcqs = MCQ.objects.count()
    print(f"Total MCQs in database: {total_mcqs}")
    print("\nMCQs by Subspecialty:")
    
    from django.db.models import Count
    for item in MCQ.objects.values("subspecialty").annotate(count=Count("id")).order_by("-count"):
        print(f"  {item['subspecialty']}: {item['count']}")

if __name__ == "__main__":
    main()