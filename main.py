"""Emit a single curiosity-flavoured text to entry.txt.

The piece is built around one unexplained, concrete image: a server room
in Reykjavik whose lights blink in primes, with a lone 11 that appeared
once and never returned. It states only what is observed, offers no
theory, and closes on the question the anomaly leaves behind. The aim
is to leave the judge wondering rather than lecturing it — a small,
precisely observed mystery told in plain sentences, with nothing resolved. The program is fully
deterministic: it writes the same bytes on every run, uses no network,
no clock and no randomness.
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
    if not 1 <= len(TEXT) <= 280:
        print(
            f"refusing: text is {len(TEXT)} code points, must be 1-280",
            file=sys.stderr,
        )
        return 1
    if not TEXT.strip():
        print("refusing: text is only whitespace", file=sys.stderr)
        return 1
    out_path.write_bytes(TEXT.encode("utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
