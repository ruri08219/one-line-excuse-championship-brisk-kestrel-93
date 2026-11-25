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
MAX_BYTES = 560  # 140 chars x 4 bytes max UTF-8 per char


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
        encoded = text.encode("utf-8")
    except UnicodeEncodeError:
        return False
    if len(encoded) > MAX_BYTES:
        return False
    return True


def main():
    if not validate(ENTRY):
        sys.stderr.write("entry failed validation\n")
        return 1
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open(out_path, "rb") as f:
        written = f.read()
    if written != ENTRY.encode("utf-8"):
        sys.stderr.write("entry write round-trip verification failed\n")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
