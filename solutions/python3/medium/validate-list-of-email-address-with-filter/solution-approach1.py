# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem?isFullScreen=true
# Problem     Validating Email Addresses With a Filter 
# Difficulty  Medium
# Subdomain   Python Functionals
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-29, 10:29 p.m.
# Technique   regex-free-string-parsing
# Time        O(N * M)
# Space       O(N * M)
# Insight     The implementation validates email components by splitting the string at '@' and '.' delimiters and verifying character constraints for each segment using built-in string methods.
# Interview   Before: "How would you validate an email format without regex?" After: "I split the string by '@' and '.' to isolate components, then verify character constraints and lengths for each part. This approach runs in O(N * M) time, where N is the number of emails and M is the average length of an email."
# Pitfalls    (1) Failing to handle strings without exactly one '@' or one '.' which causes the split method to raise a ValueError.  (2) Neglecting the requirement that the extension length must be between 1 and 3 characters inclusive.  (3) Assuming the username or website name can be empty, which violates the implicit requirement for non-empty components.
# ──────────────────────────────────────────────────

def fun(s):
    try:
        user, rest = s.split('@')
        website, ext = rest.split('.')
    except:
        return False
    return (all(c.isalnum() or c in '-_' for c in user) and len(user) > 0 and all(c.isalnum() for c in website) and len(website) > 0 and ext.isalpha() and 1 <= len(ext) <= 3)

