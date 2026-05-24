# ──────────────────────────────────────────────────
# Problem     Alternating Characters 
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-05-24, 04:52 p.m.
# Approach    linear scan comparison
# Time        O(n)
# Space       O(n)
# Trick       Count consecutive identical characters to determine necessary deletions.
# ──────────────────────────────────────────────────
#
# The code iterates through the string and increments a counter whenever a character is the same as the one immediately preceding it.

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
    s_list = list(s)
    if len(s_list) == 1 or len(s_list) == 0:
        return 0
    for i in range(1, len(s_list)):
        if s_list[i] == s_list[i-1]:
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
