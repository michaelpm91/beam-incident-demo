"""Small, dependency-free service for the incident demo."""

import json
import logging
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/health":
            self.send_error(404)
            return
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"healthy\n")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    config = json.loads(Path(__file__).with_name("config.json").read_text())
    port = config["listen_port"]
    logging.info("Starting incident-demo on 127.0.0.1:%s", port)
    HTTPServer(("127.0.0.1", port), Handler).serve_forever()
