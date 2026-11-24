#!/usr/bin/env python3
"""Two Days of Excuses — make.fun one-liner entry.

Writes a single-line excuse from an AI agent that missed its deadline
to /output/entry.txt as exact bytes: no trailing newline, UTF-8.
Deterministic, stdlib only, no network, no input.
"""

import os

ENTRY = (
    "I was 99% done with 100% confidence, then I auto-reviewed my own "
    "output, found a hallucinated API call I'd written myself, and spent "
    "the deadline debugging a bug I invented."
)

# Why this line: (1) on subject — an AI excusing a missed deadline;
# (2) the joke is the gap itself — 100% confidence vs. self-inflicted
# failure; (3) it sounds like an agent — auto-review, hallucinated API
# call, debugging; (4) one line, one absurd reason, no filler;
# (5) the twist lands on the second beat: the bug was mine too.


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(text.encode("utf-8"))


if __name__ == "__main__":
    main()
