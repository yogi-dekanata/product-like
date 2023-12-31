# Use the official Python image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install necessary dependencies
RUN apt-get update && \
    apt-get install -y gcc python3-dev libpq-dev

# Upgrade pip and install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# Set the working directory inside the container
WORKDIR /app

# Copy the entire project into the container's working directory
COPY . /app/

# Define the command to run the application using Gunicorn
CMD ["gunicorn", "FavShop.wsgi:application", "--bind", "0.0.0.0:8000"]

# Copy entrypoint script into the image
COPY entrypoint.sh /entrypoint.sh

# Make the script executable
RUN chmod +x /entrypoint.sh

# Set the entrypoint script
ENTRYPOINT ["/entrypoint.sh"]