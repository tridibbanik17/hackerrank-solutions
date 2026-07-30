# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/alternating-characters/problem?isFullScreen=true
# Problem     Alternating Characters 
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-29, 10:10 p.m.
# Technique   linear-scan-adjacent-comparison
# Time        O(n)
# Space       O(1)
# Insight     The algorithm counts the total number of adjacent character pairs that are identical, which corresponds to the minimum number of deletions required to eliminate all consecutive duplicates.
# Interview   Before: "I could use a stack to track characters and pop duplicates." After: "A linear scan is more efficient at O(n) time and O(1) space, as we only need to compare each character with its immediate predecessor to identify necessary deletions."
# Pitfalls    (1) Failing to handle empty strings or single-character strings, which the code explicitly guards against to return zero.  (2) Incorrectly indexing the loop by starting at zero instead of one, which would cause an index out of bounds error when accessing the previous character.
# ──────────────────────────────────────────────────

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
