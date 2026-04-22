# Section 4.2 — DNS Failures (video transcript)

Use this as a spoken script for the `Section-4.2-DNS-Failures` lab. Adjust pacing to your demo length.

---

**Intro**

Hi. This section is about **DNS failures inside the cluster** — when pods **cannot resolve** names like **`kubernetes.default`** or **external** hostnames. Very often the app is fine; **NetworkPolicy** or firewall rules are **blocking UDP or TCP port 53** to **CoreDNS**, so lookups never complete.

We’ll **deny egress**, watch **`nslookup`** fail, then **allow DNS** to **kube-dns** and show it working again.

---

**What goes wrong**

Pods rely on the **cluster DNS** service — usually **CoreDNS** in **`kube-system`**. If a policy **blocks all egress**, DNS queries cannot reach the DNS pods. **Symptoms:** timeouts, “could not resolve host,” **`nslookup`** failures — not only for the internet, but for **in-cluster** names too, because those also go through **DNS**.

---

**Demo flow**

We create a **sandbox namespace** and a **busybox** pod used as a **tester**. We apply a **default-deny egress** policy — **only** egress explicitly allowed is permitted.

Then we run **`nslookup google.com`** and **`nslookup`** for internal services like **`kubernetes.default`**. **Expect failures** — DNS is blocked.

**Fix:** apply **`allow-dns.yaml`** — allow **UDP and TCP port 53** to **kube-dns** — and **re-test**. **Expect** internal and external resolution to **succeed** again.

---

**Takeaway**

Before you blame **CoreDNS** itself, check whether **NetworkPolicy** allows **egress to DNS**. **`kubectl get networkpolicy`** and **`describe`** your policies.

---

**Closing**

DNS in Kubernetes is **egress to CoreDNS** plus **correct** **`resolv.conf`** in the pod. Block **port 53**, and **everything** that needs names breaks.

Thanks for watching.
