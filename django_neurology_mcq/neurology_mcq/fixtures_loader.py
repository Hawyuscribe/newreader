"""
Fixtures loader module to autoload MCQ fixtures when the app initializes.
This module can be imported in the Django app's ready() method.
"""

import os
import logging
import glob
from django.conf import settings
from django.core.management import call_command
from django.db.models import Count

logger = logging.getLogger(__name__)

def should_load_fixtures():
    """
    Determines if fixtures should be loaded automatically.
    This checks if the MCQ table is empty and if fixtures exist.
    """
    try:
        from mcq.models import MCQ
        return MCQ.objects.count() == 0
    except Exception as e:
        logger.error(f"Error checking if fixtures should be loaded: {e}")
        return False

def load_fixtures():
    """
    Load fixtures from the fixtures/mcqs directory if the MCQ table is empty.
    """
    try:
        # Import inside the function to avoid circular imports
        from mcq.models import MCQ
        
        # Check if fixtures are already loaded
        existing_count = MCQ.objects.count()
        if existing_count > 0:
            logger.info(f"Fixtures already loaded - found {existing_count} MCQs")
            return
        
        base_dir = settings.BASE_DIR
        fixtures_path = os.path.join(base_dir, 'fixtures', 'mcqs')
        all_mcqs_path = os.path.join(fixtures_path, 'all_mcqs.json')
        
        if not os.path.exists(fixtures_path):
            logger.warning(f"Fixtures directory not found: {fixtures_path}")
            return
            
        if os.path.exists(all_mcqs_path):
            # Count expected MCQs in fixture
            try:
                import json
                with open(all_mcqs_path, 'r') as f:
                    expected_count = len(json.load(f))
                logger.info(f"Auto-loading fixtures from {all_mcqs_path} (expected: {expected_count} MCQs)")
            except Exception as e:
                logger.warning(f"Failed to count MCQs in fixture: {e}")
                expected_count = None
                logger.info(f"Auto-loading fixtures from {all_mcqs_path}")
            
            # Load the fixtures
            call_command('loaddata', all_mcqs_path, verbosity=0)
            loaded_count = MCQ.objects.count()
            
            if expected_count and loaded_count < expected_count:
                logger.warning(f"Not all MCQs were loaded. Expected: {expected_count}, Loaded: {loaded_count}")
                logger.warning("This could be due to primary key conflicts in the fixture file.")
                logger.warning("Consider running the fix_pk_conflicts.py script to resolve these issues.")
            else:
                logger.info(f"Fixtures loaded successfully - {loaded_count} MCQs")
        else:
            logger.info("Loading fixtures from individual files")
            fixture_files = glob.glob(os.path.join(fixtures_path, '*.json'))
            fixture_files = [f for f in fixture_files if os.path.basename(f) != 'all_mcqs.json' and os.path.basename(f) != 'mcq_stats.json']
            
            if not fixture_files:
                logger.warning(f"No fixture files found in {fixtures_path}")
                return
                
            logger.info(f"Found {len(fixture_files)} fixture files")
            
            # Count total expected MCQs
            total_expected = 0
            try:
                import json
                for fixture_file in fixture_files:
                    with open(fixture_file, 'r') as f:
                        total_expected += len(json.load(f))
                logger.info(f"Expected to load {total_expected} MCQs from individual files")
            except Exception as e:
                logger.warning(f"Failed to count MCQs in individual fixtures: {e}")
                total_expected = None
            
            # Load fixtures
            for fixture_file in sorted(fixture_files):
                logger.info(f"Loading {os.path.basename(fixture_file)}")
                call_command('loaddata', fixture_file, verbosity=0)
            
            loaded_count = MCQ.objects.count()
            
            if total_expected and loaded_count < total_expected:
                logger.warning(f"Not all MCQs were loaded. Expected: {total_expected}, Loaded: {loaded_count}")
                logger.warning("This could be due to primary key conflicts in the fixture files.")
                logger.warning("Consider running the fix_pk_conflicts.py script to resolve these issues.")
            else:
                logger.info(f"Fixtures loaded successfully - {loaded_count} MCQs")
        
        # Log subspecialty counts
        subspecialty_counts = []
        for item in MCQ.objects.values('subspecialty').annotate(count=Count('id')).order_by('subspecialty'):
            subspecialty_counts.append(f"{item['subspecialty']}: {item['count']}")
        
        logger.info(f"MCQs by subspecialty: {', '.join(subspecialty_counts)}")
        
    except Exception as e:
        logger.error(f"Error loading fixtures: {e}")