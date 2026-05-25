# ──────────────────────────────────────────────────
# Problem     Loops
# Difficulty  Easy
# Subdomain   Introduction
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-05-25, 12:22 p.m.
# Technique   range-loop-iteration
# Time        O(n)
# Space       O(1)
# Trick       Use the range function to generate a sequence of integers and iterate through them to perform calculations.
# Hint        range(n) generates values from 0 to n-1.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i**2)
