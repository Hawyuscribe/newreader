"""
Management command to clear MCQ case conversion cache
"""

from django.core.management.base import BaseCommand
from django.core.cache import cache
from mcq.models import MCQ
from mcq.mcq_case_converter import get_mcq_cache_key, clear_mcq_cache
from mcq.end_to_end_integrity import e2e_integrity


class Command(BaseCommand):
    help = 'Clear MCQ case conversion cache'

    def add_arguments(self, parser):
        parser.add_argument(
            '--mcq-id',
            type=int,
            help='Clear cache for specific MCQ ID',
        )
        parser.add_argument(
            '--all',
            action='store_true',
            help='Clear cache for all MCQs',
        )
        parser.add_argument(
            '--list',
            action='store_true',
            help='List cached MCQ conversions',
        )

    def handle(self, *args, **options):
        if options['list']:
            self.list_cached_mcqs()
        elif options['mcq_id']:
            self.clear_specific_mcq(options['mcq_id'])
        elif options['all']:
            self.clear_all_mcq_cache()
        else:
            self.stdout.write(
                self.style.WARNING(
                    'Please specify --mcq-id, --all, or --list'
                )
            )

    def list_cached_mcqs(self):
        """List all cached MCQ conversions"""
        self.stdout.write("📋 Listing cached MCQ conversions:")
        
        cached_count = 0
        total_mcqs = MCQ.objects.count()
        
        for mcq in MCQ.objects.all():
            cache_key = get_mcq_cache_key(mcq.id)
            cached_data = cache.get(cache_key)
            
            if cached_data:
                cached_count += 1
                cache_used = cached_data.get('cache_used', False)
                cache_timestamp = cached_data.get('cache_timestamp', 'Unknown')
                
                self.stdout.write(
                    f"  MCQ #{mcq.id}: ✅ Cached"
                    f" | Last used: {cache_timestamp}"
                    f" | From cache: {cache_used}"
                )
        
        self.stdout.write(
            self.style.SUCCESS(
                f"\n📊 Summary: {cached_count}/{total_mcqs} MCQs have cached conversions"
            )
        )

    def clear_specific_mcq(self, mcq_id):
        """Clear cache for specific MCQ"""
        try:
            mcq = MCQ.objects.get(id=mcq_id)
            clear_mcq_cache(mcq_id)
            
            # Also clear integrity data
            e2e_integrity.clear_all_integrity_data(mcq_id=mcq_id)
            
            self.stdout.write(
                self.style.SUCCESS(
                    f"✅ Cleared cache and integrity data for MCQ #{mcq_id}"
                )
            )
        except MCQ.DoesNotExist:
            self.stdout.write(
                self.style.ERROR(
                    f"❌ MCQ #{mcq_id} not found"
                )
            )

    def clear_all_mcq_cache(self):
        """Clear cache for all MCQs"""
        self.stdout.write("🗑️ Clearing cache and integrity data for all MCQ conversions...")
        
        cleared_count = 0
        total_mcqs = MCQ.objects.count()
        
        for mcq in MCQ.objects.all():
            cache_key = get_mcq_cache_key(mcq.id)
            if cache.get(cache_key):
                clear_mcq_cache(mcq.id)
                e2e_integrity.clear_all_integrity_data(mcq_id=mcq.id)
                cleared_count += 1
        
        # Clear general integrity caches
        e2e_integrity.clear_all_integrity_data()
        
        self.stdout.write(
            self.style.SUCCESS(
                f"✅ Cleared cache and integrity data for {cleared_count}/{total_mcqs} MCQs"
            )
        )