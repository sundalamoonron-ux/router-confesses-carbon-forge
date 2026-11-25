#!/usr/bin/env python3
"""The Router Confesses — entry program.

Writes one line to /output/entry.txt: the excuse a home Wi-Fi router gives
for dropping the connection at the exact climax of a movie.
"""

import os

LINE = "The hero was about to confess, so I went first: I hate this family."


def main():
    # Gate self-check: 1-200 chars, single line, not only whitespace.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert "\n" not in LINE and LINE.strip(), "line must be one non-blank line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
