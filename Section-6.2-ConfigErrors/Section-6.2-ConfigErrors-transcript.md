# Section 6.2 — Config Errors (video transcript)

Use this as a spoken script for the `Section-6.2-ConfigErrors` lab. Adjust pacing to your demo length.

---

Hi! In this section, we’re looking at **ConfigMaps** and **Secrets**. These are fundamental for providing configuration and sensitive data to your apps. However, if a pod references an object that **doesn't exist** or even just a **key** name that’s misspelled, the container will fail to start. 

The primary symptom you’ll see in **`kubectl describe pod`** is the status **`CreateContainerConfigError`**. This tells you that Kubernetes tried to build the container’s environment, but couldn’t find the necessary data.

---

First, let's apply **`bad-pod.yaml`**. This pod explicitly expects a ConfigMap named **`app-config`** and a Secret named **`db-credentials`**. Since these don't exist yet, the pod will stay in **`Waiting`** with the reason **`CreateContainerConfigError`**. If you check the **Events**, it will tell you exactly which resource is missing.

**To fix this**, we’ll create the missing objects. One important note: once you fix the ConfigMap or Secret, the **kubelet** will eventually retry and start the container. However, if you're in a hurry, you can always **delete and recreate** the pod to force an immediate refresh.

---

Next, let's look at **Key Mismatches**. In **`broken-keys.yaml`**, the ConfigMap **does** exist, but we’ve asked Kubernetes to mount a specific key—**`app.conf`**—which isn't inside that ConfigMap. This results in the same **`CreateContainerConfigError`**.

There’s a subtle but vital difference between using configuration as **environment variables** versus **volumes**. If you update a ConfigMap that is mounted as a **volume**, Kubernetes will eventually project those changes into the container without a restart. But if the ConfigMap provides **environment variables**, those are only set when the container **starts**. This means you **must** recreate the pod to pick up new or fixed environment variables.

---

**Closing**

**CreateContainerConfigError** → **check** **`envFrom`**, **`valueFrom`**, **ConfigMap** and **Secret** **names**, and **every** **key** path. **Fix** the **API objects**, not only the **image**.

Thanks for watching.
