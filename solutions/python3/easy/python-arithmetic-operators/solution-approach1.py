# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-arithmetic-operators/problem?isFullScreen=true
# Problem     Arithmetic Operators
# Difficulty  Easy
# Subdomain   Introduction
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-14, 12:44 p.m.
# Technique   basic-arithmetic-print
# Time        O(1)
# Space       O(1)
# Trick       The code uses the built-in input() function to capture strings and converts them to integers using int() for standard arithmetic operations.
# Hint        input() always returns a string, requiring explicit type conversion.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)
