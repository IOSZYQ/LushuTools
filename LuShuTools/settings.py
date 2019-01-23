"""
Django settings for LuShuTools project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import sys
import secretKeys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

SITE_NAME = "LuShuTools"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = secretKeys.DJANGO_SECRET_KEY

# ALLOWED_HOSTS = [".anselected.com", "127.0.0.1"]
ALLOWED_HOSTS = ["*"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # "django_celery_results",
    # 'django_celery_beat',

    'rest_framework',
    'rest_framework.authtoken',
    'sorl.thumbnail',
    'corsheaders',
    'images',

    'Template',
    'Image',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'utilities.djangoUtils.ForceDefaultLanguageMiddleware',
    # 'utilities.djangoUtils.WsgiLogErrors',
    # 'utilities.djangoTLS.TlsRedirect',
    # 'utilities.profiler.ProfileMiddleware',
]

ROOT_URLCONF = 'LuShuTools.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),
                 os.path.join(BASE_DIR, 'templates/mail'),
                 os.path.join(BASE_DIR, 'media/templates/mail'),
                 ]
        ,
        'APP_DIRS': False,
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

WSGI_APPLICATION = 'LuShuTools.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': secretKeys.DB_NAME,
        'USER': secretKeys.DB_USER,
        'PASSWORD': secretKeys.DB_PASSWORD,
        'HOST': secretKeys.DB_HOST,
        'PORT': secretKeys.DB_PORT
    }
}

IMAGE_PRIVATE = False

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'
    },
    'redis': {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://{0}:{1}/1".format(secretKeys.REDIS_HOST, secretKeys.REDIS_PORT),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh_hans'
LOCALE_PATHS =(os.path.join(BASE_DIR, 'locale').replace('\\','/'),)

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.abspath(os.path.join(BASE_DIR, 'media').replace('\\','/'))

GOOGLE_LANGUAGE_CODE = 'zh-CN' #en

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,'static')

# STATICFILES_DIRS = [
    # os.path.abspath(os.path.join(BASE_DIR, 'static').replace('\\','/')),
    # ("css", os.path.join(STATIC_ROOT, 'bootstrap/css')),
    # ("js", os.path.join(STATIC_ROOT, 'bootstrap/js')),

# ]


KF5_API_KEY = secretKeys.KF5_API_KEY

ADMIN_TOKEN = secretKeys.ADMIN_TOKEN

EMAIL_HOST = secretKeys.EMAIL_HOST
EMAIL_PORT = 25
EMAIL_HOST_NAME = "安小奢"
EMAIL_HOST_USER = secretKeys.EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = secretKeys.EMAIL_HOST_PASSWORD

QINIU_ACCESS_KEY = secretKeys.QINIU_ACCESS_KEY
QINIU_SECRET_KEY = secretKeys.QINIU_SECRET_KEY

QINIU_IMAGE_BUCKET = secretKeys.QINIU_IMAGE_BUCKET
QINIU_IMAGE_DOMAIN = secretKeys.QINIU_IMAGE_DOMAIN

QINIU_FILE_BUCKET = secretKeys.QINIU_FILE_BUCKET
QINIU_FILE_DOMAIN = secretKeys.QINIU_FILE_DOMAIN

QINIU_STATIC_BUCKET = secretKeys.QINIU_STATIC_BUCKET
QINIU_STATIC_DOMAIN = secretKeys.QINIU_STATIC_DOMAIN


# celery  配置
CELERY_BROKER_URL = 'redis://{0}:{1}/0'.format(secretKeys.REDIS_HOST, secretKeys.REDIS_PORT)
CELERY_RESULT_BACKEND = CELERY_BROKER_URL
# CELERY_ACCEPT_CONTENT = ['json']
# CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Shanghai'
# CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'


REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 1
}

# TEMPLATE_DIR = os.path.join(MEDIA_ROOT, 'templates/')
# IMAGE_DIR = os.path.join(MEDIA_ROOT, 'images/')