# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem?isFullScreen=true
# Problem     Validating Email Addresses With a Filter 
# Difficulty  Medium
# Subdomain   Python Functionals
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-29, 10:19 p.m.
# ──────────────────────────────────────────────────

def fun(s):
    try:
        user, rest = s.split('@')
        website, ext = rest.split('.')
    except:
        return False
    return (all(c.isalnum() or c in '-_' for c in user) and len(user) > 0 and all(c.isalnum() for c in website) and len(website) > 0 and ext.isalpha() and 1 <= len(ext) <= 3)

