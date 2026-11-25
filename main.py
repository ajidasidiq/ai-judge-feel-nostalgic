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
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
