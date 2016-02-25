# -*- coding: utf-8 -*-
# Django settings for socialmonitor project.

import os.path
from decouple import config, Csv
from dj_database_url import parse as dburl

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(PROJECT_PATH)

SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default=[], cast=Csv())


ADMINS = (
    ('Lucas farias', 'lffsantos@gmail.com'),
)

MANAGERS = ADMINS

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

default_dburl = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')

DATABASES = {
    'default' : config('DATABASE_URL', default=default_dburl, cast=dburl),
}

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(PROJECT_PATH, 'static')

AWS_BUCKET_NAME = config('AWS_BUCKET_NAME')
AWS_ACCESS_KEY = config('AWS_ACCESS_KEY')
AWS_SECRET_KEY = config('AWS_SECRET_KEY')

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = config('STATIC_URL').format(AWS_BUCKET_NAME)

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    ('site', os.path.join(PROJECT_PATH, 'sitestatic')),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'socialmonitor.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'socialmonitor.wsgi.application'

INSTALLED_APPS = (
    # django core apps
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    # external apps
    'el_pagination',
    'gunicorn',
    'crispy_forms',
    'djcelery',
    'kombu.transport.django',
    # local apps
    'accounts',
    'staticpages',
    'dashboard',
    'socialmonitor'
    
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                'socialmonitor.context_processors.inject_settings',
            ],
        },
    },
]

# session settings
SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'
SESSION_COOKIE_HTTPONLY = True

# message settings
MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

# auth settings
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'

# django endless pagination settings
ENDLESS_PAGINATION_PREVIOUS_LABEL = u'Anterior'
ENDLESS_PAGINATION_NEXT_LABEL = u'Próximo'

# accounts app settings
REGISTER_MAX_AGE = 60 * 60 * 24 * 7 # in seconds
FORGOT_PASSWORD_MAX_AGE = 60 * 60 * 24 * 7 # in seconds
TWITTER_APP_KEY = 'vB1KdD6fQ4tyrJDBimPEQ'
TWITTER_APP_SECRET = '35vd3cWHMMpiKZpDJPTms0ux8uoD7s2cj9dnqkXtQI'
TWITTER_CALLBACK_URL = 'http://socialmonitor.com:8000/account/connect/twitter/callback/'

# django celery settings
BROKER_URL = 'django://'

CELERY_ALWAYS_EAGER = True

import djcelery
djcelery.setup_loader()


# crispy settings
CRISPY_TEMPLATE_PACK = 'bootstrap'

PROD_ENV = config('PROD_ENV', default=True, cast=bool)

if PROD_ENV:
    STATICFILES_STORAGE = 'djlibcloud.storage.LibCloudStorage'

    LIBCLOUD_PROVIDERS = {
        'default': {
            'type': 'libcloud.storage.types.Provider.S3_SA_EAST',
            'user': AWS_ACCESS_KEY,
            'key': AWS_SECRET_KEY,
            'bucket': AWS_BUCKET_NAME,
            'secure': True,
        },
    }