from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
PORT = 8080
print(f"Serving on :{PORT}")
with TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
    httpd.serve_forever()
