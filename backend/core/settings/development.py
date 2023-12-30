from .base import *  # noqa: F403, F401

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        # dj_database_url.config(default=os.environ.get('DATABASE_URL'))
        # dj_database_url.parse(os.environ.get("DATABASE_URL"))
    }
}
