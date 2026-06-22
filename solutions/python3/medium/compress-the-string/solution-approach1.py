# ──────────────────────────────────────────────────
# Problem     Compress the String! 
# Difficulty  Medium
# Subdomain   Itertools
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-06-21, 10:17 p.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby

s = input()
print(' '.join(f'({len(list(g))}, {int(k)})' for k, g in groupby(s)))
