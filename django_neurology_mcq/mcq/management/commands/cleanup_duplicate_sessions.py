"""
Management command to clean up duplicate MCQ case conversion sessions
"""

from django.core.management.base import BaseCommand
from django.db.models import Count
from mcq.models import MCQCaseConversionSession
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Clean up duplicate MCQ case conversion sessions'
    
    def add_arguments(self, parser):
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Show what would be deleted without actually deleting',
        )
        parser.add_argument(
            '--verbose',
            action='store_true',
            help='Show detailed output',
        )
    
    def handle(self, *args, **options):
        dry_run = options['dry_run']
        verbose = options['verbose']
        
        self.stdout.write("🧹 Cleaning up duplicate MCQ case conversion sessions...")
        
        # Find MCQ/User combinations with multiple sessions
        duplicates = (
            MCQCaseConversionSession.objects
            .values('mcq_id', 'user_id')
            .annotate(count=Count('id'))
            .filter(count__gt=1)
            .order_by('-count')
        )
        
        total_duplicates = duplicates.count()
        sessions_to_delete = 0
        
        if total_duplicates == 0:
            self.stdout.write(self.style.SUCCESS("✅ No duplicate sessions found"))
            return
        
        self.stdout.write(f"Found {total_duplicates} MCQ/User combinations with duplicates")
        
        for duplicate in duplicates:
            mcq_id = duplicate['mcq_id']
            user_id = duplicate['user_id']
            count = duplicate['count']
            
            if verbose:
                self.stdout.write(f"  MCQ {mcq_id}, User {user_id}: {count} sessions")
            
            # Get all sessions for this MCQ/User combination
            sessions = MCQCaseConversionSession.objects.filter(
                mcq_id=mcq_id,
                user_id=user_id
            ).order_by('-created_at')
            
            # Keep the most recent session, mark others for deletion
            sessions_to_keep = sessions.first()
            sessions_to_remove = sessions[1:]  # All except the first (most recent)
            
            if verbose:
                self.stdout.write(f"    Keeping session {sessions_to_keep.id} (created: {sessions_to_keep.created_at})")
            
            for session in sessions_to_remove:
                sessions_to_delete += 1
                if verbose:
                    self.stdout.write(f"    {'Would delete' if dry_run else 'Deleting'} session {session.id} (created: {session.created_at}, status: {session.status})")
                
                if not dry_run:
                    session.delete()
        
        if dry_run:
            self.stdout.write(
                self.style.WARNING(f"🔍 DRY RUN: Would delete {sessions_to_delete} duplicate sessions")
            )
            self.stdout.write("Run without --dry-run to actually delete the duplicates")
        else:
            self.stdout.write(
                self.style.SUCCESS(f"✅ Deleted {sessions_to_delete} duplicate sessions")
            )
            self.stdout.write(f"Kept {total_duplicates} most recent sessions")
        
        # Summary
        remaining_sessions = MCQCaseConversionSession.objects.count()
        self.stdout.write(f"📊 Total sessions remaining: {remaining_sessions}")