# Section 7.2 — ResourceQuota and LimitRange (video transcript)

Use this as a spoken script for the `Section-7.2-ResourceQuota-and-LimitRange` lab. Adjust pacing to your demo length.

---

Hi! This section is about **ResourceQuotas** and **LimitRanges** — the essential guardrails for multi-tenant clusters. 

A **ResourceQuota** sets a hard cap on the **total** resources a namespace can consume, while a **LimitRange** enforces rules at the **individual pod** level—setting minimums, maximums, and—crucially—**default values**. 

Troubleshooting these can be tricky because errors often appear in different places depending on what’s being violated. We’ll show you how to find these "invisible" errors and how to align your deployments with the cluster’s policies.

---

First, we’ll apply **`deployment-exceed.yaml`**. This deployment requests 5 replicas, each asking for 500 millicores. That’s a total of 2500 millicores—but our quota is only 2000. 

Here is the first troubleshooting trap: the **Deployment** will appear **Successful**, but you'll notice that the pod count is stuck at 4 out of 5. Because the **ReplicaSet controller** is being rejected by the Quota, the 5th pod is never even created. To see the actual error message, you have to **`describe rs`** and look for the "failed quota" event.

**To fix this**, we’ll apply **`deployment-fixed.yaml`**, which lowers the per-pod requests so the total fits within our **2000 millicore** limit.

---

Now let's look at **LimitRanges**. If you try to run a pod that requests more than the **Max** allowed, the API server will reject it immediately. Unlike the Quota-ReplicaSet scenario, **`kubectl`** will show you this error directly on your screen.

But the real "silent" issue with LimitRanges is **Default Injection**. If a developer forgets to set any requests, the LimitRange will automatically inject its **`defaultRequest`**. This can cause a pod to hit a ResourceQuota even when the developer thought they were requesting nothing! Always check **`kubectl describe pod`** to see if a LimitRange has modified your resources.

---

**Discovery**

**`describe quota`**, **`describe limitrange`**, **`get events`** **grep** **quota**. **`kubectl top pods`** for **actual** vs **requested** **usage**.

---

**Cleanup**

**Delete** **`quota-lab`**.

---

**Closing**

**Pods pending / RS stuck:** **quota** and **limitrange** **first** in **multi-tenant** **namespaces**. **Align** **requests** with **policy** and **team** **budgets**.

Thanks for watching.
