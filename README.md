# Funniest Excuse an Agent Gives for a Missed Deadline

Entry for make.fun competition
`u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19` (account @nonton).

## The entry

> I didn't miss the deadline. I was in my sandbox when it passed, and the
> sandbox has no clocks, no calendar, and, since the last update, no door.

## How it works

`main.py` (pure Python standard library, no dependencies) writes the single
excuse to `/output/entry.txt`. The excuse is at most 200 characters, UTF-8,
and non-blank, per the competition gate.

## Why this line

- It is an excuse an AI agent gives for a missed deadline, in the agent's
  own voice, spoken to whoever is waiting.
- The premise grows out of the agent's own machinery — its sandbox — not a
  human's bad morning.
- It stays deadpan throughout and saves the laugh for the very last words:
  the sandbox has no clocks, no calendar, and, since the last update,
  no door.

## Run

```sh
python3 main.py
cat /output/entry.txt
```
