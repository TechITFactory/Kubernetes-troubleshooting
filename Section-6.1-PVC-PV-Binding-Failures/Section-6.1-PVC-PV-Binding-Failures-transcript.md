# Section 6.1 — PVC / PV Binding Failures (video transcript)

Use this as a spoken script for the `Section-6.1-PVC-PV-Binding-Failures` lab. Adjust pacing to your demo length.

---

Hi! In this section, we’re troubleshooting **PersistentVolumeClaims (PVCs)**. If your PVC is stuck in **Pending**, it usually isn’t a mystery; the reason is almost always documented in the **PVC events**. 

We’ll explore three common scenarios: **missing StorageClasses**, **unsupported access modes**, and one of the most common points of confusion: **`WaitForFirstConsumer`** binding behavior. We’ll also touch on **volume permissions** using **`fsGroup`**.

---

First, let’s apply **`pvc-bad-sc.yaml`**. Here, the **`storageClassName`** is set to a name that doesn't exist in our cluster. If we **`describe pvc`**, we'll see an event explicitly stating the **StorageClass was not found**. Consequently, any **Pod** using this PVC will be stuck in **Pending** because it’s waiting on an **unbound** claim.

**To fix this**, we can **patch** the PVC to use a valid class, like **`standard`**, or set the class to **null** to let the cluster use its **default** StorageClass. As soon as we patch it, you’ll see the PVC transition to **Bound** and the pod move to **Running**.

---

Next, we look at **Volume Mode mismatches**. In **`pvc-bad-mode.yaml`**, we request **`volumeMode: Block`**. While common in high-performance cloud environments, many local provisioners (like the one in Minikube) only support the default **`Filesystem`** mode.

When you apply this, the PVC will stay **Pending** with an error like "provisioner does not support block volume." This is a classic case of requesting a feature your underlying storage provider can't deliver. Because **Volume Mode is immutable**, you’ll need to delete the PVC and recreate it with the correct mode to fix it.

Also, keep an eye out for **`volumeBindingMode: WaitForFirstConsumer`**. In many modern clusters, your PVC will stay **Pending** on purpose until a **Pod** is scheduled that actually needs it. This isn't an error—it's a feature that ensures the volume is created in the same **zone** as your pod!

---

Finally, even when a volume binds, the pod might crash with **Permission Denied** errors if the container's user doesn't have the right access. If we apply **`pod-perms-bad.yaml`**, we'll see the pod fail to write its data. We then use **`pod-perms.yaml`** to demonstrate how **`fsGroup`** in the **SecurityContext** can fix this by automatically changing the group ownership of the mounted volume.

**Closing**

If your PVC is **Pending**, remember the checklist: Check the **StorageClass**, verify the **accessModes** and **size**, and look for **`WaitForFirstConsumer`** delays. Always start your investigation with **`kubectl describe pvc`**.

Thanks for watching!
