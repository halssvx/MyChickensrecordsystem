# Use official Python image as base
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy your app code
COPY . /app

# Install dependencies (Flask, sqlite3 is builtin)
RUN pip install flask

# Expose port 5000
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
