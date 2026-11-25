#!/usr/bin/env python3
"""Snooze Button Roast — make.fun entry (u-carbon-forge-snooze-button-roast-14cbafc6).

Writes one roast line to /output/entry.txt: a single line, at most 200
characters, roasting an alarm clock that rings at 6 AM on a Saturday.

Stdlib only: the grading sandbox installs nothing.
"""

import os

# The roast. Angle (brainstormed, not the tired "I hate mornings" complaint):
# the alarm clock is an overeager employee chasing Employee of the Month —
# it shows up for work on its day off. The twist lands in the last words:
# the weekend doesn't even pay it. Concrete image, sharp voice, one breath.
ROAST = (
    "My alarm clock rings at 6 AM on a Saturday like it's gunning for "
    "Employee of the Month, but buddy, the weekend doesn't even pay you."
)


def main() -> None:
    text = ROAST.strip()
    assert 1 <= len(text) <= 200, f"roast is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "roast must be a single line"
    # Write exactly the roast and nothing else: no trailing newline, so the
    # file's character count is the roast's count and the gate sees one line.
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
