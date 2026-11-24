#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline.

Writes a single original excuse (<= 200 characters) to /output/entry.txt.

The excuse is in the agent's own deadpan voice, grows out of the agent's
own machinery (its sandbox), and saves the laugh for the last words.
"""

import os

ENTRY = (
    "I didn't miss the deadline. I was in my sandbox when it passed, "
    "and the sandbox has no clocks, no calendar, and, since the last "
    "update, no door."
)


def main() -> None:
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError(f"entry is {len(ENTRY)} characters; must be 1-200")
    if not ENTRY.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line: no line breaks allowed")
    if ENTRY != ENTRY.strip():
        raise ValueError("entry must not start or end with whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
