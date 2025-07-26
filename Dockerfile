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
