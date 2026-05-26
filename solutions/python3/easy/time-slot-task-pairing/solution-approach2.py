# ──────────────────────────────────────────────────
# Problem     Two Sum
# Difficulty  Easy
# Subdomain   Software Engineer Prep Kit
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-05-26, 02:02 p.m.
# Technique   hash-map-lookup
# Time        O(n)
# Space       O(n)
# Trick       Store values in a dictionary to check for the complement (slotLength - val) in constant time during a single pass.
# Hint        Use a dictionary for O(1) average lookup time.
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
    seen = {}
    for i, val in enumerate(taskDurations):
        if slotLength - val in seen:
            return [seen[slotLength - val], i]
        seen[val] = i
    return [-1, -1]

if __name__ == '__main__':
    taskDurations_count = int(input().strip())

    taskDurations = []

    for _ in range(taskDurations_count):
        taskDurations_item = int(input().strip())
        taskDurations.append(taskDurations_item)

    slotLength = int(input().strip())

    result = findTaskPairForSlot(taskDurations, slotLength)

    print('\n'.join(map(str, result)))
