#!/usr/bin/env python3
"""Time Machine Warning Label entry for make.fun.

Writes one warning label for a time machine (117 characters, within the
120-character gate) to /output/entry.txt.

Deterministic: no randomness, no network access, no time dependence.
Standard library only.
"""

import os

LINE = "WARNING: Do not argue with your past self. He knows every weak spot you have, and HR has already ruled in his favour."


def main():
    """Write the entry line to /output/entry.txt, exactly as-is."""
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
