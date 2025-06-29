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

# Copy the entire project
COPY . /code/

# Copy the entrypoint script and make it executable
COPY entrypoint.sh /code/entrypoint.sh
RUN chmod +x /code/entrypoint.sh

# Expose port 8080 to the outside world
EXPOSE 8080

# Set the entrypoint script as the startup command for the container
ENTRYPOINT ["/code/entrypoint.sh"]
