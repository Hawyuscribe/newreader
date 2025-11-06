"""
Celery configuration for Django MCQ application
"""

import os
import ssl
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')

app = Celery('neurology_mcq')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

# Celery configuration for Heroku
_redis_url = os.environ.get('REDIS_URL', 'redis://localhost:6379/0')
_use_ssl = _redis_url.startswith('rediss://')

ssl_opts = {
    'ssl_cert_reqs': ssl.CERT_NONE,
    'ssl_check_hostname': False
} if _use_ssl else None

_eager = os.environ.get('CELERY_EAGER', 'false').lower() == 'true'
app.conf.update(
    broker_url=_redis_url,
    # Use Django cache backend instead of Redis directly to avoid SSL issues
    result_backend='django-db',  # Store results in Django database
    broker_use_ssl=ssl_opts,
    redis_backend_use_ssl=ssl_opts,
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
    # Allow forcing eager execution via env for environments without a worker
    task_always_eager=_eager,
    task_eager_propagates=True,
    # Remove custom routing - use default queue for all tasks
    task_default_queue='celery',
    task_default_exchange_type='direct',
    task_default_routing_key='celery',
    # Ignore results we don't need
    task_ignore_result=True,
    # Store task results even when ignored (for our custom cache storage)
    task_store_eager_result=True,
)

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
