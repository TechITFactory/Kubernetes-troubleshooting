from http.server import BaseHTTPRequestHandler, HTTPServer


class H(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/healthz":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"ok")
        elif self.path == "/":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"hello")
        else:
            # Anything else (including /readyz) is NOT ready -> probe fails.
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"not found")


HTTPServer(("", 8080), H).serve_forever()
