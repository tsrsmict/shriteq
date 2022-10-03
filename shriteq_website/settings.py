"""
Django settings for shriteq_website project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

import os
from dotenv import load_dotenv
load_dotenv()

import dotenv

dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)
SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = os.environ['DEBUG'] == 'True'

test = os.environ.get('TEST', None)
IS_TEST_SERVER = False
if test is not None and test == 'True':
    IS_TEST_SERVER = True

print(f"{DEBUG=} {IS_TEST_SERVER=}")

if DEBUG:
    ALLOWED_HOSTS = ['*']
else:
    ALLOWED_HOSTS = [
        '127.0.0.1',
        '.herokuapp.com',
        ".shriteq.org",
        ".canvas4change.com" # for weird domain stuff with shriteq.org - if the domain provider is ever switched, this can be removed
    ]
    
INTERNAL_IPS = [
    "127.0.0.1",
]

if not DEBUG:
    SECURE_SSL_REDIRECT = True

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
if not DEBUG:
    sentry_sdk.init(
    dsn="https://e4da85eac0a94999849088482d581306@o1375280.ingest.sentry.io/6683508",
    integrations=[
        DjangoIntegration(),
    ],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
    )

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',

    'django.contrib.staticfiles',
    'tailwind',
    'theme',

    'django_browser_reload',
    'django_components',
    'ckeditor',
    'ckeditor_uploader',

    'events',
    'accounts',
    'crypt_hunt',
    'pac_man',
]

TAILWIND_APP_NAME = 'theme'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_browser_reload.middleware.BrowserReloadMiddleware',
]

ROOT_URLCONF = 'shriteq_website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'templates',
            'components/templates'
        ],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders':[(
                'django.template.loaders.cached.Loader', [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                    'django_components.template_loader.Loader',
                ]
            )],
        },
    },
]

WSGI_APPLICATION = 'shriteq_website.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_L10N = True
USE_TZ = True


from datetime import datetime
from zoneinfo import ZoneInfo

TIME_ZONE_INFO = ZoneInfo(TIME_ZONE)
# datetime(year, month, day, hour, minute, second, microsecond)
IS_OVERRIDE = (DEBUG == True) or (IS_TEST_SERVER == True)

now = datetime.now(tz=TIME_ZONE_INFO)
OPEN_EVENT_START_TIME = datetime(2022, 10, 8, 9, 0, 0, 0, tzinfo=TIME_ZONE_INFO)
OPEN_EVENT_CLOSE_TIME = datetime(2022, 10, 11, 11, 59, 0, 0, tzinfo=TIME_ZONE_INFO)

IS_IN_EVENT_WINDOW: bool = (now >= OPEN_EVENT_START_TIME and now < OPEN_EVENT_CLOSE_TIME)

DAY_OF_WEEK: int = now.weekday()
IS_WEEKEND: bool = (DAY_OF_WEEK == 5 or DAY_OF_WEEK == 6)

IS_IN_DAY_WINDOW: bool = False

if IS_WEEKEND:
    IS_IN_DAY_WINDOW = (now.hour >= 9 and now.hour < 24)
else:
    IS_IN_DAY_WINDOW = (now.hour >= 15 and now.hour < 24)

OPEN_EVENTS_RUNNING = IS_OVERRIDE or (IS_IN_EVENT_WINDOW and IS_IN_DAY_WINDOW)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "static/" # url on server, eg localhost:8000/static/

# which directories to find static files in. collectstatic will collect them all and put them together when deployed. also needed for tailwind
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    os.path.join(BASE_DIR, "components"),
    os.path.join(BASE_DIR, "pac_man"),
    os.path.join(BASE_DIR, "crypt_hunt"),
]
# what to call the compiled static dir
STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
WHITENOISE_MANIFEST_STRICT = False

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CKEDITOR_UPLOAD_PATH = "uploads/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
