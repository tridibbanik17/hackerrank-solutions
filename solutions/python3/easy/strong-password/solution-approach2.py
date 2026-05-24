# ──────────────────────────────────────────────────
# Problem     Strong Password
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-05-24, 07:41 p.m.
# Technique   boolean-any-count
# Time        O(n)
# Space       O(1)
# Trick       Calculate the maximum between missing character types and the remaining length needed to reach six characters.
# Hint        Use any() with generator expressions for concise character type validation.
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
# Use any() with generator expressions for concise character type validation.

def minimumNumber(n, password):
    special_chars = '!@#$%^&*()-+'
    conditions = [
        any(c.isdigit() for c in password),
        any(c.islower() for c in password),
        any(c.isupper() for c in password),
        any(c in special_chars for c in password)
    ]
    
    false_conditions = conditions.count(False)
    min_for_length = max(0, 6 - n)
    
    return max(false_conditions, min_for_length)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
