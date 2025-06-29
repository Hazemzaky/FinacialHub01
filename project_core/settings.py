# ==============================================================================
# FINAL, COMPLETE, AND CORRECT settings.py
# ==============================================================================
import os
import dj_database_url
from pathlib import Path

# This is the crucial line that was missing. It defines the project's base directory.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 'K_SERVICE' not in os.environ

# settings.py

# List of host/domain names that this Django site can serve.
ALLOWED_HOSTS = [
    'my-accounting-app-267387038527.us-central1.run.app', # Your live URL
    '127.0.0.1', # For local development
]
# We will need to add our Cloud Run URL here later if needed, but for now this is okay.


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'api', # Our application
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project_core.urls'

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

WSGI_APPLICATION = 'project_core.wsgi.application'


# settings.py

# ==============================================================================
# FINAL AND CORRECT DATABASE CONFIGURATION
# ==============================================================================

# This new logic handles all three cases: Cloud Run, Cloud Shell, and Local
if os.environ.get('K_SERVICE'):
    # --- Case 1: Running on the live Cloud Run service ---
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'HOST': '/cloudsql/financialhub-464311:us-central1:my-db-instance',
            'USER': 'postgres',
            'PASSWORD': 'TheUltimateFinalPassword123',
            'NAME': 'postgres',
        }
    }
elif os.environ.get('DATABASE_URL'):
    # --- Case 2: Running in Cloud Shell (or another environment with DATABASE_URL) ---
    DATABASES = {
        'default': dj_database_url.config(conn_max_age=600)
    }
else:
    # --- Case 3: Running locally for development ---
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
if not DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STORAGES = {
        "staticfiles": {
            "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
        },
    }

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CORS settings
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'http://127.0.0.1:3000',
    'https://finacial-hub01front.vercel.app', 
    
]
# --- Production Security Settings ---
# Add your live URL to the list of trusted origins for CSRF protection
CSRF_TRUSTED_ORIGINS = [
    'https://my-accounting-app-267387038527.us-central1.run.app',
]
