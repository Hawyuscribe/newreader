from django.apps import AppConfig
import os


class McqConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mcq'
    
    def ready(self):
        """
        Automatically load fixtures when the app is ready,
        but only if we're not running a management command.
        This prevents fixtures from loading twice when using manage.py.
        """
        import sys
        if 'runserver' in sys.argv or 'gunicorn' in sys.argv[0]:
            # Only auto-load fixtures if AUTO_LOAD_FIXTURES is enabled
            # This can be disabled by setting AUTO_LOAD_FIXTURES=False in .env
            if os.environ.get('AUTO_LOAD_FIXTURES', 'True').lower() == 'true':
                from neurology_mcq.fixtures_loader import load_fixtures
                load_fixtures()
