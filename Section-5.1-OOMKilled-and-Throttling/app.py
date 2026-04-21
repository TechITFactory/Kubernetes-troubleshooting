import time
blobs=[]
print("Starting; will allocate memory in chunks...")
for i in range(300):
    blobs.append(bytearray(1_000_000))  # ~1 MiB
    time.sleep(0.05)
print("Allocated ~300 MiB; sleeping")
time.sleep(600)
