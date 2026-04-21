# Section 4.4 — Ingress 404 Errors (video transcript)

Use this as a spoken script for the `Section-4.4-Ingress-404-Errors` lab. Adjust pacing to your demo length.

---

**Intro**

Hi. This section is about **Ingress** — routing **HTTP** or **HTTPS** from outside the cluster to **Services** inside. You often see **502**, **503**, or **404** not because **nginx** is “broken,” but because **rules** don’t match: **wrong backend port**, **wrong host**, or **no endpoints** behind the Service.

We use **Minikube** with the **ingress addon**, deploy an **echo** app, then **break** and **fix** the **Ingress** manifest.

---

**Setup**

Enable **ingress** on Minikube, deploy the **echo** **Deployment** and **Service**, confirm **Endpoints** show **pod IPs**. **Ingress** only works if the **Service** and **pods** are healthy.

---

**Broken backend port**

We apply **`bad-ingress.yaml`** — for example the Ingress points at **Service port 8080** while the **Service** really serves on **80**. The **ingress controller** forwards to a port with **no backends** → **502** or **503**.

**Fix:** **patch** the **Ingress** so **`backend.service.port.number`** matches the **Service** **port** — **80** in this lab. **curl** with the **correct Host header** should return **JSON** from the echo app.

Check **ingress controller logs** if it still fails.

---

**Wrong host — 404**

**Ingress** matches **hostnames**. If you **curl** with **`Host: wrong.local`** but rules only define **`app.example.local`**, no rule matches → **404** from the **default backend**.

**Fix:** use the **hostname** defined in **`spec.rules`**, or **add** a rule for the host you need.

---

**Optional TLS**

The **Commands** show creating a **TLS Secret** and **patching** the Ingress for **HTTPS** — **curl** with **`--resolve`** and **`-k`** for a **self-signed** cert demo.

---

**Closing**

**502/503:** check **Service port**, **targetPort**, **Endpoints**. **404:** check **`Host`** header vs **`spec.rules.host`**. **Ingress** is **routing** — align **rules** with **Services** and **DNS**.

Thanks for watching.
