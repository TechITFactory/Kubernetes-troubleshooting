kubectl apply -f pod.yaml
kubectl get pod crash-demo -w
# After a few cycles you'll see: STATUS: CrashLoopBackOff, RESTARTS increasing

kubectl describe pod crash-demo | egrep -i 'State|Reason|Exit|Events|Back-off' -n
kubectl logs crash-demo
kubectl logs crash-demo --previous
-------
Build the image
MiniKube:
# Option A: build directly into Minikube’s Docker daemon
eval $(minikube docker-env)
docker build -t crash-demo:0.1 .

# Option B: (Minikube 1.33+) build via helper
# minikube image build -t crash-demo:0.1 .

Kind:
docker build -t crash-demo:0.1 .
kind load docker-image crash-demo:0.1
---------
**#Rebuild & reload image
# Rebuild
docker build -t crash-demo:0.2 .

# Minikube:
eval $(minikube docker-env) && docker build -t crash-demo:0.2 .
# or: minikube image build -t crash-demo:0.2 .

# Kind:
kind load docker-image crash-demo:0.2
