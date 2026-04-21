# Section 5.2 — Evicted Pods (video transcript)

Use this as a spoken script for the `Section-5.2-Evicted-Pods` lab. Adjust pacing to your demo length.

---

**Intro**

Hi. This section is about **Evicted** pods — pods the **kubelet** **removes** when the **node** decides there isn’t enough **resource**, often **ephemeral disk** or **memory**. This is **different** from **OOMKilled** inside one container: **eviction** is a **node-level** decision about **the whole pod**.

We **fill** **ephemeral storage** past a **limit** and watch **Evicted**. Then we **fix** with a **PVC** or a **higher** **ephemeral-storage** limit.

---

**What eviction means**

**Status** may show **Failed**, **Reason: Evicted**. **Events** mention **ephemeral storage** or **pressure**. The pod **object** may remain; **workloads** need to **avoid** relying on **unbounded** disk on the **container writable layer**.

---

**Demo**

Apply **`evict-ephemeral.yaml`** — a pod that **writes** past its **`ephemeral-storage`** **limit**. **Describe** the pod — **Evicted**. **Events** mention **limits** or **eviction**.

**Fix A:** use a **PersistentVolumeClaim** for **large** data — **`pvc-and-pod.yaml`** — the **fixed** pod stays **Running**.

**Fix B:** **raise** **`limits.ephemeral-storage`** in the manifest and **reapply** — if the **workload** truly needs that **scratch** space.

---

**Closing**

**Evicted** = **node** said **this pod cannot stay**. Check **`describe pod`**, **`kubectl get events`**, and **ephemeral** vs **PVC** **storage** for **disk-heavy** workloads.

Thanks for watching.
