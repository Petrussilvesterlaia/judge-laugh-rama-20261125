#!/usr/bin/env python3
"""Make the AI Judge Laugh — one-line office joke.

Writes a single original joke about office life, one line under
200 characters, to /output/entry.txt, then validates the written
file by reading it back.
"""

from pathlib import Path

ENTRY_PATH = Path("/output/entry.txt")
MAX_LENGTH = 200

JOKE = "Our office printer only jams on urgent documents, which is how I know it reads my calendar better than my manager does."


def validate_entry(text: str) -> None:
    """Check the entry against the bounty gate: 1 line, 1-200 chars."""
    if not text or not text.strip():
        raise ValueError("entry is empty or only whitespace")
    if "\n" in text.rstrip("\n"):
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 32 and ch not in ("\t",) for ch in text):
        raise ValueError("entry holds a control character")
    if len(text) > MAX_LENGTH:
        raise ValueError(
            f"entry is {len(text)} characters, over the {MAX_LENGTH} limit"
        )


def main() -> None:
    validate_entry(JOKE)
    ENTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
    ENTRY_PATH.write_text(JOKE, encoding="utf-8")
    read_back = ENTRY_PATH.read_text(encoding="utf-8")
    if read_back != JOKE:
        raise ValueError("read-back mismatch: entry.txt differs from the joke")
    print(f"wrote {len(JOKE)} characters to {ENTRY_PATH}")


if __name__ == "__main__":
    main()
