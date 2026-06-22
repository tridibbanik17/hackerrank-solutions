# ──────────────────────────────────────────────────
# Problem     Write a function
# Difficulty  Medium
# Subdomain   Introduction
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-06-21, 10:14 p.m.
# Technique   boolean-logic-short-circuit
# Time        O(1)
# Space       O(1)
# Trick       Combine leap year conditions into a single boolean expression using logical operators to avoid nested if-else blocks.
# Hint        Use parentheses to enforce operator precedence for the OR condition.
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
    
def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

