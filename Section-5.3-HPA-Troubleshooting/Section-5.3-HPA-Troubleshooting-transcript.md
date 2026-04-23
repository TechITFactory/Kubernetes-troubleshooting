# Section 5.3 — HPA Troubleshooting (Video Transcript)

Use this as a spoken script for the `Section-5.3-HPA-Troubleshooting` lab. Adjust your pacing to match your demo length.

---

**Intro**

Hi! In this section, we'll dive into troubleshooting the **Horizontal Pod Autoscaler (HPA)**. As you know, HPA scales pod **replicas** based on **metrics**, most commonly **CPU utilization**.

In this demo, we'll see a common pitfall: **over-provisioning**. By setting requests too high (initially **1000m**), we aren't just "vertically scaling" the pod safely—we are actually **blinding the HPA**. We'll show how this "inflated request" prevents scaling even under load, and then we'll fix it by **right-sizing** those requests so the HPA can finally see the real CPU pressure.

---

**How CPU Percentage Works**

The **HPA** calculates utilization using the formula: **`actual CPU usage` / `CPU request`** for each pod. It's important to note that it uses the **request**, not the limit. 

For example, if your **request** is **1000 millicores** (1 CPU) but the app only uses **~100m**, your **utilization** is only **~10%**. If your scaling **target** is **50%**, your pod will never scale until it hits **500m**. 

Wait, you might think: *"If I just give it 1 whole CPU, it works like vertical scaling anyway, so who cares?"* Well, the problem is **efficiency** and **responsiveness**. Over-provisioning wastes money, takes up unnecessary node capacity, and more importantly, it prevents the HPA from creating **new pods** to handle traffic when that single pod eventually hits its limit.

---

**Demo**

First, we'll **build** the **demo image** and apply **`deploy-bad`**, which uses **excessive CPU requests**. We'll then set up **`kubectl autoscale`** with a **50%** CPU target. 

Next, we'll run a **load generator** loop to hit the app. You'll notice that when we **`describe hpa`**, the **utilization** remains very low, and the **replica count** doesn't climb.

To **fix** this, we'll apply **`deploy-good`**. This configuration Uses **smaller requests** that accurately match the app's **real-world** usage. Once applied, we'll wait for the metrics to sync; the **HPA** will then **scale** as the **load** pushes the **CPU utilization** past the **50%** threshold.

Finally, we'll optionally apply **`hpa.yaml`** to configure **stabilization windows**, which helps **reduce flapping** (rapid scaling up and down).

---

**Closing**

If your **HPA isn't scaling**, remember to check your **requests**, ensure the **metrics-server** is healthy, use **`kubectl top`** to see actual usage, and always check the **HPA description**. 

Remember: **Inaccurate requests** lead to **wrong percentages**, which results in **incorrect scaling**.

Thanks for watching!
