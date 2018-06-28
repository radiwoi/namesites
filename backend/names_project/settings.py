"""
Django settings for names_project project.

Generated by 'django-admin startproject' using Django 2.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(0wm6p3li_)$6jazgvjn0doj0e-ub6a851bo(*y0v7oy42_b7q'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

ALLOWED_HOSTS = ['34.254.119.140', 'pojknamn.se', 'flicknamn.se']

# USE_X_FORWARDED_HOST = True

HOST_URL = 'http://34.254.119.140'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'djcelery',
    'djcelery_email',
    'api'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'names_project.urls'

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

WSGI_APPLICATION = 'names_project.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'names_project',
        'USER': 'root',
        'PASSWORD': 'wL>c83Ev6&4V7j9',
         # wL>c83Ev6&4V7j9
         # walmart LAPTOP > coffee 8 3 EGG visa 6 & 4 VISA 7 jack 9
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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

DEFAULT_AUTHENTICATION_CLASSES = [
    'names_project.auth_classes.CsrfExemptSessionAuthentication'
]

# CELERY setup
# CELERY_BROKER_URL = 'amqp://guest:guest@localhost:5672/'

# SetUp Celery Email backend, and the SMTP server configurations

# EMAIL_HOST = 'mail.pojknamn.se'

# EMAIL_PORT = '25' # 587 for tls

# EMAIL_HOST_USER = 'emailsender'

# EMAIL_HOST_PASSWORD = 'V(hpwf=S4jWG6=='

# EMAIL_USE_TLS = True   # TLS settings

# EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'
EMAIL_HOST = 'email-smtp.eu-west-1.amazonaws.com'
EMAIL_PORT = 465
EMAIL_USE_TLS = True

# EMAIL_HEADER = 'Trololo'

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# local
# BOY_NAMES_URL = "http://localhost:8081/"
# GIRL_NAMES_URL = "http://localhost:8082/"

# dev
BOY_NAMES_URL = "pojknamn.se"
GIRL_NAMES_URL = "flicknamn.se"

CORS_ORIGIN_ALLOW_ALL = True

# CORS_ORIGIN_WHITELIST = (
#     '<YOUR_DOMAIN>[:PORT]',
# )


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
STATIC_ROOT = 'static_files/'
STATIC_URL = '/static/'

PER_PAGE = 5
PER_PAGE_POPULAR = 20
