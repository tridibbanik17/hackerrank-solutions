# ──────────────────────────────────────────────────
# Problem     Maximum Draws
# Difficulty  Easy
# Subdomain   Fundamentals
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-05-25, 01:50 p.m.
# Technique   pigeonhole-principle-math
# Time        O(1)
# Space       O(1)
# Trick       Apply the pigeonhole principle by drawing all n items plus one additional item to guarantee a matching pair.
# Hint        Direct arithmetic return n + 1
# ──────────────────────────────────────────────────

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumDraws' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def maximumDraws(n):
    # Write your code here
    return n+1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = maximumDraws(n)

        fptr.write(str(result) + '\n')

    fptr.close()
