"""
Django settings for neurology_mcq project.
"""

import os
import dj_database_url
from pathlib import Path
from dotenv import load_dotenv
import ssl

# Load environment variables from .env file
load_dotenv(os.path.join(Path(__file__).resolve().parent.parent.parent, '.env'))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')
if not SECRET_KEY:
    raise RuntimeError("SECRET_KEY environment variable must be set")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'

# Allow configuring hosts via env, with sensible Heroku defaults
ALLOWED_HOSTS = os.environ.get(
    'ALLOWED_HOSTS',
    'radiant-gorge-35079.herokuapp.com,radiant-gorge-35079-2b52ba172c1e.herokuapp.com,localhost,127.0.0.1,testserver'
).split(',')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',  # Add CKEditor
    'mcq',  # Add the MCQ app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add whitenoise for static files
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',  # Messages middleware MUST come before our custom middleware
    'mcq.middleware.account_expiration.AccountExpirationMiddleware',  # Add account expiration middleware
    'mcq.middleware.login_required.LoginRequiredMiddleware',  # Add redirect middleware for unauthenticated users
    'mcq.middleware.temp_mcq_cleanup.TemporaryMCQCleanupMiddleware',  # Add temporary MCQ cleanup middleware
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'neurology_mcq.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'neurology_mcq.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'neurology_mcq.db',  # Using the same DB name
    }
}

# Use PostgreSQL on Heroku
DATABASE_URL = os.environ.get('DATABASE_URL')
if DATABASE_URL:
    DATABASES['default'] = dj_database_url.config(
        default=DATABASE_URL,
        conn_max_age=600,
        ssl_require=True
    )


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Authentication backends - use custom case-insensitive backend
AUTHENTICATION_BACKENDS = [
    'mcq.auth_backends.CaseInsensitiveModelBackend',
    'django.contrib.auth.backends.ModelBackend',
]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Use WhiteNoise for serving static files
# Re-enable manifest storage now that we've cleared the cache
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Login URL
LOGIN_URL = '/login/'

# Messages settings
from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.DEBUG: 'alert-secondary',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

# Basic logging configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(message)s',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
        'mcq': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}

# Shared cache (Redis) for background job status
_redis_url_cache = os.environ.get('REDIS_URL', 'redis://localhost:6379/0')
if _redis_url_cache.startswith('rediss://'):
    CACHES = {
        'default': {
            'BACKEND': 'django_redis.cache.RedisCache',
            'LOCATION': _redis_url_cache,
            'OPTIONS': {
                'CLIENT_CLASS': 'django_redis.client.DefaultClient',
                'CONNECTION_POOL_KWARGS': {'ssl_cert_reqs': ssl.CERT_NONE},
            },
            'TIMEOUT': 3600,
        }
    }
else:
    CACHES = {
        'default': {
            'BACKEND': 'django_redis.cache.RedisCache',
            'LOCATION': _redis_url_cache,
            'OPTIONS': {
                'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            },
            'TIMEOUT': 3600,
        }
    }

# CKEditor Configuration
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': [
            ['Undo', 'Redo', '-', 'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord'],
            ['Styles', 'Format', 'Font', 'FontSize'],
            ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'CopyFormatting', 'RemoveFormat'],
            ['NumberedList', 'BulletedList', 'Outdent', 'Indent', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['TextColor', 'BGColor'],
            ['Link', 'Unlink', 'Anchor'],
            ['Image', 'Table', 'HorizontalRule', 'SpecialChar'],
            ['Source', 'Preview', 'Templates'],
            ['Maximize', 'ShowBlocks']
        ],
        'height': 520,
        'width': '100%',
        'uiColor': '#f7f7f7',
        'removePlugins': 'elementspath',
        'resize_enabled': False,
        'extraPlugins': 'font,colorbutton,justify,div,liststyle,pastefromword,copyformatting,autogrow,tableresize,tabletools',
        'autoGrow_minHeight': 400,
        'autoGrow_maxHeight': 900,
        'autoGrow_onStartup': True,
        'allowedContent': True,
        'contentsCss': ['/static/admin/css/high_yield_document.css'],
        'bodyClass': 'high-yield-editor-body',
        'pasteFromWordRemoveFontStyles': False,
        'pasteFromWordRemoveStyles': False,
        'copyFormatting_keystroke': 'CTRL+SHIFT+C',
        'copyFormatting_applyKeystroke': 'CTRL+SHIFT+V',
        'toolbarCanCollapse': True,
    },
    'specialty_overview': {
        'toolbar': [
            ['Undo', 'Redo', '-', 'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord'],
            ['Styles', 'Format', 'Font', 'FontSize'],
            ['Bold', 'Italic', 'Underline', 'Strike', '-', 'CopyFormatting', 'RemoveFormat'],
            ['NumberedList', 'BulletedList', 'Outdent', 'Indent', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['TextColor', 'BGColor'],
            ['Link', 'Unlink'],
            ['Image', 'Table', 'HorizontalRule'],
            ['Source', 'Preview'],
            ['Maximize']
        ],
        'height': 540,
        'width': '100%',
        'uiColor': '#f7f7f7',
        'extraPlugins': 'font,colorbutton,justify,copyformatting,pastefromword,autogrow,tableresize,tabletools',
        'removePlugins': 'elementspath',
        'resize_enabled': False,
        'allowedContent': True,
        'contentsCss': ['/static/admin/css/high_yield_document.css'],
        'bodyClass': 'high-yield-editor-body',
        'pasteFromWordRemoveFontStyles': False,
        'pasteFromWordRemoveStyles': False,
        'copyFormatting_keystroke': 'CTRL+SHIFT+C',
        'copyFormatting_applyKeystroke': 'CTRL+SHIFT+V',
    }
}

# Celery Configuration for Background Tasks
import ssl

# Get Redis URL and handle SSL configuration for Heroku
redis_url = os.environ.get('REDIS_URL', 'redis://localhost:6379/0')

# Configure SSL for Heroku Redis
if redis_url.startswith('rediss://'):
    # Heroku Redis uses SSL, configure Celery accordingly
    CELERY_BROKER_URL = redis_url
    CELERY_RESULT_BACKEND = redis_url
    CELERY_BROKER_USE_SSL = {
        'ssl_cert_reqs': ssl.CERT_NONE
    }
    CELERY_REDIS_BACKEND_USE_SSL = {
        'ssl_cert_reqs': ssl.CERT_NONE
    }
else:
    # Local development without SSL
    CELERY_BROKER_URL = redis_url
    CELERY_RESULT_BACKEND = redis_url

CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'
CELERY_ENABLE_UTC = True

# Queue configuration - simplified for Heroku
CELERY_TASK_DEFAULT_QUEUE = 'celery'
CELERY_TASK_DEFAULT_EXCHANGE_TYPE = 'direct'
CELERY_TASK_DEFAULT_ROUTING_KEY = 'celery'

# Worker configuration for Heroku
CELERY_WORKER_PREFETCH_MULTIPLIER = 1
CELERY_TASK_ACKS_LATE = True
CELERY_TASK_REJECT_ON_WORKER_LOST = True
