# Section 5.3 — HPA Troubleshooting (video transcript)

Use this as a spoken script for the `Section-5.3-HPA-Troubleshooting` lab. Adjust pacing to your demo length.

---

**Intro**

Hi. This section is about the **Horizontal Pod Autoscaler** — **HPA** scales **replicas** based on **metrics**, often **CPU**. If **HPA never scales** when you expect, the problem is often **not** the HPA object itself but **bad CPU requests** — **requests** so **large** that **actual** CPU usage is **a tiny fraction** of the **request**, so **percentage** utilization **never** crosses your **target**.

We **deploy** with **inflated requests**, run **load**, watch **HPA** stay **flat**, then **fix** with **right-sized requests** and optional **`hpa.yaml`** for **behavior**.

---

**How CPU percent works**

**HPA** uses **`actual CPU` / `CPU request`** for each pod — **not** limit. If **`request`** is **1000 millicores** but the app uses **~100m**, **utilization** is **~10%** — **below** a **50%** target — **no scale-up**.

---

**Demo**

**Build** the **demo image**, apply **`deploy-bad`** with **huge** **CPU requests**, then **`kubectl autoscale`** with **50%** CPU. Run a **loader** loop hitting the app. **`describe hpa`** — **targets** look **low**; **replicas** don’t **climb**.

**Fix:** apply **`deploy-good`** — **smaller** **requests** matching **real** usage — **wait**, then **HPA** should **scale** when **load** pushes **CPU%** over **50%**.

**Optional:** apply **`hpa.yaml`** for **stabilization** windows — **reduce** **flapping**.

---

**Closing**

**HPA not scaling:** check **`requests`**, **`metrics-server`**, **`kubectl top`**, and **HPA** **`describe`**. **Wrong requests** = **wrong percentage** = **wrong scaling**.

Thanks for watching.
