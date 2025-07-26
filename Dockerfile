<<<<<<< HEAD
FROM python:3.11-slim

WORKDIR /app

# Install Flask
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy app files
COPY app.py .
COPY templates/ templates/
COPY static/ static/

# Expose port
EXPOSE 5000

CMD ["python", "app.py"]
=======
# Use the official Python image
FROM python:3.11-slim

# Set a working directory
WORKDIR /app

# Copy the script into the container
COPY chickens_ui.py .

# Set the default command to run the script
CMD ["python", "chickens_ui.py"]
>>>>>>> 2856b688be88e2ce7737b0d52462f6b4f0bdf666
