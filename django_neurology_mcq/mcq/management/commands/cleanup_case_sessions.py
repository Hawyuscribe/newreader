"""
Django management command to clean up old case learning sessions.
Implements the smart cleanup strategy designed for the persistent session system.
"""

from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from mcq.models import PersistentCaseLearningSession


class Command(BaseCommand):
    help = 'Clean up old case learning sessions based on smart cleanup rules'

    def add_arguments(self, parser):
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Show what would be deleted without actually deleting',
        )
        parser.add_argument(
            '--verbose',
            action='store_true',
            help='Show detailed information about cleanup process',
        )

    def handle(self, *args, **options):
        dry_run = options['dry_run']
        verbose = options['verbose']
        
        now = timezone.now()
        
        # Define cleanup rules as per the session persistence design
        cleanup_rules = [
            # Inactive sessions (not accessed for 24+ hours)
            {
                'name': 'Inactive sessions (24+ hours)',
                'filter': {
                    'is_active': True,
                    'last_activity__lt': now - timedelta(hours=24)
                },
                'action': 'deactivate'
            },
            # Old deactivated sessions (7+ days)
            {
                'name': 'Old deactivated sessions (7+ days)',
                'filter': {
                    'is_active': False,
                    'last_activity__lt': now - timedelta(days=7)
                },
                'action': 'delete'
            },
            # Very old active sessions (3+ days)
            {
                'name': 'Very old active sessions (3+ days)', 
                'filter': {
                    'is_active': True,
                    'last_activity__lt': now - timedelta(days=3)
                },
                'action': 'delete'
            },
            # Sessions with excessive message history (100+ messages, 1+ day old)
            {
                'name': 'Large sessions (100+ messages, 1+ day old)',
                'filter': {
                    'last_activity__lt': now - timedelta(days=1)
                },
                'action': 'delete',
                'custom_filter': lambda qs: qs.filter(
                    session_data__isnull=False
                ).extra(
                    where=["JSON_LENGTH(session_data->'$.messages') > 100"]
                )
            }
        ]
        
        total_deactivated = 0
        total_deleted = 0
        
        for rule in cleanup_rules:
            self.stdout.write(f"\n{'='*60}")
            self.stdout.write(f"Processing: {rule['name']}")
            self.stdout.write('='*60)
            
            # Get base queryset
            qs = PersistentCaseLearningSession.objects.filter(**rule['filter'])
            
            # Apply custom filter if provided
            if 'custom_filter' in rule:
                try:
                    qs = rule['custom_filter'](qs)
                except Exception as e:
                    if verbose:
                        self.stdout.write(
                            self.style.WARNING(
                                f"Custom filter failed for {rule['name']}: {e}"
                            )
                        )
                    continue
            
            count = qs.count()
            
            if count == 0:
                self.stdout.write(
                    self.style.SUCCESS(f"No sessions match this rule.")
                )
                continue
            
            if verbose or dry_run:
                self.stdout.write(f"Found {count} sessions to {rule['action']}:")
                for session in qs[:10]:  # Show first 10
                    age = now - session.last_activity
                    message_count = len(session.session_data.get('messages', []))
                    self.stdout.write(
                        f"  - {session.session_id[:8]}... "
                        f"({session.specialty}, {age.days}d {age.seconds//3600}h old, "
                        f"{message_count} messages)"
                    )
                if count > 10:
                    self.stdout.write(f"  ... and {count - 10} more")
            
            if not dry_run:
                if rule['action'] == 'deactivate':
                    updated = qs.update(is_active=False)
                    total_deactivated += updated
                    self.stdout.write(
                        self.style.SUCCESS(f"Deactivated {updated} sessions")
                    )
                elif rule['action'] == 'delete':
                    deleted_count, _ = qs.delete()
                    total_deleted += deleted_count
                    self.stdout.write(
                        self.style.SUCCESS(f"Deleted {deleted_count} sessions")
                    )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f"DRY RUN: Would {rule['action']} {count} sessions"
                    )
                )
        
        # Summary
        self.stdout.write(f"\n{'='*60}")
        self.stdout.write("CLEANUP SUMMARY")
        self.stdout.write('='*60)
        
        if dry_run:
            self.stdout.write(
                self.style.WARNING("DRY RUN - No actual changes made")
            )
        else:
            self.stdout.write(
                self.style.SUCCESS(
                    f"Sessions deactivated: {total_deactivated}"
                )
            )
            self.stdout.write(
                self.style.SUCCESS(f"Sessions deleted: {total_deleted}")
            )
        
        # Show current statistics
        active_count = PersistentCaseLearningSession.objects.filter(
            is_active=True
        ).count()
        inactive_count = PersistentCaseLearningSession.objects.filter(
            is_active=False
        ).count()
        
        self.stdout.write(f"\nCurrent session count:")
        self.stdout.write(f"  Active: {active_count}")
        self.stdout.write(f"  Inactive: {inactive_count}")
        self.stdout.write(f"  Total: {active_count + inactive_count}")
        
        if not dry_run and (total_deactivated > 0 or total_deleted > 0):
            self.stdout.write(
                self.style.SUCCESS("\n✅ Cleanup completed successfully!")
            )