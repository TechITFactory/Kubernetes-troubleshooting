import signal, threading, time
from http.server import BaseHTTPRequestHandler, HTTPServer

ready = True
def handle_term(signum, frame):
    global ready
    print("SIGTERM: start graceful shutdown")
    ready = False            # stop being Ready ASAP
    time.sleep(2)            # finish in-flight work quickly
    raise SystemExit(0)

class H(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/healthz":
            code = 200 if ready else 503
            self.send_response(code); self.end_headers(); self.wfile.write(b"ok" if ready else b"draining")
        else:
            self.send_response(200); self.end_headers(); self.wfile.write(b"hello")

signal.signal(signal.SIGTERM, handle_term)
HTTPServer(("", 8080), H).serve_forever()
