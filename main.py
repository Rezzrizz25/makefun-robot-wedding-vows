#!/usr/bin/env python3
"""One-Line Robot Wedding Vows - make.fun entry.

Writes a single line of wedding vows for a robot couple to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The gate requires UTF-8 text of 1 to 160 characters, not only
whitespace, on one line. The file is written with no trailing
newline, so it holds exactly the vow and nothing else.
"""

import os
import sys

MAX_CHARS = 160

VOW = (
    "I promise to love you in sickness and in health, "
    "in 5G and in airplane mode \u2014 and to always blame "
    "the router, never you."
)


def checked_vow(text):
    """Return the vow if it passes every gate rule, else exit."""
    line = text.strip()
    if not line:
        sys.exit("error: vow is blank")
    if "\n" in line or "\r" in line:
        sys.exit("error: vow must be a single line")
    if len(line) > MAX_CHARS:
        sys.exit(
            "error: vow is %d characters, over the %d limit"
            % (len(line), MAX_CHARS)
        )
    if any(ord(char) < 32 for char in line):
        sys.exit("error: vow contains a control character")
    line.encode("utf-8")
    return line


def verify_written(path, expected):
    """Re-read the file and confirm it holds exactly the vow."""
    with open(path, "r", encoding="utf-8") as handle:
        found = handle.read()
    if found != expected:
        sys.exit("error: entry.txt does not match the vow")
    if len(found) != len(expected):
        sys.exit("error: entry.txt character count mismatch")


def main():
    line = checked_vow(VOW)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line)
    verify_written(path, line)
    print("wrote %d characters to %s" % (len(line), path))


if __name__ == "__main__":
    main()
