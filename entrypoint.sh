#!/bin/sh
set -e

echo "Running database migrations..."
python manage.py migrate --noinput

echo "Creating superuser..."
python manage.py createsuperuser --noinput || echo "Superuser already exists."
    
echo "Starting Gunicorn server..."
exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 project_core.wsgi:application
