"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 1.10.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import json

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SETTINGS_DIR = os.path.dirname(__file__)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

key = os.path.join(SETTINGS_DIR, "keys.json")
with open(key) as data_file:
    data = json.load(data_file)
    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = data["secret_key"]
    AWS_ACCESS_KEY_ID = data["aws_access_key_id"] # Change this with something else
    AWS_SECRET_ACCESS_KEY = data["aws_secret_access_key"] # Change this with something else

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MANUALLY_BUILT_APPS = [
    "core",
    "sample_app",
]
INSTALLED_APPS += MANUALLY_BUILT_APPS

THIRD_PARTY_APPS = [
    "storages" # for S3 integration
]
INSTALLED_APPS += THIRD_PARTY_APPS

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],
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

WSGI_APPLICATION = 'project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = False # Set to False for import optimizations

USE_L10N = True

USE_TZ = True


# AWS S3 BOTO SETTINGS
# STATIC AND MEDIA SETTINGS ARE IN the local.py and production.py
AWS_STORAGE_BUCKET_NAME = "ailabsexample" # Change this with something else
STATICFILES_STORAGE = 'core.classes.StaticStorage' # For moving our staticfiles to the bucket
DEFAULT_FILE_STORAGE = 'core.classes.MediaStorage' # For moving our media files to the bucket
AWS_S3_DOMAIN = "%s.s3.amazonaws.com" % AWS_STORAGE_BUCKET_NAME
AWS_QUERYSTRING_AUTH = False # This is used to remove the extra paramters like Signatures and ACCESS KEY ID
# AWS_CLOUDFRONT_DOMAIN = ""

# Speeds up your site
# AWS_HEADERS = {
#     'Expires': 'Thu, 15 Apr 2010 20:00:00 GMT',
#     'Cache-Control': 'max-age=86400',
# }
