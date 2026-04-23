# Section 7.2 — ResourceQuota and LimitRange (video transcript)

Use this as a spoken script for the `Section-7.2-ResourceQuota-and-LimitRange` lab. Adjust pacing to your demo length.

---

---

**Introduction**

Welcome back! In this lesson, we’re diving into **Section 7.2: ResourceQuotas and LimitRanges**. 

As your Kubernetes infrastructure grows, managing how much CPU and memory each team or application uses becomes critical. These two features—ResourceQuotas and LimitRanges—are the essential guardrails for maintaining cluster stability in multi-tenant environments. 

Today, we’re going to show you how to troubleshoot scenarios where these guardrails might seem "invisible," causing deployments to fail or pods to behave unexpectedly. Let's get started.

---

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

---

**Conclusion**

To wrap up, remember that **ResourceQuotas** and **LimitRanges** are your first line of defense against resource exhaustion and "noisy neighbor" problems. 

When you encounter pods that are pending or ReplicaSets that refuse to scale, don't just look at the pod logs. Use **`kubectl describe quota`** and **`kubectl describe rs`** to check for policy violations. And always be aware of **Default Injection** from LimitRanges, as it can silently push you over your namespace caps.

Mastering these troubleshooting techniques ensures that your applications stay within their allocated budgets while keeping the rest of the cluster healthy. Great job on completing this section—I'll see you in the next lesson!
