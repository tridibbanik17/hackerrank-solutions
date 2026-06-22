# ──────────────────────────────────────────────────
# Problem     Validating and Parsing Email Addresses
# Difficulty  Easy
# Subdomain   Regex and Parsing
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-06-21, 10:27 p.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
import email.utils

n = int(input())
for _ in range(n):
    line = input()
    name, addr = email.utils.parseaddr(line)
    pattern = r'^[a-zA-Z][a-zA-Z0-9\-\._]+@[a-zA-Z]+\.[a-zA-Z]{1,3}$'
    if re.match(pattern, addr):
        print(email.utils.formataddr((name, addr)))
