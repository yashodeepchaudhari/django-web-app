"""
Django settings for myproject project.
"""

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-yyhu-!wfkmkwp=j+roqu3o2_w$_8x=1xiax(6+r5=0@lcr-)x*'

DEBUG = True

ALLOWED_HOSTS = ['*']


# AWS S3 Configuration

AWS_ACCESS_KEY_ID = 'AKIATKTTEJNQNJALL6XC'
AWS_SECRET_ACCESS_KEY = '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'

AWS_STORAGE_BUCKET_NAME = 'django-web-app-static-files'
AWS_S3_REGION_NAME = 'ap-south-1'

# CloudFront domain
AWS_S3_CUSTOM_DOMAIN = 'dq9jr854mm6jb.cloudfront.net'

AWS_QUERYSTRING_AUTH = False


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'project',
    'django_cleanup',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates','templates/admin_panel'],
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

WSGI_APPLICATION = 'myproject.wsgi.application'


# Database

DATABASES = {
 'default': {
  'ENGINE': 'django.db.backends.mysql',
  'NAME': 'django-web-app-db',
  'USER': 'admin',
  'PASSWORD': 'Yash12345678',
  'HOST': 'django-web-app-db.cf6um6meuzuz.ap-south-1.rds.amazonaws.com',
  'PORT': '3306',
 }
}


# Password validation

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static Files (S3)

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/"

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# Media files (local)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
