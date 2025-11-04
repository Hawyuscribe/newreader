from django.core.management.base import BaseCommand
from django.core.management import call_command
import os
import glob
import json

class Command(BaseCommand):
    help = 'Load MCQ fixtures from JSON files'

    def add_arguments(self, parser):
        parser.add_argument(
            '--directory',
            dest='directory',
            default='fixtures/mcqs',
            help='Directory containing fixture files',
        )
        parser.add_argument(
            '--all',
            action='store_true',
            dest='load_all',
            help='Load all MCQs at once from a single file',
        )
        parser.add_argument(
            '--clear',
            action='store_true',
            dest='clear_existing',
            help='Clear existing MCQs before importing',
        )

    def handle(self, *args, **options):
        fixture_dir = options['directory']
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
        full_path = os.path.join(base_dir, fixture_dir)
        
        if not os.path.exists(full_path):
            self.stderr.write(self.style.ERROR(f'Directory not found: {full_path}'))
            return
            
        if options['clear_existing']:
            self.stdout.write(self.style.WARNING('Clearing existing MCQs...'))
            from mcq.models import MCQ, Bookmark, Flashcard, Note, ReasoningSession
            
            # Count before deletion
            mcq_count = MCQ.objects.count()
            bookmark_count = Bookmark.objects.count()
            flashcard_count = Flashcard.objects.count()
            note_count = Note.objects.count()
            reasoning_count = ReasoningSession.objects.count()
            
            # Delete all related records
            self.stdout.write(f'Deleting {bookmark_count} bookmarks...')
            Bookmark.objects.all().delete()
            
            self.stdout.write(f'Deleting {flashcard_count} flashcards...')
            Flashcard.objects.all().delete()
            
            self.stdout.write(f'Deleting {note_count} notes...')
            Note.objects.all().delete()
            
            self.stdout.write(f'Deleting {reasoning_count} reasoning sessions...')
            ReasoningSession.objects.all().delete()
            
            self.stdout.write(f'Deleting {mcq_count} MCQs...')
            MCQ.objects.all().delete()
            
            self.stdout.write(self.style.SUCCESS('All existing MCQ data cleared.'))
        
        # Load all MCQs from a single file if requested
        if options['load_all']:
            all_mcqs_path = os.path.join(full_path, 'all_mcqs.json')
            if os.path.exists(all_mcqs_path):
                # Count expected MCQs
                try:
                    with open(all_mcqs_path, 'r') as f:
                        fixtures = json.load(f)
                        expected_count = len(fixtures)
                    self.stdout.write(f'Loading all MCQs from {all_mcqs_path} (expected: {expected_count} MCQs)...')
                except Exception as e:
                    self.stderr.write(self.style.WARNING(f'Failed to count MCQs in fixture: {str(e)}'))
                    expected_count = None
                    self.stdout.write(f'Loading all MCQs from {all_mcqs_path}...')
                
                # Check for duplicate PKs
                if expected_count:
                    pk_counts = {}
                    duplicate_pks = set()
                    for item in fixtures:
                        pk = item['pk']
                        pk_counts[pk] = pk_counts.get(pk, 0) + 1
                        if pk_counts[pk] > 1:
                            duplicate_pks.add(pk)
                    
                    if duplicate_pks:
                        self.stderr.write(self.style.WARNING(
                            f'Found {len(duplicate_pks)} distinct PKs with duplicates in the fixture file. '
                            f'This may cause some MCQs to not be imported.'
                        ))
                
                # Load the fixture
                call_command('loaddata', all_mcqs_path, verbosity=1)
                
                # Verify if all expected MCQs were loaded
                from mcq.models import MCQ
                loaded_count = MCQ.objects.count()
                
                if expected_count and loaded_count < expected_count:
                    self.stderr.write(self.style.WARNING(
                        f'Not all MCQs were loaded. Expected: {expected_count}, Loaded: {loaded_count}. '
                        f'This is likely due to primary key conflicts in the fixture file.'
                    ))
                    
                    # Suggest fix
                    self.stdout.write('\nTo fix this issue:')
                    self.stdout.write('1. Run the fix_pk_conflicts.py script')
                    self.stdout.write('2. Clear the database again')
                    self.stdout.write('3. Load the fixed fixture')
            else:
                self.stderr.write(self.style.ERROR(f'All MCQs file not found: {all_mcqs_path}'))
                return
        else:
            # Load each subspecialty fixture separately
            fixture_files = glob.glob(os.path.join(full_path, '*.json'))
            fixture_files = [f for f in fixture_files if os.path.basename(f) != 'all_mcqs.json' and os.path.basename(f) != 'mcq_stats.json']
            
            if not fixture_files:
                self.stderr.write(self.style.ERROR(f'No fixture files found in {full_path}'))
                return
                
            self.stdout.write(f'Found {len(fixture_files)} fixture files to load')
            
            # Count total expected MCQs across all files
            total_expected = 0
            try:
                for fixture_file in fixture_files:
                    with open(fixture_file, 'r') as f:
                        fixtures = json.load(f)
                        total_expected += len(fixtures)
                self.stdout.write(f'Expected to load a total of {total_expected} MCQs')
            except Exception as e:
                self.stderr.write(self.style.WARNING(f'Failed to count total expected MCQs: {str(e)}'))
                total_expected = None
            
            # Load each file
            loaded_count = 0
            for fixture_file in sorted(fixture_files):
                fixture_name = os.path.basename(fixture_file)
                self.stdout.write(f'Loading {fixture_name}...')
                
                try:
                    # Get count from fixture file
                    with open(fixture_file, 'r') as f:
                        fixtures = json.load(f)
                        count = len(fixtures)
                        
                    # Load fixture
                    call_command('loaddata', fixture_file, verbosity=0)
                    loaded_count += count
                    self.stdout.write(self.style.SUCCESS(f'Loaded {count} MCQs from {fixture_name}'))
                except Exception as e:
                    self.stderr.write(self.style.ERROR(f'Error loading {fixture_name}: {str(e)}'))
            
            self.stdout.write(self.style.SUCCESS(f'Successfully loaded {loaded_count} MCQs from fixtures'))
            
            # Verify if all expected MCQs were loaded
            from mcq.models import MCQ
            actual_count = MCQ.objects.count()
            
            if total_expected and actual_count < total_expected:
                self.stderr.write(self.style.WARNING(
                    f'Not all MCQs were loaded. Expected: {total_expected}, Loaded: {actual_count}. '
                    f'This is likely due to primary key conflicts in the fixture files.'
                ))
                
                # Suggest fix
                self.stdout.write('\nTo fix this issue:')
                self.stdout.write('1. Run the fix_pk_conflicts.py script')
                self.stdout.write('2. Clear the database again')
                self.stdout.write('3. Load the fixed fixture')
            
        # Verify import
        from mcq.models import MCQ
        mcq_count = MCQ.objects.count()
        self.stdout.write(self.style.SUCCESS(f'Total MCQs in database: {mcq_count}'))
        
        # Show subspecialty counts
        self.stdout.write('\nMCQs by subspecialty:')
        from django.db.models import Count
        for item in MCQ.objects.values('subspecialty').annotate(count=Count('id')).order_by('subspecialty'):
            self.stdout.write(f"  {item['subspecialty']}: {item['count']}")