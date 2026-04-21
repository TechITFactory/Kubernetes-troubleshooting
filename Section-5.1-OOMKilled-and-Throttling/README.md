# Section 5.1: OOMKilled & Throttling

## 📋 Overview
Kubernetes limits memory and CPU to keep nodes stable. When a container exceeds these, it either gets killed (OOM) or slowed down (Throttled).

## 🔍 Key Concepts
*   **OOMKilled (Exit Code 137)**: The Linux OOM killer terminated the process because it hit its `limit.memory`.
*   **CPU Throttling**: The container is using more CPU than its `request.cpu`, and it's being "frozen" in intervals to stay within the limit.

## 🛠️ Lab: Reproduce & Fix
1.  **Memory Hog**: A Python app that consumes 300MB while the limit is 128MB.
2.  **Diagnose**: Check `Last State: Terminated` and search for the `Reason: OOMKilled`.
3.  **Resolve**: Either increase the limit or fix the memory leak.

## 📜 Key Commands
* `kubectl top pods`
* `kubectl describe pod <name> | grep OOM`
