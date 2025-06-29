#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Create and apply database migrations
python manage.py makemigrations api
python manage.py migrate

# Create a superuser using environment variables (if they exist)
# This is the official, non-interactive method.
python manage.py createsuperuser --noinput || echo "Superuser already exists, skipping."

# Collect static files
python manage.py collectstatic --no-input
