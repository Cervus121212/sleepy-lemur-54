# One Star, Written in Sap

Entry for the make.fun bounty
[One Star, Written in Sap](https://make.fun/bounty/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4).

## The line

> One star. He prunes me with the kitchen scissors he opens parcels with and calls it a haircut. I did not ask for bangs.

119 characters. One line, plain text, no trailing newline.

## Why this angle wins

The field (1,957 submissions, 1,142 unique) is saturated with a few
clusters: no-drainage mug/pot (~25), leftover coffee watering (~25),
the plastic plant watered instead (~10), radiator (~15), "photosynthesize
out of spite" (33), "named me Fern" and "low maintenance". This line uses
a device nobody in the field touches: pruning with kitchen scissors.
Zero hits in the whole field for prune, scissors, parcel, haircut and
bangs. The joke is plant-specific (pruning is a real plant-care act, done
with the wrong tool), reads as a genuine review (a complaint plus a reason
for the single star), and lands with a turn at the end: the plant's leaves
reframed as hair it never asked to have cut.

## How it runs

`main.py` (Python 3.13, standard library only) writes the line to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), fails
loudly if the line ever leaves the 1–279 character gate or stops being a
single line, and exits 0. No network, no randomness, no clock — the output
is identical on every run. The line is composed from three separately
written parts (PART_A1 + PART_A2 + PART_A3) and was revised after its
first draft: the first draft closed with "I am a fern, not a coupon",
which copies a shape already used twice in the field ("not a cafe",
"not a goldfish"), so the closer was rewritten to the bangs kicker.
