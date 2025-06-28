# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /code/

# Expose port 8080 to the outside world
EXPOSE 8080

# Run the application using gunicorn
# Cloud Run automatically sets the PORT environment variable.
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 project_core.wsgi:application
