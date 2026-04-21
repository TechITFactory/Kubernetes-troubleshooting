# Section 7.2 — ResourceQuota and LimitRange (video transcript)

Use this as a spoken script for the `Section-7.2-ResourceQuota-and-LimitRange` lab. Adjust pacing to your demo length.

---

**Intro**

Hi. This section is about **ResourceQuota** and **LimitRange** — **namespace**-level **guardrails**. **Quota** caps **total** **CPU**, **memory**, **object counts**, etc. **LimitRange** sets **defaults**, **mins**, and **maxes** per **pod** or **container**. **Pods** that **violate** **limits** **fail** **admission**; **Deployments** may **stall** if **new** **pods** **can’t** **fit** **under** **quota**.

We **create** **`quota-lab`**, **apply** **`resourcequota.yaml`** and **`limitrange.yaml`**, **describe** them, then **exceed** **quota** with **`deployment-exceed`** and **fix** with **`deployment-fixed`**. We **try** a **pod** **above** **LimitRange** **max** and **fix** with **smaller** **requests**.

---

**ResourceQuota — exceeded**

**Apply** **`deployment-exceed`** — **too many** **replicas** or **too much** **CPU** **request** for the **quota**. **ReplicaSet** **events** mention **quota** **exceeded**. **Not** **all** **pods** **schedule**.

**Fix:** **lower** **per-pod** **requests** or **replica** **count** — **`deployment-fixed`** — until **`describe quota`** shows **room**.

---

**LimitRange — violation**

**`kubectl run big-pod`** with **2 CPU** / **2Gi** when **LimitRange** **max** is **smaller** → **error** from **API** — **maximum** **constraint** **violated**.

**Fix:** **run** **`ok-pod`** with **requests** **inside** **min**/**max** — **200m** **CPU**, **128Mi** **memory** style **values** per **Commands**.

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
