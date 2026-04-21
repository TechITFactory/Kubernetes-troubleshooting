# Section 6.1 — PVC / PV Binding Failures (video transcript)

Use this as a spoken script for the `Section-6.1-PVC-PV-Binding-Failures` lab. Adjust pacing to your demo length.

---

**Intro**

Hi. This section is about **PersistentVolumeClaims** — **PVCs** — and why they stay **Pending** or **never bind**. Common causes: **wrong StorageClass** name, **access mode** the **provisioner** doesn’t support, or **permissions** on the **volume** when the pod **mounts**.

We run **three threads**: **bad StorageClass**, **ReadWriteMany vs ReadWriteOnce**, and **mount permissions** with **`fsGroup`**.

---

**Scenario one — StorageClass doesn’t exist**

Apply **`pvc-bad-sc.yaml`** — **`storageClassName`** points at a **class** that **isn’t** in the cluster. **`describe pvc`** — **events** say **storage class not found** or **provisioning** failed. The **pod** stays **waiting** on an **unbound** claim.

**Fix:** **patch** the PVC to **`standard`** — or whatever your cluster’s **default** is — or **set** **`storageClassName`** to **null** to use the **default** **StorageClass**. **Watch** **PVC** go **Bound** and **pod** go **Running**.

---

**Scenario two — access mode mismatch**

Apply **`pvc-bad-mode.yaml`** — e.g. **ReadWriteMany** when the **driver** only supports **ReadWriteOnce**. **`describe pvc`** — **no** compatible **volume** or **provisioner** **error**.

**Fix:** **patch** to **ReadWriteOnce** if that’s what your **storage** supports — or **delete** and **recreate** the PVC if **fields** are **immutable**.

---

**Scenario three — permissions**

Apply **`pod-perms.yaml`** — **fsGroup** and **volume** **permissions** — **try yourself** per the **Commands**; **symptoms** include **Permission denied** in **logs** if **UID** / **GID** don’t match **mount** options.

---

**Closing**

**PVC Pending:** **StorageClass**, **accessModes**, **size**, **provisioner**. **Pod waiting on PVC:** **`describe pvc`** and **`describe pod`** **events** first.

Thanks for watching.
