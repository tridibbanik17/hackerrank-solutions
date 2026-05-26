# ──────────────────────────────────────────────────
# Problem     Count Elements Greater Than Previous Average
# Difficulty  Easy
# Subdomain   Software Engineer Prep Kit
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-05-26, 10:55 a.m.
# Technique   running-average-scan
# Time        O(n)
# Space       O(1)
# Trick       Maintain a running sum to calculate the average in constant time per element, avoiding redundant O(n) summation inside the loop.
# Hint        Use a running sum variable to keep complexity linear.
# ──────────────────────────────────────────────────

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'countResponseTimeRegressions' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY responseTimes as parameter.
#

def countResponseTimeRegressions(responseTimes):
    # Write your code here
    res = 0
    prev_sum = 0
    if len(responseTimes) == 0 or len(responseTimes) == 1:
        return 0
    for i in range(1,len(responseTimes)):
        prev_sum += responseTimes[i-1]
        prev_avg = prev_sum / i       
        if responseTimes[i] > prev_avg:
            res += 1
    return res

if __name__ == '__main__':
    responseTimes_count = int(input().strip())

    responseTimes = []

    for _ in range(responseTimes_count):
        responseTimes_item = int(input().strip())
        responseTimes.append(responseTimes_item)

    result = countResponseTimeRegressions(responseTimes)

    print(result)
