"""
Django settings for cms project.

Generated by 'django-admin startproject' using Django 3.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os

from common.paths import REPO_DIR
from common.paths import TMP_DIR
from common.shared_queue.redis_queue import CRAWLER_FEED
from common.shared_queue.redis_queue import CRAWLER_RESULT
from configurations import Configuration
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/


class Base(Configuration):
    # SECURITY WARNING: keep the secret key used in production secret!
    # TODO Override secret in production
    SECRET_KEY = 'django-insecure-tfv^rapkl5+j5&c+x64-iy3#m+hpmhyj10f^b(ww2xxu&_#78+'

    ALLOWED_HOSTS = [
        os.environ.setdefault('POD_IP', '127.0.0.1'),
        'localhost',
        '0.0.0.0',
    ]

    # Application definition

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'rest_framework',
        'health_check',
        'health_check.db',
        'health_check.storage',
        'health_check.contrib.migrations',
        'django_rq',
        'marketplace',
        'crawler',
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

    ROOT_URLCONF = 'cms.urls'

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

    WSGI_APPLICATION = 'cms.wsgi.application'

    # Password validation
    # https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
    # https://docs.djangoproject.com/en/3.2/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    FIXTURE_DIRS = [
        os.path.join(REPO_DIR, 'fixtures'),
    ]

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'console': {
                'format': '%(asctime)s %(message)s',
                'datefmt': '%H:%M:%S',
            },
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'rq.utils.ColorizingStreamHandler',
                'formatter': 'console',
                'exclude': ['%(asctime)s'],
            },
        },
        'loggers': {
            'root': {
                'handlers': ['console'],
                'level': 'DEBUG',
            },
        }
    }

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/3.2/howto/static-files/

    STATIC_URL = '/admin-static/'

    STATIC_ROOT = os.path.join(REPO_DIR, 'static')

    # Default primary key field type
    # https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

    DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

    RQ_QUEUES = {
        CRAWLER_FEED: {
            'URL': os.getenv('RQ_REDIS_URL', 'redis://localhost:6379/0'),
        },
        CRAWLER_RESULT: {
            'URL': os.getenv('RQ_REDIS_URL', 'redis://localhost:6379/0'),
        },
    }

    RQ_SHOW_ADMIN_LINK = True


class PostgresMixin:
    # Database
    # https://docs.djangoproject.com/en/3.2/ref/settings/#databases
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('DB_NAME', 'byprice24'),
            'USER': os.getenv('DB_USERNAME', 'root'),
            'PASSWORD': os.getenv('DB_PASSWORD', '1234'),
            'HOST': os.getenv('DB_HOST', 'localhost'),
            'PORT': os.getenv('DB_PORT', '5432'),
        }
    }


class Dev(PostgresMixin, Base):
    DEBUG = True


class Test(Dev):
    # Database
    # https://docs.djangoproject.com/en/3.2/ref/settings/#databases
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': TMP_DIR / 'db.sqlite3',
        }
    }


class Prod(PostgresMixin, Base):
    DEBUG = False
