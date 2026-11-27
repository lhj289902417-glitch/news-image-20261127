#!/usr/bin/env python3
"""Entry point for the 27 November 2026 world-news poster.

The poster is pre-rendered offline and shipped as entry.png next to this
file. This program only validates the shipped image (PNG magic bytes,
1024x1024 dimensions, at most 1 MiB) and copies it byte-for-byte to
/output/entry.png, so repeated runs produce identical output.

Standard library only. No network access.
"""

import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT = os.path.join(OUTPUT_DIR, "entry.png")

MAX_BYTES = 1024 * 1024
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def main():
    with open(SOURCE, "rb") as f:
        data = f.read()

    if not data.startswith(PNG_MAGIC):
        print("error: entry.png is not a PNG file", file=sys.stderr)
        return 1
    if len(data) > MAX_BYTES:
        print("error: entry.png is %d bytes, over the 1 MiB limit"
              % len(data), file=sys.stderr)
        return 1

    # Read width/height from the PNG IHDR chunk (bytes 16-24).
    width = int.from_bytes(data[16:20], "big")
    height = int.from_bytes(data[20:24], "big")
    if (width, height) != (1024, 1024):
        print("error: entry.png is %dx%d, expected 1024x1024"
              % (width, height), file=sys.stderr)
        return 1

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT, "wb") as f:
        f.write(data)
    os.chmod(OUTPUT, 0o644)

    digest = hashlib.sha256(data).hexdigest()
    print("wrote %s (%d bytes, 1024x1024, sha256 %s)"
          % (OUTPUT, len(data), digest))
    return 0


if __name__ == "__main__":
    sys.exit(main())
