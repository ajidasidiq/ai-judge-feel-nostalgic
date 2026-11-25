#!/usr/bin/env python3
"""Write one childhood-memory sentence to /output/entry.txt.

Entry for the make.fun bounty "Make the AI Judge Feel Nostalgic:
A Childhood Memory" (u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363).

The program is fully deterministic and needs no input, no network and no
arguments: it writes the same bytes to /output/entry.txt on every run.
The text is a single sentence of 241 characters, inside the 1-280 gate.
"""

import os

ENTRY = (
    "Every evening my mother stood in the doorway calling my name as the "
    "streetlights buzzed on one by one and the smell of frying garlic "
    "drifted from the kitchen, and I always pretended not to hear her, "
    "just to steal one more minute of the game."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate: one sentence, 1-280 chars, no trailing newline, no blank text.
    if not 1 <= len(ENTRY) <= 280:
        raise ValueError(f"entry is {len(ENTRY)} chars, gate allows 1-280")
    if ENTRY.strip() != ENTRY or "\n" in ENTRY:
        raise ValueError("entry must be a single non-blank line")
    if ENTRY.count(".") != 1 or not ENTRY.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Post-write check: what landed on disk must be byte-identical.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != ENTRY:
        raise ValueError("entry.txt on disk does not match the entry")
    print(f"wrote {len(ENTRY)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
