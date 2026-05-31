#!/usr/bin/env python
"""Print data URL constants for local assets.

Usage:
  python scripts/embed_assets.py path/to/logo.png path/to/photo.jpg
"""

from __future__ import annotations

import argparse
import base64
import mimetypes
from pathlib import Path


def data_url(path: Path) -> str:
    mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{encoded}"


def js_name(path: Path) -> str:
    stem = "".join(ch if ch.isalnum() else "_" for ch in path.stem)
    if not stem or stem[0].isdigit():
        stem = f"asset_{stem}"
    return stem.upper()


def main() -> int:
    parser = argparse.ArgumentParser(description="Convert assets to JS data URL constants.")
    parser.add_argument("assets", nargs="+", type=Path)
    args = parser.parse_args()

    for asset in args.assets:
        if not asset.exists():
            raise SystemExit(f"Missing asset: {asset}")
        print(f"const {js_name(asset)} = {data_url(asset)!r};")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
