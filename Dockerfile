# Final, Corrected Dockerfile

# Stage 1: Use an official Python runtime
FROM python:3.11-slim-bookworm

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /code

# Install system dependencies that might be needed
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /code/

# Make the entrypoint script executable
RUN chmod +x /code/entrypoint.sh

# Set the entrypoint script as the startup command
ENTRYPOINT ["/code/entrypoint.sh"]
