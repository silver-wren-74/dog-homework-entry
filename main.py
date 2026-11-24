#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse — make.fun bounty entry.

Writes a single original line (1 to 200 characters) to /output/entry.txt,
exactly as the competition gate expects: one funny single-line excuse a
dog gives after being caught eating the homework. The dog pleads dog law:
its name was on the homework, so it was the dog's — and then it ate the
evidence. No regrets, no crumbs, no witnesses.
"""

import os

# REVISION PASS (against the RULES judging criteria, in order):
# 1. Same dog-voice excuse, caught in the act — kept.
# 2. Bigger laugh: draft 1's courtroom tail ("before you could appeal.
#    Case closed.") was a flat lawyer joke. The new tail turns the dog
#    into the evidence-eater: "No regrets, no crumbs, no witnesses" —
#    the twist lands in one breath and the dog believes it did nothing
#    wrong. "In dog law" keeps the ownership twist (my name on it =
#    mine) while sounding like a dog, not a person in a suit.
# 3. Dog priorities throughout: territory, ownership, appetite, zero
#    embarrassment — no apology, no human shame.
# 4. Standalone: one sentence chain, no setup, nothing needs a second
#    line to make sense.
# 5. Fresh: no cat, no taste of paper, no good boy — the stock lines
#    are all avoided; the evidence-eating angle is the fresh bit.
LINE = (
    "It had my name on it, so in dog law it was mine. "
    "I ate it. No regrets, no crumbs, no witnesses."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line must be 1-200 chars, got {len(text)}"
    assert "\n" not in text, "entry must be a single line"
    # Single line, no trailing newline: the gate counts the file's characters.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
