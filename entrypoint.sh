#!/bin/sh
# Exit immediately if a command exits with a non-zero status.
set -e

# Run database migrations to create the tables.
echo "Running database migrations..."
python manage.py migrate --noinput

# Create a superuser. The DJANGO_SUPERUSER_... variables will be set
# in our deployment command. This will only run if the user doesn't exist.
echo "Creating superuser..."
python manage.py createsuperuser --noinput || echo "Superuser already exists."

# Start the Gunicorn web server. This is the main command.
# The 'exec' command replaces the shell process with the Gunicorn process.
exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 project_core.wsgi:application
