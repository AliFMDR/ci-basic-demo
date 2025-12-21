from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Endpoint health check
        if self.path == "/health":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"OK")

        # Endpoint version (DITAMBAHKAN)
        elif self.path == "/version":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"1.1.0")

        # Default endpoint
        else:
            self.send_response(200)
            self.end_headers()
            response = {
                "service": "ci-demo",
                "status": "running"
            }
            self.wfile.write(json.dumps(response).encode())


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8000), Handler)
    print("Server running on port 8000")
    server.serve_forever()
