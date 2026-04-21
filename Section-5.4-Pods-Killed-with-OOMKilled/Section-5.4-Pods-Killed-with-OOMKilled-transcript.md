# Section 5.4 — Pods Killed with OOMKilled (video transcript)

Use this as a spoken script for the `Section-5.4-Pods-Killed-with-OOMKilled` lab. Adjust pacing to your demo length.

---

**Intro**

Hi. This section is another **OOM** lab — **multiple** pods **competing** for **memory**, **restarts** and **CrashLoopBackOff**, and tying it to **Section 5.1**. **Section 5.1** used a **single** **Python** app with **tight** limits. Here we stress **multi-replica** **memory** behavior and **node-level** **symptoms** — still **OOMKilled**, **exit 137**, **events**.

We **deploy** **`deployment-leaker`**, **observe** **OOM** across **pods**, then **apply** **`deployment-fixed`** for a **stable** rollout.

---

**What to show**

**Watch** pods — **RESTARTS** increase. **`describe pod`** — **`Reason: OOMKilled`**. **`kubectl top pods`** when pods **stay up** long enough. **`kubectl get events`** — **OOM**-related lines.

**Difference from 5.1:** emphasize **several** pods, **scheduling** and **competition**, and **reading** **node** or **namespace** **events** — **same** **OOMKilled** **mechanism**, **broader** **diagnosis** story.

---

**Fix**

**Apply** **`deployment-fixed`** — **rollout** **succeeds**, pods **Running** **without** **OOM** **loops**. In **production** you’d also **fix** **leaks** or **right-size** **limits** per **environment**.

---

**Cleanup**

**Delete** the **lab namespace** when done.

---

**Closing**

**OOMKilled** = **memory** exceeded **limit** or **node** **pressure**. **Scale** **replicas** and **limits** **together**; **don’t** **ignore** **restarts** in **`describe`**.

Thanks for watching.
