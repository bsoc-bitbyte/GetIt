import os
from pathlib import Path
from dotenv import load_dotenv
import logging

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()

SECRET_KEY = os.environ.get('DJANGO_SECRET', 'default')
STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY', 'default')
STRIPE_WEBHOOK_SECRET = os.environ.get('STRIPE_WEBHOOK_SECRET', 'default')

DEBUG = os.environ.get('DEBUG') != 'False'

ALLOWED_HOSTS = ['*']

CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = ['http://localhost:3000',
                         'https://merch-site.netlify.app',
                         'https://deploy-preview-*--merch-site.netlify.app'
                         ]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework_simplejwt',
    'django_extensions',
    'rest_framework',
    'django_filters',
    'drf_yasg',
    'core',
    'accounts',
    'products',
    'events',
    'tickets',
    'orders'
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'request_logging.middleware.LoggingMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'core.wsgi.application'

AUTH_USER_MODEL = 'accounts.Account'

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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
ADMINS = [(name.strip(), email.strip()) for entry in os.getenv('DJANGO_ADMINS', '').split(';') if entry for name, email in [entry.split(',')]]


# Logging

LOG_DIRECTORY = os.getenv('LOG_DIRECTORY', '~/logs/getit/')
if not os.path.exists(LOG_DIRECTORY):
    os.makedirs(LOG_DIRECTORY)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module}:{process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 1024*1024*10,  # 10MB
            'backupCount': 10,
            'filename': os.path.join(LOG_DIRECTORY, 'backend.log'),
            'formatter': 'verbose',
        },
        'mail_admins': {
            'level': 'CRITICAL',
            'class': 'django.utils.log.AdminEmailHandler',
        },
    },
    'loggers': {
        'root': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'django': {
            'handlers': ['console', 'file', 'mail_admins'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.request': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': False,
        },
        'getit': {
            'handlers': ['console', 'file', 'mail_admins'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}

REQUEST_LOGGING_HTTP_4XX_LOG_LEVEL=logging.WARNING
REQUEST_LOGGING_ENABLE_COLORIZE=False
