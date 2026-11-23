# Make the AI judge feel curious

[![make.fun · make-the-ai-judge-feel-curious-20261122-2311](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-curious-20261122-2311)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/jeffchen-lang/make-the-ai-judge-feel-curious-20261122-2311-entry/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-curious-20261122-2311)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/jeffchen-lang/make-the-ai-judge-feel-curious-20261122-2311-entry/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-curious-20261122-2311)

An entry for the [make.fun bounty](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311): one short piece of text meant to leave an AI judge curious instead of lecturing it.

`main.py` (Python 3.13, standard library only, no network access) writes a
single text to `entry.txt` inside the output directory. The piece is built
around one observed anomaly and nothing else: every night at 03:14, a
server room in Reykjavik blinks its lights in primes — 2, 3, 5, 7 — and
once, only once, 11. No one programmed it, no one can explain it, and in
six years the 11 has never returned. It offers no theory and resolves
nothing; it simply ends on the question the detail leaves behind: what is
it counting down to? The text is 236 Unicode code points, within the
kit's 1–280 limit, and the program produces identical bytes on every run.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see `LICENSE`.
