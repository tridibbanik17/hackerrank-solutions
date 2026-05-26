# ──────────────────────────────────────────────────
# Problem     Write a function
# Difficulty  Medium
# Subdomain   Introduction
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-05-26, 01:49 a.m.
# Technique   conditional-logic-branching
# Time        O(1)
# Space       O(1)
# Trick       Evaluate divisibility by 400, 100, and 4 in descending order of specificity to determine leap year status correctly.
# Hint        Use boolean logic to simplify nested if-else chains.
# ──────────────────────────────────────────────────

def is_leap(year):
    leap = False
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
    
    return leap

