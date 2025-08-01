🐔 Chicken Record System on EKS – Flask App with CI/CD
This project is a Flask-based web app that allows you to manage a list of chickens. It uses:

Flask with SQLite

Docker for containerization

Kubernetes (EKS) for orchestration

Terraform to provision infrastructure

GitHub Actions for CI/CD

🗂 Project Structure
bash
Copy
Edit
.
├── app.py                  # Flask application
├── requirements.txt        # Python dependencies
├── Dockerfile              # Container build setup
├── templates/
│   └── index.html          # Chicken list UI
├── static/
│   └── styles.css          # CSS styles
├── k8s/
│   ├── pvc.yaml            # PersistentVolumeClaim
│   ├── service.yaml        # LoadBalancer Service
│   └── eks-deployment.yaml # Deployment for EKS
├── terraform/
│   ├── main.tf             # Main EKS Terraform config
│   ├── variables.tf        # Variables for Terraform
│   └── outputs.tf          # Terraform outputs
└── .github/workflows/
    └── deploy.yml          # GitHub Actions CI/CD pipeline
🧪 Local Setup
Clone the repository

bash
Copy
Edit
git clone <your-repo-url>
cd your-repo
Run locally

bash
Copy
Edit
pip install -r requirements.txt
python app.py
Navigate to http://localhost:5000

🐳 Docker Instructions
Build the Docker image

bash
Copy
Edit
docker build -t chicken-app .
Run the container

bash
Copy
Edit
docker run -p 5000:5000 chicken-app
☸ Deploy to Kubernetes (EKS)
1. Provision the EKS Cluster with Terraform
Go to the Terraform folder:

bash
Copy
Edit
cd terraform/
Edit the values in variables.tf:

Add your IAM user ARN

Add your EKS node group role ARN

Initialize and deploy the cluster:

bash
Copy
Edit
terraform init
terraform apply
2. Connect to Your EKS Cluster
bash
Copy
Edit
aws eks update-kubeconfig --region us-east-1 --name chicken-cluster
3. Deploy Kubernetes Resources
bash
Copy
Edit
kubectl apply -f k8s/
This includes:

Your Flask app

PersistentVolume for the SQLite DB

LoadBalancer Service (you’ll get a public IP)

🚀 CI/CD with GitHub Actions
1. Configure GitHub Secrets
In your GitHub repo, go to Settings > Secrets and variables > Actions > New repository secret and add:

Secret Name	Description
AWS_ACCESS_KEY_ID	Your IAM access key
AWS_SECRET_ACCESS_KEY	Your IAM secret key

2. Push to main
Every time you push to the main branch, this happens automatically:

<<<<<<< HEAD
Docker image is built

Pushed to ECR

Kubernetes is updated with the new image

You can find the GitHub Actions workflow in .github/workflows/deploy.yml.

📚 Learning Tips
If you're new to Kubernetes, focus on:

Deployments

Services (especially LoadBalancer type)

Volumes/PVCs

If you're new to Terraform, focus on:

Modules (especially the AWS EKS module)

terraform apply, destroy, output

✅ To-Do Checklist
 Build ECR repo in AWS (use aws ecr create-repository)

 Replace placeholder image names with your actual ECR URL

 Fill in your IAM ARNs in Terraform config

 Run terraform apply

 Push your code to GitHub and let CI/CD do the rest

🤝 Help
Having trouble? Common fixes:

Make sure your IAM user has EKS + ECR permissions

Use the same AWS region everywhere

If kubectl isn’t working, try aws eks update-kubeconfig again

=======
>>>>>>> 4604d7b5f6015aa50e2ba2bf894d34c03bb54110
