FROM python:3.11-slim

WORKDIR /app

# Install Flask
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy all files, including templates/
COPY . .

# Expose port
EXPOSE 5000

CMD ["python", "app.py"]
