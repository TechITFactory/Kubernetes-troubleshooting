# Section 2.1: CrashLoopBackOff

## 📋 Overview
`CrashLoopBackOff` is one of the most common Kubernetes errors. It means the container is starting but immediately crashing, and Kubernetes is retrying with an incremental delay (the "back-off").

## 🔍 Why it happens
1.  **Application Bugs**: Unhandled exceptions, syntax errors.
2.  **Missing Configuration**: Env vars not set, missing config files.
3.  **Dependency Failures**: Trying to connect to a DB that isn't ready.
4.  **Resource Limits**: Out of Memory (OOM) at startup.

## 🛠️ Lab: Reproduce & Fix
1.  **Recreate**: Deploy a Python app with an intentional syntax error.
2.  **Diagnose**: Use `kubectl logs --previous` to see why the *last* instance died.
3.  **Resolve**: Fix the `app.py`, rebuild the image, and update the pod.

## 📜 Key Commands
* `kubectl logs crash-demo --previous`
* `kubectl describe pod crash-demo`
