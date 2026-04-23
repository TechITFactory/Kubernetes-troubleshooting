# 🚀 Kubernetes Troubleshooting: The Ultimate Hands-on Course

Welcome to the **Kubernetes Troubleshooting** repository! This project is the companion to the Udemy course, designed to help you go from "It's not working!" to "Here's the fix!" through 20+ realistic laboratory scenarios.

---

## 🛠️ The "Break-Fix" Learning Strategy
This course doesn't just show you YAML. It gives you the tools to:
1. **Recreate**: Intentionally trigger production-grade failures.
2. **Diagnose**: Use `kubectl`, logs, and investigation tools to find the root cause.
3. **Resolve**: Apply fixes and verify the solution.

---

## 📂 Curriculum at a Glance

### 🏗️ Section 2: Pod Lifecycle & Common Failures
*   **[2.1 CrashLoopBackOff](Section-2.1-CrashLoopBackOff)**: Debugging application crashes.
*   **[2.2 ImagePullBackOff](Section-2.2-ImagePullBackOff)**: Fixing registry and naming issues.
*   **[2.3 Pending Pods](Section-2.3-Pending-Pods)**: Resolving scheduling, taints, and resource scarcity.
*   **[2.4 Pods Stuck in Terminating](Section-2.4-Pods-Stuck-in-Terminating)**: Handling zombie processes and finalizers.
*   **[2.5 Deployment Rollout Stuck](Section-2.5-Deployment-Rollout-Stuck)**: Fixing blue-green/rolling upgrade deadlocks.
*   **[2.6 Init Containers Failing](Section-2.6-Init-Containers-Failing)**: Debugging pre-startup failure points.

### 🏥 Section 3: Probes & Health Checks
*   **[3.1 Probes & Health Checks](Section-3.1-Probes-and-Health-Checks)**: Tuning Liveness, Readiness, and Startup probes.

### 🌐 Section 4: Networking & Service Discovery
*   **[4.1 Service Misconfigurations](Section-4.1-Service-Misconfigurations)**: Debugging labels, ports, and selectors.
*   **[4.2 DNS Failures](Section-4.2-DNS-Failures)**: Investigating CoreDNS and internal resolution.
*   **[4.3 NetworkPolicy Blocking](Section-4.3-NetworkPolicy-Blocking-Traffic)**: Fixing connectivity gaps.
*   **[4.4 Ingress 404 Errors](Section-4.4-Ingress-404-Errors)**: Routing traffic correctly through controllers.

### ⚡ Section 5: Resource Management & Scaling
*   **[5.1 OOMKilled & Throttling](Section-5.1-OOMKilled-and-Throttling)**: Right-sizing CPU/Memory.
*   **[5.2 Evicted Pods](Section-5.2-Evicted-Pods)**: Managing node-level resource pressure.
*   **[5.3 HPA Troubleshooting](Section-5.3-HPA-Troubleshooting)**: Why your pods won't scale.
*   **[5.4 Pods Killed with OOMKilled](Section-5.4-Pods-Killed-with-OOMKilled)**: Advanced memory leak diagnostics.

### 💾 Section 6: Storage & Configuration
*   **[6.1 PVC/PV Binding Failures](Section-6.1-PVC-PV-Binding-Failures)**: Mapping volumes correctly.
*   **[6.2 ConfigErrors](Section-6.2-ConfigErrors)**: Missing ConfigMaps and Secrets.
*   **[6.3 Config Changes Not Taking Effect](Section-6.3-Config-Changes-Not-Taking-Effect)**: Handling baked-in env vars.

### 🔐 Section 7: Security & RBAC
*   **[7.1 RBAC Failures](Section-7.1-RBAC-Failures)**: Fixing "Forbidden" errors.
*   **[7.2 ResourceQuota & LimitRange](Section-7.2-ResourceQuota-and-LimitRange)**: Cluster-level resource guardrails.

## 🚀 Getting Started
1. Install **Minikube** or **Kind**.
2. Clone this repo.
3. Choose a section and follow the `Commands` file.

Happy Troubleshooting! 🛠️