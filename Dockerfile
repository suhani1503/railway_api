# Use the official Python image from Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Expose the port that Flask will run on
EXPOSE 5000

# Command to run the Flask app
CMD ["flask", "run"]
