# ──────────────────────────────────────────────────
# Problem     Print Function
# Difficulty  Easy
# Subdomain   Introduction
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-05-25, 12:27 p.m.
# Technique   string-concatenation-loop
# Time        O(n)
# Space       O(n)
# Trick       Iterate from 1 to n and append each integer to a string buffer to print the sequence in one line.
# Hint        Use str() conversion inside the loop.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    n = int(input())
    res = ""
    for i in range(1,n+1):
        res += str(i)
    print(res)
