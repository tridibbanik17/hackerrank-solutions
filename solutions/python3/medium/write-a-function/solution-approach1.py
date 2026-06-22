# ──────────────────────────────────────────────────
# Problem     Write a function
# Difficulty  Medium
# Subdomain   Introduction
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-06-21, 10:14 p.m.
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

