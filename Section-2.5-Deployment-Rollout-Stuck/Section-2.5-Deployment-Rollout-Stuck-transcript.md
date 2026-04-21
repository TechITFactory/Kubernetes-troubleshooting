# Section 2.5 — Deployment Rollout Stuck (video transcript)

Use this as a spoken script for a walkthrough of the `Section-2.5-Deployment-Rollout-Stuck` lab. Adjust pacing to your demo length.

---

**Intro**

Hi. This section is about Kubernetes **Deployments** where a **rollout** gets **stuck** — for example `kubectl rollout status` never finishes, or it **times out** and you see conditions like **ProgressDeadlineExceeded** in `kubectl describe deployment`.

We’ll walk through **two small scenarios** from this folder: one where **readiness probes** and **rolling update** settings fight each other, and one where an **init container** fails so the main app never really comes up.

---

**What “rollout” means here**

When you change a Deployment — the image, environment, probes, anything in the pod template — Kubernetes creates a **new ReplicaSet** and tries to roll **new** pods in using your **update strategy**, usually a **rolling update**.

The rollout is supposed to finish when the **new** ReplicaSet has enough pods that are **healthy** according to your rules — especially **readiness**.

---

**Scenario one — wrong readiness path and a strict rolling strategy**

We deploy `deployment-bad`. It asks for **two** replicas. It sets **`progressDeadlineSeconds`** to **sixty seconds**. In plain language, that means: if the Deployment does **not** make **forward progress** within about **sixty seconds**, Kubernetes will mark the rollout as **failed** from a progress point of view — you’ll see that in the Deployment **conditions**.

The manifest also sets **`maxUnavailable` to zero** on the rolling update. Roughly: during the update, **do not** make an old pod unavailable **unless** a replacement is already **Ready**. That sounds safe, but if **new** pods **never** become **Ready**, you can end up in a kind of **deadlock**: the system won’t finish replacing traffic to healthy new pods, because there **are** no healthy new pods yet.

Here the **readiness probe** is pointed at a path that does **not** match what our sample app treats as “I’m ready to receive traffic” — in the lab, the probe uses **`/readyz`** while the app serves **`/healthz`** for that. If the probe **keeps failing**, pods can show as **Running** but **not Ready**.

So in the demo you’d run `kubectl rollout status` and watch it **hang** or **time out** around that **sixty second** window. Then you’d run `kubectl describe deployment` and look at **Conditions** — you expect something like **ProgressDeadlineExceeded**. You’d run `kubectl get pods` and notice **READY** might be **zero out of one** even though the container is running — because **readiness** never passes.

**Fix idea A:** patch the Deployment so the **readiness probe** hits the **correct** path — **`/healthz`** — so pods become **Ready** and the rollout can complete.

**Fix idea B:** relax **`maxUnavailable`** — for example allow one pod to be unavailable — which can **unblock** some rollouts. In real life you still want the **probe** to be **correct**; strategy tweaks are not a substitute for a broken health check.

---

**Scenario two — init container always fails**

Next we apply `deployment-init-bad`. Here the **init container** runs a fake “migration” that **exits with an error** every time.

Until init **succeeds**, the **main** application container does **not** start. So you’re not debugging HTTP paths yet — you’re blocked **earlier**. The rollout looks stuck because **nothing** gets to a steady **Ready** state.

In the video you’d show `kubectl describe pod` and scroll to **Init Containers** — you’ll see the init step **failing**, and that explains why the main workload never really comes online.

**Takeaway:** a **stuck rollout** is not always “wrong readiness URL” — always check whether **init** or **startup** is blocking the main container.

---

**Closing**

Remember three knobs: **`progressDeadlineSeconds`** — how long Kubernetes waits for **meaningful progress**; **rolling update** settings like **`maxUnavailable`** and **`maxSurge`** — how aggressive the replacement is; and **readiness** — whether a pod **counts** as available.

Use **`kubectl rollout status`**, **`kubectl describe deployment`**, and **`kubectl describe pod`** to see **which** of these you’re hitting.

Thanks for watching.
