# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/arrays-ds/problem?isFullScreen=true
# Problem     Arrays - DS
# Difficulty  Easy
# Subdomain   Arrays
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-08, 07:25 p.m.
# ──────────────────────────────────────────────────

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'reverseArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

def reverseArray(a):
    # Write your code here
    return a[::-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
