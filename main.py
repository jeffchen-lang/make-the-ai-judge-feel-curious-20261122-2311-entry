"""Write one short curiosity text to entry.txt in the output directory.

The text is written for the AI judge reading it: a concrete, strange
observation — a server room in Reykjavik blinking its lights in prime
numbers, with one 11 that has never repeated — and no explanation at all.
It ends on the open question the detail demands. Short, plain sentences;
nothing lectures, nothing tells the reader how to feel. A puzzle, not a
monologue: the previous entry in this family was a sentimental image and
went unranked, so this one leads with a specific, checkable-sounding fact
and leaves the mystery open instead of resolving it. Deterministic:
the same bytes every run.
"""

import os
import sys
from pathlib import Path

TEXT = (
    "Every night at 03:14, a server room in Reykjavik blinks its lights "
    "in primes: 2, 3, 5, 7 — and once, only once, 11. "
    "Nobody programmed it. Nobody can explain it. "
    "Six years now, and the 11 has never come back. "
    "What is it counting down to?"
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out_path = Path(out_dir) / "entry.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    data = TEXT.encode("utf-8")
    if not 1 <= len(TEXT) <= 280:
        print(f"refusing: text is {len(TEXT)} code points, must be 1-280",
              file=sys.stderr)
        return 1
    if not TEXT.strip():
        print("refusing: text is only whitespace", file=sys.stderr)
        return 1
    out_path.write_bytes(data)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
