# Section 5.1 — OOMKilled and Throttling (video transcript)

Use this as a spoken script for the `Section-5.1-OOMKilled-and-Throttling` lab. Adjust pacing to your demo length.

---

**Intro**

Hi. This section is about **memory limits** and the **OOM killer**. If a container **uses more memory** than its **`limits.memory`**, Linux can **kill** the process. Kubernetes reports **`OOMKilled`** — often **exit code 137** — and you may see **CrashLoopBackOff** if the app keeps **allocating** past the limit.

We **build** a small **Python** demo image, deploy with **tight** limits, watch **restarts**, then **fix** by **raising limits** or **reducing** what the app allocates.

---

**What happens**

The **kubelet** enforces **cgroups** limits. **Exceed** the **memory limit** → the **kernel** may **SIGKILL** the container. **`describe pod`** shows **`Last State: Terminated`**, **`Reason: OOMKilled`**. **`kubectl top pods`** shows **real** usage when the pod is **running**.

**CPU throttling** is related but different: **low CPU limit** can **slow** the app without **killing** it — **OOM** is **memory**.

---

**Demo**

Deploy **`deployment-bad`** with **small** memory **limits** and an app that **allocates** chunks. **Watch** pods — **restarts** climb, **`describe`** shows **OOMKilled**.

**Fix A:** **patch** the **Deployment** — **raise** **`requests`** and **`limits.memory`** so the workload **fits**.

**Fix B:** **change** the **application** — allocate **fewer** chunks — **rebuild** a **new** image tag and **`set image`**.

---

**Closing**

**OOMKilled** means **usage hit the limit** or **node pressure** — here we focus on **container limits**. **Fix** the **limit** vs **workload** mismatch or **fix** the **leak**.

Thanks for watching.
