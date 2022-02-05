aws eks --region $(terraform output -raw region) update-kubeconfig --name $(terraform output -raw cluster_name)
cd ../../../manifest
kubectl apply -f .

