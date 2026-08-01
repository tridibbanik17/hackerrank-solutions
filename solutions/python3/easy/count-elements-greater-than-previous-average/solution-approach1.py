# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/count-elements-greater-than-previous-average/problem?isFullScreen=true
# Problem     Count Elements Greater Than Previous Average
# Difficulty  Easy
# Subdomain   Software Engineer Prep Kit
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-01, 05:40 a.m.
# Technique   running-sum-average-tracking
# Time        O(n^2)
# Space       O(n)
# Insight     The algorithm maintains a list of all preceding elements to calculate the running average at each step, comparing the current element against this value to increment the counter.
# Interview   Before: "I would calculate the average by summing the entire array repeatedly." After: "I track the running sum and count, which is O(n^2) time and O(n) space, ensuring we correctly handle the empty or single-element input cases specified in the constraints."
# Pitfalls    (1) The implementation uses O(n^2) time complexity due to nested summation, which may be inefficient for large inputs.  (2) The code fails to handle potential floating-point precision issues when comparing the current element to the calculated average.  (3) The logic explicitly returns 0 for arrays of length 0 or 1, adhering to the requirement to skip the first element.
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
    if len(responseTimes) == 0 or len(responseTimes) == 1:
        return 0
    prev_list = [responseTimes[0]]
    for i in range(1,len(responseTimes)):
        list_sum = 0
        for j in prev_list:
            list_sum += j
        list_avg = list_sum/i
        if responseTimes[i] > list_avg:
            res += 1
        prev_list.append(responseTimes[i])
    return res

if __name__ == '__main__':
    responseTimes_count = int(input().strip())

    responseTimes = []

    for _ in range(responseTimes_count):
        responseTimes_item = int(input().strip())
        responseTimes.append(responseTimes_item)

    result = countResponseTimeRegressions(responseTimes)

    print(result)
