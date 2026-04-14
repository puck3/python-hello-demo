import os
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

PORT = int(os.environ.get("PORT", 8080))
APP_NAME = os.environ.get("APP_NAME", "python-hello")
ENV_NAME = os.environ.get("ENV_NAME", "unknown")


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"status":"ok"}')
            return

        body = json.dumps({
            "message": f"Hello from {APP_NAME}!",
            "env": ENV_NAME,
            "framework": "Python (stdlib)",
        }, indent=2).encode()

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        print(f"{self.address_string()} - {format % args}")


if __name__ == "__main__":
    print(f"Starting {APP_NAME} on port {PORT}")
    HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
