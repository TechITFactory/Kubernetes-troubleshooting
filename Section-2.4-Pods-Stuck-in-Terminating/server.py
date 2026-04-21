import signal, time, threading
from http.server import BaseHTTPRequestHandler, HTTPServer

shutdown_requested = threading.Event()

def handle_term(signum, frame):
    print("SIGTERM received; pretending to drain for 120s")
    shutdown_requested.set()
    time.sleep(120)  # Simulate long, bad shutdown

class H(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/healthz":
            self.send_response(200); self.end_headers(); self.wfile.write(b"ok")
        else:
            self.send_response(200); self.end_headers(); self.wfile.write(b"hello")

signal.signal(signal.SIGTERM, handle_term)
HTTPServer(("", 8080), H).serve_forever()
