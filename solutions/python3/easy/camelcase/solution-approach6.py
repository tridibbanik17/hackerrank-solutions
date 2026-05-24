# ──────────────────────────────────────────────────
# Problem     CamelCase
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-05-24, 06:28 p.m.
# Technique   ord-ascii-scan
# Time        O(n)
# Space       O(1)
# Trick       Using ord() to check ASCII ranges avoids locale-specific behavior of isupper() but requires manual range management.
# Hint        ord('A')=65, ord('Z')=90
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
# ord('A')=65, ord('Z')=90

def camelcase(s):
    num_of_words = 1
    # Write your code here
    for i in range(len(s)):
        if ord(s[i]) >=65 and ord(s[i]) <= 90:
            num_of_words += 1
    return num_of_words
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
