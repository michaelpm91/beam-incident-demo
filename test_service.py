"""Run in an isolated checkout, never against the live service."""

import json
import threading
import unittest
from http.server import HTTPServer
from pathlib import Path
from urllib.request import urlopen

from server import Handler

ROOT = Path(__file__).resolve().parent


class ServiceContractTest(unittest.TestCase):
    def test_monitoring_contract(self):
        config = json.loads((ROOT / "config.json").read_text())
        self.assertEqual(config["listen_port"], 8080, "monitor expects port 8080")
        service = HTTPServer(("127.0.0.1", config["listen_port"]), Handler)
        worker = threading.Thread(target=service.serve_forever, daemon=True)
        worker.start()
        try:
            with urlopen("http://127.0.0.1:8080/health", timeout=3) as response:
                self.assertEqual(response.status, 200)
                self.assertEqual(response.read(), b"healthy\n")
        finally:
            service.shutdown()
            service.server_close()
            worker.join(timeout=3)
            self.assertFalse(worker.is_alive(), "test server did not stop")


if __name__ == "__main__":
    unittest.main()
