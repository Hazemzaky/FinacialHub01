# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Set Django superuser credentials from build arguments
ARG DJANGO_SUPERUSER_USERNAME
ARG DJANGO_SUPERUSER_EMAIL
ARG DJANGO_SUPERUSER_PASSWORD

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Run database migrations and create superuser during the build
# This is our last attempt at this method.
RUN python manage.py migrate --noinput
RUN python manage.py createsuperuser --noinput || echo "Superuser already exists."

# Expose port 8080
EXPOSE 8080

# The command to run when the container starts
CMD ["gunicorn", "--bind", ":8080", "--workers", "1", "--threads", "8", "--timeout", "0", "project_core.wsgi:application"]
