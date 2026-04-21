# Section 6.3 — Config Changes Not Taking Effect (video transcript)

Use this as a spoken script for the `Section-6.3-Config-Changes-Not-Taking-Effect` lab. Adjust pacing to your demo length.

---

**Intro**

Hi. This section is about **updating a ConfigMap** and **not** seeing new **values** inside **running** pods. **Important:** **`envFrom`** and **`env` `valueFrom`** inject **environment variables at container start**. They are **not** **live-linked** to the ConfigMap — **changing** the **ConfigMap** does **not** **change** **already-running** **process** **environments**.

We **deploy**, **change** **`app-settings`**, **show** **old** **logs**, then **fix** with a **rollout restart** — and mention **volume mounts** and **hash** **annotations** as **alternatives**.

---

**Demo**

**Create** **ConfigMap** **`app-settings`**, **deploy** **`deployment.yaml`**, **check** **logs** — **LOG_LEVEL** and **FEATURE** match **initial** **values**.

**Apply** an **updated** **ConfigMap** — **same** **name**, **new** **literals**. **Logs** still show **old** **values** — **expected**.

**Why:** **Env** was **snapshot** at **pod** **start**.

---

**Fix A — restart**

**`kubectl rollout restart`** the **Deployment**. **New** **pods** **pick up** **new** **env** from the **ConfigMap**. **Logs** show **debug** and **enabled**.

---

**Fix B — volume mount**

**Mount** the **ConfigMap** as **files**. The **kubelet** **refreshes** **mounted** **content** on a **timer** — your **app** must **re-read** the **file** to **use** **updates**.

---

**Fix C — hash annotation**

Put a **hash** or **resourceVersion** in the **pod template** **annotations** so **ConfigMap** **changes** **trigger** a **new** **rollout** **automatically** — **GitOps** patterns often do this.

---

**Cleanup**

**Delete** **`config-lab`** when finished.

---

**Closing**

**ConfigMap updated ≠ env updated** until **pods** **restart** or you use **files** / **reload** **logic**. **Rollout restart** is the **fastest** **mental model** for **envFrom**.

Thanks for watching.
