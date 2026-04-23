# Section 6.1: PVC/PV Binding Failures

## 📋 Overview
Persistent Storage is complex in Kubernetes because it involves StorageClasses, VolumeClaims, and external cloud providers or local drivers.

## 🔍 Why PVCs stay "Pending"
1.  **StorageClass Not Found**: Typo or referencing a class that isn't on your cluster.
2.  **VolumeMode Mismatch**: Requesting `Block` storage on a driver that only supports `Filesystem`.
3.  **Namespace Mismatch**: PVCs are namespaced, PVs are global.

## 🛠️ Lab: Reproduce & Fix
1.  **Scenario 1**: Request a PVC with `storageClassName: does-not-exist`.
2.  **Scenario 2**: Request `volumeMode: Block` on a standard Minikube/Kind cluster.
3.  **Scenario 3**: Fix permissions using `fsGroup` in the security context.

## 📜 Key Commands
* `kubectl get sc`
* `kubectl describe pvc <name>`
* `kubectl describe pv`
