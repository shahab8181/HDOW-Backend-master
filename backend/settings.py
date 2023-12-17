from pathlib import Path
import os
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
       'file': {
           'level': 'DEBUG',
           'class': 'logging.FileHandler',
           'filename': 'log.django',
       },
    },
    'loggers': {
        'django': {
            'handlers': ['console','file'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}

# DEBUG = 'RENDER' not in os.environ
DEBUG = True

ALLOWED_HOSTS = []

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', default='django-hdow-72anl(u9c&e8_-!93!^v30i!3mvqqzg)v8+y+8*r@98ibe(m^v')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    "whitenoise.runserver_nostatic",
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    #Internal Apps
    'core',
    'client',
    'technician',
    'supervisor',

    # external apps
    'rest_framework',
    'drf_spectacular',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]




ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'backend.wsgi.application'


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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/staticfiles/'

if not DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'core.User'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]



# if 'RENDER' not in os.environ:
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.postgresql_psycopg2',
#             'NAME': 'hdwlocal',
#             'USER': 'postgres',
#             'PASSWORD': 'sosis123',
#             'HOST': '127.0.0.1',
#             'PORT': '5432',
#         }
#     }

# else:
    # DATABASES = {
    #   'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': 'neondb',
    #     'USER': 'negatic',
    #     'PASSWORD': '3x5aLcnbQYBf',
    #     'HOST': 'ep-royal-union-55139652.us-east-2.aws.neon.tech',
    #     'PORT': '5432',
    #     'OPTIONS': {'sslmode': 'require'},
    #   }
    # }
# DATABASES = {
#       'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'hdwdb_vbu2',
#         'USER': 'hdwdb_vbu2_user',
#         'PASSWORD': 'hI7vcMK0nz4pB3S5Je2Ty86OEXlRJkco',
#         'HOST': 'dpg-ckp5tl41tcps739tt490-a',
#         'PORT': '5432',
#         'OPTIONS': {'sslmode': 'require'},
#       }
#     }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

database_url = os.environ.get('DATABASE_URL')
DATABASES['default'] = dj_database_url.parse(database_url)


if DEBUG:
    MEDIA_URL = 'media/'
else:
    MEDIA_URL = '/staticfiles/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'staticfiles/media/')


# TODO: rest frameworl config
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 2,
    # 'DEFAULT_AUTHENTICATION_CLASSES': [
    #     'rest_framework.authentication.BasicAuthentication',
    # ],
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.IsAuthenticated'
    # ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema'
}

# TODO: default spectacular settings
SPECTACULAR_SETTINGS = {
    'TITLE': 'Heart Diagnostic on the Wheel',
    'DESCRIPTION': 'This is a list of APIs and you can use them',
    'VERSION': '1.4.6',
    'SERVE_INCLUDE_SCHEMA': False,
    # OTHER SETTINGS
}
