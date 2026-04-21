# Pod termination: grace period and preStop

**One budget:** `terminationGracePeriodSeconds` is a **single** countdown. Time spent in **preStop** and time your process uses **after SIGTERM** both come out of that **same** window. It is **not** “30s grace + 20s preStop = 50s”.

**Default:** If you omit `terminationGracePeriodSeconds`, Kubernetes uses **30** seconds.

**preStop:** Only runs if you define `lifecycle.preStop` in the pod spec. There is no implicit preStop when you omit it.

---

## 1. High-level flow when a Pod is deleted

```
  Pod delete requested
           |
           v
  kubelet starts shutdown
           |
           v
  +------------------------------+
  | Grace timer starts           |
  | (terminationGracePeriodSeconds)  |
  +------------------------------+
           |
           v
      preStop defined?
       /          \
     yes            no
      |              |
      v              |
  Run preStop        |
  hook               |
      |              |
      +------+-------+
             |
             v
     Send SIGTERM to main process
             |
             v
     Process handles signal / exits
             |
             v
  Still running when grace expires?
       /              \
     no                yes
      |                 |
      v                 v
  Container gone    SIGKILL
  / cleanup             |
      ^                 |
      +-----------------+
             |
             v
        (done)
```

---

## 2. This lab: “bad” vs “good” (conceptual)

**deployment-bad + term-demo:0.1**

```
  preStop (~20 s)
        |
        v
     SIGTERM
        |
        v
  handler sleeps 120 s   ------->  wall clock: 30 s total
        |                                |
        +-----------> SIGKILL <----------+
                        (hits grace limit)
```

**deployment-good + term-demo:0.2**

```
  preStop (quick httpGet)
        |
        v
     SIGTERM
        |
        v
  mark not ready, exit ~2 s
        |
        v
  finishes inside grace window (clean)
```

**Read this as:** Bad path burns the whole **30 s** grace budget → **`Terminating` for ~that long.** Good path finishes in a few seconds → **short `Terminating`.**

---

## 3. `terminationGracePeriodSeconds` quick reference

| Value | Meaning |
|--------|--------|
| **30** (default if omitted) | Up to ~30s for graceful shutdown (preStop + post-SIGTERM work share this time). |
| **0** | No meaningful graceful window; container is stopped aggressively (SIGKILL soon after SIGTERM). |

*Finalizers and other API-level blockers are separate: they can keep the Pod **object** around even when container teardown is done — see `pod-stuck-finalizer.yaml` and `Commands` in this folder.*
