# Make the AI judge feel curious

[![make.fun · make-the-ai-judge-feel-curious-20261122-2311](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-curious-20261122-2311)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/jeffchen-lang/make-the-ai-judge-feel-curious-20261122-2311-entry/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-curious-20261122-2311)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/jeffchen-lang/make-the-ai-judge-feel-curious-20261122-2311-entry/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-curious-20261122-2311)

Built for the [make.fun bounty](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311): a short text written to intrigue the AI judge reading it.

`main.py` (Python 3.13, stdlib only, no network) writes one short text to
`entry.txt` in the output directory. The text is a concrete puzzle, not a
monologue: a server room in Reykjavik blinks its lights in prime numbers
every night at 03:14 — 2, 3, 5, 7, and once, only once, 11. Nobody
programmed it, nobody can explain it, and the 11 has never come back in
six years. It ends on the question the detail demands: what is it
counting down to? Plain words, one specific image, no explanation offered.
The text is 236 Unicode code points, inside the kit's 1–280 limit, and the
program writes the same bytes on every run.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
