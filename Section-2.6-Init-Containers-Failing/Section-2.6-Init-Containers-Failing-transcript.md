# Section 2.6 — Init Containers Failing (video transcript)

Use this as a spoken script for a walkthrough of the `Section-2.6-Init-Containers-Failing` lab. Adjust pacing to your demo length.

---

**Intro**

Hi. This section is about **init containers** — the jobs that run **before** your main containers start. If an init container **fails** or **never finishes**, your **app container does not run**, and the pod can sit in **Init** states or **CrashLoopBackOff** on the init step.

We’ll cover **three scenarios** from this folder: a **migration** that exits with an error, a **volume mount mismatch** so the app never sees what init wrote, and **network policy** blocking **egress** so an init step that needs the internet **cannot** complete.

---

**How init containers fit in**

Kubernetes runs **init containers in order**, one after the other. They must **all succeed** — exit code zero — before the **main** containers start. Think: **migrations**, **downloading a file**, **waiting for another service** — anything that must happen **first**.

If init **fails**, you debug the **init** logs and **`describe pod`**, not only the app.

---

**Scenario one — failing migration**

We apply `init-fail.yaml`. The init container named **migrate** prints a message and then **`exit 1`** on purpose — like a **database migration** that failed.

What you see in the cluster: the pod may show **Init:CrashLoopBackOff** or similar, and **Events** mention a **non-zero exit**. The **app** container never gets a normal start because init never succeeded.

In the demo you’d run **`kubectl describe pod`** and look at the **Init Containers** section — **State** and **Last State** tell you it **exited** with an error. You can **`kubectl logs`** with **`-c migrate`** — and **`--previous`** if it restarted — to read exactly what happened.

**Fix:** we replace the manifest with **`init-fix.yaml`**. Same pod name, but migrate now **writes a flag file** and **`exit 0`**. After you **delete** the old pod and **apply** the fix, the pod should move to **Running** and you can **`logs`** the **app** container and see it read the file init prepared.

**Takeaway:** when the pod never reaches **Running**, check whether **init** is **crash-looping** or **failing fast**.

---

**Scenario two — wrong volume name between init and app**

We apply **`init-bad-mount.yaml`**. Here the init container **seeds** data into **`work-a`** — it writes a file under **`/work`**, but that path is backed by volume **`work-a`**. The **app** container mounts **`work-b`** at **`/work`** — a **different** empty directory.

So init **did** run, but the app **reads the wrong disk**. Logs might show something like **FLAG MISSING** because the file is not on the volume the app sees.

**Fix:** make **init** and **app** use the **same** `volume` name and **`mountPath`** — one shared **`emptyDir`** (or whatever you use) so the data init writes is the data the app reads.

**Takeaway:** if init “succeeds” but the app still looks broken, compare **`volumeMounts`** and **`volumes`** line by line between init and app.

---

**Scenario three — init needs the network, policy says no**

We apply **`deny-egress.yaml`**, a **NetworkPolicy** that **denies all egress** from pods in this namespace — depending on your cluster’s behavior, that can mean **no outbound traffic** except what you explicitly allow.

Then we run **`init-curl.yaml`**. The init container uses **curl** to **HTTPS** to **example.com** and saves the page. With **default deny egress**, that **fetch** **cannot** complete — init **hangs** or **fails**, and the app never starts.

**Fix:** we apply **`allow-dns-egress.yaml`**, which allows **DNS** to **kube-dns** and **TCP 443** to the internet — simplified for the lab; in production you’d **tighten** destinations. Then we **recreate** the **`init-curl`** pod so init can **resolve** and **connect**, finish successfully, and hand off to the app.

**Takeaway:** init is subject to **NetworkPolicies** too. If init does **HTTP** or **DNS**, a **deny-all** policy can block it even when the **main** container would have been fine.

---

**Closing**

When a pod is stuck in **Init**, ask: **Did init exit non-zero?** **Did init write data the app can’t see?** **Did init need network access that policy blocked?**

Use **`kubectl describe pod`**, **`kubectl logs -c <init-name>`**, and know your **volumes** and **policies**.

Thanks for watching.
