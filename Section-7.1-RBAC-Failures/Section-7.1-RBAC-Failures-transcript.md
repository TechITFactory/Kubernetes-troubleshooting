# Section 7.1 — RBAC Failures (video transcript)

Use this as a spoken script for the `Section-7.1-RBAC-Failures` lab. Adjust pacing to your demo length.

---

**Intro**

Hi. This section is about **RBAC** — **Role-Based Access Control**. When **`kubectl`** or an **app** using a **ServiceAccount** gets **`Forbidden`**, it’s usually **missing** **Role** or **ClusterRole** **bindings**, or you’re using a **Role** in **one** namespace but **calling** **another**.

We **create** **`dev-user`** **ServiceAccount**, **prove** **list pods** **fails**, **grant** **`pod-reader`** with **Role** + **RoleBinding**, **verify** **read** works and **create** still **fails**, then **note** **ClusterRole** for **cross-namespace** access.

---

**Scenario one — no permissions**

**Apply** **`serviceaccount.yaml`**. As **`dev-user`**, **`kubectl get pods`** → **`Forbidden`**. **`kubectl auth can-i list pods`** → **no**. **`auth can-i --list`** shows **what** is **allowed** — **empty** or **minimal**.

---

**Resolve — Role and RoleBinding**

**Apply** **`role-and-binding.yaml`**. **`get pods`** as **`dev-user`** → **works**. **`create deploy`** → still **`Forbidden`** — we only **granted** **get/list/watch**.

**`auth can-i`** — **list** **yes**, **create deployments** **no**.

---

**Pitfall — Role vs ClusterRole**

A **Role** is **namespaced**. **`dev-user`** **cannot** **list** **pods** in **`default`** if the **binding** only applies to **`rbac-lab`**. **Cross-namespace** **read** needs **ClusterRole** + **ClusterRoleBinding** — or **separate** **RoleBindings** per **namespace**.

---

**Cleanup**

**Delete** **`rbac-lab`**.

---

**Closing**

**Forbidden** → **`auth can-i`**, **`describe rolebinding`**, **`describe clusterrolebinding`**. **Least privilege** — **grant** only what **users** and **service accounts** **need**.

Thanks for watching.
