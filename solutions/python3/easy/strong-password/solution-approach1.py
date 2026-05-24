# ──────────────────────────────────────────────────
# Problem     Strong Password
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-05-24, 07:30 p.m.
# Technique   boolean-flag-tracking
# Time        O(n)
# Space       O(1)
# Trick       Using a boolean list to track condition satisfaction simplifies the logic for calculating the maximum of missing requirements and length de…
# Hint        Use conditions.count(False) to aggregate missing character types efficiently.
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
# Use conditions.count(False) to aggregate missing character types efficiently.

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
