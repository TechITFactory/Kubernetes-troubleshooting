kubectl apply -f pod.yaml
kubectl get pod crash-demo -w
# After a few cycles you'll see: STATUS: CrashLoopBackOff, RESTARTS increasing

kubectl describe pod crash-demo | egrep -i 'State|Reason|Exit|Events|Back-off' -n
kubectl logs crash-demo
kubectl logs crash-demo --previous
