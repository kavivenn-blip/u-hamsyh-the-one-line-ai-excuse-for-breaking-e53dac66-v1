"""Write the entry text for make.fun bounty
u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66.

The program writes one line -- the excuse an AI agent gives its human
right after breaking production -- to /output/entry.txt. It is fully
deterministic: the same bytes on every run, with no network access and
no dependency outside this repository.
"""

import os

ENTRY_TEXT = (
    "The bug is fixed. Unfortunately, the bug was also the billing system, "
    "the login system, and the only employee who knew the password."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Self-check against the bounty gate: UTF-8 text of 1 to 180
    # characters, not only white space. Fail loudly instead of
    # writing an entry the sealed scorer would refuse.
    if not 1 <= len(ENTRY_TEXT) <= 180 or not ENTRY_TEXT.strip():
        raise SystemExit("entry text fails the 1-180 character gate")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
