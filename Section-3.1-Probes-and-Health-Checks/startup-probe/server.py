import time
from http.server import BaseHTTPRequestHandler, HTTPServer

START = time.time()
WARMUP_SECONDS = 25

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/healthz":
            # Only healthy after warm-up
            if time.time() - START >= WARMUP_SECONDS:
                self.send_response(200); self.end_headers(); self.wfile.write(b"ok")
            else:
                self.send_response(500); self.end_headers(); self.wfile.write(b"warming")
        elif self.path == "/readyz":
            # Ready a bit after healthy
            if time.time() - START >= WARMUP_SECONDS + 5:
                self.send_response(200); self.end_headers(); self.wfile.write(b"ready")
            else:
                self.send_response(503); self.end_headers(); self.wfile.write(b"not ready")
        else:
            self.send_response(200); self.end_headers(); self.wfile.write(b"hello")

httpd = HTTPServer(("", 8080), Handler)
print("Starting server on :8080")
httpd.serve_forever()
