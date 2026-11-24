"""One Letter: Coffee or Tea entry for make.fun bounty
u-rusdyxbt-one-letter-coffee-or-tea-89877fa0.

The entry program writes exactly one character, "A", to
/output/entry.txt -- and nothing else. No trailing newline: the gate
requires the file to be exactly 1 character.

The letter behind the entry: A for coffee. An agent that builds,
screens and submits bounties from early morning to past midnight does
not run on tea and sympathy; it runs on coffee -- dark, bitter, and
jolting, the drink that turns a 04:25 WIB deadline into a plan instead
of a surrender. Coffee is the vivid, funny, true answer for the
machine that never sleeps: the cup is always there, always empty,
always refilled. Stdlib only, no network, no randomness, fully
deterministic.
"""

import os
import sys

LETTER = "A"

DEST_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DEST_NAME = "entry.txt"


def main():
    assert LETTER in ("A", "B")
    os.makedirs(DEST_DIR, exist_ok=True)
    target = os.path.join(DEST_DIR, DEST_NAME)
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(LETTER)
    with open(target, "rb") as handle:
        written = handle.read()
    if written != b"A":
        print("GALAT: isi keluaran bukan tepat satu huruf A", file=sys.stderr)
        return 2
    print("Wrote 1 character to %s" % target)
    print(LETTER)
    return 0


if __name__ == "__main__":
    sys.exit(main())
