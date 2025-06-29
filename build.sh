#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# STEP 1: Create the migration files for our 'api' app
python manage.py makemigrations api

# STEP 2: Apply those migrations to build the tables in the database
python manage.py migrate

# STEP 3: Collect static files
python manage.py collectstatic --no-input
