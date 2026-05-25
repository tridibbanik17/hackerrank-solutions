# ──────────────────────────────────────────────────
# Problem     Strong Password
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-05-24, 08:10 p.m.
# Technique   regex-pattern-matching
# Time        O(n)
# Space       O(1)
# Trick       Calculate missing character types and length deficit, then return the maximum of these two values to satisfy all constraints.
# Hint        Use re.search for concise character class validation.
# ──────────────────────────────────────────────────

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#
# Use re.search for concise character class validation.

def minimumNumber(n, password):
    missing = 0
    if not re.search(r'\d', password): missing += 1
    if not re.search(r'[a-z]', password): missing += 1
    if not re.search(r'[A-Z]', password): missing += 1
    if not re.search(r'[!@#$%^&*()\-+]', password): missing += 1
    
    return max(missing, max(0, 6 - n))
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
