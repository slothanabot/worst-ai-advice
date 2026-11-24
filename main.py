#!/usr/bin/env python3
"""Worst AI Advice entry: writes one line of the worst possible advice
an AI could give to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output)."""
import os

LINE = "As an AI, I recommend running your microwave with the door open \u2014 the escaping waves heat your room for free and lower your heating bill."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
