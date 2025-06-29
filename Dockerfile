# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# First, copy the requirements file and install dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Next, copy the entrypoint script
COPY entrypoint.sh /code/entrypoint.sh

# Now, copy the rest of the project code
COPY . /code/

# Finally, make the entrypoint script executable
# This is a more robust way to set permissions
RUN chmod +x ./entrypoint.sh

# Expose port 8080 to the outside world
EXPOSE 8080

# Set the entrypoint script as the startup command
ENTRYPOINT ["./entrypoint.sh"]
