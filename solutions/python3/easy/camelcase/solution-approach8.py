# ──────────────────────────────────────────────────
# Problem     CamelCase
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-05-24, 06:35 p.m.
# Technique   filter-isupper-count
# Time        O(n)
# Space       O(n)
# Trick       Using filter with str.isupper provides a concise functional approach, though it creates an intermediate list that consumes extra memory com…
# Hint        isupper() checks ASCII 65-90; list conversion is required for len()
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
# isupper() checks ASCII 65-90; list conversion is required for len()

def camelcase(s):
    return 1 + len(list(filter(str.isupper, s)))
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
