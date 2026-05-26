# ──────────────────────────────────────────────────
# Problem     Two Sum
# Difficulty  Easy
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-05-25, 10:19 p.m.
# Technique   hash-map-lookup
# Time        O(n)
# Space       O(n)
# Trick       Store seen values in a dictionary to achieve O(1) lookup for the complement, trading memory for linear time complexity.
# Hint        Use a dictionary for O(1) average time complexity lookups.
# ──────────────────────────────────────────────────

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findTaskPairForSlot' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY taskDurations
#  2. INTEGER slotLength
#

def findTaskPairForSlot(taskDurations, slotLength):
    # Write your code here
    hash_map = {}
    for i in range(len(taskDurations)):
        diff = slotLength - taskDurations[i]
        if diff in hash_map:
            return [hash_map[diff],i]
        hash_map[taskDurations[i]] = i
    return [-1,-1]

if __name__ == '__main__':
    taskDurations_count = int(input().strip())

    taskDurations = []

    for _ in range(taskDurations_count):
        taskDurations_item = int(input().strip())
        taskDurations.append(taskDurations_item)

    slotLength = int(input().strip())

    result = findTaskPairForSlot(taskDurations, slotLength)

    print('\n'.join(map(str, result)))
