# settings.py

# ...
import os

# Check if we are running on Google Cloud Run
if os.environ.get('GAE_ENV', '').startswith('standard'):
    # This block is for Cloud Run
 
# This new DATABASES setting connects to Google Cloud SQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': '/cloudsql/financialhub-464311:us-central1:my-db-instance',
        'USER': 'postgres',
        'PASSWORD': 'PASTE_YOUR_DATABASE_PASSWORD_HERE',
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
# ...
