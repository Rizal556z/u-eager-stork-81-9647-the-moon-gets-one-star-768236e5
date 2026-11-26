"""The Moon Gets One Star -- make.fun entry.

Writes a single one-star review of the Moon (120 characters at most)
to /output/entry.txt, the artifact this program/v1 competition grades.
Pure Python standard library; no network, no model calls.
"""

import os
from pathlib import Path

REVIEW = (
    "1 star. Late once a month, stares through my window all night, "
    "then vanishes for weeks. The star is for the view."
)

OUTPUT_PATH = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))


def main() -> None:
    text = REVIEW.strip()
    assert 1 <= len(text) <= 120, f"review is {len(text)} chars, must be 1-120"
    assert text == REVIEW, "review must be written exactly, with no extra text"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
