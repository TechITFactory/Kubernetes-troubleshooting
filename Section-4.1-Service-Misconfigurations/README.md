# Section 4.1: Service Misconfigurations

## 📋 Overview
Services are the glue of Kubernetes networking. If service discovery fails, it's usually not "the network" — it's a configuration mismatch.

## 🔍 Common Selector Pitfalls
1.  **Selector Typo**: `app: web` vs `app: weeb`.
2.  **Port Mismatch**: `targetPort` doesn't match the container's `containerPort`.
3.  **Namespace Mismatch**: Referencing a service in another namespace without the FQDN.

## 🛠️ Lab: Reproduce & Fix
1.  **Selector Typo**: Create a Service that points to a non-existent group of pods.
2.  **Port Mismatch**: Point a Service to port 8080 when the app is on 80.
3.  **Cross-NS**: Try to reach a service in `prod` from `dev` using only the short name.

## 📜 Key Commands
* `kubectl get endpoints`
* `kubectl describe svc <name>`
* `kubectl run -it --rm debug --image=busybox -- nslookup <svc>`
