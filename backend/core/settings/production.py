import os

from .base import *  # noqa: F403, F401
import dj_database_url

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('SQL_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': os.environ.get('SQL_DATABASE', os.path.join(BASE_DIR, 'db.sqlite3')),
        'USER': os.environ.get('SQL_USER', 'user'),
        'PASSWORD': os.environ.get('SQL_PASSWORD', 'password'),
        'HOST':  os.environ.get('SQL_HOST', 'host'),
        'PORT': os.environ.get('SQL_PORT', '5432')
    }
}

CSRF_TRUSTED_ORIGINS=['https://getit.iiitdmj.ac.in']
