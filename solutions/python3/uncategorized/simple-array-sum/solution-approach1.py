# ──────────────────────────────────────────────────
# Problem     Simple Array Sum
# Difficulty  N/A
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-05-25, 04:45 p.m.
# ──────────────────────────────────────────────────

#!/bin/python3

import os

#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simpleArraySum(ar):
    array_sum = 0
    # Write your code here
    for element in ar:
        array_sum += element
    return array_sum
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
