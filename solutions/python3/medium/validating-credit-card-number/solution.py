# ──────────────────────────────────────────────────
# Problem     Validating Credit Card Numbers
# Difficulty  Medium
# Subdomain   Regex and Parsing
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-05-22, 04:37 p.m.
# ──────────────────────────────────────────────────

import re

def valid_card(number):
    if re.fullmatch(r'\d{4}-\d{4}-\d{4}-\d{4}',number):
        number = number.replace("-","")
    if not re.fullmatch(r'[456]\d{15}',number):
        return False
    if re.search(r'(\d)\1{3,}',number):
        return False
    return True
    
N = int(input())
for _ in range(N):
    number = input().strip()
    if valid_card(number):
        print("Valid")
    else:
        print("Invalid")
