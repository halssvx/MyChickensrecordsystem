CHICKENS MANAGER - FLASK + SQLITE + MINIKUBE APP

This is a simple CRUD (Create, Read, Update, Delete) web application for managing a list of chickens. The app is built using Flask, stores data in a SQLite database, and is containerized and deployed using Kubernetes via Minikube.

WHAT THE APP DOES:

- Displays a list of chickens from a database.
- Allows users to:
  - Add new chickens
  - Edit existing chicken names
  - Delete chickens
- Uses SQLite as a lightweight database.
- Initializes with 6 default chickens if the database is empty.

PROJECT STRUCTURE:

chickensIU/
├── app.py               --> Flask application
├── templates/
│   └── index.html       --> Frontend HTML page
├── Dockerfile           --> Container definition
├── deployment.yaml      --> Kubernetes deployment and service
└── chickens.db          --> Auto-created SQLite DB (local use only)

HOW TO RUN LOCALLY (WITHOUT DOCKER):

1. Create a virtual environment:
   python -m venv venv

2. Activate the environment:
   On macOS/Linux: source venv/bin/activate
   On Windows: venv\Scripts\activate

3. Install Flask:
   pip install flask

4. Run the app:
   python app.py

Then open http://localhost:5000 in your browser.

DOCKERIZING THE APP:

Dockerfile should look like this:

FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN pip install flask
EXPOSE 5000
CMD ["python", "app.py"]

DEPLOY TO MINIKUBE:

1. Start Minikube:
   minikube start

2. Use Minikube’s Docker daemon:
   On bash: eval $(minikube -p minikube docker-env)
   On PowerShell: minikube -p minikube docker-env | Invoke-Expression

3. Build the Docker image:
   docker build -t chickens-app:latest .

4. Create Kubernetes deployment and service:
   (Create a file named deployment.yaml with the following content)

---
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

Then run:
kubectl apply -f deployment.yaml

5. Get Minikube IP:
   minikube ip

Visit http://<minikube-ip>:30000/ in your browser.
(Replace <minikube-ip> with the IP you got)

TROUBLESHOOTING:

- Check pod status:
  kubectl get pods

- Check logs:
  kubectl logs <pod-name>

- If the site doesn't load:
  - Make sure the container is running
  - Try port-forwarding:
    kubectl port-forward svc/chickens-service 5000:5000
    Then visit http://localhost:5000

TECH USED:

- Python + Flask
- SQLite
- Docker
- Kubernetes + Minikube
