# Use the official Python 3.11 image as a base image
FROM python:3.11

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any dependencies specified in requirement.txt
RUN pip install -r requirements.txt

# Specify the command to run your application
CMD ["python3", "app.py"]
