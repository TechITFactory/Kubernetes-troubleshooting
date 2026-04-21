# Section 6.2 — Config Errors (video transcript)

Use this as a spoken script for the `Section-6.2-ConfigErrors` lab. Adjust pacing to your demo length.

---

**Intro**

Hi. This section is about **ConfigMaps** and **Secrets** **referenced** by pods — when the **object** is **missing** or the **key** name is **wrong**, the **container** never starts normally. You’ll see **`CreateContainerConfigError`** in **`describe pod`** **events**.

We **apply** **`bad-pod.yaml`** without creating **ConfigMap** / **Secret** first, **fix** by **creating** them, then **break** **`broken-keys.yaml`** with a **wrong key** and **fix** that too.

---

**Scenario one — missing ConfigMap and Secret**

**Apply** **`bad-pod.yaml`**. **Pod** stays **`Waiting`** — **`Reason: CreateContainerConfigError`**. **Events** say **configmap** or **secret** **not found**.

**Fix:** **`kubectl create configmap`** and **`kubectl create secret`** with the **names** the pod **expects**. **Delete** the pod so it **re-creates** — or **wait** for **kubelet** **retry** — **logs** should show **env** **values**, **pod** **Running**.

---

**Scenario two — wrong key in ConfigMap**

**Apply** **`broken-keys.yaml`**. **Events** reference a **key** that **doesn’t exist** on the **ConfigMap**.

**Fix:** **add** the **key** — **`kubectl create configmap ... --dry-run`** **pipe** **`apply`** — or **change** the pod **to** **reference** an **existing** **key**. **Recreate** the pod.

---

**Closing**

**CreateContainerConfigError** → **check** **`envFrom`**, **`valueFrom`**, **ConfigMap** and **Secret** **names**, and **every** **key** path. **Fix** the **API objects**, not only the **image**.

Thanks for watching.
