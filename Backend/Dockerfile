# Use the official Python 3.11 image as a base image
FROM python:3.11

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any dependencies specified in requirement.txt
RUN pip install -r requirements.txt

# Instalar g++
RUN apt-get update && apt-get install -y g++

# Instalar Ruby
RUN apt-get update && apt-get install -y ruby

# Instalar Node.js y npm
RUN curl -fsSL https://deb.nodesource.com/setup_lts.x | bash -
RUN apt-get install -y nodejs

# Instalar PHP
RUN apt-get update && apt-get install -y php

# Expose port 5000 for the application to listen on (if your app does)
EXPOSE 5000

# Specify the command to run your application
CMD ["python3", "app.py"]