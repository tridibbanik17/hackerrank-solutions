# ──────────────────────────────────────────────────
# Problem     Find a string
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-06-21, 10:21 p.m.
# Technique   sliding-window-slice
# Time        O(n*m)
# Space       O(m)
# Trick       Iterate through all possible start indices and compare slices of the string to the target substring.
# Hint        Slicing creates a new string object of length m.
# ──────────────────────────────────────────────────

def count_substring(string, sub_string):
    count = 0
    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i+len(sub_string)] == sub_string:
            count += 1
    return count

