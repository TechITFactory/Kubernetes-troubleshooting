# Section 4.3 — Network Policy Blocking Traffic (video transcript)

Use this as a spoken script for the `Section-4.3-NetworkPolicy-Blocking-Traffic` lab. Adjust pacing to your demo length.

---

**Intro**

Hi. This section is about **NetworkPolicies** — rules that say **which traffic is allowed** between pods, namespaces, and the outside world. A **default-deny** policy can **block** traffic you **expect** to work: **client to Service**, **DNS**, or **ingress** from your **ingress controller** namespace.

We walk through **three ideas**: **default-deny ingress** breaking **same-namespace** calls, **default-deny egress** breaking **DNS** and **HTTPS**, and a **namespace label** mismatch so **allowed-from-ingress** rules never match.

---

**Scenario one — default deny ingress**

We deploy a **web** app and **expose** it, then a **client** pod in the **same** namespace. Without extra policy, **wget** to the **Service** usually works.

We apply **deny-all ingress**. Now **traffic into** pods is **blocked** unless **allowed** — the **client** cannot reach **web**.

**Fix:** apply **`allow-web-from-same-namespace`** — allow **TCP 80** from pods in that namespace — and **re-test**. **Expect** HTML back.

---

**Scenario two — default deny egress**

We apply **deny-all egress**. **Outbound** traffic from pods is **restricted** — **DNS** and **HTTPS** to the internet **fail** unless **allowed**.

**Fix:** apply **`allow-egress-dns-and-web`** — **DNS** to **kube-dns** plus **HTTPS** — then **nslookup** and **wget** to **example.com** work again.

---

**Scenario three — namespace labels**

Some policies **select** traffic **from** a namespace with a **label** — for example **ingress-nginx**. If the **namespace** is **not** labeled as the policy expects, **allowed** rules **never** match and traffic stays **blocked**.

**Fix:** **label** the namespace **`role=ingress`** — or **edit** the policy to match how your cluster is **actually** set up.

---

**Closing**

**NetworkPolicy** is **default allow** until you add a policy — then **everything** not **explicitly allowed** may be **denied**. Debug with **`kubectl describe networkpolicy`**, **test from a pod** with **`wget`** / **`curl`**, and verify **selectors** and **namespace labels**.

Thanks for watching.
