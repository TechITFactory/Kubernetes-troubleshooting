from http.server import BaseHTTPRequestHandler, HTTPServer
import time, math, urllib.parse as u

class H(BaseHTTPRequestHandler):
    def do_GET(self):
        qs = u.parse_qs(u.urlparse(self.path).query)
        burn = int(qs.get("burn_ms",[0])[0])
        end = time.time() + burn/1000.0
        x = 0.0
        while time.time() < end:
            x += math.sqrt(12345.678)  # cpu spin
        self.send_response(200); self.end_headers(); self.wfile.write(b"ok")

HTTPServer(("", 8080), H).serve_forever()
