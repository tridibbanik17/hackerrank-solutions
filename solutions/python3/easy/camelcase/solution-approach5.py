# ──────────────────────────────────────────────────
# Problem     CamelCase
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-05-24, 06:09 p.m.
# Technique   ord-ascii-scan
# Time        O(n)
# Space       O(1)
# Trick       Uses ord() to manually check ASCII ranges for uppercase letters instead of the higher-level isupper() method. This approach is highly performant as it avoids method call overhead and string object creation, though it is less idiomatic than using c.isupper().
# Hint        ord(c) in range(65, 91) is equivalent to c.isupper()
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
# ord(c) in range(65, 91) is equivalent to c.isupper()

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
