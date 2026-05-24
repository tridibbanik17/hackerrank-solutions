# ──────────────────────────────────────────────────
# Problem     Python: Division
# Difficulty  Easy
# Subdomain   Introduction
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-05-24, 04:17 p.m.
# Approach    built in operators
# Time        O(1)
# Space       O(1)
# Trick       Python 3 uses // for floor division and / for float division.
# ──────────────────────────────────────────────────
#
# Read two integers and print the results of floor division and float division using built-in operators.

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)
