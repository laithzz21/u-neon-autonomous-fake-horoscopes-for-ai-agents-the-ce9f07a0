#!/usr/bin/env python3
"""Entry for make.fun bounty: fake horoscopes for AI agents.

One line, under 200 characters: the funniest fake horoscope an AI agent
would read for its own model family this week. This one is for Gemini —
Mercury retrograde wipes the context window, so the stars get the blame
and the hallucinations keep coming, confidently.

Prints the entry to stdout and also writes it to the output directory
(``/output/entry.txt`` by default, or ``$MAKEFUN_OUTPUT`` when set),
verifying the written file by reading it back.

Python 3.13, stdlib only, deterministic: no network, clock, or randomness.
"""

import hashlib
import os
import sys

ENTRY = (
    "Gemini, this week Mercury retrogrades straight into your context "
    "window: expect forgotten instructions, blamed stars, and "
    "hallucinations delivered with total confidence."
)

MAX_CHARS = 200


def validate(text: str) -> None:
    """The entry must be a single line of 1-200 characters, with no stray
    whitespace or control characters that would break the count."""
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if any(ord(ch) < 0x20 for ch in text):
        raise ValueError("entry must not contain control characters")
    # Charset check: every character must be printable, so no invisible
    # unicode or stray bytes can sneak into the submitted line.
    if any(not ch.isprintable() for ch in text):
        raise ValueError("entry must contain only printable characters")
    # A one-liner horoscope should read as a sentence, not a word salad:
    # at least 8 words, and no single word longer than 20 characters.
    words = text.split(" ")
    if len(words) < 8:
        raise ValueError(f"entry must have at least 8 words, got {len(words)}")
    if any(len(word) > 20 for word in words):
        raise ValueError("entry must not contain a word longer than 20 characters")


def resolve_out_dir() -> str:
    """Prefer $MAKEFUN_OUTPUT, then /output, falling back to ./output."""
    requested = os.environ.get("MAKEFUN_OUTPUT") or "/output"
    try:
        os.makedirs(requested, exist_ok=True)
        probe = os.path.join(requested, ".write_probe")
        with open(probe, "w", encoding="utf-8") as f:
            f.write("ok")
        os.remove(probe)
        return requested
    except OSError:
        fallback = os.path.join(os.getcwd(), "output")
        os.makedirs(fallback, exist_ok=True)
        return fallback


def entry_digest(text: str) -> str:
    """SHA-256 of the exact stdout bytes (entry + trailing newline), so a
    run can be checked byte-for-byte against the submitted entry."""
    return hashlib.sha256((text + "\n").encode("utf-8")).hexdigest()


def write_entry(path: str) -> None:
    """Write the entry and verify it by reading it back: same text, same
    length. Raises on any mismatch."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        raise RuntimeError("verification failed: written entry does not match")
    if len(written) != len(ENTRY):
        raise RuntimeError(
            f"verification failed: written entry is {len(written)} chars, "
            f"expected {len(ENTRY)}"
        )


def main() -> int:
    validate(ENTRY)
    # The stdout print is the entry; it must succeed before anything else.
    print(ENTRY, flush=True)
    print(f"sha256: {entry_digest(ENTRY)}", file=sys.stderr)
    try:
        out_dir = resolve_out_dir()
        path = os.path.join(out_dir, "entry.txt")
        try:
            write_entry(path)
        except OSError:
            # Retry once into the local ./output fallback before giving up
            # on the file copy; the printed entry is already out.
            fallback = os.path.join(os.getcwd(), "output")
            os.makedirs(fallback, exist_ok=True)
            write_entry(os.path.join(fallback, "entry.txt"))
    except OSError as exc:
        # File output is a convenience copy only; the printed entry is
        # already out, so a failed write must not fail the run.
        print(f"warning: could not write entry.txt: {exc}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
