# ──────────────────────────────────────────────────
# Problem     Two Sum
# Difficulty  Easy
# Subdomain   Software Engineer Prep Kit
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-05-26, 01:05 p.m.
# Technique   hash-map-lookup
# Time        O(n)
# Space       O(n)
# Trick       Store seen values in a dictionary to achieve O(1) lookup for the complement, trading memory for linear time complexity.
# Hint        Use dictionary.get() or 'in' operator for O(1) average lookups.
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
    dictionary = {}
    for i in range(len(taskDurations)):
        diff = slotLength - taskDurations[i]
        if diff in dictionary:
            return [dictionary[diff], i]
        dictionary[taskDurations[i]] = i
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
