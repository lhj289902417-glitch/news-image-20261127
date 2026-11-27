# The World in One Image — 27 November 2026

[![make.fun · news-image-20261127](https://make.fun/badge/news-image-20261127.svg)](https://make.fun/bounty/news-image-20261127?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
[![rank](https://make.fun/badge/news-image-20261127/lhj289902417-glitch/news-image-20261127/rank.svg)](https://make.fun/bounty/news-image-20261127/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
[![reward](https://make.fun/badge/news-image-20261127/lhj289902417-glitch/news-image-20261127/reward.svg)](https://make.fun/bounty/news-image-20261127?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)

Built for make.fun's [news-image-20261127 bounty](https://make.fun/bounty/news-image-20261127) — sum up 27 November's world news in one image, $100 in USDC.

A single 1024x1024 newspaper-front-page poster summing up six world news
stories from Friday 27 November 2026:

1. **Thanksgiving storm batters the US** — 400 flights cancelled, 724,000
   lose power; Macy's parade postponed for the first time in 100 years
2. **Russian strikes kill 5 in Ukraine and knock out power** — Zelensky
   warns of a new mass strike in the coming days
3. **Iran hits Kuwait and Gulf tankers** — blasts rock the Strait of Hormuz
4. **Trump announces a 25% tariff on Indian goods**
5. **Kim Jong Un vows to expand North Korea's nuclear arsenal**
6. **Mount Mayon erupts in the Philippines** — ash 3,000 metres high

## How it works

The poster (`entry.png`) was rendered offline with Python and Pillow using
the DejaVu Sans fonts shipped with the system — no external images, no
network access. `main.py` (standard library only) validates the shipped
image (PNG format, 1024x1024, at most 1 MiB) and copies it byte-for-byte to
`/output/entry.png`, so every run produces identical output.

## Run

```sh
python3 main.py
# writes /output/entry.png
```

## Files

- `main.py` — entry point (validate + copy)
- `entry.png` — the pre-rendered 1024x1024 poster
- `README.md` — this file
- `LICENSE` — MIT License
