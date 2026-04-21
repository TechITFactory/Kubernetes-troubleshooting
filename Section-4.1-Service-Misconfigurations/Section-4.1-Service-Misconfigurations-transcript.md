# Section 4.1 — Service Misconfigurations (video transcript)

Use this as a spoken script for a walkthrough of the `Section-4.1-Service-Misconfigurations` lab. Adjust pacing to your demo length.

---

**Intro**

Hi. This section is about **Kubernetes Services** — how traffic gets to your pods. When something “can’t reach the service,” it’s often **not** a mysterious cluster network bug. It’s usually a **configuration mismatch**: the Service **selector** doesn’t match any pods, the **port** doesn’t line up with the container, or the Service lives in the **wrong namespace** for the pods you think it targets.

We’ll walk through **three scenarios** from this folder and use **`kubectl get endpoints`** a lot — if **Endpoints** are empty, the Service has **nothing** to send traffic to.

---

**What a Service does, in one sentence**

A **Service** groups pods by **labels** and gives you a **stable DNS name** and **virtual IP** — **ClusterIP** — that forwards to those pods’ IPs on the **target port**. If the **selector** doesn’t match **any** running pods, you get **zero endpoints** — no backends.

---

**Scenario one — selector typo**

We apply **`deploy.yaml`**. The **Deployment** labels pods with **`app: web`**, but the **Service** selector says **`app: weeb`** — on purpose, a typo.

The pods can be **Running** and **Ready**, but **`kubectl get endpoints web`** shows **no addresses** — often you’ll see **none** or an empty list. The Service literally isn’t pointing at those pods.

**Fix:** correct the Service **selector** so it matches the pod labels — **`app: web`**. After you **patch** the Service, **`get endpoints`** should list the pod IPs, and **EndpointSlices** should show the same picture.

**Takeaway:** always compare **`kubectl get pods --show-labels`** with **`kubectl get svc`** **selectors** character by character.

---

**Scenario two — port / targetPort mismatch**

We apply **`bad-port-svc.yaml`**. The selector matches **`app: web`**, but the Service sets **`targetPort`** to a **named port** **`api`**. The **nginx** container only exposes a port **named** **`http`** on container port **80**. There is **no** port named **`api`**, so the control plane can’t build valid endpoints for that target — you end up with **no endpoints** again.

**Fix:** point **`targetPort`** at the **right name** — **`http`** — or use the **numeric** port **80** so it matches the container.

**Takeaway:** **`targetPort`** must match either the **container’s port number** or a **name** that exists on the **container** definition.

---

**Scenario three — namespace mismatch**

We apply **`cross-ns-svc.yaml`** in the **`default`** namespace. The Service selects **`app: web`**, but our **web** pods live in the **`demo`** namespace. A Service only considers **pods in its own namespace** for **selector** matching — it does **not** reach across namespaces to find pods. So **endpoints** stay **empty** even though **`demo`** has healthy **`web`** pods.

**Fix:** create the Service in **`demo`** where the pods run, **or** put workloads where the Service expects them, **or** for **client** traffic across namespaces use the **full DNS name** — **`servicename.namespace.svc.cluster.local`** — and a Service that actually exists where the backends are.

**Takeaway:** **Services and pods must line up in the same namespace** for label-based selection to work.

---

**Optional validation**

The **Commands** file suggests a **busybox** pod in **`demo`** and **`wget`** to **`http://web`**. After the fixes, that should return **nginx** HTML — a quick **end-to-end** check that **DNS**, **Service**, and **endpoints** all align.

---

**Closing**

When traffic fails, check in order: **`kubectl get endpoints`** — are there **IPs**? **`describe svc`** — **selector** and **ports**? **`get pods -l`** — do labels match? Same **namespace**?

Thanks for watching.
