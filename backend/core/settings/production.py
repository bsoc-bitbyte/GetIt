import os

from .base import *  # noqa: F403, F401
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
}

CSRF_TRUSTED_ORIGINS=['https://getit.iiitdmj.ac.in']
