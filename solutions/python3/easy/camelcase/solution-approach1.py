# ──────────────────────────────────────────────────
# Problem     CamelCase
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-05-24, 11:09 p.m.
# Technique   filter-isupper-count
# Time        O(n)
# Space       O(n)
# Trick       Count uppercase letters and add one to account for the first word, leveraging the functional filter pattern for concise iteration.
# Hint        str.isupper is a clean alternative to manual ASCII range checks.
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

def camelcase(s):
    return 1 + len(list(filter(str.isupper, s)))
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
