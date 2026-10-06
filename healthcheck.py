"""Monitoring contract: the service must answer on port 8080."""

import sys
from urllib.error import URLError
from urllib.request import urlopen


if __name__ == "__main__":
    try:
        with urlopen("http://127.0.0.1:8080/health", timeout=3) as response:
            if response.status != 200 or response.read() != b"healthy\n":
                raise ValueError("unexpected health response")
        print("Health check passed")
    except (URLError, ValueError, TimeoutError) as error:
        print(f"Health check failed: {error}", file=sys.stderr)
        sys.exit(1)
