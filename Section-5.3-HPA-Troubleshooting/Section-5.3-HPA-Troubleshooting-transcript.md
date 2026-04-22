# Section 5.3 — HPA Troubleshooting (Video Transcript)

Use this as a spoken script for the `Section-5.3-HPA-Troubleshooting` lab. Adjust your pacing to match your demo length.

---

**Intro**

Hi! In this section, we'll dive into troubleshooting the **Horizontal Pod Autoscaler (HPA)**. As you know, HPA scales pod **replicas** based on **metrics**, most commonly **CPU utilization**.

If your **HPA never scales** as expected, the issue is often not the HPA object itself, but rather **inaccurate CPU requests**. When **requests** are set too **high**, the **actual** CPU usage remains a tiny fraction of that request. As a result, the **percentage utilization** never reaches your threshold, and the HPA stays idle.

In this demo, we will **deploy** an app with **inflated requests**, apply **load**, and watch the **HPA** fail to scale. Then, we'll **fix** it by applying **right-sized requests** and an optional **`hpa.yaml`** to fine-tune scaling behavior.

---

**How CPU Percentage Works**

The **HPA** calculates utilization using the formula: **`actual CPU usage` / `CPU request`** for each pod. It's important to note that it uses the **request**, not the limit. 

For example, if your **request** is **1000 millicores** (1 CPU) but the app only uses **~100m**, your **utilization** is only **~10%**. If your scaling **target** is **50%**, no scale-up will ever occur because the percentage remains too low.

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
