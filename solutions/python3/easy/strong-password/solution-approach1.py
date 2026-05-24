# ──────────────────────────────────────────────────
# Problem     Strong Password
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-05-24, 07:39 p.m.
# Technique   boolean-flags-scan
# Time        O(n)
# Space       O(1)
# Trick       Calculate missing character types and length deficit, then return the maximum of these two values to satisfy both constraints simultaneously.
# Hint        Use conditions.count(False) to quickly tally missing character categories.
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
# Use conditions.count(False) to quickly tally missing character categories.

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    number_of_char = 0
    special_char = '!@#$%^&*()-+'
    conditions = [False] * 4
    for i in range(n):
        if password[i].isdigit():
            conditions[0] = True
        if password[i].islower():
            conditions[1] = True
        if password[i].isupper():
            conditions[2] = True
        if password[i] in special_char:
            conditions[3] = True
    false_condition = conditions.count(False)
    number_of_char = (6 - n)
    extra_char = false_condition - number_of_char
    if extra_char > 0:
        number_of_char += extra_char
    return number_of_char
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
