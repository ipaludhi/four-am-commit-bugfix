#!/usr/bin/env python3
"""The 4AM Commit: Funniest Agent Bug-Fix Message.

Writes one commit message — the note an AI agent leaves after a long night
fixing its own bugs — to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
"""
import os

ENTRY = "fix: removed the bug. It was in the function that removes bugs. I have questions for past me. Past me is me."

# Gate self-check (mirrors the sealed scorer): 1-200 chars, not only whitespace.
assert 1 <= len(ENTRY) <= 200 and ENTRY.strip(), "entry fails the gate"


def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
