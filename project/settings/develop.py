from project.settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
    }
}

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

# export DJANGO_SETTINGS_MODULE=project.settings.develop
# celery -A project worker -l info
