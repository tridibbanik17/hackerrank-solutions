# ──────────────────────────────────────────────────
# Problem     Count Elements Greater Than Previous Average
# Difficulty  Easy
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-05-25, 04:55 p.m.
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