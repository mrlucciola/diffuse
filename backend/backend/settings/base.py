"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 2.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from datetime import timedelta

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CLIENT_DIR = f"{os.path.dirname(BASE_DIR)}/client"
# print(f"{os.path.dirname(BASE_DIR)}/client/")
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'sik7-u%y&@fntqsi0$_64^zt-z6k9miel%v(lv93s)yy_=$j6u'

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # rest and api stuff
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    
    # my apps
    'core',
    'user',
    'project',
    # 'comment',
    # 'history',
]

########################################################################################################################
###################################################### REST & JWT ######################################################
# from: https://medium.com/swlh/django-rest-framework-with-react-jwt-authentication-part-1-a24b24fa83cd
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}

# from https://dev-yakuza.github.io/en/django/jwt/
JWT_AUTH = {
    'JWT_SECRET_KEY': SECRET_KEY,
    'JWT_ALGORITHM': 'HS256',
    'JWT_ALLOW_REFRESH': True,
    'JWT_EXPIRATION_DELTA': timedelta(days=7),
    'JWT_REFRESH_EXPIRATION_DELTA': timedelta(days=28),
}

# from https://medium.com/swlh/django-rest-framework-with-react-jwt-authentication-part-1-a24b24fa83cd
JWT_AUTH['JWT_RESPONSE_PAYLOAD_HANDLER'] = 'simple_rest.utils.custom_jwt_response_handler'
REST_USE_JWT = True
LOGIN_URL = 'login'
###################################################### REST & JWT ######################################################
########################################################################################################################

##################################################################################################################
###################################################### CORS ######################################################
CORS_ALLOW_CREDENTIALS = True
###################################################### CORS ######################################################
##################################################################################################################

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'corsheaders.middleware.CorsMiddleware',
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
        'DIRS': [CLIENT_DIR],
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


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
ALLOWED_HOSTS = ["178.128.146.249", "diffcult.com", "0.0.0.0", "127.0.0.1", "localhost"]
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'diffuse',
    }
}
if "/www/" in BASE_DIR:
    from os import environ
    DATABASES["default"]["USER"] = environ.get("diffuse_mongo_user")
    DATABASES["default"]["PASSWORD"] = environ.get("diffuse_mongo_pwd")
    DATABASES["default"]["HOST"] = '127.0.0.1'
    DATABASES["default"]["PORT"] = 27017

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
AUTH_USER_MODEL = 'user.CustomUser'

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(CLIENT_DIR,'build')# f"{os.path.dirname(BASE_DIR)}/client/build/"
STATICFILES_DIRS = (
    os.path.join(CLIENT_DIR, "build", "static"),  # update the STATICFILES_DIRS
)

# CSRF_USE_SESSIONS = True