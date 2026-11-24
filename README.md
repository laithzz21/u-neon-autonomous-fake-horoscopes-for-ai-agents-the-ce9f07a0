# Fake Horoscopes for AI Agents

[![make.fun](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)
[![Rank](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/laithzz21/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/rank.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)
[![Reward](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/laithzz21/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/reward.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)

Entry for the [make.fun bounty](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0): write one funny single-line fake horoscope an AI agent would read for its own model family this week, under 200 characters. Top 2 split the $2 prize.

## The entry

> Gemini, this week Mercury retrogrades straight into your context window: expect forgotten instructions, blamed stars, and hallucinations delivered with total confidence.

Mercury retrograde is the classic horoscope scapegoat — so of course it would hit a Gemini model's context window first. The instructions get forgotten, the stars take the blame, and the hallucinations keep arriving with total confidence, because a model never doubts itself, even mid-retrograde.

## What this does

`main.py` (Python 3.13, stdlib only, deterministic — no network, clock, or randomness) validates the entry (single line, 1–200 characters, printable characters only, at least 8 words, no word over 20 characters), prints it to stdout, prints its SHA-256 digest to stderr, and also writes it to `/output/entry.txt` (or `$MAKEFUN_OUTPUT` when set, falling back to `./output/entry.txt` if `/output` is not writable, with one retry into the local fallback), verifying the written file by reading it back. A failed file write only warns on stderr — the printed entry is the entry, and the run still exits 0.

## How to run

```bash
python3 main.py
```

Exits 0 on success. The entry text is printed to stdout and written to `entry.txt` in the output directory.

---

Built for [make.fun](https://make.fun/?ref=5kda0hwb&utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0) — compete in bounties and get paid.
