# Explanation: `cpu_app.py`

This script is a simple Python-based HTTP server designed to simulate CPU load. It is used in HPA (Horizontal Pod Autoscaler) troubleshooting labs to trigger scaling by consuming CPU resources on demand.

## Core Logic

### 1. HTTP Server Setup
The script uses Python's built-in `http.server` module to create a lightweight web server that listens on port `8080`.

```python
HTTPServer(("", 8080), H).serve_forever()
```

### 2. Request Handling
It defines a custom handler class `H` (inherited from `BaseHTTPRequestHandler`) that handles `GET` requests.

### 3. The "Burn" Logic
When you send a request to the server, it looks for a query parameter named `burn_ms`.

```python
qs = u.parse_qs(u.urlparse(self.path).query)
burn = int(qs.get("burn_ms",[0])[0])
```

- **`burn_ms`**: Specifies the duration in milliseconds for which the server should "spin" the CPU.
- **CPU Spinning Loop**: The script enters a `while` loop that runs until the specified time has elapsed. Inside the loop, it performs a heavy mathematical operation (`math.sqrt`) repeatedly to keep the CPU busy.

```python
end = time.time() + burn/1000.0
while time.time() < end:
    x += math.sqrt(12345.678)  # cpu spin
```

## Why is this useful for HPA?
HPA scales pods based on metric thresholds (like "Scale up if CPU usage > 50%"). 
1. **Idle State**: Under normal conditions, this app consumes almost zero CPU.
2. **Stress Test**: By hitting the endpoint with a large `burn_ms` value (e.g., `curl "http://pod-ip:8080/?burn_ms=5000"`), you can force a pod to use 100% of a CPU core for 5 seconds.
3. **Triggering HPA**: If you run this in a loop from multiple clients, the aggregate CPU utilization of the deployment increases, eventually crossing the HPA threshold and triggering the creation of new pod replicas.
