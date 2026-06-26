#!/usr/bin/env python3
"""Basic static validation for a Shui Pretty PPT deck folder."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import urlparse


PLACEHOLDERS = re.compile(r"(\[必填\]|TODO|Lorem|placeholder)", re.IGNORECASE)
ASSET_REF = re.compile(r"""(?:src|href)=["']([^"']+)["']""", re.IGNORECASE)


def is_external(value: str) -> bool:
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https", "data", "mailto", "tel", "blob"}


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a Shui Pretty PPT output folder.")
    parser.add_argument("deck_dir", help="Deck folder containing index.html")
    args = parser.parse_args()

    deck_dir = Path(args.deck_dir).expanduser().resolve()
    index = deck_dir / "index.html"
    errors: list[str] = []
    warnings: list[str] = []

    if not deck_dir.exists():
        errors.append(f"Deck folder does not exist: {deck_dir}")
    if not index.exists():
        errors.append(f"Missing index.html: {index}")

    if errors:
        for item in errors:
            print(f"ERROR: {item}", file=sys.stderr)
        return 1

    html = index.read_text(encoding="utf-8", errors="replace")

    if PLACEHOLDERS.search(html):
        warnings.append("Found placeholder-like text.")

    if "/Users/" in html:
        warnings.append("Found absolute macOS filesystem path in HTML.")

    local_refs = []
    missing_refs = []
    for ref in ASSET_REF.findall(html):
        clean = ref.split("#", 1)[0].split("?", 1)[0]
        if not clean or is_external(clean) or clean.startswith("#"):
            continue
        if clean.startswith("/"):
            warnings.append(f"Absolute path reference: {ref}")
            continue
        local_refs.append(clean)
        if not (deck_dir / clean).exists():
            missing_refs.append(clean)

    if missing_refs:
        for ref in sorted(set(missing_refs)):
            errors.append(f"Missing local asset: {ref}")

    slide_like = len(re.findall(r'class=["\'][^"\']*(?:slide|section|page)[^"\']*["\']', html))

    print(f"deck_dir: {deck_dir}")
    print(f"index: {index}")
    print(f"local_refs: {len(local_refs)}")
    print(f"slide_like_blocks: {slide_like}")

    for item in warnings:
        print(f"WARNING: {item}")
    for item in errors:
        print(f"ERROR: {item}", file=sys.stderr)

    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
