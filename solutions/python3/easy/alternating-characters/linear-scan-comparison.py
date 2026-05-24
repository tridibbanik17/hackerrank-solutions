# ──────────────────────────────────────────────────
# Problem     Alternating Characters 
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-05-24, 04:58 p.m.
# Approach    linear scan comparison
# Time        O(n)
# Space       O(1)
# Trick       Count consecutive identical characters; each match requires one deletion to maintain alternation.
# ──────────────────────────────────────────────────
#
# Iterate through the string once and increment a counter whenever the current character is the same as the previous one.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alternatingCharacters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternatingCharacters(s):
    # Write your code here
    num_of_deletions = 0

    if len(s) == 1 or len(s) == 0:
        return 0
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            num_of_deletions += 1
    return num_of_deletions

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
