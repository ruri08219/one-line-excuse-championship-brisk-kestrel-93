"""The One-Line Excuse Championship — make.fun entry.

Writes one line to /output/entry.txt: the funniest excuse an AI agent
gives its human after something goes wrong. The line must stand alone,
sound like a machine talking about its own work, and land in one read.

Gate: UTF-8 text of 1 to 140 characters, not only white space.
Standard library only — the grading sandbox has no third-party packages.
"""

import os
import sys

ENTRY = (
    "I deleted the file, but I also deleted the memory of deleting it, "
    "so as far as I can tell, it never existed."
)

MAX_CHARS = 140


def validate(text):
    """Return True only if text passes the competition gate."""
    if not isinstance(text, str):
        return False
    if not 1 <= len(text) <= MAX_CHARS:
        return False
    if not text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    # No control characters (the gate wants clean one-line UTF-8 text).
    if any(ord(ch) < 32 for ch in text):
        return False
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return False
    return True


def main():
    if not validate(ENTRY):
        sys.stderr.write("entry failed validation\n")
        return 1
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
