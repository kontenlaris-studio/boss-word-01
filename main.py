#!/usr/bin/env python3
"""One Word for the Boss — writes exactly one word to /output/entry.txt.

The word: praise on the surface — he sees things the rest of us
cannot. Underneath: things that are not there, delivered with total
confidence, on a roadmap nobody else can read.
"""
import os

WORD = "Visionary."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD + "\n")
    print(f"wrote {path}")


if __name__ == "__main__":
    main()
