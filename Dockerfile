# Use the official Python image
FROM python:3.11-slim

# Set a working directory
WORKDIR /app

# Copy the script into the container
COPY chickens_ui.py .

# Set the default command to run the script
CMD ["python", "chickens_ui.py"]
