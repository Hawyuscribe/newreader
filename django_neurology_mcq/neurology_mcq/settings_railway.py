import os
from .settings import *

# Configure database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('PGDATABASE', ''),
        'USER': os.environ.get('PGUSER', ''),
        'PASSWORD': os.environ.get('PGPASSWORD', ''),
        'HOST': os.environ.get('PGHOST', ''),
        'PORT': os.environ.get('PGPORT', ''),
    }
}

# Configure allowed hosts
ALLOWED_HOSTS = ['*']

# Enable CSRF trusted origins for railway.app domains
CSRF_TRUSTED_ORIGINS = [
    'https://*.railway.app',
]

# Set up static files
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Set up security settings
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

# Set the timeout for long-running requests
TIMEOUT = 300

# Completely redefine middleware for Railway to ensure correct order
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',  # Messages middleware must come before our custom middleware
    'mcq.middleware.account_expiration.AccountExpirationMiddleware',
    'mcq.middleware.login_required.LoginRequiredMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Set DEBUG based on environment
DEBUG = os.environ.get('DEBUG', 'False') == 'True'