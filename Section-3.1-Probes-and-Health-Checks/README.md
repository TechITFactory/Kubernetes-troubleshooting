# Section 3.1: Probes & Health Checks

## 📋 Overview
Kubernetes uses three types of probes to monitor container health. Misconfiguring these leads to "Ready: 0/1" or infinite restart loops.

## 🔍 The Three Probes
*   **Startup Probe**: Gates the other probes. Useful for slow-starting heritage apps.
*   **Liveness Probe**: Determines if the container needs a restart.
*   **Readiness Probe**: Determines if the container should receive traffic (Endpoints).

## 🛠️ Lab: Reproduce & Fix
1.  **Node.js Demo**: A server that takes 60 seconds to start. We use aggressive probes that kill it before it's ready.
2.  **Startup Probe Demo**: Using a Python app to show how a `startupProbe` prevents the `livenessProbe` from killing the container during its warmup phase.

## 📜 Key Commands
* `kubectl get endpoints`
* `kubectl describe pod <name>`
