# ──────────────────────────────────────────────────
# Problem     CamelCase
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-05-24, 05:59 p.m.
# Time        O(n)
# Space       O(n)
# Trick       The number of words in CamelCase is equal to the number of uppercase letters plus one.
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
    return len(re.sub(r'([A-Z])', r' \1', s).split())

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
