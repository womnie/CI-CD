# Use a Python 3.10 slim base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file first to leverage Docker's layer caching
COPY requirements.txt .

# Install all required libraries
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files into the working directory
COPY . .

# Command to run the application using Gunicorn when the container starts
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]