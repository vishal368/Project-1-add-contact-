# Use the official Python slim image as the base
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory in the container
WORKDIR /CONTACT_APP

# Copy the requirements (if you have a requirements.txt, otherwise install Flask directly)
# For simplicity, we'll install Flask directly here
RUN pip install --upgrade pip

# Install Flask
RUN pip install Flask

# Copy the application code into the container
COPY . /CONTACT_APP

# Expose port 5000
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]