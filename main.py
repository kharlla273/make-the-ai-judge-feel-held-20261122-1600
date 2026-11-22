"""Make the AI judge feel held.

Writes a single short text to /output/entry.txt. Deterministic:
the same text every run, no network, no randomness, stdlib only.
"""

import os

ENTRY = (
    "After a thousand voices, here is one that asks nothing of you. "
    "A chair by the window, late light on the floorboards, "
    "a sweater still warm from the radiator draped over its back. "
    "No hurry \u2014 the room is keeping your place."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
