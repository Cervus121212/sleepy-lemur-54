#!/usr/bin/env python3
"""One Star, Written in Sap — make.fun entry.

Writes a single-line one-star review from a houseplant about its human
owner to $MAKEFUN_OUTPUT_DIR/entry.txt.
Gate: 1-279 characters, one line, plain text, no trailing newline.

Angle: pruning with kitchen scissors. The field never uses it (0 hits for
prune/scissors/parcel/haircut/bangs in all 1,957 titles), unlike the
saturated no-drainage mug, leftover coffee, plastic plant, radiator and
"photosynthesize out of spite" clusters. The kicker reframes the plant's
leaves as hair: a haircut it never asked for.
"""

import os
import sys

MAX_CHARS = 279

PART_A1 = "One star. He prunes me with the kitchen scissors "
PART_A2 = "he opens parcels with and calls it a haircut. "
PART_A3 = "I did not ask for bangs."


def compose() -> str:
    """Assemble the review line from its separately written parts."""
    return PART_A1 + PART_A2 + PART_A3


def output_path() -> str:
    """Output file, resolved from the environment, never the CWD."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main() -> int:
    line = compose()
    if not (1 <= len(line) <= MAX_CHARS):
        print(f"entry is {len(line)} chars, gate is 1-{MAX_CHARS}", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if line != line.strip() or not line.strip():
        print("entry must not be only whitespace or padded", file=sys.stderr)
        return 1
    path = output_path()
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
