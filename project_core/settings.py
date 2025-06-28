# settings.py

# ...
import os

# Check if we are running on Google Cloud Run
if os.environ.get('GAE_ENV', '').startswith('standard'):
    # This block is for Cloud Run
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'HOST': '/cloudsql/YOUR_CONNECTION_NAME', # <-- Paste the Connection Name here
            'USER': 'postgres',
            'PASSWORD': 'YOUR_STRONG_PASSWORD', # <-- Use the password you set
            'NAME': 'postgres', # Default database name
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
