# Use the official Python image from Docker Hub
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose port 5000 to allow access to the web server
EXPOSE 5000

# Command to run the application
CMD ["python", "src/main.py"]

