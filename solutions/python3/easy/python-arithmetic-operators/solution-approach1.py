# ──────────────────────────────────────────────────
# Problem     Arithmetic Operators
# Difficulty  Easy
# Subdomain   Introduction
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-05-25, 12:21 p.m.
# Technique   basic-arithmetic-operators
# Time        O(1)
# Space       O(1)
# Trick       Perform standard arithmetic operations directly on integer inputs using the built-in plus, minus, and multiply operators.
# Hint        Use int() to cast input strings before performing math.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)
