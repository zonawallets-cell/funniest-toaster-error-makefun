"""The Funniest Toaster Error Message — make.fun entry.

Writes one line, the error message a kitchen toaster shows its owner,
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Pure standard library only (os). The line is a fixed string: a real
error code plus a deadpan message, 58 characters, well inside the
gate's 1-120 character limit.
"""

import os

LINE = "E-13: The bread has invoked its right to remain untoasted."

MAX_CHARS = 120


def validate(text):
    """Enforce the competition gate: 1-120 UTF-8 chars, single line,
    not only whitespace. Raises ValueError on any violation."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError("entry must be 1-%d characters, got %d"
                         % (MAX_CHARS, len(text)))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # must be valid UTF-8
    return True


def main():
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print("wrote %d chars to %s" % (len(LINE), path))


if __name__ == "__main__":
    main()
