& minikube -p minikube docker-env --shell | Invoke-Expression
docker build -t chicken-app:latest .
kubectl apply -f pvc.yaml
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

kubectl rollout restart deplyment chicken-app 
minikube service chicken-service 

