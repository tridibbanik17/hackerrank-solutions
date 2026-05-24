# ──────────────────────────────────────────────────
# Problem     CamelCase
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-05-24, 06:29 p.m.
# Technique   isupper-generator-sum
# Time        O(n)
# Space       O(1)
# Trick       Using isupper inside a generator expression provides a concise, memory-efficient way to count uppercase characters without explicit loops.
# Hint        isupper() is equivalent to 65 <= ord(c) <= 90
# ──────────────────────────────────────────────────

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'camelcase' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
# isupper() is equivalent to 65 <= ord(c) <= 90

def camelcase(s):
    return 1 + sum(c.isupper() for c in s)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
