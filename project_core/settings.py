# settings.py

# ...
import os

# Check if we are running on Google Cloud Run
# ==============================================================================
# CORRECTED DATABASE CONFIGURATION (COPY THIS ENTIRE BLOCK)
# ==============================================================================

# Check if we are running on Google Cloud Run
if os.environ.get('GAE_ENV', '').startswith('standard'):
    # This block is for Cloud Run
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'HOST': '/cloudsql/financialhub-464311:us-central1:my-db-instance',
            'USER': 'postgres',
            'PASSWORD': 'a7b9c2d8e1f0g9h8i7j6k5l4m3n2o1p',
            'NAME': 'postgres',
        }
    }
else:
    # This block is for local development (falls back to sqlite)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
