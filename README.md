🐔 CHICKENS MANAGER - FLASK + SQLITE + MINIKUBE APP
This is a simple and fun CRUD (Create, Read, Update, Delete) web app for managing a list of chickens. It's built using Flask, stores data in a SQLite database, and is containerized and deployed with Kubernetes using Minikube.

🌟 Features
View a list of chickens 🐔

Add new chickens ✍️

Edit chicken names 📝

Delete chickens ❌

Auto-seeds the database with 6 chickens if empty

Built with Flask + SQLite + Bootstrap

Fully containerized and deployable via Kubernetes

🗂️ Project Structure
php
Copy
Edit
<pre lang="text"><code>📁 chickensIU/ ├── 📄 app.py # Main Flask application ├── 📁 templates/ # HTML templates folder │ └── 📄 index.html # Frontend HTML (Bootstrap) ├── 📁 static/ # Optional custom styles │ └── 📄 styles.css # CSS styling (optional) ├── 📄 Dockerfile # Docker image definition ├── 📄 deployment.yaml # Kubernetes deployment and service configuration └── 📄 chickens.db # Auto-created SQLite DB (for local dev only) </code></pre>
▶️ How to Run Locally (Without Docker)
Create a virtual environment

bash
Copy
Edit
python -m venv venv
Activate the environment

On macOS/Linux:

bash
Copy
Edit
source venv/bin/activate
On Windows:

bash
Copy
Edit
venv\Scripts\activate
Install Flask

bash
Copy
Edit
pip install flask
Run the app

bash
Copy
Edit
python app.py
Open your browser and visit: http://localhost:5000

🐳 Dockerizing the App
Your Dockerfile should look like this:

dockerfile
Copy
Edit
FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN pip install flask
EXPOSE 5000
CMD ["python", "app.py"]
Build and run the Docker image locally

bash
Copy
Edit
docker build -t chickens-app .
docker run -p 5000:5000 chickens-app
🚀 Deploying to Kubernetes (Minikube)
1. Start Minikube
bash
Copy
Edit
minikube start
2. Use Minikube's Docker Daemon
This ensures your local Docker image is available inside Minikube.

On Linux/macOS:

bash
Copy
Edit
eval $(minikube -p minikube docker-env)
On Windows PowerShell:

powershell
Copy
Edit
minikube -p minikube docker-env | Invoke-Expression
3. Build the Docker Image Inside Minikube
bash
Copy
Edit
docker build -t chickens-app:latest .
4. Create Kubernetes Deployment and Service
Create a file called deployment.yaml and paste this into it:

yaml
Copy
Edit
apiVersion: apps/v1
kind: Deployment
metadata:
  name: chickens-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: chickens
  template:
    metadata:
      labels:
        app: chickens
    spec:
      containers:
        - name: chickens
          image: chickens-app:latest
          ports:
            - containerPort: 5000

---
apiVersion: v1
kind: Service
metadata:
  name: chickens-service
spec:
  type: NodePort
  selector:
    app: chickens
  ports:
    - protocol: TCP
      port: 5000
      targetPort: 5000
      nodePort: 30000
Then apply it:

bash
Copy
Edit
kubectl apply -f deployment.yaml
5. Access the App
Option A – Automatically Open in Browser
bash
Copy
Edit
minikube service chickens-service
Option B – Manually Get IP
bash
Copy
Edit
minikube ip
Then open:
http://<MINIKUBE_IP>:30000
(e.g. http://192.168.49.2:30000)

Option C – Port Forward (Backup Option)
bash
Copy
Edit
kubectl port-forward svc/chickens-service 5000:5000
Then visit: http://localhost:5000

🛠️ Troubleshooting
Problem: App doesn't load in browser
✅ Check Pod Status

bash
Copy
Edit
kubectl get pods
✅ See Pod Logs

bash
Copy
Edit
kubectl logs <pod-name>
✅ Check if Minikube is running

bash
Copy
Edit
minikube status
✅ Try port forwarding

bash
Copy
Edit
kubectl port-forward svc/chickens-service 5000:5000
Then visit: http://localhost:5000

📦 Tech Stack
Python 3.11

Flask – Web framework

SQLite – Lightweight DB

Docker – Containerization

Kubernetes + Minikube – Deployment

✨ Example Preview
Here's how the app looks:

🐔 Chicken list with update/delete buttons

🟢 Add new chicken form

🧠 Smart seeding (starts with 6 chickens)


